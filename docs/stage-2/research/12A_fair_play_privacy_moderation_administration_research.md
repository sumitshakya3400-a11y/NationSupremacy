# 12A — Fair play, player protection, privacy and administration: research, evidence and design foundations

**Project:** Nation Supremacy (internal codename *Project X*)
**Stage:** Stage 2 — the Master Game Design Bible (`D-012`)
**Prompt:** 12A — research, evidence, requirements and design foundations for the Prompt 12 system family
**Executed:** 2026-11-06
**Level of completion:** research and design-foundations. **Documentation only.** No rule, penalty, permission, schema, screen or implementation is approved by this document, and no control described here is implemented, executed or runtime-tested.
**Bible part this feeds:** B-12 — Fair play, player protection, privacy and administration ([outline](../02_master_game_design_bible_outline.md))
**Canonical companions:** [sources and benchmarks register](12A_sources_and_benchmarks_register.md) · [requirements, integration and risk registers](12A_requirements_integration_and_risk_registers.md) · independent validator [`12A_validate_foundations.py`](../../qa_backups/12A_validate_foundations.py)

---

## 1. Executive summary

### 1.1 Verdict

**PARTIAL — research and design foundations substantially complete; twenty requirements cannot be closed without an owner or legal decision, two confirmed weaknesses remain open, and this pass was not independently reviewed.**

Prompt 12A inspected the live project, conducted five external research passes across all twenty areas of brief §5.1, benchmarked eighteen comparator platforms against their **mechanisms** rather than their feature lists, and produced 106 candidate requirements, 30 cross-system dependency rows, 32 threat rows, 15 failure-posture rows, 15 open research questions, 15 recorded design directions and nine newly opened owner questions. It resolves no owner-reserved decision and closes none of the 51 existing unresolved rows.

Three things prevent a FULL PASS, and all three are recorded rather than concealed:

1. **Twenty candidate requirements carry an explicit owner or legal dependency and five more are assigned to a named downstream stage or prompt.** They cannot be closed by a prompt acting under `D-014`. They cover the ladder's tier authority, appeal budgets and deadlines, staffing and review independence, the reach of a value correction, emergency authority, the automation policy shape, transparency scope, retention and erasure, and age assurance — `UD-052`…`UD-060`.
2. **Two confirmed weaknesses are identified and not fixed, because they are not this prompt's to fix.** The feasibility prototype still grants `authenticated` a table-wide `UPDATE` on `feasibility.profiles` including its `treasury` column, with only a row-scoped policy, and the designed correction exists **only inside abandoned bytecode** — there is no `0005` migration, no `tests/sql/` directory and no test source on disk. And the prototype's `audit` table has no protective trigger and no delete revocation outside the player role, so the project's audit spine is append-only **by convention**, not tamper-evident. Both are Stage 5 obligations; `12A-RK-007` and `12A-RK-026` keep them visible.
<<<<<<< HEAD
3. **Thirteen of the 153 registered evidence rows were not read in full** — nine are substantive retrieval failures and four are one index-only row, one abstract-only row, one secondary case note and this pass's internal absence finding. The Wayback Machine and EUR-Lex were unreachable for the whole session, and no operator publishes an appeal-overturn rate. The affected rows are labelled in the register and the claims they support are bounded accordingly; no requirement rests on one of them alone. Confidence and access are separate measurements (§4.2).
=======
3. **Nine of the 152 external sources were read only as excerpts of an official page or not at all**, the Wayback Machine and EUR-Lex were unreachable for the whole session, and no operator publishes an appeal-overturn rate. The affected rows are labelled in the register and the claims they support are bounded accordingly; no requirement rests on one of them alone.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

Separately, the moderation and governance pass **corrected three premises it was given** — the Italian AGCM action against Blizzard is an *investigation opened in January 2026*, not a fine; the EA-Italy matter *closed with commitments and no infringement found*, and the €10 m action was *Dutch* and was *overturned on appeal* in 2022 (`12A-RS-135`…`12A-RS-138`). Those corrections matter: they move item-economy regulation out of the moderation design's assumed obligations and into the separate legal dependency under `UD-017`.

### 1.2 The nine findings that change the design

These are the results that a reader who reads nothing else should carry into Prompt 12B. Each is evidenced in §5 and discharged into requirements in §23.

1. **Server authority is not a mitigation here — it is essentially the whole control, and it is unusually affordable.** With no downloadable client, the only defence a realtime game can use that this game cannot is client-side integrity; the only defence it *must* use is that the client never supplies a value the game acts on. Roblox and Valve state the same rule (`12A-RS-001`, `12A-RS-002`), and it is already approved policy as `SEC-010` and `D-032`. The consequence for 12A is uncomfortable but clarifying: most of the brief's "anti-cheat" question is answered by **architecture already designed**, and the remainder is not detection at all but economics.
2. **Hidden-information abuse in a mapless game is an API-response problem, not a detection problem.** The security literature's central finding on information cheats is that they exist because the server legitimately *sent* what the player should not know (`12A-RS-040`, `12A-RS-041`). Nation Supremacy's secrets are not spatial — they are diplomatic intent (`D-030`), trade terms (`D-017`), military values (band-only, `WEP-651`) and Alliance finances (`ALL-156`). Every one is a response-shape decision that can be made correctly and audited statically, at zero surveillance cost.
3. **Network-derived identification is documented to over-punish, and by a factor this project cannot dismiss.** Cloudflare's own measurement finds near-identical bot rates on CGNAT and non-CGNAT addresses while CGNAT traffic is rate-limited **three times more often** (`12A-RS-034`); MaxMind states IP data is never household-precise (`12A-RS-058`); Richter et al. show carrier-grade sharing is structural (`12A-RS-057`). Two comparable browser nation games reached the same conclusion in policy language, not telemetry — eRepublik states same-IP is not a criterion (`12A-RS-049`), and Politics & War restricts interaction rather than banning on it (`12A-RS-050`). **The approved `NET-039` ceiling is therefore not a compromise; it is the correct answer, and this research strengthens it.**
<<<<<<< HEAD
4. **Identity-layer multi-accounting cannot be reliably detected under the current fixed constraints, and the design must say so.** The Sybil literature's negative results are explicit: absent special assumptions — trusted certification, scarce resources or a fast-mixing social graph — Sybils cannot be prevented (`12A-RS-060`, `12A-RS-061`). Nation Supremacy has refused certification (`D-042`), cannot afford a proof-of-work posture that would be hostile UX, and has no friend graph at first playable. That is an inability to reliably establish a *common identity*, not an inability to see coordinated abuse: behavioural, transactional and outcome evidence can still support a named case (§8.4–§8.5). The honest conclusion is `12A-RK-027`: **an accepted critical residual**, disclosed rather than papered over.
=======
4. **One-controller-many-identities is information-theoretically undetectable under this project's constraints, and the design must say so.** The Sybil literature's negative results are explicit: absent special assumptions — trusted certification, scarce resources or a fast-mixing social graph — Sybils cannot be prevented (`12A-RS-060`, `12A-RS-061`). Nation Supremacy has refused certification (`D-042`), cannot afford a proof-of-work posture that would be hostile UX, and has no friend graph at first playable. The honest conclusion is `12A-RK-027`: **an accepted critical residual**, disclosed rather than papered over.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
5. **The exploitable surface is therefore the *value*, not the *identity* — and the industry's effective answer is outcome offences plus reversible value correction.** EVE recovers value from the "main" character without proving control and treats both sides of a trade as one story (`12A-RS-066`); GGPoker defines chip dumping as an offence for which "both the user who transferred the chips and the user who received the chips are at fault" (`12A-RS-055`); Riot routes ~296,000 boosting cases to rank resets and rating reversion rather than one global verdict (`12A-RS-018`, `12A-RS-052`); Jagex moved against buyers because buyer demand, not sellers, is the supply engine (`12A-RS-075`). This yields the report's central architectural distinction (§6.5): **value correction versus conduct sanction**, with different evidence bars, different reversibility and different appeal rights.
6. **A hard close every two hours manufactures a timing-abuse class, and the answer is an ending rule.** Roth and Ockenfels show that a fixed deadline endogenously produces strategic last-moment bidding, and that extension rules reduce it (`12A-RS-036`). B-02 already publishes deterministic ordering that is **not** arrival order (`TR-048`, `SEC-018`), which removes the value payoff by construction. What remains is perception, and the requirement is disclosure of what ordering does and does not affect (`12A-CR-009`) — not monitoring the burst.
7. **The project's own anti-surveillance posture is a compliance asset, not only a value.** GDPR Art. 35(3)(a) makes *profiling with significant effects* the DPIA trigger (`12A-RS-086`); the design's refusal to profile is therefore doing legal work as well as ethical work. That reframing matters for Prompt 12B: the privacy posture should be defended on both grounds, and weakened controls should be resisted on both grounds.
8. **Three incompatible classification vocabularies already exist, and `WEP-647`'s inheritance claim is inaccurate as written.** `D-042` assigns four handling classes, `TR-021` four visibility classes with `TR-090` adding purpose classes, and `WEP-647` says it "uses B-02's classes" then lists **eight** role levels (`12A-OPEN-001`). A fourth flat list would make the corpus worse. The recommendation (§11) is a **three-axis model** with a reconciliation duty, not new adjectives — informed by NIST's split between access enforcement and information-flow enforcement (`12A-RS-116`) and by SP 800-60's method of deriving categories from information types first (`12A-RS-117`).
9. **Two confirmed weaknesses exist today, and neither is a research finding — both are inspection findings.** First, the feasibility prototype grants table-wide `UPDATE` on `feasibility.profiles` including its `treasury` column, with only a row-scoped policy (`prototypes/supabase-feasibility/migrations/0003_grants_and_rls.sql:14` and `0001_schema.sql:69-87`); the designed fix exists **only inside abandoned bytecode** — there is no `0005` migration, no `tests/sql/` directory and no test source on disk. Second, the `feasibility.audit` table has **no trigger and no delete restriction** protecting it (`0001_schema.sql:47-54`, `0003_grants_and_rls.sql:15`): append-only is convention, and the vendor's own model of tamper-*evidence* requires chained digests plus a verification step that nobody performs unless a job does it (`12A-RS-029`). Prompt 12A records both; it fixes neither, because both are Stage 5 production-architecture work.

### 1.3 What Prompt 12A deliberately did not do

No penalty amount, tier duration, appeal deadline, retention day-count beyond what `D-026` and `D-042` already fix, administrator permission table, detection threshold, composite confidence score, database schema or legal conclusion. The brief forbids each (§10.3, §12.2, §15.2, §19, §24), and where the omission blocks a rule it is registered as an owner or legal dependency (`UD-052`…`UD-060`, `12A-OPEN-001`…`12A-OPEN-015`) rather than filled with a plausible number.

---

## 2. Research purpose and scope

### 2.1 Question

How should a persistent, browser-delivered, mapless, turn-resolved nation-strategy game — one where cooperation is the core mechanic, alliances hold treasury powers, markets and elections exist, and identity verification is limited to e-mail — be designed so that competitive integrity, player trust, privacy and administrative accountability are all defensible **without** building a surveillance system or promising a detection capability the architecture cannot supply?

### 2.2 Scope, following brief §24

**In scope:** research and benchmarking; design principles and architectural direction; candidate requirements; a threat and risk register; failure postures; the information-classification foundation; an authority-boundary model; the Prompt 12B handoff; and the documentation and validation record.

**Out of scope:** the B-12 rulebook itself (12B), all workflows and tool design (12C), every penalty value and ladder tier as approved policy, administrator permission tables, reporting and appeal workflows, schemas, anti-cheat or moderation software, production authentication, production security testing, numerical calibration (Prompt 14), screens (Prompt 13), and any modification of approved gameplay mechanics.

### 2.3 What was inspected before any research was read

Per the brief §3 and the mandatory start-of-prompt procedure (stage-2/01 §1), the live project was inspected first: the five root governance documents, all seven Stage 2 register documents, the Stage 2 progress log through §72, Stage-1 Report 08 in full (1,555 lines, §§0–26), all fourteen relevant Bible specifications and their registers, contracts, failure codes and audit-event catalogues, the acceptance crosswalks, and the feasibility prototype's four applied SQL migrations together with the recorded executed permission tests. Register frontiers were read from the files, not from memory: `REQ-763`, `D-162`, `DD-210`, `UD-051`, progress log `§72`.

---

## 3. Project baseline: what Prompt 12A inherits, and its true status

### 3.1 The five-class control status, applied honestly

The brief §3.3 requires each control to be classified as approved, documented, prototype-implemented, executed and verified, or unverified. Applying that to the security-relevant corpus:

| # | Control | Status | Evidence |
|---|---|---|---|
| 1 | Server-authoritative validation of valuable actions | **Approved design requirement** | `SEC-010`/`SEC-011` proposed; `D-018` policy confirmed; `REQ-019` Provisional assigned to B-12; restated by every rulebook's settlement sections |
| 2 | Session-derived acting identity; object references authorised separately | **Approved design requirement** | `D-032` Confirmed (design) |
| 3 | Reservation, idempotent single-spend, atomic settlement, no-debt | **Approved design requirement** | `D-016`, `ECN` settlement order, `MKT` atomic P4 settlement |
| 4 | Exactly-once boundary claim, phase checkpoints, forward-only resume | **Approved design requirement** | `D-025` Confirmed; `SEC-019`…`SEC-021` proposed |
| 5 | Aggregate suppression `k = 5`, complementary suppression, no differencing | **Approved design requirement** | `D-027` Confirmed; `TR-022`; `WEP-649`/`WEP-650` Approved |
| 6 | No raw IP stored; normalised /64; HMAC digest; pepper outside the repository | **Approved design requirement**, enforcement deferred | `D-036` Confirmed (design), **Deferred to Stage 5/6** |
| 7 | One account, one active nation; five pair states; IP-only ceiling; attestation-based clearance; no co-resident exemption | **Approved design requirement** | `D-018`, `D-032`, `D-033`, `D-034`, `D-037`, `NET-039` |
| 8 | Retention classes S/P/O and a permanent audit spine | **Approved design requirement**; class-O operational value left to Prompt 12 | `D-025`, `D-026`, `TR-090`, `TR-092` |
| 9 | Least-privilege administration; privileged read logged; no silent history rewrite; no enforcement without a recorded reason and an appeal route | **Approved design requirement**, unimplemented | `D-042` Confirmed (design), values Provisional; `DAT-004`; `DIP-121` |
| 10 | RLS and grants denying prohibited player writes | **Implemented in a prototype and executed against a live database** — *narrowly* | `stage-1/11` §15.3, `stage-1/12` §4 (8/8), `results/nation-supremacy-project.json` |
| 11 | Column-scoped protection of a server-owned profile value | **Documented but not implemented, and unverified** | The intended fix (`0005_profile_column_privileges.sql`, a guard trigger, `tests/sql/profile_permissions.test.sql`) exists only as expectations inside a gitignored `.pyc`; **no such file is on disk** |
| 12 | Tamper-evident audit spine | **Documented requirement; not implemented; the prototype contradicts it** | `SEC-031` proposed; `feasibility.audit` has no delete restriction or trigger |
| 13 | Moderation ladder, appeals, ban-evasion and multi-account enforcement procedure | **Not designed.** Assigned to Prompt 12 | `NET-040` "the detailed procedure belongs to Prompt 12"; `TR-087`; `WAR-155`; `WEP-704`; `AX-23` Deferred |
| 14 | Privileged-read auditing | **Required in four places, owned nowhere** | `DPE-054` PARTIAL; `WEG-04`; `NET-051`; `DIP-121` |
| 15 | Backup and restore drill | **Blocked, owner-side; never performed** | CF-02; `stage-1/11` and `stage-1/12` state no drill and no provider-managed backups on the free plan |
| 16 | Supabase Auth end-to-end, rate limiting, sessions | **Not verified; explicitly excluded from executed tests** | `stage-1/12` §6; `stage-1/11`: "No authentication, no session, no rate limiting, no per-user authorization … none is claimed as tested" |

### 3.2 The 8/8 permission result does not cover the defect

The executed live test set read `nations.treasury` as denied (`42501 permission denied for table nations`) and updated "own profile — 1 row" generically. It **never issued `UPDATE profiles.treasury` on the owner's own row**, which is the one write the permissive grant actually allows. The 8/8 and 7/7 counts are accurate as recorded; they are simply silent on this case. Prompt 11C's own §16.6 states the prototype is not security-verified, and this pass confirms that statement is correct rather than over-cautious. **This is a scope observation, not a correction of the earlier report.**

### 3.3 Known-issue status, checked against the current tree

| Reported issue | Current status, verified in this pass |
|---|---|
| Prompt 11A "C29 historical allocation assumption" | Not re-opened. 11A's own validator check 29 still asserts `REQ max 703` and **fails** against the live register (12B's reserved `REQ-764` mention is now the scanned maximum, although no row was allocated). Recorded as pre-existing debt `D-1`; 12A neither repairs nor weakens it, and §32 names what would |
| Legacy final-validator assumptions | Measured at **12** failing checks in `validate_final.py` before 12A — stale frontiers left over from Prompt 11B (`11B` as next prompt, `REQ-001..703`, `DD-001..199`, `UD-001..049`, the 27/4/18 counts, `UD-024` still deferred, and the 55/630/17/1 requirement counts). 12A advanced the assertions its own edits legitimately moved, taking the suite to **10** failures and recording debt `D-2`. The 2026-11-07 review remediation advanced the remaining assertions to the current registers — `REQ-001..763`, `DD-001..225`, `UD-001..060` at **28/3/29**, `UD-024` Resolved, the §6 inventory and the 55/688/19/1/0 requirement counts — so `validate_final.py` now passes; no check was weakened or deleted |
| Supabase profile treasury-permission issue | **Still open**, as described in §3.1 rows 11 and 12, with the correction present only in bytecode |

### 3.4 Approved decisions that bind this prompt and were not touched

`D-014` (autonomy), `D-015` (OP model), `D-016`, `D-017`, `D-018` (multi-account prohibition, review-before-action, published ladder and appeals, no automated ban on one signal), `D-021`, `D-022`, `D-024`, `D-025`, `D-026`, `D-027`, `D-028`, `D-029`, `D-030`, `D-031`–`D-042` (account, pair, network, naming, reroll, protection, lifecycle, data and administration), `D-064`, `D-122` and the Global Trade gate state, `D-137`, `D-140`, `D-141`, `D-142`, `D-143`, and the resolution of `UD-032`, `UD-033`, `UD-039`, `UD-013` and `UD-024`. Owner-reserved `UD-017`, `UD-040`–`UD-049`, `UD-050` and `UD-051` are preserved exactly as recorded, with no status change.

---

## 4. Research methodology and evidence quality framework

### 4.1 Method

<<<<<<< HEAD
Five research passes were conducted against the twenty areas of brief §5.1, organised as: server authority and anti-cheat architecture; multi-account detection and identity abuse; collusion, market and ranking manipulation; privacy, data protection and information classification; and moderation, appeals, administrative accountability and auditability. All five are complete. The deliverable is 153 registered evidence rows in five contiguous registers, 40 benchmark-mechanism comparisons and 18 comparator profiles, with a stated retrieval-failure record.
=======
Five research passes were conducted against the twenty areas of brief §5.1, organised as: server authority and anti-cheat architecture; multi-account detection and identity abuse; collusion, market and ranking manipulation; privacy, data protection and information classification; and moderation, appeals, administrative accountability and auditability. All five are complete. The deliverable is 152 sourced rows in five contiguous registers, 40 benchmark-mechanism comparisons and 18 comparator profiles, with a stated retrieval-failure record.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

Every design question in brief §5.6 was worked in the same order: problem, evidence, options, comparison, security consequence, player-experience consequence, operational consequence, recommendation, assumptions, and any owner reservation. Where the recommendation is not obvious, the alternatives and their rejection reasons are in §5.4 and §27.

### 4.2 Evidence quality framework

The brief §5.3 hierarchy was applied with two project-specific additions:

| Rule | Why it was added |
|---|---|
| A vendor's own description of its product is **high** for what the product does and **zero** for how well it works | Otherwise the register would have recorded marketing claims as detection efficacy. Riot, Valve, Epic, Ubisoft, Jagex and Chess.com all decline to publish detection internals, and one of them states the reason on the record (`12A-RS-013`) |
<<<<<<< HEAD
| A source that could not be read is recorded with a retrieval-failure row and its actual confidence (`Unverified`, `Low` or `Medium`), never dropped | A later session would otherwise re-derive the claim from a plausible memory. Nine rows are substantive retrieval failures, three carry the `Unverified` token and thirteen were not read in full; register §10.1 reconciles the sets |

Confidence is `High`, `Medium`, `Low` or `Unverified`, assigned per row by the **leading token** of its confidence cell. Across all 153 rows the distribution is `High` **65**, `Medium` **71**, `Low` **14** and `Unverified` **3**; the 140 rows read in full split `High` **63**, `Medium` **68** and `Low` **9**, while the 13 rows not read in full split `High` **2**, `Medium` **3**, `Low` **5** and `Unverified` **3**. Confidence is not source-access status: access is classified separately in register §10.1. Contradictions are recorded as contradictions rather than averaged: the clearest is `12A-RS-044`/`12A-RS-045` (declared shared access permitted) against `12A-RS-047` (shared IP automatically escalates and a paid tier buys exemption) — two live designs reaching opposite conclusions, whose reconciliation for this project is §8.3.
=======
| A source that could not be read is recorded with a retrieval-failure row and marked `Unverified`, never dropped | A later session would otherwise re-derive the claim from a plausible memory. Six rows are in this state, listed in the register §9 |

Confidence is `High`, `Medium`, `Low` or `Unverified`, assigned per row, and 45 of 120 read rows reach `High`. Contradictions are recorded as contradictions rather than averaged: the clearest is `12A-RS-044`/`12A-RS-045` (declared shared access permitted) against `12A-RS-047` (shared IP automatically escalates and a paid tier buys exemption) — two live designs reaching opposite conclusions, whose reconciliation for this project is §8.3.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

### 4.3 What counts as a verified research result here

A claim is treated as a **result** only when it is (a) read from a primary source, (b) attributable, and (c) transferred to Nation Supremacy with an explicit statement of the setting difference. Claims about undisclosed internals — how any vendor actually detects an alt account — are recorded as *unknown* and never converted into a design requirement.

---

## 5. Benchmarking findings

<<<<<<< HEAD
The full comparison lives in the benchmark register (`12A-BM-001` … `12A-BM-040`, eighteen comparator profiles `12A-CMP-01` … `12A-CMP-18`). This section states only what the comparison **changed** in the design direction.
=======
The full comparison lives in the benchmark register (`12A-BM-001` … `12A-BM-032`, twelve comparator profiles `12A-CMP-01` … `12A-CMP-12`). This section states only what the comparison **changed** in the design direction.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

### 5.1 Coverage

| Domain | Comparators actually read | Deepest evidence |
|---|---|---|
| Persistent browser nation and strategy games | Politics & War, Travian Kingdoms, Supremacy 1914 / WW3 / Call of War, Tribal Wars 2, Forge of Empires, eRepublik, NationStates, EVE Online | Politics & War (rules plus moderation practice) and Bytro Supremacy WW3 (the same-IP automation case) |
| Ranked and competitive enforcement | Riot (League of Legends, VALORANT), Valve (VAC), Blizzard, Bungie, Niantic, Epic, Chess.com, Lichess | Valve's VAC page and Riot's penalty FAQ, both read in full |
| Real-money and fraud-adjacent platforms | GGPoker Security Ecology Policy, PayPal graph-fraud engineering | GGPoker's numbered offence taxonomy |
| Non-game governance | English Wikipedia sockpuppet and meatpuppet doctrine | Wikipedia's declared-connection convention |
| Market manipulation | U.S. CFTC spoofing alert and enforcement order, U.S. SEC definition | CFTC's intent-plus-structure drafting |
| Timing and mechanism design | Roth & Ockenfels; Lenzi's Sybil-resistant voting analysis | Reviewed economics |
| Security and privacy standards | OWASP Top 10 Web and API, ASVS 5, Authentication, Business-Logic and Automated-Threats material, IETF RFC 9110, RFC 6962, RFC 3161, NIST SP 800-53 Rev. 5 (read from the official OSCAL catalogue), SP 800-60, SP 800-61r2, SP 800-86, ISO/IEC 27035-1 sample pages, CISA zero-trust microsegmentation, EDPB Guidelines 01/2025 and 9/2022, WP29 05/2014, ICO archived guidance, GDPR articles and recitals, the DSA consolidated text, the EU adequacy list, Supabase and Cloudflare platform and contract documentation, Microsoft's emergency-access guidance | Standards and regulator text, with the proxy and excerpt caveats recorded per row |

### 5.2 The comparison in one table

| Mechanism family | Exemplar | Works here? | Why |
|---|---|---|---|
| Prohibit, publish, report, decide | Travian, Bytro intake, InnoGames | **Yes, with a mandatory addition** | Cheap and community-scaled, but needs a stated evidence bar or it becomes a harassment tool (`12A-CR-063`) |
<<<<<<< HEAD
| Declared-connection register | Tribal Wars 2, Wikipedia | **Yes, re-scoped** | Converts a fact about common identity that cannot be reliably established into an attested one; must not unlock interactions, because `D-037` forbids an exemption (`12A-CR-016`) |
=======
| Declared-connection register | Tribal Wars 2, Wikipedia | **Yes, re-scoped** | Converts an undetectable fact into an attested one; must not unlock interactions, because `D-037` forbids an exemption (`12A-CR-016`) |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
| Automatic per-turn interaction restriction | Politics & War | **Yes, re-keyed** | Attacks payoff, not identity; must key to declarations and evidenced relationships, never to IP (`12A-CR-015`) |
| Outcome and value offences | GGPoker, EVE, Jagex, Riot | **Yes — the primary tool** | Needs no proof of control, and this game already records every flow (`12A-CR-018`, `12A-CR-054`) |
| Bright-line eligibility rules | Riot Clash, Chess.com | **Yes** | Auditable, needs no detection, and fits standings, objectives and events (`12A-CR-026`) |
| Mechanism design (make Sybils net-negative) | Lenzi | **Yes, but assigned elsewhere** | The only family that works without identity data; it is a balance question for Prompt 14 (`12A-CR-026`) |
| Graph and behavioural scoring as triage | EA research, PayPal | **Yes, as a queue only** | The same topology is a friendship or a ring; sparse turn data makes it weaker still (`12A-CR-024`) |
| Statistical detection producing auto-punishment | Chess.com scale, Bytro Suspicion Score | **No** | Requires dense telemetry and accepts an undisclosed verdict; mimicry defeats it (`12A-RS-020`) |
| Device or hardware binding | Riot HWID | **No, and say so publicly** | Documented innocent-housemate sanctions; rejected by `D-042` (`12A-RK-012` row `12A-BM-012`) |
| Identity or payment verification | GGPoker KYC, Riot SMS, South Korea | **No** | Explicitly refused by `D-033`; the exclusion is the design's honest ceiling |
| Paid exemption from a fairness restriction | Bytro Security Council | **No** | Converts fairness into revenue; contradicts `D-018` |
| High-volume automated enforcement | Jagex, Ubisoft | **No** | Three to four orders of magnitude beyond a one-operator service (`12A-OPEN-005`) |

### 5.3 Where the evidence disagrees, and what the disagreement means

**Automatic versus attested handling of shared networks.** Bytro's pipeline and InnoGames' declaration route are both live, both in the same genre, and opposite. Bytro's is the only one with a published *outcome* (auto-blacklist plus paid relief) and it is the one every comparable community complains about; InnoGames' has no published efficacy data at all. The disagreement is therefore not "measurement versus opinion" on one side — it is **an undisclosed automated verdict against an attested manual process whose cost is reviewer time**. For a one-operator service with `D-018` already forbidding automated punishment on one signal, the attested route is the only one that is both available and lawful under the project's own approved policy. Recorded as `12A-CR-016`, with the `D-037` guard.

**Value recovery without proof of control.** EVE and GGPoker both act on both sides of a flow; Riot also reverses gains across linked accounts but only "where we are extremely certain". These are not contradictory — they differ on **how much culpability the remedy implies**. Reverting a reward needs less certainty than suspending an account, and the industry's practice splits exactly along that line. §6.5 and `12A-CR-054` adopt the split rather than picking a side.

**Publication of detection method.** 343 Industries, CCP and Chess.com all refuse on the ground that evaders read the documentation; P&W publishes its penalty scale and its evidence bar anyway and remains popular. These are compatible if read precisely: what is secret is the **detector**, what is published is the **rule, the consequence and the standard of proof**. Nation Supremacy can and should publish the latter three, which is what `12A-CR-058` and `12A-CR-072` require.

### 5.4 Options considered and rejected, with reasons

| Design question | Rejected option | Reason | Adopted |
|---|---|---|---|
| How to identify controllers | Device fingerprinting, payment correlation, ID documents | Contradicts `D-033`/`D-042`; documented innocent-housemate harm (`12A-RS-053`); the regulator has since moved these identifier classes *toward* stricter treatment (`12A-RS-101`) | Attested declaration plus outcome offences; disclosed inability |
| How to decide an anomaly | A composite confidence score | No validated method or dataset; false precision that cannot be defended on appeal; brief §7.3 forbids it | Five named evidence states plus a corroboration rule |
| Where to enforce limits | Edge or client checks | Cloudflare counters are per-datacentre and seconds-late (`12A-RS-032`); service role bypasses RLS (`12A-RS-010`) | Same-transaction enforcement (`12A-CR-010`) |
| How to answer information cheats | Detection of readers | The literature shows the leak is the operator's own response (`12A-RS-040`) | Response minimisation (`12A-CR-011`) |
| Whether to allow Alliance or group voting delegation | Any delegation | `D-137`/`D-140` settled it; `UD-047` remains owner-reserved | National authority only; untouched |
| Moderation of Alliance discipline | Platform hearing an Alliance expulsion | `UD-044` is owner-reserved and the roadmap forbids it | Platform enforcement stays platform-level |
| Emergency powers | Standing broad authority | Produces exactly the permanent power brief §13.6 warns against | Enumerated, turn-counted, self-expiring (`12A-CR-084`) |

---

## 6. System A — fair-play foundations

### 6.1 The principle

The client is a display surface. It may express intent; it may never report a result. Every quantity the game acts on is recomputed from authoritative state at the point of effect, in the same transaction that writes it. This is approved policy (`SEC-010`, `D-032`) and externally corroborated (`12A-RS-001`, `12A-RS-002`); what Prompt 12A adds is the *enumeration* — because the principle is only testable once someone has listed what it covers.

### 6.2 Source of truth, per protected category

The brief §6.1 requires this enumeration and warns that the implementation mechanism need not be uniform. It is not: four different mechanisms already exist in the approved corpus, and this table names which one owns which category rather than forcing one pattern.

| Protected category | Source of truth | Computing authority | Existing rule that owns it |
|---|---|---|---|
| Treasury balance | The append-only ledger | Turn resolver at P3, trade settlement at P4 | `ECN` ledger, `D-064`, `MKT` atomic settlement |
| Resource balances and reservations | Warehouse and reservation state | Turn resolver; offer acceptance | `ECN` storage, `TR-067`/`TR-069` reservation |
| Population, housing, city and infrastructure state | B-05 city state | P3/P4 settlement | `URB-040`, `D-069`/`D-070` |
| Approval, stability, legitimacy, political state | B-06 | P3.8 and P4.4 settlements | `DMP-132`, `DMP-267` |
| Research and technology | B-05 research state | P4 | `D-076`…`D-078` |
| Military readiness and inventories | B-10 force pools | P3.7 snapshot | `WAR-053m`, `D-015` |
| Operations Points | One persistent national military-only pool | +1 at the P3.7 opening, cap and carry per `D-015` as amended | `D-015`, B-02 §19 |
| Warfare outcomes | B-10 deterministic resolution plus one seeded fortune roll | P5 campaign resolution | `B10-AD` rows |
| Diplomatic posture and agreements | B-08 three-layer object | Boundary activation and expiry | `DIP` lifecycle, `D-137` |
| Alliance membership, roles, policy, ARL | B-09 | P3 tax settlement, role edits immediate-with-audit | `ALL-006`…`ALL-008`, `ALL-071`, `D-140`/`D-141` |
| Market transactions | B-07 offer and execution records | P4 | `D-016`, `D-110`, `D-111` |
| Objective progress and completion | B-11 keyed completion | P6 W1 in the fixed intra-P6 order | `WEP` objective rules, `DD-198` |
| Event participation | B-11 participation records | P6 | `WEP-132`…`WEP-144` |
| Standings, rankings and snapshots | B-11 sealed snapshot | P6 snapshot, P7 publish | `WEP-335`, `WEP-647`…`650` |
| Progression grants, reward entitlements and honours | B-11 derived layers | P6, ledgered reward class | `WEP-447`…`WEP-458`, `DD-199` |
| Moderation, investigation and enforcement records | **B-12 — this is the only category 12A adds** | Enforcement writes a record; it never writes another system's state | `12A-CR-002`, `12A-CR-056` |

Two observations follow. First, B-12's source of truth is **only** its own records; the brief's warning that these foundations must not become "universal controllers over all gameplay" is discharged by `12A-CR-096`. Second, the enforcement record is the one category whose integrity nothing else can vouch for — which is why §19 auditability is the load-bearing requirement rather than a compliance chore.

### 6.3 The exploit taxonomy

Built on the three axes the reviewed taxonomy supplies — vulnerability, consequence and principal (`12A-RS-038`) — and evaluated against the mechanics above rather than against a generic list. Full mapping in the risk register `12A-RK-001`…`12A-RK-032`; the classes:

client manipulation · request and parameter tampering · object-, property- and function-level authorization abuse · resource duplication · transaction replay · duplicate or unentitled reward · state manipulation through an over-broad write path · race conditions · automation and bot abuse · rate-limit and quota circumvention · timing exploitation at the boundary · pipeline integrity abuse · market manipulation · ranking and standing manipulation · objective farming · event-participation manipulation · warfare exploit behaviour · alliance-structure abuse · unauthorised information acquisition · aggregate disclosure · account and identity abuse · sanction evasion · report abuse · **insider and administrative abuse**.

The last class is not decoration. Report 08 already listed moderator abuse, compromised operator accounts and insider access as distinct threats (`TH-017`–`TH-019`), and a 2026 operator incident shows the pattern live: a developer used production tools on player runs and was dismissed, with the scope of the incident asserted by the operator rather than evidenced (`12A-RS-028`). A fair-play design that models only external players is modelling the wrong adversary.

### 6.4 Evidence states, and what each may produce

Five states, deliberately not merged:

| State | Definition | Maximum permitted consequence |
|---|---|---|
| Suspicion indicator | One rule fired; no independent support | Nothing. Logged for triage only |
| Policy signal | A declared limit or invariant was crossed, self-evident from the record | A preventive, reversible restriction, disclosed as temporary |
| Corroborated evidence | Two or more independent evidence sources agree, at least one non-behavioural | Investigation; value correction where the flow itself establishes the effect |
| Established violation | A reviewer recorded the finding against a stated rule with its evidence | Any tier of the ladder, appealable |
| Inconclusive | Investigation exhausted without corroboration | Nothing adverse; the case is closed as inconclusive and that fact is recorded |

The distinction between **suspicious activity, policy violation, confirmed exploitation, deliberate cheating, unintentional breach and legitimate unusual behaviour** (brief §6.3) is carried by two axes rather than six labels: whether a rule was crossed (violation or not) and what the record says about intent (deliberate, unintentional, or not determinable). A statistical oddity is on neither axis. `12A-CR-004` and `12A-CR-005` make that a requirement.

### 6.5 The central architectural distinction: value correction versus conduct sanction

This is the report's main design recommendation.

| | Value and standing correction | Conduct sanction |
|---|---|---|
| Question answered | "What did the system produce that it should not have?" | "Did this person break a rule?" |
| Evidence required | The effect itself: a flow, a grant, a score the rules could not produce | An established violation, corroborated |
| Certainty about identity | **None required** | Required; the account must be the right one |
| Reversibility | Always reversible; reversal is the default if wrong | Reversal requires an appeal, and the record must show it |
| Appeal | Defined by `12A-OPEN-012`; the industry treats it as lighter | Full appeal right (`NET-044`, `12A-CR-070`) |
| Public statement | Never named publicly | Outcome only, in the narrow form permitted (`NET-050`) |
| Industry precedent | Riot rating reversion and reward revocation (`12A-RS-018`, `12A-RS-052`); EVE main-character recovery (`12A-RS-066`) | Travian and Bytro report-plus-decision routes; P&W's point-scale bans (`12A-RS-050`) |

Adopting the split gives Nation Supremacy an effective, honest, low-cost first response in exactly the situations where it can never prove identity — and it removes the incentive to build a surveillance capability to reach a verdict it does not need for the value case. It is recorded as `12A-CR-054`, with the owner-dependent extension in `UD-052`.

### 6.6 False-positive prevention

The brief §6.4 lists eleven legitimate behaviours; all eleven are registered as a maintained catalogue (`12A-CR-029`) rather than as good intentions, because a detection rule cannot be reviewed without knowing what it will wrongly catch. Four deserve their reason stated here:

- **Shared households, campuses, workplaces, public connections and mobile networks** are structurally indistinguishable at the network layer, and CGNAT is not a user choice (`12A-RS-034`, `12A-RS-057`). This is why `NET-039`'s ceiling is a *correctness* rule, not a mercy rule.
- **Families and friends playing the same game** are permitted by `D-018` itself — household members "may each hold an account". A detector that cannot tell them apart is not conservative; it is wrong by design.
- **Legitimate Alliance coordination** is the game. EVE's alliance-scale structures emerge precisely because coordination is hard (`12A-RS-079`), and B-09, B-10 and B-11 already treat coordinated action as normal gameplay (`ALL`, `WAR`, `WEP-654`). `12A-CR-025` makes alliance-scale similarity an explicit non-indicator.
- **Similar economic behaviour caused by the game itself** is the subtlest class. A shared scarcity engine, a common upkeep curve and twelve boundaries a day make legitimate players look like each other by construction; RuneScape's own analysis attributes the symptoms to net inflow, not conspiracy (`12A-RS-076`). `12A-CR-026` therefore routes such cases to balance diagnosis first.

### 6.7 Fair-play architecture, by responsibility

| Responsibility | Owner | Automated or discretionary |
|---|---|---|
| Prevention | B-02 turn engine, each subsystem's own invariants, response-shape policy | **Automated, deterministic, and the primary control** |
| Detection | Rule-generated signals; ledger and graph analytics; player reports | Automated **triage only** |
| Evidence collection | The audit spine; the ledger; the reservation and turn-state records | Automated capture, no interpretation |
| Investigation support | Case records, corroboration tracking, conflict-of-interest flags | Tool-assisted, human-directed |
| Enforcement authority | B-12 ladder, exercised through the owning subsystem's correction path | **Discretionary, recorded, reasoned** |
| Appeals | B-12 appeal record; different reviewer where possible | Discretionary |
| Monitoring | Minimal operational rail: conservation breaks, spine-verification failure, queue depth | Automated alerting, no player inference |
| Auditability | Append-only spine with chained digests and a verification job | Automated integrity, human review |
| Recovery | Forward-only correction, restitution through owning rules, disclosed incident | Discretionary with a stated rule |

`D-014`-compliant, and consistent with Report 08's "review-then-act" posture while adding the external support it previously lacked (`12A-RS-004`, `12A-RS-033`, `12A-RS-062`).

---

## 7. System A continued — anti-cheat architecture

### 7.1 What is actually buildable here

| Layer | Available to Nation Supremacy | Design consequence |
|---|---|---|
| Client integrity attestation | **No** — browser delivery, no binary, and `D-042` refuses fingerprinting | Never claim it; the honest ceiling is stated in `12A-CR-034` |
| Network reputation and bot scoring | **Not affordable** — an enterprise add-on (`12A-RS-033`), and it over-punishes CGNAT (`12A-RS-034`) | Excluded |
| Server-side deterministic validation | **Yes** — and it is the strongest layer available | `12A-CR-001`, `12A-CR-006`, `12A-CR-010` |
| Economic invariants and conservation checks | **Yes** — C1–C4 already exist | `12A-CR-004`-class detection is arithmetic, not statistics |
| Transactional atomicity and idempotency | **Yes** — already approved | `12A-CR-007`, `12A-CR-008` |
| Disclosure minimisation at the response layer | **Yes** — and it retires a whole cheat class | `12A-CR-011` |
| Statistical and graph analytics | **Yes, for triage** | `12A-CR-023`, `12A-CR-024` |
| Human investigation | **Yes, at low volume** | `12A-CR-031`; capacity risk in `12A-OPEN-005` |

### 7.2 Prevention before detection, expressed as a design duty

`12A-CR-026` states the duty: for each abuse, the design must first consider an eligibility bright line, a structural cap, a per-account one-time key, a velocity bound, or a mechanism-design change, and reach for detection only when those are unavailable. Two worked examples show why this is not rhetoric.

**Boundary sniping.** The literature's answer to a hard close is to change the closing rule (`12A-RS-036`). Nation Supremacy's ordering is already deterministic and published (`TR-048`, `SEC-018`), so the value payoff is gone; the residue is informational, and the correct response is a disclosure sentence about what ordering does and does not affect, not a monitor.

**Election manipulation by alt accounts.** B-06 already closes the mechanical route: challengers are not accounts, players or second nations, and a second account cannot act inside one nation (`DMP-185`, `D-032`) — a structural answer that no detection could match. Where any residual risk lies in collective or Alliance-level balloting, that is `UD-042`/`UD-049` territory and owner-reserved. The only further tool available is cost, which Lenzi's analysis shows trades Sybil-resistance for wealth influence (`12A-RS-065`) — a balance decision for Prompt 14, not a policing decision for 12B.

### 7.3 Detection has a ceiling, and it is measurable

A behaviour-mimicking automation defeats state-of-the-art detectors (`12A-RS-020`); the only cross-vendor review available concludes that no single layer suffices and that server-side analytics have limited visibility (`12A-RS-015`); and the Sybil literature states the negative result at the identity layer itself (`12A-RS-060`). Nation Supremacy's telemetry is also sparse by construction: twelve coarse events a day, no per-action signal, no device, no payment graph. **The correct posture is therefore prevention-heavy, detection-light, and remedy-based.** Any 12B text implying otherwise would be an overclaim that §26 and Report 08 §12.6 both forbid.

---

## 8. System B — multi-account abuse foundations

### 8.1 The approved position, restated because 12B must not drift from it

`D-018` already settled the policy half: one account per person; multiple accounts prohibited; enforcement proportionate and behavioural; rule-generated signals; review before action; a published ladder and appeals; no claim of perfect verification; no automated ban on a single signal; household members may each hold an account but must not share access or coordinate through one login. `D-032` settled the ownership model: an account owns 0..1 active nations, ownership is resolved from the session, and the system must not claim it can count the people behind an account. `REQ-043` is **Approved**.

Prompt 12A therefore has no policy decision to make. Its work is the enforcement, evidence, false-positive and appeal machinery `NET-040` deferred here — and the discipline not to imply the policy is stronger than `D-018` says it is.

### 8.2 Threat scenarios, evaluated against the mechanics rather than listed

| Scenario (brief §7.1) | Is it available in this game? | What actually blocks it |
|---|---|---|
<<<<<<< HEAD
| One player controlling several nations | **Yes**; common identity cannot be reliably established | Fresh-nation one-sided transfer rule (`ONB-031`/`ONB-032`), fair-value band (`MKT-144`), pair restrictions (`D-034`), value correction |
=======
| One player controlling several nations | **Yes**, and undetectable at identity | Fresh-nation one-sided transfer rule (`ONB-031`/`ONB-032`), fair-value band (`MKT-144`), pair restrictions (`D-034`), value correction |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
| Election or political manipulation | **Mostly no** | `DMP-185` excludes non-account candidacy; a second account cannot act inside one nation (`D-032`) |
| Alternates to bypass a restriction | Yes | `D-035` indirect-route rule; `CR-020` named ban-evasion offence |
| Secondary accounts feeding resources | Yes | `ECN` conservation, transfer-graph review, both-legs offences (`12A-RS-055`, `12A-RS-066`) |
| Manufacturing artificial demand | Yes post-gate | `MKT-097`/`MKT-098`; dormant until Global Trade releases |
| Market manipulation | Yes post-gate | Structure-and-intent definition (`12A-RS-071`) |
| Objective farming | Yes | Individual-equivalent objective rule (`DD-195`); completion keys |
| Ranking manipulation | Yes | Windowed measures (`11A-RK-002`); snapshot sealing; eligibility tests |
| Artificial event participation | Yes | Eligibility independence; participation records keyed per nation |
| Sanction evasion | Yes | `D-039` sanctions survive reroll; `NET-041` ban survives reroll; `CR-020` |
| Unauthorised diplomatic or military advantage | Yes | `D-030` intent opacity; `WAR` participation rules; response minimisation |
| Multiple accounts coordinating Alliance actions | **And that is legitimate** | `D-035` bank prohibition targets the evasion, not the coordination |

### 8.3 Legitimate multi-user handling

The brief §7.2 requirement — that a household, school, workplace or shared network is never assumed to be one player — is satisfied in this design by three independent mechanisms that already exist or are proposed:

1. `NET-039`'s approved ceiling: network evidence alone never supports anything above the lowest preventive tier. Reinforced by `12A-RS-034`, `12A-RS-049`, `12A-RS-057`, `12A-RS-058`.
2. A **proactive shared-context declaration** (`12A-CR-016`), modelled on Tribal Wars 2's pre-notification (`12A-RS-044`) and Wikipedia's declared-connection convention (`12A-RS-059`), scoped so that a declaration is *evidence for review* and never an unlock. This is the point where the `D-037` conflict had to be resolved rather than averaged: `D-037` forbids a standing co-resident exemption, and it remains exactly as written, because the declaration changes nothing about permissions. What it changes is the reviewer's information — a declared household is a different case from a discovered one, and can be triaged faster and decided more fairly.
3. `D-034`'s `LARGE` classification, which already refuses blanket restriction above 25 accounts on one key in 24 hours and requires a second observation. That is the right instinct; `12A-CR-012` keeps it keyed to accounts for enforcement purposes.

### 8.4 Detection signals, ranked by what they can actually support

| Signal | Ordinary behavioural correlation? | Strongest claim it can support |
|---|---|---|
| Repeated one-directional beneficial transfers | No — this is a **transactional** fact | Value correction; corroboration for a conduct finding |
| Circular flow sets across three or more nations | Weakly | Queue entry only; friendship and rings look alike (`12A-RS-063`) |
| Shared network digest | Yes, structurally (`12A-RS-034`) | Triage priority and review context. Never a finding |
| Similar schedules or similar build orders | Yes — the game causes it | Nothing |
| Coordinated timing against one shared reward | Moderate | Eligibility review; bright-line enforcement where the rule is published |
| Account creation clustering | Weak at this scale | Creation throttle, not accusation |
| Repeated circumvention patterns (`D-035` indirect routes) | No | Conduct finding when the legs are evidenced |
| Declared shared-context record | Not a signal at all | Review context, and a faster, fairer decision |
| Ban-evasion transition pattern | Moderate | Named evasion offence with its own evidence bar |

**No composite confidence score is proposed.** The brief §7.3 forbids one without an approved statistical methodology, and none exists: the reviewed collusion work supplies a *degree* score for triage and explicitly warns about false positives (`12A-RS-062`), and the fraud-graph practice states that the topology alone cannot separate friends from rings (`12A-RS-063`). `12A-CR-030` turns that into a prohibition on inventing one.

<<<<<<< HEAD
**What the identity limit does not excuse.** Inability to reliably establish that two accounts share one controller is not a finding that coordinated abuse is invisible. Behavioural evidence (matching schedules that the game itself causes, repeated circumvention patterns), transactional evidence (one-directional beneficial flows, circular flow sets, both legs of a transfer) and outcome evidence (conservation breaks, objective or ranking effects) can each support a named case and a least-harmful remedy. The residual is specifically about **proving common identity**, not about observing coordinated effects; a design that treated it as blanket immunity would fail §8.5's evidence requirements.

=======
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
### 8.5 Investigation and evidence requirements

A multi-account case may proceed only where: the rule breached is named; at least two independent evidence sources agree, at least one non-behavioural; the false-positive classes for those sources are recorded and considered; the reviewer declares no interest; and the outcome states which evidence state was reached, including *inconclusive*. The remedy selected must be the least culpability-bearing one that corrects the effect — value correction before restriction, restriction before suspension.

---

## 9. System C — collusion and coordinated manipulation

### 9.1 One sentence, not a list

The brief §8.2 requirement — that cooperation must not be reclassified as collusion — is best served by a single player-testable boundary rather than a catalogue of forbidden coordination. Report 08 already states it: players may cooperate, they may not manufacture false agents to exploit agent-counting rules. This report adopts that as the definition (`12A-CR-022`) and derives everything else from it: an alliance of forty independent nations is not collusion; forty nations voting as one while presenting as independent decision-makers is, **and the difference is a fact about agency, not about scale or similarity**.

That framing also explains why the corpus's existing integrity rules are already collusion rules in disguise: `D-035`'s indirect-route prohibition, `MKT-097`'s self-trade ban, `ALL`'s same-Alliance attack prohibition, `DMP-185`'s non-account candidacy and `WEP`'s individual-equivalent objective requirement each remove a payoff that manufactured agency would otherwise capture. 12B should build on them rather than alongside them.

### 9.2 What is protected, explicitly

The register lists protected behaviours positively (`12A-CR-021`) so that a future detector cannot quietly capture them: alliance military operations, joint diplomacy, economic agreements, coordinated defence, negotiated peace, officially permitted shared objectives, competitive market conduct including cartels where the market rules allow them (`MKT-159`), and strategic voting. Each is stated with the rule that makes it legitimate, so the protection is auditable rather than rhetorical.

### 9.3 Detection architecture and its lawful data basis

The brief §8.3 asks which data may be collected lawfully and which must remain private. Because the project refuses new collection (`12A-CR-033`), the honest answer is that collusion detection may use **only** data the game already writes for gameplay, account-security or a justified purpose — the ledger, reservations, treaty and alliance records, ballot structure, completion keys and the turn-state ledger. That constraint, which reads like a limitation, is actually the design's strength: it is what keeps the system outside the automated-profiling trigger of Art 35(3) (`12A-RS-086`) and is consistent with the DPIA-shaped argument that the *absence* of profiling supports.

Graph analysis is therefore an internal queue generator (`12A-CR-024`) whose output is a *reviewer's shortlist*, never a tier. Circular-flow and paired-flow indicators are computed from transaction structure (`12A-CR-023`) with the intent test supplied by the offence definition, mirroring the CFTC's structure-plus-intent drafting (`12A-RS-071`).

### 9.4 Threshold for a disciplinary action

Coordinated-abuse cases require the strictest corroboration in the corpus, because the innocent explanation — an alliance doing what alliances do — is always available. The proposed rule for 12B: a coordinated-manipulation finding needs (a) a demonstrated beneficial effect, (b) at least one independent non-behavioural evidence source, (c) explicit consideration and rejection of the legitimate-cooperation explanation recorded in the case, and (d) a named reviewer with no declared interest. Anything short of that is inconclusive, and `12A-CR-031` requires that outcome be written down rather than left open.

---

## 10. System D — privacy architecture

### 10.1 Position

Privacy here is not an account-registration concern; it is the ordering principle for the entire information architecture, because in a game about secrets — diplomatic intent, military readiness, alliance finances, investigation records — the visibility rules **are** gameplay rules. That is why the existing corpus already makes visibility decisions in B-02 (`TR-021`), B-03 (`DAT-001`), B-07 (`D-017`), B-08 (`D-030`), B-09 (`ALL-156`), B-10 (`WAR-148`–`151`) and B-11 (`WEP-647`–`WEP-654`), and why adding an eighth vocabulary would have been the wrong deliverable.

### 10.2 What the research changes

Four concrete shifts:

1. **The HMAC decision is validated and bounded at the same time.** The EDPB names keyed one-way functions such as MACs as suitable pseudonymising transformations and expressly prefers one-way functions (`12A-RS-092` ¶89), and its breach guidance treats a keyed hash with an uncompromised key as the example of an exposure that may not need notification (`12A-RS-093` ¶77). So `D-036` is sound. But Art 4(5)'s "kept separately" condition, the footnote's plain-hash matching attack, and the small size of the IPv4 and /64 space together mean the protection is entirely a function of **key custody and algorithm agility** — which the design states but has never specified as an auditable obligation. `12A-CR-043`, `12A-CR-044` and `12A-RK-030` close that.
2. **`k = 5` needs an inference argument attached to it.** A regulator states that pseudonymisation is not anonymisation, that k-anonymity's "main flaw is that it does not prevent any type of inference attack", and that shrinking the quasi-identifier set to raise apparent *k* is a named common mistake (`12A-RS-094`); the reviewed formulation makes the condition precise — *k* is a property of the quasi-identifier combinations actually released (`12A-RS-095`). `D-027` already forbids differencing, which is the main inference path, and `WEP-650` applies it to publication sets. What is missing is the per-aggregate enumeration of which fields count as quasi-identifiers. `12A-CR-039` supplies it.
3. **Retention needs justification, not numbers.** The supervisory guidance requires a policy, a justification, periodic review, and documented reasons where a decision goes the other way (`12A-RS-096`, `12A-RS-097`); nothing external prescribes a day count. `D-026` and `DAT-003` already provide the structure. The genuine unresolved item is a conflict, not a number: erasure versus a permanent spine (§10.4).
4. **The absence of profiling is doing legal work.** Art 35(3)(a) attaches the DPIA duty to systematic extensive evaluation *based on automated processing including profiling* with significant effects (`12A-RS-086`). The project's refusal to profile is therefore both the ethical posture Report 08 argued on its own terms and a defensible design position. Stating it that way strengthens the resistance to later pressure to add scoring.

### 10.3 Access principles

Least privilege is approved (`DAT-004`, `D-042`) along with the two sharpest sentences in the corpus: "Every privileged read of a restricted record is logged. The game does not have a 'see everything' idle role," and no permission for convenience. The research adds the structural distinction the design was missing — that **who may read a class** and **which flows between classes are permitted** are two separate rule sets (`12A-RS-116`, AC-3 versus AC-4). Without the second, a compliant-looking permission table still permits a diplomatic-confidential value to be *carried* into an alliance-restricted view by a correctly authorised reader. `12A-CR-038` requires both.

Emergency and service-to-service access are handled as their own cases rather than as exemptions: emergency access is enumerated, expiring and retrospectively reviewed (§18), and a service path that bypasses the policy — the documented `service_role` behaviour (`12A-RS-010`) — is treated as an authority boundary that must be specified, not as a trusted internal shortcut. `12A-OPEN-015` requires the corpus-wide sweep for sentences that currently imply RLS is the guarantee.

### 10.4 Boundaries, leakage and the unresolved conflicts

Leakage surfaces the corpus already covers partially, and where `12A-CR` closes the gap: API over-fetch (`CR-011`), error text (`CR-041`, `TR-023`), log content (`CR-089`: the fields the log *omits* are protective), aggregate disclosure (`CR-039`), notification content (`CR-040`, and B-08's `DPA-087` privacy test), Alliance financial data through moderation tooling (`CR-052`, and the roadmap's explicit prohibition), military values (`WEP-651` band-only, unchanged), investigation records (`DAT-009` summary-not-evidence, unchanged) and administrative confidentiality (`CR-091`).

Three conflicts are recorded as unresolved rather than resolved by preference:

- **Erasure versus the permanent audit spine.** `D-026` makes spine and class-P rows permanent; an erasure right, if a jurisdiction attaches, would reach them. `REQ-024` is already Open for exactly this. Carried as `UD-055`.
- **Availability versus the ₹0 constraint.** Art 32(1)(c) requires the ability to restore availability, and the regulator treats a permanent loss as an availability breach — while the free plan supplies no managed backups and no drill has been run (`12A-RS-083`, `12A-RS-093` ¶79; CF-02). `12A-CR-047` records the exposure as a disclosed limitation. It is not solved by wanting it to be.
- **Region choice versus transfer posture.** The vendor states that region selection is a data-location control and not proof of compliance (`12A-RS-106`), the strict residency tools are enterprise-gated (`12A-RS-112`), and **India — where `ap-south-1` actually is (`12A-RS-105`) — appears nowhere on the adequacy list** (`12A-RS-080`). Whether that matters depends entirely on the undecided jurisdiction (`UD-017`).

### 10.5 Data lifecycle

Collection (justified per element, `CR-042`) · processing (purpose-bound, `CR-037`) · storage (class-labelled, `CR-035`) · access (least privilege plus flow rules, `CR-038`) · sharing (default-off, `12A-RS-082` Art 25(2) "accessibility") · correction (append-only, `CR-092`) · retention (justified per class, `CR-045`) · deletion (obligation-recorded, `CR-067`) · anonymisation (never claimed for a pseudonymised value, `CR-043`) · backups (secret, rotated, availability-exposed, `CR-047`) · incidents (assessed and documented either way, `CR-094`).

---

## 11. Information classification: the authoritative foundation

### 11.1 The three-axis model

One model, three orthogonal axes, no field with two values on any axis. This is the reconciliation `12A-OPEN-001` assigns to 12B, and the recommended shape is stated here so 12B is not choosing from nothing.

| Axis | Question it answers | Values (already in the corpus) | Owner |
|---|---|---|---|
| **A. Handling class** | How must it be stored, transmitted, logged and read? | `Public` · `Private` · `Restricted` · `Secret` | `D-042`, `DAT-001` |
| **B. Subject visibility** | Who in the game may see it? | `PUBLIC` · `NATION_OWNER` · `PARTICIPANT` · `ALLIANCE_MEMBER` · `ALLIANCE_OFFICER` · `MODERATOR` · `ADMIN` · `INTERNAL` (as reconciled with `TR-021`'s four classes) | `WEP-647`, `TR-021`, `WEP-648` matrix |
| **C. Record purpose class** | Why does this record exist, and how long? | `S` summarised · `P` permanent · `O` operational (moderation and abuse evidence) · **audit spine** | `TR-090`, `D-026` |

The eleven candidate categories of brief §9.1 map onto this rather than replacing it, which is what §9.1's own instruction ("reconcile them with the existing architecture and create the authoritative classification only after evaluating the design") requires:

| IC | Candidate category from brief §9.1 | Axis A | Axis B (widest legitimate reader) | Axis C | Owning subsystem | Notes |
|---|---|---|---|---|---|---|
| `12A-IC-01` | Public game information | Public | `PUBLIC` | P | B-02, B-08, B-10, B-11 | Chronicle, declared acts, signed treaties, published standings |
| `12A-IC-02` | Player-private information | Private | `NATION_OWNER` | S/O | B-03 | Account settings, private notifications, session state |
| `12A-IC-03` | Nation-private information | Private | `NATION_OWNER` | S | B-04, B-05, B-06, B-10 | Treasury detail, pending orders, reserves, plans (`TR-020`) |
| `12A-IC-04` | Alliance-restricted information | Private/Restricted | `ALLIANCE_MEMBER`, `ALLIANCE_OFFICER` where scoped | S/O | B-09 | Membership, roles, tax reports, contribution history (`ALL-156`, `ALL-186`) |
| `12A-IC-05` | Diplomatic-confidential information | Private | `PARTICIPANT` only | P/S | B-08 | Pending proposals and terms are parties-only (`D-030`) |
| `12A-IC-06` | Military-confidential information | Private | `NATION_OWNER` | S | B-10 | Exact force values never leave the owner; publication is band-only (`WEP-651`) |
| `12A-IC-07` | Economic and transaction information | Private → Restricted | parties, then integrity role | P/S | B-04, B-07 | Terms parties-only (`D-017`); ledger rows become spine-visible |
| `12A-IC-08` | Moderation and investigation records | Restricted | `MODERATOR` | O | **B-12** | 12-month floor unless a case requires longer; summary-not-evidence (`DAT-009`) |
| `12A-IC-09` | Administrative and security records | Restricted | `ADMIN` | **spine** | B-12 with B-02 | Permanent; the class 12A is adding a definition for |
| `12A-IC-10` | Authentication and account-security information | Secret | `INTERNAL` only | S, bounded | Stage 6 | The game database must not hold plaintext; recovery secrets one-use |
| `12A-IC-11` | Sensitive personal information | Private/Secret | `INTERNAL`, purpose-bound | per class | B-03 | E-mail is the only personal datum the design retains; no ID, biometrics, address, phone or real name (`D-042`) |

Two categories the brief lists are **not** added as new classes because they are already fully owned elsewhere: economic *values* (B-04's conservation and ledger rules, not a privacy class) and *ranking information exposure* (handled as an axis-A and axis-B interaction under `12A-CR-039`, not a category).

## 12. System E — moderation foundations

### 12.1 A single taxonomy

`12A-CR-048` proposes fifteen categories covering the brief §10.1 list plus two that Nation Supremacy specifically needs and a generic list omits: **unauthorised API or backend access** as a named violation — a published operator policy in this genre already names "accessing game clients or backends in an unauthorized manner" (`12A-RS-042`) — and **undeclared real-value exchange**, which is the risk that converts an in-game economy into a regulated surface (`12A-RS-078`, `12A-RS-079`). Every category is a classification, not a penalty; brief §10.1's warning that a category must not conjure a sanction is discharged by `12A-CR-053`.

### 12.2 The ladder reconciliation problem

Two incompatible ladders exist in approved documents: Report 08 §12.3's six tiers (L0 educational … L5 most destructive) and `NET-038`'s levels 0–6 (seven tiers) with `NET-039` fixing the approved network-evidence ceiling at level 1. Later documents cite both. `12A-CR-049` requires 12B to publish exactly one ladder, with each tier stating who may impose it, its minimum evidence state from §6.4, its notice and its appeal route — and because tier **authority** touches owner-reserved questions (`OSQ-011` was never answered, and permanent termination is a serious irreversible measure), the choice is registered as `UD-053` rather than decided here.

The external evidence sharpens the shape without settling the number. Published ladders sit on a spectrum: Blizzard states progression only as a principle — "more serious and repeated violations will result in greater restrictions" (`12A-RS-126`); Riot states exact per-behaviour durations, "First offense: 3 day ban / Second offense: 14 day ban / Third offense: Permanent ban", plus a separate six-month suspension for duoing with a confirmed scripter (`12A-RS-124`); Niantic publishes a three-strike model **and** its carve-out in the same breath — "Offenders are not always offered three strikes. Some misbehaviors may result in immediate account termination without prior warning" (`12A-RS-125`). Three consequences follow for 12B:

1. **A ladder must publish its own escalation carve-out.** Otherwise immediate severe action becomes silent policy deviation, which is exactly the failure `D-018` forbids.
2. **Day counts are the wrong unit for this game.** With a two-hour cadence, tiers expressed in *turn boundaries*, *frozen features* and *season eligibility* are more honest than durations a single adjudicator cannot calibrate — and they survive a scheduler outage in a way "7 days" does not.
3. **At first playable there is no chat to restrict.** Bungie-style middle rungs assume a communication surface (`12A-RS-127`); Nation Supremacy's middle rung must be a **game-object** restriction — trading, posting an offer, objective entry, event eligibility, or a market or Alliance action — which is also more reversible and easier to audit. `12A-CR-052` already forbids moderation from editing another subsystem's state, so the restriction has to be modelled as an account-level capability flag, not as a data mutation.
4. **"Benefited from abuse" is its own tier.** Riot's duo penalty and Bungie's ban-wave language both punish gain without personal cheating (`12A-RS-124`, `12A-RS-128`), which is the conduct-lane analogue of the value-correction class in §6.5. 12B should carry it as a named, lower-culpability tier with a materiality threshold rather than folding it into the cheating ladder.

### 12.3 Severity, with the accusations rule honoured

`12A-CR-050` adopts the brief §10.2 factors and keeps the one prohibition that matters: prior **unconfirmed** accusations never count as priors. Report 08's two-lane design is preserved unchanged — the exploit and incident lane fixes and discloses without blame language and treats a first honest report as intelligence, while the conduct lane applies the ladder (`12A-CR-051`, `12A-RS-027` as external support).

### 12.4 Moderation is not game administration

The brief §10.4 authority-boundary model, expressed as the seven separations it asks for:

| Function | May | May not |
|---|---|---|
| Player support | Read the account's own state; initiate recovery | Read another account's private data; apply a sanction |
| Community moderation | Record a report; open a case; apply tiers within evidence | Decide a value effect another subsystem owns |
| Security investigation | Read restricted evidence with a purpose code | Edit any record; act on an unread signal |
| Game operations | Halt or resume a path; disclose a delay | Change an outcome; alter a snapshot |
| Financial administration | Trigger a correction with a reason code | Set a balance; mint a value (`ECN-213`) |
| Emergency administration | Apply a bounded, expiring restriction | Delete, confiscate, transfer or rewrite |
| All of the above | Be audited | Be unaudited, or audit-exempt |

`12A-CR-075` states the prohibition list positively, and the external case for doing so is `12A-RS-028`: the operator is an adversary candidate, and the incident demonstrated that the trust-based assumption fails exactly once and expensively.

---

## 13. Disciplinary principles

`12A-CR-053` holds that no penalty is approved because a category exists. What this pass can do is specify the **shape** a penalty specification must take, so that 12B's ladder is testable rather than expressive: each tier states the minimum evidence state from §6.4, the actor permitted to impose it, the notice text class, the end condition, the appeal route, whether it is reversible, and which subsystem's own path executes any state effect. The candidate measures listed in brief §10.3 are carried as candidates: warning, formal notice, communication restriction (which is near-vacuous at first playable, since there is no chat — a fact 12B should state rather than inherit silently), feature restriction, temporary suspension, value or activity correction, account suspension, and permanent termination.

Three principles worth arguing rather than asserting:

- **Reversibility is a property of the tier, not of the reviewer's mood.** `12A-CR-054` makes value correction always reversible and `12A-CR-085` makes permanent effects unreachable through the emergency path. This is what allows the game to act quickly under uncertainty without being unjust.
- **Sanctions attach to accounts, not nations.** `D-039` and `NET-041` already decide this, and `MKT-184` applies it in the market; `12A-CR-055` generalises it so that a reroll is never a reset. It is also the answer to the "secondary account to evade" case without needing any identity technology. Valve's rule that "any bans added to an account will remain regardless of who was using the account at the time" is the same doctrine stated by the largest comparable platform (`12A-RS-122`), which makes it a normalisable position rather than a harsh local one.
- **No significant enforcement decision may be solely automated.** GDPR Art. 22 gives a data subject the right not to be subject to a decision "based **solely** on automated processing… which produces legal effects concerning him or her or **similarly significantly affects** him or her", with at least the right to "obtain human intervention… to express his or her point of view and to contest the decision" (`12A-RS-134`). Whether a game account suspension "similarly significantly affects" is unverified in case law and depends on `UD-017`, so this is stated as a **design decision that is also a compliance posture**, not as a legal conclusion: `D-018` already forbids a punishment on one signal, and `12A-CR-027` now carries the external reason. For a game whose entire resolution model is server automation, this is the single highest-value control to keep, because it is also the one most likely to erode under volume pressure.

## 14. System F — reporting and evidence handling

### 14.1 Intake

Structured intake with a named category, subject, time window and free-text account, stored as an **accusation** (`12A-CR-059`), clustered against duplicates (`12A-CR-060`), with reporter-visible fairness and a false-report counter-rule that protects good-faith mistakes (`12A-CR-061`) and a confidential route plus an anti-retaliation offence for reports naming an administrator (`12A-CR-062`). Report 08's design is retained and strengthened on one point: P&W's published rule that "screenshots alone will not be considered sufficient evidence" (`12A-RS-050`) supplies the external corroboration for what was previously an internal intuition, and `12A-CR-063` states the general rule — player evidence is a **pointer** to be corroborated against server records, never the finding.

### 14.2 Investigation

Case record with the evidence examined, the rules relied on, the reviewer, the decision, the date and the outcome including *inconclusive* (`12A-CR-031`); conflict-of-interest detection with honest labelling when staffing cannot segregate (`12A-CR-032`); reopening only on new evidence (`12A-CR-071`); and a documented review-outcome statistic as the only realistic false-positive instrument at this scale (`12A-CR-104`).

### 14.3 Evidence integrity

Provenance, producer and recording time for every artefact (`12A-CR-064`); a chain of custody in which access, annotation, correction and export are themselves events (`12A-CR-065`); conflict handling where two records disagree (`12A-CR-069`); obligation-driven deletion recorded as a redaction event with its authority (`12A-CR-067`); and case-scoped minimisation so that evidence never leaks into operational logs or a support tool's default view (`12A-CR-068`).

The uncomfortable finding here is `12A-RK-026` and `12A-CR-066`: **the project's audit spine is not currently tamper-evident.** In the applied prototype the `audit` table has no protective trigger and `DELETE` is revoked only from the `authenticated` role, leaving the owner and service paths unrestricted (`0001_schema.sql:47-54`, `0003_grants_and_rls.sql:15`), and RLS is forced on the ledger tables without any policy that would deny an authorised-role rewrite. The vendor model for actual tamper-*evidence* — chained SHA-256 digests with signatures, and a separate, explicitly-performed validation step — is documented and states its own caveat that enabling validation does not validate (`12A-RS-029`). Append-only by convention is not evidence. This is a Stage 5 build obligation, recorded as a confirmed weakness, and it is the single most important technical prerequisite for every accountability claim B-12 will make.

## 15. System G — appeals and dispute resolution

The approved minimum is already fixed and is not re-opened: one appeal, stated grounds, the action stays in force pending the decision, a written reasoned outcome, reopening only on genuinely new evidence, false-positive correction with reversal, and review by a different reviewer "where possible" described honestly as "a process standard, not a claim of independent adjudication" (`NET-044`–`NET-047`).

Four things this pass adds.

**A disclosure rule with a stated boundary.** Players must learn enough to contest; detection method and third-party private data must not be disclosed. Both halves now have external support: the operator-side reason for secrecy is stated on the record twice (`12A-RS-013`, `12A-RS-067`), Valve states the same position while also stating that it keeps complete internal records (`12A-RS-123`), and the DSA frames the obligation as a **"clear and specific statement of reasons"** delivered "at the latest from the date that the restriction is imposed, regardless of why or how it was imposed" (`12A-RS-133`). Read together with `NET-048` and `DAT-009`, the design conclusion is precise and cheap: **the notice is a projection of the enforcement record, not a document someone writes afterwards.** `12A-CR-058` therefore states notice content as a property of the record, and `12A-CR-072` bounds it by rule rather than by reviewer discretion.

**A reversal duty that does not depend on the player asking.** Valve's VAC design has no appeal at all, yet commits that an incorrectly issued ban "will automatically be removed" after investigation (`12A-RS-121`). The appeal-exclusion half is incompatible with `NET-044` and with any plausible EU-facing obligation, but the **duty** half is exactly what `NET-046`'s new-evidence reopening needs to become: a standing obligation on the operator, not only a right on the player. `12A-CR-071` is extended accordingly in `12A-DR-026`.

**A bounded appeal budget.** Jagex publishes two appeals per offence and Epic one per sanction, each with categories that are not appealable (`12A-RS-129`, `12A-RS-132`). That converts `UD-059` from an open-ended question into a bounded one: 12B should choose a small integer, publish the non-appealable categories, and keep the new-evidence reopening outside the budget so the cap cannot trap an unjust decision. The number is the owner's; the shape is now evidenced.

**Independence honesty.** `12A-CR-074` requires the record to show when a review could not be segregated. A one-operator service that claims independent adjudication is making a false statement; one that labels the limitation is making a defensible one. The corresponding owner question — what staffing model the project is actually committing to — is `UD-054`, and it is genuinely outside AI authority because it is a resourcing decision (`OSQ-005`, `OSQ-012` were never answered).

Appeal limits, deadlines, reversal mechanics and administrative-appeal boundaries are deliberately **not** proposed here. Brief §12.2 lists them as owner-dependent, and inventing a number would create an approval that nobody granted.

## 16. System H — administrative roles and authority

### 16.1 Candidate roles, evaluated rather than assumed

The brief §13.1 asks whether all eight candidate roles are necessary. They are not, and the honest answer depends on staffing that `UD-054` reserves.

| Candidate role | Recommended at launch | Reason |
|---|---|---|
| Community moderator | **Merged into the operator** | No volume to separate |
| Support operator | **Yes, as a scoped permission set** | Recovery and account questions are the highest-volume real need (`D-041`) |
| Security investigator | **Yes, as a separate permission, not a separate person** | The permission split is what survives a single holder and constrains growth |
| Senior moderator | **No** | Meaningless at one operator; would be a title, not a control |
| Game administrator | **Split by prohibition list, not by title** | A "game admin" who can edit outcomes is precisely the `12A-RS-028` case |
| Financial operations administrator | **Deferred; `UD-046` and `UD-045` boundaries apply** | Alliance treasury authority is owner-reserved |
| System operator | **Yes, technically distinct** | Deploy and configuration duties already exist |
| Emergency authority | **Yes, as an expiring capability, not a role** | §18 |

The recommendation to 12B is therefore **four permission sets and one person**, with the note that the split is designed so a second person can be added without redesign — which is Report 08's `OSQ-012` compensation strategy expressed as a structure.

### 16.2 Least privilege, step-up and the read audit

`12A-CR-076` forbids the superuser, which `DAT-004` already rules out and `UD-045`'s recorded ban on granting beyond one's own rights reinforces. `12A-CR-077` adopts privileged step-up and shorter, separately-revocable privileged sessions — the recommendation Report 08 made in `OSQ-002` and nobody ever decided — while leaving the **mechanism level** open, because the provider capability and cost at ₹0 are unmeasured (`12A-OPEN-004`).

`12A-CR-078` is the requirement with the widest reach: privileged **reads** must be auditable. Four separate documents already demand it (`NET-051`/`NET-052`, `DIP-121`, the `DPE-054` residual, `WEG-04`) and none owns it; a Supabase-side contract even defines a security incident to include "unauthorized internal access" (`12A-RS-108`). An operator who can read any investigation file without trace makes the entire accountability model decorative.

The control catalogue now names these obligations precisely. NIST SP 800-53 Rev. 5, read from the official OSCAL catalogue, states AC-5 as requiring documented separation of duties and access authorisations defined "to support separation of duties", AC-6 as the least-privilege rule, **AC-6(9) "Log the execution of privileged functions"**, AU-3's mandatory record fields (originator identity, event type, time stamp, source and destination objects, outcome), AU-9's duty to "protect audit information and audit logging tools from unauthorized access, modification, and deletion" **and to alert upon detection**, with AU-9(3) cryptographic protection, AU-9(4) access by a subset of privileged users, AU-9(5) dual authorisation and AU-9(6) read-only access (`12A-RS-140`). Three consequences: `12A-CR-088`'s event set should map to AU-3's field list so the shape is defensible rather than invented; `12A-CR-066`'s tamper evidence is AU-9 plus AU-9(3); and **AU-9(5) dual authorisation is the named substitute** for the separations one person cannot perform, which is exactly the gap `12A-CR-083` requires be declared rather than disguised. CISA's zero-trust guidance supplies the equally plain default: "removing implicit trust (allow by default) and replacing it with explicit verification (**deny by default**)" (`12A-RS-147`) — which is also why an unrecognised sanction code must resolve to "no action plus a review flag", never to an automatic penalty.

## 17. Separation of duties

Brief §13.3 lists six splits. At one operator, four can be implemented as **permission separation with a disclosure substitute**, and two cannot be implemented at all, which must be said plainly rather than papered over.

| Split | Implementable now? | Design position |
|---|---|---|
| Investigation versus final enforcement | As permissions | `12A-CR-080`; the same person holding both is disclosed in the case record |
| Evidence creation versus evidence approval | Partially | Automatic capture is unauthored; a reviewer cannot author the record they judge (`12A-CR-065`) |
| Financial correction versus authorisation | Yes, by routing | The owning subsystem computes; the reason code is the authorisation (`12A-CR-082`) |
| Suspension versus appeal review | Only nominally | `NET-045` already labels this a standard, not a guarantee |
| Configuration versus publication | **Gap** | `WEG-05` registered it; `12A-CR-081` requires either a second approver or a disclosed compensating control |
| Emergency access versus retrospective review | Yes | `12A-CR-086` |

`12A-CR-083` states the meta-rule: an unimplementable split is declared a control gap with its substitute, never described as a separation of duties.

## 18. Emergency administration

Four rules, derived from brief §13.6 and the project's own disclosed-outage precedent (`D-025`, `D-022`): enumerated capabilities; scope and expiry expressed **in turn boundaries** rather than an unpinned duration, so an expiry cannot survive a scheduler outage (`12A-CR-084`); reversible measures only, with permanent effects requiring the ordinary path (`12A-CR-085`); and mandatory retrospective review with a recorded outcome whether or not the action is reversed (`12A-CR-086`).

`12A-CR-087` adds the disclosure half, which is where most emergency designs quietly fail: players are told a temporary measure is in force and when it will be reviewed, without the notice teaching anyone what triggers it. Silent emergency intervention is not permitted, consistent with `SEC-022` and `TR-023`.

## 19. Auditability and accountability

`12A-CR-088` consolidates eleven event classes the corpus currently demands in nine different places but never defines as a set — privileged login and access, permission changes, investigation and evidence reads, moderation and disciplinary actions, appeal outcomes, administrative overrides, emergency actions, financial corrections and configuration publication. It also names the two existing event families that already partly cover this (`AUD-AL-###` shape owned by B-09 through `AX-21`; `WPA-42`/`43`/`45`/`50` in B-11) so that 12B extends rather than duplicates.

Three design obligations make the set worth having: the content rule (`12A-CR-089` — identifiers, decisions and reasons, never content bodies or secrets), the anti-quota rule (`12A-CR-090` — integrity logging is never sampled away below value, pipeline or privileged rows; Report 08 §15.2 already states this and CF-01 is the pressure that will test it), and the readership rule (`12A-CR-091` — audit access is itself restricted, purpose-bound and logged).

Ordinary application logs do not satisfy accountability, and the brief §13.5 is right to say so. The difference is precisely `12A-CR-066`: an append-only spine with **chained digests and a scheduled verification job whose failure is loud**. Without the verification step the chain is a claim — the vendor that built the model states plainly that enabling validation does not validate, and that checking is a separate action someone must take (`12A-RS-142`).

Two extensions the research makes available and that 12B should weigh, because both are cheap and both attack the one-operator problem directly:

- **Make the root observable, not merely checkable.** Certificate Transparency's mechanism is "**publicly auditable, append-only, untrusted logs**" (`12A-RS-143`), and its force comes from outsiders being able to check without trusting the operator. A periodic published signed root over the audit and enforcement tables — one hash per season, published as a class-P record — gives Nation Supremacy the same property at almost no cost, and RFC 3161-style external timestamping can anchor it if a third party is ever acceptable (`12A-RS-144`). Because it is a *publication* decision, it is routed to `UD-058` rather than assumed.
- **Document custody, and accept selective recording.** NIST SP 800-86 defines forensic readiness as identifying, collecting, examining and analysing data "while preserving the integrity of the information and maintaining a strict **chain of custody**", warns that electronic records "can be altered or otherwise manipulated" so an organisation must be prepared to **demonstrate** their integrity, and expressly accepts that "although it may not be feasible to record every event… having a record of the major events and actions taken helps ensure that nothing has been overlooked" (`12A-RS-149`). That last clause is the external warrant for `12A-CR-090`'s tiering rule — high-volume rows may be sampled, integrity rows may not — which means the quota pressure is not an excuse but a recognised engineering trade-off, provided the boundary is drawn deliberately.

Finally, `12A-RS-148` and `12A-RS-141` supply the two operational disciplines Report 08 left implicit: fail mode must be an **enumerated per-control choice**, and an elevated emergency capability should be dormant by default, **alert on every use**, be tested periodically ("at least every 90 days"), and require a **post-use review of whether the use was authorised**. The first becomes `12A-CR-099` and the fifteen `12A-FR-##` rows; the second becomes `12A-CR-084`–`12A-CR-087`.

## 20. Cross-system dependencies

The full matrix — thirty rows, twelve fields each — is `12A-INT-01`…`12A-INT-30` in the register. Three structural points are worth stating here because they determine whether B-12 can be built without breaking something.

**Ownership is already assigned, and B-12's slice is narrow but load-bearing.** Economy state belongs to B-04, political state to B-06, market rules to B-07, treaty objects to B-08, Alliance objects to B-09, warfare to B-10, and events, objectives, standings and progression to B-11. Each of them already published its own integrity obligation — `MKT-157` signals, `WEP-640` manipulation scenarios, `WAR-148`–`151` visibility rows, `ALL-158` no-officer-suspension, `DMP-267` political-state-is-not-a-sanction. B-12's own categories are the **evidence state model, the ladder, the case and appeal record, the access and flow rules, the audit event set, and enforcement against accounts**. `12A-CR-096` and `12A-CR-097` make that boundary a requirement, which is how the brief's fear of a "universal controller" is actually prevented — by a rule, not by an intention.

**Four deferrals point here and must be disposed of by 12B explicitly:** `DPE-049` (operator correction), `DPE-054` (privileged-read audit), `REQ-674` (DEFERRED — warfare fair play), and `AX-23` (Deferred to Prompt 12 — Alliance conduct moderation), plus `WEG-02`, `WEG-04`, `WEG-05`, `WEG-06` from B-11 and `GAP-13`/`WCR-33`/`WCR-44` from warfare. Anything that does not close one of these is scope creep.

**Global Trade gate G-1 is the one place where 12A's output blocks another subsystem's release.** The 07C companion records G-1 as **NOT MET** because the multi-account and shared-network incident-rate tolerance band is not defined anywhere. `12A-CR-015`, `12A-CR-016` and `12A-CR-029` supply its inputs, and `12A-INT-25` records the dependency; the band value itself is Prompt 12B's with owner sign-off, and no 12A text may imply the gate has moved.

## 21. Security threat model

Thirty-two rows with eighteen fields each in `12A-RK-001`…`12A-RK-032`, scored on Report 08 §2.2's ordinal bands with a stated basis and classified by evidence strength (`CONFIRMED` / `PLAUSIBLE` / `RESEARCH` / `HYPOTHETICAL` / `IMPL`) exactly as brief §17 requires.

**The confirmed items, which is where attention belongs:** `RK-007` the player-writable profile treasury column (Critical band, open today, correction exists only in bytecode); `RK-024` untraceable privileged reads (registered in three places, owned nowhere); `RK-026` the audit spine is append-only by convention with no digest chain or verification job; and `RK-031` the unrecoverable-loss exposure with no drill behind it.

<<<<<<< HEAD
**The accepted residual:** `RK-027`, identity-layer multi-accounting cannot be reliably detected under the current fixed constraints, rated L5 by the Sybil negative results and disclosed as the honest ceiling rather than treated as a gap to be closed later by some better detector. The limit is on reliably establishing common identity, not on using behavioural, transactional or outcome evidence against coordinated abuse (§8.4–§8.5). Any 12B sentence implying either a reliable identity detector or blanket undetectability must be refused.
=======
**The accepted residual:** `RK-027`, undetectable multi-accounting at the identity layer, rated L5 by the Sybil negative results and disclosed as the honest ceiling rather than treated as a gap to be closed later by some better detector. Any 12B sentence implying otherwise must be refused.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

**The compound case:** `RK-032` exists because the brief §17 is right that cross-system consequence is the distinctive risk here. One resource-creation defect propagates through the market into an Alliance tax base, an event eligibility band, a standing and a permanent honour — and each subsystem's own check passes while the chain is illegitimate. Its mitigation is not a detector but B-04's conservation identities C1–C4 evaluated across the chain, plus staged reversal, which is why `12A-OPEN-013` assigns the ordering to Prompt 12C and Prompt 14 rather than pretending it is settled.

## 22. Failure and recovery foundations

Fifteen postures in `12A-FR-01`…`12A-FR-15`, and the point of the register is that **no single answer is correct**. Value-moving, authorising and audit-writing paths fail closed with the transaction; a failed detection service degrades without blocking play, because a missed signal is recoverable and a halted world is not; a corrupt investigation record makes the case inconclusive rather than proven, because absent evidence must not become adverse evidence; an emergency measure expires by default; and an account-association error fails open toward the least-harmful reading, because a wrongful restriction damages a person while a missed link damages only a case.

Availability versus integrity is resolved the same way the corpus already resolves a failed turn: the world waits rather than skipping (`D-025`). Restoring from a stale point is worse than a disclosed hole (`12A-RK-031`, `12A-FR-15`), and Report 08's statement that there is "no admissible exception to 'no silent correction'" is preserved as `12A-CR-092` and `12A-CR-089`.

---

## 23. Requirements overview

106 candidate requirements in 20 categories, each carrying all fifteen fields of brief §15.2 across the two linked halves of the register. Computed distribution: Stage A **49**, Stage B **55**, Stage C **2**; `Restates approved policy` **46**, `New proposal` **46**, `New proposal, closes a registered gap` **11**, `extends` **2**, `consolidates` **1**; **20** rows carry an explicit owner or legal dependency, **5** are assigned to a named downstream stage or prompt, **81** sit within 12B's own authority. Sixty-one cite at least one external source identifier.

**No global `REQ-` identifier is allocated.** `REQ-763` remains the frontier and `REQ-764` is reserved for Prompt 12B's conversion, exactly as `11A-CR` → `REQ-704` and the `DD-193` precedent provide. §6.2 of the register lists the fourteen existing rows each candidate overlaps, so 12B extends rather than duplicates; §6.1 records the twenty-two candidates rejected for failing necessity or atomicity, which is the evidence that the count was not inflated.

Four requirement clusters matter more than the rest and should be read first by anyone with limited time: the source-of-truth and single-writer cluster (`CR-001`…`CR-006`, `CR-010`); the evidence-state and corroboration cluster (`CR-003`, `CR-004`, `CR-027`, `CR-028`, `CR-030`, `CR-063`); the value-versus-conduct cluster (`CR-018`, `CR-019`, `CR-054`, `CR-085`); and the auditability cluster (`CR-066`, `CR-078`, `CR-088`…`CR-092`).

## 24. Design decisions recorded by Prompt 12A

Fifteen ordinary Category B design positions were recorded autonomously under `D-014`, as **D-163 … D-177** in [DECISIONS.md](../../DECISIONS.md) and mirrored as **DD-211 … DD-225** in the [04 register](../04_approved_and_provisional_decisions.md). Each is at the **research and design-foundations level**: none approves a rule, a number, a penalty, a permission table or an implementation.

| D / DD | Subject | Position adopted | Principal evidence |
|---|---|---|---|
| `D-163` / `DD-211` | Prompt 12 execution split and paths | 12A research → 12B specification → 12C workflows; 12A artefacts under `research/12A_*`; B-12's rulebook reserved at `20_fair_play_and_player_protection.md` because `19_` is taken by the B-11 companion | 07A–11C convention; outline §"File numbering" |
| `D-164` / `DD-212` | Identifier policy | `12A-RS/BM/CMP/DR/CR/INT/RK/FR/OPEN`; no `12A-DEC` register; no global `REQ-`; candidates convert in 12B | `DD-193` precedent; `03` maintenance rule 5 |
| `D-165` / `DD-213` | Value correction versus conduct sanction | Two distinct enforcement classes with different evidence bars, reversibility and appeal rights | `12A-RS-018`, `12A-RS-052`, `12A-RS-066`, `12A-RS-055` |
| `D-166` / `DD-214` | Anti-cheat architecture for a clientless game | Server authority, transactional invariants and response minimisation are the control; attestation, fingerprinting and paid bot scoring are unavailable and may not be implied | `12A-RS-001`, `12A-RS-040`, `12A-RS-041`, `12A-RS-053` |
| `D-167` / `DD-215` | Five evidence states | Suspicion indicator · policy signal · corroborated evidence · established violation · inconclusive, each with a permitted consequence set | Brief §6.3, §11.1; Report 08 §13.3 |
| `D-168` / `DD-216` | Network evidence demotion | Account-keyed counters; network attribute is triage only; `NET-039` confirmed rather than amended | `12A-RS-034`, `12A-RS-049`, `12A-RS-057`, `12A-RS-007` |
| `D-169` / `DD-217` | Declared shared-context record | An attested declaration feeds review and unlocks nothing; `D-037` preserved verbatim | `12A-RS-044`, `12A-RS-059`; `D-033`, `D-037` |
| `D-170` / `DD-218` | Collusion boundary | One test — manufactured false agency; scale and behavioural similarity are excluded as indicators | Report 08 §8.5; `12A-RS-079`, `12A-RS-063` |
| `D-171` / `DD-219` | Three-axis information classification | Handling class · subject visibility · record purpose class, with a reconciliation duty and no fourth vocabulary | `D-042`, `TR-021`, `TR-090`, `WEP-647`; `12A-RS-116`, `12A-RS-117` |
| `D-172` / `DD-220` | Outcome-and-flow offence drafting | Abuse defined on transfers and effects, both legs accountable, never on proving control | `12A-RS-050`, `12A-RS-055`, `12A-RS-066`, `D-035` |
| `D-173` / `DD-221` | Administrative authority by prohibition | Four permission sets and one person; the prohibition list is the control; a privileged read is an event | `DAT-004`, `D-042`; `12A-RS-028`; `WEG-04` |
| `D-174` / `DD-222` | Tamper-evident spine | Chained digests plus a scheduled verification job whose failure escalates; append-only convention is insufficient | `12A-RS-029`; verified prototype inspection |
| `D-175` / `DD-223` | Differentiated failure postures | One posture per risk category; no global fail-open or fail-closed answer | Brief §18; `D-025`; `SEC-022` |
<<<<<<< HEAD
| `D-176` / `DD-224` | Accepted critical residual | Identity-layer multi-accounting cannot be reliably detected under the current fixed constraints, and the design says so | `12A-RS-060`, `12A-RS-061`, `12A-RS-051` |
=======
| `D-176` / `DD-224` | Accepted critical residual | Identity-layer multi-accounting is not detectable under the fixed constraints, and the design says so | `12A-RS-060`, `12A-RS-061`, `12A-RS-051` |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
| `D-177` / `DD-225` | Prevention-heavy, remedy-based posture | Make abuse unprofitable and reversible before attempting to detect it, at one-operator scale | `12A-RS-019`, `12A-RS-051`, `12A-RS-026`-class |

## 25. Unresolved owner decisions

Nine new rows are opened in the [05 register](../05_unresolved_design_decisions.md) as **UD-052 … UD-060**, every one of them `Open`, none resolved by inference, and each traceable to a specific unfilled `OSQ-` row from Stage-1 Report 08 or to a conflict the research exposed:

| UD | Question | Class | Owner approval | Origin |
|---|---|---|---|---|
| `UD-052` | May a value correction reach an account other than the one that received the value, and both legs of a flow? | B | **Yes — owner** | `12A-RS-066`, `12A-RS-055`; a fairness boundary, not a design choice |
| `UD-053` | What is the single ladder, and who may exercise its top tiers including permanent termination? | B | **Yes — owner** | `OSQ-011` unanswered; Report 08 §12.3 versus `NET-038` |
| `UD-054` | What moderation staffing and review-independence model is actually committed? | B | **Yes — owner** | `OSQ-005`, `OSQ-012`; `NET-045` |
| `UD-055` | How is enforcement evidence retained and erased against a permanent audit spine? | E | **Yes — legal** | `12A-RS-087`; `REQ-024` Open |
| `UD-056` | Who may invoke emergency authority, for how long, reviewed by whom? | B | **Yes — owner** | Brief §13.6; irreversible-effect risk |
| `UD-057` | What is the automation policy shape — permitted-behaviour list or prohibition list? | B | **Yes — owner** | `OSQ-004` never answered |
| `UD-058` | How much enforcement history, if any, becomes public? | B | **Yes — owner** | `OSQ-006`; `NET-050` |
| `UD-059` | What are the appeal limits, deadlines and review authority? | B | **Yes — owner** | Brief §12.2; `NET-044` leaves them open |
| `UD-060` | What age assurance is possible without the documents the design refuses? | E | **Yes — legal** | `12A-RS-099`, `12A-RS-100`, `12A-RS-102`; B-03 §1.3 assigns it to the owner |

`UD-017`, `UD-040`–`UD-049`, `UD-050` and `UD-051` are unchanged, still `Open`, and still owner- or evidence-reserved. `UD-044` is untouched and the boundary is enforced by `12A-CR-098`: platform moderation is distinct from an Alliance expulsion, and 12A creates no Alliance appeal right.

Register arithmetic after this pass: **60** rows, **28 Resolved / 3 Deferred / 29 Open**; the **32** non-resolved rows split by primary class A **0**, B **18**, C **8**, D **2**, E **4**. The 05 register's §6 inventory wording is corrected to these figures in the same pass, because it had drifted to a stale "22 non-resolved / 4 Deferred / 18 Open" statement predating the B-11 rows.

## 26. Legal and operational dependencies

Nothing in this deliverable is legal advice, and no jurisdiction is assumed. The separation brief §19 requires is applied as follows:

| Kind | Examples from this pass | Status |
|---|---|---|
| **Design principle** | Do not collect it; default-off disclosure; purpose-bound reads; pseudonymise and keep the key separate | Voluntary, and the strongest available artefact if a regime is later chosen |
| **Legal requirement, conditional on a jurisdiction decision** | Art 5(1)(c)/(e)/(f), 5(2), 17, 20, 21, 22, 25, 30, 32(1)(c), 33(1)/(5), 35(3), 44/46 of the GDPR; COPPA's directed-to and actual-knowledge limbs; the UK code's 15 standards; DSA Arts. 15, 16, 17, 20 and 21 | Cited with the article numbering read and cross-corroborated (§1.5 of the sources register); **applicability is `UD-017`**. The DSA duties — a statement of reasons at the time of restriction, a free internal complaint channel for at least six months, access to a certified **non-binding** out-of-court body, and annual machine-readable reporting — are structurally what 12B needs anyway, and all four are generable from the audit spine (`12A-RS-133`) |
| **Standard or catalogue** | OWASP Top 10 Web and API, ASVS 5, RFC 9110, RFC 6962, RFC 3161, NIST SP 800-53 Rev. 5 AC/AU families, SP 800-60 method, SP 800-61r2, SP 800-86, CISA zero-trust guidance, ISO/IEC 27035-1 phase names, ISO/IEC 27001 versus 27002 | Voluntary; 27001 is certifiable and 27002 is guidance, so no conformance claim is made and no paywalled clause wording is quoted (`12A-RS-119`, `12A-RS-140`, `12A-RS-146`) |
| **Platform rule** | Apple 5.1.1(v), Google Play account-deletion and web-link resource | Binds the **distribution channel**; not applicable to a browser-only service today, recorded as a conditional future duty |
| **Voluntary best practice** | Publish counts, undisclosed detectors, self-report mitigation, evidence bars | Adopted where consistent with `D-018` |
| **Unapproved operational policy** | The ladder, staffing, emergency authority, transparency scope | Owner-reserved: `UD-053`, `UD-054`, `UD-056`, `UD-058`, `UD-059` |

<<<<<<< HEAD
Three premise corrections from Register E belong here because they change what the project must **not** assume (`12A-RS-135`…`12A-RS-139`): the Italian AGCM action against Blizzard is an **investigation opened in January 2026**, not a concluded fine; the EA-Italy matter **closed with accepted commitments and no infringement found**, and the €10 m loot-box action was **Dutch** and was **overturned on appeal** by the Council of State in 2022; the live US action, filed 2026-02-25, targets **item-trading economies** rather than moderation. A later development is added as `12A-RS-153`: on **8 October 2026** AGCM announced that it is the lead authority, with the consumer-protection authorities of Norway and Denmark, in a coordinated Consumer Protection Cooperation action against Activision Blizzard UK Limited and other Microsoft group companies concerning transparency and fairness in in-game virtual currencies, purchases through multiple currencies and bundles, dark patterns, inadequate parental controls and a lack of assistance when accounts are blocked. That action **seeks to establish whether a "widespread infringement" has occurred; it is not a final finding**, and its relevance to Nation Supremacy depends on the actual product, monetisation model, player population and applicable jurisdictions. It creates **no automatic legal obligation** and leaves `UD-017` with the owner and legal counsel. The design consequence is a hard separation: **conduct moderation** is B-12's subject, while **item-economy, monetisation and consumer-protection exposure** is a distinct legal surface owned by the owner and counsel under `UD-017`. A rulebook that treated them as one topic would mis-scope both — and `12A-CR-048` therefore names undeclared real-value exchange as a conduct category without claiming any regulatory conclusion about it.
=======
Three premise corrections from Register E belong here because they change what the project must **not** assume (`12A-RS-135`…`12A-RS-139`): the Italian AGCM action against Blizzard is an **investigation opened in January 2026**, not a concluded fine; the EA-Italy matter **closed with accepted commitments and no infringement found**, and the €10 m loot-box action was **Dutch** and was **overturned on appeal** by the Council of State in 2022; the live US action, filed 2026-02-25, targets **item-trading economies** rather than moderation. The design consequence is a hard separation: **conduct moderation** is B-12's subject, while **item-economy, monetisation and consumer-protection exposure** is a distinct legal surface owned by the owner and counsel under `UD-017`. A rulebook that treated them as one topic would mis-scope both — and `12A-CR-048` therefore names undeclared real-value exchange as a conduct category without claiming any regulatory conclusion about it.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

Twelve questions require a qualified legal review before any of the conditional rows can become obligations; they are enumerated in the sources register's binding-versus-guidance section and routed to `UD-017`, `UD-055` and `UD-060`. One deserves isolating because it changes an artefact rather than a document: **is an IP-address HMAC digest personal data in this operator's hands**, under Recital 26's "means reasonably likely to be used" test and Art. 4(5)'s "kept separately" condition (`12A-RS-089`…`12A-RS-091`, `12A-RS-103`)? The design already behaves as though the answer is "reduced, not eliminated"; `UD-017` and `12A-OPEN-002` keep that judgement on the record instead of buried in an implementation note.

Operational carry-forwards unchanged: CF-01 capacity target, CF-02 backup and restore drill, CF-03 twelve boundaries, CF-04 Supabase Auth end-to-end, CF-06 true concurrency, CF-08 runbooks. **None is reported as passed.**

## 27. Recommendations for Prompt 12B

Thirty-two recommendations, `12A-DR-001` … `12A-DR-032`. A recommendation is a direction supported by evidence, not an approved rule; 12B adopts, adapts or rejects each with a recorded reason. `12A-DR-025`…`12A-DR-032` come from Register E.

| DR | Recommendation | Principal evidence | Rejected alternative | Owner or downstream dependency |
|---|---|---|---|---|
| `12A-DR-001` | Publish a source-of-truth table per protected value and forbid a second writer path | `12A-RS-001`, `12A-RS-010`; `RK-007` | A general "server is authoritative" sentence | — |
| `12A-DR-002` | Make response minimisation a first-class requirement rather than a display concern | `12A-RS-040`, `12A-RS-041` | Detecting readers of leaked state | — |
| `12A-DR-003` | Adopt the two-class enforcement model with separate evidence bars | `12A-RS-018`, `12A-RS-052`, `12A-RS-066` | One ladder for every outcome | `UD-052` for reach |
| `12A-DR-004` | Adopt the five evidence states verbatim as the corpus's only evidence vocabulary | Brief §6.3, §11.1; Report 08 §13.3 | Three labels; numeric confidence | — |
| `12A-DR-005` | Reconcile the two ladders into exactly one, published, with tier authority named | Report 08 §12.3 versus `NET-038` | Keeping both | `UD-053` |
| `12A-DR-006` | Key every counter and restriction to the account; demote network data to triage | `12A-RS-034`, `12A-RS-007` | Per-IP rate policy | — |
| `12A-DR-007` | Introduce the shared-context declaration without any exemption semantics | `12A-RS-044`, `12A-RS-059` | Paid or automatic exemption (`12A-RS-047`) | — |
| `12A-DR-008` | Draft multi-account and collusion offences as flow offences | `12A-RS-050`, `12A-RS-055`, `D-035` | Identity-proof offences | `UD-052` |
| `12A-DR-009` | State manufactured false agency as the single collusion test | Report 08 §8.5; `12A-RS-079` | A catalogue of forbidden cooperation | — |
| `12A-DR-010` | Use bright-line eligibility and reward-velocity rules wherever a rank or key exists | `12A-RS-051`, `12A-RS-052` | Broad behavioural policing | — |
| `12A-DR-011` | Route election and collective-action abuse to mechanism design and balance first | `12A-RS-065`; `DMP-185` | A voting-integrity detector | Prompt 14 |
| `12A-DR-012` | Publish rules, consequences and evidence standards; keep detectors undisclosed | `12A-RS-013`, `12A-RS-067`, `12A-RS-050` | Full method disclosure, or none | `UD-058` for counts |
| `12A-DR-013` | Implement the three-axis information model with a reconciliation duty | `D-042`, `TR-021`, `TR-090`, `WEP-647` | A fourth flat category list | `12A-OPEN-001` |
| `12A-DR-014` | Separate access permissions from permitted flows between classes | `12A-RS-116` | A permission table alone | — |
| `12A-DR-015` | Require each aggregate to enumerate its quasi-identifiers and inference argument | `12A-RS-094`, `12A-RS-095` | Rely on `k = 5` alone | — |
| `12A-DR-016` | Specify HMAC key custody, rotation and a written identifiability assessment | `12A-RS-092`, `12A-RS-089`, `12A-RS-098` | Treat the digest as anonymous | `UD-017` |
| `12A-DR-017` | State the erasure-versus-spine conflict as an unresolved obligation pair | `12A-RS-087`; `REQ-024` | Choose one duty silently | `UD-055` |
| `12A-DR-018` | Make the audit spine tamper-evident with an actively-run verification job | `12A-RS-029`; prototype inspection | Append-only by convention | Stage 5; `12A-OPEN-009` |
| `12A-DR-019` | Audit privileged **reads** with a purpose code | `WEG-04`, `DPE-054`, `DIP-121`, `NET-051` | Auditing writes only | `12A-OPEN-006` |
| `12A-DR-020` | Define administrative authority by what it may not do, and enumerate the set | `12A-RS-028`; `DAT-004` | A capability list alone | `UD-053` |
| `12A-DR-021` | Give emergency measures turn-counted expiry and mandatory retrospective review | Brief §13.6; `D-025` | Standing broad authority | `UD-056` |
| `12A-DR-022` | Assign one failure posture per risk category, with the reason recorded | Brief §18; `D-025` | A single global posture | — |
| `12A-DR-023` | Disclose the accepted identity-verification ceiling in player-facing terms | `12A-RS-051`, `12A-RS-060` | Implying detection capability | — |
| `12A-DR-024` | Close the four registered deferrals explicitly in 12B: `DPE-049`, `DPE-054`, `REQ-674`, `AX-23`, plus `WEG-02`/`04`/`05`/`06` and `GAP-13` | Their own source rows | Leaving them open again | `UD-044` untouched |
| `12A-DR-025` | Express ladder tiers in **turn boundaries, frozen game-object capabilities and season eligibility**, not day counts, and publish the escalation carve-out in the same table | `12A-RS-126`, `12A-RS-124`, `12A-RS-125`; Report 08's "feature restriction" rung | Copying a realtime title's day-count ladder | `UD-053` |
| `12A-DR-026` | Add a standing **operator re-investigation duty**, independent of any player appeal, alongside `NET-046`'s new-evidence reopening | `12A-RS-121` | Appeal-only correction | — |
| `12A-DR-027` | Cap appeals at a small published integer per sanction, publish the non-appealable categories, and keep re-openings on new evidence outside the cap | `12A-RS-129`, `12A-RS-132` | Unlimited appeal as a fairness gesture | `UD-059` |
| `12A-DR-028` | Generate the player-facing statement of reasons **from the enforcement record**, so a sanction that cannot produce its own reason notice is incomplete by construction | `12A-RS-133` (DSA Art. 17 wording); `NET-048`, `DAT-009` | Writing notices afterwards | `UD-017` for applicability |
| `12A-DR-029` | Name a **"benefited from abuse"** tier distinct from cheating, with a materiality threshold and a correction-first remedy | `12A-RS-124`, `12A-RS-128`, `12A-RS-018` | Folding gain into culpability | `UD-052` |
| `12A-DR-030` | Adopt AC-6(9) logging, AU-9 protection-and-alerting and **AU-9(5) dual authorisation as the declared substitute** for separations one person cannot perform | `12A-RS-140`; `12A-CR-083` | Claiming separation of duties that does not exist | `UD-054` |
| `12A-DR-031` | Publish a periodic **signed root over the audit and enforcement tables**, so integrity is checkable by people who do not have to trust the operator | `12A-RS-143`, `12A-RS-144`, `12A-RS-152` | Internal verification alone | `UD-058` |
| `12A-DR-032` | Keep **item-economy and monetisation regulation** out of the moderation corpus and in the legal dependency register | `12A-RS-135`…`12A-RS-139` | Treating consumer-law exposure as a moderation problem | `UD-017` |

## 28. Conclusions

The strongest result of this pass is not a list of controls but a **reordering of priorities**. Under Nation Supremacy's fixed constraints — no client, no device signal, no identity proof, one operator, ₹0 — the industry's most visible anti-cheat machinery is unavailable, and the parts of it that are available are documented to over-punish innocent players and to be defeated by mimicry. The design response is not a weaker anti-cheat posture but a stronger one in a different place: make value impossible to forge, make secrets impossible to over-read, make abuse unprofitable at the flow level, correct what the rules could not have produced, and reserve punishment for what can actually be evidenced.

That reordering also improves the game. Every control that would otherwise have watched players cooperating — the thing that makes a nation-strategy world interesting — is replaced by a rule about what an alliance, a trade or a ballot may accomplish. `D-018`, `D-037` and `NET-039` said the project would not build a surveillance system; this research says the same thing on external grounds and shows that the alternative is both fairer and cheaper.

Three obligations follow immediately and belong to other prompts rather than to B-12's rulebook: fix the single-writer breach and the audit-spine gap in the production architecture (Stage 5), perform the backup and restore drill before any launch claim (CF-02, owner), and obtain the jurisdiction review that decides retention, transfers, breach timing and age assurance (`UD-017`, `UD-055`, `UD-060`). No fair-play, privacy or accountability sentence in B-12 will survive contact with a regulator or an insider incident unless those three are done, and none of them is a documentation task.

---

## 29. Prompt 12A acceptance gate register

Statuses are the six the brief §23 allows (`PASS`, `PARTIAL`, `FAIL`, `BLOCKED`, `NOT RUN`, `NOT APPLICABLE`), using the same meanings the 11C companion gives them: `PASS` means the documentary evidence exists, resolves and demonstrates the criterion; `PARTIAL` means part of it does and the missing element is named in the row. No gate here is graded on intention.

<<<<<<< HEAD
Tally: **15 PASS · 7 PARTIAL · 0 FAIL · 0 BLOCKED · 0 NOT RUN · 0 NOT APPLICABLE**. Nothing is `NOT RUN` because every gate was assessed against an artefact that exists after this pass, and nothing is `BLOCKED` because the A-phase scope needed no owner input to be completed. The seven `PARTIAL` rows each name the missing evidence and its owner: an owner or legal ruling (`P12A-03`, `P12A-08`, `P12A-10`, `P12A-16`), a downstream implementation or verification run (`P12A-09`, `P12A-12`, `P12A-22`). None is upgraded because this pass' validator passes.
=======
Tally: **15 PASS · 7 PARTIAL · 0 FAIL · 0 BLOCKED · 0 NOT RUN · 0 NOT APPLICABLE**. Nothing is `NOT RUN` because every gate was assessed against an artefact that exists after this pass, and nothing is `BLOCKED` because the A-phase scope needed no owner input to be completed — the owner-dependent work is what 12B inherits, which is exactly what the seven `PARTIAL` rows record.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

| Gate | Original acceptance criterion | Evidence | Exact file and section | Verification method | Result | Remaining limitation | Required action |
|---|---|---|---|---|---|---|---|
| `P12A-01` | Complete authoritative project inspection | Authority hierarchy, D-014 policy, 16-row five-class control-status table, prototype migrations read line by line | this report §3, §4.1; `../../../prototypes/supabase-feasibility/migrations/` | validator checks `12A-26`, `12A-27`, `12A-33`; the control table classifies each control rather than asserting it | **PASS** | Classification is of documentation state, not of runtime behaviour | 12B must re-read the Stage 5 architecture once it exists |
<<<<<<< HEAD
| `P12A-02` | Research methodology and evidence standards established | Five-pass method, source-type and confidence vocabularies, three self-corrections, thirteen rows that admit they were not read in full, nine of them substantive retrieval failures, and a separate access classification that reconciles 140 full / 9 partial / 3 inaccessible / 1 internal | this report §4; sources register §1.3–§1.6, §9, §10.1 | validator checks `12A-03`, `12A-04`, `12A-08`, `12A-38`, `12A-39`, `12A-40`, `12A-41` | **PASS** | The standard is documentary; it cannot certify that a read page said what the row says, and the confidence rating is reported separately from the access class rather than inferred from it | 12C re-checks any row a reviewer disputes |
| `P12A-03` | Relevant game and industry benchmarking completed | 40 `12A-BM` mechanics, 18 comparator profiles, 6 cross-operator disagreements, and the 8 October 2026 AGCM coordinated action recorded as regulatory watchlist context | sources register §7, §8, §9; `12A-RS-153` | validator checks `12A-06`, `12A-07`, `12A-36`, `12A-37`, `12A-42` | **PARTIAL** | Nine rows are substantive retrieval failures — three inaccessible and six readable only as an excerpt or snippet — so parts of the comparison rest on disclosed excerpts; no operator publishes appeal-overturn statistics, so `12A-RS-152` is an absence finding; and the AGCM action is an ongoing announcement with no infringement finding or outcome | 12B proceeds only on the disclosed excerpts; a later pass may retry the blocked primaries; the regulatory question stays with owner and legal counsel under `UD-017` |
| `P12A-04` | Fair-play and anti-cheat foundations established | Clientless architecture, 16-category value-source table, exploit taxonomy, five evidence states, six-way behavioural split, eleven false-positive classes | this report §6, §7 | validator checks `12A-26`, `12A-33`; `D-166` | **PASS** | The detection ceiling is argued, not measured: `12A-RK` rows name no rate | 14 calibrates any threshold; 12B writes no threshold |
| `P12A-05` | Multi-account abuse foundations established | Threat/legitimacy separation, four-route policy layering, accepted critical residual, and the identity-proof/coordinated-abuse evidence distinction | this report §8; `D-176` / `DD-224` | validator checks `12A-18`, `12A-24`, `12A-43`, `12A-44` | **PASS** | Identity-layer multi-accounting cannot be reliably detected under the current fixed constraints and this is recorded as an accepted critical residual, not a control; behavioural, transactional and outcome evidence can still support a named case | The owner must accept the residual in writing before any launch claim (`UD-052`, `UD-053`) |
| `P12A-06` | Collusion and coordinated manipulation foundations established | Manufactured-false-agency test, five collusion families, market-manipulation drafting, `D-018` compatibility argument | this report §9; `D-169` | validator checks `12A-24`, `12A-25`, `12A-27` | **PASS** | Graph scoring is a queue generator only; the corpus has no measured precision figure | 12B must not promote a score into a finding |
| `P12A-07` | Privacy architecture and information classification established | Three-axis model, 11 candidate categories, reconciliation of `D-042`, `TR-021`, `TR-090`, `WEP-647`, lifecycle and access principles | this report §10, §11 | validator check `12A-35` | **PASS** | The category set is a candidate; retention periods are deliberately absent pending `UD-055` | Legal review decides periods; 12B adopts or amends the table |
| `P12A-08` | Moderation and disciplinary foundations established | Violation taxonomy, severity factors, two-class remedy model, ladder reconciliation, four consequences of the `WEP-655` conflict | this report §12, §13 | validator checks `12A-20`, `12A-33` | **PARTIAL** | The corpus carries two incompatible sanction ladders (B-11 `WEP-655` reversals versus B-03/B-06 permanence) and 12A has no authority under `D-014` to choose; no duration is set | Owner or 12B must resolve the ladder conflict; the required evidence is an explicit owner or 12B decision, and Prompt 14 calibrates durations |
| `P12A-09` | Reporting, investigation and evidence principles established | Report lifecycle, evidence-hierarchy rules, chain-of-custody posture from SP 800-86, the confirmed audit-spine gap | this report §14, §19 | validator checks `12A-33`, `12A-25` | **PARTIAL** | The prototype `audit` table has no protective trigger and no append-only or verification mechanism exists anywhere in the corpus; that is a confirmed open defect, not a designed control | The required evidence is a Stage 5 implementation plus an executed append-only and tamper-evidence verification against a real database; 12C may grade this only against that run |
| `P12A-10` | Appeals and dispute-resolution foundations established | Four additions to the candidate appeal design, reversal duty without a user appeal, bounded appeal budget shape | this report §15; sources register §6.1 findings 3 and 4 | validator checks `12A-14`, `12A-22` | **PARTIAL** | No comparator publishes an overturn rate, so the queue size cannot be estimated; `UD-059` is Open and the appeal count is not chosen | The owner decides `UD-059`; 12B writes the procedure, not the number, and no queue estimate may be presented as measured |
| `P12A-11` | Administrative authority and separation-of-duties foundations established | Eight candidate roles evaluated, four permission sets no one person may hold, prohibition-list authority, SoD matrix, insider controls | this report §16, §17; `D-172` | validator checks `12A-26`, `12A-27` | **PASS** | Roles and permission sets remain candidates; AC-6(9)/AU-9 separation is argued from the catalogue, not audited | 12B finalises the catalogue under the owner's `UD-056` |
| `P12A-12` | Auditability and administrative-abuse controls established | Documented candidate design for a chained-digest audit spine and a scheduled verification job — neither implemented nor running; optional published signed root; emergency-authority discipline from the break-glass guidance | this report §18, §19; `D-174` / `DD-222`, `D-175` | validator checks `12A-18`, `12A-33` | **PARTIAL** | Nothing is verified because nothing exists to verify: the chained-digest and scheduled-verification architecture is a documented candidate design, not an implemented control; the only audit table in the repository is unprotected, and CloudTrail-style validation is a separate step the project has not performed | The required evidence is a Stage 5 implementation and a real verification run; 12C may raise this gate only against that run |
| `P12A-13` | Cross-system dependencies documented | 30 `12A-INT` rows × 12 fields across 15 systems, plus the no-duplication rule | registers §4; this report §20 | validator checks `12A-23`, `12A-09` | **PASS** | A dependency table records the interfaces 12A found, not every interface that will be needed | 12B extends the rows where its rules touch systems not yet named |
| `P12A-14` | Security and privacy threat register completed | 32 `12A-RK` rows × 18 fields, five evidence classes, ordinal likelihood and impact, named residual | registers §5; this report §21 | validator checks `12A-24`, `12A-25` | **PASS** | Bands are judgement applied to a documented scale, not probabilities; `12A-RK` rows with class `HYPOTHETICAL` carry no measurement | 14 and Stage 5 convert the measurable rows into tests |
| `P12A-15` | Failure and recovery principles established | 15 `12A-FR` postures, each with a reason, and the explicit refusal of one universal policy | registers §7; this report §22; `D-176` | validator checks `12A-28` | **PASS** | Postures are designs; none has been exercised under a fault injection | Stage 5 and 12C test them |
| `P12A-16` | Requirements complete, clear and traceable | 106 `12A-CR` candidates × 15 fields, all 20 categories, overlap table against the 14 existing `REQ` rows, 22 rejected candidates | registers §2, §3, §6; this report §23 | validator checks `12A-09`–`12A-16` | **PARTIAL** | Under `D-014` an A-phase pass may not allocate `REQ-`; the rows are candidates: 20 depend on an owner or legal decision and 5 on a downstream prompt, so none can be closed here | The required evidence is owner or legal rulings on the 20 owned rows plus later-stage outcomes for the 5; 12B allocates `REQ-764` onward and must not inflate the set |
| `P12A-17` | Design recommendations and decisions properly classified | 32 `12A-DR` recommendations each naming a rejected alternative; `D-163`–`D-177` / `DD-211`–`DD-225` classified per §16 | this report §5.4, §24, §27; `DECISIONS.md`, `stage-2/04` §6 | validator checks `12A-18`, `12A-19`, `12A-21` | **PASS** | Fifteen decisions are Confirmed *as design positions*; that status buys no implementation and no rule text | 12B turns positions into rules or records why not |
| `P12A-18` | Owner-reserved decisions remain correctly unresolved | `UD-040`–`UD-049`, `UD-050`, `UD-051` untouched; `UD-052`–`UD-060` opened, none resolved; 7 owner rows and 2 legal rows | `stage-2/05` §2, §6; this report §25 | validator checks `12A-14`, `12A-22` | **PASS** | Nine new open rows is nine more things the owner must answer before B-12 can close | Owner attention; 12B proceeds only on the non-owner half |
| `P12A-19` | Prompt 12B scope and dependencies clearly defined | The 12A/12B/12C split, the reserved `20_fair_play_and_player_protection.md` path, the inherited gate list, and what 12B must not do | this report §2.3, §23.4, §32.3; `D-163` / `DD-211` | validator checks `12A-15`, `12A-33` | **PASS** | Scope is a statement of intent until the owner authorises 12B | Owner authorisation |
| `P12A-20` | Project-wide documentation synchronized | Progress logs §73 and §74, continuity status blocks, `ROADMAP.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, the Stage 2 handoff, the prompt roadmap's Prompt 12 split, the Bible outline B-12 row, and the 12A-C1 reconciliation of every live count and next-action claim | `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/stage-2/00`, `01`, `02`, `06` | validator checks `12A-31`, `12A-32`; the project link gate; `09_validate.py` and the unit tests | **PASS** | The frontiers 12A moved were refreshed in `09_validate.py`, `test_decision_registers.py`, `test_next_action.py`, `status_rules.py`, `10B_validate_warfare.py` and `09B_validate_alliance_semantic.py`; what remains stale predates Prompt 12 (`D-1`, `D-2`) plus the two broken Stage-1 sweep tools (`D-10`), and `D-2` was closed during the 2026-11-07 remediation | A frontier-refresh pass owns `D-1` and `D-10`; none of them is 12A evidence |
| `P12A-21` | Independent validator and fixtures pass | `docs/qa_backups/12A_validate_foundations.py`: 45 checks, 10 positive and 33 negative fixtures, plus the external link gate | §30 of this report | the validator itself and `--self-test` | **PASS** | It is a document checker: it grades the research record and proves nothing about any control's behaviour | 12C keeps it and extends it; it is never a substitute for a security test |
| `P12A-22` | Foundations are independently reviewable | Every claim carries an identifier, every identifier resolves, every count in §30 is a measurement, and the cross-document count checks `12A-36`–`12A-45` reconcile the registers against the report | all three deliverables | validator checks `12A-05`, `12A-16`, `12A-17`, `12A-34`, `12A-36`–`12A-45` | **PARTIAL** | `validate_final.py` passes after the 2026-11-07 review remediation, but 11A's check 29 still asserts its research-era `REQ-703` maximum (`D-1`) and the two Stage-1 sweep tools remain broken (`D-10`); the prototype also still grants table-wide `UPDATE` on `feasibility.profiles` including `treasury`, with no `0005` migration, no SQL permission tests, no protective `audit` trigger and no executed tamper-evidence job | The required evidence is a frontier-refresh pass for `D-1` and `D-10` and Stage 5's column-level privilege correction, SQL permission tests and audit-spine verification; no independent reviewer has yet approved this pass |
=======
| `P12A-02` | Research methodology and evidence standards established | Five-pass method, source-type and confidence vocabularies, three self-corrections, thirteen rows that admit they were not read in full, nine of them substantive retrieval failures | this report §4; sources register §1.3–§1.6, §9 | validator checks `12A-03`, `12A-04`, `12A-08` | **PASS** | The standard is documentary; it cannot certify that a read page said what the row says | 12C re-checks any row a reviewer disputes |
| `P12A-03` | Relevant game and industry benchmarking completed | 40 `12A-BM` mechanics, 18 comparator profiles, 6 cross-operator disagreements | sources register §7, §8, §9 | validator checks `12A-06`, `12A-07` | **PARTIAL** | Nine sources were unreadable (bot gates, 403, 429, 202); no operator publishes appeal-overturn statistics, so `12A-RS-152` is an absence finding | 12B proceeds on the disclosed excerpts; a later pass may retry the blocked primaries |
| `P12A-04` | Fair-play and anti-cheat foundations established | Clientless architecture, 16-category value-source table, exploit taxonomy, five evidence states, six-way behavioural split, eleven false-positive classes | this report §6, §7 | validator checks `12A-26`, `12A-33`; `D-166` | **PASS** | The detection ceiling is argued, not measured: `12A-RK` rows name no rate | 14 calibrates any threshold; 12B writes no threshold |
| `P12A-05` | Multi-account abuse foundations established | Threat/legitimacy separation, four-route policy layering, accepted critical residual | this report §8; `D-164`, `D-177` | validator checks `12A-18`, `12A-24` | **PASS** | Identity-layer multi-accounting is undetectable under the fixed constraints and this is recorded as an accepted critical residual, not a control | The owner must accept the residual in writing before any launch claim (`UD-052`, `UD-053`) |
| `P12A-06` | Collusion and coordinated manipulation foundations established | Manufactured-false-agency test, five collusion families, market-manipulation drafting, `D-018` compatibility argument | this report §9; `D-169` | validator checks `12A-24`, `12A-25`, `12A-27` | **PASS** | Graph scoring is a queue generator only; the corpus has no measured precision figure | 12B must not promote a score into a finding |
| `P12A-07` | Privacy architecture and information classification established | Three-axis model, 11 candidate categories, reconciliation of `D-042`, `TR-021`, `TR-090`, `WEP-647`, lifecycle and access principles | this report §10, §11 | validator check `12A-35` | **PASS** | The category set is a candidate; retention periods are deliberately absent pending `UD-055` | Legal review decides periods; 12B adopts or amends the table |
| `P12A-08` | Moderation and disciplinary foundations established | Violation taxonomy, severity factors, two-class remedy model, ladder reconciliation, four consequences of the `WEP-655` conflict | this report §12, §13 | validator checks `12A-20`, `12A-33` | **PARTIAL** | The corpus carries two incompatible sanction ladders (B-11 `WEP-655` reversals versus B-03/B-06 permanence) and 12A has no authority to choose; no duration is set | Owner or 12B must resolve the ladder conflict; 14 calibrates durations |
| `P12A-09` | Reporting, investigation and evidence principles established | Report lifecycle, evidence-hierarchy rules, chain-of-custody posture from SP 800-86, the confirmed audit-spine gap | this report §14, §19 | validator checks `12A-33`, `12A-25` | **PARTIAL** | The prototype `audit` table has no protective trigger and no append-only or verification mechanism exists anywhere in the corpus; that is a confirmed open defect, not a designed control | Stage 5 must implement the spine; 12C needs real evidence to grade this |
| `P12A-10` | Appeals and dispute-resolution foundations established | Four additions to the candidate appeal design, reversal duty without a user appeal, bounded appeal budget shape | this report §15; sources register §6.1 findings 3 and 4 | validator checks `12A-14`, `12A-22` | **PARTIAL** | No comparator publishes an overturn rate, so the queue size cannot be estimated; `UD-059` is Open and the appeal count is not chosen | Owner decides `UD-059`; 12B writes the procedure, not the number |
| `P12A-11` | Administrative authority and separation-of-duties foundations established | Eight candidate roles evaluated, four permission sets no one person may hold, prohibition-list authority, SoD matrix, insider controls | this report §16, §17; `D-172` | validator checks `12A-26`, `12A-27` | **PASS** | Roles and permission sets remain candidates; AC-6(9)/AU-9 separation is argued from the catalogue, not audited | 12B finalises the catalogue under the owner's `UD-056` |
| `P12A-12` | Auditability and administrative-abuse controls established | Chained-digest spine with an actively-run verification job, optional published signed root, emergency-authority discipline from the break-glass guidance | this report §18, §19; `D-174`, `D-175` | validator checks `12A-18`, `12A-33` | **PARTIAL** | Nothing is verified because nothing exists to verify: the only audit table in the repository is unprotected, and CloudTrail-style validation is a separate step the project has not performed | Stage 5 implements the spine; 12C may raise this gate only against a verification run |
| `P12A-13` | Cross-system dependencies documented | 30 `12A-INT` rows × 12 fields across 15 systems, plus the no-duplication rule | registers §4; this report §20 | validator checks `12A-23`, `12A-09` | **PASS** | A dependency table records the interfaces 12A found, not every interface that will be needed | 12B extends the rows where its rules touch systems not yet named |
| `P12A-14` | Security and privacy threat register completed | 32 `12A-RK` rows × 18 fields, five evidence classes, ordinal likelihood and impact, named residual | registers §5; this report §21 | validator checks `12A-24`, `12A-25` | **PASS** | Bands are judgement applied to a documented scale, not probabilities; `12A-RK` rows with class `HYPOTHETICAL` carry no measurement | 14 and Stage 5 convert the measurable rows into tests |
| `P12A-15` | Failure and recovery principles established | 15 `12A-FR` postures, each with a reason, and the explicit refusal of one universal policy | registers §7; this report §22; `D-176` | validator checks `12A-28` | **PASS** | Postures are designs; none has been exercised under a fault injection | Stage 5 and 12C test them |
| `P12A-16` | Requirements complete, clear and traceable | 106 `12A-CR` candidates × 15 fields, all 20 categories, overlap table against the 14 existing `REQ` rows, 22 rejected candidates | registers §2, §3, §6; this report §23 | validator checks `12A-09`–`12A-16` | **PARTIAL** | They are candidates, not `REQ-` allocations: 20 depend on an owner or legal decision and 5 on a downstream prompt, so none can be closed in an A-phase pass | 12B allocates `REQ-764` onward and must not inflate the set |
| `P12A-17` | Design recommendations and decisions properly classified | 32 `12A-DR` recommendations each naming a rejected alternative; `D-163`–`D-177` / `DD-211`–`DD-225` classified per §16 | this report §5.4, §24, §27; `DECISIONS.md`, `stage-2/04` §6 | validator checks `12A-18`, `12A-19`, `12A-21` | **PASS** | Fifteen decisions are Confirmed *as design positions*; that status buys no implementation and no rule text | 12B turns positions into rules or records why not |
| `P12A-18` | Owner-reserved decisions remain correctly unresolved | `UD-040`–`UD-049`, `UD-050`, `UD-051` untouched; `UD-052`–`UD-060` opened, none resolved; 7 owner rows and 2 legal rows | `stage-2/05` §2, §6; this report §25 | validator checks `12A-14`, `12A-22` | **PASS** | Nine new open rows is nine more things the owner must answer before B-12 can close | Owner attention; 12B proceeds only on the non-owner half |
| `P12A-19` | Prompt 12B scope and dependencies clearly defined | The 12A/12B/12C split, the reserved `20_fair_play_and_player_protection.md` path, the inherited gate list, and what 12B must not do | this report §2.3, §23.4, §32.3; `D-163` / `DD-211` | validator checks `12A-15`, `12A-33` | **PASS** | Scope is a statement of intent until the owner authorises 12B | Owner authorisation |
| `P12A-20` | Project-wide documentation synchronized | Progress log §73, continuity status blocks, `ROADMAP.md`, `PROJECT_PROGRESS.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, the Stage 2 handoff, the prompt roadmap's Prompt 12 split, the Bible outline B-12 row, and 63 rewritten live-status claims | `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/AI_CONTEXT.md`, `docs/stage-2/00`, `01`, `02`, `06` | validator checks `12A-31`, `12A-32`; the project link gate; `09_validate.py` 371/371 and 39 unit tests green | **PASS** | The frontiers 12A moved were refreshed in `09_validate.py`, `test_decision_registers.py`, `test_next_action.py`, `status_rules.py`, `10B_validate_warfare.py` and `09B_validate_alliance_semantic.py`; what remains stale predates Prompt 12 (`D-1`, `D-2`) plus the two broken Stage-1 sweep tools (`D-10`) | A frontier-refresh pass owns `D-1`, `D-2` and `D-10`; none of them is 12A evidence |
| `P12A-21` | Independent validator and fixtures pass | `docs/qa_backups/12A_validate_foundations.py`: 35 checks, 10 positive and 23 negative fixtures, plus the external link gate | §30 of this report | the validator itself and `--self-test` | **PASS** | It is a document checker: it grades the research record and proves nothing about any control's behaviour | 12C keeps it and extends it; it is never a substitute for a security test |
| `P12A-22` | Foundations are independently reviewable | Every claim carries an identifier, every identifier resolves, every count in §30 is a measurement | all three deliverables | validator checks `12A-05`, `12A-16`, `12A-17`, `12A-34` | **PARTIAL** | `validate_final.py` now passes after the 2026-11-07 review remediation, but 11A's check 29 still asserts its research-era `REQ-703` maximum (`D-1`) and the two Stage-1 sweep tools remain broken (`D-10`), so a reviewer still cannot reproduce every project suite green | A frontier-refresh pass clears `D-1` and `D-10`, or the handoff annotates them as accepted |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

---

## 30. Validation actually performed

Every figure below was produced by the command in its own row, first on 2026-11-06 and re-run after review remediation on 2026-11-07; none is an estimate. Exit codes are the real process exits.

| Command | Actual result | Exit |
|---|---|---|
<<<<<<< HEAD
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 45/45 passed; 0 failed` over the inventory line `sources=153 benchmark=40 comparators=18 candidates=106 dependencies=30 threats=32 postures=15 open-questions=15 recommendations=32 categories=11 · D=177 DD=225 UD=60 REQ max=763` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `POSITIVE FIXTURES: 10/10 accepted`, `NEGATIVE FIXTURES: 33/33 rejected for the expected reason` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --verbose` | 45 per-check lines, each reporting a measured count rather than a heading | 0 |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` (3,535 links found, 3,153 checked locally, 382 external skipped, 29 anchors checked) — run standalone and again inside check `12A-34` | 0 |
=======
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 35/35 passed; 0 failed` over the inventory line `sources=152 benchmark=40 comparators=18 candidates=106 dependencies=30 threats=32 postures=15 open-questions=15 recommendations=32 categories=11 · D=177 DD=225 UD=60 REQ max=763` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --self-test` | `POSITIVE FIXTURES: 10/10 accepted`, `NEGATIVE FIXTURES: 23/23 rejected for the expected reason` | 0 |
| `python docs/qa_backups/12A_validate_foundations.py --verbose` | 35 per-check lines, each reporting a measured count rather than a heading | 0 |
| `python docs/qa_backups/validate_links.py` | `Unresolved: 0` (3,532 links found, 3,150 checked locally) — run standalone and again inside check `12A-34` | 0 |
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3
| `python docs/qa_backups/09_validate.py` | `371/371 checks passed — ALL CHECKS PASSED` after the frontier refresh in §32 and the review remediation's row-12 status check | 0 |
| `python -m unittest test_next_action test_decision_registers` (from `docs/qa_backups/`) | `Ran 39 tests … OK` | 0 |
| `python docs/qa_backups/09A_validate_alliance.py` | `Checks run: 943 — PASS: all Alliance integration, source, permission and handoff checks` | 0 |
| `python docs/qa_backups/09B_validate_alliance_semantic.py` | `[PASS] All 34 semantic checks passed with no review findings` after the C17 register frontiers were advanced to D-177 / DD-225 / UD-060 | 0 |
| `python docs/qa_backups/10B_validate_warfare.py` | `PASS: all B-10 structure, disposition, formula, register and boundary checks`; 73/73 negative fixtures rejected, CF-01/CF-02 clean | 0 |
| `python docs/qa_backups/11B_validate_b11.py` | passes, with its standing trailer that gate `PASS` is documentary only | 0 |
| `python docs/qa_backups/11C_validate_b11_workflows.py` | `RESULT: PASS — 11C workflows, integration and acceptance documents are internally consistent with the B-11 sources at the documentation level` | 0 |
| `python docs/qa_backups/verify_alliance_numbers.py`, `verify_alliance_workflows.py`, `verify_city_numbers.py`, `verify_diplomacy_numbers.py`, `verify_diplomacy_workflows.py`, `verify_economy_numbers.py`, `verify_market_numbers.py`, `verify_market_workflows.py`, `verify_politics_numbers.py`, `verify_warfare_workflows.py` | every one reports all checks passed (politics `879/879`, warfare workflows `49/49`, diplomacy `17 groups`, market `07C VALIDATION: ALL CHECKS PASSED`) | 0 each |
<<<<<<< HEAD
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — legacy check 29 expects a maximum of `REQ-703` and observes a maximum textual reference of `REQ-764`, which is reserved for Prompt 12B and not allocated; the canonical frontier remains `REQ-763`. Pre-existing debt `D-1`, recorded in log §72 and **not** modified here | 1 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` — the 2026-11-07 review remediation advanced every pre-Prompt-12 frontier assertion to the current registers (`REQ-001..763`, `DD-001..225`, `UD-001..060`, 28/3/29, `UD-024` Resolved, the §6 inventory and 55/688/19/1/0) and `stage_2_next_prompt` to `12B`; no check was weakened or deleted | 0 |


### 30.1 What the 45 checks grade

Research integrity (`12A-02`–`12A-08`): 153 source rows contiguous with no gap and no duplicate, each with a registered type token, a leading confidence token and either a live URL or an explicit non-capture disclosure; every cited `12A-RS` resolves and every row is cited somewhere; 40 benchmark rows each cite sources and carry approach, strength, limitation and applicability; 18 comparator profiles each carry a verification statement; retrieval honesty is enforced by requiring rows that admit they were not read.

Requirement integrity (`12A-09`–`12A-16`): 106 candidates, unique, contiguous, and present exactly once in each half; statements inside the 60–900 character band with a rationale and a verification approach; the eight banned vague formulations absent; the closed priority and status vocabularies only, with no status allowed to say `Approved`; all 20 brief categories populated; every `Yes — owner` dependency names an existing `UD-` row; no global `REQ-` row allocated and the `REQ-764` reservation declared; every declared total reconciles with the rows in both registers.

Decision integrity (`12A-17`–`12A-22`): `D-001`…`D-177` contiguous and unique with all eight fields on the fifteen new rows; `DD-001`…`DD-225` contiguous and the §6 tally summing to the declared total; the 23 protected identifiers present and none newly superseded; 32 recommendations each naming a rejected alternative and none promoted to approval; the thirteen pre-existing owner-reserved rows plus `UD-052`…`UD-060` still Open or Deferred.
=======
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — check 29 still asserts `REQ max 703`; pre-existing debt `D-1`, recorded in log §72 and **not** modified here | 1 |
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` — the 2026-11-07 review remediation advanced every pre-Prompt-12 frontier assertion to the current registers (`REQ-001..763`, `DD-001..225`, `UD-001..060`, 28/3/29, `UD-024` Resolved, the §6 inventory and 55/688/19/1/0) and `stage_2_next_prompt` to `12B`; no check was weakened or deleted | 0 |


### 30.1 What the 35 checks grade

Research integrity (`12A-02`–`12A-08`): 152 source rows contiguous with no gap and no duplicate, each with a registered type token, a leading confidence token and either a live URL or an explicit non-capture disclosure; every cited `12A-RS` resolves and every row is cited somewhere; 40 benchmark rows each cite sources and carry approach, strength, limitation and applicability; 18 comparator profiles each carry a verification statement; retrieval honesty is enforced by requiring rows that admit they were not read.

Requirement integrity (`12A-09`–`12A-16`): 106 candidates, unique, contiguous, and present exactly once in each half; statements inside the 60–900 character band with a rationale and a verification approach; the eight banned vague formulations absent; the closed priority and status vocabularies only, with no status allowed to say `Approved`; all 20 brief categories populated; every `Yes — owner` dependency names an existing `UD-` row; no global `REQ-` row allocated and the `REQ-764` reservation declared; every declared total reconciles with the rows in both registers.

Decision integrity (`12A-17`–`12A-22`): `D-001`…`D-177` contiguous and unique with all eight fields on the fifteen new rows; `DD-001`…`DD-225` contiguous and the §6 tally summing to the declared total; the 27 protected identifiers present and none newly superseded; 32 recommendations each naming a rejected alternative and none promoted to approval; the eleven pre-existing owner-reserved rows plus `UD-052`…`UD-060` still Open or Deferred.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

Integration integrity (`12A-23`–`12A-27`): 30 dependency rows with both halves aligned and twelve fields populated; 32 threat rows with evidence class, an explicit `L1`–`L5` likelihood score, an explicit `I1`–`I5` impact score, a band word with a score on the 1–25 scale and a residual read from the dedicated column, each naming a preventive control, a detection control and a resolvable `12A-CR` link, with at least three `CONFIRMED` rows and four of the five classes in use; the 16 protected source-of-truth categories each assigned one owner; and the B-12 authority boundary checked in both directions — four forbidden formulations absent and the two required refusals present.

Documentation integrity (`12A-28`–`12A-35`): 15 failure postures with no universal fail-open/fail-closed assertion; 15 open questions each owned with resolvable `UD` references; the 22-gate register using only the six legal statuses with the declared tally matching the computed one; the nine machine-checked continuity keys agreeing across the three status files with the decisions range at `D-001..D-177`; progress-log §73 present with §§67, 70, 71 and 72 intact; no implementation, executed-test or legal-conclusion claim anywhere in the three deliverables; the external link gate at `Unresolved: 0`; and the classification model internally consistent across three axes while reconciling the four pre-existing vocabularies.

<<<<<<< HEAD
Cross-document reconciliation (`12A-36`–`12A-45`): the report's §5 benchmark range and the register's declared count both equal the 40 parsed `12A-BM` rows; its comparator range and declared count both equal the 18 parsed `12A-CMP` profiles; the leading confidence token of every row reconciles with the `High`/`Medium`/`Low`/`Unverified` summary in both documents; the access-class table's row identifiers and counts reconcile with the 153 rows and with the report's 140 full-read / 13 not-full / nine-failure statement; the register's source classes and type vocabulary equal the validator's; `12A-RS-152` is the internal absence finding and is not presented as an external URL; `12A-RS-153` carries the official AGCM URL, both dates and the ongoing/no-finding/no-automatic-obligation limits; the §1.5 access-date statement distinguishes the original `12A-RS-001`–`12A-RS-152` corpus (2026-11-06) from the `12A-RS-153` addition (2026-11-07) without overwriting per-row dates; `P12A-05` cites `D-176` / `DD-224` rather than the posture decision; and no absolute undetectability wording survives while the canonical identity-layer sentence and the behavioural/transactional/outcome distinction are present.

### 30.2 Negative fixtures

Thirty-three seeded corruptions registered in `FIXTURES` as `12A-N01`…`12A-N33`, each expected to make exactly one named check fail for a stated reason — `run_fixtures` compares the failure detail against the expected reason, so a check that fails for some unrelated cause is reported as a wrong-reason fixture rather than a pass: a deleted source row (`12A-02`), a claim citing a nonexistent source (`12A-05`), a duplicated requirement id (`12A-09`), a requirement with no verification approach (`12A-10`), a candidate promoted to `Approved` (`12A-12`), a closed owner-reserved row (`12A-22`), a removed dependency half (`12A-23`), a duplicated design position (`12A-19`), a category losing its axis assignment (`12A-35`), an unsupported legal conclusion (`12A-33`), a benchmark citing no source (`12A-06`), a gate using an illegal status (`12A-30`), an implementation claim appearing (`12A-33`), a declared total drifting (`12A-16`), a protected decision superseded (`12A-20`), an implementation claim after an unrelated negation (`12A-33`), a scope-qualified implementation claim (`12A-33`), a cross-cell negation (`12A-33`), an illegal gate Result that a legal token elsewhere must not rescue (`12A-30`), a likelihood cell that carries prose instead of an `L1`–`L5` token (`12A-24`), a band-name-only assessment with no ordinal score (`12A-24`), a band score outside the 1–25 scale (`12A-24`), a threat row truncated before its residual column (`12A-24`), a §5 benchmark range stopping at 32 (`12A-36`), a §5 comparator range stopping at 12 (`12A-37`), a register High count one below its rows (`12A-38`), a full-read count one above its access classes (`12A-39`), the internal `RESEARCH FINDING` type removed from the vocabulary (`12A-40`), `RS-152` retyped as an external operator source (`12A-41`), `RS-153` carrying the wrong publication date (`12A-42`), `P12A-05` citing the posture decision (`12A-43`), an absolute undetectability claim reappearing (`12A-44`) and the `RS-153` addition dated to the original access day (`12A-45`). Ten clean-run fixtures `12A-P01`…`12A-P10` assert the matching checks pass on the unmutated corpus. `--self-test` asserts all forty-three.
=======
### 30.2 Negative fixtures

Twenty-three seeded corruptions registered in `FIXTURES` as `12A-N01`…`12A-N23`, each expected to make exactly one named check fail for a stated reason — `run_fixtures` now compares the failure detail against the expected reason, so a check that fails for some unrelated cause is reported as a wrong-reason fixture rather than a pass: a deleted source row (`12A-02`), a claim citing a nonexistent source (`12A-05`), a duplicated requirement id (`12A-09`), a requirement with no verification approach (`12A-10`), a candidate promoted to `Approved` (`12A-12`), a closed owner-reserved row (`12A-22`), a removed dependency half (`12A-23`), a duplicated design position (`12A-19`), a category losing its axis assignment (`12A-35`), an unsupported legal conclusion (`12A-33`), a benchmark citing no source (`12A-06`), a gate using an illegal status (`12A-30`), an implementation claim appearing (`12A-33`), a declared total drifting (`12A-16`), a protected decision superseded (`12A-20`), an implementation claim after an unrelated negation (`12A-33`), a scope-qualified implementation claim (`12A-33`), a cross-cell negation (`12A-33`), an illegal gate Result that a legal token elsewhere must not rescue (`12A-30`), a likelihood cell that carries prose instead of an `L1`–`L5` token (`12A-24`), a band-name-only assessment with no ordinal score (`12A-24`), a band score outside the 1–25 scale (`12A-24`) and a threat row truncated before its residual column (`12A-24`). Ten clean-run fixtures `12A-P01`…`12A-P10` assert the matching checks pass on the unmutated corpus. `--self-test` asserts all thirty-three.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

### 30.3 What validation does not prove

The suite grades text. It does not prove that any control works: no cheat detection, privacy enforcement, RLS behaviour, moderation tooling, authentication, appeal execution, audit-log tamper resistance or playability was tested, because none of those exists to test. `12A-34` proves links resolve, not that the linked pages still say what the register records.

---

## 31. Files created and updated

Created by this pass: `docs/stage-2/research/12A_fair_play_privacy_moderation_administration_research.md` (this report), `docs/stage-2/research/12A_sources_and_benchmarks_register.md`, `docs/stage-2/research/12A_requirements_integration_and_risk_registers.md`, `docs/qa_backups/12A_validate_foundations.py` and `docs/qa_backups/12A_sync_docs.py` — the one-shot live-status synchroniser, in the shape `11C_sync_docs.py` established.

Updated: `docs/DECISIONS.md` (D-163…D-177), `docs/stage-2/04_approved_and_provisional_decisions.md` (DD-211…DD-225 and the §6 tally), `docs/stage-2/05_unresolved_design_decisions.md` (UD-052…UD-060, the counts and the §6 inventory), `docs/stage-2/03_requirements_traceability.md` (header synchronisation note only — no rows), `docs/stage-2/06_stage_2_progress_log.md` (§73 appended, nothing earlier rewritten), `docs/AI_CONTEXT.md`, `docs/PROJECT_PROGRESS.md`, `docs/ROADMAP.md`, `docs/AI_HANDOFF.md`, `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md` (B-12 path and status), the DD register's decision-count lead-in, and the live-status header of the progress log.

Six QA checkers had a hard-coded register frontier advanced to the value this pass created, each with a dated comment and none loosened or deleted: `docs/qa_backups/status_rules.py` (`CURRENT_SUBPROMPT` → `12A`, `11C` and `12A` added to the completed set, and the sub-prompt pattern extended to the `12` family — without that, `12A` was not a recognised sub-prompt token at all), `09_validate.py`, `test_decision_registers.py`, `test_next_action.py` (row 12 is no longer a bare `Pending` row, and the 11C-as-live fixture became a stale-claim case with `12B` as the live case), `10B_validate_warfare.py` and `09B_validate_alliance_semantic.py` (C17 registers to D-177 / DD-225 / UD-060 at 38 Confirmed). `validate_final.py`'s pre-Prompt-12 assertions and 11A's check 29 were deliberately left alone and are recorded as debt in §32.

No gameplay specification, prototype file or approved register row was modified, and no file was deleted.

---

## 32. Limitations and what 12B inherits

<<<<<<< HEAD
**Three structural limits on this pass.** First, it is an A-phase pass: it may not allocate `REQ-`, may not resolve an owner-reserved decision and may not write a rule, so the honest ceiling for `P12A-16` is `PARTIAL`. Second, thirteen of the 153 registered evidence rows were not read in full: nine are substantive retrieval failures — three inaccessible and six readable only as an excerpt or snippet — and four are one index-only record, one abstract-only record, one secondary case note and this pass's internal absence finding; where a claim rests on an excerpt it is marked, and the two places where an excerpt changed a conclusion are in sources register §6.2. Third, no measurement of any kind was taken — no rate, no precision, no latency, no population statistic — so every threshold in this report is left uncalibrated on purpose.
=======
**Three structural limits on this pass.** First, it is an A-phase pass: it may not allocate `REQ-`, may not resolve an owner-reserved decision and may not write a rule, so the honest ceiling for `P12A-16` is `PARTIAL`. Second, nine primary sources were unreadable and are recorded as such; where a claim rests on an excerpt it is marked, and the two places where an excerpt changed a conclusion are in sources register §6.2. Third, no measurement of any kind was taken — no rate, no precision, no latency, no population statistic — so every threshold in this report is left uncalibrated on purpose.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

**Six things 12B must not quietly assume.** The audit spine does not exist and the prototype's `audit` table is unprotected; the `service_role` bypass means no RLS claim may be written as a guarantee; the two sanction ladders are still in conflict; the information-classification table is a candidate that must survive the legal review; `UD-052`…`UD-060` are open and 12B has no authority to close them; and the identity-layer multi-accounting residual is accepted, not solved, so no marketing or design sentence may imply otherwise.

**Debt this pass records rather than repairs.** `D-1`: the 11A validator's check 29 asserts `REQ max 703`, a research-era frontier that Prompt 11B itself moved to 763; it exits 1, was recorded as debt in log §72, and 12A left it alone rather than edit another pass's expectation. `D-10`: the two Stage-1 sweep tools are in the same state — `08_sweep.py` raises `TypeError` at line 149 and `08_sweep2.py` asserts "no new D-007+ rows added", which has been false since Prompt 01. `D-2` (the final validator's ten pre-Prompt-12 frontier assertions) is no longer debt: the 2026-11-07 review remediation advanced every assertion to the current registers, and `validate_final.py` now exits 0.

**Debt this pass did repair.** The register frontiers that 12A's own additions moved were advanced in the checkers that hard-code them, with each change labelled and dated: `09_validate.py` (DD to 225, UD to 60, the 28/3/29 status reconciliation, the §6 inventory, the handoff decision-count word, the sub-prompt pattern for the `12` family via `status_rules.py`, `CURRENT_SUBPROMPT` → `12A` and its mirror in `10B_validate_warfare.py`), `test_decision_registers.py` (UD set, counts and totals), `test_next_action.py` (row 12 is no longer a bare `Pending` row; the 11C-as-live fixture is now a stale-claim case and 12B is the live case), and `09B_validate_alliance_semantic.py` (C17 registers to D-177 / DD-225 / UD-060 with 38 Confirmed). Two assertions were **weakened by nobody**: no expected count was loosened, only moved to the value the registers now hold, and no check was deleted. The 2026-11-07 review remediation completed the same operation for `validate_final.py`: its next-prompt, tracker, DD, UD, §6-inventory, 28/3/29 and 55/688/19/1/0 expectations now match the current registers, the row-10 assertion names 12B and a row-12 assertion was added, so `D-2` is closed and the suite exits 0 without a check being removed or loosened.

---

## 33. D-014 compliance record

`D-014` authorises autonomous decisions of the ordinary design/scope/policy kind and forbids it for the four Category D classes. Applied to this pass:

| Class | Count in 12A | Treatment |
|---|---|---|
| Ordinary design or architecture position | 15 (`D-163`…`D-177`) | Decided autonomously, recorded Confirmed **as a design position**, each with the evidence row that carries it |
| Candidate requirement | 106 | Proposed, never approved; no `REQ-` id allocated |
| Recommendation | 32 | Advisory, each naming the alternative rejected and why |
| Owner-reserved policy | 7 opened (`UD-052`…`UD-054`, `UD-056`…`UD-059`), 13 left untouched (`UD-017`, `UD-040`–`UD-051`) | Opened and left open; none closed, reinterpreted or assumed |
| Legal or jurisdiction-dependent | 2 (`UD-055`, `UD-060`) | Opened as `Yes — legal (Category D)`; no legal conclusion written |
| Numerical calibration | 0 | Deferred to Prompt 14 with the reason named in each row |
| External cost or irreversible action | 0 | None taken; no deployment, no purchase, no data subject request exercised, no Git operation |

<<<<<<< HEAD
Two boundary cases are called out because a reader might otherwise think this pass overreached. `D-176` / `DD-224` (the accepted critical residual) states the identity-layer detection limit and is not a waiver; `D-177` / `DD-225` records the prevention-heavy, remedy-based *posture* that sits around it, and the owner still has to accept the residual in writing before launch. `D-168` / `DD-216` (network-evidence demotion) confirms a limit that `D-037` already implied rather than creating new authority, and it is the reason `UD-053` had to be opened instead of answered.
=======
Two boundary cases are called out because a reader might otherwise think this pass overreached. `D-177` (the accepted critical residual) is a *posture* decision, not a waiver: it says the project will not build an identity layer, and the owner still has to accept that in writing before launch. `D-165` (network-evidence demotion) confirms a limit that `D-037` already implied rather than creating new authority, and it is the reason `UD-053` had to be opened instead of answered.
>>>>>>> 41111204d70371e7c649798db9f60eb5ef9f4cf3

**Nothing in this pass was Category A, B or C of the fixed-constraint list, and no approved gameplay mechanic, economy rule, diplomacy rule, alliance rule, warfare rule or progression rule was modified.**

