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
| A5 | Turn pipeline integrity: exclusive resolution claim + turn-state ledger with phased checkpoints + phase-grain dedup + deterministic boundary | SEC-018, SEC-019, SEC-020, SEC-021 | SYG-016's pipeline is the whole game's mutation engine (§6.1); a duplicate or partial resolution *is* a global economy incident with no attacker at all (TH-009/010) |
| A6 | No-negative/no-overflow server-side invariants | SEC-025 | One negative balance at resolution is systemic (scale argument; §6.1) |
| A7 | Per-action-class quotas with the scheduler's quota reserved | SEC-029 | The free tier's budget is a *functional* attack surface (TH-012); without class quotas, one abusive client can freeze the day's economy |
| A8 | Minimum audit rows for money/pipeline touching (the ledger's spine, phased) — mutation rows ride mutation transactions; sampling policy per §15.2 | SEC-031's *spine* rows | Reversals/reconciliations/disclosures (§14.4) are *evidence-driven*; without rows, compromise review (§4.6) and dispute resolution (§12) degrade to memory |
| A9 | The honest-failure contract | fail-with-reason (§5.2) | DP-004's whole posture lives here; enforcement without reasons becomes noise the community can't calibrate (and appeals become accusations) |

**Why nothing else is in stage A:** every other control in §16 has an *economic or people-scaled* dependence (a population, an adversary class, a tool surface) that a first-playable build doesn't yet exhibit; where the deferring is *eventually unsafe* it sits in stage B by population/scope, not by budget.

### 17.2 Stage B — required before public launch

| # | Work item | Requirements | Why at this stage |
|---|---|---|---|
| B1 | Account security stack's full depth — verified identity (per OSQ-003), memory-hard password handling, step-up for sensitive actions, session lifecycle discipline, login/recovery rate limits, sensitive-change notifications, the compromise runbook (rehearsed) | SEC-001…005, 007/008 | The moment real players, e-mail anchors, and *economy-held value* co-exist, account-level compromise becomes real damage (TH-001/002/014's classes); rehearsal (ST-009-style) is the proof-of-competence |
| B2 | Abuse-control suite under test conditions — the fresh-account window + per-pair velocity caps + asymmetric outgoing caps, *with* their detection tuned by evidence (ST-016's funneling test passing as "surfaced for review") | SEC-023, SEC-024 | At population scale, multi-accounting becomes the genre-verified top abuse; R-13's caps pre-exist *at design*. This stage is their *tuned enforcement*, not new mechanics |
| B3 | Moderation machinery at launch scope — the sanctions ladder documented/audited, intake fields defined, review scope rules | SEC-026 (+ SEC-027/028 to the degree staffing exists) | PXE-011's moderation-capacity plan is a launch commitment; without logged acts, ladder discipline can't be audited (the single-operator caveat is an OSQ-005 decision, not an excuse) |
| B4 | Backups + restore discipline + a restore drill (ST-009) recorded | SEC-030 | §14.2: a public launch without a rehearsed restore is exactly TH-023's "restore mishandling" pre-condition (or, run with *no restore ability*, a *disclosed* Sev-1 risk that OSQ-007 must own) |
| B5 | Audit spine completed for every §13.2 category (the stage-A rows were spine-critical; stage B fills the rest) | SEC-031 | §13's categories exist in the design's *whole* shape: without the full set the evidence spine is a selective system, which is its own trust failure (SEC-031's "evidence is complete" requirement) |
| B6 | The minimal monitoring rail, live at ops cadence (budget gauges + the two loud-failure alerts) | SEC-033's minimum | Silently degraded ops at a public launch is precisely TH-012's blindspot; budget gauges cost almost nothing and can save the day's economy |

### 17.3 Stage C — later hardening

| # | Work item | Requirements | Deferral rationale |
|---|---|---|---|
| C1 | Ops-grade identity separation, step-up on ops, scoped privileged reads | SEC-006 (with OSQ-012) | A single-operator project's *realistic* first posture is "the owner is an accountable, logged, disclosed operator" (TH-019's compensating control is disclosure); the *separation* work pays when a second operator exists |
| C2 | Server-defined turn-stamping *attribution*, ledger discipline as a "provable already-applied" layer, delay-disclosure automation | SEC-015, SEC-017, SEC-022 | Stage A's checkpoints already make these *requirements findable*; automation discloses at a polish-level, not integrity-essential |
| C3 | Abuse-evidence retention policy (data retention schedules for cases) | SEC-024 | Needs *cases at volume* to tune honestly; §11.2's tables suffice for first-playable posture |
| C4 | Two-person rule hardened for levels 4–5 + formal moderation tooling | SEC-027, SEC-028 | Follows staffing (OSQ-005) — two-operator reality first, tooling second |
| C5 | Full data-inventory discipline + monitoring polish | SEC-032, SEC-033's *full* shape | Legal-jurisdiction work (OSQ-010) and scale tuning belong with launch-jurisdiction knowledge |
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
2. **Action:** العقد of requests hammer quotas.
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
8. **Requirements:** SEC-001, SEC-005, SEC-028?no — SEC-029, OSQ-002/003 posture.

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
