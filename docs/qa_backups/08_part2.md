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
