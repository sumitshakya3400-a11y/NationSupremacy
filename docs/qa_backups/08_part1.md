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
5. **Account deletion & retention at source (SEC-009):** deletion means the account is deactivated, then expunged per §11's retention rules — gameplay state is deleted or aggregated per §11 with the technical caveat that *backups* produced while the account existed persist until backup rotation (a retention fact disclosed in the privacy record, never hidden). Data the game must retain for legal or anti-abuse reasons is minimized and documented per §11.

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
