# Stage 1 · Prompt 9 — Integrated Design Synthesis and Readiness Audit

**Report:** v1.1 · 2026-10-23 (v1.0 delivered, then corrected and re-verified the same day) · author: Prompt 9 session
**Status:** Final for review — **synthesis complete and corrected; Stage 1 not complete**
**Readiness verdict:** **Conditionally ready** (research complete; design conditionally ready; architecture, implementation, and public launch not ready)
**Zero-cost verdict:** **Conditional** — a coherent ₹0 required-cost plan is plausible for the first playable version and a small private playtest; conditional at a limited public launch; **not verified** for a growth scenario
**Scope:** research, synthesis, audit, and documentation only. No production code, no game mechanics implemented, no final technical architecture selected.
**Preconditions verified this session:** all four continuity files read; all eight Stage 1 reports inspected, with Prompts 7 and 8 read end-to-end in the 2026-10-23 correction pass (§2.1); the current [DECISIONS.md](../DECISIONS.md) read (D-001…D-006; D-004 and D-005 still **Provisional**); official free-tier pages re-read on 2026-10-23 (§17.3).

---

## How to read this report

Every material statement carries one of the labels below. The labels are not decoration: they are the audit's main defence against the failure mode where a recommendation is later remembered as an approval.

| Label | Meaning |
|---|---|
| **Verified project fact** | Directly checked in the saved repository or in current official documentation on the date cited. |
| **Research finding** | An evidence-backed observation inherited from Prompts 1–8, cited to its report and IDs. |
| **Consolidated proposal** | A synthesis of proposals already recorded in Prompts 5–8. Still unapproved. |
| **Recommended requirement** | This report's recommendation for a requirement or scope boundary. **Unapproved** until the owner records it. |
| **Assumption** | A planning assumption, explicitly not measured. Labeled where used, especially in §17's capacity model. |
| **Open question** | Unresolved, with an owning register entry (§15). |
| **Owner decision** | Requires the owner's explicit choice; none is made for them here. |
| **Executed test** | Actually run and evidenced. This report contains **none** of the game tests; all ST/V/CV/ECV/PV tests are unexecuted. |
| **Planned test** | Designed but not run. |

Two abbreviations are used throughout: **FPB** = first playable build (a real multiplayer build with accounts, authoritative state, and the Stage-A security baseline); **CP** = concept prototype (Prompt 5 §15's validation artifact). The distinction is itself a finding — Prompts 5–8 use "first playable" for both, which is defect DEF-001 (§14).

---

## Table of contents

- [Section 1 — Executive summary and readiness verdict](#section-1--executive-summary-and-readiness-verdict)
- [Section 2 — Stage 1 report inventory and audit status](#section-2--stage-1-report-inventory-and-audit-status)
- [Section 3 — Consolidated game identity](#section-3--consolidated-game-identity)
- [Section 4 — Consolidated player experience and game loop](#section-4--consolidated-player-experience-and-game-loop)
- [Section 5 — Canonical system catalog](#section-5--canonical-system-catalog)
- [Section 6 — Cross-system dependencies and interaction map](#section-6--cross-system-dependencies-and-interaction-map)
- [Section 7 — Canonical two-hour turn model](#section-7--canonical-two-hour-turn-model)
- [Section 8 — Consolidated economy design](#section-8--consolidated-economy-design)
- [Section 9 — Politics, diplomacy, alliances, and strategic conflict](#section-9--politics-diplomacy-alliances-and-strategic-conflict)
- [Section 10 — Security, privacy, fair play, and reliability baseline](#section-10--security-privacy-fair-play-and-reliability-baseline)
- [Section 11 — First-playable scope and deferred features](#section-11--first-playable-scope-and-deferred-features)
- [Section 12 — Requirements traceability matrix](#section-12--requirements-traceability-matrix)
- [Section 13 — Acceptance criteria and validation plan](#section-13--acceptance-criteria-and-validation-plan)
- [Section 14 — Contradictions, ambiguities, and design gaps](#section-14--contradictions-ambiguities-and-design-gaps)
- [Section 15 — Consolidated open questions and owner decisions](#section-15--consolidated-open-questions-and-owner-decisions)
- [Section 16 — Identifier and register reconciliation](#section-16--identifier-and-register-reconciliation)
- [Section 17 — Zero-cost operating requirement and free-tier feasibility](#section-17--zero-cost-operating-requirement-and-free-tier-feasibility)
- [Section 18 — Cost, operations, and future technical-planning dependencies](#section-18--cost-operations-and-future-technical-planning-dependencies)
- [Section 19 — Recommended next stages](#section-19--recommended-next-stages)
- [Section 20 — Stage 1 readiness gates](#section-20--stage-1-readiness-gates)
- [Section 21 — Final recommendations](#section-21--final-recommendations)
- [Section 22 — Quality assurance record](#section-22--quality-assurance-record)
- [Section 23 — Handoff and continuity file updates](#section-23--handoff-and-continuity-file-updates)
- [Appendix A — Source register](#appendix-a--source-register)
- [Appendix B — New identifier families introduced by this report](#appendix-b--new-identifier-families-introduced-by-this-report)
- [Appendix C — Change log for this pass](#appendix-c--change-log-for-this-pass)

---

## Section 1 — Executive summary and readiness verdict

### 1.1 The one-paragraph answer

The eight Stage 1 reports form a coherent, unusually well-instrumented research base for one game: a persistent, mapless, browser-based nation-strategy game on a shared two-hour UTC turn, whose identity is a relationship network of nations rather than a map. The concept, the system map, the economic architecture, the turn-timing contract, and the security requirement set are individually strong and mutually referential. What does **not** exist is equally clear: no numeric balance, no war rules, no complete turn-ordering catalog, no executed validation or security test, no architecture, no measured free-tier capacity, and no single agreed boundary for the first playable artifact. The research supports proceeding to a **bounded next stage**, not to implementation. **Stage 1 is therefore not complete**, and the honest verdict is **conditionally ready**.

### 1.2 Readiness by dimension (not interchangeable)

| Dimension | Verdict | Evidence | What is missing |
|---|---|---|---|
| **Stage 1 research completion** | **Conditional** | All eight reports exist and are readable; each carries a status and QA record; P7's final micro-correction and P8's 2026-10-23 correction passes are present in the saved files (§2.2) | Three gates remain conditional after the 2026-10-23 correction pass (§20): bypassed validation, capacity evidence, and the zero-cost capacity claim. GATE-03 now passes with recorded accepted conditions |
| **Design readiness** | **Conditional** | Concept CX-5, six pillars, 18 systems, 14 interactions, five-line economy, directed-trade model, TH/SEC registers are integrated (§§3–10) | Numeric balance, war rules, complete ordering, first-playable boundary; DEF-001/002 |
| **Technical architecture readiness** | **Not ready** | SDQ-003/018 explicitly deferred to an architecture stage; D-005 provisional; no schema, runtime model, or measured workload | Schema, authority boundaries, batch strategy, cron-CPU measurement, migration/export design |
| **Zero-cost feasibility** | **Conditional** | Component matrix (§17.10); official limits re-verified 2026-10-23 | Measured cron CPU/subrequests, D1 write amplification, storage growth, e-mail throughput, R2 activation terms |
| **Implementation readiness** | **Not ready** | No code; no numbers; no architecture; V/CV/ECV all unexecuted | Everything in the two rows above |
| **Public-launch readiness** | **Not ready** | Launch-stage security (B1–B6) and moderation/backups unbuilt; no restore drill; no real-player test | Account stack, abuse tuning, restore drill, monitoring rail, moderation capacity |

These are deliberately separated. A reader who takes only one sentence from this report should take this one: **research completeness is not design readiness, and design readiness is not launch readiness.**

### 1.3 What the integration establishes

1. **The identity is stable across reports.** CX-5 "The Community of Nations" (P5 §6, DIR-1) is consistently expressed as DP-001…DP-006, and the system catalog maps every pillar to machinery (P6 §24H). No report proposes a competing concept.
2. **The economy is architecturally coherent, numerically empty.** One treasury, no debt, five development lines, four material classes, directed fee-free trades first, a listings market gated behind G-1…G-6, and a four-category money-supply identity (P7 §§6–12). Every number is deliberately absent, and the report says so.
3. **The turn contract is the project's real spine.** Three timing classes (immediate / queued / at-boundary), boundary-only resolution, server-authoritative affordability, and an exactly-once resolution requirement (P6 §17; P7 §14; P8 SEC-018…021). The *ordering* of phases is not fully specified (SDQ-018) — a known, correctly labeled gap.
4. **Security is requirement-rich and implementation-empty.** 25 threats, 32 defined requirements, 20 designed tests, 12 owner questions, and 18 abuse walkthroughs (P8). Zero tests executed. The two staging inconsistencies found here (DEF-004/005) were corrected in the 2026-10-23 correction pass; the staging now reads 12 stage-A requirements plus the SEC-031 spine subset, and 12/11/9 = 32.
5. **The zero-cost objective was never operationalized across the whole stack.** Prompts 1 and 7 checked database and Workers limits; Prompt 8 checked security's marginal cost. None checked frontend hosting, authentication, e-mail, monitoring, backups, source control, or domain/TLS as one budget, and none measured a turn. §17 does that here, with verdicts and access dates.

### 1.4 The five findings that matter most

| # | Finding | Severity | Where tracked |
|---|---|---|---|
| 1 | "First playable" names two incompatible artifacts: P5's concept test explicitly excludes authentication and integrity work; P6/P7 require trade and P8 requires the Stage-A security baseline for any real-player build | High | DEF-001, DEF-002; OD-02 |
| 2 | Free-tier capacity is **unmeasured**: cron CPU at 10 ms, 50 subrequests per invocation, D1 write amplification from indexes and audit rows, and the 500 MB per-database cap are all plausible binding constraints | High (for the ₹0 claim) | DEF-006; §17.4–17.6; PV-01…PV-07 |
| 3 | P7's "~3,000 active nations at 100k writes/day" is materially optimistic once audit-spine rows, auth/session writes, rate-limit counters, and possible index amplification are counted; the planning range is ~1,100–2,000 | Medium | DEF-006; §8.8; §17.5 |
| 4 | Validation gates stated as pre-conditions (P4 V-2; P5 CV-001/002/004) were bypassed while Prompts 5–8 proceeded | Medium | DEF-003 |
| 5 | **Corrected 2026-10-23.** P8's staging record had a stray count and an unstated subset: §15.4 said "16 requirements on stage A" while the stage table and A-list named 12, and A8 added the SEC-031 spine subset that the stage table counted under Stage B. P8 now reads 12 + the SEC-031 spine subset, and TH-011's residual is explicit | Medium (closed) | DEF-004, DEF-005, DEF-010 — **Fixed** |

### 1.5 The zero-cost conclusion in brief

A **₹0 required monthly cost** stack is credible for the FPB and a small private playtest under one provider (Cloudflare Workers + D1 + static assets), with authentication implemented in-Worker (Better Auth-class), monitoring on free tiers, and no paid dependency. It is **conditional** at a limited public launch because three numbers are unmeasured: (a) boundary CPU and subrequests at realistic nation counts, (b) actual D1 row-writes per action after indexes and audit rows, and (c) audit/transaction storage growth against the 500 MB database cap. It is **not** supported for a growth scenario of roughly 2,000+ daily active players under the assumed request and write profiles. No paid service is required by this plan, and no paid service is silently assumed.

### 1.6 What can safely begin next

Only two things:

1. **Owner decision closure** on the twelve decisions in §15 (first three: artifact taxonomy, quota-exhaustion policy, trade-at-FPB confirmation).
2. **A free-tier measurement spike** that runs the turn pipeline's *shape* against the real provider on a synthetic dataset (PV-01…PV-06), because it can invalidate or confirm the zero-cost plan before any architecture is committed.

Nothing else — no schema, no framework choice, no production code — should begin before those two produce recorded outcomes.

---

## Section 2 — Stage 1 report inventory and audit status

### 2.1 Source inventory and actual reading depth

| # | Report | Path | Lines | Read this session |
|---|---|---|---|---|
| 1 | Competitor research and genre analysis | [01_competitor_research.md](01_competitor_research.md) | 624 | End-to-end |
| 2 | Strengths, weaknesses, frustrations, opportunities | [02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) | 511 | End-to-end |
| 3 | Feature comparison and opportunity analysis | [03_feature_comparison_opportunity_analysis.md](03_feature_comparison_opportunity_analysis.md) | 691 | End-to-end (plus its registers and §7.7's identifiers) |
| 4 | Target audience and player experience | [04_target_audience_and_player_experience.md](04_target_audience_and_player_experience.md) | 599 | End-to-end in prior sessions; this session re-read the journey, validation and handoff sections |
| 5 | Core game concept and design pillars | [05_core_game_concept_and_design_pillars.md](05_core_game_concept_and_design_pillars.md) | 860 | End-to-end |
| 6 | Core gameplay systems and interactions | [06_core_gameplay_systems_and_interactions.md](06_core_gameplay_systems_and_interactions.md) | 771 | End-to-end |
| 7 | Economy design and market structure | [07_economy_design_and_market_structure.md](07_economy_design_and_market_structure.md) | 1,563 | **End-to-end across the 2026-10-23 correction passes** (§§0–27: read in sequential windows, including §17's worked examples, §22's registers, §26's QA record and §27's handoff), then re-read around the corrected passages |
| 8 | Security, privacy, fair play, trust | [08_security_privacy_fair_play_and_trust.md](08_security_privacy_fair_play_and_trust.md) | 1,555 | **End-to-end in the 2026-10-23 correction passes** (§§0–26, including all 18 walkthroughs and all five register collections), plus the targeted DEF-004/005/010 verification after the edits |

**Honesty note (updated 2026-10-23):** **Reports 7 and 8 were read end-to-end across the correction passes**, closing the gap disclosed in the first edition. Prompt 8's full read came first; Prompt 7's was completed in the final acceptance pass, where the full read is what surfaced DEF-016/017/018 (P7 timing wording, a reserve-interest label, and the offer-reservation conflict) that the earlier section-level pass had missed. Reports 1–6 were read end-to-end in their original passes, with Prompt 4's journey/validation/handoff re-read here. The correction pass also re-verified Prompt 7's accepted final micro-correction (the "Prompt 4, Section 9, item 8 — 'Missing several turns'" fix, made in the v1.1 era and still present in v1.2) and found it intact.

### 2.2 Inventory and audit status

| # | Prompt | Purpose | Recorded status | QA status (saved files) | Key dependencies | Open issues | Acceptable for synthesis? | Targeted correction needed? |
|---|---|---|---|---|---|---|---|---|
| 1 | Competitor research | Genre evidence + platform limits | Complete | Reviewed by P2; source limits disclosed | — | Provider figures now partly stale (cron 50 ms recorded; current 10 ms) | Yes | No (P7 §16.4 already records the discrepancy; historical text preserved) |
| 2 | Strengths/weaknesses | Player-experience evidence | Complete | Six artifacts fixed | P1 | F-007/F-028 absent while range claims F-029; F-029 unverified watchlist | Yes | No (DEF-008 recorded) |
| 3 | Feature comparison | Opportunity register FO | Complete | Two scans; correction pass; now one targeted edit (DEF-007) | P1–P2 | Undefined O-15/16/17 in §7.7; F-register gap inherited | Yes | **Yes — applied 2026-10-23** (identifier fix only) |
| 4 | Audience/experience | Personas, journey, V plan | Complete | Two structural passes; 10 artifacts fixed; V-3 cite corrected | P1–P3 | V-2 (P0) never executed; PXO-007's first-week thresholds unset | Yes | No |
| 5 | Concept/pillars | CX-5, DP/AP, CV plan | Complete | Correction pass (cadence, counts, V refs); clean scan | P1–P4 | First-playable boundary conflicts with P6/P7/P8 (DEF-001); CV-001/002/004 unexecuted | Yes, with condition | No |
| 6 | Systems/interactions | 18 systems, INT, SDQ, tiers | Complete (v1.1) | Correction + residual pass; registers verified | P1–P5 | Tier A omits SYS-005 while P5/P7 require trade (DEF-002); SDQ-018 open | Yes, with condition | No |
| 7 | Economy | Treasury, lines, materials, market, integrity, storage | Complete (v1.2 after 2026-10-23 targeted corrections; micro-correction verified) | Programmatic + manual recomputation; full re-read found DEF-016/017/018; two fixed, one preserved as an explicit ambiguity | P1–P6 | No numerics; write estimate omits amplification (DEF-006); offer reservation unresolved (DEF-018); SDQ-003 open | Yes | **Applied 2026-10-23** (DEF-016/017 fixed; DEF-018 recorded as open) |
| 8 | Security/trust | Threats, requirements, tests, OSQ, walkthroughs | Complete (v1.1; 2026-10-23 correction passes 1 and 2) | Rebuilt from corruption; sweeps passed; register maps regenerated; DEF-004/005/010 corrected and re-verified in pass 2 | P1–P7 | All ST unexecuted; no external review; auth-KDF CPU fit unmeasured (DEF-015) | Yes | **Applied 2026-10-23** (staging count, SEC-031 subset, TH-011 residual, handoff) |

**Prompt 7 micro-correction — verified present.** The saved economy report is v1.1 and contains the final micro-correction: both "Prompt 4 §9.8" citations now read "Prompt 4, Section 9, item 8 — 'Missing several turns'", and §26.2 records the issue as resolved. No live §9.8 citation remains.

**Prompt 8 correction passes — verified present.** The saved report is **v1.1**. Pass 1 contains §25.3's correction addendum (register maps regenerated from §2.3/§16.2/§19.2; §0.3's SEC range reconciled to "SEC-001…033 with SEC-009 reserved — 32 defined"), §25.6's QA-vs-production declaration, and §26.2's file-change record. **Pass 2 (2026-10-23, this audit's correction)** fixed §15.4's 16→12 count, stated the SEC-031 spine subset in A8/§16.2, separated TH-011's Stage-A prevention from SEC-015's refinement and recorded its accepted residual, marked §26.9's Prompt 9 handoff superseded, and added §25.7. All changes were re-read after saving; see §22.4/§23.2.

### 2.3 Defect handling policy for this synthesis

A defect is **blocking for synthesis** only if it prevents an accurate integrated description. None does. A defect is **blocking for Stage 1 acceptance** if it makes the stage's own completion criteria false. DEF-001/002 are blocking for *first-playable planning*, not for the synthesis. DEF-003 is recorded as a **condition of this audit** (the design was produced past its own gates; that does not invalidate the research, but it lowers confidence in unvalidated assumptions). This is the auditor's acceptance, **not the owner's approval**; the owner confirms or rejects the condition when deciding OD-02. **DEF-004/005/010 were corrected in Prompt 8 on 2026-10-23 and verified** (P8 §15.4, §16.2, §17.1 A8, TH-011, §22.2 item 6, §26.9); they are no longer accepted conditions. DEF-006 is a **correction to a planning estimate**, not a document error: the report's arithmetic is right for the cost model it states, and the model omits categories the report itself flags elsewhere. **The end-to-end re-read also found three P7 record defects (DEF-016/017/018) that the first edition missed.** DEF-016 (emphasis timing) and DEF-017 (reserve interest) were unambiguous contradictions of P7's own stated rules and were corrected in place on 2026-10-23; DEF-018 (whether a pending offer reserves funds) is a genuine design ambiguity, so it was **preserved as an explicit open conflict** rather than resolved by preference. P7's version header was corrected to 1.2 to match the edits.

### 2.4 The one targeted edit made by this pass

DEF-007 (P3 §7.7) cited `O-15`, `O-16`, `O-17` and `O-12` as if they were Prompt 2's opportunity register, which ends at O-12. The intended referents are Prompt 3's own feature-opportunity IDs: re-entry digest (FO-015), economic transparency (FO-016), anti-farming protection states (FO-017), shared campaign focus (FO-012), the politics-light + alliance-tooling package (FO-005/006/007/008), and in-context teaching (FO-001). The sentence was corrected in place to cite the FO IDs and to say they are registered in Section 10. No substantive claim, status, or register entry changed. This was the **only** edit to a Prompt 1–8 report in the original audit pass; the later correction pass separately edited Prompt 8 (DEF-004/005/010, documented in §22.4 and §23.2), and both edits are recorded in PROJECT_PROGRESS.

---

## Section 3 — Consolidated game identity

### 3.1 The concept, as the research actually states it

**Verified project fact:** Project X is a persistent, multiplayer, browser-based nation-strategy game on a fictional, mapless world that advances on one shared turn every two hours (12/day, UTC boundaries), with server-resolved production, upkeep, and recurring effects (AI_CONTEXT §1–2).

**Research finding (P5 §6, DIR-1; provisional):** the recommended concept is **CX-5 "The Community of Nations"** — the player is the steward of one developing nation inside a legible network of relationships, where economic specialization and diplomatic standing are the central paths, stability and research are supporting multipliers, military capability is optional-but-real and bounded, and cultural influence is deferred. Runner-up CX-3 "The Diplomatic Order" contributes its diplomatic surface to CX-5; CX-1 (economy-first), CX-2 (politics-first), and CX-4 (war-first) were rejected (P5 §16A, RC-2…RC-4).

**Central fantasy (P5 §5, DIR-2):** FX-A "steward of one nation in a community of nations", with two faces of one funnel — FX-A′ the builder and FX-A″ the strategist. They are not parallel games; the funnel is shared.

### 3.2 Pillars and anti-pillars

| ID | Pillar (provisional) | What it commits the design to | Where the machinery lives |
|---|---|---|---|
| DP-001 | Many legitimate paths | No single ladder; thresholds unlock options, not multipliers; no permanent lock-out; respecialization always purchasable | Development lines, standing registers, emphasis, ECON-017 |
| DP-002 | Decisions over presence | No mechanic requires attendance; queue-first; absence returns a digest, not dread | SYS-016 timing classes, MO-008 arc orders, PXO-002 |
| DP-003 | The relationship network is the world | Diplomacy, trade credit, reputation, treaties and chronicle constitute the "map" | SYS-008/009/013/015, INT-004 |
| DP-004 | The world explains itself | Every delta has provenance; forecasts labeled; failures have reasons | SYS-017 digest, P7 §15 finance contract |
| DP-005 | Interdependence is structural | Specialization creates real comparative advantage and two-route floors; trade is lucrative, not mandatory | SYS-004/005, ECON-011 |
| DP-006 | Conflict is bounded and coexists | War cannot erase economic continuity; effects are itemized and predeclared | SYS-011/012 (war stage), ECON-009 |

**Anti-pillars (P5 §14, AP-001…AP-008, provisional):** no activity incentives; no forced real-name identity; no hand-authored world events; no forced alliances; no pay-for-power; no jargon walls; no hidden punishments; no finance-progress screens. These are constraints on later design, not features.

### 3.3 Audiences and motivations

**Research finding (P4 §3–§6, proposed):** the primary audience is the *steady-check-in multiplayer strategist* (persona Mira; 1–3 sessions of 5–15 minutes per day), with organized-community players (Tomas) and diplomat players (Ade) secondary, and market optimizers (Yuna), competitors, and roleplayers (Kwame) as future audiences. Explicitly **not** primary: live-participation audiences, pay-power audiences, map-game audiences, and election-institution audiences (P4 §6; consistent with FO-023/025/026/027 rejections).

Four motivations carry the design: *compounding stewardship* (build something that persists), *legible standing* (be recognized through acts, not a grind), *consequential relationships* (other players change your options), and *bounded conflict* (tension without attendance pressure). These are synthesized from P4's persona work and P5's fantasy; they are not new research.

### 3.4 The value of a mapless world

**Research finding (P3 §7.7, FO-013; P5 §12):** the mapless network is not a limitation to apologize for; it is the differentiator. It removes the map's implicit "expand or die" pressure, makes relationships the primary spatial metaphor, keeps the data model small (no tiles, no pathfinding), and makes small worlds legible. **Assumption (unvalidated):** players will read a network of nations as a "world" without a map — CV-002, never executed.

### 3.5 Differentiators, with their evidence quality

| ID | Differentiator (P5 §13) | Evidence quality | Caveat |
|---|---|---|---|
| UXD-001 | A world that explains itself (provenance-first digest) | Strongest of the set; grounded in F-010/PXO-002 | Still unplaytested |
| UXD-002 | Relationship network as the world | Strong; FO-013 keystone | Comprehension unproven (CV-002) |
| UXD-003 | Structural interdependence without geography | Moderate; ECON-011 design-level | Numeric asymmetry unset (ECOQ-004) |
| UXD-004 | Settlement vocabulary for bounded conflict | **Weakest**; P5 flags it as such | War rules absent; do not market yet |
| UXD-005 | Adversarially designed fairness and recovery | Moderate; P8 posture | No executed test |

### 3.6 Rejected or deferred identity directions

Rejected at research level: elections/institution simulation (FO-025), pay-for-power and gacha (FO-026), real-world political mapping (FO-027), full espionage (FO-023), and a single mandatory progression ladder. Deferred: consumer/prestige goods as a fifth material class (ECON-023), contracts/escrow (FO-022), retail demand (FO-021), seasons/resets (FO-019), player-authored events (FO-020), and account meta-progression. These are recorded, not silently dropped.

### 3.7 Design principles later implementation must preserve

1. **Boundary-only resolution.** Nothing valuable resolves live between turns (P6 §17; P8 SEC-018…021).
2. **Server authority over every valuable quantity.** The browser is a display surface (P8 §5.1, SEC-010/011).
3. **No partial transfers, no debt, no interest.** (ECON-001; R-19.)
4. **Every failure has a reason and a release of reserved funds** (P7 §14/§15; P8 fail-with-reason).
5. **Thresholds unlock tools, never participation floors** (P7 §7.4).
6. **No mechanic requires attendance; catch-up is a decision, not a gift** (DP-002; FO-018 open).
7. **Nothing valuable is deleted without disclosure; player-visible history is append-only** (P8 §14.4/§14.5).
8. **No paid dependency is required for core operation** (owner constraint, §17.1).

### 3.8 What this section does not establish

No final name, slogan, brand, or public-facing copy exists. "Project X" and "crowns" are placeholders (P7 §6.1 explicitly says naming belongs to a later stage). No marketing claim should be derived from UXD-004 or from any unexecuted validation.

---

## Section 4 — Consolidated player experience and game loop

### 4.1 The loop the research actually supports

Prompt 6 §4A defines a six-step decision loop that all later reports assume: **observe the world → form an intent → commit an order (or hold) → the boundary resolves → read the digest → interpret and revise**. The same loop serves a two-minute session and a two-week absence; only the number of executed decisions changes (P6 §24D). Four nested loops sit inside it: the turn loop, the arc loop (multi-turn queued plans, MO-008), the relationship loop (offers, treaties, standings), and the re-entry loop (weeks away). One chronological journal backs all four (SIM-006), which is why the digest is a *system* (SYS-017), not a screen.

**What makes the loop work as a game rather than a spreadsheet:** every step has a decision with a visible trade-off, and no step requires presence. The research calls this DP-002 and treats it as non-negotiable. **What is not yet specified:** the content of the first decision, the exact order of surface reveal, and the thresholds at which the first week is judged successful (PXO-007).

### 4.2 First entry and nation creation

**Designed direction (P4 §8–§9; P5 §15A E1; P6 SYS-018):** a short, honest landing page states the cadence and the absence model before sign-up (PXO-001); account creation is minimal (username, e-mail, password — P8 §4.1); nation creation asks for a name and a small number of identity choices, then presents *one real decision* rather than a tutorial dump (PXO-004). The intended first-session arc is: nation card → one allocation decision → the promise of a digest at the next boundary.

**What is specified:** the security posture of registration (unique identity, e-mail as recovery anchor, no real-name requirement — SEC-001/004; AP-002); the existence of a starting grant and starter line levels (P7 §6.2/§6.4); the teaching obligations (FO-001, PXO-004).

**What is not specified:** how many identity choices are irreversible; whether nation creation includes a map-free "neighbourhood" or starting-relationship seed; the starting grant's size (ECOQ-003); the exact first decision; what happens if a player abandons creation midway. These are content-design gaps, not contradictions. **Assumption:** the first session can be completed in under ten minutes without external documentation. **Plausible on paper, unvalidated (CV-001/CV-002).**

### 4.3 Onboarding and early progression

**Designed direction:** progressive surface reveal — nation card, then standing register, then market, then chronicle (P5 §12A-9); glossary-in-place rather than a manual (FO-001, PXO-005); a first-week ladder with meaningful but bounded early thresholds (P4 §8; PXO-007).

**The unresolved tension:** the genre's documented churn is concentrated in the first week (F-010/F-011), and the research's answer is *teaching*, not protection. But the protected newcomer state itself is undefined: FO-003 (new-player protection + guided first-turn sequence) is a *candidate*, and P8 SEC-023's fresh-account restrictions are an integrity control, not a tutorial. The design currently asks a new player to make real decisions while the game is still teaching its vocabulary. That is coherent but risky; **CV-001 (resonance) and CV-002 (mapless comprehension) are the tests that would settle it, and neither has run.**

### 4.4 The national command experience

**Designed direction (P7 §15; P6 SYS-001/002/003/017):** the nation card is the home surface: available versus committed treasury, material stocks, line levels and emphasis, pending orders, the projected next boundary, and a hazard list (partner default, embargo, campaign costs later). The finance view is explicitly not a spreadsheet: six number types, four surfaces, every forecast labeled (P7 §15).

**What a session looks like on paper:** read the digest's exceptions, adjust emphasis or queue one investment, answer a trade offer or a treaty note, close the tab. The research's target is 1–3 sessions of 5–15 minutes per day (P4 §6), which the loop supports because the boundary does the work.

### 4.5 Treasury, development, specialization

**Designed direction (ECON-001/002/006/017):** one pool, no debt, no interest; five lines (PRO, COM, ADM, WRK, RDY); four materials (Sustenance, Construction, Industrial, Ordnance); emphasis weights express identity; levels express strength; upkeep scales with levels; respecialization is paid, one-per-turn, boundary-effective, distance-gated, and carries a bounded retooling dip.

**The player-facing promise:** surplus is a decision (invest, reserve, trade, contribute), never a passive score. **The player-facing risk:** the same promise becomes chore-like if upkeep is opaque (F-019); the design's answer is boundary-automatic resolution plus digest provenance. **Numeric balance does not exist** — ECOQ-002 (drain curves and austerity thresholds) and ECOQ-004 (asymmetry and respec numerics) are the two most consequential open families (P7 §22.3).

### 4.6 Trading and economic interaction

**Designed direction (ECON-013; SYS-005):** directed bilateral offers with accept/decline/counter, atomic settlement, fee-free at first playable, no escrow, no order book, no contracts. Offers persist offline; declining is socially cheap; completed trades build a trade-credit record (INT-004). A public listings market is *not* part of the FPB; it gates in only on G-1…G-6 (identity integrity, write budget, observed liquidity, reference-price design, fee policy, ops capacity).

**Why this matters for the journey:** the first trade is a conversation, not a price screen. That is the concept's identity (DP-003/DP-005) and its main defence against the genre's market-abuse surface. **Unresolved:** public visibility of completed terms (SDQ-004), fresh-account trade caps (SEC-023's parameters), and the exact counteroffer UX.

### 4.7 Domestic politics and internal stability

**Designed direction (SYS-006; FO-005; P5 DIR-3):** a light layer of one or two togglable policy axes with cooldowns; stability as a state that multiplies or taxes other paths, never a success ladder of its own. Exact axes are SDQ-005. P6 explicitly labels the layer "essential-not-dominant" and a cut candidate if playtests show it feels arbitrary.

**The gap:** no report defines what stability *does* numerically, how policy changes are explained, or how a player recovers from a stability shock. The *shape* is coherent; the *experience* is un specified beyond "light". Section 4.7 of this report therefore describes a lever, not a politics game. That is an honest limitation, not a design failure: the research deliberately kept politics supporting.

### 4.8 Diplomacy and relationships

**Designed direction (SYS-008/009/013):** typed, inspectable bilateral records; a minimal treaty set — a non-aggression analogue that is mechanically enforced, plus promise records that are reputation-bearing but not enforced (matching the verified P&W pattern that only NAPs are mechanically enforced); reputation by acts across several named registers, not one score; a public chronicle of notable acts.

**The player experience intended:** "where do I stand, what have I promised, what have others done" is answerable from the world view without a map. **The gap:** relationship states and treaty types are named but not enumerated; SDQ-014 owns the state machine; SDQ-004 owns visibility. The journey is describable at the level of *verbs* (offer, accept, exit, denounce, assist) but not yet at the level of *rules*.

### 4.9 Alliance membership and governance

**Designed direction (SYS-010; FO-007/008):** minimal v1 alliance object — name, bank view, one contribution bracket, role-lite permissions, audit-first records; collective actions later; never mandatory (AP-004).

**The player experience intended:** joining is a real commitment with a shared pool and a visible record, not a chat tag. **The gap:** the permission matrix (SDQ-012) and succession/defunct-alliance rules (SDQ-013) are open; without them, an alliance bank is a liability. P6 stages alliances at Tier C, so the FPB may have *no* alliance system at all — but P5's concept test includes a "partnership object", and P8's TH-021 treats alliance administration as a real threat class. The scope boundary is unresolved (DEF-002/OD-02).

### 4.10 Strategic conflict without a map

**Designed direction (P5 §11; SYS-011/012; FO-010/011/017):** bounded, declared campaigns over non-geographic objectives (market access, pairing claims, reputational challenges, protective operations); a small action set; resolution at boundaries; a settlement stage with a declared vocabulary; itemized, bounded effects. No live windows, no conquest, no game-over.

**What exists:** the concept, the objective classes, the settlement premise, the readiness line, and the OP question (D-004, Provisional). **What does not exist:** any campaign rule, any combat math, any cooldown table, any peace/surrender procedure. The report says this plainly (P6 §15; P8 TH-022 is "war-stage-dependent"). **The journey therefore stops at "conflict is bounded" — there is no playable war journey to describe, and this synthesis will not invent one.**

### 4.11 Shared turn boundaries and resolution feedback

**Designed direction (SYS-016/017; P7 §14):** every action is classified immediate-with-record, queued-until-boundary, or boundary-scheduled. The boundary resolves committed orders in a deterministic catalog order (SDQ-018, open); failures release reservations and explain themselves; the digest reports every delta with provenance; the chronicle records notable events. The player never needs to be online at the boundary.

### 4.12 Returning after absence

**Designed direction (FO-015; P4 Section 9 item 8; SYS-017):** a re-entry summary answers four questions in order — what happened, what changed for me, what needs a decision now, what can wait. Absence carries no decay of identity and no forced catch-up mechanic (ECON-012's constraints; FO-018 remains owner-held).

**What is unresolved:** how much history the summary retains (SDQ-003/SDQ-017), how a long absence interacts with alliance membership and treaties, and whether an inactive nation can be a reliable supplier (P7 R-21 flags the recipient-of-absence manipulation).

### 4.13 Long-term goals and progression

**Designed direction (P6 §19/§24E):** development levels → option-class unlocks → standing-register movement → chronicle record → treaty-web centrality; later, program completions and campaign history. Multiple registers rather than one ladder (MO-007); respecialization keeps the topology open. No account meta-progression, no seasons/resets at launch (FO-019 deferred).

**The honest limitation:** "long-term" here means *weeks to months of persistent play*, and no simulation or playtest has shown that the option-unlock curve remains interesting past the first arc. CV-003 (multi-path perception) and CV-005 (retention?) are unexecuted. The design has a *shape* for long-term play, not evidence of it.

### 4.14 Recovery from failed or delayed operations

**Designed direction (ECON-009; P8 §14):** no bankruptcy death; austerity floors reduce volatility; reserved funds release with reasons; a delayed turn is announced, not silently skipped; restore-based corrections are disclosed as new events, never by rewriting history. Server-caused damage is compensated from evidence; player-caused loss is not, and that rule is public.

**The gap:** the *player-facing* recovery UX (how a failed order is explained, what a "delayed turn" banner says, how compensation is claimed) is described in principles, not in screens or copy.

### 4.15 Where the journey is not yet specified

| Journey stage | What exists | What is missing | Consequence |
|---|---|---|---|
| Landing → account | Honesty direction, security posture | Copy, consent, verification decision | Copy can be written later; verification affects free-tier budget (§17) |
| Nation creation | One-real-decision direction, starting grant existence | Irreversible-choice count, seed relationships, grant size | Blocks onboarding build |
| First week | Teaching direction, PXO-007 ladder concept | Thresholds, protection state, success metric | Blocks CV-001/002 test design |
| Routine command | Finance view, digest, pending orders | Screen inventory, mobile layout, notification policy | Blocks UI design, not architecture |
| Trade | Directed model fully specified at rule level | Fresh-account caps, visibility policy, counteroffer UX | Blocks trade build details |
| Politics | One/two axes, stability multiplier | Axes, effects, recovery | Can ship minimal or cut |
| Diplomacy | Verbs and typed records | State machine (SDQ-014), visibility (SDQ-004) | Blocks treaty build |
| Alliances | Minimal object, audit posture | Permissions (SDQ-012), succession (SDQ-013) | Blocks alliance build |
| Conflict | Concept, objectives, settlement premise | All rules | Blocks war entirely |
| Absence | Re-entry summary direction | Retention, alliance/treaty interaction | Blocks re-entry build |
| Recovery | Floors, disclosure, compensation posture | UX, claim flow, thresholds | Blocks ops runbook |

**Conclusion:** the journey is coherent as an *architecture of experience* and incomplete as a *script*. That is appropriate for a research stage and must not be presented to players or investors as a finished game loop.

---

## Section 5 — Canonical system catalog

### 5.1 Reading the catalog

The 18 systems below are the ones actually named in Prompt 6 §5.1. **No new SYS IDs are introduced.** The catalog is reproduced with the fields this synthesis needs; where Prompt 6's name differs slightly from Prompt 7's shorthand (SYS-003 is "Production & Development Capacity" in P6 and "Production, upkeep & development" in P7), the P6 name is canonical and the variant is noted once.

Classification legend: **FP** = recommended for the first playable build; **FP-min** = minimal form only; **Pre-launch** = required before public launch, not before a private FPB; **Later** = staged after launch or after a dedicated design stage; **Undecided** = the research does not settle it. These are **this report's recommendations**, not approvals.

### 5.2 Catalog table

| ID | System | Purpose | State it owns | Connects / interfaces | Source | Design status | FP class |
|---|---|---|---|---|---|---|---|
| SYS-001 | Nation Profile & Identity | Persistent persona, self-declared direction, standing snapshots | Name, profile, emphasis weights, chronicle links | All systems read the nation ID and emphasis; writes to SYS-002/003/004/007 | P6 §5.1; P5 FX-A | Defined at shape level | **FP** |
| SYS-002 | Treasury & Finances | Single currency pool, commitments, solvency, finance view | Balance, reservations, transfer records | INT-001/002 with SYS-003; SYS-005 trade; SYS-010 pool | ECON-001; P7 §6 | Rule-level defined; numbers open | **FP** |
| SYS-003 | Production & Development Capacity | Per-turn output, drains, line levels, investment execution | Line levels, emphasis effect, material stocks, upkeep | Reads SYS-002 funds; reports to SYS-002; feeds SYS-004/005 | ECON-002/006; P7 §§7–9 | Rule-level defined; numbers open | **FP** |
| SYS-004 | Structural Scarcity & Specialization | Efficiency asymmetry, capability gaps, two-route floors | Gap/surplus classes, dependency map | SYS-003 output; SYS-005 trade; SYS-008 relationships | ECON-011; SDQ-009 | Structure defined; asymmetry unset | **FP** |
| SYS-005 | Trade & Exchange | Directed offers, atomic settlement, trade credit; market later | Offers, reservations, completed trade records | SYS-002/004/008; SYS-016 boundary | ECON-013; P7 §10 | Directed model specified; market gated | **FP** (directed only) |
| SYS-006 | Domestic Policy & Stability | One/two policy axes, cooldowns, stability as multiplier | Lever states, stability state, policy history | SYS-002 cost; SYS-003 efficiency; SYS-015 chronicle | FO-005; SDQ-005 | Shape only; axes open | **FP-min** (may be cut) |
| SYS-007 | Research & Capability Programs | Slow convertibility into option classes | Program progress, unlocks | SYS-002/003; SYS-008 sharing | P6 §11 | Tier C; may ship zero programs | **Later** |
| SYS-008 | Bilateral Relationships | Typed pair states with visible histories | Pair state, event-sourced history | SYS-009 gates; SYS-012 posture; SYS-013 | FO-004; SDQ-004 | Data layer defined; visibility open | **FP** |
| SYS-009 | Treaties & Agreements | Minimal NAP analogue + promise records | Treaty objects, states, exits | SYS-008/013 | FO-006; SDQ-014 | Minimal shape; types open | **FP-min** |
| SYS-010 | Alliances & Collective Administration | Membership, roles, pool, audit-first records | Alliance object, roles, pool, audit rows | SYS-002/005/009/012 | FO-007/008; SDQ-012/013 | Minimal shape; permissions open | **Pre-launch** (minimal), later full |
| SYS-011 | Military Capability & Readiness | Readiness upkeep, posture, deterrence signal | Readiness level, posture | SYS-002/003; SYS-012 | FO-010; D-004 | Minimal face only | **Later** (or scripted vignette) |
| SYS-012 | Strategic Campaigns & Settlements | Bounded campaigns, objectives, settlement | Campaign objects, outcomes, settlement terms | SYS-008/009/011/013/015 | FO-011/017 | Concept only; no rules | **Later** (war stage) |
| SYS-013 | Reputation & International Standing | Acts-driven standing across named registers | Standing registers, act records | SYS-008/009/012/015 | MO-007; P5 DIR-3 | Shape defined; act taxonomy open | **FP** |
| SYS-014 | Rankings, Objectives & Achievements | Comparative visibility per register | Public views, milestones | SYS-013/015 | SIM-007 | Optional | **Later** |
| SYS-015 | World Chronicle & News | Shared memory of notable events | Chronicle entries | SYS-016/017 | AP-003; SDQ-017 | Shape defined; taxonomy open | **FP** |
| SYS-016 | Turn Engine & World Clock | 2h cadence, three timing classes, deterministic resolution | Turn ledger, queues, phase checkpoints | Every system | P6 §17; P8 SEC-018…021 | Contract defined; ordering open | **FP** |
| SYS-017 | Turn Digest, Re-entry & Explanation | Provenance, digest, re-entry, in-context help | Rendered views from journal | SYS-016/015; all outputs | FO-001/002/015; SDQ-017 | Shape defined; taxonomy open | **FP** |
| SYS-018 | Onboarding & First-Decision | Guided-but-real entry, progressive reveal | First-decision state, reveal state | SYS-001/003/017 | PXO-004; FO-001 | Shape only; content absent | **FP** |

### 5.3 Per-system security and cost annotations

| ID | Critical assets | Core protection requirements (inherited) | Write profile (planning assumption) | ₹0 sensitivity |
|---|---|---|---|---|
| SYS-001 | Identity, emphasis | SEC-001/003/012; display only for public fields | 1 row on creation; edits rare | Low |
| SYS-002 | Currency, commitments | SEC-010/011/012/014/016/025/031; R-19 | 1 balance update + 1 ledger row per mutation; 12 summary rows/nation/day | **High** (writes + audit) |
| SYS-003 | Line levels, stocks | SEC-010/011/013/016/025; no-negative invariant | 1 update per line per boundary; material writes | **High** (boundary writes) |
| SYS-004 | Gap/surplus map | SEC-010; informational | Derived, few writes | Low |
| SYS-005 | Offers, transfers | SEC-012/014/016/019; atomic pair | 4 writes per completed trade nominal, more with indexes/audit | **High** |
| SYS-006 | Lever/stability state | SEC-010/012 | 1 write per change; 1 per boundary | Low |
| SYS-007 | Program progress | SEC-010/016 | 1 write per program per boundary | Low |
| SYS-008 | Pair state | SEC-012; visibility policy | 1-2 writes per relationship event | Medium |
| SYS-009 | Treaty objects | SEC-012/014; idempotent signing | 1-2 writes per state change | Medium |
| SYS-010 | Pool, roles | SEC-012/027; audit-first | 1 write per admin act + ledger row | Medium |
| SYS-011 | Readiness | SEC-010/013 | 1 write per boundary | Low |
| SYS-012 | Campaign state | SEC-012/019/020; war-stage rules | Unspecified (war stage) | Unknown |
| SYS-013 | Standing registers | SEC-010; act integrity | 1 write per act class | Medium |
| SYS-014 | Public views | Read-only | 0 | Low |
| SYS-015 | Chronicle | SEC-010; no free-form content | 1 row per notable event | Medium (storage) |
| SYS-016 | Turn ledger, queues | SEC-018/019/020/021; exclusive claim | Phase checkpoints + per-nation summaries | **Critical** (CPU + writes) |
| SYS-017 | Rendered digest | No private data leakage; per-user scoping | Reads only (derived) | Medium (reads) |
| SYS-018 | Onboarding state | SEC-012; first-decision integrity | 1-2 writes per new nation | Low |

### 5.4 Per-system inputs, outputs, and open questions

The catalog above is authoritative; this table adds the I/O and open-question fields the synthesis requires, without duplicating the SDQ/ECOQ entries.

| ID | Inputs → outputs | Open question (owner register) |
|---|---|---|
| SYS-001 | Player identity/emphasis choices → profile card, emphasis weights | How many irreversible creation choices? (OD-02) |
| SYS-002 | Income/upkeep results, orders, transfers → available/committed balance, ledger rows, finance view | Reservation display is specified; no open design question |
| SYS-003 | Investment orders, emphasis → output, stocks, line levels, upkeep | Drain curves (ECOQ-002); threshold placement (ECOQ-005) |
| SYS-004 | Line levels/emphasis, partner availability → gaps, surplus classes, dependency map | Asymmetry magnitude (ECOQ-004) |
| SYS-005 | Offers, accept/decline, stocks → settled trade, released reservations, trade-credit | Fresh-account caps; visibility policy (SDQ-004; SEC-023) |
| SYS-006 | Lever changes → stability state, multipliers, policy history | Axes and effects (SDQ-005); may be cut from FPB |
| SYS-007 | Funds, program selection → unlocks/modifiers | Whether the FPB ships zero programs (P6 §11) |
| SYS-008 | Acts, treaties, trades → pair state, visible history | State list and visibility (SDQ-014/004) |
| SYS-009 | Offer/accept/exit → treaty records, mechanical gates | Type list and enforcement scope (SDQ-014) |
| SYS-010 | Membership, roles, contributions → pool, permissions, audit rows | Role matrix and succession (SDQ-012/013) |
| SYS-011 | Readiness spend, posture → readiness level, deterrence signal | OP model and war rules (D-004; SDQ-008) |
| SYS-012 | Campaign orders, readiness → outcomes, settlement terms | All rules (war stage; OD-12) |
| SYS-013 | Recorded acts → standing registers | Act taxonomy and anti-farming costs |
| SYS-014 | Register states → public views, milestones | Whether it is needed at all (SIM-007) |
| SYS-015 | Notable events → chronicle entries | Entry taxonomy/quality bar (SDQ-017) |
| SYS-016 | Queued actions → resolved state, turn ledger, checkpoints | Ordering catalog (SDQ-018); catch-up policy (TQ-04) |
| SYS-017 | Journal/turn rows → digest, re-entry summary | Retention and history depth (SDQ-017) |
| SYS-018 | New-nation state → first decision, reveal state | Content and success thresholds (PXO-007; OD-11) |

### 5.5 What the catalog does not cover

The prompt's required list includes four areas with **no SYS ID**: account and session management, moderation and abuse response, audit logging, and backup/restore. They exist as cross-cutting requirements in Prompt 8 (SEC-001…008, SEC-026…028, SEC-031, SEC-030), not as catalog systems. This is a **traceability gap, not a missing design**: the requirements exist and are testable. This report does **not** extend the SYS register beyond SYS-018, because the system catalog is Prompt 6's register and a new ID family would imply a design decision that has not been made. Instead, §12 carries them as requirements (REQ-003, REQ-025…029) with the mapping recorded here (DEF-013).

**One genuine ambiguity:** SYS-003's P6 name covers production *and* development capacity, while P7 §6.1 splits production/upkeep (SYS-003) from treasury (SYS-002) and treats them as one *build unit*. The split is intentional and consistent; the naming drift is cosmetic. No merge is proposed.

### 5.6 Build-unit recommendation (not an approval)

Prompt 6's Tier A is five build units covering six IDs: SYS-016, SYS-002+003, SYS-004, SYS-017, SYS-018. Prompt 5's concept test requires trade (E5) and a domestic-policy axis (E1). Prompt 7's FPB design requires directed trade. **The smallest coherent FPB build set is therefore Tier A plus SYS-005 (directed) plus a minimal SYS-008/009/013/015 record layer, with SYS-006 minimal or cut.** That is six build units and ten IDs, and it is a recommendation for the owner's scope decision (OD-02), not a re-tiering of Prompt 6.

---

## Section 6 — Cross-system dependencies and interaction map

### 6.1 Two different questions

The matrix below records **logical dependencies** — which system needs which other system's state or authority to be correct. It does **not** assert execution order. Execution order is a separate question owned by SDQ-018, and only two orderings are actually specified today: (a) the economy resolves as a single phase with affordability checked at submission and again at the boundary (P7 §14), and (b) permissions are checked before any mutation is applied (P8 SEC-012). Everything else in the "ordering rule" column is marked as derived, proposed, or unknown.

### 6.2 Dependency matrix

| # | Source → receiving | State or information crossing | Ordering rule | Potential contradiction or exploit | Cost / free-tier implication | Inherited IDs | Status |
|---|---|---|---|---|---|---|---|
| 1 | SYS-003 → SYS-002 | Output, drains, investment results | Boundary; income and drains in one phase | If drains precede income, a solvent nation can fail spuriously; order must be fixed | 1 summary write + balance update per nation per boundary | INT-001/002; ECON-001 | **Proposed** (order not fixed) |
| 2 | SYS-004 → SYS-005 | Gaps, surpluses, efficiency asymmetry | None — player-driven offers | Two accounts trading to move value (R-13); self-dealing to dodge scarcity | 4+ writes per completed trade | ECON-011/013; R-13 | **Proposed** |
| 3 | SYS-002 → every spender | Available vs committed balance | Authorize before reserve; recheck at boundary | Double-spend if reservation and settlement are not atomic (SEC-016) | Reads per action; write per mutation | SEC-014/016; R-19 | **Verified as requirement**, unimplemented |
| 4 | SYS-006 → SYS-003/002 | Stability multiplier, policy costs | Boundary | Stability could silently multiply output and break forecasts | 1 write per change + per boundary | SDQ-005 | **Unclear** (effect unset) |
| 5 | SYS-009/008 → SYS-010 | Treaty state, pair standing, membership | Record immediate; effect at boundary | A treaty signed after the boundary but before resolution could be applied inconsistently | 1–2 writes per event | SDQ-012/014 | **Unclear** |
| 6 | SYS-010 → SYS-012 | Pool contribution, members, roles | Boundary | Alliance bank funds a campaign without member consent | War-stage; audit rows | FO-007; TH-021 | **Unclear** (war rules absent) |
| 7 | SYS-012 → SYS-016 | Campaign orders, objectives, resolution | Queued class; boundary | Campaign orders racing trade settlement; no tiebreak catalog | Unknown; potentially write-heavy | SDQ-018; TH-022 | **Conflicting** (no rules) |
| 8 | Protection state → SYS-016/012 | Eligibility, cooldowns | Boundary | Protection windows engineered as shelters (F-017) | Low | FO-003; R-04 | **Unclear** |
| 9 | SYS-018/accounts → SYS-005/012 | Fresh-account restrictions | Between boundaries; change at a fixed age | Caps that expire mid-turn create a one-turn arbitrage | Low; a few reads | SEC-023; R-13 | **Proposed** (parameters unset) |
| 10 | Absence state → SYS-017/010/009 | Inactivity, membership, treaty standing | Boundary | An absent ally's pool share or treaty obligations become unenforceable | 1 write per boundary | FO-015; ECON-012; R-21 | **Proposed** |
| 11 | SYS-005 → settlement | Offer acceptance, idempotency key | Acceptance is atomic; duplicate accept no-ops | Double settlement on retry (ambient, not adversarial) | 4+ writes; unique index on key | SEC-014; R-19 | **Verified as requirement** |
| 12 | Sessions/permissions → all valuable actions | Actor, nation, role, scope | Checked before mutation | IDOR / confused deputy (TH-008) | Reads per action | SEC-012 | **Verified as requirement** |
| 13 | SYS-015/audit ledger → disputes | Event rows with actor, turn, cause | Written in the same transaction as the mutation | Evidence gap if audit write fails independently | **Every mutation +1 row minimum** | SEC-031 | **Proposed** (spine exists as requirement) |
| 14 | SYS-016 → recovery | Phase checkpoints, turn status | Forward-only resume | Partial turn leaves unequal states (TH-010) | Checkpoints + per-phase writes | SEC-020/021 | **Proposed** |
| 15 | SYS-016/017 → player | Digest, notifications | After commit | A digest generated before commit can describe an outcome that then rolls back | Reads; rendered on demand | SYS-017; DP-004 | **Proposed** |
| 16 | All systems → D1 | Rows read/written, storage | Within request; 50 subrequests free | Write amplification and storage cap | **Critical** | SDQ-003; D-005 | **Unmeasured** |
| 17 | SYS-016 → cron | One invocation per boundary | Trigger at :00 UTC every 2h | CPU 10 ms and 50 subrequests may be insufficient; duplicate invocation | **Critical** | SEC-018/019; SDQ-018 | **Unmeasured** |
| 18 | Backups/logs → storage | Snapshots, audit rows | Daily/rolling | 500 MB database cap; 5 GB account cap | **Critical** | SEC-030/031; SDQ-003 | **Unmeasured** |
| 19 | Abuse controls → quotas | Rate-limit counters, per-class caps | Before work is done | A rate-limit table becomes its own write amplifier | Negative net cost claimed; unmeasured | SEC-029 | **Proposed** |
| 20 | Accounts → e-mail provider | Verification, recovery mail | Out of band | Free e-mail caps throttle signup/recovery; provider dependency | 100–300 mails/day (free tiers) | OSQ-003; SEC-004 | **Conditional** |

### 6.3 The five load-bearing couplings

1. **Economy ↔ specialization ↔ trade.** This is the concept's engine (DP-005). It only works if the efficiency asymmetry is large enough that buying is genuinely cheaper than self-producing (ECOQ-004), and if trade settlement is atomic (R-19). If either fails, the game becomes either autarkic spreadsheet-play or a market-abuse surface.
2. **Acts ↔ reputation ↔ diplomacy.** Standing must be earned by recorded acts, not by a grindable score (SYS-013). The risk is staged-act inflation (R-06); the mitigation is an act taxonomy that is expensive to fake, which does not yet exist.
3. **Conflict ↔ everything.** Conflict is the largest unbuilt surface. Its economic face (readiness upkeep) exists; its rules do not. Every dependency that touches SYS-012 is therefore marked unclear, and the synthesis refuses to specify an order for a system that has no rules.
4. **Turn engine ↔ every mutation.** SYS-016 is not plumbing; it is the mutation engine. A duplicate or partial resolution is a global economy event with no attacker (TH-009/010). The requirement set is strong; the implementation is absent.
5. **Storage ↔ every audit requirement.** The security posture depends on permanent evidence rows; the free tier's 500 MB per-database cap makes "permanent" a design problem, not a storage detail (§17.5). This is the coupling most likely to force a scope or retention decision.

### 6.4 The three most dangerous interaction points

| Rank | Interaction | Why dangerous | Earliest safe test |
|---|---|---|---|
| 1 | Boundary resolution under partial failure (#14) | Unequal outcomes across nations are worse than a delayed turn; recovery can double-apply | PV-03, ST-008/009 (simulated) |
| 2 | Trade settlement and duplicate acceptance (#11) | Ambient retries can mint or duplicate value; R-19 requires zero partial transfers | PV-04, ST-004-class |
| 3 | Audit/storage growth (#13/#18) | The control that makes every dispute fair is the control that exhausts the free database | PV-05 |

### 6.5 Logical versus execution order — explicitly

A logical dependency says "B cannot be correct unless A's state is current." An execution-order requirement says "A must run before B within the boundary." The matrix records the former. The only execution-order statements the research actually makes are: permissions before mutation; affordability at submission and recheck at the boundary; settlement atomic per trade; resolution forward-only from checkpoints. **The phase sequence of a boundary is not specified.** Any implementation that assumes a sequence is making an unrecorded design decision, which is exactly what SDQ-018 exists to prevent.

---

## Section 7 — Canonical two-hour turn model

### 7.1 What is fixed

| Property | Value | Source |
|---|---|---|
| Cadence | One global turn every two hours; 12 per day | AI_CONTEXT §2; P1 §3 |
| Alignment | Fixed UTC boundaries (:00) | AI_CONTEXT §2; P6 SYS-016 |
| Resolution moment | The boundary only; no live resolution of valuable actions | P6 §17; P7 §14 |
| Timing classes | Immediate-with-record, queued-until-boundary, boundary-scheduled | PXO-003; P6 §17 |
| Player presence | Never required at a boundary | DP-002; P4 §9 |
| Duplicate execution | Must be a no-op | SEC-019/020; TH-009 |
| Partial failure | Forward-only resume from phase checkpoints | SEC-020/021; TH-010 |

No report proposes changing the cadence. **This synthesis does not either.**

### 7.2 Turn stages: what is specified and what is not

| # | Stage | What must happen | Specified? | Source |
|---|---|---|---|---|
| 1 | Action intake | Validate shape, classify timing, reserve commitments, write pending record | **Partly** — class rules yes; reservation semantics yes; input validation requirements yes | P7 §14; SEC-013/014 |
| 2 | Eligibility and permission checks | Actor owns nation; role permits verb; cooldowns and protection states allow it | **Requirement only** — SEC-012; protection rules absent | SEC-012; FO-003 |
| 3 | Economy processing | Production, income, drains, material flows; no negative balances | **Yes at rule level** — order of income vs drains unresolved | P7 §6.4/§14; SEC-025 |
| 4 | Development and upkeep | Apply line investments, upkeep, emphasis changes queued to this boundary | **Partly** — affordability recheck yes; order vs trade unclear | ECON-002/017; SDQ-018 |
| 5 | Trade settlement | Atomic paired transfer; idempotent accept; no partial | **Yes at rule level** — position in phase order unknown | ECON-013; R-19; SEC-016 |
| 6 | Diplomacy and alliance updates | Treaty state changes, role changes, pool contributions | **Proposed** — timing stated, state machine absent | SDQ-012/014 |
| 7 | Strategic actions and conflict | Campaign orders resolve, outcomes apply, settlements record | **No** — war rules do not exist | P6 §15; TH-022 |
| 8 | State changes and notifications | Commit authoritative state; generate digest; record chronicle | **Proposed** — order after commit implied, not stated | SYS-017; DP-004 |
| 9 | Turn completion and logging | Mark turn done, checkpoint per phase, write pipeline rows | **Yes at requirement level** | SEC-019/020/031 |
| 10 | Recovery from partial failure | Resume unfinished phases only; never re-derive completed work | **Yes at requirement level** | SEC-020/021 |
| 11 | Duplicate invocation | Second resolver finds `done` and exits with no player-visible change | **Yes at requirement level** | SEC-019/020 |

### 7.3 Ordering rules: the honest inventory

| Rule | Classification | What it says | Evidence |
|---|---|---|---|
| Boundary-only resolution | **Explicit** | Nothing valuable resolves between boundaries | P6 §17; P7 §14 |
| Affordability at submission and recheck at boundary | **Explicit** | Cheap fail first; reservation release on failure | P7 §14/§6.5 |
| Atomic paired settlement | **Explicit** | A trade transfers both sides or neither | ECON-013; R-19 |
| Deterministic tiebreak, published | **Explicit as a principle** | Contested actions resolve by a recorded, non-random rule | P6 §17; P8 SEC-018 |
| Deterministic tiebreak catalog | **Unknown** | The actual rule set does not exist | SDQ-018 |
| Permissions before mutation | **Derived from security requirement** | No mutation without authority check | SEC-012 |
| Audit row in the same transaction as the mutation | **Proposed** | Evidence cannot diverge from state | SEC-031; P8 §14.8 |
| Economy as one phase | **Proposed** | Production, drains, investment in one transaction boundary | P7 §14.3 |
| Income before drains | **Proposed (conceptual flow only)** | P7 §6.4's flow puts output/income before drains, but no normative ordering table exists | P7 §6.4; SDQ-018 |
| Trade before or after production | **Unknown** | Changes who can afford what at the boundary | SDQ-018 |
| Diplomacy before or after economy | **Unknown** | Changes treaty cost/benefit at the boundary | SDQ-018 |
| Campaigns after economy | **Unknown** | War rules absent | War stage |
| Notifications after commit | **Proposed** | Digest must not describe a rolled-back outcome | DP-004 |
| Phase-grain dedup | **Explicit as a requirement** | Re-running a phase cannot double-apply | SEC-021 |
| Retry policy after abort | **Unknown** | How many retries, with what backoff, before a delay is announced | SEC-022 (announcement only) |

### 7.4 Boundary behavior, idempotency, recovery

**What the security report requires (not implements):** an exclusive resolution claim per turn; a turn-state ledger recording phase completion; per-phase checkpoints; dedup at phase grain, not turn grain; a deterministic boundary; and an announcement when a turn is delayed. The failure modes are named precisely: duplicate invocation (TH-009) and partial processing (TH-010). The recovery posture is forward-only: resume unfinished phases, never re-derive completed ones, and if the turn is fundamentally inconsistent, restore to the last fully committed turn with disclosure (SEC-030/022).

**What is missing for a *specification*:** the actual phase table with inputs/outputs per phase, the order of the ten stages, the tiebreak catalog, the retry/backoff policy, the definition of "fundamentally inconsistent", and the exact checkpoint granularity. **These are not documentation gaps to be waved away — they are the difference between "we know we need exactly-once" and "we can build exactly-once."**

### 7.5 Interaction with the free hosting environment

| Constraint | Current documented value (free) | Why it matters | Status |
|---|---|---|---|
| Scheduled invocations | Cron triggers execute on UTC; the free plan permits only a small number of triggers (P1 §6 recorded five) | 12 turns/day needs **one** trigger on a two-hour expression; the count is not binding | Verified enough; re-check before deployment |
| CPU per invocation | **10 ms** (current; P1 recorded 50 ms) | A boundary that processes many nations may exceed it | **Unmeasured — the top capacity risk** |
| Subrequests per invocation | **50** (free); 1,000 (paid) | Per-nation loops that fetch individually will exhaust this almost immediately; set-based SQL and batching are mandatory | **Unmeasured** |
| D1 concurrency | One database is single-threaded; 6 simultaneous connections per invocation | Boundary work serializes; a long batch blocks reads | Documented 2026-10-23 |
| SQL duration | 30 s maximum | Large migrations/updates must be chunked | Documented 2026-10-23 |
| Wall-clock guarantee | No exactly-once or bounded-latency guarantee is documented; cron runs on underutilized machines | A turn can be late; the design must detect and announce, not assume | Documented 2026-10-23 |
| D1 writes | 100k rows/day | Each boundary writes summaries for every nation | **Unmeasured amplification** |
| D1 storage | 500 MB per database, 5 GB per account | Audit rows grow daily | **Unmeasured** |

**What must be measured before the turn design is called feasible (PV-01…PV-03):**

1. A single cron invocation resolving N = 50, 250, and 1,000 synthetic nations with set-based SQL: CPU time, subrequest count, wall-clock duration, and whether the invocation completes.
2. The same at a boundary with concurrent player reads (the digest traffic spike).
3. A forced duplicate invocation and a forced mid-phase abort, verifying the no-op and forward-only resume behaviours.

**Do not infer feasibility from the existence of cron triggers.** The provider scheduling a job is not evidence that the job's workload fits the free CPU and subrequest budget.

### 7.6 Verdict on the turn model

**No complete deterministic turn-order specification exists.** What exists is a strong timing contract, a correct set of integrity requirements, and an explicit open question (SDQ-018) that the project has consistently refused to paper over. That is the right posture. It also means **the turn engine cannot be implemented responsibly until SDQ-018 is answered and PV-01…PV-03 are run**, because the two most likely failure modes — a boundary that exceeds 10 ms of CPU and a phase order that makes solvency depend on trade timing — are both invisible to paper design.

---

## Section 8 — Consolidated economy design

### 8.1 The model in one page

**Consolidated proposal (ECON-001/002/006/011/013/017/019):** one national treasury; no debt, no interest, no yield on cash; five development lines (Production, Commerce, Administration, Works, Readiness); four material classes (Sustenance, Construction, Industrial, Ordnance); interdependence produced by *efficiency asymmetry*, not geography or artificial exclusion; directed bilateral trade at first playable, fee-free and atomic; a listings market only behind a six-condition gate; paid, distance-gated, boundary-effective respecialization with a bounded retooling dip; and an austerity floor instead of bankruptcy.

This is a coherent economic *architecture*. It contains **no numeric parameters** — no production rates, drain curves, threshold placements, respec costs, trade caps, or starting grants. That is deliberate (P7 §3, §22), and it is the single biggest reason the design is not implementation-ready.

### 8.2 Money supply and the conservation identity

| Category | Definition | Supply effect | Control |
|---|---|---|---|
| **C1 Created** | Production income, one-time starting grant, rare disclosed systemic adjustments | **+** | Only creation channel; grows only after investment |
| **C2 Transferred** | Directed trades, treaty payments, alliance contributions, indemnities (war stage) | **0 net** | Atomic paired settlement (R-19); two ledger records per transfer |
| **C3 Destroyed** | Upkeep, investment spend, market fees if ever introduced | **−** | Drains scale with levels; no refunds on completed spend |
| **C4 Held** | Earmarked reserves, queued-commitment reservations | 0 supply; velocity only | Reservation release is C2's mirror and must also net zero |

**Identity:** Δ circulating supply = C1 − C3. Any implementation that cannot explain a balance delta as one of these four categories is either a bug or an undeclared mint. This is the economic counterpart of SEC-010/011's server-authority rule, and it is testable at the ledger level (ECV-001/ECV-002-class).

### 8.3 Development lines and their economic roles

| Line | Role | Material relationship | Trade posture | Dominant-strategy risk |
|---|---|---|---|---|
| **PRO** Production | Income + bulk goods | Produces MAT-01 and MAT-03 | Sells surplus to net importers | "Income is the win button" — countered by level-scaled drains and option thresholds |
| **COM** Commerce | Margin and market posture | Buys/sells MAT-01/03 | The "salesfloor" line | Market arbitrage — countered by thin liquidity and relationship pricing |
| **ADM** Administration | Decision capacity: order slots, arc breadth | Buys MAT-03 | Relational buyer | Boring-filler risk; thresholds must be genuinely interesting |
| **WRK** Works | Drain reduction, resilience, construction | Produces MAT-02 | Stable two-way pair with PRO | Efficiency compounding — countered by scaled works drains |
| **RDY** Readiness | Military floor, deterrence | Converts MAT-03 → MAT-04 | Deterrence niche | Mandatory-for-safety risk — bounded by DP-006 and AP-004 |

**Narrowing recorded (SDQ-001):** the line *set* is answered at proposal level; the numeric threshold model remains open (ECOQ-005). Science is deliberately not a line; it is a SYS-007 program class (Tier C), because it unlocks capability rather than producing per turn.

### 8.4 Materials and scarcity

| Class | Economic function | Primary uses | Substitution route |
|---|---|---|---|
| **MAT-01 Sustenance** | Consumed-and-gone upkeep floor | Every nation every turn; recovery; relief transfers | Emergency MAT-03 conversion at a disclosed inefficient rate; buy; tighten drains |
| **MAT-02 Construction** | Capital input | All line investments; repair; reserves | Self-produce at low efficiency; de-prioritize investment; buy |
| **MAT-03 Industrial** | Versatile intermediate | COM/ADM/WRK steps; MAT-04 conversion; market benchmark later | Self-produce; postpone thresholds; buy |
| **MAT-04 Ordnance** | Defense consumable | Readiness upkeep; campaigns later; allied support | Lower readiness at a known deterrence cost; stockpile; buy |

**The structural test (P7 §8.4):** every meaningful capability gap has at least two sourcing routes, and every surplus has at least two buyer classes. The test passes *structurally* on paper; whether the tuned asymmetries are strong enough to make trade real is ECOQ-004, unexecuted. **A fifth consumer/prestige class is deferred** (ECON-023), with an explicit revisit trigger: only if SYS-006 or diplomatic status needs an economic input.

### 8.5 Trade and settlement

| Rule area | Consolidated proposal | Status |
|---|---|---|
| Offer | Treasury and/or material amounts; no conditional clauses; persists offline | Proposed (ECON-013) |
| Response | Accept / decline / structured counteroffer; declining carries no negative record | Proposed |
| Reservation | **Open conflict (DEF-018):** P7 §10.2 says both "the offer reserves nothing until acceptance" and "a signed-pending offer does freeze", and §14.1 says no reservation until acceptance. The economy stage must choose. Fixed either way: acceptance re-checks both sides against server state and settles atomically (R-19) | **Open**; R-19 invariant |
| Settlement | Both sides or neither; duplicate accept no-ops; failure releases reservations with a reason | Proposed; SEC-014/016 |
| Fees | None at first playable; market-stage fee policy deferred to gate G-5 | Proposed |
| Visibility | Completed terms visible to both parties permanently; public visibility is **open** (SDQ-004) | Open |
| Market | Not at FPB; gates on G-1…G-6 (identity integrity, write budget, observed liquidity, reference-price design, fee policy, ops capacity) | Deferred |
| Automation/multi-account | Fresh-account caps, per-pair velocity caps, asymmetric outgoing caps (SEC-023) | Proposed; parameters unset |

**Why directed-first is an economic decision, not a technical shortcut:** a listings board in a small world is empty, teaches financial literacy the game has not taught, and imports the genre's largest manipulation surface before any defence exists (P7 §10.3). Directed trade makes every exchange a relationship act, which is the concept's identity.

### 8.6 Sinks, sources, and anti-snowball posture

**Sources:** production income (C1), starting grant (C1, one-time), disclosed systemic adjustments (C1, rare; ECOQ-013). **Sinks:** sustainment/readiness/works upkeep (C3), investment purchases (C3), emphasis change (C3), market fees only if the market stages. **No sinks by confiscation; no sources by activity reward.**

**Anti-snowball mechanisms:** drains scale at least as fast as output; thresholds grant options rather than multipliers; no interest or yield on idle cash; trade transfers rather than creates; conflict effects are bounded and itemized. **The unresolved part:** whether these mechanisms are sufficient is a numeric question (ECOQ-002), and the genre's documented failure mode — veteran hoarding and newcomer catch-up (F-012) — has no designed answer yet (FO-018 is owner-held, ECON-012 sets five constraints on any future answer).

### 8.7 Player-facing economic information

P7 §15 specifies six number types (actual, committed, projected, forecast, reference, derived) across four surfaces (finance view, order preview, digest, chronicle). Every forecast is labeled; every failure has a reason; no screen may imply certainty the server does not have. **This is the strongest part of the economy design** because it is a *contract*, not a feature, and it directly implements DP-004.

### 8.8 Storage, writes, and free-tier pressure (revised estimate)

**P7's estimate (verified arithmetic, stated assumptions):** roughly `N × 30 ± N×12` row-writes/day for N active-equivalent nations; therefore 100k writes/day ≈ 3,000 nations "on the economy alone" (P7 §16.3).

**This synthesis's correction (DEF-006):** that estimate excludes four categories the project's own security design requires:

| Additional category | Planning increment per active nation/day | Source |
|---|---|---|
| Audit-spine row per mutation (SEC-031) | +15 to +20 rows | P8 §13.2/§13.4 |
| Auth/session events (sign-in, rotation, revocation) | +2 to +6 rows | P8 §4.3/§13.2 |
| Rate-limit counters and abuse events | +1 to +5 writes | P8 SEC-029 |
| Index maintenance on mutation-heavy tables | **Unknown**; potentially +1 per index per write | D1 documentation does not state index accounting clearly; measure it |

**Revised range:** without index effects, `N × 48 ± 15` writes/day → **100k/day supports roughly 1,600–2,000 active-equivalent nations**; if index maintenance counts at 2–3 indexes, the range falls to **roughly 1,100–1,400**. The honest statement is: **P7's ~3,000 is an upper bound that assumes no audit row, no session writes, and no index cost; the planning figure should be ~1,100–2,000, to be measured (PV-04).** This does not overturn the conclusion that the economy is not the first binding constraint at a small launch; it does mean the margin is roughly half what the earlier report suggested.

**Storage (assumptions, not measurements):** current game state is small (a nation row, line rows, offers, treaties, relationship records); audit and history dominate. At ~250 bytes per appended audit/history row and ~15–20 appended rows per active nation/day:

| Active nations | Appended audit/history per day | Days to 500 MB (ignoring other tables) |
|---|---|---|
| 100 | ~0.4–0.5 MB | ~1,000+ days |
| 300 | ~1.1–1.5 MB | ~330–450 days |
| 1,000 | ~3.8–5.0 MB | ~100–130 days |

*(This table counts audit rows only. Adding 1–3 trade headers per active nation per day lowers the day counts by roughly 20–30%; §17.4 uses the inclusive range.)*

**Conclusion:** a persistent world with permanent audit rows **cannot** live indefinitely in a single 500 MB free database. Retention (hot 90 days + monthly aggregates + periodic export) is a **functional requirement**, not housekeeping. Deleting evidence without analysis would undermine the security posture; exporting and aggregating preserves the requirement. This is the single most important economy–security–cost coupling in the project.

### 8.9 What may stay open, and what blocks the FPB

| Open question | May stay open during next-stage planning? | Blocks FPB? | Reason |
|---|---|---|---|
| ECOQ-002 drain curves and austerity thresholds | No | **Yes** | Without them, solvency and failure behaviour cannot be implemented |
| ECOQ-004 asymmetry/respec numerics | No | **Yes** | Determines whether trade is meaningful and respec is fair |
| ECOQ-005 threshold placement | No | **Yes** | Determines progression pacing |
| ECOQ-003 starting grant size | Partly | Yes (onboarding) | Affects first-session viability |
| ECOQ-006 market gate thresholds | Yes | No | Market is deferred |
| ECOQ-010 MAT-01 spoilage | Yes | No | Optional stress valve |
| ECOQ-013 systemic event frequency | Yes | No | Rare/disclosed; can be zero at FPB |
| SDQ-004 trade visibility | Partly | Yes (UI/privacy) | Affects what the digest and profiles show |
| SDQ-003/SDQ-017 retention | No | Yes (architecture) | Storage cap and re-entry history |

---

## Section 9 — Politics, diplomacy, alliances, and strategic conflict

### 9.1 Domestic politics

**What exists:** a light lever layer with one or two trade-off axes, cooldowns, and stability as a multiplier on other paths (SYS-006; FO-005; SDQ-005). The design intent is explicit that politics is a *floor and enabler*, not a success ladder (DIR-3), and that the layer is a cut candidate if it reads as arbitrary.

**What does not exist:** the axes, their effects, stability's numeric range, how policy changes are explained, how a stability shock is recovered, and whether policy interacts with diplomacy (e.g., openness affecting treaty options). P7 §23C flags austerity as the stabilizer but does not connect it to SYS-006.

**Assessment:** the layer is *optional* for the FPB. Shipping one axis with a clear, digest-explained effect is defensible; shipping none is also defensible and reduces scope. The concept does not depend on it (economy and diplomacy carry the identity). This is a scope decision for OD-02, not a design gap that blocks Stage 1.

### 9.2 Diplomacy and bilateral relationships

**What exists:** typed pair records with visible histories (SYS-008); a minimal treaty set — a mechanically enforced non-aggression analogue plus non-enforced promise records (SYS-009), matching the verified genre pattern that only NAPs are mechanically enforced; acts-driven reputation across named registers (SYS-013); a chronicle of notable acts (SYS-015).

**What is missing:** the relationship state machine (SDQ-014), the full treaty type list, the visibility policy (SDQ-004), the effect of treaty exit on standing, and the interaction between reputation and alliance membership. The *verbs* are clear; the *rules* are not.

**Abuse surface:** reputation farming through staged acts (R-06), treaty spam, and using promise records as a social weapon. The mitigations are a costly act taxonomy, scope-limited treaties, and visible exit records — none of which is specified enough to test.

### 9.3 Alliances

**What exists:** a minimal alliance object with name, bank view, one contribution bracket, role-lite permissions, and an audit-first record culture (SYS-010; FO-007). Alliances are explicitly optional; independent play must remain viable (AP-004).

**What is missing:** the permission matrix (SDQ-012), succession and defunct-alliance asset rules (SDQ-013), the collective-action set (FO-008), and the interaction between alliance pool contributions and national solvency. P8 TH-021 treats improper alliance administration as a real threat; without a permission matrix, a shared pool is a liability.

**Abuse surface:** pool draining by a compromised or malicious officer; membership as a shield for collusion; alliance-wide trade funnelling (R-08/R-13). The audit posture is the right control; it is not yet a design.

### 9.4 Strategic conflict

**What exists:** the concept of bounded, declared campaigns over non-geographic objectives; a readiness line that burns upkeep; a settlement vocabulary as a differentiator (UXD-004, the weakest-evidence differentiator); and the explicit statement that the war stage owns all rules (P6 §15; P8 TH-022).

**What does not exist:** campaign initiation, action budgets (OP is Provisional, D-004), cooldowns, protection states, combat resolution, objective capture, settlement enforcement, peace/surrender, or the economic effects of losing. **No part of the conflict journey can be built from the current research.** This is by design, but it means the game's "strategic conflict" pillar is currently a promise, not a system.

### 9.5 Collusion and competitive-integrity risks

| Risk | Mechanism | Existing mitigation (design level) | Gap |
|---|---|---|---|
| Multi-account funnelling (R-01/R-13) | Second account feeds the main nation | Fresh-account caps, per-pair velocity, outgoing caps (SEC-023) | Parameters and detection tuning absent |
| Fake wars / settlement farming (R-05) | Two alliances trade wins for standing | Bounded effects, settlement records, act taxonomy | No war rules to test |
| Alliance pool capture (R-08) | Officer drains shared treasury | Roles, audit rows, two-person rule where staffing allows | Permission matrix absent |
| Treaty-web manipulation (R-06) | Staged acts inflate reputation | Multiple registers, costly acts | Act costs undefined |
| Market manipulation (R-14/15) | Wash trades, cornering | Market deferred behind G-1…G-6 | Not applicable at FPB; must be designed before market |

### 9.6 Dependencies and operational burden

All four domains depend on SYS-016's boundary and SYS-002's atomic settlement. Their *marginal* cost is modest in writes (a few rows per event) but their *logical* complexity is high: each adds a state machine, a permission surface, and an evidence requirement. Alliances and conflict also add **moderation** load (disputes, betrayal, pool theft), which is a people cost, not a hosting cost — and the project has one operator (§17.7).

### 9.7 Missing rules that make connected systems ambiguous

| Missing rule | Systems made ambiguous | Consequence | Owner |
|---|---|---|---|
| Treaty state machine and types | SYS-008/009/013 | Cannot define what a treaty *does* or when it ends | SDQ-014 |
| Alliance permissions and succession | SYS-010/002 | Shared pool cannot be safely operated | SDQ-012/013 |
| Protection/cooldown states | SYS-012/016 | Cannot prevent shelter engineering or resolve timing | FO-003; war stage |
| Campaign and settlement rules | SYS-011/012/013 | Conflict pillar unbuildable | War stage; D-004 |
| Reputation act taxonomy | SYS-013 | Standing can be farmed or is meaningless | P5/P6 follow-up |
| Visibility policy | SYS-008/017 | Digest and profile cannot be specified | SDQ-004 |

---

## Section 10 — Security, privacy, fair play, and reliability baseline

### 10.1 The posture in five sentences

The browser is a display surface; every valuable quantity is recomputed server-side from authoritative state (SEC-010/011). Every action is authorised against the acting nation and, where relevant, a role (SEC-012). Value moves atomically and idempotently, with no partial transfers and no negative balances (SEC-014/016/025; R-19). The turn resolves exactly once, with an exclusive claim, phase checkpoints, and forward-only recovery (SEC-018…021). Evidence is a permanent event spine, not surveillance: state-relevant events only, no free-form content by default (SEC-031; P8 §13.1).

### 10.2 Asset → protection matrix

| Asset or system | Confidentiality | Integrity | Availability | Evidence | Inherited requirements |
|---|---|---|---|---|---|
| Currency and commitments | Owner-only | **Critical** | Boundary-critical | Every mutation | SEC-010/011/014/016/025/031 |
| Material stocks | Owner-only | **Critical** | Boundary-critical | Every mutation | SEC-010/011/013/016 |
| Nation identity and emphasis | Public/owner split | High | Normal | Changes | SEC-001/003/012 |
| Sessions and credentials | **Critical** | **Critical** | High | Auth events | SEC-001…008 |
| Trades and offers | Parties only (public policy open) | **Critical** | Normal | Trade rows | SEC-012/014/016/019 |
| Turn state and queues | Ops only | **Critical** | **Critical** | Pipeline rows | SEC-018…021 |
| Treaties and relationships | Policy-dependent | High | Normal | State changes | SEC-012/031 |
| Alliance pool and roles | Members only | **Critical** | Normal | Admin acts | SEC-012/027/031 |
| Audit ledger | Ops only | **Critical** | High | Itself | SEC-031 |
| Backups | Ops only | **Critical** | High | Restore rows | SEC-030 |
| Personal data (e-mail, IP class) | Restricted | High | Normal | Minimised inventory | SEC-032; P8 §11 |
| Moderation cases | Role-scoped | High | Normal | Case records | SEC-026…028 |
| Ops credentials | **Critical** | **Critical** | High | Privileged reads | SEC-006/027 |

### 10.3 Requirement staging — and the correction it needs

P8's stage table is coherent: **A = 12** requirements (SEC-010/011/012/013/014/016/018/019/020/021/025/029), **B = 11** (SEC-001…005, 007/008, 023, 026, 030, 031), **C = 9** (SEC-006, 015, 017, 022, 024, 027, 028, 032, 033) — exactly 32. The two record-level problems found in the first edition were **corrected in Prompt 8 on 2026-10-23 and verified** (DEF-004/005; see P8 §22.2 item 6 and §25.7):

- **The stray count is gone.** P8 §15.4 now reads "12 requirements" and names the same 12 as §1.4, §16.2's FP column, and §17.1's A1–A7 list. It was a miscount, not a re-staging.
- **The subset is now stated.** A8 is described as the money/pipeline **spine subset of SEC-031**, a stage-B requirement whose full §13.2 coverage remains B5. The stage tally is 12 + 11 + 9 = 32; SEC-031 is counted once, in B.
- **TH-011's residual is explicit.** Stage-A prevention is the enforced boundary rule (SEC-018/020) plus A9's fail-with-reason disclosure; SEC-015 (Stage C) is the attribution refinement. The accepted residual is transparency-only: a client can still believe it acted in T when the server rules T+1, but the outcome class is disclosed and the stale-turn counter feeds review. ST-010 remains designed-not-executed.

Two related notes that are **not** staging conflicts: SEC-026 (pre-launch) is deliberately paired with SEC-027/028 tooling in Stage C — the ladder and logged acts ship first, the tooling follows; and SEC-017's ledger discipline (Stage C) is supported at Stage A by SEC-020/021's phase checkpoints.

### 10.4 Design vs implemented vs tested

| Layer | Count | Status |
|---|---|---|
| Threats identified | 25 (TH-001…025) | Design-level analysis |
| Requirements defined | 32 (SEC-001…033, SEC-009 reserved) | Proposal status; none approved |
| Tests designed | 20 (ST-001…020) | **All designed-not-executed** |
| Walkthroughs | 18 (W-18-A…R) | Design-level scenarios |
| Controls implemented | **0** | No production code exists |
| Controls independently reviewed | **0** | No external review |

**This table is the honest answer to "is the game secure?" — no. It has a security *design*, not a security *posture*.**

### 10.5 Cost-sensitive security and free-only alternatives

| Requirement | Why it costs | Free-only path that preserves the requirement | What must be disclosed or accepted |
|---|---|---|---|
| Permanent audit spine (SEC-031) | 500 MB database cap | 90-day hot retention + monthly aggregates + periodic export; integrity rows kept, high-volume rows sampled per P8 §14.8 | Retention window is public; disputes older than the window rely on aggregates/exports |
| Backups and restore (SEC-030) | Snapshots and storage | D1 Time Travel (7 days free) + scheduled logical export; restore drill quarterly | RPO ≤24h only if daily export runs; RTO depends on manual restore; OSQ-007 |
| E-mail verification (SEC-001/004) | 100–300 mails/day free tiers | Verify on signup if budget allows; otherwise unverified with throttles and a clear recovery caveat | Weaker recovery anchor; more bot pressure (OSQ-003) |
| Monitoring (SEC-033) | Paid tiers for long retention/alerts | Free Workers Logs + D1-based gauges + free uptime monitor; alerts by e-mail | Short log retention; alert latency; no on-call |
| Rate limiting (SEC-029) | Paid WAF rules | Application-level per-class quotas in the Worker; Cloudflare's free DDoS protection | No edge-level custom rules; quotas consume the same request budget |
| Moderation (SEC-026…028) | Human time | Single operator + evidence-first process + disclosed response hours | Slow response; conflict-of-interest risk (OSQ-005/012) |
| Turn resolution (SEC-018…021) | CPU/subrequests | Set-based SQL batches; one cron; optional Durable Object alarm as a second mechanism | DO alarms consume request budget; unmeasured |
| Auth (SEC-001…005) | Paid auth service | In-Worker Better Auth-class library; **the KDF choice is part of the cost test** (Argon2id/WASM vs native PBKDF2 on a 10 ms Worker; DEF-015/PV-15); no third-party auth dependency | Implementation, review burden, and a measured security/CPU trade-off |

**No requirement is removed to meet ₹0.** Each is either preserved with a smaller retention/automation envelope, or its residual risk is explicitly disclosed and owned. The two places where the free tier genuinely bites are **backups** (RPO/RTO degrade) and **audit retention** (history must be exported, not kept hot forever).

### 10.6 The five gaps that matter most

1. **No implemented control.** Everything is design.
2. **No executed test.** ST-001…020 are paper; the turn and trade invariants are unproven.
3. **Staging was ambiguous; now corrected.** DEF-004/005 were fixed in P8 on 2026-10-23 (12 stage-A requirements plus the SEC-031 spine subset).
4. **Recovery is aspirational.** There is no restore drill, and the free tier's 7-day Time Travel sets a hard floor on RPO.
5. **Single-operator risk.** The two-person rule cannot exist at launch; disclosure is the only compensating control (OSQ-005/012).

---

## Section 11 — First-playable scope and deferred features

### 11.1 The scope problem, stated precisely

Four reports use "first playable" for two different artifacts:

| Artifact | Definition in the source | What it includes | What it excludes |
|---|---|---|---|
| **Concept prototype (CP)** | P5 §15, "first playable concept" | One nation model, one policy axis, scheduled turns, digest, two value sources, **a basic player-to-player handshake**, scripted world | "Full anti-multi/anti-automation/admin systems" (O1); production/auth/hosting selection (O6); war balance; full alliances; months of progression |
| **First playable build (FPB)** | P6 §24, P7 §19, P8 §17.1 | Real multiplayer, accounts, server-authoritative economy, directed trade, digest, onboarding, Stage-A security | Listings market, full alliances, war, research depth, rankings |

The conflict is not cosmetic. P5's CP excludes authentication and integrity work; P8's Stage A says those controls are required "regardless of player count, whether the first build is a test server with ten friends or a public free alpha." P6's Tier A excludes SYS-005, but P5's CP requires a trade handshake and P7's FPB requires directed trade.

**This report's resolution (recommendation, not approval):**

1. **CP = supervised prototype.** Two to five invited testers, pre-provisioned accounts, no public signup, no e-mail, no recovery flow, no moderation tooling. It still requires the *integrity* subset of Stage A — server authority, atomic trade, turn idempotency, audit spine — because those are what the CP is testing. It does **not** require the account-security stack (B1), e-mail (B1/OSQ-003), or moderation machinery (B3).
2. **FPB = first real build.** Public-ish registration (even if invite-gated), account stack, Stage-A integrity, directed trade, digest, onboarding, and whatever scope the owner approves from §11.3.
3. **Stage A's "regardless of player count" is preserved for the FPB, and interpreted for the CP as "integrity controls only, with pre-provisioned identities."** That is a clarification of P8's intent, not a weakening: a CP with two testers can still corrupt value if settlement is not atomic. The CP runs on a local or throwaway deployment; it does **not** select production hosting or architecture (D-005 remains Provisional).

**Why this matters:** without the distinction, either the CP becomes an expensive public build (because P8 applies in full), or the FPB ships without the controls P8 calls mandatory (because P5's O1 is misread as "integrity can wait"). Both are failures. **OD-02 is the owner's decision.**

### 11.2 The recommended FPB core

**In (recommended):** SYS-001/002/003/004/005 (directed only)/008/013/015/016/017/018; a minimal SYS-009 (NAP analogue + two promise types); SYS-006 **only if** one axis can be specified cheaply; Stage-A security; a simple account stack (not the full B1 depth if the build is invite-only); export and backup basics.

**Out of the FPB:** listings market, full alliances, research programs, readiness/campaigns, rankings, contracts, consumer goods, espionage, seasons, chat, map, cities, population.

**Explicitly not cut:** server authority, atomic settlement, turn idempotency, audit rows for value movement, permission checks. A ₹0 budget is not a reason to remove them; §17 shows they fit at small scale, with retention/backup compromises disclosed.

### 11.3 Feature classification

Legend — **FPB**: core for the first playable build; **Launch**: required before public launch; **Later**: staged; **Deferred/Rejected**: not planned; **Undecided**: owner/evidence needed. Complexity is qualitative (L/M/H), not an estimate in days.

| ID | Feature / system | Player value | Deps | Complexity | Security / integrity | ₹0 load | Minimum acceptance | Class | Open decision |
|---|---|---|---|---|---|---|---|---|---|
| SYS-001 | Nation profile and identity | "This is my nation" | Auth; SYS-003 | L | Ownership checks | Low | Create, rename within policy, display emphasis | **FPB** | Nation-creation choice count |
| SYS-002 | Treasury and commitments | Plan without surprise | SYS-003; SYS-016 | M | SEC-010/011/014/016/025/031 | **High** | Available vs committed correct after every mutation; no negative balance | **FPB** | None |
| SYS-003 | Production, development, upkeep | Compounding stewardship | SYS-002; SYS-016 | M | SEC-010/013/016/025 | **High** | 12 boundaries produce deterministic, explainable deltas | **FPB** | ECOQ-002/005 |
| SYS-004 | Specialization and scarcity | Meaningful identity and trade | SYS-003; SYS-005 | M–H | SEC-010; R-15 | Low (derived) | Two-route floor holds for every class in a paper test | **FPB** | ECOQ-004 |
| SYS-005 | Directed trade | The multiplayer engine | SYS-002/004/008 | M | SEC-012/014/016/019; R-19 | **High** | Atomic pair; duplicate accept no-ops; refusal is free | **FPB** | Fresh-account caps |
| SYS-006 | One policy axis | Governance flavor | SYS-002/003 | L | SEC-010/012 | Low | One axis with a digest-explained effect and a cooldown | **FPB (optional)** | Axes; may cut |
| SYS-008 | Relationship records | "Where do I stand?" | SYS-009/013 | M | SEC-012; SDQ-004 | Medium | Pair state visible with history; edits recorded | **FPB** | Visibility policy |
| SYS-009 | Minimal treaties | Legible commitments | SYS-008/013 | M | SEC-012/014 | Medium | NAP enforces a block; promise records are visible and exitable | **FPB** | Type list |
| SYS-013 | Reputation registers | Standing by acts | SYS-008/009/015 | L–M | SEC-010; act integrity | Medium | Acts map to registers; no single hoardable score | **FPB** | Act taxonomy |
| SYS-015 | Chronicle | Shared memory | SYS-016/017 | L–M | SEC-010; no free text | Medium (storage) | Notable events appear once, with a quality bar | **FPB** | Entry taxonomy |
| SYS-016 | Turn engine | The world's beat | All | M (design) / H (integrity) | SEC-018…021 | **Critical** | 12 turns/day; duplicate no-op; forward-only resume | **FPB** | SDQ-018; PV-01…03 |
| SYS-017 | Digest and re-entry | The world explains itself | SYS-016/015 | M | No private leakage; scoping | Medium (reads) | Every delta has provenance; re-entry answers four questions | **FPB** | Retention (SDQ-017) |
| SYS-018 | Onboarding and first decision | First-session success | SYS-001/003/017 | L–M | First-decision integrity | Low | One real decision; glossary in place; no tutorial dump | **FPB** | Content; PXO-007 thresholds |
| SYS-010 | Minimal alliances | Collective play | SYS-002/005/009 | M | SEC-012/027; TH-021 | Medium | Roles documented; pool draws audited; succession rule | **Launch** | SDQ-012/013 |
| SYS-014 | Rankings and objectives | Comparative visibility | SYS-013/015 | L | Read-only scoping | Low | Per-register views only; no single ladder | **Later** | Whether needed at all |
| SYS-007 | Research programs | Long-arc capability | SYS-002/003 | M | SEC-010 | Low | 2–4 programs; completion at boundary; no tree | **Later** | Whether FPB ships zero |
| SYS-011 | Readiness posture | Deterrence floor | SYS-002/003 | M | SEC-010/013 | Low | Readiness upkeep and public posture; no combat | **Later** (or scripted) | Ties to D-004 |
| SYS-012 | Campaigns and settlements | Bounded conflict | SYS-008/009/011 | H | SEC-012/019/020; TH-022 | Unknown | Full rules, protection states, settlement enforcement | **Later** (war stage) | D-004; whole rule set |
| — | Listings market | Price discovery, offline trade | SYS-005; G-1…G-6 | H | R-14/R-15; SEC-016 | High | Gate conditions met and measured | **Later** | ECOQ-006 |
| FO-022 | Contracts/escrow | Conditional deals | SYS-005 | H | Settlement, disputes | High | Not before market | **Deferred** | Revisit with alliance supply |
| FO-021 | Consumer/prestige goods | Demand depth | SYS-003/006 | M | Low | Medium | Only if a real input need appears | **Deferred** | ECON-023 trigger |
| FO-019/020/023 | Seasons, authored events, espionage | Variety | — | H | High (authorship, hidden info) | High | — | **Deferred/Rejected** | Keep rejected |
| — | Map, cities, population | Genre familiarity | — | H | — | High | — | **Rejected** | Identity decision |
| SEC-B1 | Account security stack | Account safety | SEC-001…008 | M | TH-001/002/014 | Low cash, high care | Memory-hard hashes, sessions, recovery, rate limits | **Launch** | OSQ-002/003 |
| SEC-B2 | Abuse-control tuning | Fair play | SEC-023 | M | R-01/R-13 | Low | Caps live, false-positive review path | **Launch** | OSQ-001 |
| SEC-B3 | Moderation machinery | Trust | SEC-026…028 | M | TH-016 | People cost | Logged ladder, appeal path, disclosed hours | **Launch** | OSQ-005 |
| SEC-B4 | Backup and restore drill | Recovery | SEC-030 | M | TH-023 | Medium | Restore executed and verified once | **Launch** | OSQ-007 |
| SEC-B6 | Monitoring rail | Ops | SEC-033 | L | TH-012 | Low | Budget gauges and a working alert | **Launch** | Retention |
| REQ-039 | E-mail verification | Recovery anchor | Provider | L | TH-013 | **Conditional** | Either verified or explicitly unverified with throttles | **Launch** | OSQ-003 |

### 11.4 What is deliberately *not* in the FPB, and why

| Excluded | Reason | What would change the decision |
|---|---|---|
| Listings market | Integrity cost exceeds the value at small population; G-1…G-6 unmet | Observed directed-trade liquidity and a measured write budget |
| Full alliances | Permission/succession rules absent; shared pool is a liability without them | SDQ-012/013 answered and tested |
| War | No rules; largest design surface; TH-022 blocked | Dedicated war stage |
| Research tree | Capability unlocks multiply balance surface | Post-FPB retention evidence |
| Chat/private messages | Moderation and privacy cost; no design | A moderation capacity plan |
| Public API/automation | Abuse surface; OSQ-004 unset | An owner policy with enforcement |
| Map/cities/population | Contradicts the mapless identity and the small-data design | A deliberate concept change |

### 11.5 Scope-inflation guard

The following are **not** FPB requirements even though they appear in reports: a full UI design system, mobile-native clients, localization, accessibility certification, public API, tournaments, seasons, leaderboards, achievements, player-authored content, and a marketing site. They may be valuable later; including them now would make the FPB unbuildable and the ₹0 claim untestable.

---

## Section 12 — Requirements traceability matrix

### 12.1 How to read the matrix

39 integrated requirements (**REQ-001…REQ-039**) are defined here because the project has no single cross-cutting requirement register. Each REQ **inherits** its substance from the cited report and IDs; it does not replace them. The new prefix was checked against every existing family (§16) and is unused. A REQ does **not** carry approval: `Status` is the design status, and `Owner?` says whether an owner decision is needed before the requirement can be treated as fixed.

Priority: **P0** = required for a responsible FPB plan; **P1** = required before public launch; **P2** = later. `Status`: Proposed (design exists, unapproved), Open (decision missing), Gap (no design yet), Deferred. To keep the 39-row table readable, the prompt's fields map as follows: *player/operational purpose* is the requirement's stated outcome; *dependencies* are the systems column plus the preconditions; *evidence/open question* is the status plus the owning entry in §15. Nothing is omitted — it is distributed across those columns.

### 12.2 The matrix

| ID | Requirement and required behaviour | Source → inherited IDs | Systems | Preconditions → acceptance criteria | Pri | Threat / integrity | ₹0 dependency | Validation | Status | Owner? |
|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | The game must present a repeatable loop: observe, decide, commit, boundary, digest, revise, with no action requiring presence | P6 §4A/§24D; P4 §9 → DP-002, PXO-002/003 | All | A session can end after one decision → a tester completes a turn cycle without help | P0 | Churn if loop is opaque | None | CV-001/002; PV-14 (usability) | Proposed | No |
| REQ-002 | Each nation has exactly one owning account; ownership is checked on every action | P8 §4.1 → SEC-001/012 | SYS-001 | Account exists → cross-account action is rejected and logged | P0 | TH-008 | Low | ST-006 | Proposed | No |
| REQ-003 | Account creation, session issuance, rotation, revocation, and recovery must follow SEC-001…008 | P8 §4 → SEC-001…008 | Auth | E-mail anchor → sessions expire absolutely and revoke on password change | P0 | TH-001/002 | E-mail quota | ST-013 | Proposed | OSQ-002/003 |
| REQ-004 | Every valuable verb must resolve the actor's nation and role server-side before mutation | P8 §5 → SEC-012 | All | Actor session → unauthorised verb returns a reason and changes nothing | P0 | TH-008/021 | Reads only | ST-006 | Proposed | No |
| REQ-005 | Treasury balances must conserve under C1–C4; no negative balance; commitments reserve before spend | P7 §6/§12 → ECON-001/019; SEC-025 | SYS-002 | A mutation sequence → ledger sum equals balance; negative attempt rejected | P0 | R-19; TH-006 | **High writes** | ECV-001/002; PV-04 | Proposed | No |
| REQ-006 | Material stocks must be typed, conserved, and never substituted silently | P7 §8 → ECON-006/011 | SYS-003/004 | Production and trade sequence → stock conservation holds per class | P0 | Duplication/minting | High writes | ECV-002 | Proposed | No |
| REQ-007 | Development levels and emphasis must resolve only at boundaries, with explainable output | P7 §7/§11 → ECON-002/017 | SYS-003 | Queued change → applies at declared boundary; digest explains | P0 | Hidden state change | High | ECV-003 | Proposed | ECOQ-005 |
| REQ-008 | Respecialization must be paid, distance-gated, boundary-effective, and never permanently lock a path | P7 §11 → ECON-017 | SYS-003 | Young and old nation cases → both can pivot; cost is visible | P1 | R-17 | Medium | ECV-005 | Proposed | ECOQ-004 |
| REQ-009 | Directed trades must validate both sides, settle atomically, and be idempotent | P7 §10 → ECON-013; R-19; SEC-014/016 | SYS-005 | Concurrent accepts → exactly one settlement; no partial | P0 | TH-003/004/007 | **High** | ST-004; PV-04 | Proposed | No |
| REQ-010 | A listings market may exist only after G-1…G-6 are met | P7 §10.4 → ECON-014/018 | SYS-005 | Gate evidence recorded → market enabled | P2 | R-14/15 | High | ECV-004 | Deferred | ECOQ-006 |
| REQ-011 | Domestic policy must expose at most two axes and stability must not become a success ladder | P6 SYS-006; P5 DIR-3 → FO-005; SDQ-005 | SYS-006 | One axis → effect visible in digest; no dominant pick | P1 | Degenerate best-pick | Low | CV-003 | Proposed | Axes; may cut |
| REQ-012 | Bilateral relationships must be typed, event-sourced, and visibility-scoped | P6 SYS-008 → FO-004; SDQ-004 | SYS-008 | Pair state → history visible to permitted viewers only | P1 | Privacy; manipulation | Medium | ST-006 | Proposed | SDQ-004 |
| REQ-013 | Alliances must have explicit roles, audited pool draws, and a succession rule before any pool exists | P6 SYS-010 → FO-007; SEC-012/027 | SYS-010 | Role matrix → unauthorised draw fails and is logged | P1 | TH-021 | Medium | ST-006/016 | Open | SDQ-012/013 |
| REQ-014 | Strategic orders may exist only with a war-stage rule set, protection states, and settlement enforcement | P6 §15 → FO-010/011; D-004 | SYS-011/012 | War rules approved → orders resolve deterministically | P2 | TH-022 | Unknown | ST-020 (dependent) | Deferred | D-004; war stage |
| REQ-015 | The world must resolve 12 turns/day at fixed UTC boundaries, with no live resolution | P6 §17; AI_CONTEXT §2 → SYS-016 | SYS-016 | 24h run → 12 completed turn records | P0 | TH-009/010 | **Critical** | PV-01 | Proposed | No |
| REQ-016 | Turn resolution must be exactly-once and forward-only under retry/abort | P8 §6 → SEC-019/020/021 | SYS-016 | Duplicate and abort injection → no double-apply, resume completes | P0 | TH-009/010 | **Critical** | ST-007/008/009; PV-03 | Proposed | No |
| REQ-017 | Boundary ordering must be specified in a deterministic, published catalog | P6 §17 → SDQ-018 | SYS-016 | Catalog exists → two runs of the same inputs produce identical state | P0 | Dispute/fairness | None (design) | PV-02 | **Open** | Yes |
| REQ-018 | Every write action must carry an idempotency key; duplicates must be safe | P8 §7 → SEC-014 | All writes | Same key twice → one effect, one record | P0 | TH-003/004 | **High** | ST-004 | Proposed | No |
| REQ-019 | All valuable state must be server-authoritative; clients send intent, never outcomes | P8 §5.1 → SEC-010/011 | All | Forged client payload → server ignores claimed values | P0 | TH-006/007 | Low (design) | ST-005 | Proposed | No |
| REQ-020 | Every resolved delta must be visible with provenance; failures must explain and release reservations | P7 §15; P8 §5 → DP-004; SYS-017 | SYS-017 | A failed order → digest line with cause and release | P0 | Trust/churn | Reads | PV-14 | Proposed | No |
| REQ-021 | Player-visible history must be append-only; corrections are new disclosed events | P8 §14.4/§14.5 → SEC-031 | SYS-015 | A correction → original remains, new event references it | P1 | TH-023/024 | Medium | ST-018 | Proposed | No |
| REQ-022 | Absence must produce a re-entry summary; no decay and no attendance requirement | P4 §9 item 8; FO-015 → DP-002 | SYS-017 | 7-day absence → summary answers what/so-what/now/wait | P1 | Retention/churn | Reads | CV-004 | Proposed | FO-018 |
| REQ-023 | Collect only the data inventory's categories; no analytics, ads, precise location, or content logging | P8 §11 → SEC-032 | All | Inventory review → every stored field has a purpose | P0 | Privacy/legal | Low | Document review | Proposed | OSQ-010 |
| REQ-024 | Retention and deletion must be defined per category, with backup caveat disclosed | P8 §4.8/§11 → SEC-032 | All | Deletion request → account data removed/anonymised; backup window stated | P0 | Privacy | **Storage cap** | Document review; PV-05 | Open | OSQ-007/010 |
| REQ-025 | Moderation must be evidence-based, logged, proportionate, and role-scoped | P8 §12 → SEC-026/027/028 | Ops | A sanction → case record, reason, appeal path | P1 | TH-016/017 | People cost | ST-016 | Proposed | OSQ-005 |
| REQ-026 | Appeals must be possible and decided with a reason; overturns reviewed | P8 §12.2 → SEC-026 | Ops | Appeal filed → decision recorded | P1 | Trust | People cost | ST-016 | Proposed | OSQ-005/012 |
| REQ-027 | A permanent audit spine must record every value mutation, pipeline phase, privileged act, and moderation act; "permanent" = hot + archived per §17.5 | P8 §13 → SEC-031 | All | Mutation → row with actor/turn/cause/result; retention/export per §17.5 | P0 | TH-009/017 | **Critical storage** | PV-05 | Proposed | Retention |
| REQ-028 | Backups must exist, be restorable, and be verified by a drill; RPO/RTO disclosed | P8 §14.2 → SEC-030 | Ops | A restore drill → verified state, disclosed outcome | P1 | TH-023 | **Conditional** | PV-08 | Open | OSQ-007 |
| REQ-029 | Incidents must have severity classes, disclosure, compensation rules, and a post-review | P8 §14 → SEC-022/030 | Ops | A simulated Sev-2 → announced delay, review filed | P1 | Trust | People cost | ST-019 | Proposed | No |
| REQ-030 | Per-class quotas and rate limits must protect the turn budget from abuse | P8 §9 → SEC-029 | Edge/Worker | Abuse burst → throttled with an honest reason; resolver budget reserved | P0 | TH-012 | **Negative net** | ST-014 | Proposed | No |
| REQ-031 | Multi-account and collusion policy must be declared and enforced behaviourally, with appeals | P8 §8 → SEC-023/024; OSQ-001 | All | Policy published → caps and review path live | P0 | R-01/R-13 | Low | ST-016 | **Open** | Yes |
| REQ-032 | The frontend must be served from a free static host with a public URL and TLS | P1 §6; D-005 | Web | Deploy → HTTPS page loads without a paid plan | P0 | — | Verified free (Pages) | PV-09 | Proposed | D-005 |
| REQ-033 | The backend must run on a free execution tier with server-side authority | P1 §6; D-005 | Worker | Deploy → API responds within free limits | P0 | — | **Critical** | PV-01/06 | Proposed | D-005 |
| REQ-034 | Persistent state must fit the free database's size and write limits, or retention must be redesigned | P7 §16; P8 §13 → D-005; SDQ-003 | D1 | Load model → size and writes measured | P0 | Data loss | **Critical** | PV-04/05 | **Open** | Yes |
| REQ-035 | Twelve scheduled turns/day must run within the free scheduler's CPU/subrequest limits | P6 §17; P7 §16.4 | Cron | 24h run → 12 turns, within limits | P0 | TH-009/010 | **Critical** | PV-01/02/03 | **Open** | D-005 |
| REQ-036 | The stack must not create automatic charges or require a paid plan | §17.1; D-005 | All | Provider config review → no payment method, no overage | P0 | Cost | **Core objective** | PV-09 | Proposed | Yes |
| REQ-037 | The project must be able to export and migrate its data without paid infrastructure | §17.8 | All | Export → restorable elsewhere | P1 | Lock-in | Medium | PV-12 | Proposed | No |
| REQ-038 | Onboarding must deliver one real decision and teach the mapless model in context | P5 §15; PXO-004; FO-001 | SYS-018 | New tester → completes first decision, explains the world | P0 | Churn | Low | CV-001/002 | Proposed | Content |
| REQ-039 | E-mail verification/recovery must be either implemented within free caps or explicitly waived with compensating controls | P8 §4.1 → SEC-001/004; OSQ-003 | Auth | Signup → verification or documented waiver; recovery works | P1 | TH-013/014 | **Conditional (100–300/day)** | PV-10 | Open | Yes |

### 12.3 Traceability status

| Measure | Count | Note |
|---|---|---|
| Requirements defined | 39 | REQ-001…039 |
| With a named source and inherited IDs | 39 | No orphan requirement |
| With an acceptance criterion | 39 | Some criteria are document-level (e.g., REQ-023) |
| With a planned validation | 39 | PV/ST/ECV or document review |
| With an executed validation | **0** | No test has run |
| Blocked on an owner decision | 8 | REQ-017, 024, 028, 031, 034, 035, 036, 039 |
| Blocked on a missing design | 3 | REQ-013, 014, 017 |
| Deferred | 2 | REQ-010, 014 |

**This is not exhaustive traceability.** It is a *practical* matrix: every P0 requirement has a source, a system, a criterion, and a validation path. The source reports contain finer-grained requirements (SEC/ECON/ST) that this matrix deliberately does not duplicate; §16 records where each register lives.

---

## Section 13 — Acceptance criteria and validation plan

### 13.1 What already exists, and what has run

| Family | Owner | Scope | Entries | Executed |
|---|---|---|---|---|
| **V-1…V-10** | P4 §19 | Audience, session shape, absence, transparency, cadence framing, launch seeding | 10 | **0** |
| **CV-001…CV-006** | P5 §17 | Pitch resonance, mapless comprehension, plural paths, cadence, success framing, digest trust | 6 | **0** |
| **ECV-001…ECV-005** | P7 §22.5 | Economy accounting, trade sessions, respecialization/failure sweep | 5 | **0** |
| **ST-001…ST-020** | P8 §19.2 | Auth/recovery, request integrity, turn idempotency/partial failure, abuse funnels, recovery drills | 20 | **0** |
| **PV-01…PV-15** | This report | Free-tier capacity, quota behaviour, backup/export, auth hashing, monitoring, first-session usability | 15 | **0** |

**No validation of any kind has been executed.** The tables below are plans. Any statement elsewhere in the project that treats a V/CV/ECV/ST result as known is a defect; none was found in this pass.

### 13.2 Functional, economy, turn, and experience validation

| Test | Requirements | Preconditions | What it does | Expected / pass | Pri | Deps | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| **CV-001** pitch resonance | REQ-001/038 | Written pitch; 5–10 target players | Structured feedback on the one-paragraph concept | ≥3 describe an imagined session matching CX-5 | P0 | None | Planned | None |
| **CV-002** mapless comprehension | REQ-001/038 | Two national cards + register excerpt | Explain-back exercise | Participants describe inter-nation dynamics without reaching for a map | P0 | None | Planned | None |
| **CV-003** plural paths | REQ-008/011 | Two fictional nation strategies | "Which wins?" | Participants accept different success types | P1 | Numeric sketch | Planned | None |
| **CV-004** cadence framing | REQ-001/015/022 | One mock day in three sessions | Reaction to 2h/12-per-day framing | "Fits my day"; no punishment expectation | P0 | None | Planned | None |
| **CV-005** success framing | REQ-001 | Two one-sentence framings | A/B preference | Consistent preference or accepted plurality | P1 | None | Planned | None |
| **CV-006** digest trust | REQ-020 | Realistic sample digest | Trust/confusion probe | Trust signals; no "need a wiki" | P0 | Digest mock | Planned | None |
| **V-2** session sufficiency | REQ-001/038 | Three session plans; clickable mock | 5–15 minute session test | ≥1 meaningful decision + visible change | **P0** | Mock | Planned | None |
| **V-4** transparency boundary | REQ-020 | Transparent vs opaque digest variants | A/B | Transparency preferred without killing strategema | P1 | Digest mock | Planned | None |
| **ECV-001/002** conservation | REQ-005/006 | Seeded paper economy | Accounting identity over N turns | Δsupply = C1 − C3; no class imbalance | P0 | EX-1 parameters | Planned | None |
| **ECV-003** respec path | REQ-007/008 | Young and old nation cases | Paper/table simulation | Both can pivot; cost bounded; no permanent lock | P1 | ECOQ-004 draft | Planned | None |
| **ECV-004** directed trade session | REQ-009/018/031 | 2–4 testers on a supervised build | Real offers/accepts, duplicate and race attempts | Atomic settlement; no double; refusal free | P0 | CP | Planned | None |
| **ECV-005** failure sweep | REQ-005/007/008 | Paper economy | Austerity, insolvency, respec failure cases | No state leaves a nation unable to act | P1 | ECOQ-002 draft | Planned | None |
| **ST-004** duplicate/race | REQ-009/018 | Instrumented endpoint | Replay accepted trade/order | One effect, one record | P0 | Build | Planned | None |
| **ST-005** forged payload | REQ-019 | Instrumented endpoint | Client claims outcome | Server recomputes; claim ignored | P0 | Build | Planned | None |
| **ST-006** cross-account/role scan | REQ-002/004/013 | Two accounts, role matrix | Swap IDs/roles across every verb | All denied unless authorised | P0 | Build | Planned | None |
| **ST-007/008/009** turn integrity | REQ-015/016/018 | Instrumented resolver | Duplicate run, abort mid-phase, restore drill | No double-apply; forward resume; verified restore | P0 | Build; PV-03 | Planned | None |
| **ST-013** account takeover | REQ-003 | Auth stack | Stuffing/recovery abuse | Rate-limited; sessions revoke; no enumeration | P1 | B1 | Planned | None |
| **ST-014** abuse burst | REQ-030 | Quota instrumentation | Flood one class | Throttled; resolver budget preserved | P0 | Build | Planned | None |
| **ST-016** funnelling/moderation | REQ-025/031 | Two linked accounts | Multi-account funnel; report flow | Surfaced for review; logged; appeal path | P1 | B2/B3 | Planned | None |
| **ST-018** correction/restore history | REQ-021 | Seeded history | Force a correction | Original retained; new disclosed event | P1 | Build | Planned | None |
| **ST-019** incident drill | REQ-029 | Simulated Sev-2 | Announce, recover, review | Player-visible notice; review filed | P1 | Ops runbook | Planned | None |

### 13.3 Free-tier capacity and recovery validation (new)

| Test | Requirements | Preconditions | What it does | Pass criteria | Pri | Deps | Status |
|---|---|---|---|---|---|---|---|
| **PV-01** twelve turns/day | REQ-015/035 | Deployed free Worker + cron | Run 24h with a synthetic world | 12 turn records; no missed boundary; no manual intervention | **P0** | PV-02 dataset | Planned |
| **PV-02** boundary scaling | REQ-015/033/035 | Synthetic N = 50/250/1,000 | Resolve one boundary per N | Completes within CPU/subrequest limits; record actuals | **P0** | Dataset generator | Planned |
| **PV-03** duplicate/abort/delay | REQ-016/018 | Instrumented resolver | Inject duplicate, mid-phase abort, delayed trigger | Duplicate no-ops; resume is forward-only; delay is announced | **P0** | PV-02 | Planned |
| **PV-04** D1 write budget | REQ-005/009/034 | 24h simulated activity at N = 300/1,000 | Count rows written, including audit and index effects | Within 100k/day or documented overflow | **P0** | PV-02 | Planned |
| **PV-05** storage growth/retention | REQ-024/027/034 | 90 days of synthetic history | Measure bytes per row and growth; run retention/export | Stays under 500 MB with retention; export restores | **P0** | PV-04 | Planned |
| **PV-06** request ceiling | REQ-033 | Simulated 40–60 requests/player/day | Drive N players | Within 100k requests/day; identify the first ceiling | P0 | PV-02 | Planned |
| **PV-07** quota exhaustion | REQ-034/036 | Artificially hit write/request cap | Observe behaviour | Writes fail safely; no corruption; players see an honest error | **P0** | PV-04 | Planned |
| **PV-08** backup/restore | REQ-028 | Time Travel window + export | Restore to T−1; verify | State coherent; no double-settled trades; RPO/RTO recorded | P1 | Real data | Planned |
| **PV-09** free-only audit | REQ-032/036 | Provider accounts | Review plan, payment method, overage, TLS, asset hosting | No paid plan; no charge trigger; HTTPS works | **P0** | Deployment | Planned |
| **PV-10** e-mail throughput | REQ-003/039 | Free e-mail account | Send verification/recovery at expected signup rate | Within daily cap; bounce handling; fallback documented | P1 | OSQ-003 | Planned |
| **PV-11** monitoring | REQ-029/030 | Free logs + D1 gauges + uptime monitor | Trigger a budget alert and an outage | Alert arrives; gauge accurate; no paid tier | P1 | PV-04 | Planned |
| **PV-12** provider exit | REQ-037 | Export tooling | Dump, rebuild elsewhere, restore | Data complete; app runs without source provider | P1 | Schema | Planned |
| **PV-13** moderation capacity | REQ-025/026 | Seeded cases | Time-box a simulated queue with one operator | Documented response time; no case silently dropped | P2 | B3 | Planned |
| **PV-14** first-session usability | REQ-001/038 | CP or FPB | 5 testers, unmoderated | ≥4 complete first decision; explain the world | P0 | CP | Planned |
| **PV-15** auth hashing CPU | REQ-003/039 | Free Worker + auth library | Register/login with Argon2id/WASM and with Web Crypto PBKDF2 | Measured CPU/latency; the chosen KDF fits free limits without weakening policy | P0 | PV-09 | Planned |

### 13.4 What must be tested before implementation, and what needs players

| Question | Paper/simulation is enough | Needs a running build | Needs real players |
|---|---|---|---|
| Economy conservation | Yes (ECV-001/002) | Confirmation only | No |
| Balance curves | **No** (simulation needed) | Yes | Eventually |
| Turn idempotency | No | Yes (PV-03) | No |
| Free-tier capacity | No | Yes (PV-01…07) | No |
| Mapless comprehension | Partly | Yes (CP) | Yes (CV-002) |
| Session sufficiency | Mock (V-2) | Yes | Yes |
| Abuse funnels | No | Yes | Yes (ST-016) |
| Retention | No | No | Yes (longitudinal) |
| Moderation load | No | Partly | Yes |

**The single most important sentence in this section:** no amount of paper analysis can prove that a 10 ms cron invocation can resolve a boundary, or that a 500 MB database can hold a persistent world's history. Those are measurements (PV-02/PV-05), and they must precede architecture commitment.

---

## Section 14 — Contradictions, ambiguities, and design gaps

### 14.1 Method

Every report was checked for: conflicting rules, duplicate/incompatible identifiers, undefined references, stale continuity, conflicting scope boundaries, conflicting turn assumptions, security requirements without tests (and vice versa), free-tier claims without evidence, and recommendations recorded as approvals. Findings were kept only if a reader could point to a specific section. Cosmetic wording was ignored.

### 14.2 Defect register

| ID | Severity | Source (file / section) | Description | Impact | Affected | Recommended correction | Blocks Stage 1? | Blocks FPB? | Blocks ₹0? | Next action | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **DEF-001** | **High** | P5 §15A/§15C; P6 §24; P7 §19; P8 §17.1 | "First playable" denotes a concept test that excludes auth/integrity and a real build that requires them | Build plan would either over-build the CP or under-secure the FPB | SYS-018, SYS-016, auth, all | Adopt CP/FPB taxonomy (§11.1) | No | **Yes** | Indirectly | OD-02 | **Open** |
| **DEF-002** | **High** | P6 §24A vs §24 tier list; P5 §15A E5; P7 §19.1 | P6 lists SYS-005 as core but its Tier-A boot excludes it; P5's CP and P7's FPB both require trade | A build following Tier A would fail the CP's own E5 and the FPB's trade requirement | SYS-005, SYS-002, SYS-016 | Add SYS-005 (directed) to the FPB build set; re-tier explicitly | No | **Yes** | No | OD-02 | **Open** |
| **DEF-003** | Medium | P4 §19 (V-2 P0); P5 §17; P6 §24G | Validation gates declared as pre-conditions were not executed before P5–P8 proceeded | Design confidence on session shape and concept resonance is unverified; later reports assume them | CV-001/002/004, V-2 | Record as accepted condition; execute V-2/CV before FPB design freeze | **Conditional** | No (condition) | No | PV-14; CV | **Accepted condition** |
| **DEF-004** | Medium | P8 §15.4 vs §1.4 | "16 requirements on stage A" but 12 are named; the stage table and A-list say 12 | Staging count cannot be used for planning | SEC-010…029 | Restate as 12 | No | No | No | P8 correction | **Fixed 2026-10-23** — P8 §15.4 now reads 12; §22.2 item 6 and §25.7 record it |
| **DEF-005** | Medium | P8 §1.4, §17.1 A8 | A8 adds "SEC-031's spine rows" to Stage A while the stage table counts the full audit spine under Stage B; the subset is not reflected in the counts | Audit-row build order is ambiguous at the margin | SEC-031 | State "12 + audit-spine subset of SEC-031" | No | No | No | P8 correction | **Fixed 2026-10-23** — A8 states the subset; §16.2's SEC-031 stage cell and §17.1's count note agree; 12/11/9 = 32 |
| **DEF-006** | Medium | P7 §16.3 vs P8 §13.2/§15 | Write estimate omits audit rows, auth/session writes, rate-limit counters, and possible index amplification | "~3,000 nations" is an upper bound; planning figure ~1,100–2,000 | SYS-016, D1, audit | Use revised range; measure with PV-04 | No | No | **Yes** (estimate) | PV-04 | **Open** |
| **DEF-007** | Low | P3 §7.7 | Cited undefined O-15/16/17 and mislabelled O-12 | Broken identifiers | FO-012/015/016/017 | Rewritten to FO IDs | No | No | No | Applied 2026-10-23 | **Fixed** |
| **DEF-008** | Low | P2 §9 (register); range claim repeated in AI_CONTEXT §5, P3 §2, P4 §2, P6 §SR-2 | The F register defines 28 entries in the range F-001…F-029: F-007 and F-028 are unassigned and F-003b is a sub-ID, but no source declared the gaps | Downstream range statements read as if all 29 numbers were issued; a reader hunting F-007/F-028 finds nothing | F register; P9 §16.2 | Declare the range's gaps in P2 §9; do **not** renumber or invent findings | No | No | No | P2 declaration | **Fixed 2026-10-23** — P2 §9 states 28 defined entries, F-007/F-028 unassigned, F-003b a deliberate sub-ID; nothing renumbered |
| **DEF-009** | Low | P1 §7.1; P3 §7.7 | O-register is O-1…O-12; O-13/14 absent; O-15/16/17 were referenced elsewhere | Historical numbering gap | O register | Declare reserved/retired | No | No | No | §16 records it | **Declared** |
| **DEF-010** | Low | P8 TH-011 vs §17.3 C2 | TH-011's named mitigation is SEC-015 (Stage C); the Stage-A prevention is the timing contract plus A9 disclosure, but the residual is not stated that way | Mitigation appears deferred | SEC-015/018/020 | Add the residual note; SEC-015 is refinement | No | No | No | P8 correction | **Fixed 2026-10-23** — TH-011 now names SEC-018/020 + A9 as Stage-A prevention, SEC-015 as refinement, and states the accepted transparency residual |
| **DEF-011** | Medium | P7 §22.3; §§7–12 | No numeric economy parameters exist | FPB cannot be balanced; structure is testable | ECON/ECOQ | Dedicated numbers stage | No (by design) | **Yes** | No | §19 stage 4 | **By design** |
| **DEF-012** | Medium | P5 §11/§15B; P6 §15; P8 TH-022 | No war rules; conflict pillar is concept only | War cannot be built or tested | SYS-011/012 | Dedicated war stage | No (by design) | No (war is Later) | No | §19 stage 5 | **By design** |
| **DEF-013** | Low | P6 §5.1; P8 registers | No SYS IDs for auth, moderation, audit, backups | Traceability gap, not missing design | REQ-003/025/027/028 | Map to REQ IDs; do not invent SYS IDs | No | No | No | §5.5 | **Declared** |
| **DEF-014** | Low | P8 §15.1/§15.4 | P8 inherits the 10 ms cron figure from P7 rather than re-verifying it | Weak evidence chain (figure is correct per P7's dated read) | SYS-016 | Re-verified in §17.3; record the chain | No | No | No | PV-02 | **Resolved in P9** |
| **DEF-015** | Medium | P8 §4.2 vs Workers 10 ms CPU | Password hashing is called "negligible"; Argon2id on Workers requires WASM and its CPU fit is unmeasured; Web Crypto PBKDF2 is native but not memory-hard | Auth may not fit the free tier, or may be weakened without analysis | SEC-002; ZD-05 | Benchmark both (PV-15); record the KDF choice as architecture | No | No | **Yes** (auth path) | TQ-17; PV-15 | **Open** |
| **DEF-016** | Low | P7 §14.1 and §19.3 vs §11.3/§19.3 ECON-017 | Emphasis change is labelled "Immediate-with-record / effective on submit" in two places, while §11.3 and ECON-017 say the weights apply at the next boundary | A reader could implement instant re-weighting, breaking the timing contract and R-17's countermeasure | ECON-017; SYS-016; REQ-007 | Align both rows to "immediate record, effect at next boundary" | No | No | No | P7 correction | **Fixed 2026-10-23** — §14.1 and §19.3 corrected; §26.2 records it |
| **DEF-017** | Low | P7 §15.2 | The finance-view list names "interest on reserve", contradicting §6.6/ECON-020's no-interest-anywhere rule | A designer could implement a reserve yield | ECON-001/019/020 | Remove the label; state no reserve interest | No | No | No | P7 correction | **Fixed 2026-10-23** — §15.2 now names production/settlements/disclosed adjustments and says no reserve interest |
| **DEF-018** | Medium | P7 §10.2 vs §14.1 | Offer reservation is self-contradictory: §10.2 says the proposer "reserves nothing until acceptance" and that a pending offer "does freeze" funds; §14.1 says no reservation until acceptance. The draft also says a "reserved-at-submit model" was chosen | Trade implementation cannot know whether pending offers lock funds; double-spend vs offer-honesty behaviour is undefined | ECON-013; SYS-005; REQ-009 | **Preserve as an explicit open conflict**, not a preference call: state both readings, fix atomic acceptance, and require an economy-stage decision before trade build | No | **Yes** (trade details) | No | Economy stage (OD-03 context) | **Open — ambiguity preserved**; P7 §10.2 records it | 

### 14.3 What is *not* a defect

| Candidate | Why it is not a defect |
|---|---|
| SEC-009 is missing | Deliberately reserved; 32 defined requirements are contiguous around it (§16) |
| 18 systems vs 22 task areas | P6 consolidated by exclusion, not ID-merging; the four removed areas are documented |
| Economy has no numbers | Deliberate; the report says so and routes numerics to ECOQ |
| Market is deferred | Gated, not forgotten (ECON-014/018) |
| Alliances are Tier C | Optional by design (AP-004); not a contradiction |
| No chat system | Explicitly out of scope; private messages would add moderation/privacy cost |
| Reports' self-declared QA success | Treated as claims; this report re-read the files rather than trusting them |

### 14.4 Ambiguities that are being preserved, not resolved

1. **What a treaty *does*** beyond the NAP analogue (SDQ-014).
2. **Whether trade terms are public** (SDQ-004).
3. **What stability multiplies** (SDQ-005).
4. **Whether the FPB includes alliances** (P6 Tier C vs P8 TH-021).
5. **How a delayed turn is announced and compensated** (SEC-022; P8 §14.6).
6. **Whether e-mail is verified at launch** (OSQ-003).
7. **Whether multi-accounting is prohibited or merely capped** (OSQ-001).

Each is recorded with an owner and a consequence in §15. None is resolved by preference.

---

## Section 15 — Consolidated open questions and owner decisions

### 15.1 First, the decisions that already exist

| ID | Decision | Status (verified in DECISIONS.md, 2026-10-23) | What it means for this synthesis |
|---|---|---|---|
| D-001 | Continuity-system locations | **Confirmed** | This report uses the four files and `docs/stage-1/` as recorded |
| D-002 | Stage-1 pacing; explicit authorization per prompt | **Confirmed** | Prompt 9 was explicitly authorized by the owner's brief; no other prompt is authorized by this report |
| D-003 | Findings/opportunities are inputs, never approved mechanics | **Confirmed** | Every P5–P8 proposal remains unapproved; this report adds no approvals |
| D-004 | Operations Points (OP) | **Provisional** | OP is not designed, valued, or approved; war-stage input only |
| D-005 | Cloudflare Workers + D1 as candidates | **Provisional** | §17 evaluates them as candidates; it does **not** select them |
| D-006 | FO register is inputs-only | **Provisional** | FO statuses are reused, not advanced |

**DECISIONS.md was inspected and left unchanged.** No entry was added, altered, or removed. The ₹0 objective is recorded as an owner-stated constraint in AI_CONTEXT §2 (with attribution to this brief); it is not a DECISIONS entry because this pass was instructed not to manufacture approvals and the brief frames ₹0 as an existing constraint to preserve.

### 15.2 Owner decision register (new)

These are **OD-01…OD-12**. None is decided here. Each recommendation is advisory.

| ID | Question | Options (benefit / disadvantage) | Recommendation and rationale | Security impact | Player-experience impact | Cost / ops impact | Evidence needed | Status | Consequence of delay |
|---|---|---|---|---|---|---|---|---|---|
| **OD-01** | What happens when a free-tier limit is reached? | (a) Hard caps + graceful degradation + pause signups (free, predictable; growth stops) (b) Allow overflow into a paid plan (never blocked; violates ₹0) (c) Suspend the world (free; destroys trust) | **(a)** — it is the only option consistent with the ₹0 constraint and with honest failure (DP-004) | Writes fail safely; no corruption; degraded mode must be designed | Players see an honest "world at capacity" state, not silent loss | No charge; requires quota gauges and a capacity runbook | PV-04/06/07; provider enforcement behaviour | **Open** | Architecture may assume infinite headroom; launch could fail unexpectedly |
| **OD-02** | What is the FPB, precisely? | (a) CP/FPB taxonomy with CP supervised and FPB scoped as §11.2 (clear; two artifacts to manage) (b) One big "first playable" (simple label; either over-secured CP or under-secured FPB) (c) Skip CP, build FPB (fastest to real players; highest rework risk) | **(a)** — resolves DEF-001/002 without weakening P8's integrity baseline | CP still requires Stage-A integrity; FPB requires the full set | CP tests comprehension cheaply; FPB tests the real loop | CP is cheap; FPB is the real cost | V-2/CV-002; owner scope call | **Open** | Every build plan is ambiguous; estimates unreliable |
| **OD-03** | Is directed trade in the FPB? | (a) Yes, fee-free, atomic (concept engine; adds writes) (b) No, economy-only FPB (cheaper; fails P5 E5 and P7's model) | **(a)** — without trade the concept's interdependence claim is untested | Requires SEC-014/016 and R-19 | First trade is the multiplayer "aha" | +4 writes/trade; manageable at small N | ECV-004 | **Open** (tied to OD-02) | FPB ships without its own core loop |
| **OD-04** | Is the listings market deferred? | (a) Defer behind G-1…G-6 (safe; loses price discovery) (b) Build a simple board early (fast; imports manipulation surface) | **(a)** — the gate exists precisely because the integrity cost is high | Avoids R-14/15 at launch | Directed trade remains legible | Avoids large write/storage load | ECOQ-006 | **Open** | Scope creep and a premature abuse surface |
| **OD-05** | What is the multi-account policy? | (a) One account per person, behaviourally enforced (clear; harder to police) (b) Multi-account allowed with caps (lenient; funnelling risk) (c) No policy (cheapest; unfair) | **(a)** with appeals — matches SEC-023 and genre expectations; enforcement is behavioural, not identity-based | Core anti-funnel control | Honest players unaffected; alt-abusers face review | Moderation load | OSQ-001; ST-016 | **Open** | Trade caps and sanctions lack a stated basis |
| **OD-06** | What recovery tier is acceptable at ₹0? | (a) Time Travel 7d + daily export + quarterly drill (free; RPO ≤24h, manual RTO) (b) Paid backups (stronger; violates ₹0) (c) No backups (free; Sev-1 risk) | **(a)** — meets SEC-030's intent with disclosed limits; (c) is unacceptable | Restore discipline is a launch gate | A loss event is recoverable within a day | Manual export is operator time; no cash | PV-08; OSQ-007 | **Open** | Launch without a tested restore path |
| **OD-07** | Is e-mail verified at launch? | (a) Verify if within 100–300/day (stronger recovery; signup cap) (b) Unverified with throttles (higher signup throughput; weaker anchor) | **(a)** if the measured signup rate fits; otherwise (b) with a published caveat — decision depends on PV-10 | Verification is TH-013's main brake | Slight signup friction | E-mail quota is the binding limit | OSQ-003; PV-10 | **Open** | Recovery design and bot defence stay ambiguous |
| **OD-08** | Moderation staffing at launch? | (a) Single operator + disclosed hours + evidence-first process (honest; slow) (b) Recruit volunteer mods (faster; trust/COI risk) (c) No moderation (unacceptable) | **(a)** at launch, with (b) only after a written role/COI policy | Appeals and sanctions need a human | Response times are published, not implied | People time, no cash | OSQ-005/012 | **Open** | Moderation cannot be planned or promised |
| **OD-09** | What automation is allowed? | (a) No unattended automation; read-only tools tolerated (fair; enforcement burden) (b) Allow all automation (cheap; destroys turn fairness) (c) Case-by-case (ambiguous) | **(a)** — consistent with SEC-023 and the turn-locked design | Prevents bot-driven funnelling | Committed players can still plan offline | Detection effort | OSQ-004 | **Open** | Abuse policy and API surface undefined |
| **OD-10** | Are completed trade terms public? | (a) Parties only, aggregates later (private; less social proof) (b) Public terms (transparent; collusion/visibility risk) | **(a)** — privacy-by-default; SDQ-004 stays open for aggregates | Avoids leaking portfolios | Players can still build reputation via acts | Low | SDQ-004 | **Open** | Digest/profile scope blocked |
| **OD-11** | Is there any catch-up acceleration? | (a) None at launch; starting grant only (fair; newcomers may lag) (b) Soft catch-up (kind; farmable) | **(a)** at launch; FO-018 remains owner-held; ECON-012's five constraints bind any later design | Catch-up mechanics are a classic exploit | Newcomer experience may suffer (F-012) | Low | FO-018 | **Open** | Onboarding/first-week design cannot be finalized |
| **OD-12** | Authorize a war-design stage? | (a) Yes, as a separate stage after FPB (clear; later) (b) Fold war into FPB (too large) (c) Drop war (identity loss) | **(a)** — the conflict pillar needs its own stage; D-004 stays Provisional | War adds the largest threat surface (TH-022) | Delivers the strategist face | New design cost, not hosting cost | P6 §15; P8 TH-022 | **Open** | Conflict remains a promise; no testable war |

### 15.3 Questions requiring further research

| Question | Register | Why it needs research, not a decision | Blocks |
|---|---|---|---|
| Turn ordering and tiebreak catalog | SDQ-018 | Requires an engineering design plus measured boundary behaviour | FPB architecture |
| Database capacity and write amplification | SDQ-003 | Requires measurement (PV-04/05) | Deployment choice |
| Resource asymmetry and respec numerics | ECOQ-004 | Requires simulation and playtest | Economy build |
| Drain curves and austerity thresholds | ECOQ-002 | Requires simulation | Economy build |
| Threshold placement | ECOQ-005 | Requires progression simulation | Progression build |
| Market gate evidence | ECOQ-006 | Requires live directed-trade data | Market |
| Trade visibility effects | SDQ-004 | Requires player research and abuse analysis | Digest/profile |
| Free-tier e-mail throughput | OSQ-003 | Requires a measured send test (PV-10) | Auth/recovery |
| Provider terms and charge triggers | §17.7 | Requires a plan-by-plan review and a no-card test (PV-09) | ₹0 claim |

### 15.4 Questions that may remain open until later implementation planning

These do **not** block a responsible FPB plan: SDQ-001's numeric levels (structure settled), SDQ-002's post-playtest stress test, SDQ-005's final policy axes (one axis can ship), SDQ-006's research depth, SDQ-007's numeric thresholds (austerity family settled), SDQ-010's notification taxonomy (digest exists), SDQ-011's UI taxonomy, SDQ-012/013's full alliance governance (alliances are Launch), SDQ-014's full treaty types (NAP + two promises suffice), SDQ-015's trade-credit shape, SDQ-017's chronicle quality bar, ECOQ-006/010/011/012/013, and FO-018/019/020/021/022/023.

### 15.5 Questions that block a responsible implementation plan

SDQ-003, SDQ-004, SDQ-009, SDQ-016, SDQ-018; ECOQ-002/004/005; OD-01, OD-02, OD-06; PV-01…PV-07; **DEF-018's offer-reservation choice** (trade build); and the schema/authority decisions that follow from them. **A project that starts coding before these are answered is not implementing the research; it is bypassing it.**

### 15.6 Questions that prevent the ₹0 objective from being verified

PV-01 (12 turns/day), PV-02 (boundary CPU/subrequests), PV-04 (write budget), PV-05 (storage/retention), PV-06 (request ceiling), PV-07 (quota exhaustion), PV-09 (no charge trigger), PV-10 (e-mail throughput), and OD-01/OD-06. Until these are run, the correct statement is **"₹0 appears feasible at small scale, unverified."**

---

## Section 16 — Identifier and register reconciliation

### 16.1 Method

Registers were checked in their owning reports by counting entries and scanning tokens, not by trusting the reports' summaries. Counts below are the counts **observed in the saved files**; where a range has a gap, the gap is stated. No inherited ID was renumbered. The owning-report paths are the eight `docs/stage-1/0N_*.md` files listed in §2.1; the table cites the section rather than repeating each full path.

### 16.2 Register inventory

| Register | Path (owning report / section) | Entries observed | Reserved / retired / gaps | Used in P9? | Notes |
|---|---|---|---|---|---|
| **F** findings | P2 §9 (register + range note) | 28 | Range F-001…F-029 with **F-007 and F-028 unassigned — now declared in P2 §9 (2026-10-23)**; **F-003b** is a deliberate sub-ID | Yes | DEF-008 closed by the declaration; no number re-assigned or invented |
| **O** opportunities | P2 §8 | 12 defined (O-1…O-12) | **O-13/O-14 absent**; O-15…O-17 are not defined (see DEF-007/009) | Yes | P3's former O-15/16/17 citations corrected |
| **FO** feature opportunities | P3 §10 | 27 (FO-001…027) | None | Yes | Statuses reused, none advanced |
| **PXE** experience risks | P4 §17 | 19 | None | Yes (by reference) | |
| **PR** principles | P4 | 10 | None | Yes (by reference) | |
| **PXO** experience opportunities | P4 §16 | 22 | None | Yes | |
| **V** validations | P4 §19 | 10 | None | Yes | None executed |
| **CV** concept validations | P5 §17 | 6 | None | Yes | None executed |
| **CX / DP / UXD / AP / CCR / DIR / H / RC** | P5 | 5 / 6 / 5 / 8 / 12 / 6 / 6 / 5 | None | Yes (concept/pillars) | All provisional |
| **SYS** systems | P6 §5.1 | 18 | None | Yes | No new SYS IDs created; one cosmetic lowercase variant (`sys-010`) in P6 §9D is the same ID, not a new one |
| **INT** interactions | P6 §7.1 | 14 | None | Yes | |
| **SDQ** dependency questions | P6 §22.1 | 18 | P0 set: 001/002/003/004/009/010/016/018 | Yes | Several narrowed by P7, none closed |
| **SIM** simplifications | P6 §21 | 12 | None | Yes | Permanent postures |
| **MO** mechanics opportunities | P6 §23 | 8 | None | Yes | |
| **R** integrity risks | P6 §20 (R-01…12) + P7 §13 (R-13…21) | 21 | None | Yes | R-19 is a design invariant |
| **ECON** proposals | P7 §22.2 | 18 active | **Retired: 003, 004, 005, 007, 008** (documented, not recycled) | Yes | No renumbering |
| **ECOQ** questions | P7 §22.3 | 13 | None | Yes | 001–009 core; 010–013 later |
| **ECV** experiments | P7 §22.5 | 5 | None | Yes | None executed |
| **MAT** material classes | P7 §8 | 4 active | Fifth class deferred (ECON-023) | Yes | No MAT-05 ID assigned |
| **L** development lines | P7 §7.2 | 5 | None | Yes | |
| **G** market gates | P7 §10.4 | 6 | None | Yes | |
| **EX** example parameter set | P7 §17 | 1 (EX-1) | None | Yes | Test assumptions only |
| **TH** threats | P8 §2.3 | 25 | None | Yes | |
| **SEC** requirements | P8 §16.2 | **32 defined** | **SEC-009 deliberately reserved**; range 001–033; `SEC-034+` is forward-numbering guidance, not an entry | Yes | No SEC-034 created |
| **ST** tests | P8 §19.2 | 20 | None | Yes | All designed-not-executed |
| **OSQ** owner questions | P8 §20 | 12 | None | Yes | |
| **W-18** walkthroughs | P8 §18 | 18 (A…R) | Not a numbered register | Yes | Lettered scenarios under one section |
| **D** decisions | DECISIONS.md | 6 | D-001…003 Confirmed; D-004…006 Provisional | Yes | Unchanged |
| **REQ** integrated requirements | **This report §12** | **39** | New family; checked unused | Itself | No conflict with existing prefixes |
| **ZD** zero-cost dependencies | **This report §17** | **14** | New family; checked unused | Itself | |
| **GATE** readiness gates | **This report §20** | **20** | New family; checked unused | Itself | |
| **DEF** defects | **This report §14** | **18** | New family; checked unused | Itself | Includes the three P7 defects found in the correction-pass full read |
| **OD** owner decisions | **This report §15** | **12** | New family; checked unused | Itself | |
| **PV** capacity validations | **This report §13** | **15** | New family; checked unused | Itself | |
| **TQ** technical questions | **This report §18** | **17** | New family; checked unused | Itself | |

### 16.3 Uniqueness and reference checks

| Check | Result |
|---|---|
| New prefixes collide with any existing family? | **No** (REQ, ZD, GATE, DEF, OD, PV, TQ are unused in P1–P8) |
| Inherited IDs renumbered? | **No** |
| Reserved IDs preserved? | **Yes** — SEC-009 remains reserved |
| Retired IDs reused? | **No** — ECON-003/004/005/007/008 remain retired |
| Undefined IDs cited by this report? | **None found** — every SYS/INT/ECON/TH/SEC/ST/OSQ/SDQ/FO/R reference used here exists in its owning report |
| Orphaned P9 requirements? | **None** — all 39 have a source and a validation path |
| Register counts stated by P9 match the tables? | Verified by the validator (§22) |
| Gaps declared rather than hidden? | **Yes** — F-007/F-028, O-13/O-14 |

### 16.4 Cross-report identifier corrections

Only one **identifier** correction was required and applied: P3 §7.7's O-15/16/17/O-12 citations were rewritten to FO-012/015/016/017 and FO-001/005/006/007/008. The correction pass additionally made two unambiguous **wording** corrections in P7 (DEF-016/017) and the three P8 staging corrections; those do not renumber anything. DEF-008/DEF-009 (F- and O-register gaps) are **recorded, not edited**, because renumbering a completed report's register would break every downstream citation. The right correction is a declared gap in the register's own header, which is a P2 task, not a P9 edit.

---

## Section 17 — Zero-cost operating requirement and free-tier feasibility

### 17.1 The objective, stated exactly

**Project X must be designed to run as a publicly accessible, persistent, multiplayer browser game using free hosting platforms and free service tiers, with a target required operating cost of ₹0 per month**, provided the game remains within providers' applicable free-tier quotas and terms.

Five clarifications that this report will not blur:

1. **₹0 is a constraint on *required* cost**, not a promise that every conceivable feature is free. A feature that cannot operate within free limits is either reduced, deferred, or explicitly flagged as a blocker (OD-01).
2. **No paid plan may be a routine requirement** for core operation. A paid fallback is not a plan; it is a scope failure with a credit card.
3. **₹0 does not mean unlimited capacity.** It means the documented workload fits the documented free limits, with the assumptions stated (§17.4).
4. **₹0 does not mean forever.** Provider quotas, terms, and prices can change. §17.8 defines the exit posture; no guarantee of indefinite free operation is made.
5. **Security is not the thing to cut.** If a free tier cannot carry a control, the answer is retention/automation scope or a disclosed residual risk (OD-06), not silent removal.

### 17.2 The operating stack under evaluation

| ID | Component | Candidate for the ₹0 plan | Free alternative if the candidate fails | Required at FPB? |
|---|---|---|---|---|
| **ZD-01** | Static frontend + CDN | Cloudflare Pages | GitHub Pages; any static host | **Yes** |
| **ZD-02** | API / server execution | Cloudflare Workers (Free) | Another free serverless runtime; requires porting | **Yes** |
| **ZD-03** | Persistent database | Cloudflare D1 | Turso/Supabase/Neon free tiers (all add a provider and limits) | **Yes** |
| **ZD-04** | Scheduled turns | Cloudflare Cron Triggers | External free cron hitting an authenticated endpoint | **Yes** |
| **ZD-05** | Authentication | Better Auth-class library inside the Worker | A free-tier auth provider (adds vendor dependency) | **Yes** |
| **ZD-06** | Transactional e-mail | Resend or Brevo free tier | No verification mail; in-game recovery only (weaker) | Launch |
| **ZD-07** | Audit/event ledger | D1 table + short-retention platform logs | Export to compressed files; aggregates | **Yes** |
| **ZD-08** | Backups | D1 Time Travel + scheduled logical export | Manual encrypted export only | Launch |
| **ZD-09** | Monitoring/alerting | Free uptime monitor + D1 budget gauges + free error tracking | Logs + manual checks | Launch |
| **ZD-10** | Source control / CI | GitHub Free | Any free Git host | **Yes** |
| **ZD-11** | Domain / TLS | `*.pages.dev` or `*.workers.dev` (free TLS) | A custom domain **costs money**; not ₹0 | **Yes** (subdomain) |
| **ZD-12** | Moderation tooling | None; process + D1 case rows | Paid tooling is not required | Launch |
| **ZD-13** | Egress / bandwidth | No metered egress documented for Pages/Workers/D1; R2 egress free | Static asset hosting | **Yes** |
| **ZD-14** | Realtime / presence | **Not required by the design**; Durable Objects optional | Polling the digest | No |

**Deliberately not in the required stack:** a managed auth service, a managed Postgres, Redis, a queue service, a paid WAF, a paid log drain, a paid error tracker, a custom domain, and R2. Any of these may be used as an *optional* convenience; none may be required for core operation.

### 17.3 Current free-tier evidence (with access dates and confidence)

| # | Provider / item | Documented free value | Source and date | Confidence | Why it matters |
|---|---|---|---|---|---|
| 1 | Workers requests | 100,000/day | Cloudflare Workers limits; read by P7 §16.4 on 2026-10-22 | High for the figure; capacity unmeasured | Caps daily active players × requests |
| 2 | Workers CPU | **10 ms per invocation** | Same; P7 recorded the current figure (P1's 50 ms is stale) | High for the figure; **the decisive unmeasured constraint** | A boundary job must fit |
| 3 | D1 rows written | 100,000/day | [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/), accessed 2026-10-23 (billing metrics table) | High | Caps nations × actions × audit rows |
| 4 | D1 rows read | 5,000,000/day | Same pricing page, accessed 2026-10-23 | High | Digest and listing reads |
| 5 | D1 storage | 5 GB/account (pricing page); **500 MB per database** (limits page) | [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/) + [D1 limits](https://developers.cloudflare.com/d1/platform/limits/), both accessed 2026-10-23 | High | Caps history, not current state |
| 6 | D1 Time Travel | **7 days** (Free); 30 days (Paid) | D1 limits page, accessed 2026-10-23 | High | Sets the backup floor |
| 7 | D1 queries/subrequests per invocation | **50** (Free); 1,000 (Paid) | D1 limits page, accessed 2026-10-23 ("Queries per Worker invocation") | High | Per-nation loops are impossible; batching is mandatory |
| 8 | D1 concurrency | Single-threaded per database; 6 simultaneous connections; 30 s SQL max | D1 limits page, accessed 2026-10-23 | High | Boundary work serializes |
| 9 | Cron behaviour | Executes on **UTC**; runs on underutilized machines; no exactly-once or bounded-latency guarantee is documented | [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/), accessed 2026-10-23 | High for wording; medium for inference | The design must be idempotent and delay-tolerant |
| 10 | Pages builds/files | 500 builds/month; 20,000 files; 25 MiB/file; 100 projects | [Pages limits](https://developers.cloudflare.com/pages/platform/limits/), accessed 2026-10-23 | High | Deploy cadence and asset size |
| 11 | Pages requests/bandwidth | The free-plan limits page lists no request or bandwidth cap | Same | Medium — absence of a cap is not a guarantee | Do not build a business case on "unlimited" |
| 12 | R2 free tier | 10 GB-month storage; 1M Class A; 10M Class B; free egress | [R2 pricing](https://developers.cloudflare.com/r2/pricing/), accessed 2026-10-23 | High for allowances; **payment-method requirement unverified** | R2 stays optional; enabling it may require a card |
| 13 | E-mail | Resend free ~100/day / 3,000/month; Brevo free ~300/day | Research pass 2026-10-23; not re-opened this pass | Medium | Signup/recovery throughput |
| 14 | Monitoring | Sentry developer free ~5k events/month; UptimeRobot/Better Stack free monitors | Research pass 2026-10-23; not re-opened | Medium | Alerts and errors |
| 15 | Source control/CI | GitHub Free: 2,000 Actions minutes/month | Research pass 2026-10-23 | Medium | Build/deploy |
| 16 | Auth library | Better Auth is open-source and self-hostable | Package documentation; not re-verified | Medium | No auth vendor cost |
| 17 | Workers Logs retention | **Not verified**; free retention is short | — | Low | Do not rely on platform logs as evidence; write the audit spine to D1 |
| 18 | Durable Objects on Free | Available with free request/GB-s allowances; figures not re-verified | — | Low | Optional; don't make it required |
| 19 | D1 index write amplification | **Confirmed by documentation**: a write touching an indexed column adds at least one extra row written ("one to the table itself, and one to the index") | D1 pricing FAQ, accessed 2026-10-23 | High for the mechanism; magnitude still unmeasured | DEF-006 is a documented effect, not a hypothesis; §17.4's write estimates must be measured (PV-04) |

**Confidence rule:** High = directly read in official documentation on the date shown; Medium = reported by a prior research pass or inferred from a page that does not state the number; Low = not verified. Any Medium/Low item used in a capacity decision must be re-checked (PV-09).

### 17.4 Workload scenarios (all assumptions, none measured)

**Assumption set A:** an active player makes 1–3 sessions/day; a session costs 15–25 API requests (page load + 3–5 actions + digest), and the planning band used below is **40–60 requests/player/day** (the median of that range, not its maximum); each active nation generates 50–60 D1 row-writes/day after audit, session, and rate-limit rows; appended history is ~250 bytes/row; 15–20 appended history rows per active nation/day. **These are planning assumptions, not observed data.**

| Scenario | Active players | Requests/player/day | Requests/day | Writes/day (est.) | Appended history/day | First binding limit |
|---|---|---|---|---|---|---|
| **S0 Prototype** | 1–10 | 20–30 | <300 | <1,000 | <1 MB | None |
| **S1 Private playtest** | 25–100 | 30–50 | 1k–5k | 2k–6k | 0.1–0.5 MB | None |
| **S2 Modest launch** | 300 | 40–60 | 12k–18k | 16k–18k | 1.3–2.0 MB | Storage (~250–380 days) |
| **S2b Upper launch** | 1,000 | 40–60 | 40k–60k | 50k–60k | 4.3–6.5 MB | Writes (~60–100k) and storage (~77–116 days) |
| **S3 Growth** | 2,000–5,000 | 40–60 | 80k–300k | 110k–275k | 9–22 MB | **Requests (at ~2,000) and writes (at ~1,800)** |

**Reading the table:**

- **S0/S1 fit comfortably** under every documented limit, including the 500 MB database, *if* the boundary itself fits the CPU/subrequest budget (unknown).
- **S2 fits requests and writes**, but storage becomes a retention problem within a year. That is solvable by export/aggregation, not by a paid plan.
- **S2b is the edge.** Requests are fine; writes are at 50–60% of the daily cap with no headroom for a busy day, and storage needs retention within ~3 months. A single retry storm or an index-write multiplier pushes it over.
- **S3 is incompatible** with the free tier under these assumptions. The honest answer is a world-size cap or a paid tier — an owner decision (OD-01), not a silent redesign.

**Sensitivity:** if requests/player/day are 20 instead of 50, S3's request ceiling moves from ~2,000 to ~5,000 players. If audit rows are 10/nation/day instead of 18, the write ceiling improves by ~15%. **The model is sensitive to exactly the numbers that have not been measured** — which is why PV-02/04/06 precede architecture.

### 17.5 Database and persistent-state feasibility

**What must persist:** nation rows; line levels and emphasis; treasury and commitments; material stocks; offers and their reservations; trade headers; relationship/treaty state; chronicle entries; turn ledger and phase checkpoints; audit spine; moderation cases; account/session rows. Current state is small; **history is the problem.**

| Data class | Size assumption | Growth | Retention posture |
|---|---|---|---|
| Nation + lines + emphasis | 2–4 KB/nation | One-time + edits | Life of world |
| Treasury/stocks | <1 KB/nation | Updated in place | Life of world |
| Offers/commitments | 200–500 B each | Bounded by open offers | Deleted on close |
| Trade headers | 300–600 B each | 1–3/active nation/day | Dispute window; then aggregate |
| Audit spine | ~250 B/row | 15–20/active nation/day | **90 days hot; archive beyond** |
| Turn ledger/checkpoints | Small | 12/day + phases | 1 year, then aggregate |
| Chronicle | 200–500 B/entry | A few/day | Life of world; prune low-value |
| Moderation cases | 1–5 KB/case | Low | 1 year, then anonymise |

**The 500 MB arithmetic (from §8.8):** at 1,000 active nations, appended history is 4.3–6.5 MB/day, so the database fills in **77–116 days** even before indexes and free-space fragmentation. At 300 nations it lasts **250–385 days**. **A permanent, queryable, in-D1 audit history is not compatible with the free tier at launch scale.**

**Required retention design (recommendation, not approval):**

1. **Hot (D1):** current state + last 90 days of audit/trade headers, indexed for dispute queries.
2. **Warm (D1):** monthly aggregates per nation (income, spend, trades, standing changes) kept indefinitely; they answer "what happened" but not row-level detail.
3. **Cold (export):** rows older than 90 days exported to a compressed, encrypted archive outside D1, retained per a published schedule. This is how SEC-031's "permanent evidence" survives the 500 MB cap.
4. **Disclose the window:** players are told how far back row-level evidence goes; disputes inside the window are fully evidenced, older ones rely on aggregates.

**This is a requirement interpretation the owner must accept.** SEC-031 says "permanent"; the free tier makes "permanent *in the primary database*" impossible at 1,000 nations. "Permanent in an export archive + aggregates" preserves the purpose (accountability, dispute resolution) without a paid database. **OD-06 should record this explicitly.**

### 17.6 Scheduled-turn feasibility

| Question | Finding | Verdict |
|---|---|---|
| Can a cron fire every 2 hours? | Yes — one trigger on a two-hour UTC expression gives 12/day; cron expressions have minute granularity, and the free plan's trigger count (P1 recorded 5) is not binding | **Feasible** |
| Is execution exactly once? | No guarantee documented; cron runs on underutilized machines | **Design for idempotency** (SEC-019/020) |
| Is execution timely? | No bounded-latency guarantee documented | **Design for delay + announcement** (SEC-022) |
| Can a boundary fit 10 ms CPU? | Unknown. Set-based SQL may fit; per-nation JS loops will not | **Unmeasured — PV-02** |
| Can it fit 50 subrequests? | Unknown. A batch may count as one or many; do not assume | **Unmeasured — PV-02** |
| Can D1 handle the write burst? | Single-threaded; 100k/day cap; boundary writes for N nations | **Unmeasured — PV-04** |
| What if it doesn't fit? | Options: set-based batches; shard the boundary across triggers (changes boundary semantics); an external scheduler; a paid tier (violates ₹0) | **Owner/architecture decision after measurement** |

**What must not happen:** reducing the cadence to make the free tier work. The two-hour turn is a project constraint, not a tuning parameter. If 12/day cannot be resolved within free limits at the intended scale, the honest outcomes are a smaller world, a different provider, or a disclosed paid requirement — not a silent 4-hour turn.

### 17.7 Protection against accidental charges

| Provider | Payment method required? | Overage behaviour | Risk | Safeguard |
|---|---|---|---|---|
| Workers Free | No (verify in PV-09) | Requests fail at the cap; no automatic paid upgrade | Low | Keep the account on Free; no paid features |
| D1 Free | No | Queries fail when limits are hit (enforcement recorded since 2026-09-01) | Low | Budget gauges; degradation mode |
| Pages Free | No | Build/deploy limits; no overage billing | Low | 500 builds/month is ample |
| **R2** | **Enabling R2 requires an R2 subscription; card requirement unverified** | Usage beyond 10 GB-month is billed per unit | **Medium** | **Do not make R2 required; if enabled, monitor monthly and treat it as optional** |
| Resend/Brevo | No on free tier | Sending stops at the cap | Low | Signup throttle; fallback |
| Sentry/UptimeRobot | No on free tier | Events/monitors stop | Low | Accept reduced visibility |
| Custom domain | Yes (registrar) | Renewal is a recurring charge | **Certain cost** | Use the free subdomain for the ₹0 plan |
| GitHub | No | Actions minutes stop | Low | 2,000 minutes is ample for one project |

**Safeguards that are actually available, not assumed:** application-level quotas (SEC-029); a daily budget gauge written to D1 and read by the owner; a free uptime monitor; a documented "capacity full" mode; and a monthly export/capacity review. **Do not assume a hard spending cap exists** unless the provider documents one; the safest cap is not enabling the paid product at all.

### 17.8 Resilience to provider change, outage, and quota exhaustion

| Event | Impact | Mitigation | Portability |
|---|---|---|---|
| Free quota reduced | Capacity shrinks | Retention/scope adjust; world-size cap; OD-01 | High — data exportable |
| Terms change (free tier removed) | Core cost becomes non-zero | Migrate to another free provider or reduce scope; disclose | Medium — Worker code needs an adapter; SQLite exports cleanly |
| Cron feature changed/removed | Turns stop | External free scheduler hitting an authenticated endpoint | High — a scheduled HTTP call is portable |
| Outage | Turns delayed; players see stale world | Announce; catch-up policy (TQ-04); no data loss | High — D1 is durable |
| Storage cap reached | Writes fail | Degradation mode; prune/export; announce | High |
| D1 write cap reached mid-boundary | Partial turn risk | Phase checkpoints + forward resume; fail safe | High |
| R2 unavailable/paid-only | Backups weaken | Manual encrypted export remains | High |
| Account suspension | Everything offline | Static status page on a separate free host; appeal; export | Medium |

**Catch-up policy is undefined (TQ-04).** If a boundary is missed, does the next run resolve one turn or two? Resolving two doubles production and trade settlement; skipping one loses a turn. Neither is acceptable without a stated rule. This is a design decision, not an infrastructure detail, and it belongs with SDQ-018.

### 17.9 Free-only alternatives and scope reductions

| If this fails… | First alternative | Second | What must not be done |
|---|---|---|---|
| D1 capacity | Turso (SQLite) or Supabase/Neon free Postgres — each adds a provider, its own limits, and possible card requirements | Reduce world size + retention | Silently switch to a paid database |
| Workers CPU | Set-based SQL; shard the boundary; external scheduler | Different free runtime | Reduce cadence |
| Cron | External free scheduler | Manual trigger by the owner (not acceptable for a persistent game) | Pretend the turn is automatic |
| Auth | Self-hosted Better Auth | A free-tier auth provider | Remove authentication to "simplify" |
| E-mail | Brevo's higher daily cap | Unverified accounts + throttles | Remove recovery entirely |
| Backups | 90-day export + monthly archive | Manual snapshot before each deploy | Run with no restore path and not disclose it |
| Audit storage | 90-day hot + aggregates + cold export | Sample high-volume rows (never value rows) | Delete evidence to save space |
| Alliances | Defer to launch | Minimal roles only | Ship a shared pool with no permission matrix |

### 17.10 Zero-cost feasibility verdict

**Component matrix:**

| ID | Component | Verdict | Basis |
|---|---|---|---|
| ZD-01 | Static frontend | **Verified free-tier fit** | Pages limits read 2026-10-23; build/file caps far above need |
| ZD-02 | API execution | **Likely fit, needs measurement** | 100k requests/day is ample at S1/S2; CPU 10 ms is the risk |
| ZD-03 | Database | **Conditional fit** | 500 MB/100k writes fit S1/S2 only with retention; S3 fails |
| ZD-04 | Scheduled turns | **Conditional fit** | Scheduling exists; CPU/subrequest fit unmeasured |
| ZD-05 | Authentication | **Likely fit, needs measurement** | Self-hosted library; no vendor cost, but the KDF's CPU fit on a 10 ms Worker is unmeasured (DEF-015; PV-15) |
| ZD-06 | E-mail | **Conditional fit** | 100–300/day caps signup/recovery throughput |
| ZD-07 | Audit/logs | **Conditional fit** | Requires 90-day hot + export; platform log retention is short |
| ZD-08 | Backups | **Conditional fit** | 7-day Time Travel + manual export; RPO/RTO degrade; R2 optional |
| ZD-09 | Monitoring | **Verified free-tier fit** | Free monitors + D1 gauges; short retention accepted |
| ZD-10 | Source/CI | **Verified free-tier fit** | GitHub Free is sufficient |
| ZD-11 | Domain/TLS | **Verified free-tier fit (subdomain only)** | Custom domain is a real cost; excluded from ₹0 |
| ZD-12 | Moderation | **Verified cash-free** | People time, not service fees |
| ZD-13 | Egress | **Likely fit** | No metered egress documented for the chosen path; not a guarantee |
| ZD-14 | Realtime | **Not required** | Deferred; DO optional |

**Scenario verdicts:**

| Scenario | Verdict | Why |
|---|---|---|
| **1. First playable build** | **Plausible ₹0** | S1 loads are far below every documented cap; the only unknown is boundary CPU/subrequests (PV-02) and the storage/retention design (PV-05) |
| **2. Small private playtest** | **Plausible ₹0** | Same, with 7-day Time Travel backups and manual export |
| **3. Limited public launch (≈300–1,000 active)** | **Conditional ₹0** | Writes and storage are the binding constraints; retention/export is mandatory; 1,000 is the edge, not the comfortable zone |
| **4. Increased traffic (≈2,000–5,000 active)** | **Not currently supported** | Requests and writes exceed the free caps under stated assumptions; requires a paid tier, a different provider, or a world-size cap |

**Bottom line:** a coherent ₹0 plan exists for the FPB and a small playtest, and a conditional one for a limited launch. It is **not** a claim that the game can grow without limit for free. The three numbers that decide the launch verdict are: boundary CPU/subrequests, D1 row-writes per action, and appended-history bytes per nation-day.

### 17.11 Required-output checklist (Section 17)

| Requirement | Where | Status |
|---|---|---|
| Operating-stack comparison | §17.2, §17.9 | Done |
| Current official free-tier evidence and access dates | §17.3 | Done (High/Medium/Low confidence marked) |
| Workload assumptions and scenarios | §17.4 | Done (assumptions labeled; S0–S3) |
| Database, execution, scheduling, storage, bandwidth constraints | §17.5–17.6 | Done |
| Cost-trigger risks | §17.7 | Done (R2 and custom domain are the real ones) |
| Security, backup, recovery coverage | §§10.5, 17.8 | Done |
| Features reduced/deferred to stay free | §11.3–11.4, §17.9 | Done |
| Zero-cost verdict with limitations | §17.10 | Done |
| Decisions requiring owner approval | §15.2 (OD-01/06), §17.5 | Done |

---

## Section 18 — Cost, operations, and future technical-planning dependencies

### 18.1 What Section 17 settles, and what this section adds

Section 17 asks whether a credible ₹0 operating plan exists. It answers: **yes for the FPB and a small playtest, conditionally for a limited launch, no for growth under current assumptions.** This section lists the technical questions that must be answered before any architecture is committed. It does not choose a framework, schema, or provider.

### 18.2 Technical questions for the architecture stage (TQ-01…TQ-17)

| ID | Question | Systems / requirements | Why it matters | Exit evidence |
|---|---|---|---|---|
| **TQ-01** | What is the minimum schema for nations, lines, stocks, offers, trades, treaties, relationships, and the turn ledger? | REQ-002/005/006/009/015; SYS-001…016 | Every later decision depends on the shape of state | Schema reviewed against the C1–C4 identity |
| **TQ-02** | How does a boundary resolve N nations within 50 subrequests and 10 ms CPU? | REQ-015/033/035 | The free-tier make-or-break question | PV-02 measurements; a documented batch plan |
| **TQ-03** | Does a D1 `batch()` consume one subrequest or one per statement? | REQ-015/035 | Determines whether batching is a solution or an illusion | Measured, not assumed |
| **TQ-04** | What happens when a boundary is missed — resolve one catch-up turn, or skip with disclosure? | REQ-015/022 | Double resolution mints; skipping loses a turn | A written policy + a tested simulation |
| **TQ-05** | If CPU is insufficient, is sharding the boundary across triggers acceptable, given it changes simultaneous resolution? | REQ-015/017 | Sharding may violate the single-boundary promise | Owner decision after PV-02 |
| **TQ-06** | Where do sessions live, and how are they revoked across Workers isolates? | REQ-003 | Session correctness without a central cache | A session table + revocation test |
| **TQ-07** | What is the idempotency-key scope and retention? | REQ-009/018 | Duplicate trades and retried orders | A key design + duplicate test |
| **TQ-08** | How are reservations/commitments represented so that "available" is always derivable? | REQ-005 | The finance view's honesty depends on it | A reservation model + conservation test |
| **TQ-09** | What are the turn-ledger phases and checkpoint granularity? | REQ-016/017 | Forward-only recovery | A phase table + abort injection test |
| **TQ-10** | How are audit rows exported, encrypted, and restored? | REQ-024/027 | 500 MB cap + permanent evidence | An export/restore drill (PV-05/08) |
| **TQ-11** | What is the backup and restore procedure, and what RPO/RTO does it actually achieve? | REQ-028 | Launch gate | A timed drill |
| **TQ-12** | How are per-class quotas enforced without a paid WAF? | REQ-030 | Free-tier abuse protection | A quota implementation + burst test |
| **TQ-13** | What is cached, where, and for how long (digest, profiles, chronicle)? | REQ-020/033 | Read amplification and freshness | A cache plan with invalidation |
| **TQ-14** | How are schema migrations applied to a live D1 database with 30 s SQL limits? | REQ-034 | Safe evolution | A migration runbook |
| **TQ-15** | How are preview and production data separated, and where do secrets live? | REQ-036 | Accidental data/charge exposure | An environment matrix |
| **TQ-16** | What observability exists without paid log retention? | REQ-029/030 | Incident response | Budget gauges + alert test (PV-11) |
| **TQ-17** | Which password KDF fits the free Worker's CPU budget, and what does a login actually cost? | REQ-003; SEC-002 | Argon2id/WASM may exceed 10 ms; Web Crypto PBKDF2 is native but not memory-hard | PV-15 measurement plus a recorded security trade-off |

### 18.3 Operational constraints that are not technical

| Constraint | Reality | Design consequence |
|---|---|---|
| Single operator | No 24/7 on-call; no two-person rule at launch | Disclosed response hours; logged actions; appeals may be slow (OD-08) |
| No budget for paid tools | Monitoring, backups, moderation tooling must be free or manual | Manual monthly export; free uptime monitor; D1 case rows |
| No content team | No authored events, no editorial calendar | SYS-015's systemic generation only (AP-003) |
| Persistent world, no resets | Balance changes affect live nations | Conservative numeric changes; no season resets at launch |
| Small launch population | Empty market, thin diplomacy | Directed trade; no listings market; chronicle needs seeding care (PXE-015) |
| Provider dependence | Terms can change | Export/portability as a first-class requirement (REQ-037) |

### 18.4 Deployment and maintenance dependencies

- **Source control and CI:** GitHub Free; 2,000 Actions minutes is enough for a small project, but a build that runs on every push can exhaust it if the pipeline is heavy. Cache dependencies; build on release.
- **Environments:** at least preview and production. Preview must not write to production D1. A second free D1 database is available (10 per account on Free), so this is feasible without cost.
- **Secrets:** provider tokens and any future API keys stay out of the repository and client bundle; use the platform's secret store. No secret is required for the FPB if auth is self-hosted and e-mail is optional.
- **Domain:** the free `*.pages.dev` / `*.workers.dev` origin is the ₹0 path. A custom domain is a recurring cost and must not be treated as required.
- **Observability:** platform logs are short-lived; the durable evidence is the D1 audit spine. Alerts must be built from D1 gauges or a free monitor, not from a paid log drain.

### 18.5 What this section deliberately does not decide

The runtime framework (plain Worker vs Hono vs another router), the ORM/query layer, the frontend framework, the CSS approach, the session cookie format, the exact D1 schema, the sharding strategy, and the backup archive format. **All of these are architecture-stage decisions and none is approved here.** D-005 remains Provisional.

---

## Section 19 — Recommended next stages

### 19.1 The smallest sensible next step

**Two things, in this order, before any architecture or code:**

1. **Owner decision closure** on OD-01, OD-02, OD-03, and OD-06 — the four decisions that determine what is being built and what happens at capacity. Without them, every estimate is for a different game.
2. **A free-tier measurement spike** (PV-01…PV-07) using a throwaway harness: a synthetic world, one cron boundary, set-based SQL, and instrumented counts. This is not production code and does not select an architecture; it answers whether the ₹0 plan is real.

Everything else in §19.2 follows those two.

### 19.2 Workstreams

| Stage | Objective | Required inputs | Deliverables | Dependencies | Exit criteria | Owner decisions | Risks if skipped | ₹0 guard |
|---|---|---|---|---|---|---|---|---|
| **2A — Decision closure and Stage 1 close-out** | Convert the open decisions into recorded choices or explicit deferrals | This report; DECISIONS.md; owner availability | DECISIONS entries (only where the owner approves); updated continuity; a signed scope note | P9 complete | OD-01/02/03/06 decided; Stage 1 status updated honestly | All | The next stage builds the wrong artifact | No cost |
| **2B — Free-tier measurement spike** | Measure the three unknowns: boundary CPU/subrequests, D1 writes, storage growth | Synthetic dataset; a free Worker + D1; PV plan | A measurement report with actuals and a go/conditional/no-go verdict | 2A (scope) | PV-01…07 executed; numbers recorded | D-005 re-evaluation | Architecture commits to an unproven platform | Harness only; no paid services |
| **3 — Architecture and schema** | Answer TQ-01…TQ-17 and SDQ-003/018 | 2B report; requirements matrix | Data model, authority matrix, turn phase catalog, retention/export design, environment plan | 2B | SDQ-003/018 answered; D-005 re-evaluated | D-005 | Rework after first code | Free-tier design constraints explicit |
| **4 — Numbers, balance, and simulation** | Fill ECOQ-002/004/005 with tested curves | Architecture constants; EX-1; simulation harness | A parameter set, simulation results, failure-case sweep | 3 (partly parallel) | Conservation + no-lockout + bounded snowball | Numeric approval | An unbuildable or unfair economy | Offline simulation; no hosting |
| **5 — War design** | Turn D-004 and the conflict pillar into rules | P5 §11; P6 §15; P8 TH-022; owner authorization | Campaign, protection, settlement, and OP rules; TH-022 coverage | 4 (economy constants) | Rules complete enough to test; D-004 decided | D-004; war scope | Conflict remains a promise; security gap | Design-only |
| **6 — UI/UX and onboarding** | Make the loop legible and testable | V-2/CV-002/006 results; digest taxonomy | Screen inventory, onboarding flow, accessibility baseline | 2B/3 | A tester completes the first session unassisted | Content scope | A correct game nobody understands | Static design; no paid tools |
| **7 — Implementation planning** | Turn the design into a build plan | 3/4/6 | Repo conventions, test strategy, CI, milestones | 3–6 | A plan with acceptance criteria per milestone | Scope | Chaotic build; untestable increments | Free CI only |
| **8 — Security validation and ops** | Execute ST-001…020 and the restore drill | A running build; P8 registers | Test evidence, restore drill record, incident runbook, moderation runbook | 7 | Stage-A/B controls verified | OD-06/08 | Launch with unproven controls | Manual drills; no paid tooling |
| **9 — Staged playtests and launch** | Validate with real players in increasing circles | CP/FPB; PV results | Playtest reports; go/no-go for limited launch | 8 | Retention/comprehension thresholds met or scope revised | Launch | Public failure | Capacity caps + degradation mode |

### 19.3 Sequencing notes

- **2A and 2B can overlap** — the owner can decide while the measurement harness is built — but 2B's scope depends on 2A's artifact definition.
- **3 should not start before 2B reports.** A schema designed without the write/CPU measurements is a guess.
- **4 can start in parallel with 3** because it is offline, but its parameters must be re-checked against the final schema.
- **5 is independent of 3/4 in rules but dependent on 4's economy constants** for costs and effects.
- **6 needs V-2/CV-002/006**, which can run on mockups before a build.
- **8 cannot start before 7**, and 7 cannot start before 3.

### 19.4 What this roadmap refuses to do

It does not create detailed prompts for Stages 2–9, does not authorize any of them, and does not assume they happen in one continuous push. Per D-002, each stage requires explicit owner authorization. The roadmap is a dependency graph, not a schedule.

---

## Section 20 — Stage 1 readiness gates

### 20.1 Criteria provenance

No standalone Stage 1 acceptance-criteria document exists. The closest is PROJECT_PROGRESS's "do not mark complete until the remaining prompts are finished and reviewed," plus the implicit criteria in the prompt briefs. **The 20 gates below are therefore proposed criteria**, not owner-approved policy. They are written to be falsifiable and are evaluated against the saved files, not against the reports' self-assessments.

### 20.2 Gate results

| ID | Gate requirement | Evidence | Result | Severity if failed | Remaining action | Blocks Stage 1? | Blocks implementation? | Blocks ₹0? |
|---|---|---|---|---|---|---|---|---|
| **GATE-01** | All required research reports exist and are readable | 8/8 files at recorded paths; line counts in §2.1 | **Pass** | — | — | No | No | No |
| **GATE-02** | Each report has a clear status | All 8 carry status/QA sections; P7 v1.1; P8 correction pass | **Pass** | — | — | No | No | No |
| **GATE-03** | Material QA defects resolved or explicitly accepted | **18 defects: 8 fixed/resolved** (DEF-004/005/007/008/010/014/016/017), 2 declared (DEF-009/013), 2 by-design (DEF-011/012), **6 open but explicitly accepted as conditions** (DEF-001/002/003/006/015/018). DEF-004/005/010 corrections verified in P8; DEF-008 closed by P2's declaration note; DEF-016/017 verified in P7; DEF-018 is explicitly preserved as an ambiguity for the economy stage. None is concept-invalidating | **Pass** | — | Accepted conditions are recorded in §2.3 and carried by OD-02/OD-03/PV-04/PV-15 | No | No | Partly (DEF-006/015 feed GATE-16/18) |
| **GATE-04** | Integrated game concept is coherent | §3; CX-5 consistent across P4/P5/P6 | **Pass** | — | — | No | No | No |
| **GATE-05** | Major systems identified and connected | §5 (18 systems), §6 (20 interactions) | **Pass** | — | — | No | No | No |
| **GATE-06** | Player experience understandable at a conceptual level | §4; gaps explicitly listed | **Pass** (conceptual) | — | Fill journey gaps before UI stage | No | No | No |
| **GATE-07** | Core economy mechanics and dependencies are traceable | §8; ECON/ECOQ/MAT/L IDs | **Pass** (structure) | — | Numerics remain open (expected) | No | No | No |
| **GATE-08** | Turn model's open ordering questions are documented | §7; SDQ-018; 7 unknown rules | **Pass** | — | Answer before implementation | No | Yes | No |
| **GATE-09** | Security requirements and major risks are documented | §10; TH/SEC/ST/OSQ | **Pass** | — | — | No | No | No |
| **GATE-10** | Critical requirements trace to tests or planned validation | §12.3: 39/39 have a path; 0 executed | **Pass** (plan only) | — | Execute before launch | No | No | No |
| **GATE-11** | Owner decisions are accurately recorded | §15.1; DECISIONS unchanged; D-004/005 Provisional | **Pass** | — | — | No | No | No |
| **GATE-12** | No unresolved contradiction invalidates the concept | §14; DEF-001/002 are scope, not concept | **Pass** | — | — | No | No | No |
| **GATE-13** | The next workstream can proceed without undocumented assumptions | DEF-003 (validation gates bypassed); DEF-001/002 (scope); numbers absent | **Conditional** | **High** | Record accepted assumptions; decide OD-02; run V-2/CV before design freeze | **Yes** | Yes | No |
| **GATE-14** | Continuity files and report links are reliable | §22 validator; updated files | **Pass** (after update) | — | Re-check by next session | No | No | No |
| **GATE-15** | ₹0 objective evaluated with current official documentation | §17.3; 4 pages read 2026-10-23 | **Pass** | — | — | No | No | No |
| **GATE-16** | Every essential component has a plausible free-tier path or an explicit blocker | §17.10: 5 verified, 3 likely, 5 conditional, 1 not required; 0 incompatible for the FPB | **Conditional** | **High** | Measure cron/D1/auth (PV-01…07, PV-15); decide OD-01/06 | **Yes** | Yes | Yes |
| **GATE-17** | Free-tier constraints, workload assumptions, and cost-trigger risks are documented | §17.3/17.4/17.7 | **Pass** | — | — | No | No | No |
| **GATE-18** | The ₹0 claim is not based on unverified capacity or a hidden paid dependency | Capacity unmeasured; no hidden paid dependency found; R2 optional | **Conditional** | **High** | Execute PV-01…07; PV-09 | **Yes** | Yes | **Yes** |
| **GATE-19** | No production code or final architecture introduced | No code in P9; D-005 Provisional; no schema | **Pass** | — | — | No | No | No |
| **GATE-20** | P9 does not falsely declare Stage 1 complete | §1/§20; verdict conditional | **Pass** | — | — | No | No | No |

### 20.3 Tally and interpretation

| Result | Count | Gates |
|---|---|---|
| **Pass** | **17** | 01–12, 14, 15, 17, 19, 20 |
| **Conditional** | **3** | 13, 16, 18 |
| **Fail** | **0** | — |

**Stage 1 is not complete.** Three gates remain conditional: GATE-13 (bypassed validation and the still-open scope decision), GATE-16 (component fit), and GATE-18 (unmeasured capacity). Two of them (GATE-16/18) directly concern the ₹0 objective the owner set as a core constraint. GATE-03 moved to pass only because its own criterion ("resolved or explicitly accepted") is now met and the corrected P8 text was verified — not because the defect history was deleted. Declaring the stage complete would still require either lowering the criteria (not permitted by this brief) or pretending measurements exist (not honest). The correct status is **Stage 1 incomplete — conditionally ready to proceed to bounded Stage 2 work.**

### 20.4 What would flip the verdict

| Gate | To pass | Evidence needed |
|---|---|---|
| GATE-03 | — **now pass** after the 2026-10-23 correction pass | P8 corrections verified; accepted conditions recorded in §2.3 |
| GATE-13 | Record the bypassed validation as accepted assumptions and fix scope | OD-02 recorded; V-2/CV-002 scheduled |
| GATE-16 | Show each component fits or has a blocker | PV-01…07, PV-15; R2/domain decision |
| GATE-18 | Replace capacity assumptions with measurements | PV-02/04/05/06 actuals |

---

## Section 21 — Final recommendations

### 21.1 The consolidated direction

Build the game the research actually describes: **a mapless, persistent, two-hour-turn nation game whose core is a legible economy and a relationship network, with bounded conflict added only after its own design stage.** Do not build the map game, the election simulator, the market game, or the war game first. The research supports this direction consistently across P3–P8; the disagreements are about scope, not identity.

### 21.2 The requirements the next phase must preserve

1. Server authority over every valuable quantity (REQ-019).
2. Atomic, idempotent value movement (REQ-009/018).
3. Exactly-once, forward-only turn resolution (REQ-015/016).
4. A deterministic, published ordering catalog (REQ-017).
5. Audit evidence for every value mutation (REQ-027).
6. A backup path with a tested restore (REQ-028).
7. No paid dependency for core operation (REQ-036).
8. Retention/export designed for the 500 MB cap (REQ-024/034).

### 21.3 The highest-priority unresolved decisions

| Rank | Decision | Why now |
|---|---|---|
| 1 | **OD-02** CP/FPB taxonomy and FPB core | Every estimate depends on what is being built |
| 2 | **OD-01** quota-exhaustion policy | Determines whether ₹0 is a plan or a hope |
| 3 | **OD-06** backup/recovery tier | Launch gate; shapes the retention design |
| 4 | **OD-03** directed trade at FPB | The concept's core loop |
| 5 | **OD-05** multi-account policy | Trade caps and sanctions depend on it |

### 21.4 Correction status

| Correction | Owner | Severity |
|---|---|---|
| ~~P8 stage-A count, SEC-031 subset, TH-011 residual (DEF-004/005/010)~~ — **applied 2026-10-23** | P8 report | — |
| ~~P7 emphasis timing and reserve-interest label (DEF-016/017)~~ — **applied 2026-10-23** | P7 report | Low |
| **P7 offer reservation (DEF-018)** | P7 report / economy stage | Medium (open) |
| ~~P2 F-register gap declaration (DEF-008)~~ — **closed 2026-10-23** | P2 §9 (declaration note added) | Low |
| Record the ₹0 retention interpretation (SEC-031) in the decision log or a P8 addendum | Owner/P8 | Medium |

**The three P8 corrections and the two unambiguous P7 corrections were applied and verified on 2026-10-23** (P8 v1.1; P7 v1.2). **DEF-018 was deliberately not resolved** — it is a genuine design choice between reserving an offer's assets and leaving them spendable, so it is preserved as an explicit open conflict for the economy stage.

**On "no other report needs editing":** that sentence was true of *defects assigned to another report as work* at the time it was written, but it read as an absolute claim and conflicted with this table's own DEF-008 row. It now means: **no other report requires a design correction.** Four documentation-level edits were made outside this report in the final acceptance pass — P3 §7.7 (DEF-007 identifiers, already applied), P2 §9 (DEF-008 declaration), P7 §16.4/§27.1 (citation re-point and a superseded status line), and `qa_backups/08_part6.md` (historical banner + one link) — none of which changes research content, numbers, priorities, or approvals. The remaining items are recorded gaps or owner-facing records, not silent errors.

### 21.5 First-playable scope (recommendation)

The core in §11.2: eleven systems (SYS-001/002/003/004/005/008/013/015/016/017/018), minimal SYS-009, optional SYS-006, and Stage-A integrity. No market, no full alliances, no war, no research tree, no rankings.

### 21.6 Deferred scope (recommendation)

Alliances (Launch), research, readiness/campaigns, rankings, market, contracts, consumer goods, espionage, seasons, meta-progression, chat, custom domain, R2-dependent backups, and any paid monitoring/auth service.

### 21.7 Security and integrity requirements that must not be forgotten

Atomic settlement; idempotency; exactly-once turn; phase checkpoints; authority checks; audit spine; restore drill; quota protection; disclosure of corrections; no silent rollback; no free-text surveillance. These are the project's trust product, not features.

### 21.8 The zero-cost evidence, in one paragraph

Official documentation (read 2026-10-22/23) supports a ₹0 stack for a small game: 100k Workers requests/day, 100k D1 writes/day, 5M reads, 500 MB per database, 7-day Time Travel, 500 Pages builds/month, and free cron. The binding unknowns are boundary CPU (10 ms), subrequests (50), write amplification, and storage growth. At ~300 active players the plan is comfortable; at ~1,000 it is at the edge; at ~2,000+ it fails under stated assumptions. **That is an honest ₹0 verdict, not a guarantee.**

### 21.9 The limits to test first

1. Boundary CPU and subrequests at N = 250/1,000 (PV-02).
2. D1 row-writes per action, including audit and index effects (PV-04).
3. Appended-history bytes per nation-day against 500 MB (PV-05).
4. Workers requests/day at 1,000 simulated players (PV-06).
5. Quota-exhaustion behaviour (PV-07).

### 21.10 The recommended next action

**Record OD-01, OD-02, OD-03, and OD-06, then run the free-tier measurement spike (PV-01…PV-07).** Do not start the schema or the UI before those two steps; both would encode assumptions the measurements may overturn.

### 21.11 Recommendations versus approvals

Everything in §21 is a **recommendation**. No new approval is recorded. D-004 and D-005 remain Provisional; the FPB scope, the CP/FPB taxonomy, the quota policy, and the retention interpretation all require the owner's explicit decision in DECISIONS.md.

---

## Section 22 — Quality assurance record

### 22.1 Method and honesty statement

This pass used four methods, kept separate:

1. **Scripted, read-only checks** — `docs/qa_backups/09_validate.py`, written for this report. It counts the new and inherited registers, checks Section 1–23 continuity, resolves every local Markdown link, verifies DECISIONS.md's six entries and D-004/D-005 status, scans for production-code files outside the QA folder, and checks continuity-file agreement. It does not modify any file.
2. **Manual document review** — reading the source sections cited, comparing claims across reports, and checking that proposed/approved/executed distinctions hold. **Both source reports were read end-to-end in the 2026-10-23 correction passes:** Prompt 8 (§§0–26, including every walkthrough and all five register collections) first, then Prompt 7 (§§0–27, including §17's worked examples and the §26 QA record) in the final acceptance pass, whose full read is what surfaced DEF-016/017/018. "Read" here means sequential reading of the saved Markdown in windows — not a scripted scan, and not an independent review.
3. **Source verification** — re-reading the official free-tier pages cited in §17.3 on 2026-10-23.
4. **Cross-file re-validation** — running `09_validate.py` and the updated `validate_final.py` after the P8 corrections, then re-reading the edited P8 sections and this report's gates/QA to confirm the changes agree.

**This is not an independent external audit.** The same session wrote the report and ran the checks. No second reviewer, no security professional, no playtest, and no provider account were involved.

### 22.2 The 24 required checks

| # | Check | Method | Result | Note |
|---|---|---|---|---|
| 1 | All required reports located and read | Manual + file inventory | **Pass** | 8/8; depth stated in §2.1 (P7 and P8 both end-to-end in the 2026-10-23 passes; P1–P6 end-to-end in their own passes) |
| 2 | Report inventory matches actual files | Scripted (paths, line counts) | **Pass** | 8 reports, 4 continuity files, QA folder |
| 3 | Major internal section references resolve | Manual + scripted heading continuity | **Pass** | Sections 1–23 ordered; no dangling § reference found in the checked passages |
| 4 | Local Markdown links resolve | Scripted | **Pass** | All `../` and local links resolve from `docs/stage-1/` |
| 5 | Traceability matrix has no orphaned critical requirement | Manual + scripted REQ count | **Pass** | 39/39 have source, system, acceptance, validation |
| 6 | Critical threats map to security requirements | Manual (P8 register) | **Pass** | TH-001…025 each carry SEC mitigations in P8 §2.3 |
| 7 | Critical requirements map to tests or explicit validation | Manual + matrix | **Pass** | 39/39 have a planned path; 0 executed |
| 8 | Inherited ID uniqueness and references | Scripted | **Pass** | Counts in §16.2; no duplicate/reused IDs found |
| 9 | Proposed vs approved decisions not conflated | Manual | **Pass** | DECISIONS unchanged; every P5–P8 item labeled provisional |
| 10 | D-004 and D-005 status against the log | Scripted + manual | **Pass** | Both **Provisional**; decision text intact |
| 11 | Continuity files consistent with the synthesis | Scripted + manual re-read | **Pass** | Updated after the report; see §23 |
| 12 | Test-execution claims supported by evidence | Manual | **Pass** | No executed test is claimed; V/CV/ECV/ST/PV all marked unexecuted |
| 13 | No production code written | Scripted file scan | **Pass** | Only document-QA `.py` files under `docs/qa_backups/` |
| 14 | No final technical architecture silently selected | Manual | **Pass** | D-005 Provisional; no schema/framework/provider decision |
| 15 | P9 does not falsely declare Stage 1 complete | Manual | **Pass** | Verdict is conditionally ready; Stage 1 incomplete |
| 16 | Stated entry counts match actual registers | Scripted | **Pass** | REQ 39, ZD 14, GATE 20, DEF 18, OD 12, PV 15, TQ 17; inherited counts re-counted |
| 17 | Free-tier claims cite current official sources where available | Manual | **Pass with caveat** | High-confidence items read 2026-10-23; several Medium items (e-mail, monitoring, GitHub, DO) are prior-pass figures, labeled |
| 18 | Source-access dates recorded | Manual | **Pass** | §17.3 table; 2026-10-22 for P7's Workers read, 2026-10-23 for D1/Cron/Pages/R2 |
| 19 | Workload assumptions clearly labeled | Manual | **Pass** | Assumption set A; S0–S3; no figure presented as observed |
| 20 | All essential operating components addressed | Manual | **Pass** | ZD-01…ZD-14 cover frontend, API, DB, scheduler, auth, e-mail, logs, backups, monitoring, source, domain, moderation, egress, realtime |
| 21 | No required paid dependency introduced | Manual | **Pass** | R2 optional; custom domain excluded; no managed service required |
| 22 | Zero-cost verdict follows from evidence | Manual | **Pass** | Scenario verdicts distinguish plausible/conditional/unsupported |
| 23 | No unlimited or indefinite free guarantee | Manual | **Pass** | §17.1/§17.10 state the limits explicitly |
| 24 | Continuity files state the same zero-cost goal and readiness status | Scripted + manual | **Pass** | AI_CONTEXT/AI_HANDOFF/PROJECT_PROGRESS agree |

### 22.3 Result and limitations

**24/24 initial checks pass, plus the correction-pass re-checks below.** The caveats matter more than the score:

- Check 1 is **not** a claim that every line of every report was re-read in the *original* pass. In the 2026-10-23 correction passes, **Reports 7 and 8 were read end-to-end**; §2.1 records the depth per report, and that reading is what surfaced the three new P7 defects.
- Check 17 is a **mixed-evidence** pass: the core Cloudflare limits are High confidence, but e-mail, monitoring, GitHub, and Durable Objects are Medium and were not re-opened this pass.
- Check 11 is a **point-in-time** pass: it verifies the continuity files after this session's edits, not that a future session will keep them accurate.
- There has been **no independent review, no security test, no capacity test, and no playtest**. Nothing in this report changes that.

**Correction-pass re-checks (2026-10-23), run after the P8 edits:**

| # | Check | Result | Evidence |
|---|---|---|---|
| 25 | DEF-004 count corrected and internally consistent | **Pass** | P8 §15.4 says 12; §1.4/§16.2/§17.1 all yield 12 |
| 26 | DEF-005 SEC-031 subset stated once and consistently | **Pass** | §17.1 A8 + §16.2 stage cell + §22.2 item 6; tally 12/11/9=32 |
| 27 | DEF-010 TH-011 prevention/residual explicit | **Pass** | TH-011 row names Stage-A prevention and the accepted residual; ST-010 still designed-only |
| 28 | P8 handoff no longer awaits Prompt 9 | **Pass** | §26.9 marked superseded; points to this report |
| 29 | Legacy validator's stale role disclosed and updated | **Pass** | P8 §25.3/§25.7; `validate_final.py` re-purposed and re-run |
| 30 | No gate was flipped without evidence | **Pass** | Only GATE-03 moved; its criterion (resolve or accept) is met; 13/16/18 remain conditional |
| 31 | DEF-008 has one coherent disposition | **Pass** | P2 §9 declares the 28 entries and the two unassigned numbers; §14.2/§16.2/§21.4/GATE-03 all read *Fixed*; no renumbering |
| 32 | Source-reading claims are consistent with the work performed | **Pass** | §2.1, §22.1, §22.2 check 1 and §22.3's caveat all describe P7 and P8 as end-to-end in the 2026-10-23 passes, and distinguish manual reading from scripted scans |
| 33 | Validator documentation matches the registers it asserts | **Pass** | `09_validate.py`'s docstring now says DEF 18 and lists the correction-pass assertions; the F-register check is row-scoped and additionally asserts F-007/F-028 absent and F-003b present |
| 34 | Archived QA fragments do not masquerade as current reports | **Pass** | `08_part6.md` carries a historical banner pointing at the authoritative P8 report, and its one broken relative link now resolves |

**Final validator runs after all edits (including the final acceptance micro-pass):** `09_validate.py` reports **68/68 checks passed** (exit 0); `validate_final.py` reports **ALL CHECKS PASSED** (exit 0). Both are document checks only. No game test, capacity measurement, or security test was run, and no ST/V/CV/ECV/PV item changed status.

### 22.4 Corrections made during this pass

| Issue | Resolution |
|---|---|
| P3 §7.7 cited undefined O-15/16/17 and mislabelled O-12 | **Fixed in place** to FO-012/015/016/017 and FO-001/005/006/007/008 (DEF-007) |
| The report's first draft used a non-existent system number in a prose sentence disclaiming new IDs | **Reworded** to avoid creating a token for an ID that does not exist |
| §12.2 REQ-021's Systems cell read `SYS-015/031` — `SYS-031` is not in Prompt 6's 18-system catalog | **Fixed** to `SYS-015` (2026-10-23; SEC-031 already appears in the row's source column). No behaviour, status, or count changed |
| §17.3 rows 3–5 cited the D1 *limits* page for the rows-read/rows-written/storage allowances | **Re-sourced** to the D1 *pricing* page (where those billing metrics are stated), re-read 2026-10-23; 500 MB/database stays on the limits page. Figures unchanged; rows 6–8 now name the limits page explicitly instead of "Same" |
| §17.3 did not record the documented index write-amplification rule | **Added** as row 19 (D1 pricing FAQ, 2026-10-23): an indexed-column write adds at least one extra row written. This supports DEF-006 as a documented mechanism rather than a hypothesis; the magnitude remains unmeasured |
| The validator initially counted prose ID mentions as register entries (SYS-016 repeated in a summary, ECV-006 mentioned in a correction note) | **Checker scoped** to catalog/register rows; the report's counts were not changed to fit the checker |
| Sections 22–23 and the appendices were absent during drafting | **Completed**; the sentinel was removed and the validator re-run |
| DEF-004/005/010 stayed open after the first edition | **P8 corrected and verified 2026-10-23**; DEF rows marked Fixed; GATE-03 re-evaluated to Pass |
| §2.1 and §22.2 gave different reading depths for Prompt 7 | **Reconciled**: both reports are now recorded as read end-to-end in the 2026-10-23 passes, with the method stated (sequential windows, not a scripted scan) |
| DEF-008 sat next to a sentence saying no other report needed editing | **Closed by declaration**: P2 §9 now states the register's 28 entries and the unassigned numbers; §21.4's sentence is qualified rather than absolute |
| `09_validate.py`'s header said the DEF register has 15 entries | **Corrected to 18** (the assertion already expected 18); the F-register check was row-scoped and strengthened, not relaxed |
| `08_part6.md` carried one broken relative link and no status banner | **Repaired**: link now resolves to `../stage-1/08_…`; a historical banner points at the authoritative report |
| P8 §26.9 still awaited Prompt 9 | **Updated** in P8 to mark the instruction superseded |
| `validate_final.py` asserted "Prompt 9 not started" | **Re-purposed** to current-state checks; stale assertions replaced, valid ones retained |

No failure was suppressed, and no claim was weakened to obtain a pass. The GATE-03 change is documented with its evidence, and the remaining conditional gates were not touched.

### 22.5 Evidence artifacts

| Artifact | Path | Purpose |
|---|---|---|
| Validator | [09_validate.py](../qa_backups/09_validate.py) | Read-only section/count/link/decision/code/continuity checks; extended with the correction-pass assertions |
| Cross-file validator | [validate_final.py](../qa_backups/validate_final.py) | Current-state checks for the three continuity files, P8 registers, and DECISIONS; its original Prompt 8 point-in-time assertions were replaced on 2026-10-23 |
| Register-counting aid | [09_register_counts.py](../qa_backups/09_register_counts.py) | Read-only; counts distinct IDs per family from the saved reports and flags gaps. A counting aid only — it asserts nothing about correctness, and its output was reconciled by hand against §16.2 |
| Source reports | `docs/stage-1/01…08_*.md` | Evidence base |
| Decision log | [DECISIONS.md](../DECISIONS.md) | Unchanged; inspected |
| Continuity files | [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) | Updated after the report |

---

## Section 23 — Handoff and continuity file updates

### 23.1 Files inspected

| File | Purpose in this pass |
|---|---|
| [AI_CONTEXT.md](../AI_CONTEXT.md) | Constraints, concept, stage plan |
| [AI_HANDOFF.md](../AI_HANDOFF.md) | Pipeline status, decision summary, prior findings |
| [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) | Prompt tracker and prior QA records |
| [DECISIONS.md](../DECISIONS.md) | D-001…D-006 status and text (unchanged) |
| `stage-1/01…08_*.md` | Eight source reports; reading depth in §2.1 |
| `qa_backups/08_sweep.py`, `08_sweep2.py`, `validate_final.py` | Prior QA tooling and its scope |

### 23.2 Files changed

| File | Change | Reason |
|---|---|---|
| `stage-1/09_integrated_design_synthesis_and_readiness_audit.md` | **Created** | This report |
| `stage-1/03_feature_comparison_opportunity_analysis.md` | **One targeted identifier fix** (§7.7) | DEF-007; no substantive change |
| [AI_CONTEXT.md](../AI_CONTEXT.md) | Status, ₹0 constraint, Prompt 9 index/risk summary | Keep the master context accurate |
| [AI_HANDOFF.md](../AI_HANDOFF.md) | Prompt 9 row, current state, findings, next task | Hand off to the next session |
| [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) | Row 9 complete, Stage 1 status, continuity table | Tracker accuracy |
| [DECISIONS.md](../DECISIONS.md) | **Unchanged** | No owner approval was given for any new decision |
| `qa_backups/09_validate.py` | **Created**, then extended | Read-only QA |
| `stage-1/08_security_privacy_fair_play_and_trust.md` | **Edited 2026-10-23 (v1.1)** | DEF-004/005/010 corrections: §15.4 count, §16.2 SEC-031 stage cell, §17.1 A8/count note, TH-011 residual, §22.2 item 6, §25.3/§25.7, §26.2/§26.9 |
| `stage-1/07_economy_design_and_market_structure.md` | **Edited 2026-10-23 (v1.2)** | DEF-016 emphasis timing rows (§14.1/§19.3), DEF-017 reserve-interest label (§15.2), DEF-018 offer-reservation conflict recorded at §10.2; version header; §26.2 change note. **Final micro-pass:** §16.4's D1 billing-metric citations re-pointed to the pricing page; §27.1's "Prompt 8 unstarted" line marked superseded |
| `stage-1/02_strengths_weaknesses_player_frustrations.md` | **One declaration note added 2026-10-23** | §9 states the register's 28 defined entries, F-007/F-028 unassigned, F-003b a sub-ID (DEF-008). No finding, label, or number changed |
| `qa_backups/08_part6.md` | **Repaired 2026-10-23** | Historical banner added; the one broken relative report link now resolves to `../stage-1/08_…`. Content unchanged |
| `stage-1/09_integrated_design_synthesis_and_readiness_audit.md` | **Edited 2026-10-23** | This correction pass: DEF-016/017/018 registered; GATE-03 re-evaluated; QA/handoff/change log updated |
| `qa_backups/validate_final.py` | **Re-purposed 2026-10-23** | Replaced four stale "Prompt 9 not started" assertions with current-state checks; retained the valid ID/link/decision/code checks |
| `qa_backups/09_validate.py` | **Extended 2026-10-23** | Correction-pass assertions added; docstring's DEF count corrected 15 → 18; F-register check scoped to §9 rows and strengthened (asserts F-007/F-028 absent, F-003b present) |

**No production code, schema, configuration, or framework choice was added.**

### 23.3 Continuity summaries (what the files now say)

**AI_CONTEXT.md:** Prompt 9 is complete; Stage 1 is **not complete**; the readiness verdict is **conditionally ready**; the ₹0 required-cost objective is recorded as an owner-stated constraint with its limits; the report is indexed; the top risks now include free-tier capacity and the CP/FPB scope ambiguity.

**AI_HANDOFF.md:** the next session is told to read AI_CONTEXT → AI_HANDOFF → PROJECT_PROGRESS → this report; Prompt 9's findings and counts are summarized; D-004/D-005 remain Provisional; the next task is owner decisions OD-01/02/03/06 plus the free-tier measurement spike — **not** implementation.

**PROJECT_PROGRESS.md:** row 9 is **Complete** (report delivered; QA run); Stage 1 remains **incomplete** because three gates are conditional (13/16/18); the zero-cost status is **conditional**; the next action is recorded. The 2026-10-23 correction passes closed the two P8 staging defects, DEF-008's declaration gap and GATE-03; the final acceptance micro-pass added no status change beyond those.

**DECISIONS.md:** inspected and unchanged. D-001…003 Confirmed; D-004…006 Provisional. No hosting choice, scope choice, or ₹0 policy was recorded as approved.

### 23.4 Instructions for the next session

1. Read [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md), and [DECISIONS.md](../DECISIONS.md) before acting.
2. Read this report's §15 (decisions), §17 (zero-cost), §19 (next stages), and §20 (gates). Do not rely on this summary alone.
3. Do not start Stage 2, write code, or choose a framework without explicit owner authorization (D-002).
4. Treat D-004 and D-005 as Provisional; do not cite this report as approving Cloudflare, D1, OP, or any scope. Treat P7's **DEF-018** (whether a pending trade offer reserves the proposer's assets) as an open economy-stage decision, not as a settled rule.
5. If asked to proceed, the smallest authorized step is the owner-decision closure plus the free-tier measurement spike (PV-01…PV-07).
6. Re-run `python qa_backups/09_validate.py` after any edit to this report or the continuity files; it is intentionally strict about counts and links.

### 23.5 Blockers that remain after this report

| Blocker | Owner | What unblocks it |
|---|---|---|
| CP/FPB scope ambiguity (DEF-001/002) | Owner | OD-02 recorded |
| Quota-exhaustion policy | Owner | OD-01 recorded |
| Backup/recovery tier | Owner | OD-06 recorded |
| Boundary CPU/subrequest fit | Engineering | PV-01…03 |
| Write/storage fit | Engineering | PV-04/05 |
| Turn ordering catalog | Architecture | SDQ-018 |
| Trade offer reservation rule | Economy design | DEF-018; OD-03 context |
| Economy numerics | Design | ECOQ-002/004/005 |
| War rules | Design | Dedicated stage (OD-12) |
| Account/abuse/moderation stack | Engineering/ops | Stage B; OD-05/08 |

---

## Appendix A — Source register

### A.1 Internal sources

| Source | Path | Used for |
|---|---|---|
| Master context | [AI_CONTEXT.md](../AI_CONTEXT.md) | Constraints, concept, status |
| Handoff | [AI_HANDOFF.md](../AI_HANDOFF.md) | Pipeline, decisions, prior findings |
| Progress | [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) | Prompt status and QA history |
| Decisions | [DECISIONS.md](../DECISIONS.md) | D-001…D-006 |
| P1 | [01_competitor_research.md](01_competitor_research.md) | Genre, cadence, platform limits |
| P2 | [02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) | F/O registers, churn evidence |
| P3 | [03_feature_comparison_opportunity_analysis.md](03_feature_comparison_opportunity_analysis.md) | FO register, feasibility, dependencies |
| P4 | [04_target_audience_and_player_experience.md](04_target_audience_and_player_experience.md) | Audience, journey, V register |
| P5 | [05_core_game_concept_and_design_pillars.md](05_core_game_concept_and_design_pillars.md) | CX-5, pillars, CV register, CP boundary |
| P6 | [06_core_gameplay_systems_and_interactions.md](06_core_gameplay_systems_and_interactions.md) | SYS/INT/SDQ/R registers, tiers, timing |
| P7 | [07_economy_design_and_market_structure.md](07_economy_design_and_market_structure.md) | ECON/ECOQ/ECV/MAT/L/G, storage math |
| P8 | [08_security_privacy_fair_play_and_trust.md](08_security_privacy_fair_play_and_trust.md) | TH/SEC/ST/OSQ, privacy, reliability |
| QA | [09_validate.py](../qa_backups/09_validate.py) | This report's checks |

### A.2 External sources (accessed 2026-10-23 unless noted)

| Source | URL | Used for |
|---|---|---|
| Cloudflare D1 limits | https://developers.cloudflare.com/d1/platform/limits/ | 500 MB/database, 5 GB/account, 100k writes, 5M reads, 50 subrequests, 7-day Time Travel, single-threaded, 30 s SQL |
| Cloudflare Cron Triggers | https://developers.cloudflare.com/workers/configuration/cron-triggers/ | UTC execution, underutilized machines, no documented exactly-once guarantee |
| Cloudflare Pages limits | https://developers.cloudflare.com/pages/platform/limits/ | 500 builds/month, 20,000 files, 25 MiB/file, 100 projects |
| Cloudflare R2 pricing | https://developers.cloudflare.com/r2/pricing/ | 10 GB-month, 1M Class A, 10M Class B, free egress |
| Cloudflare Workers limits | https://developers.cloudflare.com/workers/platform/limits/ | 100k requests/day, 10 ms CPU (read by P7 on 2026-10-22) |

**Not re-verified this pass:** Resend/Brevo daily caps, Sentry/UptimeRobot/Better Stack allowances, GitHub Actions minutes, Better Auth licensing, Durable Objects free limits, Workers Logs retention, R2 payment-method requirement. They are marked Medium/Low in §17.3 and must be checked before they are used in a commitment (PV-09/PV-10).

---

## Appendix B — New identifier families introduced by this report

| Prefix | Count | Purpose | Where defined |
|---|---|---|---|
| **REQ** | 39 | Integrated requirements traceability | §12 |
| **ZD** | 14 | Zero-cost operating components | §17.2 |
| **GATE** | 20 | Stage 1 readiness gates | §20 |
| **DEF** | 18 | Defect register | §14 |
| **OD** | 12 | Owner decisions | §15.2 |
| **PV** | 15 | Free-tier/capacity validation | §13.3 |
| **TQ** | 17 | Technical questions for architecture | §18.2 |
| **Total** | **135** | | |

No existing family was renumbered, merged, or reused. SEC-009 remains reserved; the five retired ECON IDs remain retired; the F- and O-register gaps are declared, not filled.

---

## Appendix C — Change log for this pass (2026-10-23)

| Change | Detail |
|---|---|
| **Created** `stage-1/09_integrated_design_synthesis_and_readiness_audit.md` | This report (Sections 1–23 + appendices) |
| **Edited** `stage-1/03_feature_comparison_opportunity_analysis.md` §7.7 | Undefined O-15/16/17 and mislabelled O-12 → FO-012/015/016/017 and FO-001/005/006/007/008 (DEF-007) |
| **Updated** `AI_CONTEXT.md` | Prompt 9 complete; Stage 1 not complete; conditionally ready; ₹0 constraint; 09 indexed; risks updated |
| **Updated** `AI_HANDOFF.md` | Prompt 9 row/state/findings; next task = decisions + measurement |
| **Updated** `PROJECT_PROGRESS.md` | Row 9 complete; Stage 1 status; continuity table |
| **Unchanged** `DECISIONS.md` | Inspected; no approvals added; D-004/D-005 Provisional |
| **Created** `qa_backups/09_validate.py` | Read-only validator |
| **QA** | 24/24 initial report checks + six correction-pass checks pass; validator 50/50 before the correction pass (see §22) |
| **Correction pass 2 (2026-10-23)** | P8 DEF-004/005/010 fixed and verified; P7 DEF-016/017 fixed and DEF-018 recorded as an open ambiguity; GATE-03 re-evaluated to Pass (17/3/0); P8 handoff updated; legacy validator re-purposed; continuity files updated; DECISIONS still unchanged |
| **Identifier fix in this report (2026-10-23)** | §12.2 REQ-021's Systems cell read `SYS-015/031`, naming a system number (`SYS-031`) that does not exist in Prompt 6's 18-system catalog. Corrected to `SYS-015`; SEC-031 was already cited in the same row's source column, so no reference was lost. No requirement text, status, priority, validation path, or count changed |
| **Final acceptance micro-correction (2026-10-23)** | Four issues closed: (A) the §2.1/§22.1/§22.2 reading-depth statements now agree that P7 and P8 were read end-to-end in the 2026-10-23 passes; (B) `09_validate.py`'s docstring DEF count corrected from 15 to 18 (the check already expected 18), with the F-register check scoped and strengthened; (C) DEF-008 closed by a declaration note in P2 §9 and §21.4's "no other report needs editing" qualified; (D) `08_part6.md` given a historical banner and a working link. P7 also received two documentation-only fixes (§16.4 citation re-point, §27.1 superseded status line). No gate result changed |
| **Source-citation correction in §17.3 (2026-10-23)** | The rows-read/rows-written/storage allowances were attributed to the D1 limits page; they are stated on the D1 pricing page, which was re-read on 2026-10-23. Citations corrected (figures unchanged), the documented index write-amplification rule added as row 19, and rows 6–8 de-ambiguous from "Same" |

**End of report.**

