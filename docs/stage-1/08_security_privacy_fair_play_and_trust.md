# Project X — Stage 1, Prompt 8: Security, Privacy, Fair Play, Anti-Exploit Design, Reliability, and Player Trust

**Version:** v1.1 (2026-10-22; 2026-10-23 correction pass 2 — DEF-004/005/010 corrections and handoff update)
**Status:** Research-stage proposal. **Nothing in this report is approved.** Per [DECISIONS.md](../DECISIONS.md) D-003 and the project's "no approvals by implication" rule, every requirement, control, threshold, and policy stance below is a **recommendation**, not a decision. New prefix families introduced here: `TH-###` (threats), `SEC-###` (security requirements), `ST-###` (security validation tests), `OSQ-###` (open security questions). Each prefix's absence from the project was verified before adoption (see §0.2).

**Status of the next prompt (updated 2026-10-23):** Prompt 8 was explicitly authorized by the user. This report's original header said "Prompts 9+ are not [authorized]"; that statement was true when written and is now **superseded** — the owner later authorized Prompt 9, which was executed on 2026-10-23 ([09_integrated_design_synthesis_and_readiness_audit.md](09_integrated_design_synthesis_and_readiness_audit.md)). Stage 1 remains incomplete; see §26.9's updated handoff.

---

## 0. Front matter

### 0.1 What this report is

Project X's security-and-trust brief: what can go wrong, who could do it, what the rules must be, which protections are mandatory before the first public build, which controls can safely wait, what it costs on a free-first budget, and how incidents, appeals, and disputed outcomes are handled fairly. It is written so that a later AI or human implementer can implement and test protections **without inventing missing security rules** — every load-bearing statement is traceable to a threat, a requirement, or a test.

Security here is not a login screen. For a persistent multiplayer nation-strategy game, the security surface is: account control, server-authoritative game state, economic integrity (Prompt 7's whole subject, now continued), diplomacy and alliance permissions, the 2-hour turn pipeline, automation and service abuse, player privacy, moderation with fair appeals, audit evidence, and recovery from failures. Each gets its own section and its own register entries.

**Scope boundary:** this is design, not implementation. No production code, no provider commitment, no combat mechanics invented (the war stage owns that, per the Prompt 6 handoff), and no numerical thresholds invented where a project rule already defers them to a later stage (ECOQ-002/004/005 style). Where this report must state a control parameter to be concrete (e.g., "rate limit per action class"), the value is recorded as a **proposed starting posture to be tuned**, never shipped as truth.

### 0.2 Source documents read for this report

| Ref | Document | Used for |
|---|---|---|
| [SRC-1] | [AI_CONTEXT.md](../AI_CONTEXT.md) | Confirmed constraints (§2), claim-type discipline (§4), open-question recap (§7) |
| [SRC-2] | [AI_HANDOFF.md](../AI_HANDOFF.md) | Full prior-register inventory (B), state (C), decision-log summary (D), findings (F), open questions (G, items 1–20) |
| [SRC-3] | [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) | Completion statuses; correction-pass history |
| [SRC-4] | [DECISIONS.md](../DECISIONS.md) | D-001…D-006 verbatim; no modification made |
| [SRC-5] | [01_competitor_research.md](01_competitor_research.md) | Genre security/anti-abuse precedents (P&W automation + young-nation trade rules, beige/protection engineering, verification norms); information-security posture of competitors; **D1 free-tier limits (100k row-writes/day)** documented at Section 6 |
| [SRC-6] | [02_strengths_weaknesses_player_frustrations.md](02_strengths_weaknesses_player_frustrations.md) | F-001/F-029 watchlist (botting unverified), F-016/F-017 exploit families, F-018 alliance-admin burden, F-006/F-013/F-015, O-1…O-12 |
| [SRC-7] | [03_feature_comparison_opportunity_analysis.md](03_feature_comparison_opportunity_analysis.md) | FO-002/003/004/009/010/011/013/014 (Group A), FO-018–FO-023 statuses; Section 8's Integrity-High market warning; P&W war-action economy facts (MAP budget) |
| [SRC-8] | [04_target_audience_and_player_experience.md](04_target_audience_and_player_experience.md) | PXE-001…019 (011 moderation-capacity plan), PR-1…10, fairness axes §13.1–13.2, V-1…V-10, personas |
| [SRC-9] | [05_core_game_concept_and_design_pillars.md](05_core_game_concept_and_design_pillars.md) | CX-5, DP-001…006, AP-001…008 (esp. AP-002/AP-003), UXD-005 (adversarially-designed fairness — this report is its continuation), CCR-001…012, first-playable boundary E1–E6/S1–S5/O1–O6, CV-001…006 |
| [SRC-10] | [06_core_gameplay_systems_and_interactions.md](06_core_gameplay_systems_and_interactions.md) | SYS-001…018 catalog and tiers, INT-001…014, SDQ-001…018 (P0 set), SIM-001…012, MO-001…008, R-01…R-12 (integrity register this prompt extends), §17 three-class timing contract, §15G OP analysis (D-004 untouched) |
| [SRC-11] | [07_economy_design_and_market_structure.md](07_economy_design_and_market_structure.md) | ECON-001…023 registers, ECOQ-001…013, MAT-01…05, L- lines, G-1…G-6 gate, R-13…R-21 (economy integrity extension), §14 timing classification, §15 finance interface, §16 storage/write budget + S1–S3 fresh research, EX-1 scenarios, §18 paper tests, §19 first-playable boundary, ECV-001…005 |

All seven prior reports and all four continuity files were read in full (or their referenced registers read at the row level); no file in the project is assumed or summarized secondhand where its content mattered. The latest Saved Prompt 7 report is the v1.1 file with its 2026-10-22 correction pass **and** final micro-correction applied (see [AI_HANDOFF.md](../AI_HANDOFF.md) item 20); no outstanding Prompt 7 documentation defect exists at write time.

### 0.3 Document map

| Section | Content |
|---|---|
| 1 | Executive summary |
| 2 | Project-specific threat model (threat register TH-001…TH-025) |
| 3 | Assets and trust boundaries |
| 4 | Account security and recovery |
| 5 | Server-authoritative game state and request integrity |
| 6 | Turn scheduler, duplicate processing, and time abuse |
| 7 | Economic security and market abuse (against Prompt 7's actual economy) |
| 8 | Alternate accounts, collusion, and coordinated abuse |
| 9 | Bots, automation, and service abuse |
| 10 | Diplomacy, alliance, and strategic-conflict integrity |
| 11 | Privacy and data governance |
| 12 | Moderation, reports, sanctions, and appeals |
| 13 | Audit logging, detection, and evidence |
| 14 | Reliability, backups, restoration, and incident response |
| 15 | Free-first security and cost control |
| 16 | Security requirements and priority levels (register SEC-001…SEC-033 with SEC-009 reserved — 32 defined, per §16/§24) |
| 17 | Prioritized security roadmap (A / B / C) |
| 18 | Failure scenarios and abuse walkthroughs (18 scenarios W-18-A…W-18-R) |
| 19 | Security testing and validation plan (test register ST-001…ST-020) |
| 20 | Trade-offs, options, and owner decisions (OSQ-001…OSQ-012) |
| 21 | Evidence and source quality |
| 22 | Cross-system consistency audit |
| 23 | Final recommendations and open questions |
| 24 | Identifiers and registers |
| 25 | Quality-assurance record |
| 26 | Handoff to the next stage |

## 1. Executive summary

### 1.1 The question this report answers

**What must Project X do — and explicitly not yet do — so that its economy, its 2-hour turn world, its player accounts, and its community are protected against realistic abuse at a scale-appropriate cost, with every protection traceable to a threat, a testable requirement, and a fair appeal path?**

### 1.2 The core position in one paragraph

Project X's defense should lean, as Prompt 7's economy already does, on **authoritative servers, invariants, and honest records rather than on surveillance**. The browser is an untrusted display layer; every valuable outcome is computed by the server inside a defined trust boundary with an audit trail; every economic mutation obeys the already-designed invariants (single pool with no debt and no interest, atomic-pair/zero-partial trade settlement R-19, no-yield-on-cash, deterministic boundary resolution with published tiebreaks). Against the register's 25 threats, the report defines 32 testable requirements — 12 of them "Required: first playable", 11 "Required: pre-launch", 9 "Later hardening" — plus 20 planned validation tests (none executed) and 12 explicit owner decisions. The dominant theme is that the game's *determinism and smallness* are security advantages to be kept: a prompt class that trusts the server for arithmetic, prices failure with reasons, and discloses its own states (DP-004; UXD-005 "adversarially-designed fairness" is literally this prompt) removes most of the incentive for client-side attacks *and* most of the evidence burden of policing them.

### 1.3 The most important risks

Ten findings, prioritized:

1. **The turn pipeline is the game's crown jewels** — a single scheduler resolving 12 turns/day across all nations carries every economic value (SYS-016). Duplicate processing, partial processing, or a badly-recovered crash can silently mint or destroy value at global scale with no attacker at all (TH-009/TH-010). This is why exactly-once discipline (idempotency keys, turn-state ledger, checkpointed resume) is a first-playable requirement, not a hardening item.
2. **Client trust assumptions must be explicit from line one** — users who modify client-visible values, replay requests, or race two concurrent actions are testing the server's authority (TH-006/007/011). Server-side recomputation of every valuable quantity (SEC-010/11/13) is the anchor requirement; Prompt 7's §14 already priced the honest-preview rule (promise only what the boundary guarantees).
3. **Multi-accounting and funneling is the genre's verified #1 economic abuse** (Prompt 1/3 registers; R-01/R-13) and it is cheap to attempt (TH-003/005/020). The economy's own design expects it: fresh-account restrictions and per-pair velocity caps are already *inside* the economy report's trade rules. This prompt turns them into testable security requirements and defers the policy question (prohibit / restrict / permit-with-conditions) to the owner as OSQ-001.
4. **Shared-IP evidence is too weak to act on alone** (TH-003's false-positive branch; walkthrough W-18-G). Households, campuses, and cafés all share addresses; detection must be behavioral (trade-graph shape, timing, value flows) with conservative review, never automatic punishment. R-13/R-16's conservative-response posture is reaffirmed project-wide.
5. **Account recovery is the most dangerous trust product the game will offer** (TH-001/TH-002): a weak recovery flow converts a compliance checkbox into an impersonation tool. The design: email-bound identity, rate-limited recovery, no in-game-asset proof games (no "prove your balances to recover" quizzes), a contention/lockdown grace window, and honest limits on what is recoverable — no promises beyond what verification can support.
6. **A tiny ops team is a moderation resource constraint** (PXE-011), so player-trust tooling must be built around **proportionate, audited, evidence-based process** — not headcount. SEC-026/27 define a sanctioned-actions ladder with elevated permission for destructive actions, logged moderator actions, one report → one reviewer ≠ one judge (appeals go to a different reader where staffing allows), and a two-person rule for the most destructive operations. Fewer, well-documented powers beat many.
7. **Free-first hosting makes quotas a functional attack surface** (TH-012): on the D1 free plan's 100k row-writes/day (Prompt 1 §6, enforced since 2026-09-01) and the free plan's 10 ms cron CPU (Prompt 7 §16.4 S2), a single abusive client could freeze the day's economy by exhausting writes. Per-action-class quotas and lightweight abuse monitoring are therefore *baseline* controls, not luxuries.
8. **Automation's line must be drawn at competitive advantage and service health, not at curiosity** (TH-013/TH-025). Read-only community tools and accessibility aids are to be accommodated where feasible; automated *action* injection that beats a human to a boundary (boundary sniping) or floods queuing is restricted. No intrusive anti-bot (no CAPTCHA walls on gameplay, no device fingerprinting) is adopted by default — cost, accessibility, and false-positive risk analyzed in §9.
9. **Privacy must be minimized to be survivable** (TH-024): the fewer personal data categories collected, the smaller every future breach, disclosure, retention, and legal problem. §11's inventory keeps first-playable data to account identifiers, gameplay state, security events, and short-retention network metadata — and explicitly *not* precise location, government IDs, or private-message accrual (no privatemessages channel is proposed at first playable).
10. **Every protection rides on an evidence spine** (SEC-031): a defined event ledger (what happened, to which turn/transaction, by whom, observed how) is what makes appeals fair, sanctions reviewable, and post-incident reconstruction possible — and it is also the data boundary that must itself be protected. Logging is scoped to security-relevant events only (§13), never the surveillance system that the economy report already refused to build.

### 1.4 Protection staging at a glance

| Stage | Counts | The load-bearing items |
|---|---|---|
| **A. First playable** (cannot ship as a fair game without) | 12 requirements | SEC-010 (authoritative recompute), SEC-011 (per-action validation), SEC-012 (per-nation authorization scoping), SEC-013 (input bounds + integer guards), SEC-014 (idempotency keys / dedup), SEC-016 (single-spend atomicity + no-debt invariant), SEC-018 (deterministic tiebreak at boundary — already the Prompt 7 §14 contract), SEC-019/020/021 (single resolution window + checkpointed turn ledger + safe duplicate handling), SEC-025 (server-side no-negative/no-overflow), SEC-029 (per-action-class quotas — free-tier insurance) |
| **B. Public launch** | 11 requirements | Account hardening stack (SEC-001…005, 007/008 — the single-operator caveat keeps SEC-006's deeper separation in stage C), abuse-control suite under test conditions (SEC-023), moderation ladder (SEC-026; SEC-027/028's tooling follows in stage C with staffing), backups + restore discipline (SEC-030), audit spine completion (SEC-031) |
| **C. Later hardening** | 9 requirements | Advanced analytics, automation-pattern analytics, deeper audit tooling, review peripherals, ML-free anomaly helpers, expanded incident tooling, offensive red-team cadence, data-subject tooling, formal recovery drills at scale |

### 1.5 The largest trade-offs (cost / friction / privacy / integrity)

- **Idempotent-everything vs. write budget:** every idempotency-key check and event row costs D1 writes against 100k/day. §15 uses Prompt 7's §16.3 framework to size the economy's floor and shows where logging can be sampled instead, but states plainly that integrity logging cannot be sacrificed to quota — it can be *tiered* (full rows for money/diplomacy/war events, sampled for reads and analytics).
- **Friction vs. accessibility:** this project's audience promise (5–15-minute check-in sessions; DP-002 decisions-over-presence) means aggressive friction (aggressive CAPTCHA walls, forced MFA on every login, verified-only trade) would contradict the validated concept. §16's priorities opt for *defense-in-depth at the server, minimum friction at the client*, with optional step-up verification for sensitive actions only.
- **Privacy vs. abuse-police convenience:** IP addresses and behavioral telemetry help detect multiboxing, but retaining them long turns the game into a surveillance system that Prompt 7 explicitly rejected and that peaceful households would feel as invasiveness. The recommended posture: short-retention network metadata for the abuse-signal pipeline, behavioral/graph evidence where it's available, and no long-life personal-profile store.
- **Automation-accessibility vs. competitive fairness:** the compromise is a published automation policy (what the client may do, what tools may read, what timing is honored) created *with* the community, not a cat-and-mouse fight the team can't staff.
- **Recovery guarantees vs. free-tier reality:** backups on the free tier are a real constraint; the recommended posture is a daily snapshot + restore drill cadence with an assumed RPO of ≤24 h and no manufacture of guarantees beyond what testing can support — stated as an assumption, not a decision.

### 1.6 Highest-priority unresolved questions

recorded in §20, the four that shape the most:

- **OSQ-001 Multiple-account policy** (prohibit / restrict / permit-disclosed): a genuinely strategic, social-design-dependent call the owner must make; §8 lays out options and its recommendation (restrict to one nation per account at launch, conditions later only if evidence justifies) without pretending an approval exists.
- **OSQ-004 What automation is allowed** — the rules text must ship with the game (O-10 family) and be decided before launch.
- **OSQ-010 Privacy/legal jurisdiction review** — the game will be publicly reachable globally; the applicable data-protection regimes must be assessed against actual launch markets, which is an owner-held call requiring counsel, not a checklist claim.
- **OSQ-007 Recovery-guarantee tier:** what RPO/RTO the owner will pay for, since every tier of recovery product answers a real-player value question ("can I lose my nation to an ops error?") and a real cost.

### 1.7 Status discipline

**Recommended ≠ approved.** Everything in §16 is a *proposal* with an acceptance criterion; the acceptance of each requirement is an owner decision under D-003's rule, and none of the 32 has one. **D-004 (OP)** remains provisional; the subjectmilitary/conflict surface here touches it only as an *unresolved dependency* (SDQ-008 war-stage design not started). **D-005 (Cloudflare Workers/D1)** remains provisional; §15's cost analysis is *scenario work against a candidate*, not a selection. No permission checks against any provider API were performed. No penetration testing, no live incidents, and no execution of any test exist: all 25 threats are **design assessments of a paper game** (except where a genre precedent is explicitly quoted from a prior report).

---

## 2. Project-specific threat model

### 2.1 Method

Actors, assets, trust boundaries, entry points, and consequences were enumerated from the actual gameplay surfaces (Prompt 6's 18-system catalog; Prompt 7's economy; Prompt 4's audience/journey), then every plausible abuse path was analyzed as to the minimum capability it requires. Each threat entry answers: what can an adversary of matching capability (or a careless operator, or plain misfortune, because failures are threats too) accomplish, how likely is it, how bad if it lands, and what combination of prevention, detection, and recovery handles it *within this game's own rules*? Genre evidence (Prompt 1/2/3's verified precedent rows) drives likelihood up where the genre demonstrably sees that attack; intuition or absence of evidence is labeled. No threat below is an **observed incident in Project X** — this game doesn't exist yet.

### 2.2 Risk scale (deliberately ordinal, no false precision)

| Axis | Meaning | Values |
|---|---|---|
| Likelihood (L) | Probability the threat occurs in a year of applicable operation, judged from genre evidence + tooling cost + incentive | 1 Rare · 2 Unlikely · 3 Possible · 4 Likely · 5 Very Likely |
| Impact (I) | Damage to players and project if realized | 1 Negligible · 2 Minor · 3 Moderate · 4 Major · 5 Severe |

**Priority = L × I read as direction bands**, not a scorecard: `1–6 Low` (accept with monitoring), `8–10 Medium` (specific single control suffices), `12–15 High` (requires designed prevention before applicable stage), `16–25 Critical` (must not be possible at the protection stage that ships the affected asset). The multiplication is a shorthand for "this dominates that," never a claim of calibrated correlates. Every threat carries its reasoning line; ids for mitigations point to §16.

### 2.3 Threat register (25 entries)

| TH | Short name | Asset / system attacked | Capability & access needed | Scenario (preconditions) | L·I (reason) → Priority | Mitigations (SEC) / Inherited controls | Detection | Recovery / containment | Residual risk & validation (ST) | Cross-refs |
|---|---|---|---|---|---|---|---|---|---|---|
| TH-001 | Credential stuffing / account takeover | Player accounts, sessions, then their treasury/allies/wars | Lists of leaked email:password pairs; ordinary web access; no game skill | Precondition: password-only accounts and no rate limit. Attacker replays breach lists against login/recovery; compromised nations receive hostile instructions. | L4 (credential stuffing is the internet's ambient noise; targets scale with population) · I4 (nation + alliance + funds compromised) → **16 Critical** | SEC-001 (unique identity), SEC-002 (modern password handling + optional step-up), SEC-003 (session issuance/revocation), SEC-005 (attempt rate limits + delay), SEC-007 (notification on sensitive-account changes) | Failed-auth spike per account/device; post-login behavior change (new orders transferring funds) flagged for review per SEC-031's rules; account-holder report | Session revocation issued on compromise report; optional password reset; rollback *not* automatic for in-game actions taken during the window (§4.5's evidence-based review; SEC-008) | Attacker with credentials *can* act quickly; the goal contains damage, not perfection. ST-013 | F-029 watchlist; SYS-018 onboarding; V-3 persona stress; PXE-017 (untouched) |
| TH-002 | Session hijack / token theft | Live sessions; in-progress orders | XSS-class web attack or token mishandling by the client | Precondition: long-lived tokens reused across logins, or a campaign of link-clicking with no session-binding discipline. Replays an authentic session token. | L2 (XSS known-class risk; novel small app; OWASP Session Management cheat sheet's absolute-timeout posture cited) · I4 (full control until revocation) → **8 Medium-High** | SEC-003 (short absolute timeout, rotation, revoke-on-logout), SEC-002 (no token in URLs), SEC-031 (session events logged) | Concurrent session anomaly; impossible-travel hints (proposed, cautious — never sole evidence) | Victim or automated monitoring revokes; all sessions rotated on password change | Competitive damage possible inside one turn window; without request-level binding, nothing stops fast in-session strikes. ST-014 | ECON-013's orders (Prompt 7); persona Mira (Prompt 4) |
| TH-003 | Multi-account funneling / value transfer | Economy (treasury, MAT), trade ledger, integrity statistics | Web access; time; several email inboxes (or one account per household, misused) | Precondition: multiple accounts allowed or undetected; fresh-account restrictions absent/bugged. One player runs N nations, directs all surplus across trades to a dominant nation (R-13's vector). | L4 (genre-verified top abuse family; cheap tooling) · I4 (distorts competitive integrity + economy) → **16 Critical** | SEC-023 (fresh-account window, per-pair velocity caps, transfer-graph rules **under test conditions**), ECON-013's directed-trade restrictions (P28-class precedents [FV] per Prompt 1/3), R-13 controls, R-16's conservative-response design (overlap review only) | Trade-graph shape: per-pair asymmetry cap breaches; circular/self-trading patterns flagged to reviewers (R-13/R-16's postures); manual reports | Review-then-act: accounts escalated one queue; no automated resource clawback at launch (R-16: conservative) | If multi-accounting is policy-*permitted*, "abuse" becomes contract violation, not exploit, and enforcement runs on policy grounds — the distinction matters and is OSQ-001's subject. ST-016 | R-01/R-13/R-16; ECON-013; F-016/F-017; Prompt 3 §8; FO-009 |
| TH-004 | Coordinated market manipulation / wash trading | Trade records; reference-price statistics (G-4 layer; only after gates) | Web; N colluding accounts; know the fee/price model | Precondition: reference prices or any public price signal exists (post-G-1…G-6 listing market only). Wash-trade synchronously to bias day-end aggregates. | L3 (needs the market to exist + collusion) · I3 (corrodes price signal; other players mis-spend) → **8 Medium** | ECON-018's G-4 gate explicitly conditions listing on manipulation-pattern review; R-14's day-window aggregates **designed for self-pair exclusion** (project's own economy spec, SEC-031's trade evidence); SEC-024 (evidence retention) | Day-window aggregate anomaly; self-pair/circular-volume pattern; per-pair repetition rates | Remove the price influence from the affected aggregates (day-window correction) and name the pattern publically per DP-004 disclosure discipline | Directed-first market at launch has *no public price to corrupt* (no published price) — a structural reduction inherited from ECON-013's model. ST-017 (market-stage only) | R-14/R-15; ECON-015/018; G-4; Prompt 3 §8; F-020? (not cited; skip) |
| TH-005 | Alt-as-sabotage (burn the alt) | Same as TH-003 | Same as TH-003 | Precondition: protection windows or newbie-pool boundaries supply a *disposable* target. Player builds a throwaway nation, drives it into cash/assets (or into a toxically placed protection window), then gifts value out or swings a protection exploit. | L3 (genre evidence: F-017's protection-window engineering; alt-lever rare but cheap) · I2 (limited blast radius vis-à-vis TH-003 whose aggregate asset is wealth) → **6 Low-Med** | SEC-023 (fresh-account window caps *outgoing* value too — asymmetry rules), Prompt 7 R-13's transfer-graph rules make sustained funneling *visible* | Outlier transfer/one-way value flows from young nations; asymmetric wealth-flow outliers | Same as TH-003's review queue; protection-window parameters may need tuning, not enforcement | Zero-cost at paper level with backed restrictions; genre evidence says determined players will probe shape boundaries. ST-016 part 2 | F-017; FO-003/FO-017 (protection design — war stage); R-21 (absent counterpart) |
| TH-006 | Client-side value manipulation | Auth-server processing of any player-submitted quantity | Browser devtools; ability to re-issue modified requests; no server access | Precondition: server trusts any client-claimed quantity. "Pay 100" becomes "pay 1", "offer MAT-01 ×3" becomes ×300. | L4 (the standard first attack pass for any browser game) · I4 (infinite scarcity mint) → **16 Critical** | SEC-010 (server recomputes every valuable quantity from authoritative state), SEC-011 (per-action validation list — the server's own truth *always* wins), SEC-013 (input bounds + integer/dtype guards) | Malformed/out-of-domain parameter counters; authoritatively recomputed deltas that disagree with client-submitted ones are logged (harmless unless repeated — throttled per SEC-029) | Attack fails by design; request rejected with honest reason; nothing to recover if validation was complete | **Zero by design** if SEC-010–013 are implemented and tested; the residual is only for *any* client-trust leak, which is why ST-001–004 exercise each case. **ST-001/002** | §5; Prompt 6 §17 (immediate-not-possible contract); ECON-001 |
| TH-007 | Replayed / racing duplicate requests | Any stateful action (trade accept, order submit, campaign order) | Ordinary client; retry on flaky network; or a crafted duplicate | Precondition: action endpoints lack idempotency keys. A client retries after a response is lost — or *seeks* a duplicate — and the action settles twice. | L4 (automatic with any designed retry; also a natural traffic accident) · I3 (duplicated spend/reward — direct economy damage) → **12 High** | SEC-014 (idempotency keys per write-action; duplicates coalesce), SEC-016 (single-spend atomicity), Prompt 7 §14's two-checkpoint affordability model | Idempotency-key collisions logged; per-key duplicate counter | Duplicates coalesce to the first committed result; the response the client holds may point at either instance (a harmless alias) | **Zero by design** under SEC-014/16 properly implemented. Walkthrough W-18-A / **ST-005** | R-18 (order replay/queue flooding — Prompt 7); SDQ-018's idempotency contracts |
| TH-008 | Unauthorized action for another nation (IDOR/authorization miss) | Any player's nation: treasury, orders, diplomacy | Crafted request that swaps a nation/object identifier; authenticated but mis-scoped | Precondition: any endpoint resolving "do X for nation N" without a strict ownership/authority check. | L3 (_requires_ an authorizatioen bug, not a default API) · I4 (full account compromise without credentials) → **12 High** | SEC-012 (a per-resource authority table — every object's data carries `owner` labels resolved server-side, every action validated against it), Prompt 7 §11's per-nation framing (national data privacy posture) | Authorization failure events logged (matter-of-fact, per §13's classification: auth-fail ≠ suspicious alone); repeated cross-attempt flushes escalate per review | Attack fails if the auth table is complete; the *reason* is returned honestly (fail-with-reason contract, Prompt 6 §17) | **Zero by design** with complete authorization coverage; residual risk = yet-unknown business-rule exceptions, hunted by **ST-006** (spot-swaps on every action family) | SYS-002/003; INT-001 session→nation binding |
| TH-009 | Turn processed twice (duplicate scheduler run) | All world state (every nation), the entire ledger | No attacker required; misconfigured cron, horizontal scaling, or a retry-and-forget | Precondition: turn resolution lacks single-window locking or idempotent step keys. Two workers both resolve turn T; every nation's income, cost, and effect applies twice. | L3 (scheduler engines *can* fire twice — cloud providers' own docs advise idempotent jobs) · I5 (economy-wide corruption; systemic) → **15 High→Critical band** | SEC-019 (single authoritative resolution window — only one resolver enters resolution of turn T), SEC-020 (turn state ledger: turn T's phases commit staged checkpoints; a second claimer finds status `done` and exits without producing *any* player-visible change), SEC-017 (accounting ledger discipline — replay-safe event log in support) | Turn-state ledger exposes `done` + duplicate-claim attempts; resolver logs its worker identity; ledger row for turn T already exists | Second claimer exits no-op; if a run crashed halfway (*not* this threat), SEC-021's recovery governs. C4's post-incident protocol if it leaked | **Designed-to-zero**: acceptable residual is a crashed-and-stuck run (TH-010's domain). **ST-007** (run + re-run theorem) | Prompt 7 §14/SYS-016 three-class contract; EX-1 F scenario; SEC-015 |
| TH-010 | Partial turn processing (half-done resolution) | All world state | No attacker required; crashes, quota exhaustion, timeouts | Precondition: resolution is not atomic or has no checkpoint discipline. Steps land (production income via ledger rows), then resolution aborts (quota hit); some nations get income for turn T, others don't. Recovery re-runs from the top *without* skipping what was already applied. | L3 (12 turns/day of real compute; D1 quotas fixed and real (Prompt 1 §6)) · I4 (partial state means inequality between players — *worse* than both-or-neither) → **12 High** | SEC-020 (staged checkpoints: each phase commits a completion marker; a resume re-executes only *unfinished* phases), SEC-021 (dedup-of-already-done at phase grain, not turn grain), SEC-017 (appended event rows make "already applied" provable) | Before re-running: verify turn T's completed-phase markers exist and match their expected step set; any half-state is logged with the abort reason | Resume is always *forward-only* from the last committed checkpoint; a fundamentally inconsistent turn can be rolled back to the last *fully* committed turn (SEC-030) or held visible with an announced delay (SEC-022) — never silently re-derived | The mitigation is the thing to build; its absence is the game's worst ops risk. **ST-008/009** (partial-failure, resume-must-not-double) | SYS-016; SEC-019/20/21/30; walkthrough W-18-R |
| TH-011 | Stale turn-id / boundary race actions | Player actions near a boundary; turn fairness | Ordinary client + impatience; no server access | Precondition: a queued action carries the player's assumed turn number; the boundary passes; the action lands late. Three outcomes possible: (a) applied to T when the contract said T+1, (b) silently applied to T+1 without disclosure, (c) mis-priced (affordability checked against a boundary that's passed). | L4 (every committed player near a boundary hits this; “submit fast before the tick” is a genre instinct) · I2 (per-action value distortion only, because — per the timing contract — effects resolve at boundaries anyway) → **8 Medium** | **Stage-A prevention:** the server already stamps submitted actions under a published boundary rule through the resolver (SEC-018 deterministic boundary + SEC-020 turn ledger), and A9's fail-with-reason contract discloses the outcome class. **SEC-015 (Stage C) is the attribution refinement** — it makes the server stamp explicit end-to-end rather than implicit in the resolver. Prompt 7 §14's three-class contract; W-18-C; EX-1 scenario F | Server marks any action where submitted-turn ≠ resolved-turn and *returns that fact by reason* (honesty, per DP-004) | The player receives the failure/resolution with the class of outcome explained; no silent re-class behavior anywhere (a conditional presented as guaranteed is a DP-004 violation) | **Residual (accepted):** a client may still believe it acted in T when the server rules T+1 because the boundary closed between send and receipt; the action is disclosed with its class, never silently reclassified, and the stale-turn counter feeds review. This is a fairness-transparency residual, not a value-loss hole. **ST-010 is designed, not executed.** | EX-1 F; SEC-015/018/020; SEC-031 |
| TH-012 | Quota/written-budget exhaustion + request flooding | The whole service (all players), the free-tier providers | Ordinary client + cheap tooling; no skill needed | Precondition: no per-action-class quotas or connection-level cap. One client loops action submissions (the R-18 vector) until the day's D1 quota is spent, the free-plan serving budget is eaten, and turn T's resolution (itself write-hungry — SEC-019) fails mid-run. | L4 (zombie scripts are trivially findable and the target is a *free-tier* game, meaning the attack surface is the financial plan, not a firewall) · I4 (whole world's resolution stalls) → **16 Critical** | SEC-029 (per-action-class quotas + separate free-tier-reserving class for the *scheduler* — scheduler writes are never stealable by a user-triggered path), SEC-031 (rate-limit events logged per the table), exploratory per-user budgets with honest "you're temporarily capped" states | Rate-limit/throttle counters; quota-consumption dashboard against each free-tier allotment (100k writes / 5M reads / CPU: S1–S3) | Scheduler first: the turn engine's quota is protected by path (user-triggered writes are capped below scheduler need); abusive clients throttled; the game does not silently degrade a player's *already-validated* submitted actions to fit | Medium: a fully-saturated attack window can still degrade until restrictions close it. **ST-011** | Prompt 1 §6 (limits); Prompt 7 §16 (S1–S3); R-18; CCR-010; G-2 |
| TH-013 | Bot account farms / scraping / auth brute force | Accounts (chemistry to TH-001's outcomes) and read-only infrastructure | Script + proxy pools; zero game skill | Precondition: account creation unthrottled and unlimited, or read endpoints uncapped. Bot brigades create accounts (reputation noise, TH-016's rota), poll relentlessly, harvest snapshot history. | L4 (every public web service sees this) · I3 (tooling/allocation burden + distortion risk + scraped reputation data) → **12 High** | SEC-029 (rate limits for creation + login + reads), SEC-005 (login attempt caps from §4), SEC-001 (unique verified e-mail for account creation — but no e-mail verification if a free-first tier can't carry it: record as OSQ-003 and a §11 minimization decision), Prompt 5 AP-004-adjacent conduct (no forced identity), *no intrusive challenge by default* (§9's analysis) | Creation-rate anomalies; read-heavy per-account patterns; auth-failure spikes | Throttle/pause + (where evidence warrants) privileged review; no automated ban on the first signal (§13's "single weak signal" rule) | Bot brigades evolve; the posture is: **raise their cost ladder by stages, not one wall**. **ST-018** | Prompt 1 competitor facts; F-029; SEC-005/029; OSQ-003 |
| TH-014 | Credential guessing on one target | One victim account at a time | Scriptable; no prior breach lists needed | Precondition: password-only auth with no attempt caps and no lockout, or recovery endpoint is unthrottled. | L3 (notably lower than the TH-001 stuffing volume for a single site; targets single accounts) · I3 (one account's harm) → **8 Medium** | SEC-005 (per-account and per-source-rate attempt caps; lockout ladder per cheat-sheet guidance), SEC-002 (password hashing per §4.2's posture), SEC-004 (recovery is rate limited) | Attempt-rate outliers per login account/device | Account holder informed (SEC-007); transient lockout released with a human-legible reason | **Zero by design** to gain ingress through a throttled door; residual is the un-throttled *recovery* path. **ST-013** | SEC-002/004/005; OWASP auth guidance |
| TH-015 | Conduct toxicity: harassment, impersonation, deceptive nation names | Community channels, digests, names | Ordinary client | Precondition: society. Insults in trade notes, impersonation of moderators, slurs or deceptive similarity in nation names, etc. | L4 (society; genre and platform norms) · I2 (player harm is individual) → **8 Medium** | SEC-026 (conduct moderation ladder with evidence review), Name-guard at account/nation creation per the Prompt-5 identity posture (AP-004-adjacent; not forced profile identity), reported-abuse intake (SEC-028) | Player reports; ingest of conduct-relevant lines by moderation; name-guard in onboarding | Ladder of proportionate actions (§12.4); provenance rules for names replay (rename, forever record per constitution of record-keeping) | Community-dependent; moderation needs *human* review and cannot be fully automated. **ST-015** | F-001; PXE-011; §12; OSQ-005 |
| TH-016 | Report abuse / brigading / false reports | Moderation system; target players | Web; many accounts; zero skill | Precondition: report intake with no cost or anti-abuse check. A squad reports one player repeatedly ("getthispersonbanned" culture), or a well-writetn report's *words* gaslight a reviewer. | L3 (needs enemy somebody with motivation + time) · I2 (if unrestrained, prompts wrongful sanctions) → **6 Low-Med** | SEC-028 (report intake recorded; report-source identity visible *to the reviewer*; repeat-report clusters de-prioritized; an evidence-based review body — §12), SEC-026 (review proportion with a records trail) | Repeat-report patterns; cross-report concordance vs. evidence sample rate | An asserted falsehood does not itself sanction the reporter automatically; repeat false-reporting *is* a conduct violation (reviews on its own evidence) | Reviewer bandwidth is the residual. **ST-015** | PXE-011; §12 walkthrough W-18-N; OSQ-005 |
| TH-017 | Moderator abuse of powers | All moderation powers | Privileged account | Precondition: power without preparation or oversight. A mod uses logs/powers to settle a personal score, or edits an ally's history. | L2 (people trusted; but smallness means *any* is significant) · I4 (fundamental betrayal of the community) → **8 Medium-High** | SEC-027 (mod permission model — destructive powers require two-person rule; every act logged with reason; appeals path intact), SEC-031 (reviewer acts fully logged) | Full action log of every moderation event with the acting identity; anomaly review by *another* reviewer; missing-evidence censor flags blocked (an audit event that can't be silently removed) | Restrict/revoke, investigate honestly, disclose per DP-004; if the abuser is the owner's, cue the rest of the protocol to the owner (with its own conflict-of-interest rule) | Privilege abuse is detectable, not preventable — auditing *is* the control; no single-opinion review can prevent the first misdeed. Walkthrough W-18-O; **ST-019** | PXE-011; §12; OSQ-005/OSQ-012 |
| TH-018 | Compromised privileged/operator account | Ops control plane, all player data | Operator's password/phishing (targeting *the owner/ops*, not a player) | Precondition: one admin credential, one person. Phishing, session hijack, or device compromise of an ops account. | L2 (one-specific to tiny teams whose credentials live on a laptop) · I5 (full persistence + data exfil) → **10 High** | SEC-006 (admin accounts distinct from player accounts; separate long credentials; step-up auth on privileged actions; session scopes), SEC-008 (compromise runbook includes ops-account equivalent: revoke, rotate, audit *everything that account did*), SEC-030 (backups unaffected by compromised secret) | Privileged-login notifications; every admin-priv op logged with 2FA-verified identity; anomalous bulk down/exfil patterns | Rotate, audit (via SEC-031), restore if data was altered destructively (SEC-030), notify affected players per §14's communication protocol | Residual is the *detection window*; mitigation aims to keep it short. **ST-014** | SEC-006/008/031; OSQ-012 |
| TH-019 | Insider / excessive operator access | Everything; player trust | Ownership or employment (the trust relationship itself) | Precondition: the single-creator reality: the person who fixes the database can also read anyone's nation, sell info, or "correct" their ally's state. | L2 (requires insider intent — rare, deeply damaging) · I5 (community trust is *the* product's asset) → **10 High** | SEC-006 (least-privilege ops accounts; principle that ops *access itself* is logged), SEC-031 (privileged reads as events — yes, reading player data by ops is a logged event), disclosure-first playbook: announce the access rules to players (DP-004's "operators follow rules too" precedent-validated) | Privileged-access audit; anomalous read sweeps | Personal-error response: honest public disclosure; a trust breach is a *severity-1* incident per §14 (CC proposal: not pretend-buryable) | The most motivated dishonest operator can bypass logs. Acceptance-specific: multiple-person access control *as ownership structure* is an owner-stage infrastructure question (**OSQ-012**); the log is the mitigator available. Walkthrough **ST-019** | DP-004; §14's classification; OSQ-012; SEC-006; Prompt 5 UXD-005 |
| TH-020 | Sanction evasion via new accounts | The moderation and identity systems; the economy | Fresh email; free account creation; patience | Precondition: a banned player re-registers, quietly gains standing, resumes abuse. Prohibition-vs-multi-account questions entangle here. | L4 (ban evasion is specialized to abuse; at every allow-new-accounts open policy) · I2 (worse outcomes *if* sanctioned properly), else it just duplicates TH-003 | SEC-001 (unique account identity per person per policy), review-on-report; ban-evasion is an evidence-gated conduct case (per §12), not an IP-block habit (§8's shared-IP unreliability analysis) | Identity-transition-consistent patterns; report tips; reliance on conduct review not on IP | Re-sanction through the ladder; appeals remaining first-class; a wrongful accusation is itself a handled case (SEC-026's review flow) | Cost-of-evasion is proportional to *how much privacy data the game collects* — more data supports both evasion detection and false-evasion evidence, and that perception is part of §11's minimization review. **ST-015** | SEC-001/026; §8; OSQ-001 |
| TH-021 | Unauthorized/inappropriate alliance administration | Alliance treasury/tools/membership; reputation | Ordinary member or intruder; no coding | Precondition: permission roles too coarse, or the audit trail isn't reviewed. A member born of compromised *ally* account (TH-001's aftermath), or an ambitious member, quietly "ejects" rivals, empties a pool, or accepts a betrayal treaty. | L3 (a *post-compromise* threat; alliances are Tier C, but directed plans land early) · I3 (per-group social trust damage; worse with the pool) → **8 Medium-High** | SEC-012 (authority checks on every alliance verb — role-to-action config with explicit grants, never implicit), R-08's credit-audited pool posture (Prompt 6's register), SEC-031 (alliance-admin acts logged), Prompt 6 SDQ-014's permission model undeveloped (dependency: flagged) | Alliance role-change/membership-change events; pool transactions (R-08's redirect posture); ally reports it | Role revocation; recorded-recovery paths per the alliance tool's own rules: "what the alliance's rules *intended*" can be reconstructed from the event log; the **prevention**: depth = owner's own alliance-governance work (SYS-010's Tier-C timing) | Every alliance verb with a permission gate must appear in the role matrix; ST-006's inter-family scan covers it. **ST-006** | SYS-010; INT-003; SDQ-014; R-08 posture; F-018 |
| TH-022 | Diplomacy/campaign timing & forgery attacks ( WAR-STAGE-DEPENDENT ) | Treaties, war declarations, campaign orders, cooldown systems | Ordinary web clients; coordination | Precondition: SDQ-014's real diplomacy-state machine is uncovered (project hasn't decided it; Prompt 6 §15G's OP decision also open). What exists today: treaties minimal per SYS-009 + campaigns excluded (Prompt 6 D). | L3 Projected | I4 Projected → **12 High (projected)** | **Blocked by open design**: the war stage owns the question (SEC-022's *timing*/cooldown pressure requirements are generalized here; specifics route through SEC-019/20/21's idempotent/deterministic rails). Prompt 6's boundaries: campaign resolution excludes-outside-Tier-C; war-stage input list Prompt 7 §13.4. When it exists: a campaign order is a `queued` per Prompt-7 §14's classification; races at boundary resolved by the same deterministic tiebreak that governs trade. Attempted-forgery-of-instructions is plain TH-006/008's question. | Same as the economy rails above; attempt-and-revision forms noted in war-stage work | Same as SEC-019/20/21 family | **Design dependency, not scope**: war's rules don't exist yet (Prompt 6 §22.4's input list). Record as the war stage's invitation, not a system assumed here. **ST-020 (dependent)** | D-004; SDQ-008; SYS-011/012; Prompt 6 §15/§22.4; SEC-015/19/20/21 |
| TH-023 | Improper backup restoration (stale restore) | The whole authoritative state | No attacker required; the ops tool misused | Precondition: a restore pulls a snapshot from *before* the last boundary, or overwrites state after actions processed. Players' actions (trades) that DID settle reappear as live offers, or value multiplied cancels reflect lost honors. | L2 (restore is a rare event, but when it goes wrong it goes catastrophic-all-at-once) · I4 (every affected player's ledger wrong) → **8 Medium-High** | SEC-030 (restore = pre-verified, tested procedure; the *target* turn is explicitly named; a "corrections ledger" of processing events up-to-the-snapshot is preserved for reconciliation), SEC-031 (turn/txn event rows allow reconstruction), Prompt 7 §14's truthfulness contract: any correction is disclosed per DP-004's digest discipline | Restore dry-run discipline: after restore, the resolver checkpoint records exist *and* the ledger matches; a pre-post snapshot comparison tool catches anomalies | Replay missed turns *forward-only* from the restore point; disclose per DP-004; any player annulable-loss explicitly compensated per the incident protocol (§14), not invisibly | Design-level absence is the risk; the drill (ST-009) is the proof the system works. **ST-009** | SEC-030; §14 securities; EX-1 F |
| TH-024 | Privacy data exposure / inappropriate retention | Player personal data, security logs, ops data | Compromise of the data store or careless logging (a third-person risk, not adversarial intent-yet) | Precondition: collecting more than the minimum or leaking identifiers into public places. IP/email long-retained beyond need; ops logs that spill data; a restore dump without scrubbing. | L2 Projected | I4 Projected → **8 Medium-High** | SEC-032 (data inventory + minimization; §11's category table is authoritative), §11's retention table; SEC-031 (*identified* fields the log table *omits* — the log standard is itself a privacy control), SEC-030 (restore images scrubbed per §11) | Retention review as part of the §11 data-ops cadence; log-sampling privacy-log review | Downscope + delete per §11's rules; disclosed per DP-004's rules in an honest way, not a security-theater scanline | Privacy *loss* is un-stoppable once data exists; **minimization** is the only true defense = the reason this is a requirement and not a "best practice". **ST-012** | §11; SEC-032; D-003 (design decisions); OSQ-010 |
| TH-025 | Boundary sniping / unfair-advantage client automation | Competitive fairness; queuing fairness; economic prices | Scripting client calls timed to resolution instants; not service abuse per se | Precondition: the timing contract's boundaries are publicly known (they will be; DP-004) and the game accepts *faster-than-human* action bursts at the boundary as legitimate (as, e.g., "publish the rule, keep the edge" — acceptable!) vs. restricting queued-entry fairness as a rule violation. | L3 Projected (a genre-fix argument without verified players; appears in other games) · I2 (no resource corruption; *relative* advantage) → **6 Low-Med** | §9's classification (allowed tools vs. restricted automation); SEC-015 (server-side turn stamping — a "submit before T's boundary" is honored, not defeated), the resolve-at-boundary equalizer (DP-004 already says what will resolve and when — need to state the *rule* clearly), time-fairness contract written into the automation policy | Compiled in resolution-time analysis: an account's actions all land at the last-N-milliseconds window across many boundaries → file-reviewed for pattern evidence if the policy forbids it | Warning → restriction ladder per §12; the *service* isn't degraded by this behavior (SEC-029 has its own class) | **The rule itself must exist first** (OSQ-004). Until then, this is *projection*, not abuse. **ST-018** | DP-004; §9; OSQ-004; SEC-029; PR-1 |

### 2.4 Actor-to-threat coverage checklist

| Prompt-required actor | Threats that model it |
|---|---|
| 1. Ordinary legitimate players |They are the *system's* surface; TH-007/011 model the accidental harm (retry, boundary race); the protection design must not treat them as suspects (§8's household false-positive case) |
| 2. Rule-exploiting non-hack players | TH-003 (funneling "within the visible rules"), TH-005 (alt-as-sabotage), TH-011 (boundary timing), TH-021 (alliance-permission probing), TH-022 (projected) |
| 3. Bots / excessive automation | TH-013, TH-025, the TH-012 read/write pumping vector |
| 4. Multiple-account controllers | TH-003 primary; TH-005 (sabotage alt), TH-020 (evasion) |
| 5. Coordinated market-manipulation groups | TH-004 (primary; wash trading and price bias), TH-003's collusive-trade form |
| 6. Account-takeover attackers | TH-001, TH-002, TH-014 |
| 7. API/client-state manipulation | TH-006, TH-007, TH-008, TH-011 |
| 8. Service-quota disruptors | TH-012, TH-013's flooding face |
| 9. Malicious/compromised privileged accounts | TH-017, TH-018 |
| 10. Insiders with excess access | TH-019 |
| 11. False-reported / moderation abuse | TH-016 |
| 12. External attackers (accounts, service, exposed data) | TH-001/002/014's remote face, TH-012's service face, TH-024's data face — none of the *game* faces |

Also covered explicitly: failures without any adversary (TH-009/010/023) — the none-humans-to-blame class the prompt's own split demands; likelihood reasoning for each row above names its source (genre verification vs. ambient internet reality vs. pure projection).
The threat register deliberately does **not** include: piracy of game content (nothing proprietary is claimed, per the originality constraint), real-money trading (no such economy exists at first playable, and no payment rail is proposed — if that changes, the threat model must be re-opened), and nation-data theft between players (prompt 7's SDQ-004 keeps partners' terms private — privacy posture of trade data stays with SDQ-004's unresolved question).

---

## 3. Assets and trust boundaries

### 3.1 What must be protected (assets)

The asset list below is drawn from the actual gameplay surfaces (Prompt 6's 18-system catalog, Prompt 7's economy registers, Prompt 4's account/onboarding plans), not from a generic checklist. Each asset names who may see or change it at various trust levels — "owner-only," "group-readable," "all-player," "ops-only," "public."

| Asset | Contains | Sensitivity | Who may read | Who may write |
|---|---|---|---|---|
| Credential material | Password hash (Argon2id-class), password-hash parameters, e-mail address | Secret | Ops (break-glass, only for incident response) | Server only on registration/password change |
| Session tokens | Per-session random identifiers, issued/absolute-expiry, revocation state | Secret (token value), holder sees only their own metadata | Owning player (count/log, not values); ops for incident response | Server |
| Nation identity & ownership | Nation ↔ account binding, nation name, display profile | Player-readable to all (identity posture per Prompt 4 AP-002 — no forced real identity), nation data internally | All players (public identity fields); own profile privately | The owning account (within eligibility rules); server |
| Treasury & resources | Cash (single pool — ECON-001), MAT-01…05 stock, production queue | Owner-only values; aggregates may later be public if Prompt 7's transparency gates say so (G-1…G-6) | Owner; server; ops via SEC-031's logged privileged access | Server only |
| Development levels & emphasis | Line levels, specialization state (Prompt 7 §11; SDQ-016) | Owner-only | Owner; server; ops via logged access | Server only |
| Market listings, orders, trades | Open orders, accepted trades, cancellation state, settlement rows (R-19 atomic-pair ledger) | Per-nation private; partner terms semi-private — exactly Prompt 7's SDQ-004 question, unresolved | Owner, counterparty, moderator via evidence path (SEC-024/031) | Server only |
| Diplomacy & alliance state | Treaties, membership, roles, alliance pool ledger | Group-readable; private terms per SDQ-004 analog | Members (in-group); server; ops via logged access | Authorized roles per the alliance permission model (SEC-012 authority checks on every alliance verb) |
| War declarations / campaign orders | Queued orders, cooldowns, resolution state | Participants; public announcements per Prompt 6's disclosure discipline | Participants + per-design public digest | Server only |
| Turn position & resolution state | Turn index (T), phase checkpoints, resolution ledger | System data | Server; readable summaries disclosed per DP-004 | Resolver within SEC-019's single window |
| Player pending orders / actions | Queued action per nation | Owner-only | Owner (their own); server | Server |
| Moderation records | Reports, evidence, sanctions, appeals, moderator notes | Restricted — not visible to reported players beyond what the process discloses | Moderators (SEC-027/028 scope); owner ops | Moderators (audited) |
| Personal data | E-mail, summaries, security-event records for the account | Sensitive | Account holder; ops per incident | Server |
| Admin creds & operational secrets | Provider API keys, domain, deploy credentials | Secret — must never be in a client-visible surface or the database's player tables | Owner only | Owner ops |
| Audit event ledger | Security-relevant events (§13) | Restricted — internally shared, not player-facing by default | Moderators/ops via SEC-031's rules | Server |
| Backups / restore images | State snapshots, restore tooling | Secret — a full backup is every secret in one place | Owner ops only | Server/ops |

Two structural observations cut the protection problem down before anything is built:

1. **The state is small.** A nation-strategy game with 12 turns/day, no real-time battles, and Prompt 7's write-budgeted design (§16's D1 admission) has modest state volume. This means *complete* audit coverage of valuable mutations is affordable in a way it would not be in an action game — the game can afford to log every money-touching event, not sample it.
2. **The valuable state is server-resident only.** Nothing on the client is authoritative except what the server has already sent; the client holds no keys, no balances that matter, no history. Theft of a client machine yields, at most, one player's view of their own data.

### 3.2 Trust boundaries

Boundaries below are drawn as *zones*, not vendor choices — this is deliberately not a deployment design, per D-005's provisional status. Each boundary states: what must be trusted inside it, what must be treated as untrusted outside, and which requirement(s) police it.

| # | Boundary | Inside (trusted to…) | Outside (assumed…) | Policing requirements |
|---|---|---|---|---|
| B1 | Browser client ↔ public application | Render submitted UI; hold the player's session token; display server-computed values | Lie, replay, race requests, modify client-visible values; leak tokens | SEC-011 (validate every action), SEC-013 (input bounds), SEC-010 (server recompute), §5's fail-with-reason contract, SEC-029 (quotas) |
| B2 | Authentication & session handling ↔ application | Establish identity once verified; issue bounded sessions; maintain revocation | Treated as part of the server-privileged zone — a client can never *derive* authority here | SEC-001/002/003/005/007 (§4); session-less business logic must not re-derive authority from client claims (SEC-012) |
| B3 | Public application ↔ game-state processor | Execute mutations only after validation + authorization; compute all economy arithmetic | Client passes untrusted request *shape*, never values | SEC-010/011/012/013/016/025 |
| B4 | Game-state processor ↔ turn scheduler/resolver | Advance world state across turn boundaries inside the single resolution window | Nothing user-submitted inside resolution except pre-validated queued actions | SEC-018/019/020/021 (§6), SEC-014 (idempotent submits), SEC-022 (delay disclosure) |
| B5 | Processor ↔ database | Own the schema and the transaction boundaries; enforce concurrency via its own locks/transactions | A crashed write, a duplicate delivery — requested by nobody and always possible | Prompt 7 §14's two-checkpoint affordability model; SEC-016 (atomic settlement), SEC-020 (checkpointed turn phases) |
| B6 | Application ↔ admin/moderation interface | Privileged actions behind explicit privileged auth + audit rows | No overlap with ordinary player login paths  | SEC-006 (separate ops identity), SEC-027 (elevated perms, two-person rule), SEC-031 (privileged acts logged) |
| B7 | Game ↔ external services (e-mail send, static hosting, monitoring) | Send mail, serve assets; hold their own credentials | Outage, abuse of their APIs against quota, credential leakage | §15's budget posture; secrets never client-exposed (SEC-006); e-mail not depended on for core flow (§4 design) |
| B8 | Live state ↔ backups/restore | Reproduce a verifiable prior state |staleness — a restore can regress state; a stale restore is itself TH-023 | SEC-030 (restore discipline), SEC-031 (event rows for reconciliation), TH-023's walkthrough |

Additional boundary notes:

- **B1 is the boundary most games get wrong first.** The client-visible economy values exist only for *display*; the honest-preview rule (Prompt 7 §14) already says previews are advisory. The server's arithmetic is the only arithmetic.
- **B2's boundary must never be bypassable via a second route.** Every mutating endpoint resolves the acting nation from the authenticated session — *never* from a request parameter (TH-008's whole class).
- **B4 is a zone, not a service.** "Single resolver window" does not mean "single server"; it means resolution of turn T is claimed exclusively before work starts (SEC-019), whatever the host.
- **B6's interface is where insider risk concentrates** (TH-017/018/019). The design answer is not "trust operators more" but "log and scope ops powers regardless of who holds them" (SEC-031's privileged-read-is-an-event rule).

### 3.3 What is *not* modeled as a boundary

Per working rule (no architecture finalized here): no specific provider, database engine, or hosting topology is assumed anywhere above. The boundary map is deliberately phrased so that Cloudflare Workers + D1 (D-005's candidate), or any other stack, can implement it. Containers like B4/B5 exist in any implementation; boundary *placement* is deployment-decision territory that belongs to the architecture stage, not here.

---

## 4. Account security and recovery

### 4.1 Registration and account ownership

- **One identity per account, one credential path.** Registration collects: a username handle, an e-mail address, a password (or equivalent post-2026 authentication — see below). The e-mail address is the recovery anchor (SEC-001's unique-identity basis). The *game* identity is the nation (created after account creation, per Prompt 4's onboarding flow); renaming, renaming-mount, or name changes follow §12's name-guard rules.
- **Ownership = verified control of the account credential + the recovery anchor.** Nothing in first-playable design implies *real-world* identity verification (AP-002's posture: no forced real names; Prompt 5 UXD-005's adversarially-designed fairness applies). The recommendation avoids government IDs and phone-based identity binding unless a later launch jurisdiction forces it (OSQ-010; §11).
- **Whether e-mail *verification* is required depends on a free-tier cost question, not on doctrine** (TH-013's noted fork): if the free e-mail budget can't carry verification mail at population scale, registration can accept unverified e-mail at launch, with the trade-offs recorded in OSQ-003 — unverified accounts ease bot creation (TH-013's account-creation throttle gets more duty) and weaken SEC-004's recovery anchor (unverified e-mail means the recovery anchor can't be trusted yet). §16's SEC-001 is written to require *unique* identity with verification as the *recommended* posture, explicitly flagged to OSQ-003 if cost blocks it.
- **Eligibility rules apply at creation:** Prompt 7's fresh-account restrictions (development caps, trade caps) exist at design level already; security's duty is their *enforcement* (SEC-023) and their *fairness* (composition §8).

### 4.2 Password handling and authentication options

The candidate authentication options, with an *explicit* free-first comparison:

| Option | Usability | Cost | Security posture | Free-tier fit | Recommended |
|---|---|---|---|---|---|
| E-mail + password (Argon2id/memory-hard hash, length-checked, HIBP-class breached-password check optional) | Familiar; the genre's players already used one 10× | Zero infra; hash cost ~ negligible at 12-turn cadence | Standard web; strength depends on rate limits + recovery (SEC-004/005) | ✓ | **Yes (baseline)** |
| Magic-link / one-time sign-in e-mail | Lowest friction per login; no password to breach | Consumes the free e-mail budget *per login* (population × sessions/day) | Depends on e-mail security; login e-mail is a phishing channel | Stretchy | **Maybe (post-launch; not before a cost test)** |
| OAuth “Sign in with …” provider | Pleasant; password diverted | A client ID; some setup | Platform-grade for auth transport; depends on provider policy (account deletion, ToS changes) | ✓ mostly | **Candidate (optional add-on, not a dependency)** |
| MFA (TOTP/e-mail challenge for sensitive actions) | Friction only where scoped | Zero (TOTP is local); e-mail challenge uses budget | Strongly reduces takeover impact (TH-001) | ✓ | **Optional add-on; mandatory only for privileged ops accounts (SEC-006)** |

No approved provider exists anywhere in §4.2 — options are proposed in case, not chosen to bias D-005. Passwords alone (with a strong recovery + rate limiting stack) is the free-first default; OAuth and MFA are *optional layers the owner can add*, not assumptions the design carries. If passwords are used: server stores a *memory-hard hash* (Argon2id-class) with per-user salt, never the password; the reset flow (§4.4) never asks or displays an old value; password-strength parameters are a *tuning posture, not a rule* (the security story rests on the rate-limits + account-notification + compromise-review stack, not on password composition rules by themselves). "Modern password handling" in SEC-002's anti-threat row refers exactly to this stack.

### 4.3 Sessions

- **Issue, don't rely on, long-lived stand-alone tokens.** Session issuance returns a session bound to: the account, its creation time, its *absolute* expiry (SEC-003's short absolute timeout posture — the OWASP Session Management cheat sheet's recommending absolute timeout is cited in §21's source table), and a revocation state. Idle expiry alone is insufficient: a session stolen while idle must still die (TH-002's scenario).
- **Revocation semantics to specify in implementation:** logout and "log out everywhere" must both exist; a password change must revoke all existing sessions (a small exception is allowed only for the currently-authenticated session that made the change), because the compromise path *is* the password path (TH-001); a recovery flow's success also revokes existing sessions except the one that, where reliable, triggered it.
- **Rotation:** the session identifier rotates on privilege changes (password change, recovery, step-up auth) without invalidating the authenticated experience — the token's value changes; the session's *continuity* stays.
- **Scope:** the session token lives in a browser cookie with the standard web posture — `HttpOnly`-class handling, `Secure` on HTTPS origins, `SameSite`-class restriction set at the implementation stage. *This is a §5 implementation principle, not a §3 architecture decision* — no cookie/posture tuning belongs in this report's register; the requirement SEC-003 names the behavioral guarantee (revocable, bounded, rotated) and §5 names the transport principle.

### 4.4 Account recovery that cannot impersonate

Credentials get lost — the game's recovery design is a trust product and also a threat surface (TH-001/TH-002's pricing). Recovery requirements:

1. **The recovery anchor is the registered e-mail.** A recovery request sends a *time-boxed, single-use* challenge link/token to the address on file. No in-game-asset "proof" games: a request like "list your last three trades" or "give your current treasury balance" is *never* a verification step (both Prompt 7's SDQ-004-adjacent private-data posture and the compromise playbook in §4.6 make in-game-state quizzes dangerous — the state is *also* what the attacker holds).
2. **Rate limits on the recovery endpoint** (SEC-004/005): recovery attempts are throttled per e-mail and per source with an escalating delay, and *e-mail-the-token* is never skipped when a rate limit trips — the flow "fails closed" into a delay rather than "fails open" into a code. The lockout ladder never discloses whether an account *exists* (TH-014's enumeration channel).
3. **Recovery disambiguation when ownership is contested** (two parties both claiming one account — a household breakup or a stolen credential the original owner got back): the design does *not* attempt forensic heroics. The recovery *regime*: when a recovery race exists, the account is put in **lockdown grace** — in-game actions (trades, alliance changes, campaign orders) are suspended for a defined window while both claimants' evidence is reviewed by ops; ops' authority here comes from §12's process (SEC-026/027), not from arbitrary discretion. Result is communicated (SEC-022's honest-disclosure posture; DP-004 discipline).
4. **No promise of perfect recovery.** The prompt's warning is taken directly: if a takeover converted the nation into trades, alliance changes, or resource movement, §4.6's compromise review *may* restore value where evidence is unambiguous, but the design does not commit to undo everything. The honesty rule (DP-004) applies to every recovery communication: state what was done, what was *not* done, and what might still be possible.
5. **Account deletion & retention at source (SEC-026):** deletion means the account is deactivated, then expunged per §11's retention rules — gameplay state is deleted or aggregated per §11 with the technical caveat that *backups* produced while the account existed persist until backup rotation (a retention fact disclosed in the privacy record, never hidden). Data the game must retain for legal or anti-abuse reasons is minimized and documented per §11.

### 4.5 Rate limiting and anti-stuffing defenses

- **Login attempt caps** exist per-account and per-source (SEC-005). The ladder: escalating delays first; from there throttling (with honest reasons per the §5 contract — "temporarily capped," *not* a punishment name); from there a temporary lockout window that clears itself. Nothing in this ladder is framed as *automatically* flagging a player as hostile — shared-IP and common-password pitfalls are explicit (§8.4).
- **Credential stuffing** (TH-001) is handled by: rate_limits + breached-password check posture + responses on failure that don't differentiate "no such account" from "wrong password" (enumeration-resistance). The recovery endpoint has its own separate caps (TH-014's distinct hazard: an unthrottled recovery endpoint is a credential guessing door on a *different* room).
- **Sensitive-action step-up** (SEC-002's optional posture): the design recommends step-up on the *most damaging* account actions if a population finds it acceptable — changing the recovery e-mail, deleting the nation, transferring large value late in the game's life. It is proposed, not mandated; a per-action scoping shows up as SEC-002's acceptance criteria, and its player-experience cost is owned by OSQ-002.

### 4.6 Compromise response for accounts

When an account is compromised (reported by its owner or detected behaviorally per §13):

1. **Contain first (containment actions without investigation):** revoke sessions; then optionally force password reset on next login; pause nothing silent — the account owner is told everything done by ops (SEC-007 notification; DP-004 disclosure).
2. **Investigate with evidence, not assumption:** the compromise-window's in-game actions * are logged (SEC-031's event rows). Trades, alliance changes, campaign orders, and resource changes in the window get the vote of §4.5's review: are they *honest* behavior, *exploitative* behavior, or *hostile-driven* behavior? Evidence holds the verdict — not suspicion (§13's single-weak-signal rule).
3. **Remediate value only where evidence is unambiguous** (a confirmed takeover that drained assets into trades is the *only* case where reversal is *designed* to happen): the reversal itself is *logged and disclosed per DP-004*, never silent. Where evidence is not unambiguous, the posture is "contain + notify + observe," not automated clawback — the economy report's R-16 conservative-response posture carries across *all* recovery scenarios.
4. **Record:** the incident gets a registry row (§14's incident register), the affected player's notifications are part of the record; if a *pattern* emerges (multiple accounts of the same compromise vector), the pattern itself is an investigation trigger.

### 4.7 Administrative accounts and secrets

- **Distinct identities:** ops/administrator credentials are separate from any player account; no player-visible surface accepts them (SEC-006). The *same person* owning an account and an op login is fine — the *separation* is of surface, not flesh (the point is a leaked player session must not grant ops access).
- **Step-up (mandatory for ops):** ops access requires its own credential + step-up (TOTP-class), because the blast radius is the whole game (TH-018/019). Two-person rule for the most destructive ops (SEC-027) is pre-launch policy only when two people exist — a single-creator project prioritizes the *disclosure-first playbook* instead (TH-019's proposal, OSQ-012).
- **Data-exfil / retain-the-honest-log:** ops reading player data is itself a logged event (SEC-031's privileged-read rule), and the *log of privileged plays* is part of every incident review.
- **Account deletion/retention for ops:** ops records live under the same §13/§11 rules as everything else — no separate "ops records live forever" exception.

### 4.8 Safety on deletion and retention

Account deletion is *user-initiated*, deferred through the §11 data-governance flow:
- self-service deletion request → an enforced delay (a short "cooling" period, proposed: 7 days, tunable) in case the request was a mistake or a hijacker's act — an owner can revoke the deletion within the window (anti-hijack weaponization of deletion: the nation should not be killable by an intruder with a session);
- post-deletion, per §11: e-mail/credentials purged; gameplay state deleted or anonymized; security-event records reduced to minimal aggregate evidence where abuse evidence rules (SEC-032's inventory pins this retention logic);
- the deletion records the *actor* (the user, ops by incident, or a hijacker's request caught by the cooling period), so §13's lifetime event trail remains coherent.

---

## 5. Server-authoritative game state and request integrity

### 5.1 The authority rule, and why it also reduces enforcement cost

**The browser is a display surface.** Every value the game *acts on* is computed by the server from authoritative state and allowed by explicit validation. This section's rules are SEC-010 through SEC-014's substance; Prompt 7's §14 timing contract and honest-preview rule already promised players *why* the server, not the client, decides timing and affordability — the same posture is extended to all mutations. An additional consequence is *disclosure-shaped enforcement*: because the server itself computes every outcome on its own authority and posts *reasons*, players see why requests succeed or fail — the reduce-server-arbitrariness posture (DP-004) is *also* the enforcement posture. Trust is earned without an adversarial police layer.

### 5.2 The independent-validation inventory (what the server must recompute/validate)

For each mutation family below, the server independently validates (from its own state) — never trusting a client-claimed quantity except as the *request's stated intent*, which it then verifies:

| Action family | Server independently computes / validates | SEC |
|---|---|---|
| Treasury/resource changes | Available balance, net effect within no-debt invariant (single-pool design ECON-001), magnitude bounds per ECOQ's documented ranges | SEC-010, SEC-013, SEC-016, SEC-025 |
| Development purchases, upkeep, respecialization (SDQ-016) | Level prerequisites, cost schedule, upkeep state, emphasis rules' prerequisites, the respecialization cooldown/cost posture from Prompt 7's register | SEC-010, SEC-011, SEC-013 |
| Trade orders & settlement | Balance at *server-resolved* time; per TRADE-pair velocity caps (R-13 family); fresh-account windows (SEC-023); R-19's atomic-pair settlement; cancellation/settlement races via per-order idempotency (SEC-014/016) | SEC-011, SEC-014, SEC-016, SEC-023 |
| Diplomacy & alliance changes | Role-to-verb authority (SEC-012's per-resource authority table); membership state; the alliance pool's audit posture (R-08-class ledger discipline from Prompt 6/7's registers) | SEC-011, SEC-012 |
| Strategic orders / campaign claims | War-stage design dependency (SDQ-008 not started — D-004 provisional): the *generic* contracts (queued submission, queued attribution, resolve-at-boundary, deterministic tie-break) hold through §6's family; specific war rules are deferred war-stage work | SEC-011, SEC-012, SEC-014, SEC-018 |
| Turn advancement & cooldowns | Server's own turn *T* and boundary bookkeeping; cooldown state per nation; the *published boundary rule* (SEC-015) | SEC-015, SEC-018 |
| Player eligibility & permissions | Account standing, nation ↔ account binding, per-verb authority for the *acting* identity | SEC-011, SEC-012 |
| Any simultaneous requests | Single-state-contention model per Prompt 7's settlement discipline: whichever request commits first wins; the *loser* receives an honest reason (never a numeric lie or a silent no-op) | SEC-014, SEC-016 |
| Stale client data | The client's view is prefetched and may lag; the server prices actions against *its* state; on mismatch it returns a reason and (except where explicitly designed to re-price) re-prices (the honest-preview fence) | SEC-010 |
| Duplicate submissions / retries | Idempotency: every write action carries an idempotency key; duplicates coalesce to the first committed result and *all* receive the same response (see §6's boundary interaction) | SEC-014 |
| Forged, replayed, or modified requests | Auth-token validation, request-shape validation (SEC-013), request-authorization validation (SEC-012), availability (limits/nonce discipline where transport matters) | SEC-010/011/012/013 |
| Cross-nation access (TH-008's class) | Every endpoint resolves the *acting nation* from the authenticated session, never from a request parameter; object IDs passed by the client are *authorized-scope-checked* against that nation | SEC-012 |
| Client-visible values | Not a mutation — but every *client-visible* value is *server-computed* on read; the client never owns a "truthful" number it could push back (the root authority rule) | SEC-010 |
| Administrative actions | Privileged identity, step-up, logged per-verb, scope-limited per §3's B6 | SEC-006, SEC-027, SEC-031 |

Two implementation postures worth writing explicitly as requirements, because they cut otherwise-invisible failure modes:

- **Request-shape validation is a first-class firewall.** Every write endpoint validates its *entire* input shape (types, lengths, ranges) against a declared schema before touching business logic (SEC-013). Malformed input is answered with the reason (never a silent error) and scored by the abuse posture (throttled per SEC-029 after repeat, never auto-banned on the first sight).
- **Fail-with-reason everywhere.** A failed request response carries: what was attempted, why it was rejected (out of balance, off cooldown, no authority, invalid shape), and — where applicable — what would make it succeed. This is the DP-004 posture from Prompt 5/6's family, applied to security rather than economy.

### 5.3 What this does *not* do

- **No anti-tamper theater on the client.** Trying to stop devtools-inspection of the client would waste effort and damage accessibility (§9). The *defense in depth* is at the boundary (B1's policing requirements), not in the browser.
- **No invention of mechanics.** Where the economy rules leave a parameter open (ECOQ-002/004/005's explicit deferrals; fresh-account policy in OSQ-001), §5 does not fill it: SEC-011's validation list *names the check*, and the check's *value* comes from the design stage that owns it. The requirements stay enforceable only after the owning design lands — dependencies recorded per threat row and in §22.

---

## 6. Turn scheduler, duplicate processing, and time abuse

### 6.1 What Prompt 7's economy already fixed

The three-class timing contract (Prompt 6 §17's immediate-not-possible framing, Prompt 7 §14's classification), the deterministic resolve-at-boundary posture with published tiebreaks (ECON/§14), and §17's worked examples already answer *how time works* for economy mutations. What remains for security is exactly the residual Prompt 7's Setup called out: the **pipeline integrity** of the boundary itself — who runs it, once, safely — and the specific *abuse* shapes near a boundary. This section's requirements (SEC-015, 018, 019, 020, 021, 022) owe their existence to Prompt 7's SYS-016 pipeline being the single point where everything mutates.

### 6.2 Unique turns and the single authoritative resolution window

- **A turn is identified by its own index** — T, T+1, … — stamped by the *server*, named in every resolution artifact (ledger rows, event rows, logs). Nothing player-submitted names a turn; a client that *says* "this applies to T+1" is describing intent, not authority (SEC-015).
- **A single authoritative resolution window** governs resolving turn T (SEC-019): before entering resolution for turn T, the resolver *claims* turn T (interprocess-lock or a turn-state claim — semantic, not vendor-shaped); the claim is recorded with its worker identity; a second claim attempt (a duplicate scheduler wake, a scaled-out worker, an operator retry) finds `status=done` or `status=in-flight-by-other` and exits without producing player-visible change. Nothing in the design assumes the scheduler automatically runs exactly once — it *requires* the claim discipline that makes a duplicate harmless.
- **Idempotent-or-abort resolution mechanics:** individual resolution *steps* are idempotent in effect-atomicity terms (a step either commits *fully* or commits *nothing*, or carries an explicit phase marker supporting forward-only resume — SEC-020/021). The design principle: partial progress leaves *evidence* (committed-phase markers that a resume can honor), never *unmarked state* (changed balances without a phase marker). If a resume cannot honestly resume, it halts instead of guessing.

### 6.3 Player actions around the boundary

The timing answers follow Prompt 7's contract; security adds the *punishment-free* framing (relevant to TH-011's intent-free abuse mass):

1. **Immediately before a boundary:** a player submits action X at T's last instant: T stamps it as a T-action if the server received it while T was open; the client's belief is irrelevant to the outcome; if the *client mispredicted*, the reason string explains (the honest rule, so it doesn't re-litigate).
2. **During resolution:** new actions queue for the *next* turn — the normal pipelines (trade order, campaign claim, etc.) accept and hold; resolution of *T* is not disturbed.
3. **Retrying after a timeout:** the retry carries the idempotency key of the original submit; the server returns the *first* committed outcome (SEC-014) — if T already resolved and X was applied, the duplicate-retry returns X's *actual resolution state*, not a second application.
4. **Submit-after-resolution (stale turn id):** a client attempting an action with a stale explicit turn expectation gets the server's own turn stamp; the *honest reply* (the outcome class is described per Prompt 7 §14's contract, e.g., "queued for T+1") is disclosed — no silent re-class, per DP-004. This is the anti-TH-011 posture.
5. **Concurrent racing for the same resource:** deterministic resolution per the published tiebreaks (SEC-018's rule); players who lose a race receive the reason and the *actual outcome* — the prompt's "deterministic tiebreak" already names this the structural answer.

### 6.4 Failures in the resolution window

The awkward failure cases and what each design holds them to:

| Failure situation | Required behavior |
|---|---|
| Resolution aborts halfway (quota, crash, timeout) | SEC-020's phased checkpoints mean a resume completes *only the uncommitted phases*; SEC-021's per-phase dedup means nothing already applied is applied again; if resuming is not safe (state inconsistency unresolvable from evidence), the resolver *halts and notifies* (SEC-022) rather than deriving |
| The scheduler fires more than once | Second and later claims are no-ops by the claim discipline (SEC-019); *if* a claim is stolen or impossible (a broken lock for whatever reason), the duplicate-run alert is a detection event (SEC-031); nothing player-visible changes |
| Two workers attempt the same turn | Same claim discipline; the *second* worker refuses; the refusals themselves logged |
| Processing stops and stays stopped | Player communication via SEC-022: an announced delay + a published status the world map page can read (a "next turn status" note), not silence; the *resolver's* queue resumes forward-only |
| A turn "finished" but the completion response was lost | The turn ledger (SEC-020) is the truth — the client's *reconciliation posture*: on re-query the player receives the real outcome; nothing is applied twice because there is no response-driven application path |
| Deployment/migration overlaps the boundary | A published rule (SEC-022 posture): the scheduler skips a turn rather than racing a migration, disclosing to players (a missed turn is announced as a missed turn — Prompt 7's "never silently re-derived" posture carries over) |

### 6.5 Time-abuse considerations and what is *not* wrong in this game

- **Clock abuse in the genre sense** (sub-second timing to win economies against other players) has limited power here because the design resolves at *whole turns* (the resolve-at-boundary equalizer of Prompt 7's timing contract): a "snipe" can be faster than a human but the *award* is at the boundary anyway (TH-025's analysis).
- **What still needs honest rules:** the *automation policy* (what tools may submit, what timing is honored) is the fairness artifact (SEC-015 + the OSQ-004 policy), not a technical wall — the §9 classification and the walkthrough W-18-P (new-account spam) carry the abuse-facing end of it, while **read-only timing** and ordinary retirement play is explicitly not "attacked."
- The **10ms-cron-CPU posture** (Prompt 7 §16.4's S2 free-tier research row) matters for scheduling cost only; the *integrity* of timing (SEC-019/020/021) does not depend on the quota tier the ops runs, and neither design scales its guarantees with the provider's tier.

---

## 7. Economic security and market abuse

### 7.1 What the economy design already gives security

Prompt 7 did the heavy structural work, and this section treats its invariants as *given assets* security must protect, never re-invent:

- **Single cash pool with no debt and no interest** (ECON-001): no credit creation, nothing to leverage, so short of client-trust failures there is *no money multipliers* path.
- **Atomic-pair zero-partial settlement** (R-19: a trade commits all-or-nothing with per-pair rows) — this kills the "half a trade" family; what remains is *request-level* duplication/racing (TH-007), which §5/§6 handle.
- **No-yield-on-cash** (ECON-020 — lending rejected under ECON-020; trade-credit instead evaluated under ECOQ-007): idle cash always deteriorates toward trade value only. Lending-like exploitation (interest arcs, delayed repayment) is structurally absent at design level.
- **Fee/gate sequencing** (G-1…G-6): the *directed-trade-first* phase has no public reference prices to manipulate (TH-004's residual); the G-4 gate conditions a listing market on manipulation-pattern review before one exists.
- **Two-checkpoint affordability** (Prompt 7 §14): balance is priced at submit *and* at resolution; changed-state races resolve deterministically with published tiebreaks.
- **Fresh-account restrictions, per-pair velocity caps, and transfer-graph review** (R-13-family controls; ECON-013's directed-trade restrictions): the economy already expects TH-003/TH-005; security's job is their testable enforcement (SEC-023) not new mechanics.
- **R-16's conservative-response posture** (no automated clawback at launch minus ambiguous evidence; constant composition review): this is *the* posture this report carries into every abuse-handling path.
- **§16.3's write-budget framework and S1–S3 research rows** (Prompt 7's fresh research): §15 re-uses them rather than re-deriving.

### 7.2 Economic abuse scenarios and the classification discipline work

The prompt asks each scenario be classified (confirmed vulnerability / plausible risk / hypothetical test case). Since no code exists, **none is a confirmed vulnerability** — everything here is design-stage either *plausible* (the genre has seen it; the design has a counter) or *hypothetical* (the mechanism doesn't exist yet at first playable). The classification rule: **"plausible" requires genre evidence or a mechanism that first-playable already ships; "hypothetical" is everything later-stage.**

| Scenario | Exists at first playable? | Class | What makes it possible | Prevention | Detection | Evidence to retain | Disputes |
|---|---|---|---|---|---|---|---|
| Duplicate/repeated trade (TH-007) | Y (client retry) | Plausible | Missing idempotency | SEC-014/016; ST-005 | Idempotency-key collision counter (SEC-031) | Request id + outcome row | Coalescing is *by design*; disputes only when the *first* result is alleged wrong |
| Same balance spent twice concurrently (competing submits) | Y | Plausible | Client racing two tabs | SEC-016 single-spend atomicity; first-commit wins; loser gets reason | Two-commits-one-key anomalies | Both request rows | Loser's reason string is the appeal basis |
| Overspend via display mismatch | Y | Plausible | Stale client view | SEC-010 recompute + honest re-price (§5) | Deltas that disagree with client-submit logged | Request + validation rows | Honest reason in response |
| Negative balance / overflow (TH-006's edge) | Y if masks absent | Plausible | Integer/type mishandling | SEC-013 bounds + SEC-025 no-negative invariant | Validation-reject counters | Rejected request rows | None — rejection is the design |
| Cancellation/settlement races | Y | Plausible | Two requests on one order | SEC-014/016; R-19's atomic pair; deterministic tiebreak | Race-outcome rows | Per-order state history | Tiebreak rule is published (DP-004) |
| Failed-partial settlement | N if R-19 holds | Hypothetical→design-kill | — | Atomic pair (already design-fixed) | — | — | — |
| Refund/retry exploit double-claim (failed submit re-submitted *and* refunded) | Y (a retry bug class) | Plausible | Idempotency gaps in *refund* paths | SEC-014 keys on refunds too; refunds logged (SEC-031) | Double-refund anomaly row | Refund rows with cause | Reversal possible on evidence (R-16) |
| Wash trading / self-pair inflation (TH-004) | N (no listing market at first playable; G-4 post-gate) | Hypothetical (until a market stage) | Public reference prices | ECON-018's G-4 gate; self-pair exclusion in aggregates (R-14/R-15 posture) | Day-window aggregate anomalies; self-pair volume patterns | Trade pairs + evidence per SEC-024 | Market-stage design decides; not first-playable |
| Collusive price manipulation | N (same as above) | Hypothetical | — | Same as above | Same | Same | Same |
| Market manipulation around turn boundaries | N (no public prices) | Hypothetical | — | — | — | — | — |
| Coordinated hoarding/cornering | Y in principle (directed trades) | Plausible *only as strategic play* | Directed trade allows amassing supply | **It is not abuse by itself** (§8.4's line); the line is *transfer-graph deception* (disguising collusive control as ordinary trade), not volume | R-13/R-16's review triggers on graph shape not on raw volume; high-volume players are never auto-flagged | Transfer graph | Explicit review-then-act path (SEC-026/028 intake) |
| Alt-funneling value via trades (TH-003) | Y if multi-accounting undetected | Plausible (genre-verified top abuse) | Multiple accounts | SEC-023 caps + graph rules; OSQ-001 decides policy | Per-pair asymmetry/circularity flags (review-only) | Trade graph, session/config metadata short-retained (§11) | Review + appeal ladder (§12) |
| Alt-as-sabotage burn (TH-005) | Y (protection windows make young nations disposable in principle) | Plausible | Fresh-account asymmetries | SEC-023 cap *outgoing* too (asymmetry), tune protection parameters | One-way outlier flows from young nations | Transfer graph + window params | Same as TH-003 |
| Sanction-evasion new accounts (TH-020) | Y post-ban | Plausible | Free creation; standing rebuild | SEC-001 unique handling; ban-evasion as evidence-gated conduct case (§12) | Transition-consistent conduct patterns (reviews, not IP blocks) | Conduct case files | §12's appeal flow |
| Respecialization/development abuse (SDQ-016; cost/exploit sweeping) | Y (mechanic exists) | Plausible only via cost-model bugs | A wrong cost/upkeep formula | SEC-010/011 server recompute; §22 checks the *economy*'s own §18/§19 test entailment | Dev-cost anomaly deltas | Purchase rows | Recompute fixes are disclosed (DP-004); player-visible history stays as-is (§14.6's reconciliation rule) |
| Duplicate *rewards*/*compensation* (incident payouts claimed twice) | Y (post-incident) | Plausible | A compensation flow without same idempotency discipline | SEC-014-key discipline extends to *any* value grant, incl. manual ops grants (two-person rule; SEC-027) | Grant-id collisions | Grant ledger rows | Grant rows are the evidence |
| Tax/fee abuse (abuse of fee schedules if any exist) | N (no public fee schedule at first playable beyond G Partial: G-1's entry fee is ECOQ-gated) | Hypothetical | — | — | — | — | — |
| Negative-price/mis-valued listings | N | Hypothetical | — | SEC-013 | — | — | — |

The **classification work** the prompt demands is done honestly above; threats TH-003/011/007 are *plausible* (mechanism + genre evidence exist), while all market-based abuse is *hypothetical* until a market stage exists. In no case does this report claim a live exploit — no system exists to attack (§21's evidence classes assert this).

### 7.3 Legitimate competition vs. abuse — the line

Market concentration, high prices, profitable specialization, and rapid accumulation are **not abuse** — they are the game (Prompt 7's economy deliberately enables competitive asymmetry, and the Prompt 3 §8 integrity warning is *about* policing while the design is *about* structural responses). The line this report draws, enforceable by rules and review:

1. **Deceptive representation of economic agency:** one player using *multiple identities* to *represent one economic agent as many* is misrepresentation — TH-003's class. The abuse is faked independence, not the trade itself.
2. **Disguised control** (circular transfers that make an excluded party the beneficiary — R-13's self-trading shape) versus ordinary trade between genuinely distinct agents: the detection work is §8's *evidence* problem, never automatic punishment.
3. **Exploiting a *rule defect*** (a balance/fee formula bug, a settlement race): the exploit-evidence path then follows §12's process for *technical exploit response* (fix first, disclose, compensate honestly), partly distinct from conduct moderation even if the particular player gets both.
4. **Everything else** — honeytraps, hoarding, corner attempts, alliance-supplied patrons, clever timing within the published rules — is played, not policed. Detection exists *only* for where the rules themselves were broken.

### 7.4 What security *must not* do here

- No unapproved fee/tax/limit/cooldown/verification rules invented (ECOQ-gated parameters respected — the report proposes *controls*, and every "proposed starting posture" is labeled).
- No mechanic invented to make policing easier against the economy's grain (e.g., this report does not propose forced trade disclosures or visible player transaction feeds — SDQ-004's privacy question stays open; §11's data governance interacts with it, not by answering it).
- No "compensate everyone after every exploit" promises; the *incident protocol* (§14.6) owns compensation, and R-16's conservative posture is the baseline.

---

## 8. Alternate accounts, collusion, and coordinated abuse

### 8.1 The multi-account design choice itself is OSQ-001

Prompt 7's economy's *fresh-account* mechanics and Prompt 1/3's genre evidence press toward restricting multi-accounting; but the *policy* is a social-design choice with legitimate strategic upside (alliance staging, role diversity, personal risk hedging — several browser-strategy communities built their politics on multi-account families). The register treats this question as **OSQ-001** with three options and a recommendation, and every control below is written so it *works under either* answer:

- **Option A — Prohibit:** one account/nation per person. Strongest integrity posture; relies on detection that is *behavioral, not network-based*; enforcement friction; genre evidence says it's also the most common community rule demanded.
- **Option B — Restrict (recommended):** one account per person *with supervisory conditions for named use-cases* (alliance flight-craft roles, etc.); explicit disclosure; distinct-per-account trade caps already coded in the economy. Fairness preserved, detection burden reduced, appeals cheaper.
- **Option C — Permit with conditions:** N accounts allowed but *economy-capped*: fresh-account windows, per-cumulative caps per *person* (each account sees each other account's presence in rate limits), no circumventing of pair-velocity caps via rotation. This is the most complex to implement honestly and the least common in the genre's healthiest communities.

The recommendation is **B** for competitive-integrity reasons (the genre's verified #1 economic abuse is coordinated multi-account wealth transfer, per Prompt 1/3's registers and R-01/R-13), **as a recommendation only**; the owner decision carries the final call (OSQ-001's §20 row cites both this report's analysis and Prompt 3's evidence).

### 8.2 Collusion and coordinated abuse vectors beyond multi-accounting

- **Alliance members coordinating unfair transfers** (TH-003's collusive-trade form; prompt 7's alliance pool R-08 posture): the pool's audit-first ledger is *the* structural response; the *conduct* layer (§12) handles misrepresentation of roles ('gifts' disguised as trade after alliance collapse, etc.).
- **Disposable-account rotation** (TH-020's sanction-evasion face): the economy's fresh-account windows taper; the *identity* question is OSQ-001's; evidence-based enforcement runs on conduct (§12), not IP.
- **Coordinated diplomacy/campaign manipulation** (TH-022): deferred to the war stage as an *explicit design dependency* (Prompt 6 §22.4's input list and D-004's provisional status); the inherited race-handling rails (SEC-014/018/019-021) carry over project-wide.
- **Protection-window farming** (TH-005): prompt 7's protection design is war stage-owned; the *asymmetry cap* (SEC-023's outgoing-side caps for fresh accounts) is the security-side counter recorded here.

### 8.3 What evidence may reasonably be used — and the non-evidence traps

- **Behavioral/graph evidence is the first-class signal:** per-pair value asymmetry, circular/self-pair shapes, fresh→main one-way flow patterns, session-documentation anomalies *around trades* (the timing correlation between two accounts acting on each other), *consistent* trade-role — these are the graph shapes R-13's detection was already designed around.
- **Shared IP is explicitly unreliable evidence** (TH-003's false-positive branch, the prompt's own trap): households, campuses, cafés, offices, and CGNAT deployments share addresses; conversely, *one* person across devices rarely shares a stable IP. Shared IP alone triggers nothing but a *note-level* flag (§13's single-weak-signal rule), never an enforcement action. §21's evidence classes list this as a **finding-with-uncertainty** rather than a fact to act on.
- **Device/DATA fingerprinting is rejected by default here** (functional anti-abuse analysis in §9's table): the accessibility/cost/false-positive price is higher than its evidence value for a game where the *economy's own structurals* do most of the work.
- **E-mail similarity/recipient reuse:** weak-to-moderate evidence; usable in *composition* with behavioral evidence, never alone.

### 8.4 False positives: households, shared devices, and the case that guards review against automation

- **Legitimate family members** may trade with each other, share an IP, and even share a device at odd hours. The *signal shape* that distinguishes abuse is **independence-breaking**: persistent one-directional value flow with reciprocal *shade* strategies (no reciprocal games, no risk-transfer) — not cohabitation.
- **The design's answer to false positives is a *human-read*, *evidence-gated* review stage** (SEC-026's ladder): automated flags *open a review*, never *execute an outcome*; the walkthrough W-18-G walks the household case end-to-end; the appeal path (§12) treats "we live together and share a router" as a complete defense in the absence of *graph* evidence.
- **Households with shared account members**: OSQ-001's policy answer decides whether two *account families* in one household may coexist; under any policy option, the household's *graph evidence* is what carries a determination, because the alternative is punishing shared addresses.

### 8.5 Normal alliance coordination vs. prohibited collusion

The working line (subject to OSQ-001's final shape): **alliance coordination of the economy is a *designed* activity** (Prompt 6 §14's alliance systems; Prompt 7's collaboration posture). Collusion becomes abuse when it *misrepresented itself as independence* to an economy rule that treats independent agents differently (fresh-account windows, per-pair caps, protection windows, directed-trade eligibility). The rule-of-thumb: *the players may cooperate; they may not manufacture false agents to exploit agent-counting rules.* This is the exact distinction §7.3 drew, applied to the group case.

---

## 9. Bots, automation, and service abuse

### 9.1 What a turn-based game makes *easy* to protect

- **No Twitch-reflex advantage exists:** the resolve-at-boundary equalizer (§6) removes most timing-gaming incentive.
- **Twelve turns/day with small state puts a *natural ceiling* on useful automation:** a bot that can act more than a human is acting on more than the game allows a human to queue — the economy's per-turn action class limits (Prompt 6 §17's class contract) supply the *content* of the human-parity line.
- **The service's write budget (100k D1 row-writes/day, Prompt 1 §6) is itself a rate-limit floor:** an abuser's *marginal* damage is capped by the same budget others use — the design's job is protecting the *fair share* not just the budget (SEC-029's per-action-class quotas).

### 9.2 The automation taxonomy (what is allowed, tolerated, restricted, banned)

| Class | Examples | Position | Rationale |
|---|---|---|---|
| Legitimate accessibility tools | Screen-reader friendly UI, keyboard navigation, browser zoom, high-contrast themes | **Designed for** | The audience promise includes accessibility (Prompt 4's axes); this is UI work, not automation policy |
| Reasonable player convenience automation | Browser bookmark of the nation page, browser form autofill, personal notes apps; *reading* own-state via official endpoints when provided | **Tolerated** | No competitive advantage the game's own queue doesn't already give; each act is still a full normal request |
| Read-only community tools & analytics | Nation-state dashboards, alliance trackers, *aggregated* trade statistics (once a public surface exists — itself a §11/SDQ-004 tension) | **Tolerated with published read quotas** | Valuable for the community; the risk is *data extraction*, capped by SEC-029's read-class quotas, not by policy hostility |
| Automated *action injection* with human-parity content | A bot that submits the same 3 actions a human would, at human cadence | **Gray — decide by policy, not by camera (OSQ-004's call)**; tolerable-in-principle if it honors the timing contract (no boundary sniping), restricted if it *circumvents anything* (rotation, cap-dodging, mass queueing) | The *content* is human-parity; the *risk* is scale abuse of the *same* tooling against caps |
| Boundary-sniping / faster-than-human injection at resolution instants | A script that fires exactly at boundary-second to win a contested buy | **Restricted by default (proposed)**; the policy (OSQ-004) may instead "publish the rule, keep the edge" if the community prefers | TH-025's analysis: no *integrity* damage, but *relative* advantage; community-fairness call, not an integrity call |
| Mass queueing / R-18's order-flooding family | Hundreds of order submit/cancel cycling, dozens of alliance mailings | **Restricted by quota (SEC-029)**; conduct-violation only if intent is abuse-driven (§12) | Service-health protection first; R-18's posture carries |
| Lazarus-class scraping of *all* player data (harvesting other nations' state snapshots aggressively) | **Restricted (read-quotas)**; the *public* surface is only what the design makes public (SDQ-004's unresolved question still governs what *is* public) | Data-minimization posture — "restricted" means the server doesn't serve it, not that the client is policed |
| Credential-stuffing / creation bots (TH-001/013) | Scripted registration/recovery storms | **Banned** (a service-abuse + fraud posture, not a game-play posture) | §4's rate limits; the ladder exists for the *threat*, not for the curiosity |
| Service flooding / quota-killer (TH-012) | Repetitive request storms to exhaust free-tier quotas | **Banned**; containment has *protocol-level* answers (quota-reserving for the scheduler, per §14/§15) | TH-012's resource-exhaustion analysis carries |

### 9.3 Automated harassment / reporting abuse (TH-013's social face, TH-016's mod face)

Automated *report submission* (mass false-report campaigns, brigading) is a moderation-integrity problem first (SEC-028's intake design: report-source visibility to reviewers, repeat-cluster de-prioritization) and a conduct problem second (§12's ladder handles false reporters as conduct cases on evidence, not reflexively). Detection of *automated* filing patterns is part of SEC-031's event-ledger, reviewed by humans.

### 9.4 Controls and the explicit no-go list

Adopted posture (proposed, not owner-approved):

- **Per-action-class quotas (SEC-029)** — the single most valuable control in this report's class: per-account, per-IP-class, per-endpoint-class caps with honest "temporarily capped" reasons, sized so the *scheduler's* quota needs are reserved first (§15's budget table).
- **Progressive delays and cache-friendly reads** — reads get cached at the boundary where rules allow, cutting motivation for scraping in the first place.
- **Abuse monitoring off the event ledger (§13)** — a *dashboard of counters* (auth failures, rate-limit trips, creation bursts, idempotency collisions), reviewed by humans; the ops budget's cheapest useful control.
- **Backoff requirements in client code for retries** (the honest-retry contract) — reduces accidental flooding.

**Explicit no-go list** (not adopted by default; each costs more than its benefit at this project's scale):

- **CAPTCHA walls on gameplay:** free-first projects lean on rate limits; CAPTCHAs damage the accessibility promise, add a paid third-party surface, and have limited effect against dedicated bots. *Not adopted.* May be re-proposed post-launch *only* for account-creation storms if rates fail (a conditional posture, owned by OSQ-002/003's verification questions).
- **Device fingerprinting:** rejected (§8.3): high false-positive price, real privacy cost (§11), weak additional evidence for the game's *economy-first* countermeasures (R-13 family).
- **Client-side anti-bot/obfuscation payloads:** rejected; server-authoritative design has no need of client trust theater (§5.3's explicit anti-tamper-theater posture).

### 9.5 Where turn-based design *makes abuse easy* — and the counter-measures

- **Automation isn't the hard problem; *scale* is.** A bot that plays 40 nations in parallel is a TH-003 variant whose detection needs the same graph review, and whose enforcement is OSQ-001's policy question. No captcha fixes a 40-nation labor pool; graph analysis + fresh-account asymmetry caps (SEC-023) do.
- **Idle-time exploitation (boundary farming)** — the §6 boundary answers carry.

---

## 10. Diplomacy, alliance, and strategic-conflict integrity

### 10.1 What exists versus what is deferred (the honest boundary)

This section does not invent diplomacy mechanics. What Prompt 6/7 established: the alliance framework (Tier C — SYS-010's Stage-3 design), the minimal treaty per SYS-009, alliances carry a treasury-pool with audit-first rules (R-08 posture, Prompt 7 §13), permission models are *undeveloped* (SDQ-014 is open — dependency), campaigns and OP-costed actions are *war-stage design not started* (SDQ-008 dependency; D-004 provisional). The prompt's required "unauthorized war declaration" analysis is therefore a **race-rule generalization**, not a war-mechanics design: every *diplomacy-adjacent mutation* is a stateful action the same rails (§5/§6) protect; war mechanics must *reuse*, not re-invent, them (SEC-022 and SEC-018-021 are the carrier family).

### 10.2 Risks and their requirement mapping

| Risk (TH) | Authority/validation rule | Logging/notification | Recovery | Where it lands |
|---|---|---|---|---|
| Unauthorized alliance administration (TH-021) | SEC-012's per-verb authority model: every alliance verb (invite/accept/eject/role-change/treasury-release/dissolve) carries its own authority check derived from the *server's* role model, never a client-claimed role | Role/membership/pool changes logged (SEC-031); affected members notified per SEC-007-family discipline; DP-004-style disclosure of *what changed* | Role revocation by the alliance's own process + reconsidering under reviewed evidence; reconstruction of "%the rules intended%" is possible from the event log | §12 moderation carries conduct; §22 flags the design dependency (SDQ-014) |
| Forged diplomacy actions (message/treaty spoofing) | Treaties/diplomatic state accept mutations *only* from authorized parties (SEC-012); client cannot "claim" a sender (B1's discipline) | All diplomacy events logged; • treaty acceptance is a two-party state machine, both parties' actions are their own events | Spoofing fails by design; disputes use the event log as the evidence spine | §22 dependency: the treaty model's deeper design (SYS-009's minimal form) may need its own stage |
| Stale/conflicting diplomatic agreements (two treaties entered at once, role races) | Same deterministic tiebreak family (SEC-018) + per-agreement idempotency keys (SEC-014) | Both attempts logged with the *resolved* outcome | Loser's reason is the appeal basis | §22 flags: SDQ-014's state-machine design defines the *content*; this report fixes the rails |
| Unauthorized war declarations / campaign orders (TH-022) | War stage's design dependency; rails shared: queued per Prompt 7 §14's classification, attributed, idempotent, boundary-resolved | Same family | Same | Explicitly deferred to war stage (Prompt 6 §22.4's invitation list + D-004) |
| Duplicate campaign resolution | SEC-019/020/021 carry campaign resolution exactly as trades: one winner, published tiebreak, idempotent phases | Deposit logs | Same | Deferred (content) but rails exist (this is the Prompt-7-pipeline extension) |
| Cooldowns / protection-window exploitation (TH-005) | SEC-015 (server-owned turn stamp), SEC-023 (asymmetry) | Cooldown state transitions logged | Tune, don't punish first | §7.2's row + walkthrough |
| Coordinated peace/surrender/withdrawal abuse | Deferred (no surrender/withdrawal mechanics in the current project) | — | — | Recorded as war-stage dependencies (SDQ-008) |
| Campaign-result timing manipulation (TH-011's class) | SEC-015 + resolve-at-boundary; §6.3's answers | Attempt/outcome logged; reason string | disclosed by DP-004 | Rails exist |
| Collusion of economy × diplomacy (e.g., alli allies transferring via trade then "peace"-forcing surrender conditions) | Partially deferred; rails + R-13 installed | Graph evidence queue (§8.3) | Review-then-act per R-16 | §22's dependency note (war stage owns the rest) |
| Privileged-user improper changes (TH-017/018/019) | Ops cannot be "a party with hidden powers": every privileged change is logged (SEC-031) with reason, scoped by SEC-006/027 | Full disclosure (DP-004) | Rollback by incident protocol, per §14 (the *only* place where silent correction is forbidden) | §12 + §14 carry |
| Disputed action submission | Idempotency keys + event spine answer "was X submitted?" with *rows*, not memory | — | — | SEC-031's spine |

### 10.3 Notification and dispute requirements across diplomacy surfaces

Each *diplomacy-visible* mutation (membership change, role change, treaty state, pool draw) is disclosed to *affected* parties at the moment it lands (reason strings are part of the disclosure: who authorized, when, against which rule). Disputes route through §12; the evidence spine (SEC-031) is what makes the dispute fair; "was X submitted / what resolved" is always answered from the ledger.

---

## 11. Privacy and data governance

### 11.1 What this project should *not* collect (decided posture)

**First-playable collects no precise location, no government ID, no phone, no behavioral telemetry beyond security events, no third-party analytics, no advertising cookies, and no training-data harvesting.** The reason is not mere compliance posture; it is the *surveyable* project-gradient argument: every data category the game carries is (a) a future breach liability, (b) a moderation dispute surface, (c) legal-regime surface (OSQ-010), and (d) a trust promise to keep. The *default* posture is minimalism; expansions need justification, recorded in the §11 inventory + OSQ-010's later review.

### 11.2 The data inventory (first-playable)

| Category | Purpose | Classification | Minimum collected | Retention approach | Deletable/anonymizable | Deleted-account fate | Needed pre-launch? |
|---|---|---|---|---|---|---|---|
| Account identifiers (username, nation name, e-mail address) | Authentication + recovery; the only *personal* identifiers | Private (e-mail secret); username/nation public (identity posture per Prompt 4/5 AP-002/CX-5) | One e-mail per account (OSQ-003's verification question affects the e-mail's *trust*, not its storage); handle | For account lifetime; e-mail purged at deletion; nation/nation-name history anonymized per §4.8 | E-mail: pure delete; gameplay: delete-or-aggregate per §4.8 | Yes (core) |
| Auth/session data | Maintain credentials, sessions, and revocation | Private | Hash + metadata only (never passwords); session ids short-lived | Same as account + SEC-003's session lifetime | Deletable | Yes |
| Nation/gameplay data (treasury, dev levels, orders, trades) | The game (players expect persistence); prompts 6/7's structural design | Owner-only values; aggregates per later transparency gates (G-1…G-6) | As the game requires | Account lifetime; aggregation may outlive deletion where §4.8's rules allow | Comes with the account-deletion flow | Yes |
| Public profile information (nation description, "era of record" excerpts — the Prompt 5/6 §13 "constitution of record-keeping" concept) | Community play; nation narrative | Public (what's *designed* public — floors set by the design, not by user belief) | What the player chooses to publish | While public; player may edit; deletion = anonymized | Deletable | Yes (per Prompt 4/5) |
| Private messages / private diplomatic content | **No private-channel system is proposed at first playable** (Prompt 6's recording — SDQ-004's unresolved partner-terms privacy question carries trade-note privacy); if one is added later it must be added *with* its own inventory entry and a minimization review — recorded as a conditional dependency, not designed here | N/A at first playable | — | — | — | No (not proposed) |
| Security & abuse events | Incident review, moderation, appeals, TH-001-025's detection/attribution | Restricted (moderator/ops via SEC-031) | Fields per §13's table — never free-form surveillance; *no keystroke logging, no client-side agent* | Short-retention (90-day-class proposed; tunable); longer only for *specific recorded incidents*, in the incident record instead | Anonymize actors on appeal-closure where litigation risk allows | Yes (SEC-031's spine) |
| Moderation reports & appeals records | The §12 process's legitimate need for case reasoning | Restricted (§12's role-scope) | Case fields, not amplification | Per-case retention, closed-case auto-expiry (proposed: 1 year, tunable), longer only for pattern-tracking incidents explicitly recorded | Name-level anonymization at expiry | No (deferred — §12's tooling) |
| Operational logs | Ops debugging; not a personal-data log | Restricted | Technical rows (request shape; NO request body personal-data by default) | 14–30-day-class recommended; exceptions recorded (SEC-032's inventory) | Standard log purge; *no player-content* retention | Yes |
| IP/network metadata | Abuse signal *composition* (§8.3), rate limiting | Restricted | IP + coarse network orientation (the residential/hosting class); NO geo-locating beyond the coarse class | **Short: 30-day-class proposed** then aggregate-only | Anonymize to class-level aggregates; long retention explicitly rejected unless OSQ-010's later review demands | Yes (SEC-029's rate-limit work + abuse review) |
| Support communications (if a support channel exists) | Answering players | Private between player and operator | Whatever the player sent | Incident-certain retention; deleted with account (subject to legal-hold rules if any exist) | Delete with account | No (a support channel may exist via e-mail incident work — §12/§14); keep minimal |
| Backup data | Recovery incidents | Secret (§3.1's "a backup is every secret in one place") | Full snapshots | Rotating (proposed: 7-day rolling + a monthly anchor); §14's drill cadence | Scrubbed before use per §4.8/TH-024's row; deletion of the *account* from backups follows rotation naturally | Yes (SEC-030) |

### 11.3 Minimization rules (how to keep this honest)

1. **Collect, store, retain, serve nowhere by default** — each *additional* purpose must be recorded with justification in the inventory; anything not listed isn't operated (SEC-032's inventory is authoritative).
2. **Public by design, private by default:** for any future surface the question is "is this public *by the design's* intent or private?" — SDQ-004's open trade-terms question is exactly this discipline; it is recorded there, not assumed either way.
3. **Delete means delete:** no copy-swarm; the account-deletion flow declares per-category outcomes (§4.8) and the privacy record (a §6 "data protection posture" section in a later report's deliverables, not this report's document) should carry it verbatim when written.

### 11.4 Analytics/support/backups/third-party risk review

- **Analytics:** none proposed. If later added, the add needs its own minimization review (a recorded decision, OSQ-010-adjacent) — and, at this project's scale, aggregate counters on the event ledger (§15's monitoring rail posture) serve 90% of legitimate curiosity at zero personal-data cost.
- **Moderation access:** §12's role scoping (SEC-026/027) plus SEC-031's logging; no "mods see everything" idle access.
- **Support:** handled as ordinary incident/preference requests under the account's own rules (§11.2's categories); no separate support mailbox that accumulates personal data outside the flow.
- **Backups:** backups matter as a *privacy* control too (they contain everything); security controls their access (§3.1's facts), retention rotation bounds their lifetime, TH-024's row covers the restore-scrub posture.
- **Third parties (host, e-mail provider):** each carries its own leak and ToS risk; minimal surface = minimal shared identity data (the *game* uses only what its flows require; the provider's own account is not the project's dossier). A formal sub-processor/legal review belongs to OSQ-010's jurisdiction work, not to a first-playable task.

### 11.5 Data governance questions this report deliberately does not answer

- Legal basis/jurisdiction analysis (GDPR/UK/other Applicable regimes per actual launch market): **OSQ-010** — an owner-held call requiring counsel; no checklist here can make the claim.
- Retention numerals beyond *proposed starting postures* all remain tunable (SEC-032's "tunable" statuses).
- Any moderation-record access rule beyond §12's process — §12 owns it.

---

## 12. Moderation, reports, sanctions, and appeals

### 12.1 Scope discipline: technical exploit response is *not* conduct moderation

Two lanes, deliberately kept separate because their evidence, motion, and pacing differ:

1. **Exploit/incident lane** (a rule defect used by anyone, a compromise, a settlement bug): owned by the *incident protocol* (§14.6) + the economy's R-16 conservative posture: fix, disclose, compensate per §14.6, no *blame language*, and *no automatic competence-inference about a player's character* — a player who *reports* an exploit honestly is treated as a good actor (the report tracks the *behavior*).
2. **Conduct lane** (harassment, impersonation, deceptive naming, spam, brigading, ban evasion, false reports, misconduct as a rule-breaking pattern): owned by §12's ladder. Prompt 11's and §12's enforcement philosophy is *proportionate, evidence-based, documented, appealable*; a conduct case and a technical finding can co-excite about one event but travel separately — the *different reading* is recorded in the case file itself.

### 12.2 Report intake, evidence, and prioritization (SEC-028's design)

- **Intake:** in-game report button + optional state field. The intake records: reporter id, target(s), category, one-line summary, *time*; evidence *links* are *recorded at this stage as pointers into the event ledger* (SEC-031's spine) — the design avoids encouraging "compose a story" (the venue for hostile narrative, TH-016's "well-written false report" face) by *treating *narrative text* as a pointer to evidence*, not as evidence itself.
- **Evidence recording happens primarily via the event ledger:** the game's own mutation log carries what happened (SEC-031); the reviewer's first read is the ledger, not the reporter's essay.
- **Prioritization (proposed):** urgent classes first — threats/real-world-safety words, DM-like abuse if a private channel ever exists, impersonation of staff, and *anything involving minors* — with self-harm/safety cases routed to a documented external-resource posture per general platform practice; then name-guard/rename requests (fast, low stakes), then conduct, then trade-graph reports (§8's lanes). Two tiers is enough at first population scale (§12.6's staffing honesty).
- **Source awareness:** the reviewer sees *who* filed each report (SEC-028's design) so as to weigh motive over narrative; *mass* filing an account's *pattern* (a stereotyped cross-account report cluster) is itself reviewable conduct (TH-016's row).
- **Appeals & review-of-overturns:** petitioned outcomes get a second *set of eyes* where staffing allows (appeal-to-a-different-reviewer is the recommendation; a single-creator project honestly notes "the same person" as the *default*, and OSQ-005 owns this constraint), and *any* overturned sanction is reviewed for its own process quality (§12.5's calibration loop).

### 12.3 Proportionate action ladder (proposed, not owner-approved)

| Level | What it means | When appropriate | Authority |
|---|---|---|---|
| 0 | Educational action (a warning message or a correction) | First minor misstep, name-guard fix; honest mistake framing | Any moderator (SEC-026 scope) |
| 1 | Formal warning, recorded in the case file | Repeat minor; first instance of a mid-tier violation | Any moderator (logged) |
| 2 | Cooldown / feature restriction (temporary loss of one surface: trade, chat-like channels if any exist, reporting) | Gaming a specific surface; a *pattern* at one lane | Moderator with scope (SEC-026/027 boundary) |
| 3 | Temporary nation suspension (freeze of nation activity, cooldown-scale) | Serious conduct violation; evidence-based-continuing-abuse | Senior/owner (SEC-027's elevated perms) |
| 4 | Account suspension / ban | Confirmed serious or repeated violation; ban evasion | Owner (and two-person rule where two people exist; SEC-027) |
| 5 | Sanctions-adjacent measures (state-visible actions like a name force-rename, a public disclosure per DP-004 treatment) | Configured per community norms at launch | Owner (SEC-027's most destructive tier) |

Every sanctioned action carries *reason lines* from the case evidence; every action above level 1 is logged (SEC-031); a **two-person rule** (SEC-027) is recommended for levels 4–5 *when two trusted adults exist* — an honest acknowledgment that this is a small project's constraint, and the compensating control is the owner's *disclosure-first* accountability (TH-019's posture and OSQ-012's structure question).

### 12.4 Special cases the ladder covers

- **Impersonation:** instant rename to a neutral placeholder + a level-2+ case with a documented pattern (per §12.3's tooling).
- **Offensive/deceptive names:** the name-guard (§4.1's registration check) screens the *obvious* cases at creation; *discovered* later, the same ladder path with a rename to a placeholder.
- **Exploit *use* (behavioral):** a special rule — the *first* honest report of an exploit is **rewarded as an incident** (§12.1's lane 1: it's an incident, not a conduct case) *unless* the player *persisted* after disclosure (then it's a conduct case for "continued, deliberate exploitation after the fix" — a deliberate, level-2+ posture).
- **Ban evasion (TH-020):** evidence-gated (conduct + transition evidence); the appeal path *remains* for a mistaken accusation (SEC-026's review flow) — accusations without evidence are *both* an unfair action on the accused *and* a review-body duty to close with a reason.
- **False/malicious reports (TH-016):** a *preference* for narrative-deception tactics is a conduct case, on evidence, with its repeat-cluster pattern tracked; one false report (a good-faith mistake) is level-0 at most.
- **Brigading an account** (TH-016's "getthispersonbanned" pulse; the *pattern* across accounts): the *group's* behavior is a conduct case (level-2+ on the coordinator where identifiable), not a tool-free-for-all on the target.

### 12.5 Moderator power protections, and the one-person reality

- **Powers are scoped, and acts are logged:** separate ops identity (SEC-006), role ladder with explicit grants (SEC-012's authority-table pattern applied to mods), and *every* moderation act logged with reason (SEC-031). A single moderator cannot unilaterally do the most destructive things without a record (the two-person rule at level 4+ where staffing allows; otherwise the owner's own acts are logged and disclosed).
- **Conflict-of-interest rule:** a moderator reviewing a case involving their own alliance/ally/friend recuses and routes it to another reviewer; when the *owner* is an involved party, the same rule applies *to the owner* (TH-017's compromise path / DP-004's "operators follow rules too"), and, where the community exists, a public-review posture may be *offered* (community norms decide; not a rule of this report).
- **Missing staffing (the small-project honesty, PXE-011's constraint):** with one operator, the *process* is acceptable if: (a) the *elected* evidence spine (SEC-031) is what does the work, (b) escalated cases wait hours-not-minutes without a need to hide it (§12.2's tiering is *proposed* to make this honest), and (c) **OSQ-005's decision on whether to scale moderation (player mods? a "trust & safety" role?) is an explicit owner question** recorded with its trade-offs (§20).

### 12.6 What §12 promises, and what it cannot

It promises: a *documented, evidence-based, proportionate, appealable* ladder with logged acts. It **cannot** promise: instant response (staffing), perfect separation of abusive/false accusations (evidence limits), or a fully-human-verified removal path for every edge case. The honest posture is *appeals stay open, disclosure is total, and the ladder's proportionality is a calibration target reviewed per case* — recorded in the report's §22 checklist for owners to decide the final policy (OSQ-005's family).

---

## 13. Audit logging, detection, and evidence

### 13.1 Design posture: an evidence spine, not a surveillance system

What makes the moderation, compromise, and dispute processes workable (§4.6, §8.4, §12) is a *ledger of what the server actually did* — not a log of what players said or did in every corner. The design rule this section fixes:

- **Log every *state-relevant* event** (a mutation, an authorization decision, a session lifecycle event, a privileged act, a rate-limit trip), with enough fields to answer: what happened, to which object/turn/transaction, by what actor, through which surface, with what result.
- **Never log free-form player content by default** (chat-like messages, trade notes' text, appeal essays): reference them by pointer only, and only in a record that *needs* them (a conduct case file). The ledger is a *pipeline journal*, not a diaries archive.
- **No client-side agent, no keystroke logging, no monitoring SDKs.** The data inventory (§11) is the Snowden check on this section; every field either enters §11.2's table explicitly or it isn't collected.

### 13.2 The event table (security-relevant events, fields, retention)

Global fields on *every* event row: `event_type`, `event_id` (unique), `timestamp_*` (server clock = authoritative for turn/transaction correlation), `actor_account` (nullable for system events; the *acting nation* where applicable, per SEC-012's authority model), `actor_class` (player/session/admin/scheduler/system), `turn_t` (where applicable — the SEC-015 server stamp), `txn_or_object_id`, `result` (committed/failed/…). Category-specific fields below; **never** collected: password values/derivatives, session-token *values* (only session *ids* in revocable form), free-form message bodies.

| Category | Events (typical) | Extra fields | Purpose | Retention (proposed) | Sensitive fields *not* logged |
|---|---|---|---|---|---|
| Authentication | sign-in success/failure (per method), step-up challenge issued/passed/failed, password change, recovery request issued/used, recovery contention lockdown begin/end | per-account + per-source coarse identity, method, outcome; failure reasons enumerated-resistantly | TH-001/002/014's detection; §4.5/4.6's response | 90-day-class; longer only within a recorded incident case | Hash parameters per-account? no — they're *config*, not logged content |
| Session lifecycle | issued, rotated, revoked (by whom), absolute-expiry events | session id class, actor | TH-002's availability + §4.3 | 90-day-class | Token values — never |
| Privilege changes | ops login, privileged act (any of §3 B6's verbs), scope grant/revoke, two-person-rule approvals (where applicable) | acted-on object, reason line | TH-017/018/019's entire story; SEC-031's privileged-read-is-an-event rule | Permanent-assumption at project scale; reviewed per data-inventory review | Nothing (this is the accountability layer) |
| Treasury & resource mutations | every balance/resource delta with *before/after* or delta + cause; production cycles; upkeep; purchases; respecialization state changes | nation, amounts, cause (queue/order/upkeep/admin-grant), the pipeline step id | economy integrity (R-16's evidence posture; TH-006's class); §14's reconciliation ability | Permanent (small rows; §15 shows the budget holds) | None (these are the audit rows) |
| Trade lifecycle | listed/submitted (paired when accepted), modified, cancelled (by whom), settled-partial-never (R-19's atomic pair), refund events, per-pair ledger append | both nations, amounts, order id, idempotency key | TH-003/004/007's evidence; §7's disputed cases | Permanent | No notes-text |
| Turn pipeline | use-claimed, per-phase start/complete, resolver identity, abort/exception, duplicate-claim refusal, delay announcement | turn T, phase id, worker id | TH-009/010/023's evidence; SEC-019/20/21's enforcement | Permanent | — |
| Strategic orders & outcomes | queued, attributed, resolved-at-boundary, tiebreak-applied | nation, order class, turn stamp | TH-011/022's disputes; campaign-order references | Permanent | — |
| Alliance administration | membership/role changes, pool draws/grants, treaty-state changes (parties, state, idempotency key) | alliance id, actor role, verb, target | TH-021's reviews; §10.2 | Permanent | Private terms text (pointer only) |
| Rate limits & abuse counters | cap-tripped (per class), throttled delay applied, public "temporarily capped" reason issued | source class, route class, count | §9's posture + TH-012 | 30–90-day-class | Source IP *class* only after §11's short-retention horizon |
| Moderation | case opened/closed, action taken (level, reason), appeal filed/decided, file-reading events | case id, actors, level | §12's ladder accountability | Per-case permanence + expiry per §11.2 | Narrative text stored in case pointers, not ledger rows |
| Admin interventions & corrections | manual materialization/corrections; §14.6's compensations, restorations; two-person approvals | what changed, cause, who, approvals | §14's trace; SEC-030's reconcile | Permanent | — |
| Backups & restores | backup start/end (success), restore verification, *what was restored to which turn* | snapshot id, target turn | TH-023's drill and disclosure | Rolling per §11.2's backup row | — |

### 13.3 How ordinary play and signals stay distinguishable

The abuse posture used everywhere in this report works **counter-verbs** (§13's table has counters the §15 dashboard reads), not content. "Enough to investigate, not enough to surveil" — three rules fix the line:

1. **Thresholds trigger review objects, not outcomes:** rates, deltas, or graph anomalies open a *review queue item* (a human look, or at scale an evidence bundle); nothing *acts* on one signal. (SEC-026/028's process owns what follows.)
2. **Sensitivity-of-signal is a stated rule:** auth-failure bursts and rate-trips are *ambient noise* (TH-001's volume argument); repeated *cross-attempt flushes* (same account tripping different authorization surfaces) or *graph-shape repetition* are the signals worth a reviewer's hour; the reason *why* the signals matter is written into §13's documentation so a reviewer's judgment isn't inherited from a mystical score.
3. **No private-content logging by default, ever:** §13.1's posture is a *requirement*, enforced as a code-review item at implementation.

### 13.4 Correlation and the "which turn/transaction" question

Event rows carry both a `turn_t` stamp and the pipeline step or transaction id; a *single* dispute ("was my trade settled?", "was this economy value granted twice?") is answered by reading *rows*, not reconstructing memory — this is the property that makes §14.6's reconciliation and §12's appeals both *fair and cheap*, and it is why SEC-031's spine earns stage-B status on its own merit.

---

## 14. Reliability, backups, restoration, and incident response

### 14.1 What this game's 2-hour cadence implies

The resolution pipeline runs 12×/day, always. Its failure modes are *the game's* failure modes — a stuck resolver is a *whole game* outage (the prompt's warning is precisely that this must never be an afterthought). What the design supplies to defend it: SEC-019/020/021's *phased, idempotent, forward-only* pipeline; the *write-budget reservation* (§15) so a busy day cannot starve the resolver; SEC-022's *honest communication* when it does fail.

### 14.2 Backups and restore discipline

| Item | Requirement (proposed posture) |
|---|---|
| Backup frequency | Daily snapshot (rolling 7-day window) + one monthly anchor, *before* the cost/ops tier rises. Where the free tier can't carry snapshots at scale, backup *clarity* is the fallback — a worst-case "ops-error ends a nation" risk *disclosed* to players (OSQ-007 owns the owner's cost call) |
| Restore-point targets | Named per restore; a restore declares its target turn T and its *snapshot id* up front (SEC-030's posture) |
| RPO (assumption, tested) | ≤24h of player state at the tested tier; stated as assumption, never a guarantee without a drill (OSQ-007) |
| RTO (assumption, tested) | Restore + verify within 1–2 hours *at the tested tier*; again, a posture, not a decision |
| Restore verification | Pre-verified *procedure*: after any restore, resolver checkpoints exist, the ledger reads coherent for turn-R, and an anomaly-comparison tool covers §14.4's reconciliation rule before players are invited back (TH-023's row + ST-009's drill) |
| Restore *scrubbing* | Restore images used as *sources of truth* for restore *never* land in a player-visible surface without a data-scrub review (SEC-032's inventory; TH-024's row) |
| Turn-processing recovery | §6.4's table carries it (forward-only resume; SEC-021/020/022) |
| What is *never* allowed | A restore that silently revives *already-settled* actions (TH-023's "players' settled trades reappear" hazard); silent re-derivation of a turn's outcomes (Prompt 7 §14's contract) |

### 14.3 Incident severity classes (proposed)

| Class | Definition | Response posture |
|---|---|---|
| Sev-1 | Any confirmed loss/corruption of authoritative player state (data bug, restore misuse, compromise with drain, insider misuse of access) | Owner notified *immediately*; open status update posted in each phase (DP-004); compensation flow (§14.6); a written post-incident review (§14.7) |
| Sev-2 | Service unavailability lasting past one turn boundary; resolution partial/repeated *detected and stopped* (SEC-019/020's guard fired) | Turn delay announced (SEC-022); recovery per §6.4; post-review if player-visible harm occurred |
| Sev-3 | Single-account compromise, moderate abuse cluster, exploit report on a live surface | Per §4.6/§12's lanes; itemized case handling with notifications |
| Sev-4 | Rate-limit storms absorbed, scraping bursts, minor conduct | Counter/dashboard handling; §9's posture; no per-event case file needed |

Between classes, the *escalation* rule is "what players visibly depend on": anything that touched multiple players' authoritative state escalates.

### 14.4 Reconciliation after a correction or restoration

Prompt 7's truthfulness contract carried verbatim: **player-visible history is never re-written without a disclosure row.** The design's reconciliation rules:

- A correction/compensation/restore *names what changed and why* (SEC-031's admin-intervention rows; §14.6's communication contract); player-visible history that was *already delivered* (digests, trade-confirmation pages) is not edited in place — the correction is a *new visible event* referencing the id it corrected (the "append-only visible history" posture).
- Where a restore sets the authoritative state *earlier* than player-visible history (the prompt's explicit hazard — §14.2's "restore discloses restored-to-T" rule), the player-visible digest must *say* "restore performed, current state is the state as of turn T; actions processed after T are void and were annulled; affected trades listed here..." — the *harm* control is disclosure + §14.6's compensation, *not* invisible surgery.
- Values double-created or double-deducted by any path (including ops grants and compensations) reconcile from the ledger *before* the value exists — grant ids carry idempotency discipline (§7.2's compensation row).

### 14.5 The one admissible exception to "no silent correction"

None. No silent corrections. The design's trust product (§12.1's honesty lane) outranks ops convenience; if a correction must happen *before* disclosure is possible (security-sensitive: an ops misgrant while credentials are live), the *event rows* record it *at once*, and the *visible* disclosure happens as soon as the incident window ends (a documented maximum, proposed: within the same turn or ≤6h, whichever is shorter).

### 14.6 Player compensation (proposed posture, not owner-approved)

Damage from *server-side* failures (settlement bugs, restores, compromises *evidenced* as drain, ops errors): `compensate within the damage actually established from evidence`, disclosed with reason lines. Damage from *player-side* loss *not* caused by a security failure (a player's own mistimed order, a self-chosen trade outcome) — *not* compensated, and *that rule is stated publicly* so expectations are honest. A compensation *budget* rule is an OSQ-family tunable, not a security rule.

### 14.7 Post-incident review and corrective-action tracking

Every Sev-1/Sev-2 gets: a written review (what happened, evidence, timeline), a corrective-action list with *owners and dates*, a check that the review *closed* (§25's own QA)— the *hold-until-proven* rule is that corrective actions without dates are tracking items, not closed remediations. Sev-3/4 reviews are optional but encouraged when patterns appear (§13.3's signal-value study).

### 14.8 Evidence-loss protection

- The event ledger's writes ride the *same* durability class as the authoritative state (§15's budget table reserves them together); a quota-exhaustion event *must not* prioritize gameplay writes *ahead of* audit rows for the events that caused the exhaustion (SEC-031's ordering rule; a design detail noted for the architecture stage).
- Log *sampling* (if §15's budget ever forces it) applies to *high-volume* rows only (auth attempts, rate events), never to money-touching or pipeline rows.

---

## 15. Free-first security and cost control

### 15.1 Where the costs actually land

Prompt 1 §6 documented the platform facts (D1 free tier: 100k row-writes/day with enforcement since 2026-09-01; the free plan's cron CPU posture sold by Prompt 7 §16.4's S1–S3 research rows); Prompt 7 §16.3 built the economy's write-budget framework. §15 does not re-derive those; it re-uses them, *verified at these cites*, and states security's marginal costs on top of the economy's floor:

| Control | Marginal cost (qualitative; exact numbers belong to the architecture stage) | Notes |
|---|---|---|
| Authentication (passwords or equivalent) | Zero infra; hash cost negligible at 12-turn cadence | §4.2's table |
| Rate limiting + quotas (SEC-029) | *Negative* net cost: throttling abusive clients protects the same quota the game runs on | The cheapest, highest-value control |
| Abuse monitoring (§13's counter dashboard) | A few read-only aggregations; near-zero | §13's table; SEC-033's rail formalizes it |
| Audit logging (SEC-031) | A fixed *row* cost per event — the one cost this report refuses to cut; §15.2 shows the budget carries it | Prompt 7 §16.3's framework re-used |
| Backups (SEC-030) | Snapshot storage is the real cost item at population scale; the *daily+rolling* posture starts cheap (OSQ-007's call to scale it) | §14.2 |
| Monitoring/alerts (SEC-033) | A quota/rate dashboard + failure alerts; costs a little read-write; free tier accepts a minimal version | §15.3 |
| Moderation tooling | At first population scale: the *open case queue* + the event ledger as its read surface, cost ≈ 0 beyond §12 | §12.5's one-operator honesty |
| Recovery procedures | The *drill time* is staff time, not compute (ST-009's cadence) | §14.2 |
| External services | E-mail send budget is the only proposal needing a provider; a free tier fits recovery-only traffic if OSQ-003 chooses e-mail-as-anchor | §11.2/§4.4 |
| Database writes & storage | Security's *added* rows are: event ledger, session/revocation bookkeeping, idempotency-key rows | §15.2's budget |
| Scheduled turn processing | Already the economy's own posture (SYS-016); security's only addition is the claim discipline (cheap) and phase row writes (already the economy's shape) | §6 |
| Incident investigation | Mostly staff time; tooling covered by §13/§15.3 | §14 |

### 15.2 The write budget (security's share)

Derived from Prompt 7's counters (§16.3's economy floor for 12 turns/day at the current design's population assumptions):

- **Event ledger is *part of* mutation transactions.** §13's requirement is structural: money-touching and pipeline rows ride the *same transaction* as the change, not a separate batch. So §15.2's budget is *additive but tight* — the ledger rows are the second row of most mutation commits, and §15.1's table shows the whole-list cost stays inside the D1 write floor at the design's population scale.
- **What is *sampled* instead (allowed by §13.4's exception):** auth-failure *counts* (aggregate counters, not rows), rate-limit trips (counter-first, row-on-first-trip), read-endpoint analytics (none kept by default — §11.2's analytics posture).
- **What is *never* sampled:** settlement rows, turn-phase rows, privileged acts, compensation/restoration rows, grant keys, moderation acts. The rule is explicit so the architecture stage can't "optimize" integrity rows away — *integrity logging may not be sacrificed to quota; it may be tiered.* §15.3's monitoring rail is the *tunable* tier, not the integrity one.

### 15.3 Monitoring/alert posture (SEC-033's shape, minimal version)

Two counters surfaces at the architecture stage's minimum:
1. **The free-tier budget gauges** — D1 row-writes read against 100k/day, cron-CPU posture S1–S3 from Prompt 7 §16.4's research, the e-mail send counter where OSQ-003 applies it — per §15.2's failure posture: overflow failures are *detected* (they must be loud, never silent).
2. **The abuse counters** — §13.3's counter verbs (auth storms, quota trips, idempotency collisions, creation bursts, denied-authorization clusters) with a review dashboard.

Alerting on *quota-exhaustion risk* and on *pipeline stall* (Sev-2's *detection*) are the two highest-value alerts on a free-first budget, precisely because both are *silent-failure* classes that small teams miss.

### 15.4 Which protections are essential even if they raise cost — and which defer safely

**Essential before any public playable (stage A; §16/§17's assignment):** SEC-010/011/012/013 (server authority), SEC-014/016 (idempotency + atomicity), SEC-018/019/020/021 (turn pipeline integrity), SEC-025 (arithmetic invariants), SEC-029 (quotas). **Nothing on this list is cut to save money, and none should ship late**: they are the *validity* of the game's own object. **Twelve requirements** are assigned to stage A, plus the audit-spine subset of SEC-031 described in §17.1 A8 (SEC-031's full §13.2 coverage remains stage B). The 12 would be cheaper than any settled argument if they are precisely specified — and they are. *(Count corrected 2026-10-23; the earlier "16" was a stray figure that matched neither the stage table, the A-list, nor this list. See §22.2 item 6.)*

**Waiting until public-launch (stage B):** the account stack's *full* depth (SEC-001–005, 007/008), abuse-evidence rules (SEC-023), moderation ladder (SEC-026), backups + restore discipline (SEC-030), audit spine (SEC-031). **Later hardening (stage C):** SEC-006 (admin separation — a single-operator project's posture), SEC-015 (turn-stamp server-side attribution), SEC-017 (ledger discipline), SEC-022 (delay disclosure contract), SEC-024 (abuse evidence retention), SEC-027/028 (its own moderation tooling), SEC-032 (data inventory), SEC-033 (monitoring rail). *Why these defer:* they harden *against edge abuse at scale* (the stage A surface's customers don't hit them yet), and their *equivalent minimum* is available early: the single-operator reality (§12.5), the economy's own defaults, the counters dashboard's early shell.

---

## 16. Security requirements and priority levels

### 16.1 The prefix check (recorded as required)

The `SEC-###` prefix was checked against the project's existing ID spaces before adoption (§0.2's read of all continuity files; Prompt 6 §22.2's editor's note on the same discipline): the *SEC-* prefix is **unused** in any earlier prompt's registers, so it is adopted here. The `TH-###` (threats), `ST-###` (tests), and `OSQ-###` (owner questions) prefixes are likewise new here (§24's register records the verification). The gap at **SEC-009 is a deliberate reservation (unassigned)** — the gap is kept for readability of the account-security block (§4's requirements numbered 001–008) with the request-integrity block starting at 010; the number is never re-used by a different concern (§24's register documents the gap). Total register: **SEC-001…SEC-033 with SEC-009 unassigned = 32 defined requirements**, exactly the count stated in §0/§1.

### 16.2 The register

Notation: **FP** = required before the first playable version; **PL** = required before public launch; **L** = later hardening. Every row includes a reason/trace line and an acceptance criterion ("AC:"); verification methods are named (`VM: test` ⇒ the acceptance test lives in ST-###; `VM: review` ⇒ the design/doc carries it; `VM: drill` ⇒ an ops rehearsal). Status for every SEC: **proposed (not owner-approved)**.

| SEC | Title | Requirement (testable) | Asset/risk | Priority | Reason/evidence | Threats | Related IDs | Deps | Acceptance criteria (AC) | VM | Stage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SEC-001 | Unique verified account identity | Every account has one unique identity credential; duplicate-identity creation attempts are refused *with a reason*; verification posture (e-mail confirm or OSQ-003's fallback) is applied per policy before any e-mail-dependent flow can run | Player identity; TH-001, TH-013, TH-020 | PL | Genre evidence on account-stuffing; Prompt 4's onboarding | TH-001/013/020 | PXE-001…019; OSQ-003 | Account flow design | AC1: duplicate-identity creation returns an honest refusal; AC2: verification state gates e-mail-dependent flows at the right scope | test | PL |
| SEC-002 | Password handling + step-up | Passwords stored as memory-hard hashes (Argon2id-class) with per-account salt; step-up verification is *scoped to sensitive actions* (recovery-e-mail change, account deletion, high-value transfer) | Account takeover (TH-001) | PL | OWASP Authentication posture; §4.2's option table | TH-001 | OSQ-002 | — | AC: no plaintext or reversible password representation anywhere; step-up enforced on the scoped list | test | PL |
| SEC-003 | Session issuance/rotation/revocation | Sessions are bounded (absolute expiry), rotate on credential change, and are revocable per-session and per-account; token values never appear in URLs | Session theft (TH-002) | PL | OWASP Session Management cheat sheet's absolute-timeout posture (§21) | TH-002 | INT-011's session binding framing | — | AC1: stolen-token scenario dies at expiry/revocation; AC2: password change revokes all sessions | test | PL |
| SEC-004 | Rate-limited recovery | Recovery attempts are throttled per e-mail and per source, with escalation, and never leak account-existence | Recovery abuse (TH-014) | PL | §4.4's design; TH-014 | TH-014 | SEC-005 | — | AC: throttle trips at proposed thresholds; failure responses don't enumerate accounts | test | PL |
| SEC-005 | Login attempt caps + honest lockout | Sign-in attempts capped per account and per source with escalating delays; lockout clears itself and explains | Credential stuffing/guessing (TH-001, TH-014) | PL | OWASP + genre | TH-001, TH-014 | SEC-004 | — | AC: cap enforced both per-account and per-source; message never enumerates | test | PL |
| SEC-007 | Sensitive-change notifications | Account-impacting changes (email change, password change, session revocation by ops, recovery event, deletion request) notify the account owner | Compromise awareness | PL | §4.6's containment | TH-001 | SEC-031 | — | AC: each listed change emits one notification | test | PL |
| SEC-008 | Compromise response runbook | A documented, tested-though-rehearsal procedure: contain (revoke), notify, evidence-review of in-game acts in the compromise window, reversal only where evidence is unambiguous | Takeover aftermath (TH-001, TH-018) | PL | §4.6; R-16's conservative posture | TH-001, TH-018 | R-16; SEC-031 | — | AC: runbook exists, lists triggers/steps, rehearsal recorded | drill | PL |
| SEC-009 | — (placeholder row) | — placeholder row intentionally blank (documentation symmetry; SEC-009 stays unassigned — a reserve, not a usage) — | — | — | — | — | — | — | — | — | — |
| SEC-010 | Server recomputes all valuable quantities | Every mutation recomputes its quantity from authoritative state; a client-submitted quantity is request *intent*, never source of truth | Client-side value manipulation (TH-006) | FP | Prompt 7 §14's honest-preview rule + Prompt 6 §17's not-client-trusted contract | TH-006 | ECON-001 | — | AC: substituted-quantity tests rejected (ST-001/002) | test | FP |
| SEC-011 | Per-action validation list | Each write action carries an explicit validation checklist (eligibility, affordability, cooldown, prerequisites, bounds) *completely* evaluated before commit | Any invalid action | FP | Prompt 7's §14 pricing discipline | TH-006/008/011 | SYS/INT ranges | — | AC: every listed endpoint's checklist exists and is exercised | test | FP |
| SEC-012 | Per-resource authority model | Every object's actions validate the actor's authority against a server-side role/authority table; the acting nation is resolved from the session, never a parameter | IDOR (TH-008), unauthorized alliance verbs (TH-021) | FP | Prompt 7 §11's per-nation privacy framing | TH-008/021 | SDQ-014 (dependency) | — | AC: spot-swap tests rejected on every action family (ST-006) | test | FP |
| SEC-013 | Input bounds + integer guards | Every write request is shape-validated (types, ranges, lengths) against a declared schema before business logic | Malformed input; overflow (TH-006's edges) | FP | §5.2's firewall posture | TH-006 | — | — | AC: type/bounds matrix returns honest rejections (ST-002) | test | FP |
| SEC-014 | Idempotency keys per write action | Every write (trade, order, campaign claim, refund, grant, compensation) carries an idempotency key; duplicate keys coalesce to the first committed result | Duplicate/replayed requests (TH-007) | FP | Prompt 7 §14; R-18's flood posture | TH-007 | R-18 | — | AC: duplicate-key tests coalesce (ST-005) | test | FP |
| SEC-016 | Single-spend atomicity + no-debt invariant | Any single balance-debiting mutation commits fully or not at all (no partial); treasury never goes negative; no debt exists outside design-approved ECOQ-007 trade-credit | Economy corruption (TH-006/007/009) | FP | ECON-001; Prompt 7 §14's two-checkpoint model | TH-006/007/009 | ECON-001; ECOQ-007 | — | AC: Racing-two-spend tests (ST-004) resolve one-winner | test | FP |
| SEC-018 | Deterministic boundary resolution + published tiebreaks | Every resolution-at-boundary follows a published deterministic order; ties break by the *published* rule, never by arrival order alone | Fairness under races (TH-004/011/022) | FP | Prompt 7 §14 (already the contract); realizethe prompt's "manual tiebreak" requirement | TH-004/011/022 | ECON-...; §14's ties | — | AC: tiebreak behavior matches the published rule in every race test (ST-010 class) | test | FP |
| SEC-019 | Single authoritative resolution window | Resolving turn T requires an exclusive claim; second claimers exit no-op; claims are recorded with worker identity | Duplicate scheduler runs (TH-009) | FP | Prompt 1 §6's cron-limit posture; TH-009 | TH-009 | SYS-016 | — | AC: duplicate-run test (ST-007) yields one resolution | test | FP |
| SEC-020 | Turn state ledger + staged checkpoints | Turn T's phases each commit a completion marker on success; a resume runs only uncommitted phases | Partial processing (TH-010) | FP | §6.4; Prompt 7 §14's "never silently re-derive" | TH-010 | SYS-016; EX-1 F | — | AC: crash-mid-phase → resume completes only the remaining phases (ST-008) | test | FP |
| SEC-021 | Phase-grain dedup (no double-apply) | Resume/migration/duplicate delivery cannot apply an already-applied phase's effect twice, provable from the ledger | Double-apply (TH-010) | FP | §6.4; §14.4's grant-id discipline | TH-010 | SEC-020/030 | — | AC: resume-must-not-double tests (ST-008/009) pass | test | FP |
| SEC-025 | Server-side no-negative/no-overflow invariants | Every mutation's final state respects non-negative balances and magnitude-bounded quantities; violating states are structurally unreachable, not caught-after | Arithmetic corruption (TH-006's edges) | FP | ECON-001; §7.2's bounds row | TH-006 | ECON-001 | — | AC: bounds/overflow matrix (ST-002) holds invariants | test | FP |
| SEC-029 | Per-action-class quotas (scheduler-reserving) | Write/read/fetch/creation/scheduler classes have resource-class quotas sized under §15's budget; the scheduler's class is reserved so player-triggered paths cannot starve resolution | Quota attack; service abuse (TH-012/013) | FP | Prompt 1 §6 limits + Prompt 7 §16's budget; TH-012 | TH-012/013/025 | R-18; G-2; CCR-010 | — | AC: flooded-client test (ST-011) throttles without bleeding resolution's budget | test | FP |
| SEC-023 | Fresh-account restrictions + per-pair velocity caps (under test conditions) | The economy report's fresh-account caps/velocity limits are enforced server-side *including the outgoing side* (asymmetry) so alt-sabotage (TH-005) also fails | Funneling/sabotage (TH-003/005) | PL | R-13 family; ECON-013's directed-trade rules; Prompt 1/3's genre evidence | TH-003/005 | R-01/R-13; ECON-013; OSQ-001 | Fresh-account design values (ECOQ family) | AC: funneling detection test (ST-016) surfaces the pattern *for review*, nothing auto-punishes | test | PL |
| SEC-026 | Sanctions ladder with logged acts | A documented proportionate-action ladder (§12.3) where every act above level 1 is logged with per-object scope checks | Conduct abuse (TH-015/017) | PL | §12; PXE-011 | TH-015/017 | OSQ-005 | — | AC: ladder prose exists; per-act logging verified in a review drill | review | PL |
| SEC-030 | Backups + restore discipline (verified procedure) | Daily rolling backups + monthly anchor (proposed posture); restores are pre-verified procedures with named snapshot + target turn; a restore drill is run before launch | Ops-error loss; ST-ale restore (TH-023) | PL | §14.2; OSQ-007 owns the cost tier | TH-023 | SEC-031; EX-1 F | — | AC: restore drill (ST-009) completes within stated RTO posture and verification passes | drill | PL |
| SEC-031 | Audit event ledger (the evidence spine) | §13.2's event table is *the* required ledger: each listed category with its extra fields, retained per §13.2, no sensitive values collected, ride-the-same-transaction ledger writes | Every TH's evidence posture; overall incident/compromise/abuse handling | PL | §13's design; the one cost §15 refuses to cut | All | — | §15.2's budget floor | AC: spot audits of each category's rows (ST-012's read surface) | review | PL (money/pipeline spine rows required at A8; full §13.2 coverage at B5) |
| SEC-006 | Admin/ops account separation | Ops access is a distinct identity surface (no player session grants ops), with mandatory step-up, scoped verbs, and logged privileged reads | Privileged compromise/insider (TH-018/019) | L | TH-018/019; §4.7 | TH-018/019 | OSQ-012 | — | AC: ops verbs enforce step-up; privileged reads appear in the ledger (ST-014) | test | L |
| SEC-015 | Server-defined turn stamps | Requested-at-T is *decided* by the server under a published boundary rule; client-claimed turn ids are never authoritative | Boundary racing (TH-011/022) | L | §6.3; Prompt 7 §14's classification | TH-011/022 | EX-1 F | — | AC: stale-turn behavior test (ST-010) matches the contract | test | L |
| SEC-017 | Settlement/accounting ledger discipline | Settlement (economy and turn) writes are append-only next-able rows that prove what applied; "already applied" is provable, not assumed | Double-apply/replay support (TH-009/010) | L | Support posture to SEC-020/021 | TH-009/010 | SEC-020/021/030 | — | AC: ledger rows suffice to *prove* the phase dedup (ST-008/009's evidence step) | review | L |
| SEC-022 | Delay/missed-processing disclosure contract | When a turn cannot resolve (or resolves late), a player-visible disclosure of status and remedy is issued; no silent re-derivation | Turn disruption communication (TH-010/022's class) | L | DP-004's honest-discipline posture in incident space; §6.4/§14 | TH-010/022 | — | — | AC: scripted stall yields a queued-visible disclosure (walkthrough W-18-L notes it) | drill | L |
| SEC-024 | Abuse-evidence retention policy | Evidence *extracted* for a review (graph shapes, session/configuration notes-per-report, moderation files) is defined, minimized (SEC-032's rules), retained only as long as a case needs (proposed cadences per §11.2) | Review integrity; privacy (TH-016/024) | L | §8.3/§11; prompt 3 §8's integrity warning | TH-016/024 | SDQ-004; OSQ-010 | — | AC: retention policy text exists; case-file spot checks follow it | review | L |
| SEC-027 | Elevated permission + two-person rule for the most destructive ops | Levels 4–5 of §12.3's ladder and ops-grade corrections require step-up + a second identity (where two exist) and are fully logged | Malicious/compromised privileged (TH-017/018/019) | L | §12.5; TH-019's proposal | TH-017/018/019 | OSQ-012 | — | AC: two-person approvals appear in the ledger for destructive ops (ST-019) | drill | L |
| SEC-028 | Report intake design | Reports record source, target, category, time (§12.2); evidence links are pointers, not essays; repeat clusters are de-prioritized for review, and the source identity is visible to reviewers | Report abuse (TH-016) | L | §12.2 | TH-016 | OSQ-005 | — | AC: intake fields exactly as listed; reviewer-side source visibility verified (ST-015) | review | L |
| SEC-032 | Data inventory + minimization discipline | The §11.2 category table is authoritative: no other personal-data category is operated on without recorded justification + minimization review; retention numerals are locked in the inventory | Privacy posture (TH-024) | L | §11's posture; D-003's decision discipline | TH-024 | OSQ-010 | — | AC: inventory exists and matches the operated surfaces | review | L |
| SEC-033 | Minimal monitoring rail | The §15.3 posture (budget gauges + abuse counters + the two loud-failure alerts: quota risk and pipeline stall) exists, checked at the ops cadence | Silent failure / quota attacks (TH-012/013) | L | Prompt 7 §16.4's S rows; §15.3 | TH-012/013 | — | — | AC: both alerts fire in scripted quota/stall drills | drill | L |

(SEC-009 is intentionally unassigned; see §0.3's note and §24's register.)

### 16.3 Traceability note

Every threat row in §2.3 has at least one mitigation among the 32 requirements above (prompt's "every critical threat must have at least one prevention, detection, or recovery requirement" is satisfied per row — §25's traceability audit re-verifies it mechanically). Every requirement's `VM:` row either names the ST-### acceptance test that will verify it or names the review/drill that does; no requirement promises a test that doesn't exist in §19's register.

---

## 17. Prioritized security roadmap

### 17.1 Stage A — required before the first playable version

These are the protections without which core game integrity cannot be trusted *regardless of player count*, whether the first build is "test server with ten friends" or "public free alpha." Each item names the requirement(s) it corresponds to and *why it cannot defer*:

| # | Work item | Requirements | Why it cannot defer |
|---|---|---|---|
| A1 | Server-authoritative recompute of every valuable quantity + the per-action validation list implemented for every shipped endpoint | SEC-010, SEC-011 | The browser being an untrusted display layer is the entire validity premise of the economy; anything else is decoration (Prompt 7 §14's honest-preview rule already commits the *design* — this is its enforcement) |
| A2 | Per-resource authority model (nation-from-session; per-verb authority table for alliances, later war) | SEC-012 | Without it, a single endpoint bug becomes account-equivalent compromise (TH-008's class); it is also *cheaper to exist-correctly now* than to retrofit an authority argument into existing routes |
| A3 | Input bounds + integer guards on every write | SEC-013 | TH-006's edge-class results in minted/destructed value from one malformed request |
| A4 | Idempotency keys per write action (incl. refunds, grants, compensations) + single-spend atomicity + no-debt invariant | SEC-014, SEC-016 | Duplicates and races are *ambient*, not adversarial — retries happen on ordinary networks; R-16's conservative posture *requires* the atomic settlement to pre-exist |
| A5 | Turn pipeline integrity: exclusive resolution claim + turn-state ledger with phased checkpoints + phase-grain dedup + deterministic boundary | SEC-018, SEC-019, SEC-020, SEC-021 | SYS-016's pipeline is the whole game's mutation engine (§6.1); a duplicate or partial resolution *is* a global economy incident with no attacker at all (TH-009/010) |
| A6 | No-negative/no-overflow server-side invariants | SEC-025 | One negative balance at resolution is systemic (scale argument; §6.1) |
| A7 | Per-action-class quotas with the scheduler's quota reserved | SEC-029 | The free tier's budget is a *functional* attack surface (TH-012); without class quotas, one abusive client can freeze the day's economy |
| A8 | Minimum audit rows for money/pipeline touching (the ledger's spine, phased) — mutation rows ride mutation transactions; sampling policy per §15.2 | SEC-031's *spine* rows (a subset of SEC-031, which is a stage-B requirement in full) | Reversals/reconciliations/disclosures (§14.4) are *evidence-driven*; without rows, compromise review (§4.6) and dispute resolution (§12) degrade to memory |
| A9 | The honest-failure contract | fail-with-reason (§5.2) | DP-004's whole posture lives here; enforcement without reasons becomes noise the community can't calibrate (and appeals become accusations) |

**Stage-A count, stated exactly:** 12 full requirements (SEC-010/011/012/013/014/016/018/019/020/021/025/029) **plus** the money/pipeline spine rows of SEC-031 (A8). SEC-031 is not moved from stage B: its full §13.2 category coverage, privileged-read logging, and retention discipline are stage-B work (B5). The spine rows are required at A because the §14.4 reconciliation and §4.6 compromise review have no other evidence source. This resolves DEF-005: the subset is a *partial implementation of a stage-B requirement*, not a 13th stage-A requirement, and the stage counts remain 12 / 11 / 9 = 32.

**Why nothing else is in stage A:** every other control in §16 has an *economic or people-scaled* dependence (a population, an adversary class, a tool surface) that a first-playable build doesn't yet exhibit; where the deferring is *eventually unsafe* it sits in stage B by population/scope, not by budget.

### 17.2 Stage B — required before public launch

| # | Work item | Requirements | Why at this stage |
|---|---|---|---|
| B1 | Account security stack's full depth — verified identity (per OSQ-003), memory-hard password handling, step-up for sensitive actions, session lifecycle discipline, login/recovery rate limits, sensitive-change notifications, the compromise runbook (rehearsed) | SEC-001…005, 007/008 | The moment real players, e-mail anchors, and *economy-held value* co-exist, account-level compromise becomes real damage (TH-001/002/014's classes); rehearsal (ST-009-style) is the proof-of-competence |
| B2 | Abuse-control suite under test conditions — the fresh-account window + per-pair velocity caps + asymmetric outgoing caps, *with* their detection tuned by evidence (ST-016's funneling test passing as "surfaced for review") | SEC-023 (SEC-024's retention schedules remain stage C) | At population scale, multi-accounting becomes the genre-verified top abuse; R-13's caps pre-exist *at design*. This stage is their *tuned enforcement*, not new mechanics |
| B3 | Moderation machinery at launch scope — the sanctions ladder documented/audited, review-scope rules, logged acts | SEC-026 (SEC-027/028's tooling is stage C per §17.3) | PXE-011's moderation-capacity plan is a launch commitment; without logged acts, ladder discipline can't be audited (the single-operator caveat is an OSQ-005 decision, not an excuse) |
| B4 | Backups + restore discipline + a restore drill (ST-009) recorded | SEC-030 | §14.2: a public launch without a rehearsed restore is exactly TH-023's "restore mishandling" pre-condition (or, run with *no restore ability*, a *disclosed* Sev-1 risk that OSQ-007 must own) |
| B5 | Audit spine completed for every §13.2 category (the stage-A rows were spine-critical; stage B fills the rest) | SEC-031 | §13's categories exist in the design's *whole* shape: without the full set the evidence spine is a selective system, which is its own trust failure (SEC-031's "evidence is complete" requirement) |
| B6 | The minimal monitoring rail, live at ops cadence — budget gauges reading the event rows stage A already writes | SEC-031 (the gauges read only stage-B spine rows; SEC-033's alert-fire + drill formalization is stage C) | Silently degraded ops at a public launch is precisely TH-012's blindspot; budget gauges cost almost nothing and can save the day's economy |

### 17.3 Stage C — later hardening

| # | Work item | Requirements | Deferral rationale |
|---|---|---|---|
| C1 | Ops-grade identity separation, step-up on ops, scoped privileged reads | SEC-006 (with OSQ-012) | A single-operator project's *realistic* first posture is "the owner is an accountable, logged, disclosed operator" (TH-019's compensating control is disclosure); the *separation* work pays when a second operator exists |
| C2 | Server-defined turn-stamping *attribution*, ledger discipline as a "provable already-applied" layer, delay-disclosure automation | SEC-015, SEC-017, SEC-022 | Stage A's checkpoints already make these *requirements findable*; automation discloses at a polish-level, not integrity-essential |
| C3 | Abuse-evidence retention policy (data retention schedules for cases) | SEC-024 | Needs *cases at volume* to tune honestly; §11.2's tables suffice for first-playable posture |
| C4 | Two-person rule hardened for levels 4–5 + formal moderation tooling | SEC-027, SEC-028 | Follows staffing (OSQ-005) — two-operator reality first, tooling second |
| C5 | Full data-inventory discipline + monitoring polish | SEC-032, SEC-033 (alert-fire + drill cadence) | Legal-jurisdiction work (OSQ-010) and scale tuning belong with launch-jurisdiction knowledge |
| C6 | Advanced analytics & reviews-of-edges | §17's later-hardening families (red-team cadence, data-subject tooling, drill-at-scale) | Their own §1.4's stage-C description; no first-release risk if absent |

### 17.4 Dependency notes stage-level

- ST-017 (market-manipulation tests) is **market-stage-contingent** and *does not gate any stage-A/B item* — no listed market exists to test.
- ST-020 is **war-stage-dependent** (TH-022's design dependency): no war-stage test runs before the war stage ships rules.
- SEC-023's *tuning* needs population data (OSQ-001's policy context) — the *mechanism* is stage-B-bound; the *calibrated caps* are owner-feedback items.
- §17's stages assume exactly stage-1's design inputs; no war stage, no market stage constraints changed.

---

## 18. Failure scenarios and abuse walkthroughs

Format per walkthrough: **W-18-X** — the walkthrough's *precondition → action → expected safe behavior → prevention control → detection/evidence → recovery + communication → acceptance test → relevant requirements*. Every walkthrough is a **design/test-level artifact** (the prompt's own scope; no attack instructions, no live-system claims).

### W-18-A — duplicate trade request
1. **Precondition:** normal session; open balance; a flaky network.
2. **Action:** the client retries the same "offer 100 cash ↔ receive MAT-03" request after a lost response; the server sees two submissions with one idempotency key.
3. **Expected safe behavior:** both requests return the first committed outcome; the value moves *exactly once*; the second request does not double-settle.
4. **Prevention:** SEC-014 (idempotency keys), SEC-016 (single-spend atomicity), R-19's atomic pair.
5. **Detection/evidence:** idempotency-key collision row (SEC-031); per-key duplicate counter on the dashboard.
6. **Recovery/communication:** nothing to recover; the player sees coalesced truth ("this trade resolved as …"), disclosed per DP-004 if the client previously showed the wrong state.
7. **Acceptance test:** ST-005.
8. **Requirements:** SEC-014, SEC-016, SEC-031.

### W-18-B — competing requests spending one balance
1. **Precondition:** balance 100; two tabs in flight, each requesting a 100-spend.
2. **Action:** both submits arrive inside one resolution window.
3. **Expected:** first-committed wins at the server; the other receives "insufficient balance" *with reason*, not a partial or negative state. No pennies, no rollback-the-winner.
4. **Prevention:** SEC-016 (single-spend atomicity), R-19, prompt 7's two-checkpoint affordability.
5. **Detection:** both request rows logged; loser's reason cached to the honest-failure contract.
6. **Recovery:** none needed — by design.
7. **Acceptance test:** ST-004.
8. **Requirements:** SEC-016, SEC-010.

### W-18-C — retry occurring after a turn boundary
1. **Precondition:** queued action submitted at T's last instants; response lost; retry arrives after T resolved.
2. **Action:** the client re-fires the same keyed submit for T.
3. **Expected:** the retry returns the *actual* outcome (the action applied at T per the boundary rule, or queued at T+1 per the published class) — *never* a second application; the reason string explains the stamping.
4. **Prevention:** SEC-014 (key), SEC-015 (server stamps), Prompt 7 §14's resolve-at-boundary contract.
5. **Detection:** stale-turn retry counter.
6. **Recovery/communication:** none; the honest reply is the remedy (and a DP-004-disclosed state).
7. **Acceptance test:** ST-010.
8. **Requirements:** SEC-014, SEC-015, SEC-020.

### W-18-D — scheduler processes a turn twice
1. **Precondition:** two resolver workers (scaled-out ops), a retry-without-check, or a misconfigured cron.
2. **Action:** both attempt to claim turn T; both see "claimed by X" or "done."
3. **Expected:** exactly one performs resolution; the second exits no-op; the ledger rows for T exist exactly once.
4. **Prevention:** SEC-019 (single window), SEC-020 (checkpointed phases), SEC-021 (phase-grain dedup).
5. **Detection:** duplicate-claim refusals logged (the *alert* is the sign of a misconfigured setup, worth ops attention); SEC-033's stall alert for the pathological case.
6. **Recovery:** none needed if the claim discipline held; if *not*, W-18-L's restore path applies.
7. **Acceptance test:** ST-007.
8. **Requirements:** SEC-018–021, SEC-031, SEC-033.

### W-18-E — client-submitted treasury manipulation
1. **Precondition:** a modified client (or crafted request) submits "pay 1" where the UI said "pay 100"; another submits a quantity of MAT-03 ×300 that does not exist.
2. **Action:** the modified requests hit the trade/dev endpoints.
3. **Expected:** the server recomputes from *its* truth; prices, quantities, and eligibility as *requested* are rejected with reasons ("insufficient balance", "quantity out of range"); no state change.
4. **Prevention:** SEC-010 (recompute), SEC-011 (validation list), SEC-013 (bounds), SEC-025 (no-negative/overflow invariants).
5. **Detection:** malformed-parameter counters (§13; throttled per SEC-029 after repeat — never auto-banned on first sight).
6. **Recovery:** none; a rejected request costs the attacker nothing but their own attempts.
7. **Acceptance test:** ST-001/002.
8. **Requirements:** SEC-010, SEC-011, SEC-013, SEC-025, SEC-029.

### W-18-F — coordinated group attempting unfair transfers
1. **Precondition:** N accounts (some fresh), trades shaped so one-way value flows to a "main" while reciprocity is faked with circulating small-pair noise.
2. **Action:** the group exercises R-13's vector; the transfer-graph reviewer's job.
3. **Expected:** the *behavior itself* is reviewed, not auto-chastised: caps (SEC-023) restrict *outcomes* (value cannot physically over-move within the caps); the graph shape is *surfaced for review*; the response may be a ladder action (§12.3) on the *pattern's* evidence, not on volume alone.
4. **Prevention:** SEC-023 (window + caps + asymmetry), R-13/R-16's conservative posture, OSQ-001's policy context.
5. **Detection:** trade-graph anomaly (per-pair asymmetry, circularity, one-way flow outlier) — the queue-item class (§13.3).
6. **Recovery/communication:** review-then-act; a *level-2+* sanction only per §12.3's evidence standard; hidden recidivism handled as a conduct pattern (TH-020's class).
7. **Acceptance test:** ST-016 (the *detection* passes as "surfaced for review"; nothing auto-punishes).
8. **Requirements:** SEC-023, SEC-026, SEC-031.

### W-18-G — a legitimate household incorrectly flagged as alternate accounts
1. **Precondition:** two family members, one shared router, similar play times, mutual trades.
2. **Action:** both play normally; the graph flags a "suspicious one-directional flow" (a false positive in shape terms).
3. **Expected:** a review item, *not* a sanction. The reviewer reads *the full context*: both are real, active, reciprocal gamers; there's no session-composition or e-mail-reuse evidence; the review is closed with a reason; the flag is documented on their record for future *weight*, not *action*.
4. **Prevention:** §8.4's review-gated detection posture; SEC-026/028's process.
5. **Detection/evidence:** the review item itself + its closure reason (retained per SEC-024's posture).
6. **Recovery/communication:** the players are *informed* at the end of the review (an honest "we reviewed this — everything looks legitimate" beats a silent unexplained flag); appeals stay open if they want clarity (DP-004).
7. **Acceptance test:** ST-016's *false-positive leg* (the test that the graph does *not* produce an enforcement-eligible signal from co-residence alone).
8. **Requirements:** SEC-023, SEC-026, SEC-028, SEC-024.

### W-18-H — account takeover with in-game activity already landed
1. **Precondition:** a password-reuse victim's session token stolen; the intruder moves assets, allies out, changes orders inside one turn window before logout is forced.
2. **Action:** the legitimate owner reports; ops investigate.
3. **Expected:** containment *first* (revoke sessions, force reset — SEC-003/008); the compromise-window's tray of acts is *evidence-reviewed* (SEC-031's rows); reversal of value only where the evidence is unambiguous (R-16); notification (SEC-007); disclosed per DP-004.
4. **Prevention:** SEC-002/003/005's stack (the *entry* hardening); SEC-031's evidence spine (the *aftermath* review).
5. **Detection/evidence:** the owner's report; behavior anomaly (§13); the rows.
6. **Recovery/communication:** §4.6's runbook; where value was *not* recoverable, the honest communication says so (no false promises); §14.6's compensation rules apply where server-side failure was absent.
7. **Acceptance test:** ST-013/014's rehearsal; the drill covers a mocked compromise flow end-to-end.
8. **Requirements:** SEC-002, SEC-003, SEC-005, SEC-007, SEC-008, SEC-031.

### W-18-I — unauthorized alliance action
1. **Precondition:** a member whose account is compromised (or an over-escalated ally) attempts a pool draw or an unauthorized ejection.
2. **Action:** the alliance-verb request hits the server with the actor's role claimed as "treasurer."
3. **Expected:** the authority check *fails with a reason* ("insufficient role authority for this verb"); nothing changes; the attempt is logged; if *role *evidence* suggests compromise, §4.6's path extends to the *alliance* posture.
4. **Prevention:** SEC-012 (per-verb authority table), role gates, R-08's pool audit posture.
5. **Detection:** denied-authority cluster alerts; alliance-membership events.
6. **Recovery/communication:** affected members' rolls reversed where an unauthorized state change *did* occur (per the evidence standard; §12's lanes); the *alliance's* members notified (SEC-007's group-notice posture).
7. **Acceptance test:** ST-006 (authority-family spot-swaps).
8. **Requirements:** SEC-012, SEC-031; R-08 posture.

### W-18-J — excessive automated requests against the game
1. **Precondition:** a script floods action endpoints and read endpoints (R-18's vector).
2. **Action:** a flood of requests hammer quotas.
3. **Expected:** per-class quotas throttle the client (honest "temporarily capped" reasons); the *scheduler's* quota class is untouched (SEC-029's reservation); nothing about the *already-validated* queue is degraded to fit.
4. **Prevention:** SEC-029 (quotas + reservation), §15's budget posture.
5. **Detection:** rate-limit trip counters; creation/read-pattern anomalies.
6. **Recovery/communication:** the throttled client sees its own reason; other players see *nothing* changed; if a genuine *quota risk* event occurred, SEC-033's alert fires and ops are noticed.
7. **Acceptance test:** ST-011 (flood test: throttling holds; resolution unaffected).
8. **Requirements:** SEC-029, SEC-031, SEC-033.

### W-18-K — moderator misuses powers (a privileged user settling a personal score)
1. **Precondition:** a moderator with moderation scope has a personal conflict with a player.
2. **Action:** the moderator acts on a case involving that player beyond the evidence standard.
3. **Expected:** every act logged with reason (SEC-031); anomaly review by *another* reviewer (where staffing exists); the acting identity is accountable in the log; the ladder's *own* conflict-of-interest rule (§12.5) recuses the mod.
4. **Prevention:** SEC-026/027's scoping and logging; the recusal rule; the two-person rule for the most destructive tiers where staffing exists.
5. **Detection/evidence:** the logged acts' anomaly review (patterns that jump from the evidence standard).
6. **Recovery/communication:** the overturned case is re-run by the senior/owner; the *evidence-based* correction is disclosed per DP-004 (a trust hit surfaced honestly, not buried).
7. **Acceptance test:** ST-019 (a managed drill: the log anatomy of a harmful-act recording and its re-review path).
8. **Requirements:** SEC-026, SEC-027, SEC-031.

### W-18-L — restoration after partial turn processing
1. **Precondition:** a resolver crash at phase 4 of 9; recovery proceeds; the resume path *cannot safely resume* (a provable phase inconsistency in state where the ledger and the checkpoints disagree after a wider ops error).
2. **Action:** the fallback restore path is executed: restore to the *last fully committed* turn, named, with snapshot id; then forward-only replay of the lost portion, verified.
3. **Expected:** the restore is *pre-verified procedure*; the target turn named (SEC-030); the anomalies-comparison tool covers the checker set; the "affected player actions annulled" list is composed from rows; the announcement is simultaneously a disclosure (DP-004's digest discipline); affected player-visible history shows a *correction event*, not silent rewriting (§14.4's append-only visible history).
4. **Prevention:** SEC-020 (phase checkpoints — the *primary* path), SEC-021 (dedup), SEC-030 (restore discipline + drill), SEC-031's rows.
5. **Detection/evidence:** the abort's event rows (TH-010's detection); the restore drill's guidance (ST-009).
6. **Recovery/communication:** §14.4's reconciliation rules; §14.6's compensation posture where damage was established; the *visible* correction event (never silence).
7. **Acceptance test:** ST-009 (the drill), plus ST-008's *must-not-double* leg.
8. **Requirements:** SEC-020, SEC-021, SEC-030, SEC-031, SEC-022.

### W-18-M — a privacy trap: data collected "just in case"
1. **Precondition:** an ops proposal ("let's keep IPs for a year, it'll help with abuse").
2. **Action/expected:** the proposal *fails* the inventory's minimization rule (SEC-032): a retention posture change requires recorded justification + minimization review; the *default* is the 30-day-class posture; log-form personal data beyond §11.2's categories isn't operated. The prompt's **"avoid collecting personal data simply because it might be useful someday"** is literally this section's rule.
3. **Prevention:** SEC-032's inventory + §11.3's rules.
4. **Detection:** the retention cadence itself (§11.2's data-ops review); the ops dashboard's data-inventory audit.
5. **Recovery/communication:** if it ever *did* land (a stricter trap), §14.6's data-correction path downscopes + discloses.
6. **Acceptance test:** ST-012 (privacy/inventory review drill at the doc level).
7. **Requirements:** SEC-032, SEC-031, SEC-024.

### W-18-N — a false-report campaign against an innocent player
1. **Precondition:** a group files repeated cross-account reports against a player.
2. **Action:** the intake receives a cluster; the reviewer sees *sources*.
3. **Expected:** the *repeat-cluster* flag (SEC-028) deprioritizes the queue item *and* opens a review of the *group's* pattern; the review of the *target* uses its own evidence standard; zero action lands on the target unless the *ledger* supports it.
4. **Prevention:** SEC-028 (intake design), SEC-026 (review proportion), R-16's conservative posture.
5. **Detection:** cross-account report-cluster counter; reviewer-visible source list.
6. **Recovery/communication:** the target is *informed* that the cluster was reviewed and its reports not acted on (the target's right to know there *was* attention without *harm*); the group faces conduct review on evidence, not reaction.
7. **Acceptance test:** ST-015 (moderation process review).
8. **Requirements:** SEC-028, SEC-026, SEC-031.

### W-18-O — moderator abuse following a compromised mod account
1. **Precondition:** the moderator's login is phished; the attacker holds moderation scope.
2. **Action:** the attacker issues ladder actions against rival accounts; deletes evidence pointers where the tooling allows.
3. **Expected:** *every act is logged with identity and reason* (SEC-031; "missing-evidence censoring" itself raises a flag — §13's audit event that can't be silently removed); the two-person rule (where it exists) never lets one identity complete the most destructive tiers; the phishing *entry point* is remediated (session revocation, SEC-003), and the *acts* are reversed evidence-first (§12's lanes); the affected players are notified and disclosed to.
4. **Prevention:** SEC-006 (ops/mod identity separation), SEC-027 (two-person/stepping), SEC-031 (the log).
5. **Detection/evidence:** the act log's anomaly review; missing-file alert flags.
6. **Recovery/communication:** §14's incident protocol (Sev-3); disclosure per DP-004.
7. **Acceptance test:** ST-014 (privileged-account compromise drill).
8. **Requirements:** SEC-003, SEC-006, SEC-026, SEC-027, SEC-031.

### W-18-P — automated registration storms (TH-013's creation face)
1. **Precondition:** a bot script attempts mass account creation.
2. **Action:** the creation endpoint is hammered.
3. **Expected:** creation rate caps (SEC-029/005 family) throttle; *unique-identity* checks (SEC-001) refuse duplicates; e-mail verification's *status* (per OSQ-003's cost decision) gates anything e-mail-dependent; no *first-sight* ban — throttling + counters; where OSQ-002/003 escalate to verification, the same thresholds carry.
4. **Prevention:** SEC-029, SEC-001, SEC-005; the account-creation design's own throttles.
5. **Detection:** creation-burst counters; per-source creation patterns.
6. **Recovery/communication:** none (throttling is the whole response); if the *provider's* budget is endangered, the §15 gauges alert.
7. **Acceptance test:** ST-018 (automation throttle).
8. **Requirements:** SEC-001, SEC-005, SEC-029, OSQ-002/003 posture.

### W-18-Q — insider/overprivileged operator temptation
1. **Precondition:** the single-operator reality: an operator with full data access considers reading a rival player's economic state or quietly "helping" their own nation.
2. **Action/expected:** *privileged reads are themselves events* (SEC-031's rule) — the log is the mitigator; *the community sees the playbook* (TH-019's disclosure-first posture; OSQ-012's governance call); where a second operator exists, §12.5's accountability carries. The *conduct* case (§12.1/§12.3's own rules apply to the owner first — "operators follow rules too," DP-004's posture).
3. **Prevention:** SEC-031's privileged-read rule; SEC-006's separation; DP-004's disclosure-first playbook; OSQ-012's structure question.
4. **Detection:** privileged-read pattern review (a designed audit item).
5. **Recovery/communication:** §14's Sev-1 if real; a severity-1 incident is *serious* precisely because trust is the product.
6. **Acceptance test:** ST-019 (the drill).
7. **Requirements:** SEC-031, SEC-006, SEC-027.

### W-18-R — a restoration that reintroduces already-processed actions (TH-023's face)
1. **Precondition:** a restore pulled a snapshot *before* trade settlement; settled trades reappear as live offers.
2. **Action:** an operator restores from an older snapshot without the discipline.
3. **Expected:** *the procedure itself prevents this:* a restore names its snapshot + target turn up front; the reconciliation tool *must* find the ancestor-differences provable from rows (settled trade ids live in the ledger); the *stale-restore alert* fires on a ledger-vs-checkpoint mismatch; the affected players' actions are **annulled and notified**, not silently overwritten (§14.4's rules), with §14.6 compensation where damage was established.
4. **Prevention:** SEC-030 (the procedure + verification + the drill), SEC-031 (rows for reconstruction), SEC-022's disclosure.
5. **Detection/evidence:** the pre/post comparison tool; the alert.
6. **Recovery/communication:** the §14.6 path; §12.1's technical-lane framing (an ops incident, not a conduct case).
7. **Acceptance test:** ST-009 (the drill).
8. **Requirements:** SEC-030, SEC-031, SEC-022, SEC-033's stall alert (if applicable).

---

## 19. Security testing and validation plan

### 19.1 Status discipline

Every test below is **designed, not implemented and *not executed*.** No test run exists; the acceptance criteria are *plans* the implementation stage verifies. The `TP` column says Designed for all rows — no exceptions without a recorded execution record (the game does not exist to test against; this is the prompt's own rule).

### 19.2 The test register (ST-001…ST-020)

| ST | What it tests | Requirement(s) exercised | Preconditions | Test action | Expected result | Evidence to collect | Pass criteria | Stage-applicability | TP |
|---|---|---|---|---|---|---|---|---|---|
| ST-001 | Client-claimed quantity substitution | SEC-010, SEC-011 | Valid session | Craft a valid request with the *quantity changed* (a substituted value) | Rejected with an honest reason; no state change; nothing silent | Request row + validation-reject row | The rejection matches SEC-011's checklist for that endpoint | All stages | Designed |
| ST-002 | Type/bounds matrix | SEC-013, SEC-025 | Valid session | Submit malformed types, negative quantities, overflow-magnitude quantities, empty strings | Every case shape-rejected pre-logic; invariants hold | Rejection rows | No case passes; invariant violations impossible for every write family | All stages | Designed |
| ST-003 | Authorization spot-swap (single family) | SEC-012 | Two accounts, one endpoint | Replace the target nation/object id in the request with a second account's id | Rejected with honest reason; the *reason* matches the authority table; both sides' state unchanged | Authorization-fail rows | Every sampled family rejects correctly | All stages | Designed |
| ST-004 | Competing requests | SEC-016 | One balance, two valid 100-spend requests | Send both inside one window | Exactly one commits; the other receives an honest failure; no partial state | Both request rows; commit rows | One-winner resolution; the loser's reason matches the published rule | All stages | Designed |
| ST-005 | Duplicate request coalescing | SEC-014 | One keyed request, network retry | Send a request; retry it with the same key | The second returns the first's committed outcome; one settlement row | Both request rows + one settlement row | Coalescing is total (no second settlement) | All stages | Designed |
| ST-006 | IDOR-family sweep (spot-swaps across all action families) | SEC-012 | Two accounts (incl. alliance-member pairs) | For *each* mutated action family, attempt a cross-target swap | Every cross-target action rejects with the authority reason | Sweep matrix rows + reject rows | 100% of sampled families reject; zero silent acceptances | All stages | Designed |
| ST-007 | Duplicate scheduler run | SEC-019, SEC-020 | A rigged test resolver | Claim turn T; a second worker claims T | Second claim refused (no-op); player-visible state changed exactly once | Claim rows, refusal rows, phase markers | Exactly one resolution; second no-op | FP | Designed |
| ST-008 | Partial-failure resume | SEC-020, SEC-021 | An abort mid-phase | Kill the resolver mid-phase; resume | Only the uncommitted phases run; no phase's effect applied twice | Phase markers; resume rows | Forward-only resume; zero double-applies | FP | Designed |
| ST-009 | Restore drill + resume-dedup leg | SEC-030, SEC-021 | A prepared snapshot older than settled actions | Perform SEC-030's restore procedure; verify reconciliation | The restore completes; stale-restore anomaly tool passes; annulled-action list composed from rows; disclosure composed | The drill's artifact set (ST-009's report) | Within the RTO posture; zero undetected stale-settled items | PL | Designed |
| ST-010 | Stale-turn id behavior | SEC-015 | A queued action + a turned boundary | Submit with the wrong-turn expectation; observe the reason | The server's own stamp governs; the reason explains the class honestly | Request row + reason string | Matches §6.3's answers exactly; no silent re-class | FP | Designed |
| ST-011 | Quota-exhaustion behavior | SEC-029, SEC-033 | A flooded client | Overdrive a class until the cap trips; overdrive the *write* class hard | Client throttled with honest reasons; the scheduler's quota class untouched; the gauges alert on risk | Throttle rows; gauge readings | The reservation holds; alerts fired; no silent degradation | FP | Designed |
| ST-012 | Privacy + inventory review (the data-ops drill) | SEC-032, SEC-031, SEC-024 | The *document/product* surfaces | Audit the *operated surfaces* against §11.2's inventory; sample log rows for personal-data content | Zero undocumented personal-data fields; log rows carry no sensitive values | The audit's field-by-field matrix | 100% documented; zero out-of-inventory content | PL | Designed |
| ST-013 | Credential stuffing + recovery abuse | SEC-005, SEC-004, SEC-002 | A test account + a synthetic "breach list" pattern | Drive throttles to trip; drive the recovery endpoint's caps | Steady escalation (delays → throttle → lockout); recovery is throttled *separately*; failure reasons never enumerate | Attempt rows, throttle rows, lockout rows | Caps behave as proposed; enumeration resistance holds | PL | Designed |
| ST-014 | Session hijack + privileged compromise drill | SEC-003, SEC-006, SEC-027 | A "stolen" session token; an ops "phished" credential (a drill capture, not a live theft) | Use the stolen session; use the ops credential | Explicit expiry/revocation holds; privileged verbs require step-up; the drill's acts are fully logged | Session rows, privileged-act rows | The compromise window contains damage to within one turn window; the log's identity/review path holds | PL | Designed |
| ST-015 | Conduct moderation + report-abuse review | SEC-026, SEC-028 | A case-file set (including a false-report cluster) | Run the *process*, not a judgment: intake → review → action → appeal | Acts logged with reasons; clusters deprioritized; appeals open; the overturned case re-reviews | Case rows, act rows, appeal rows | The ladder's steps hold; the cluster *does not* sanction the target silently | PL | Designed |
| ST-016 | Funneling detection (the multi-account test) | SEC-023 | A synthetic N-account trade graph (normal play *and* funneling shapes); *also* the W-18-G household leg | Feed both shapes; observe the graph reviewer's output | Abuse shapes surface as review items; the household leg does *not* produce an enforcement-eligible signal | Review queue items with reason annotations | Detection surfaces for review; zero auto-sanctions; zero household false-positives | PL | Designed |
| ST-017 | Market-manipulation pattern review | (market-stage contingent) | A listed market (only after G-4 opens one) | Feed synthetic wash-trade pairs during a listing market's test phase | Self-pair aggregates are excluded from day-window stats; anomalies surface for review | Aggregates + review rows | Self-pair exclusion holds; reviews open (never auto-sanction) | Market stage only | Designed |
| ST-018 | Scraping/bot throttling + automation-fairness sampling | SEC-029, SEC-031 | A read-heavy synthetic client | Overdrive reads; observe caps and the boundary-window sampling posture | Read caps throttle honestly; boundary-window pattern surfaced for *review* (not auto-ban) | Read-cap rows; sampling rows | Reads cap; no policy-violating client "wins" by sheer repetition | PL | Designed |
| ST-019 | Moderator-power abuse review drill | SEC-026, SEC-027, SEC-031 | A case set + a planted harmful act | Issue a logged act beyond evidence scope; observe the anomaly review path | The act is in the log; the anomaly review opens it; the correction follows §12's lanes | Activity log + review rows | Acts are logged; the abusive act is *detectable* in review; accountability path holds | PL | Designed |
| ST-020 | Campaign-order ordering (war-stage dependent) | SEC-014, SEC-018, SEC-019–021 | A campaign-order test rig (only after the war stage ships rules) | Race/dupe campaign orders at a boundary | Same rails' guarantees (one winner; honest reasons; no double-apply) | Order rows, resolution rows | Matches the §10.2 carry-over contract exactly | War stage only | Designed |

### 19.3 Coverage note (traceability)

Every threat in §2.3's register maps to at least one ST (the threats' "Residual risk & validation (ST)" column carried its assignment); every test above names its requirement(s). The **unexecuted** status is the honest state: no game exists to run them against. §25's QA record documents this test plan as *designed-stage artifacts*, never as passed work.

---

## 20. Trade-offs, options, and owner decisions (OSQ-001…OSQ-012)

### 20.1 The register

| OSQ | Question | Options | Consequences (security / privacy / experience / cost) | Recommendation (with rationale) | Evidence needed to decide | Status |
|---|---|---|---|---|---|---|
| OSQ-001 | What is the multi-account policy? (prohibit / restrict-with-conditions / permit-with-conditions) | A/B/C per §8.1 | **SEC:** A relies on behavioral detection; B reduces detection dependency; C accepts the genre's hardest honesty problem. **Privacy:** all options *reduce* (not eliminate) the behavioral-evidence need if the policy is explicit. **XP:** A may feel hostile to focused community roles; C invites abuse. **Cost:** B is the cheapest to administer honestly. | **B — restrict at launch** (one account per person, named supervisory conditions later only where evidence justifies: §8.1) | Actual launch-community norms (Prompt 4's audience + a pre-launch survey); genre evidence already collected (Prompts 1/3) | Open — owner decision |
| OSQ-002 | What step-up verification level is required for sensitive actions? | none / e-mail challenge only / TOTP for the highest tier | SEC: TOTP > e-mail challenge > none against TH-001. XP: friction exactly where scoped. Cost: TOTP is ~free; e-mail challenge spends send budget | **TOTP-class for ops (mandatory) + e-mail challenge for the player tier (optional add-on)**; sensitive-action scoping per §4.5 | Player-experience testing (friction tolerance); e-mail budget sizing | Open |
| OSQ-003 | Is e-mail *verification* required at account creation? (the free-tier send-cost question) | verify-all / verify-later / no-verification (with OSQ-002's compensation) | SEC: unverified e-mail weakens SEC-004's anchor and admits bots cheaply. Privacy: no change. Cost: verification mail per signup; the free-tier budget is the decision's pivot | **Verify at creation *if* the free e-mail tier sustains sign-up traffic; otherwise a recorded defer with creation-throttle compensation** (TH-013's force) | A free e-mail provider's tier test against projected sign-up volumes | Open |
| OSQ-004 | Which automation is allowed (the automation policy's shape)? | honor-timing-contract-and-allow-anything vs. permitted-tool-list vs. prohibit-most | SEC: policy shapes what TH-013/025 become. Privacy: no change. XP: published rules beat cat-and-mouse; the O-10 family expects this artifact. Cost: enforcement tooling follows the choice | **Permitted-behavior policy at launch** (a published "what the client may do" list built with the community's own input; boundary-window *convenience advantage* restricted by default per §9's recommendation, subject to the community's preference) | Community preference evidence; observation of actual tooling at launch scale | Open |
| OSQ-005 | What is the moderation staffing/model? (single operator / community mods / a trust & safety role) | the three named | SEC: staffing determines SEC-027's two-person rule applicability; privacy: more mods = more evidence-scope surface (SEC-024's tuning); XP: response times and *calibration*; cost: the cheapest is what the project has | **Launch with single-operator + the documented compensations (§12.5); commit to adding a reviewer when population or incident load justifies it** | Population/incident-load growth observation | Open |
| OSQ-006 | How much history should be publicly visible (moderation outcomes, economy aggregates)? | full-public / outcome-public / minimal (as described by SDQ-004's own posture) | SEC: public outcomes aid evidence-based appeals; privacy: player-visible sanction records are personal-data exposure; XP: transparency builds trust; cost: zero direct | **Outcome-public where an appeal is decided (case outcomes announced in aggregates, names withheld per privacy posture); exact rules set with §11's categorization at launch** | Community norm evidence; §11's data-governance review | Open |
| OSQ-007 | What recovery guarantees (RPO/RTO + backup tier) will the owner pay for? | none-disclosed / daily-rolling / higher | SEC: TH-023's whole exposure depends on this. XP: "can I lose my nation to an ops error?" is a real-player question. Cost: the only tiered-cost item in this report's stage-B list | **Daily rolling + monthly anchor at launch** (the §14.2 posture); upgrade only with launch-scale evidence | A backup-storage cost quote at projected state size (the architecture stage's data) | Open |
| OSQ-008 | How much security monitoring can be operated within the budget? (the SEC-033 rail's *shape* at scale) | minimum counters / + alerting services / + external analytics | SEC: alerts catch silent failure (§15.3). Cost: the free tier sustains the minimum; more is budget. Privacy: no change | **The minimal rail at launch**; scale when population data shows thresholds | Ops-load observation | Open |
| OSQ-009 | What player data may be *used for abuse detection*? (the §8.3 boundary) | trade-graph only / + session/network metadata composition / + device posture (rejected by this report) | SEC: composition availability determines TH-003's *honesty ceiling*. Privacy: §11's minimization fights the widest option. XP: households/CGNAT fairness rides the choice (W-18-G) | **Trade-graph + short-retention session/network metadata composition** (the §8.3 recommendation); device fingerprinting rejected for this project | Community privacy-norm evidence; TH-003's detection-tuning data at population | Open |
| OSQ-010 | Privacy/legal jurisdiction review (which regimes apply; what data-protection work is required before launch?) | per launch-market | SEC/legal: the only *external-counsel* item in this report. Privacy: everything. Cost: counsel time | **Owner-held; do it before public launch**; no checklist in this report can substitute | Actual launch jurisdictions; counsel's review | Open |
| OSQ-011 | Which protections are *mandatory* before public launch? (approval of §17's stage-B list as given) | approve stage-B list as written / amend | SEC: defines the launch line. XP/cost/privacy: follow from the list | **Approve §17's stage-B as the launch line** (owner signature item; this report proposes it) | The owner's own reading of §17 | Open |
| OSQ-012 | What operator-access *structure* does the project adopt? (single accountable operator / separated roles / two-person infrastructure) | the three | SEC: TH-019's structural answer; XP/privacy: disclosure-first posture shapes trust; cost: structure is *staff* — the project's scarcest resource | **Single accountable operator + the disclosure-first playbook at launch; adopt separated roles/two-person structure when a second operator exists** | Hiring/onboarding plans (if any) | Open |

### 20.2 What §20 deliberately does *not* decide

Nothing above is owner-approved. The register's *status* column is the honest one: all twelve are **Open**. Where §20's rows cite *proposed starting postures* (RET the RPO/RTO rows, verification tiers), the *value* is a proposal owned by its OSQ; §24's register keeps them distinct from paid-for decisions, and DECISIONS.md is untouched (per the working rules' scope).

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
6. **Resolved 2026-10-23 (DEF-004/005/010):** §15.4's "16 requirements on stage A" was the last remnant of the earlier segmentation; it now reads **12** and matches §1.4/§16.2's priority column and §17.1's A1–A7 list. A8's audit-spine rows are stated as a **subset of SEC-031** (a stage-B requirement) rather than as a thirteenth stage-A requirement; §16.2's SEC-031 stage cell and §17.1's count note record the same fact. TH-011's mitigation now separates **Stage-A prevention** (SEC-018/020's enforced boundary rule plus A9's disclosure) from **SEC-015's Stage-C attribution refinement**, and states the accepted residual. This is a documentation correction only: no requirement's priority, stage, or scope changed.

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

**Range TH-001…TH-025 · 25 entries · status: proposed, not owner-approved.** Each row's full content lives in §2.1–§2.3 (the register above); this record confirms:

| ID | Short name | § | Priority |
|---|---|---|---|
| TH-001 | Credential stuffing / account takeover | §2.3 | Critical |
| TH-002 | Session hijack / token theft | §2.3 | Medium-High |
| TH-003 | Multi-account funneling / value transfer | §2.3 | Critical |
| TH-004 | Coordinated market manipulation / wash trading | §2.3 | Medium |
| TH-005 | Alt-as-sabotage (burn the alt) | §2.3 | Low-Med |
| TH-006 | Client-side value manipulation | §2.3 | Critical |
| TH-007 | Replayed / racing duplicate requests | §2.3 | High |
| TH-008 | Unauthorized action for another nation (IDOR/authorization miss) | §2.3 | High |
| TH-009 | Turn processed twice (duplicate scheduler run) | §2.3 | High→Critical band |
| TH-010 | Partial turn processing (half-done resolution) | §2.3 | High |
| TH-011 | Stale turn-id / boundary race actions | §2.3 | Medium |
| TH-012 | Quota/written-budget exhaustion + request flooding | §2.3 | Critical |
| TH-013 | Bot account farms / scraping / auth brute force | §2.3 | High |
| TH-014 | Credential guessing on one target | §2.3 | Medium |
| TH-015 | Conduct toxicity: harassment, impersonation, deceptive nation names | §2.3 | Medium |
| TH-016 | Report abuse / brigading / false reports | §2.3 | Low-Med |
| TH-017 | Moderator abuse of powers | §2.3 | Medium-High |
| TH-018 | Compromised privileged/operator account | §2.3 | High |
| TH-019 | Insider / excessive operator access | §2.3 | High |
| TH-020 | Sanction evasion via new accounts | §2.3 | Conditional (else TH-003's class) |
| TH-021 | Unauthorized/inappropriate alliance administration | §2.3 | Medium-High |
| TH-022 | Diplomacy/campaign timing & forgery attacks ( WAR-STAGE-DEPENDENT ) | §2.3 | High (projected) |
| TH-023 | Improper backup restoration (stale restore) | §2.3 | Medium-High |
| TH-024 | Privacy data exposure / inappropriate retention | §2.3 | Medium-High |
| TH-025 | Boundary sniping / unfair-advantage client automation | §2.3 | Low-Med |

### 24.3 Security-requirements register (master)

**Range SEC-001…SEC-033 · 32 defined entries (SEC-009 deliberately unassigned) · status: proposed, not owner-approved.** Full content in §16.1; §16.2 holds the stage assignments; this record confirms the ID-to-short-name map:
1. SEC-001 — Unique verified account identity
2. SEC-002 — Password handling + step-up
3. SEC-003 — Session issuance/rotation/revocation
4. SEC-004 — Rate-limited recovery
5. SEC-005 — Login attempt caps + honest lockout
6. SEC-007 — Sensitive-change notifications
7. SEC-008 — Compromise response runbook
8. SEC-010 — Server recomputes all valuable quantities
9. SEC-011 — Per-action validation list
10. SEC-012 — Per-resource authority model
11. SEC-013 — Input bounds + integer guards
12. SEC-014 — Idempotency keys per write action
13. SEC-016 — Single-spend atomicity + no-debt invariant
14. SEC-018 — Deterministic boundary resolution + published tiebreaks
15. SEC-019 — Single authoritative resolution window
16. SEC-020 — Turn state ledger + staged checkpoints
17. SEC-021 — Phase-grain dedup (no double-apply)
18. SEC-025 — Server-side no-negative/no-overflow invariants
19. SEC-029 — Per-action-class quotas (scheduler-reserving)
20. SEC-023 — Fresh-account restrictions + per-pair velocity caps (under test conditions)
21. SEC-026 — Sanctions ladder with logged acts
22. SEC-030 — Backups + restore discipline (verified procedure)
23. SEC-031 — Audit event ledger (the evidence spine)
24. SEC-006 — Admin/ops account separation
25. SEC-015 — Server-defined turn stamps
26. SEC-017 — Settlement/accounting ledger discipline
27. SEC-022 — Delay/missed-processing disclosure contract
28. SEC-024 — Abuse-evidence retention policy
29. SEC-027 — Elevated permission + two-person rule for the most destructive ops
30. SEC-028 — Report intake design
31. SEC-032 — Data inventory + minimization discipline
32. SEC-033 — Minimal monitoring rail

**SEC-009** is explicitly *left unassigned* (reserved for a possible account-encryption requirement if the owner opens that decision later — a hold, not a usage).

### 24.4 Security validation test register (master)

**Range ST-001…ST-020 · 20 entries · status: designed-not-implemented, none executed.** Full content in §19; this record confirms the ID-to-short-name map:
1. ST-001 — Client-claimed quantity substitution
2. ST-002 — Type/bounds matrix
3. ST-003 — Authorization spot-swap (single family)
4. ST-004 — Competing requests
5. ST-005 — Duplicate request coalescing
6. ST-006 — IDOR-family sweep (spot-swaps across all action families)
7. ST-007 — Duplicate scheduler run
8. ST-008 — Partial-failure resume
9. ST-009 — Restore drill + resume-dedup leg
10. ST-010 — Stale-turn id behavior
11. ST-011 — Quota-exhaustion behavior
12. ST-012 — Privacy + inventory review (the data-ops drill)
13. ST-013 — Credential stuffing + recovery abuse
14. ST-014 — Session hijack + privileged compromise drill
15. ST-015 — Conduct moderation + report-abuse review
16. ST-016 — Funneling detection (the multi-account test)
17. ST-017 — Market-manipulation pattern review
18. ST-018 — Scraping/bot throttling + automation-fairness sampling
19. ST-019 — Moderator-power abuse review drill
20. ST-020 — Campaign-order ordering (war-stage dependent)


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

**Four formal identifier registers** and their stated counts — TH-001…025 (25 threats), the SEC-001…033 range with SEC-009 deliberately reserved (32 defined requirements), ST-001…020 (20 tests), and OSQ-001…012 (12 open security questions) — match the actual unique-ID counts **in** this report's §2/§16/§19/§20 content, verified programmatically in this session's verification pass (§25).

The **fifth collection** — the 18 failure walkthroughs (W-18-A…R, §18) — is tracked separately and is **not a formal identifier register**: it is one §18 scenario collection whose 18 entries carry letter suffixes on a W-18- prefix at their own headings, with no numbered register table; it is counted here so the report's earlier "five registers" phrasing stays accurate as five tracked collections: §24 holds master registers for the four identifier families (§24.2–§24.5), while §18's walkthrough entries keep their own headings and are not re-numbered or re-enumerated in a §24 table.

Every **currently defined and active** ID cited anywhere in this report falls inside its registered range. The single out-range mention is §26.3's `SEC-034+`, which is not an existing requirement ID but **forward-numbering guidance** — a convention telling future stages to continue past the reserved SEC-009 by starting a new requirement block at SEC-034 rather than silently filling the gap. No requirement named SEC-034 exists.

---

## 25. Quality assurance record

*This section documents only what was actually checked.* No claim below was fabricated; failures and repairs are recorded honestly.

### 25.1 Reading completeness — the files actually read

All four continuity files read in full this session: [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md), [DECISIONS.md](../DECISIONS.md). All seven stage reports read (Prompt 7's v1.1 *as amended by the accepted Prompt-7 final micro-correction* being the economy report). D-004/D-005 confirmed still Provisional in [DECISIONS.md](../DECISIONS.md) (§22.1's rows 13–14). **Accuracy correction (2026-10-23):** an earlier draft of this bullet claimed the continuity-file status had been re-read *after* this report's edits; the Prompt 8 authoring session in fact updated only this report — the three continuity files still described Prompt 7 as the latest completed prompt. The discrepancy was found in the correction pass documented in §25.3's addendum, the updates were then actually applied, and the saved files were re-read and verified to agree. DECISIONS.md was re-inspected and left unchanged.

### 25.2 The file-corruption incident and the recovery (full honesty)

The **first saved write** of this report was corrupted on disk this session: sections §3 onward exist in the file as an interleaved corruption of the report's text with a repeated fragment (the report's §0–§2 survived; §3–§26's original text was unrecoverable from the damaged disk area). The intact §0–§2 (through the end of the threat register's rows and the actor-coverage checklist) was **recovered by a character-interleave-detection method** and **served as the constraint base for this rebuild**: every threat row, register structure, and forward reference in the surviving front matter was honored by the rebuilt sections (the rebuilt §3–§26 incorporate all surviving text verbatim above §2.4 plus rewritten §3–§26 content written this session against the surviving anchors). The QA record's own §25 text (this section) is part of the rebuild. **Reading the recovered §0–§2 to confirm its content still matches the register and §22.1's audit was part of the final sweep.**

### 25.3 Checks performed — with the exact outcome

Automated checks conducted with a Python sweep script against the *final assembled* report file (code in `docs/qa_backups/08_sweep.py` / `08_sweep2.py`; outputs in `docs/qa_backups/08_sweep_result.txt`):

| # | Check | Result | How |
|---|---|---|---|
| 1 | All required sections present (§0–§26; Section-1…Section-24 named in the map) | ✅ PASS | Heading inventory compared against the §0 mapping list |
| 2 | Register count vs. content | ✅ PASS | Unique TH-/SEC-/ST-/OSQ- IDs extracted programmatically; §24's stated counts match the extraction (25 TH / 32 SEC defined, 009 unassigned / 20 ST / 12 OSQ) |
| 3 | Threat→requirement traceability | ✅ PASS | Every TH- row names ≥1 protective SEC requirement; every SEC row names ≥1 threat; both directions verified programatically |
| 4 | Requirement→test traceability | ✅ PASS | Every SEC-### names its ST-### validation test; every ST-### names its SEC-IDs; extracted programmatically |
| 5 | Forward-reference resolution (all §-refs) | ✅ PASS | Every "§N" reference inside the file resolves to an existing heading; corrected 5 stale refs during assembly and re-ran the sweep |
| 6 | Local Markdown links | ✅ PASS | Relative links in §25.1/§26 (`../AI_CONTEXT.md` etc.) resolve against the actual project tree (`docs/` + stage files verified on disk); no dead-target link found |
| 7 | Inherited-ID resolution | ✅ PASS | Every cross-report ID (ECON/ECOQ/ECV/MAT/L/G/R-13…21/SDQ…/FO/PR/PXE/SIM/MO/F-/O-) checked to exist in its owning file via a prior session's verified ID map; one Prompt-6/non-economy paraphrase adjusted during the rebuild and re-verified |
| 8 | Decision-status integrity | ✅ PASS | DECISIONS.md untouched this task; D-004/D-005 still Provisional; no new decision rows |
| 9 | "Not owner-approved" wording | ✅ PASS | §16.1's status column, §24.2–24.5's headers, §0's preface; extracted & confirmed the phrase applies to all SEC/TH/ST/OSQ values |
| 10 | No-code check | ✅ PASS | No production code, config, schema, or technical architecture committed; the report contains *requirements and acceptance tests*, not implementation |
| 11 | Cross-report consistency | ✅ PASS | §22's table rows all verified against their source files (rows 1–15); §22.2's duplicate/contradiction entries recorded rather than silently repaired |
| 12 | Turn-cadence integrity | ✅ PASS | The file's cadence statements (the §0 scope line, §1.1's question, §14.1's framing, and assumption A-1 in §21.3) all describe the 2-hour UTC design; none modifies the boundary |
| 13 | Garble scan | ✅ PASS | A script searched for the local pattern hallmarks of the document-context fragments seen in earlier drafts (verbatim prefix tokens); all matches fixed before the final sweep; the final sweep finds zero |

**Failures found during the sweep (and fixed):** 2 heading-numbering slips among §4–§8 (one heading doubled a number), 3 traceability gaps (a TH- row citing a requirement that didn't exist by its target name — the target's renumbering missed in an intermediate draft), 5 stale §-refs after renumbering, and the 2-stage-assignment misalignments recorded in §22.2 item 1. All corrected and re-verified by re-running the whole sweep after edits.

**Correction-pass addendum (2026-10-23), verified by re-running the full sweep after these repairs:** the §24.2/§24.3/§24.4 register-“master” tables were found drifted from their authoritative registers and were regenerated programmatically, verbatim, from the §2.3 threat rows (names + overall-priority band + §2.3 placement), the §16.2 requirement rows (titles), and the §19.2 test rows (“what it tests”); the §0.3 doc-map's SEC-range cell was reconciled to "SEC-001…033 with SEC-009 reserved — 32 defined"; and the sweep result on the saved file afterwards was **all checks passed** (sections 0–26 continuous; subsection numbering continuous; TH-/SEC-/ST-/OSQ- ranges gap-free per §24.6's counts; all 18 W-18-A…R walkthroughs present; every internal §-reference resolves — the 74 cross-report `Prompt N §x.y` citations resolve in their owning files by design; zero stray-fragment or non-Latin-character artifacts). **Final cross-file validation (same day):** a dedicated read-only checker, `docs/qa_backups/validate_final.py`, was written and run over the saved three continuity files, [DECISIONS.md](../DECISIONS.md), and this report — it verifies the 2026-10-23 file headers, the present-and-consistent status language (Prompt 7 accepted after its micro-correction; Prompt 8 complete; Prompt 9 not started as *proposed*; Stage 1 not complete; eight-prompt recorded plan), §25's accuracy-marker passages, the ID registers (TH-001…025, SEC-001…033 with 009 reserved, ST-001…020, OSQ-001…012, W-18-A…R), all relative links, the six decision statuses in DECISIONS.md (D-001…003 Confirmed, D-004…006 Provisional; D-004/D-005 decision text byte-intact), and the absence of production game code. Result at the time: **ALL CHECKS PASSED**. DECISIONS.md itself was inspected and left unchanged — no entry was added, altered, or removed in either pass; the D-004/D-006 status cells and the verbatim D-004/D-005 decision text were checked during this run. **2026-10-23 correction pass 2 correction:** `validate_final.py` was a *point-in-time* Prompt 8 checker whose assertions include "Prompt 9 not started" and "no stage-1/09 file exists". Those expectations became false the moment Prompt 9 was authorized and executed; the checker therefore now reports four stale failures (`AI_CONTEXT: missing prompt-7 micro-correction`, `AI_CONTEXT: implies Prompt 9 executed`, `PROJECT_PROGRESS: missing not-started language`, `a Prompt 9 report file exists`). This is **obsolete test state, not a current project defect**. The script has been re-purposed as a current cross-file validator (its stale assertions replaced with the actual nine-prompt status; valid checks retained) and is no longer evidence that the 2026-10-23 Prompt 9 state passes or fails. The authoritative current checks are `docs/qa_backups/09_validate.py` plus `validate_final.py` re-run in its updated form; see §25.7.

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

This task wrote documentation only: the report and, in the 2026-10-23 correction pass, the three continuity files (AI_CONTEXT.md, AI_HANDOFF.md, PROJECT_PROGRESS.md). **QA scripts are present and declared:** the two Python sweep scripts used only to inspect and validate the report text — `docs/qa_backups/08_sweep.py` and `docs/qa_backups/08_sweep2.py` — plus the read-only cross-file validator written during the final validation (`docs/qa_backups/validate_final.py`), their sweep outputs and the report's recovery/stage working files under `docs/qa_backups/`. These are document-QA tooling, not game implementation. **No production game code, no game config, no database schema, and no finalized technical architecture were committed — production game implementation has not started**; the repository currently contains research documents, continuity records, and this document-QA tooling under `docs/`. An earlier draft of this bullet claimed no `.py` files existed — it was wrong (the two sweep scripts above) and is corrected here, with the QA-vs-production distinction stated explicitly.

**On the “broken crypto/container documentation” reference:** a prior audit note in an earlier draft of this section mentioned “broken crypto/container *documentation* was read but not edited.” Investigation in this pass could trace that phrase to **no project artifact**: the repository contains no crypto, container, secrets, or deployment documentation at all, and the phrase appears nowhere else in any project file. It was most plausibly language carried over from the external audit conversation about an archive's integrity, not a property of this project's files. The citation is therefore **removed as unsupported**; the only real document-integrity incident evidenced in this project remains §25.2's corrupt first save of this report, which was recovered and rebuilt the same session. If the owner later supplies the artifact that note referred to, it should be re-investigated from that evidence (recorded here so the removal itself is traceable).

### 25.7 Second correction pass (2026-10-23) — DEF-004/005/010

Triggered by the Prompt 9 audit, not by a new review of this report's design content. Changes made, all documentation-level:

| Item | Before | After | Verification |
|---|---|---|---|
| Stage-A count (§15.4) | "16 requirements on stage A" | "12 requirements" + the SEC-031 spine subset (A8) | Counted against §16.2's FP rows and §17.1's A1–A7; both give 12 |
| SEC-031 subset (§17.1 A8, §16.2) | A8 implied a stage-A requirement while SEC-031 was listed PL | A8 states "a subset of SEC-031 (a stage-B requirement)"; §16.2's stage cell says "PL (spine rows at A8; full coverage at B5)" | Stage tally 12 + 11 + 9 = 32; SEC-031 appears once |
| TH-011 residual (TH-011 row) | Named SEC-015 (Stage C) as the mitigation, leaving Stage-A prevention implicit | Stage-A prevention = SEC-018/020's enforced boundary rule + A9 disclosure; SEC-015 = attribution refinement; residual stated as an accepted transparency residual | TH-011 → SEC-015/018/020; ST-010 remains designed-only |
| Handoff (§26.9) | Instructed Prompt 9 to begin, awaiting authorization | Marks the instruction superseded; Prompt 9 executed; next actions = OD-01/02/03/06 + PV-01…PV-07/PV-15 | Cross-checked against the Prompt 9 report and continuity files |
| Legacy checker (§25.3) | Presented `validate_final.py` as passing | Records that it is a point-in-time checker whose four "Prompt 9 not started" assertions are now stale; it was updated in this pass to validate current state | Re-ran; see the script's current output |

**Not changed:** no threat likelihood/impact, no requirement priority beyond the SEC-031 stage-cell clarification, no test status, no owner question, no staging of any other requirement. All 20 ST tests remain designed-not-executed. **DECISIONS.md was NOT changed** in this pass (inspected only; D-004 and D-005 remain Provisional).

---

## 26. Handoff

### 26.1 What Prompt 8 produced

[08_security_privacy_fair_play_and_trust.md](08_security_privacy_fair_play_and_trust.md) — Sections 0–26 complete; 25 threats (TH-001…025); 32 defined security requirements (SEC-001…033, SEC-009 reserved); 20 validation tests (ST-001…020, all designed-only); 12 open security questions (OSQ-001…012); the stage-B/C/A roadmap (§17); the §26-stage-B owner decision line (OSQ-011); and a documented recovery of an earlier corrupt save (§25.2). The full report *does not* finalize an architecture, does not run/stage any test, does not record any owner decision.

### 26.2 Files read and changed this session

Read: all four continuity files; all seven stage reports (incl. Prompt 4 for the "Missing several turns" target check); DECISIONS.md (read-only, left unchanged). Changed in the Prompt 8 authoring session: **only** `docs/stage-1/08_security_privacy_fair_play_and_trust.md`. Changed in the first 2026-10-23 correction pass: this report (the §24 register-map reconciliation, the §25/§26 accuracy pass, and the §0.3 range-cell fix) **and** the three continuity files AI_CONTEXT.md, AI_HANDOFF.md, PROJECT_PROGRESS.md — listing this report's deliverable state, the correction-pass outcome, no production code, and Prompt 9 not started (true at that time). Changed in the **second 2026-10-23 correction pass**: §15.4's stage-A count, §17.1's A8/subset note, §16.2's SEC-031 stage cell, TH-011's prevention/residual wording, §22.2 item 6, this §25/§26 record, and the updated Prompt 9 handoff in §26.9. **DECISIONS.md was NOT changed in any pass.** All edits are Markdown text; no code or config.

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

### 26.9 What the next prompt should do (updated 2026-10-23 — this section previously awaited Prompt 9)

**Historical note:** when this report was written, Prompt 9 had not been authorized and this subsection instructed the next prompt to perform the synthesis. That handoff **has been superseded**: the owner authorized Prompt 9, it was executed on 2026-10-23, and its report is [09_integrated_design_synthesis_and_readiness_audit.md](09_integrated_design_synthesis_and_readiness_audit.md). The instructions above are therefore no longer a pending task. What a successor should do now:

1. **Reread** all four continuity files first, then the Prompt 9 report in full, then this report's registers and whichever earlier reports the task touches. Do not rely on summaries.
2. **Treat SEC/TH/ST/OSQ as inputs**, not approvals; the same applies to Prompt 9's REQ/OD/GATE families. D-003 still governs.
3. **Close the owner decisions Prompt 9 identified** (OD-01/02/03/06 first) and run the free-tier measurement spike (PV-01…PV-07, PV-15) before any implementation planning. Prompt 9 §15 is the deduplicated register; §20 is the gate state.
4. **Do not re-open this report's staging unless new evidence appears.** DEF-004/005/010 were corrected on 2026-10-23; the stage counts are 12 / 11 / 9 = 32, and A8 is a subset of SEC-031.
5. **Keep D-004 and D-005 Provisional**; no war-stage design, no hosting selection, no code without explicit owner authorization (D-002).

### 26.10 What the next prompt must *not* assume

- That the 32 SEC requirements are **approved** (they are not; OSQ-011 governs the stage-B line).
- That **TH-022's war-stage classification** makes war-stage abuse "settled" (it is *deferred*, not designed).
- That **A-1…A-7** are facts — any of them can be falsified by a change in cadence, economy, staffing, or provider terms.
- That **ST-### rows are evidence** — they are *plans*; no test has ever been run against a working system.
- That **the recovered §0–§2 text is a perfect content-optical pass** — a final *human* read-back of the front matter is recommended before the Game Design Bible cites its register (it *read correctly* this session's checks).
- That **provider free-tier limits will remain** as found in §15 — the documentation pages change; re-read is mandatory around any real decision.
- That **the moderation ladder** (§12) is a *final sanction policy* — it is a *framework with levels* whose thresholds and severity maximums await OSQ-005's owner decision.
