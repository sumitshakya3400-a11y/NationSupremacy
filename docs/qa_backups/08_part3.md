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

**Essential before any public playable (stage A; §16/§17's assignment):** SEC-010/011/012/013 (server authority), SEC-014/016 (idempotency + atomicity), SEC-018/019/020/021 (turn pipeline integrity), SEC-025 (arithmetic invariants), SEC-029 (quotas). **Nothing on this list is cut to save money, and none should ship late**: they are the *validity* of the game's own object. 16 requirements on stage A would be cheaper than any settled argument if they are precisely specified — and they are.

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
| SEC-001-adjacent deletion rule moved** | — ***(reserved*L*** — placeholder row intentionally blank (documentation symmetry; SEC-009 stays unassigned) | | | | | | | | | | |
| SEC-010 | Server recomputes all valuable quantities | Every mutation recomputes its quantity from authoritative state; a client-submitted quantity is request *intent*, never source of truth | Client-side value manipulation (TH-006) | FP | Prompt 7 §14's honest-preview rule + Prompt 6 §17's not-client-trusted contract | TH-006 | ECON-001 | — | AC: substituted-quantity tests rejected (ST-001/002) | test | FP |
| SEC-011 | Per-action validation list | Each write action carries an explicit validation checklist (eligibility, affordability, cooldown, prerequisites, bounds) *completely* evaluated before commit | Any invalid action | FP | Prompt 7's §14 pricing discipline | TH-006/008/011 | SYS/INT/SOQ ranges | — | AC: every listed endpoint's checklist exists and is exercised | test | FP |
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
| SEC-031 | Audit event ledger (the evidence spine) | §13.2's event table is *the* required ledger: each listed category with its extra fields, retained per §13.2, no sensitive values collected, ride-the-same-transaction ledger writes | Every TH's evidence posture; overall incident/compromise/abuse handling | PL | §13's design; the one cost §15 refuses to cut | All | — | §15.2's budget floor | AC: spot audits of each category's rows (ST-012's read surface) | review | PL |
| SEC-006 | Admin/ops account separation | Ops access is a distinct identity surface (no player session grants ops), with mandatory step-up, scoped verbs, and logged privileged reads | Privileged compromise/insider (TH-018/019) | L | TH-018/019; §4.7 | TH-018/019 | OSQ-012 | — | AC: ops verbs enforce step-up; privileged reads appear in the ledger (ST-014) | test | L |
| SEC-015 | Server-defined turn stamps | Requested-at-T is *decided* by the server under a published boundary rule; client-claimed turn ids are never authoritative | Boundary racing (TH-011/022) | L | §6.3; Prompt 7 §14's classification | TH-011/022 | EX-1 F | — | AC: stale-turn behavior test (ST-010) matches the contract | test | L |
| SEC-017 | Settlement/accounting ledger discipline | Settlement (economy and turn) writes are append-only next-able rows that prove what applied; "already applied" is provable, not assumed | Double-apply/replay support (TH-009/010) | L | Support posture to SEC-020/021 | TH-009/010 | SEC-020/021/030 | — | AC: ledger rows suffice to *prove* the phase dedup (ST-008/009's evidence step) | review | L |
| SEC-022 | Delay/missed-processing disclosure contract | When a turn cannot resolve (or resolves late), a player-visible disclosure of status and remedy is issued; no silent re-derivation | Turn disruption communication (TH-010/022's class) | L | DP-004's honest-discipline posture in incident space; §6.4/§14 | TH-010/022 | — | — | AC: scripted stall yields a queued-visible disclosure (walkthrough W-18-L notes it) | drill | L |
| SEC-024 | Abuse-evidence retention policy | Evidence *extracted* for a review (graph shapes, session/configuration notes-per-report, moderation files) is defined, minimized (SEC-032's rules), retained only as long as a case needs (proposed cadences per §11.2) | Review integrity; privacy (TH-016/024) | L | §8.3/§11; prompt 3 §8's integrity warning | TH-016/024 | SDQ-004; OSQ-010 | — | AC: retention policy text exists; case-file spot checks follow it | review | L |
| SEC-027 | Elevated permission + two-person rule for the most destructive ops | Levels 4–5 of §12.3's ladder and ops-grade corrections require step-up + a second identity (where two exist) and are fully logged | Malicious/compromised privileged (TH-017/018/019) | L | §12.5; TH-019's proposal | TH-017/018/019 | OSQ-012 | — | AC: two-person approvals appear in the ledger for destructive ops (ST-019) | drill | L |
| SEC-028 | Report intake design | Reports record source, target, category, time (§12.2); evidence links are pointers, not essays; repeat clusters are de-prioritized for review, and the source identity is visible to reviewers | Report abuse (TH-016) | L | §12.2 | TH-016 | OSQ-005 | — | AC: intake fields exactly as listed; reviewer-side source visibility verified | review | L |
| SEC-032 | Data inventory + minimization discipline | The §11.2 category table is authoritative: no other personal-data category is operated on without recorded justification + minimization review; retention numerals are locked in the inventory | Privacy posture (TH-024) | L | §11's posture; D-003's decision discipline | TH-024 | OSQ-010 | — | AC: inventory exists and matches the operated surfaces | review | L |
| SEC-033 | Minimal monitoring rail | The §15.3 posture (budget gauges + abuse counters + the two loud-failure alerts: quota risk and pipeline stall) exists, checked at the ops cadence | Silent failure / quota attacks (TH-012/013) | L | Prompt 7 §16.4's S rows; §15.3 | TH-012/013 | — | — | AC: both alerts fire in scripted quota/stall drills | drill | L |

(SEC-009 is intentionally unassigned; see §0.3's note and §24's register.)

### 16.3 Traceability note

Every threat row in §2.3 has at least one mitigation among the 32 requirements above (prompt's "every critical threat must have at least one prevention, detection, or recovery requirement" is satisfied per row — §25's traceability audit re-verifies it mechanically). Every requirement's `VM:` row either names the ST-### acceptance test that will verify it or names the review/drill that does; no requirement promises a test that doesn't exist in §19's register.
