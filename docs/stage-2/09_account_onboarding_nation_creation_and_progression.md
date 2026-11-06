# Account holder policy, nation creation, onboarding and progression

**Version:** 1.1 · **Created:** 2026-10-24 · **Stage 2, Prompt 03** · **Revised:** 2026-11-04 (Prompt 10B-C3: `NAT-018` and the creation-state table state the Operations Points starting value as the national cap with one OP regenerated at each later boundary, matching B-10 `WAR-039`; no other rule, ID or value changed) · **Status:** **Complete as a specification** — the authoritative document for Bible part **B-03**. No rule here is implemented or tested.
**Rule status vocabulary:** **Approved** (established by an owner constraint or a confirmed decision) · **Provisional** (a design that binds later prompts but is not owner-approved) · **Proposed** (a candidate a later prompt may adopt or discard) · **Deferred** (belongs to a later stage). A rule ID is stable; rules are superseded, never deleted.
**What this document is not:** application code, a database schema, a migration, an authentication configuration, a deployment, or evidence that any rule has been implemented or tested. No game code exists.

**Companions:** [Bible outline](02_master_game_design_bible_outline.md) · [requirements](03_requirements_traceability.md) · [design decisions](04_approved_and_provisional_decisions.md) · [unresolved questions](05_unresolved_design_decisions.md) · [progress log](06_stage_2_progress_log.md) · [B-02 core loop and turn system](07_core_gameplay_loop_symbolic_world_and_turn_system.md) · [decision-closure audit](08_final_decision_closure_audit.md) · [DECISIONS.md](../DECISIONS.md) · [autonomous decision policy](../AUTONOMOUS_DECISION_POLICY.md)

---

## 1. Purpose and scope

### 1.1 What this document decides

This document is the authoritative rulebook for the boundary between a person and the game:

1. who may hold an account, and what an account is allowed to own;
2. how an account, a player profile and a nation relate, and what survives a nation's deletion;
3. how Nation Supremacy treats accounts observed on the same network, without treating a shared address as proof of cheating;
4. how a person creates a first nation and a replacement nation;
5. the standard starting state and the progression contract a new nation receives;
6. what an instant nation reroll is, what it destroys, what it preserves, and how it is confirmed;
7. the account lifecycle: registration, verification, recovery, suspension, closure and ban;
8. first-session onboarding, tutorial progress, newcomer protection and returning-player behaviour;
9. the data classes, retention limits and access boundaries these rules require;
10. the invariants, player journeys, messages, tests and cross-system contracts later prompts must satisfy.

Everything here is a **design specification**. No rule in this document has been implemented. The requirement register records **zero executed validations**; this document adds test specifications, not test results.

### 1.2 In scope

| Area | Decided here | Rule family |
|---|---|---|
| Account holder policy and ownership model | One account per person; one active nation; account/nation/history separation; enforcement limits | `ACC-001…ACC-049` |
| Shared-network interaction restrictions | Trusted signal, matching, states, interaction matrix, review, appeals, enforcement ladder | `NET-001…NET-061` |
| Nation creation and naming | Eligibility, idempotency, concurrency, name normalisation, rename, stable identity | `NAT-001…NAT-053` |
| Instant reroll | Definition, confirmation, reset boundary, survival, cross-system cleanup, anti-abuse | `RRL-001…RRL-034` |
| Onboarding, protection and return | First session, tutorial, newcomer protection, dormancy, progression contract | `ONB-001…ONB-052` |
| Privacy and data | Data classes, retention, access, deletion and anonymisation | `DAT-001…DAT-012` |
| Invariants and tests | 32 invariants and a 51-test specification | `INV-001…INV-032`, `T03-*` |

### 1.3 Out of scope (assigned, not silently decided)

| Not decided here | Owner | Why |
|---|---|---|
| Treasury values, resource yields, upkeep, starting grant *size*, deficit rule | Prompt 04, tuned in Prompt 14 | Economy numerics; Prompt 03 defines only the starting-state contract |
| Construction slots, building catalogue, research programmes | Prompt 05 | This document names the starting state, not the investment rules |
| Domestic-policy axes, stability values | Prompt 06 | Starting politics is a preset; its effects belong to Prompt 06 |
| Trade offer/accept mechanics, fair-value bands, listing-market gates | Prompt 07 | Prompt 03 fixes the transfer restriction shape; Prompt 07 fixes the trade rules |
| Treaty types, breach consequences, diplomatic reputation scope | Prompt 08 | Prompt 03 fixes the reroll and shared-network contracts only |
| Alliance roles, bank permissions, succession | Prompt 09 | Prompt 03 fixes membership status at reroll and the pair-bank prohibition |
| Campaign lifecycle, forfeit rule, protection states in war | Prompt 10 | Prompt 03 blocks reroll during an active campaign until Prompt 10 defines a forfeit |
| Rankings, achievements, world chronicle presentation | Prompt 11 | Prompt 03 fixes historical attribution and no transferable first-time rewards |
| Moderation tooling, sanction forms, appeal workflow implementation | Prompt 12 | Prompt 03 fixes the minimum policy, states and permissions |
| Screens, navigation, component behaviour | Prompt 13 | Prompt 03 writes messages and journey requirements, not visual design |
| Every formula, rounding rule and numeric value | Prompt 14 | All numbers here are labelled provisional anti-abuse parameters |
| Tables, RLS policies, functions, migrations, scheduler code | Stage 5 (architecture), Stage 6 (accounts) | This document is not a schema |
| Legal jurisdiction, age gate, privacy-law basis | Owner, prepared by Prompt 12 (UD-017) | Cannot be self-assigned |

### 1.4 How to read a rule

Each numbered rule carries a status and, where applicable, the requirement or decision it serves. Rules marked **Provisional** bind later Stage 2 prompts: a later prompt may change one only by editing this document and recording why (outline §3). A *player-facing* rule is still a design rule; it is not a promise that a screen exists.

**ID families used here.** `ACC-` account policy and ownership; `NET-` shared-network restrictions; `NAT-` nation creation, naming and starting state; `RRL-` reroll; `ONB-` onboarding, protection and return; `DAT-` data and privacy; `INV-` invariants; `T03-` tests; `J-` journeys; `MSG-` messages. None of these reuses an existing ID.

### 1.5 One-paragraph summary

One person may hold one account, and an account owns at most one active nation. An account is the persistent identity; a nation is the thing that can be lost. Two accounts observed on the same network may be restricted from interacting with each other until an authorised review clears the relationship, but a shared address is never by itself proof of multi-accounting and never justifies a permanent ban. A player may permanently delete their own nation and immediately create a replacement on the same account, with no gameplay cooldown; the old nation's assets, progress and standing are destroyed, while the account, its sanctions, its network relationships and the historical record survive. A replacement nation receives the same standard starting state as any other new nation, but not a second round of first-nation protection. No rule here is implemented or tested.

---

## 2. Source documents and design authority

### 2.1 What this document inherits

| Source | What it contributes | Authority here |
|---|---|---|
| [AI_CONTEXT](../AI_CONTEXT.md) §2 | Browser game, mapless world, 2-hour UTC cadence, Cloudflare Pages + Supabase, one account per person, free-first | Owner-stated constraints |
| [DECISIONS.md](../DECISIONS.md) D-018, D-021, D-025, D-026, D-028, D-029, D-030 | Multi-account prohibition; no catch-up; recovery/backup; retention; dormancy; verified e-mail; pending-act visibility | Confirmed decisions; this document applies them |
| [B-02](07_core_gameplay_loop_symbolic_world_and_turn_system.md) TR-015/016/017, TR-084…087, TR-096 | Membership by nation, ownership by account, identity through absence, no-presence rule, Prompt 03 inheritance | Provisional foundation rules |
| [Report 08](../stage-1/08_security_privacy_fair_play_and_trust.md) §4, §8, §11, §12, §13 | Recovery, shared-IP evidence limits, data inventory, moderation ladder, audit spine | Stage 1 evidence; proposals, not approvals |
| [Report 07](../stage-1/07_economy_design_and_market_structure.md) §12.5, §13, §19 | Fresh-account restrictions, starting-grant dependency, registration loops | Stage 1 evidence; numerics open |
| [Report 09](../stage-1/09_integrated_design_synthesis_and_readiness_audit.md) §12 | REQ-001…REQ-039 inherited text | Stage 1 evidence |
| [Prompt 01 registers](03_requirements_traceability.md) | REQ-001…REQ-060, DD-001…DD-048, UD-001…UD-030 | Stage 2 working registers |
| Politics & War public sources | Structural precedent for one-account, shared-network and reroll rules | Research findings only; never a rule by citation |
| Cloudflare and Supabase official docs | Trust boundary and platform behaviour | Provider evidence, dated in §21 |

**Precedence on conflict:** confirmed owner decision → this document (for B-03) → Stage 2 design register → Stage 1 report → proposal. A later prompt that finds a conflict edits the owning document and records the change; it does not leave two competing rules. **This document's own rule IDs are `ACC-`, `NET-`, `NAT-`, `RRL-`, `ONB-`, `DAT-`, `INV-`, `J-`, `MSG-` and `T03-`; its requirements are `REQ-061…REQ-097` (§19). It uses no ID that belongs to B-02 (`TR-`) or to the decision registers (`D-`, `DD-`, `UD-`).**

### 2.2 Conflicts found in the existing records, and how they were resolved

| # | Conflict or gap | Existing text | Resolution | Where recorded |
|---|---|---|---|---|
| C-1 | Multi-account policy | [Report 08](../stage-1/08_security_privacy_fair_play_and_trust.md) §8.1 recommended Option B, "one account per person with supervisory conditions", as a proposal | **D-018 chose prohibition**: one account per person, no capped multi-accounting. Report 08's option analysis remains historical evidence; its recommendation is superseded for policy. This document implements D-018 and does not reopen it | D-018; ACC-001/ACC-003 |
| C-2 | E-mail verification | Report 08 §4.1 left open the possibility of accepting unverified e-mail if the free e-mail budget could not carry verification | **D-029 requires a verified e-mail before nation creation at public launch** and makes custom SMTP mandatory for open registration. The old fork is closed; this document applies D-029 | D-029; ACC-001; NAT-001 |
| C-3 | Fresh-account trade restriction shape | Report 07 R-13 proposed that fresh accounts "cannot trade for their first N days at all" | Prompt 03 narrows the harm: the rule is **no one-sided transfer of value** during the fresh-nation window; reciprocal trade at fair value remains possible, subject to Prompt 07's band. Prompt 07 must update R-13's wording to match and own the numeric band. This is a deliberate refinement, not a silent reversal | §9.4; REQ-073; Prompt 07 |
| C-4 | IP retention | Report 08 §11.2 proposed 30-day retention of IP/network metadata, then aggregate-only | Prompt 03 is stricter: the application stores **no raw IP at all**, only a keyed digest for matching plus timestamps; the pair relationship is retained while it matters. The 30-day raw-IP posture is not adopted. Report 08's minimisation intent is preserved and strengthened | DAT-002/DAT-003 |
| C-5 | Verification method | Politics & War's official verification page asks for a photograph holding a signed paper | **Rejected.** Nation Supremacy uses no photograph, government identity document, biometric or precise address by default. Clearance is an authenticated attestation plus behavioural review (§5.6). Privacy-sensitive verification is a last resort, not a default | D-033; NET-030…NET-037 |
| C-6 | Inactivity and deletion | The community Politics & War FAQ describes vacation mode at 90 days and automatic deletion at 270 days | **Not copied.** D-028 already fixes dormancy at 14 days/168 turns, protection, no decay and reversible archival at 12 months; no automatic deletion. This document applies D-028 | D-028; ONB-017…ONB-020 |
| C-7 | Deliverable filename | The Stage 2 register and handoff named Prompt 03's document `08_nation_creation_and_progression.md`, but `08` is occupied by the [decision-closure audit](08_final_decision_closure_audit.md) | The authoritative path is **`09_account_onboarding_nation_creation_and_progression.md`**. The audit keeps its number; the register, outline and handoff are repointed here. No competing copy exists | §22.3; register/outline/handoff updates |
| C-8 | Newcomer protection vs catch-up | Report 07's EX-1 illustration includes a starting grant and line levels; ECOQ-003 leaves the grant size open because it interacted with FO-018 | **D-021 forbids catch-up acceleration.** Prompt 03 defines the starting-state *structure* and leaves every number to Prompt 04/Prompt 14. No catch-up bonus, veteran tax or accelerated yield is introduced | D-021; §9; NAT-017…NAT-020 |
| C-9 | Reroll during a war | No existing rule covered a nation deleting itself mid-campaign | Fail-closed default: reroll is **blocked while the nation is a participant in an active campaign**, pending Prompt 10's forfeit rule. This avoids silently erasing an opponent's legitimate outcome. It is a state condition, not a cooldown | RRL-013; UD-032 |
| C-10 | Account-level vs nation-level reputation | Report 08 and the diplomacy material did not settle whether a treaty breach follows the account or the nation | Prompt 03 requires the **old nation's acts to remain attached to the old nation identity**, and requires that a reroll must not erase an *enforcement* sanction. Whether in-game diplomatic reputation is account-scoped is left to Prompt 08, with an explicit anti-abuse contract | RRL-014; UD-033; Prompt 08 |

**No conflict was resolved by deleting the older text.** Reports 07–09 and the audit keep their wording as dated evidence; the decision log and this document carry the current rule.

---

## 3. Research findings — Politics & War

### 3.1 Purpose and method

The purpose is to learn the **policy structure**, not to copy another game's wording, interface, artwork, private-data practice or complete rulebook. Sources were fetched on **2026-10-24**. Source type is stated for every claim, because a forum post is not proof that a mechanic is current.

### 3.2 Sources consulted

| # | Source | URL | Type | What it showed | Confidence | Access note |
|---|---|---|---|---|---|---|
| P1 | Registration page | `https://politicsandwar.com/register/` | **Official** page | The page exists and is branded "Create a Nation and Start Playing"; the fetched text is the site shell, not the registration policy | Low for policy; high for existence | No account was created; no form was submitted |
| P2 | Game Rules | `https://politicsandwar.com/rules/` | **Official** rulebook | Rule 1: no individual may have more than one nation "for any reason"; nation-sitting prohibited. Rule 2: no limit on nations per network if each is owned and controlled by a separate individual; automatic restrictions on same-network nations; using Alliance Banks to evade same-network trade restrictions is bannable; same-network nations may share an alliance but may not declare wars on the same nations. Rule 3: new nations may not send all or most money/resources; nations created solely to send value are a serious violation. Rule 11: one account, not sellable or transferable. Rule 16: use of a brand-new nation's starting protection to shield an alliance bank is prohibited. The page also describes a moderation-points ladder with expiry and two-moderator approval | **High** | Full text fetched |
| P3 | P&W-pedia Terminology Glossary | `https://politicsandwar.com/pwpedia/article/Terminology-Glossary` | **Official domain, community-maintained** (page says "maintained by Team PnWPedia") | Defines **Reroll**: "Someone who deleted their nation and made a new one" | Medium-high | Full text fetched |
| P4 | Frequently Asked Questions | `https://politicsandwar.fandom.com/wiki/Frequently_Asked_Questions` | **Community wiki (Fandom)** — not official | One account/nation maximum; different people may play from the same network but "cannot interact in-game in any way": no wars against each other, no sweetheart trades, no alliance-bank transfers, no third-nation intermediary, no both fighting the same nation; many restrictions are mechanically imposed and can be removed by verification. New nations under 30 days cannot buy resources outside ±30% of the average market price; same-network-flagged nations face the same band on buying and selling. Inactivity: vacation mode after 90 days, deletion after 270 days. Messages blocked for a new nation's first 3 minutes | Medium (community; may lag the live game) | The HTML page returned **403**; the same page's wikitext was retrieved through the Fandom MediaWiki API, which is the community wiki's own content endpoint |
| P5 | Forum thread: "What can people living in the same house do and not do" | `https://forum.politicsandwar.com/index.php?/topic/31880-...` | **Community forum** | The topic shell and title were fetched; the reply bodies were not rendered. It confirms such a thread exists, not what current staff policy says | **Low** | Body unavailable; no claim is based on it |
| P6 | Forum thread: "How to Start Over?" | `https://forum.politicsandwar.com/index.php?/topic/8112-how-to-start-over/` | **Community forum** | The topic shell and opening description were fetched (a player asking how to restart without a second account); replies were not rendered | **Low** | Body unavailable; no claim is based on it |
| P7 | Privacy Policy | `https://politicsandwar.com/privacy/` | **Official** | Collects IP address, browser, time zone and cookies; uses IP to screen for risk and fraud. "Verification" is **completely optional and never required to play**; it requires sending a personal photograph by e-mail, stored on an offline server, used only to check that one person is not operating multiple accounts; never public; destroyed if the game is sold; not kept after a user quits or deletes the account. The game is not intended for under-13s | **High** | Full text fetched |
| P8 | Account Verification page | `https://politicsandwar.com/account/verification/` | **Official** | Verification is only necessary for shared networks (university, work, home); it allows unrestricted interaction; each person is still allowed one nation; 13+. The process requires an e-mail from the account address with nation name, leader name, nation ID, and a photograph holding a handwritten sheet stating the date, ownership, age 13+, sole account, shared-network location and a signature. Approved verification lasts 30 days; renewal lasts 6 months; later renewals 1 year; renewals ensure ownership is not transferred. "No one needs to be verified"; verified nations show a checkmark next to "Founded" | **High** | Full text fetched |
| P9 | "Edit Nation" wiki page | `https://politicsandwar.fandom.com/wiki/Edit_Nation` | **Community wiki** | The Edit Nation page lets a player change nation details, **delete their nation**, or enter Vacation Mode | Medium | Retrieved through the MediaWiki API after the HTML was blocked |
| P10 | Search-result snippets for nation deletion | Forum and Reddit results returned by a web search | **Community, unverified snippets** | Snippets suggest deletion is irreversible, that a recent transaction ("past 3 days") or an active offensive war can block deletion, and that deletion lives on the Edit page | **Low** | Pages not opened or not renderable; these are search snippets, not verified current rules. They are recorded as leads only |

### 3.3 What the official sources establish

1. **One account, one nation.** The official rules prohibit more than one nation per individual "for any reason" and prohibit nation-sitting. The FAQ states the same rule in player language.
2. **Shared networks are legitimate, with restrictions.** The official rules explicitly allow multiple nations per network when each is owned and controlled by a separate person, and state that automatic restrictions apply. The official verification page says verification is only necessary for shared networks and is optional.
3. **The restricted interactions are broad.** The rules name trades, alliance-bank transfers, and wars against the same nations; the FAQ adds sweetheart trades, third-nation intermediaries and coordinated wars. The structure is a **pairwise interaction restriction**, not a network-wide ban.
4. **Rerolling is a recognised, named behaviour.** The official-domain glossary defines a reroll as deleting a nation and making a new one.
5. **Verification is privacy-sensitive.** The official process collects a photograph and a signed statement. The privacy policy says the material is optional, stored offline, never public, and destroyed on sale or account deletion. This is exactly the kind of sensitive collection Nation Supremacy must evaluate rather than copy.
6. **Newcomer protection exists and is abusable.** Official rule 16 treats a brand-new nation's starting protection as an asset that can be abused to shield an alliance bank. The design lesson is that protection must be account-scoped and not repeatable by rerolling.
7. **Moderation is graduated.** The official rules use a points ladder with expiry and a two-moderator approval for moderation actions. The design lesson is a published, proportionate ladder; the numbers and mechanisms are not copied.

### 3.4 What only community sources establish (and how it is treated)

| Claim | Source type | Treatment |
|---|---|---|
| New nations under 30 days face a ±30% trade-price band; same-network-flagged nations face the same band | Community FAQ | **Adapted in structure, not copied.** Prompt 03 uses a fresh-nation *one-sided transfer* restriction and assigns the fair-value band and duration to Prompt 07/Prompt 14 |
| Inactivity: vacation mode at 90 days, deletion at 270 days | Community FAQ | **Not adopted.** D-028 already fixes dormancy at 14 days and reversible archival at 12 months, with no automatic deletion |
| Deletion is irreversible; a recent transaction or active war can block it | Forum/Reddit snippets | **Treated as a lead only.** Prompt 03 independently chooses irreversibility and a fail-closed campaign block; it does not claim P&W's current mechanic |
| "No interaction in any way" between same-network players | Community FAQ | **Adapted.** The interaction matrix in §6.5 is Nation Supremacy's own, broader and explicit; it does not rely on the FAQ's phrase |
| Verified players receive a public checkmark | Official verification page | **Not adopted.** Clearance is private by default; a public badge would expose a sensitive status and create pressure to disclose identity |

### 3.5 What was deliberately rejected

| P&W pattern | Why it is not copied |
|---|---|
| Photograph plus signed paper as the standard verification | Disproportionate collection of sensitive personal data for a browser game; creates a breach and minors-risk surface; conflicts with the project's minimisation posture |
| Optional verification as the *only* route to normal interaction | Leaves unverified legitimate players permanently restricted; Nation Supremacy offers a review route that does not require identity documents |
| A public "verified" badge | Turns a private anti-abuse status into a social rank and pressures disclosure |
| A 30-day price band as the sole anti-farming control | A price band alone does not cover gifts, banks, third-party routing or coordinated war; Prompt 03 uses an explicit interaction matrix plus a fresh-nation transfer rule |
| Nation deletion blocked by a fixed multi-day timer | Nation Supremacy requires **instant** rerolling; the design uses state conditions (active campaign, pending settlement, preservation order) instead of a timer |
| Automatic deletion after months of inactivity | Conflicts with D-028 and DP-002; archival is reversible and disclosed |
| Exact moderation-point values and expiry periods | P&W's numbers are its own; Nation Supremacy records a proportionate ladder and leaves operational values to Prompt 12 |

### 3.6 Research limitations

- The registration page was fetched as a shell; no registration was attempted, so no statement is made about its form fields or current validation.
- Both forum topics returned only their topic shells. Their reply bodies could not be read, so no rule is based on them.
- The Fandom HTML pages returned 403; the wiki's own API was used. That is still **community** content and may lag the live game.
- P&W's public rules can change; this is a dated snapshot, not a claim about P&W's current or future state.
- No P&W account was created and no logged-in page was inspected. The research therefore cannot confirm deletion preconditions, verification renewal enforcement or the live behaviour of automatic restrictions.
- The research supports **policy structure**. It is not evidence that Nation Supremacy's rules will work, be fair, or be enforceable.

---

## 4. Account holder policy — one account and one nation per person

### 4.1 The core rule

**ACC-001 — One account, one active nation.** *Approved policy (owner constraint; D-018; REQ-043 and REQ-061).* A human player may hold **one game account** and that account may hold **at most one active nation** at any moment. The two halves are different rules: the first is about people, the second about ownership. Neither is a technical claim that every person can be identified.

**ACC-002 — The account is the persistent identity; the nation is the replaceable one.** *Approved policy.* Authentication credentials, the account, the player profile, account-level settings, tutorial progress, sanctions and network relationships belong to the account. A nation is a political entity owned by that account. A reroll replaces the nation and leaves the account intact (§7).

**ACC-003 — Prohibited evasions.** *Approved policy (D-018).* A person may not evade ACC-001 by any of:

1. registering another account with a different e-mail address;
2. using another browser, device or profile to run a second account;
3. using a VPN, proxy, carrier change or other network change to conceal a second account;
4. using another person as a nominal account holder while controlling that account;
5. sharing, lending, selling or transferring account access;
6. operating a secondary account to transfer resources, coordinate warfare, influence an alliance or manipulate a market;
7. deleting a nation and recreating it to obtain a second account, reset a sanction or bypass a moderation decision.

**ACC-004 — A permitted reroll is not a second account.** *Approved.* Deleting one's own nation and immediately creating a replacement on the **same** account is allowed and is specified in §7. It does not require a new registration, a new e-mail address or an operator's approval.

**ACC-005 — Households and shared devices.** *Approved policy (D-018).* Two or more people living at one address may each hold an account, provided each account is owned and controlled by a different person and credentials are not shared. Their accounts become subject to the shared-network interaction policy (§5). "We live together" is a complete explanation for a shared network observation; it is not, by itself, a defence against behavioural evidence of a single operator.

**ACC-006 — Proportionate enforcement, not perfect identification.** *Approved policy (D-018).* The game cannot conclusively determine how many humans stand behind an account by inspecting an IP address, device, browser, e-mail address or login history. The policy is therefore enforced by a combination of mechanical controls and evidence-based review. No text in this project may claim that one-person-per-account is perfectly enforced.

**ACC-007 — No sensitive identity verification by default.** *Approved policy direction (C-5).* Government identification, face photographs, biometric identifiers, precise home addresses and similar sensitive data must not be required to play or to clear a shared-network restriction. A future proposal to require them needs a separately justified necessity, a documented safeguards review, an owner decision and a legal review; it is not a default.

**ACC-008 — No account or nation transfer.** *Approved policy.* An account, a nation, a place in an alliance or a historical identity may not be sold, gifted, inherited or transferred between people. Account recovery restores the *same* account to its rightful holder; it is not a transfer mechanism.

**ACC-009 — Account holders are responsible for their credentials.** *Provisional.* A player is responsible for keeping their password, recovery codes and sessions secure. Sharing credentials is prohibited. A compromised account is handled as a security incident (§10.8), not as a permitted way to let another person play.

**ACC-010 — Age and legal eligibility.** *Provisional, pending UD-017.* Registration must state a minimum age of **13** and require the person to confirm it, matching common platform practice and the P&W precedent; the game must not collect a birth date unless a legal review requires it. The applicable jurisdiction's age and privacy rules remain **UD-017**, an owner/legal question for Prompt 12 before public launch. This paragraph is a design posture, not a legal-compliance claim.

**ACC-011 — Data minimisation at the account boundary.** *Provisional (REQ-023; DAT-001).* Registration collects an e-mail address, a password and a player handle. It does not collect a real name, postal address, phone number, government identifier, photograph or precise location. A nation name is a public game identity, not a civil identity.

### 4.2 The ownership model

**ACC-012 — Object model.** *Provisional.* The design recognises these objects. The table is a vocabulary, **not a schema**; Stage 5 owns tables and Stage 6 owns authentication wiring.

| Object | Identity | Cardinality | Lifetime | Public? |
|---|---|---|---|---|
| **Human player** | Not identifiable by the system; a policy subject | 1 person → 1 account (policy) | Real world | Never modelled as data |
| **Authentication identity** | Supabase `auth.users` record (or successor) | 1:1 with the game account | Until account closure; credentials can change | Never public |
| **Game account** | Immutable `account_id` (UUID), separate from the auth UID | 1:1 with auth identity; 1 person per account (policy) | From registration until closure | Never public as an account; only its nation is public |
| **Player profile** | 1:1 with account | 1:1 | Account lifetime | Handle and public preferences only |
| **Active nation** | Immutable `nation_id` (UUID) plus a public nation number | 0..1 per account at any moment | From creation to retirement | Public identity; private state |
| **Nation history** | Prior `nation_id` values | 0..n per account | Permanent class-P record; bounded class-S detail (D-026) | Public historical identity; no account link |
| **Reroll / retirement record** | `retirement_id` | 0..n per account | Permanent | Not public as a record; the old nation's status is public |
| **Enforcement record** | `case_id` | 0..n per account | Class-O floor, 12 months after closure of the case unless an open case requires longer (D-026) | Never public; outcome may be disclosed to the affected account only |
| **Network association** | `(account_id, network_key)` | 0..n per account | 180 days after last observation (provisional) | Never public |
| **Pair relationship** | `(account_low, account_high)` canonical pair | 0..n per account | Active restriction plus 12 months after closure | Never public |

**ACC-013 — The account ID is stable.** *Provisional.* Changing an e-mail address, password, player handle or nation does not change `account_id`. A closed account's ID is never reused. Historical records reference `account_id` internally and `nation_id` publicly.

**ACC-014 — One active nation, enforced at the transaction.** *Approved policy; mechanism provisional (REQ-061).* The database must enforce at most one row per account with `nation.status = 'ACTIVE'`, using a partial unique constraint or an equivalent transaction-safe mechanism, and nation creation must take a per-account lock before checking. Application code alone is not sufficient: concurrent requests, retries and interrupted operations must not be able to create two active nations. The design requirement is absolute; the implementation is Stage 5/6.

**ACC-015 — Ownership is resolved server-side on every action.** *Provisional (REQ-002).* The acting account is derived from the authenticated session, never from a request parameter. Every nation-scoped action checks that the authenticated account is the nation's owner. A client-supplied `account_id`, `nation_id` or e-mail address is an object reference to be authorised, never an identity claim.

**ACC-016 — Account status and network restrictions are separate objects.** *Provisional.* A shared-network restriction is a property of a **pair of accounts**, not a suspension of either account. An account can be in good standing and simultaneously be restricted from interacting with one other account. Conversely, an account-level suspension applies to the account regardless of any pair relationship. Mixing the two would either punish innocent network neighbours or let a restricted pair escape by presenting the restriction as an account ban. §5.4 defines the states.

### 4.3 What the rule does and does not mean

| The rule means | The rule does not mean |
|---|---|
| One person should hold one account and one active nation | The system can prove how many people are behind an account |
| Household members may each play, with interaction limits | Everyone on a shared network is a cheater |
| A player may reroll on the same account | A player may open a second account to keep the old nation |
| Enforcement is evidence-based, published and appealable | Every suspicion results in a ban |
| The account survives a nation's deletion | Sanctions or network restrictions disappear with the nation |
| A shared IP can trigger an interaction restriction | A shared IP justifies a permanent ban by itself |
| The game avoids sensitive identity collection | The game has no anti-abuse controls at all |

### 4.4 Ownership flow (conceptual)

```
Person
  │ registers (e-mail + password + 13+ confirmation)
  ▼
Authentication identity ──1:1──► Game account (immutable account_id)
                                     │
                                     ├── Player profile (handle, settings, tutorial progress)
                                     ├── Active nation (0..1) ──► public nation identity
                                     ├── Nation history (0..n) ──► public historical pages
                                     ├── Enforcement record (0..n) ──► restricted
                                     └── Network associations / pair relationships ──► restricted
```

The diagram is an ownership map, not a database diagram. The arrow from person to authentication identity is a **policy expectation**, not a measurable link.

---

## 5. Shared-network interaction restrictions

### 5.1 The principle

**NET-001 — A shared address is a signal, not an identity.** *Approved policy (REQ-062/REQ-066).* Two accounts observed on the same public network may be restricted from interacting with each other. That observation never proves that one person controls both accounts, and it never by itself justifies a permanent ban. The restriction is a **pairwise interaction control**, not an account suspension and not a finding of cheating.

**NET-002 — Why the control exists.** *Approved policy.* A shared network makes value transfer, market manipulation and coordinated warfare between the accounts unusually cheap to arrange and unusually hard to distinguish from ordinary cooperation. The game therefore isolates the pair's value-moving and coordinating verbs until a human review clears the relationship. The control protects the world's economy and wars, not the game's reputation for catching cheaters.

**NET-003 — Independence is the goal.** *Provisional.* The affected accounts may continue to build, produce, research, trade with third parties, join alliances, participate in public rankings and use every non-restricted surface. The restriction is limited to interactions that could move value or create a coordinated advantage between the pair. A legitimate student, sibling or colleague must be able to keep playing.

**NET-004 — No collective punishment.** *Approved policy.* A shared network is never banned, throttled or labelled as a group. Restrictions attach to a canonical **pair** of accounts, not to an IP address, a household, a school or a carrier. A large shared network must not produce account-level suspensions merely because many accounts were observed on it.

### 5.2 The trusted network signal

**NET-005 — The browser is never asked for its IP.** *Provisional security design (REQ-065).* No request body, query parameter, cookie or client-computed field may supply an IP address or a network identifier. A client-supplied value is ignored completely, even if it looks plausible.

**NET-006 — Collection point.** *Provisional security design.* The trusted collector is a **Cloudflare Pages Function** on the game's own origin. It reads the `CF-Connecting-IP` request header that Cloudflare provides for the incoming request. It does **not** read `X-Forwarded-For` (which appends proxy addresses and is not a single authoritative value), and it does not read `X-Real-IP`. Cloudflare's documentation states that `CF-Connecting-IP` provides the client IP address to the origin and that `X-Forwarded-For` may contain a chain; this is why only the former is used.

**NET-007 — Normalisation.** *Provisional.* Before matching, the signal is normalised:

| Input | Normalised network prefix | Note |
|---|---|---|
| IPv4 public address | The address itself | A household or small office typically shares one |
| IPv6 public address | The first 64 bits (`/64`) | A residential IPv6 allocation commonly gives a whole /64 to one site |
| Loopback, link-local, private, documentation, multicast or unspecified ranges | **Discard** | Not a public network observation |
| Cloudflare-internal or known proxy egress range | **Discard** | Prevents matching the platform, not the player |
| Missing, malformed or ambiguous value | **No signal** | High-risk verbs fail closed (§5.3); low-risk actions proceed and the gap is logged |

**NET-008 — Keyed digest, not an address.** *Provisional security design (DAT-002).* The Pages Function computes a keyed digest, `network_key = HMAC-SHA-256(normalised_prefix, pepper)`, using a secret held in the Worker's environment and never in the database, the repository or the browser. Only the digest is sent to Supabase. The application database stores **no raw IP address** for matching. The pepper is stable for the world; rotating it requires a documented re-keying plan or a deliberate matching gap, because old and new digests will not match.

**NET-009 — Server-side persistence.** *Provisional.* The Function authenticates the player's Supabase session, derives `account_id` from the verified token, and calls a Supabase function using a server-only credential. The function writes `(account_id, network_key, observed_at, source='page_function')` into a restricted table. The browser has no grant to read or write that table. `service_role` bypasses row-level security, so the server credential must never reach the client (Supabase's own documentation says this).

**NET-010 — Enforcement point.** *Provisional.* Pair evaluation and the block/allow decision run in a server-side function, in the same transaction as the action being attempted. A client cannot disable the check by changing a field, calling a different endpoint or editing local state. The Pages Function may perform an early check for responsiveness, but the authoritative check is the one that commits or rejects the action.

**NET-011 — Where the signal is recorded.** *Provisional.* The signal is recorded for:

1. account creation and first nation creation;
2. each authenticated session start (not every page view);
3. each high-risk verb in the interaction matrix (§5.5) that has a network dimension;
4. a reroll confirmation;
5. a recovery sign-in.

Recording on session start keeps the data volume small and matches the 2-hour cadence; recording on every request would be disproportionate.

**NET-012 — No trust in the request path.** *Provisional.* The Function ignores any `CF-Connecting-IP` value that arrives through a subrequest it did not receive directly from Cloudflare's edge. Cloudflare's documentation warns that Worker subrequests can alter `CF-Connecting-IP` and `X-Real-IP`; the implementation must therefore read the header from the incoming request and must not forward a user-controlled header set. Verifying that a forged header cannot reach the Function is a Stage 6 test (`T03-D03`), not a claim made here.

**NET-013 — Unknown network is not a bypass.** *Provisional.* If a high-risk verb arrives without a trustworthy signal, the action is rejected with a retryable technical reason (`AC-20`) and the gap is logged. A player cannot obtain an unrestricted transfer by stripping a header or using a client that does not send one. Low-risk actions that do not move value may proceed so a temporary platform fault does not lock the game.

### 5.3 Observation, matching and thresholds

**NET-014 — Observation window.** *Provisional parameter (`W_obs`).* A pair is **observed** when both accounts have a network observation on the same `network_key` within a rolling **24-hour** window. The window is evaluated at the moment of the attempted action, not only at daily maintenance.

**NET-015 — Pair record.** *Provisional.* The system stores a canonical pair `(account_low, account_high)`, the shared `network_key` digest, first and last shared observation times, the current state, the review status and the case reference. It does not store a list of every IP either account has ever used. The pair record is the minimum needed to apply and review the restriction.

**NET-016 — Pair observation lifetime.** *Provisional parameter (`R_obs`).* An `OBSERVED` pair with no further shared observation for **180 days** returns to `NONE`. A `RESTRICTED` or `MAINTAINED` pair does **not** expire while the restriction is in force; only a review decision or account closure ends it. This is the rule that prevents a player from clearing a restriction by changing networks.

**NET-017 — Action-triggered restriction.** *Provisional.* A pair moves from `OBSERVED` to `RESTRICTED` when:

1. either account attempts a restricted verb against the other while the pair is observed; or
2. an operator applies the restriction after independent evidence; or
3. a `CLEARED` pair re-enters on new evidence (§5.4).

The attempted action is rejected before any value moves, ownership changes or a war declaration becomes effective. The first attempt is therefore not a free attempt.

**NET-018 — Proactive restriction.** *Provisional.* An operator may apply `RESTRICTED` before an interaction is attempted when independent evidence supports it (for example a confirmed multi-account admission, a transaction graph showing a circular flow, or a prior `MAINTAINED` decision). The decision is logged with a reason and is appealable. IP matching alone is not sufficient for a proactive restriction beyond the automatic action-triggered path.

**NET-019 — Large shared networks.** *Provisional parameter (`L_large`).* A `network_key` observed for more than **25 distinct accounts** in a rolling 24 hours is classified **LARGE** (a university, office, carrier NAT or public Wi-Fi). On a LARGE network:

1. no account is pre-restricted against every other account;
2. a high-risk verb between a newly observed pair is still blocked, because value must not move before review;
3. the pair becomes `RESTRICTED` only after a second shared observation at least **6 hours** apart within 7 days, or an operator decision; until then it is `OBSERVED` and each high-risk attempt is independently blocked;
4. the review queue is expedited and the pair receives a plain-language explanation that large shared networks are common and the block is not an accusation;
5. aggregate metrics count blocked attempts, cleared pairs and review times, but never publish a list of accounts on a network;
6. no account-level suspension or ban follows from the size or identity of the network.

**NET-020 — False-positive posture.** *Provisional.* A blocked legitimate interaction is a cost, not a conviction. The player is told what happened, why, and how to request review. If review finds unrelated players or an incorrect match, the pair is `CLEARED` with the basis `FALSE_POSITIVE`, the block is removed, and the correction is recorded. The game does not compensate game value that never moved; it does correct the record and the status.

### 5.4 Relationship state model

**NET-021 — Five relationship states and a separate review status.** *Provisional.* The design uses five states, not seven. "Restriction under appeal" is a **review status**, not a sixth relationship state, because an appeal does not change what is allowed while it is pending. This avoids duplicate states that would drift apart in implementation.

| State | Entry conditions | Allowed | Prohibited | Player-visible explanation | Review and exit | Audit | New evidence |
|---|---|---|---|---|---|---|---|
| **NONE** | No shared observation in the window, or the pair expired after 180 days | Everything | Nothing by this policy | No message | — | Observation history only | A new shared observation → OBSERVED |
| **OBSERVED** | Both accounts observed on the same key within 24h; no restricted verb attempted yet | All non-restricted play; high-risk verbs are checked and blocked if attempted | Nothing yet, but a high-risk attempt is rejected | Only shown when an action is blocked: "These accounts recently used the same network. This interaction is limited while the relationship is reviewed." | Review may be requested voluntarily; a restricted attempt → RESTRICTED; 180 days without a shared observation → NONE | Pair record and block events | A restricted attempt → RESTRICTED; a second observation on a LARGE network → RESTRICTED; an operator decision → RESTRICTED or CLEARED |
| **RESTRICTED** | A restricted verb was attempted between an observed pair, or an operator applied it on independent evidence | Public play; building, production, research; trade with third parties; alliance membership subject to §5.5; diplomacy with third parties; rankings; support | Every verb marked Block or Prohibit in §5.5 | "Interactions between these two accounts are restricted because they recently used the same network. This is an interaction limit, not a finding that you cheated. You can request a review." | Review request → review_status REQUESTED; decision → CLEARED or MAINTAINED; account closure → CLOSED | Every block, review act and decision | New independent evidence may reopen a CLEARED pair; a MAINTAINED pair may be reviewed after 30 days or on new evidence |
| **CLEARED** | Review found separate people or a false positive | Everything, subject to the 90-day probation watch | Nothing by this policy | "The shared-network review is complete; the interaction limit has been removed." | Probation 90 days; new shared observation plus a value-transfer signal → RESTRICTED with priority review; no new evidence → NONE after probation | Decision, basis, reviewer, date | New evidence → RESTRICTED (priority) |
| **MAINTAINED** | Review found the relationship inconclusive or a likely duplicate | Same as RESTRICTED | Same as RESTRICTED | "The interaction limit remains after review. You can appeal the decision." | Appeal → review_status APPEALED; a later review may CLEAR; account closure → CLOSED | Decision, reason, appeal record | New evidence → review; a confirmed duplicate → account-level enforcement (separate) |

**NET-022 — Review status values.** *Provisional.* `review_status` is one of `NONE`, `REQUESTED`, `IN_REVIEW`, `DECIDED`, `APPEALED`. The relationship state remains `RESTRICTED` or `MAINTAINED` while a request or appeal is open. A decision records one of: `SEPARATE_PEOPLE`, `FALSE_POSITIVE`, `INCONCLUSIVE`, `LIKELY_DUPLICATE`, `REFERRED_TO_ENFORCEMENT`, `ACCOUNT_CLOSED`. The pair's state and the review status are stored separately so that an appeal never accidentally lifts a restriction.

**NET-023 — Player-visible status.** *Provisional.* Each account can see its own pair statuses, the counterparty's public nation identity, the date of the block, and the review route. It cannot see the other account's e-mail, account ID, IP, network key, login history, enforcement record or the exact detection thresholds. A pair status is private to the two accounts; it is never published on a nation page or in a ranking.

**NET-024 — A restriction is not a sanction.** *Provisional.* `RESTRICTED` and `MAINTAINED` do not reduce score, remove a nation, freeze production or appear as a punishment in the account's record. They are interaction controls. Only the account-level ladder (§5.8) imposes sanctions, and only on independent evidence.

---

### 5.5 The interaction matrix

**NET-025 — The matrix is the policy.** *Provisional (REQ-063).* The following table is the complete default matrix for a pair in `OBSERVED`, `RESTRICTED` or `MAINTAINED`. **Block** means the server rejects the action before any state changes. **Prohibit** means the action is a rule violation; it may not be mechanically preventable in every route, so it is detected, recorded and reviewed, and the burden is on the player not to structure around it. **Allow** means permitted. **Conditional** means permitted only under the stated condition.

| # | Interaction | Examples | Policy | Enforcement | Owning prompt |
|---|---|---|---|---|---|
| 1 | Direct treasury transfer | Gift, aid, subsidy, cash transfer, debt repayment | **Block** | Server rejects at submission; no reservation, no movement | 04/07 |
| 2 | Direct material transfer | Gift or transfer of any MAT class | **Block** | Same as row 1 | 04/07 |
| 3 | Directed trade with the paired account | Offer, accept, counter, settle | **Block** | Offer cannot be created or accepted; matching engine excludes the pair | 07 |
| 4 | Market or listing match with the paired account | Anonymous order book, listing purchase | **Block** at match | Matching engine must evaluate the pair before reserving; the listing market may only launch if it can do so (Prompt 07) | 07 |
| 5 | Asset swap or exchange of any value | "You build my city, I send you steel" | **Block** when it is a transfer; **Prohibit** when disguised as independent play | Review of transfer graph and action logs | 07/12 |
| 6 | Alliance bank deposit or withdrawal by either account | Deposit, withdraw, transfer, grant | **Block** | While a pair is restricted, neither account may use an alliance-bank transfer surface. Existing balances remain; automatic taxes are not a transfer to the pair | 09 |
| 7 | Alliance grant or subsidy to a restricted account | Leader sends pool funds to the account | **Block** | Grant function checks the recipient's pair state; a grant from a pool controlled by the paired account is also blocked | 09 |
| 8 | Alliance-bank routing through a third member | A deposits, B withdraws for C, C sends to A | **Prohibit** | Transaction-graph review; bank permissions may be frozen while a case is open | 09/12 |
| 9 | Attack against the paired account | Declare war, launch a campaign operation | **Block** | War declaration and every offensive order re-check the pair | 10 |
| 10 | Both declare war on the same third nation | Same target, same window | **Block** the later declaration; **Prohibit** coordination around an existing shared target | War declaration check; campaign participation review | 10 |
| 11 | Join the same campaign on the same side | Both join an alliance war or a world objective | **Block** | Campaign membership check | 10/11 |
| 12 | Joint operations or support | Reinforce, supply, shield, fund a campaign | **Block** | Support verbs check the pair; no value or readiness may move | 10 |
| 13 | Coordinated attacks on a third player | Same target, alternating turns, one softens and the other finishes | **Block** when detectable as a joint operation; **Prohibit** otherwise | Campaign logs and battle reports reviewed; no automatic ban | 10/12 |
| 14 | Espionage or intelligence against each other | Spy, scout, infiltrate | **Block** if espionage is adopted | Server rejects the operation | 10 |
| 15 | Treaty or formal agreement between the pair | NAP, trade pact, defence pact | **Block** | Diplomacy function checks the pair | 08 |
| 16 | Alliance membership together | Same alliance | **Conditional** | Allowed, but rows 6–8 and 18 apply; no simultaneous bank-authorising role | 09 |
| 17 | Voting for each other in an alliance election | Leadership vote | **Block** if elections are adopted | Ballot function checks the pair | 09 |
| 18 | Shared alliance benefit that is a material transfer | Pool-funded building, direct grant, resource stipend | **Block** | Only public, non-transferable benefits are allowed | 09 |
| 19 | Public market participation with third parties | Buy, sell, trade with an unrelated account | **Allow** | Normal trade rules; the pair is not a counterparty | 07 |
| 20 | Public world participation | Build, produce, research, rank, post, join an alliance, sign a treaty with a third party | **Allow** | Normal rules | All |
| 21 | Indirect value transfer through a third account | A sends to C, C sends to B; C is a friend, alt or paid intermediary | **Prohibit** | Transfer-graph audit; structuring is itself a violation. Detection is not claimed to be complete | 12 |
| 22 | Using a reroll to create a fresh nation and interact | Delete, recreate, then trade with the paired account | **Block** | Network associations and pair records are account-level and survive the reroll (RRL-011) | 03/12 |
| 23 | Account recovery | Restore access to the existing account | **Allow** | The pair restriction does not block recovery | 03/06 |
| 24 | Support and appeal contact | Ask for help, file an appeal | **Allow** | No restriction | 12 |
| 25 | Any verb added later that moves value or creates a coordinated advantage | New subsystem, event or alliance tool | **Default Block until reviewed** | The subsystem owner must add a pair check before launch; an unclassified value-moving verb is a specification defect | Later prompt |

**NET-026 — Indirect routes are covered.** *Provisional.* The prohibition in rows 5, 8, 13 and 21 is deliberately wider than a pairwise check. A player may not achieve through an alliance, a third nation, a market mechanism, a gift chain, a loan, a campaign or a timed sequence what the matrix forbids directly. Mechanical prevention is required where the system can see both legs; where it cannot, the act is a rule violation supported by the audit record. The design does not claim that every indirect route is automatically detectable.

**NET-027 — The pair may not use the bank.** *Provisional.* While a pair is `RESTRICTED` or `MAINTAINED`, neither account may deposit to, withdraw from or transfer through an alliance bank. The accounts may remain members and may receive non-transferable public benefits. This is a deliberate over-inclusion: a bank transfer is not pairwise attributable once it enters a pool, so the safe rule is that the pair cannot use the pool at all until cleared. If the pair is already in the same alliance, the restriction does not eject them; it suspends their bank permissions and records the conflict for the alliance's leadership.

**NET-028 — Public participation stays open.** *Provisional.* A restricted account may still build, produce, research, trade with third parties, join an alliance, sign a treaty with a third party, appear in rankings, read the chronicle and contact support. A restriction that quietly stopped ordinary play would be an account suspension by another name and would breach NET-024.

**NET-029 — A blocked action moves nothing.** *Provisional.* A block occurs before reservation, before ownership change, before a war declaration becomes effective and before a transfer is recorded. The action receives a stable reason code (`AC-08` or `AC-09`) and no cost is charged. A blocked attempt is recorded as an event, not as a completed action.

### 5.6 Verification, review and clearance

**NET-030 — The review exists; identity documents do not.** *Approved policy direction (C-5, D-033).* A legitimate pair must have a realistic route to clearance. The route is an **authenticated attestation plus an evidence-based review**, not a photograph, government ID, biometric or home address. The review is designed to distinguish separate people from a single operator as well as the available evidence allows; it does not pretend to be a proof of personhood.

**NET-031 — Who may request.** *Provisional.* Either account in the pair may request review. One open request covers the pair. A request may be made from the restricted-interaction message, the account's security page, or a support route. The request is authenticated; an unauthenticated e-mail is not enough to change a pair's state.

**NET-032 — What the attestation asks.** *Provisional.* Each account submits, in its own session:

1. a statement that it is controlled by a different person from the other account;
2. the nature of the shared network (household, university, workplace, public access, other);
3. confirmation that credentials, sessions and recovery codes are not shared and that neither person controls the other's account;
4. confirmation that the interaction limits are understood and that value will not be routed through a third party;
5. optional free-text context;
6. an explicit consent to the review of the account's interaction history for this purpose.

No field asks for a legal name, address, age document, photograph or identity number. A refusal to provide the attestation does not itself prove cheating; it means the review cannot clear the pair on that basis.

**NET-033 — What the reviewer may inspect.** *Provisional.* The reviewer may inspect: account creation dates and verification state; nation creation and reroll history; session and recovery events; the transfer and trade graph; campaign participation; alliance and treaty records; prior pair states and decisions; and the attestations. The reviewer may not inspect content the game does not collect (private messages, keystrokes, device fingerprints) and may not demand sensitive identity documents as a condition of clearance.

**NET-034 — Decision types.** *Provisional.* A review ends with exactly one of:

| Decision | Meaning | Pair state after | Account-level action |
|---|---|---|---|
| `SEPARATE_PEOPLE` | The evidence supports two independent players | `CLEARED` with 90-day probation | None |
| `FALSE_POSITIVE` | The match was wrong or the accounts are unrelated | `CLEARED`, basis recorded, block removed | None; correction recorded |
| `INCONCLUSIVE` | The evidence neither clears nor confirms | `MAINTAINED`; re-review after 30 days or new evidence | None |
| `LIKELY_DUPLICATE` | The evidence indicates one operator | `MAINTAINED` | Enforcement is a separate decision under §5.7; it is not automatic |
| `REFERRED_TO_ENFORCEMENT` | A confirmed or strongly supported violation | `MAINTAINED` until the enforcement case resolves | §5.7 ladder, with its own notice and appeal |
| `ACCOUNT_CLOSED` | One account closed or was removed | `CLOSED`; no live restriction | Closure or removal record |

**NET-035 — A claim is not a clearance.** *Provisional.* A statement that two people are different is necessary but not sufficient. The reviewer weighs it against the interaction graph, the account history and any independent evidence. Conversely, an unsupported suspicion is not a `LIKELY_DUPLICATE` finding; `INCONCLUSIVE` is the honest outcome when the evidence does not decide.

**NET-036 — Probation after clearance.** *Provisional.* A `CLEARED` pair is watched for **90 days**. A new shared observation plus a value-transfer or coordinated-war signal reopens `RESTRICTED` with priority review; a new shared observation alone does not, because the same household will keep sharing a network. The probation is a review priority, not a sanction.

**NET-037 — Clearance is private.** *Provisional.* A cleared pair is not announced, badged or ranked. The two accounts see their own status; nobody else does. Clearing a restriction does not publish that either account was ever restricted.

### 5.7 Enforcement ladder

**NET-038 — Graduated, evidence-based, appealable.** *Provisional (REQ-064; D-018).* Account-level enforcement uses this ladder. The pair restriction is level 1 and is not a punishment. Levels 2–6 require a recorded reason and an appeal route; levels 4–6 require independent evidence and, where staffing allows, a second reviewer.

| Level | Measure | Applies to | Minimum evidence | Notice and appeal |
|---|---|---|---|---|
| 0 | No action | Account | A network observation alone | None |
| 1 | Pair interaction restriction | Pair | A high-risk attempt between an observed pair, or operator decision | In-product message; review route |
| 2 | Recorded warning | Account | Independent behavioural signal plus review, or repeated blocked attempts after a level-1 explanation | Notice with reason; appeal |
| 3 | Account review flag | Account | Behavioural graph or conflicting attestations; may request information | Notice; the account can still play except restricted verbs |
| 4 | Temporary suspension | Account | Independent evidence of a violation; not IP alone | Notice with reason and end condition; appeal |
| 5 | Removal of an additional account | Account(s) | Confirmed multi-accounting or a confirmed attempt to evade | Notice; appeal; the retained account is identified |
| 6 | Permanent ban | Account | Confirmed serious or repeated violation, ban evasion, or a confirmed multi-account operation with value transfer | Owner/senior approval where available; notice; appeal; record |

**NET-039 — The IP-only ceiling.** *Approved policy (REQ-066).* A shared IP, a shared network key or a shared device observation is sufficient for **level 1 only**. It is never sufficient by itself for level 4, 5 or 6. A permanent multi-account ban requires independent evidence, such as a confirmed admission, a transaction graph that only a single operator explains, or a verified link between the accounts that is not merely a network address.

**NET-040 — Additional-account removal.** *Provisional.* When a person is confirmed to hold more than one account, the additional account(s) are closed. The person may identify one account to retain if identity and control are established and no other disqualifying violation exists; the retained account keeps its nation and receives the appropriate warning or suspension. Value moved between the accounts may be reversed where the evidence is unambiguous and the reversal is recorded and disclosed; it is not reversed on suspicion. If the accounts are both part of a coordinated operation, both may be closed. The detailed procedure belongs to Prompt 12.

**NET-041 — Permanent ban and return.** *Provisional.* A permanent ban ends access to the account and blocks nation creation. The person may appeal once. A banned person may not return on a new account; attempting to do so is a new violation and is evidence for the ban record. A ban is not cleared by a reroll, a new e-mail, a new network or a new nation. The ban record is retained under D-026 and UD-017.

**NET-042 — Reroll is not an enforcement reset.** *Provisional.* A reroll does not remove a warning, review flag, suspension, ban, pair restriction, evidence record or appeal. The replacement nation is created by the same account and inherits the account's status. If the account is suspended from nation creation, the reroll cannot complete until the suspension ends.

**NET-043 — No automatic punishment from a blocked attempt.** *Provisional.* A single blocked interaction, a single shared network or a single refused attestation does not automatically escalate beyond level 1. Escalation needs a pattern, independent evidence or a review decision. This protects the student who tries one trade before reading the message.

### 5.8 Appeals

**NET-044 — One appeal, with reasons.** *Provisional (REQ-026).* A pair decision or an account-level sanction may be appealed once. The appeal states the ground (mistaken identity, unrelated players, evidence error, disproportionate measure, new evidence). The restriction or sanction remains in force while the appeal is pending unless an authorised reviewer grants interim relief for a documented reason. The appellant receives a written decision with reasons.

**NET-045 — A different reviewer where possible.** *Provisional.* The appeal should be decided by a reviewer who did not make the original decision. In a single-operator project that may be impossible; the record must say so, and the decision must be written as if it will be read publicly. This is a process standard, not a claim of independent adjudication.

**NET-046 — New evidence, not endless re-litigation.** *Provisional.* A closed appeal may be reopened only on genuinely new evidence, not on repetition. The final decision is recorded. A `MAINTAINED` pair may request a fresh review after 30 days without new evidence; that is a review, not an appeal.

**NET-047 — Correcting a false positive.** *Provisional.* If an appeal or review finds that unrelated players were restricted, the pair is `CLEARED`, the basis is recorded, any account-level measure traceable to the error is reversed, and the affected accounts are told what was corrected. The game does not claim to restore value that never moved.

### 5.9 Player-facing behaviour

**NET-048 — Explain the limit, not the detection.** *Provisional.* When a restricted interaction is blocked, the player sees which action was blocked, that it was blocked because the two accounts recently used the same network, that this is an interaction limit rather than a finding of cheating, and how to request review. The message does not name an IP address, network key, threshold, detection window, the other account's private data or the reviewer's evidence.

**NET-049 — Explain the next step.** *Provisional.* Every block, review request, decision and appeal message names a next action: request review, wait for the other account, appeal, continue playing, or contact support. A message that only says "blocked" is a specification defect.

**NET-050 — No public accusation.** *Provisional.* A nation page, ranking, chronicle entry, alliance list or world feed never displays a shared-network restriction, a review status or an enforcement case against another player. Public history may record an enforcement outcome only in the narrow form Prompt 12 permits (for example a ban notice that does not disclose private evidence).

### 5.10 Audit, privacy and retention

**NET-051 — What is recorded.** *Provisional.* The audit spine records: the observation event (account, keyed digest, timestamp, source), pair state changes, every blocked attempt (verb, target, reason code, timestamp), review requests, attestations, decisions, appeals, account-level measures and every privileged read of a pair record. It does not record the raw IP, the other player's credentials, private message content or the reviewer's personal notes beyond the case record.

**NET-052 — Access.** *Provisional.* Pair records, attestations and enforcement evidence are `restricted`: only an integrity/moderation role may read them, every read is logged, and a player may see only their own record. Ordinary administrators, alliance leaders and other players have no access. Least privilege applies; a support role may see a status but not the evidence.

**NET-053 — Retention.** *Provisional (D-026; DAT-003).* Network observations: **180 days** after last seen, then deleted or reduced to a pair-level timestamp. Pair records: while active plus **12 months** after closure. Enforcement and appeal records: class-O floor of **12 months** after the case closes, longer only for an open case; the audit spine is permanent. The raw IP is not stored by the application at all, so there is no raw-IP retention period to set.

**NET-054 — Aggregates.** *Provisional (D-027).* Published statistics about shared-network controls are counts and bands with at least 5 contributors; no list of accounts, networks or pairs is published. Internal dashboards may show individual cases only to an authorised role.

**NET-055 — Legal and jurisdiction.** *Deferred (UD-017).* Whether network data is personal data, what notice is required, how a deletion request interacts with an active enforcement record, and whether a legal hold applies are jurisdiction questions. Prompt 12 states the posture; the owner obtains legal review before public launch. This document makes no compliance claim.

### 5.11 Limits of the mechanism

**NET-056 — IP matching is weak evidence.** *Provisional.* A VPN, a proxy, a carrier-grade NAT, a mobile network, a school network, an IPv6 privacy address or a simple network change can hide or create a match. The control is a **speed bump plus a review trigger**, not a detector of all multi-accounting.

**NET-057 — False positives are expected.** *Provisional.* Households, roommates, campuses, offices and public Wi-Fi will produce matches. The design accepts this and invests in review, messaging and correction rather than in pretending the match is proof. A large network must not be treated as a offender list (NET-019).

**NET-058 — A determined evader can route around a pair block.** *Provisional.* A player who uses a third account, a VPN, an out-of-game arrangement or a slow transfer pattern may evade mechanical checks. The response is behavioural review, audit records and account-level enforcement where evidence supports it, not a claim that the block is airtight. This is why the one-account rule is a policy with evidence-based enforcement, not a technical guarantee.

**NET-059 — Review capacity is a real constraint.** *Provisional.* A small project may not answer a review within a day. The message must not promise an immediate decision. A target of **7 days** is recorded as a service target, not a guarantee; a review that takes longer does not convert the restriction into a sanction. The backlog is monitored and disclosed in aggregate.

**NET-060 — The control is one layer.** *Provisional.* The shared-network restriction sits alongside the one-account policy, the fresh-nation transfer rule, the audit spine and the enforcement ladder. None of them is sufficient alone; none may be described as perfect.

**NET-061 — No standing co-resident exemption.** *Approved policy direction (D-037).* Living at the same address is **not** a permission to interact. There is no self-service "family mode", household link-up, shared-device allowance or repeated-login auto-clear. Two accounts on one network are cleared only through the review in §5.6, where a co-residence claim is evidence to be weighed rather than a switch that unlocks transfers. A cleared pair that keeps sharing a network stays under the 90-day watch (NET-036). The player-facing explanation says plainly that households are allowed to play but do not thereby gain an exception.

---

## 6. Nation creation

### 6.1 Eligibility

**NAT-001 — Prerequisites.** *Provisional (REQ-002/REQ-039).* A nation may be created only when **all** of the following are true:

1. the request is authenticated as an existing game account;
2. the account's e-mail is verified (D-029);
3. the account is not suspended, banned or closed;
4. the account has no active nation (§4.2);
5. the account is not in a recovery lockdown that forbids game actions;
6. the submitted name and short name pass §7;
7. the request carries a valid idempotency key;
8. the server can resolve the acting account from the session, not from a request field;
9. the account is not subject to a nation-creation pause under the free-tier posture (D-022), with a disclosed reason.

**NAT-002 — What the player supplies.** *Provisional.* The player supplies a nation name, a short name, an optional emblem choice from the game's own set (not an uploaded image at first playable), and a starting posture from the options Prompt 06 will define. The player does **not** supply starting resources, account IDs, nation IDs, ownership fields, creation timestamps or a score. Client-supplied values in those fields are ignored or rejected.

**NAT-003 — What the server assigns.** *Provisional.* The server assigns `nation_id`, the public nation number, `account_id` (from the session), the creation turn and timestamp, the starting state, and the audit record. The public nation number is stable and never reused.

### 6.2 The creation flow

**NAT-004 — Normal flow.** *Provisional.*

```
[1] Player submits name + short name + posture with an idempotency key
        │
[2] Server validates session, verification, account standing, name syntax
        │
[3] Server opens a transaction and locks the account row
        │
[4] Server re-checks: no active nation for this account
        │
[5] Server inserts the nation + starting state + audit row atomically
        │
[6] Server returns the nation identity and the starting digest
```

**NAT-005 — Idempotency.** *Provisional (REQ-018/REQ-070).* The creation request carries a client-generated key scoped to `(account, 'nation_create')`. The first request with a key creates the nation; a repeat with the same key and the same payload returns the **same** nation and the same starting state. A repeat with a different payload under the same key is rejected (`AC-06`) and creates nothing. The key is not a name and does not become the nation identity.

**NAT-006 — Concurrency.** *Provisional (REQ-070).* Two simultaneous creation requests for one account must produce **exactly one** nation. The design requires a transaction-safe uniqueness rule plus a per-account lock or equivalent serialisation. The loser receives `AC-03` ("this account already has a nation") and is shown the existing nation. No second row, no second starting grant, no second audit record.

**NAT-007 — Interrupted request.** *Provisional.* If the connection drops after the server commits but before the response arrives, the retry with the same key returns the existing nation. If the connection drops before the commit, the transaction rolls back and the retry creates the nation once. The player is never left with a half-created nation or a charge without a nation. The interface shows the creation state on return.

**NAT-008 — Repeated creation after success.** *Provisional.* A deliberate second creation request from an account that already has a nation is rejected (`AC-03`) and is **not** a violation by itself; it is usually a double-click or a stale tab. Repeated attempts after the rejection are rate-limited at the transport level, not treated as cheating.

**NAT-009 — No duplicate starting resources.** *Provisional.* The starting state is written once, keyed to `nation_id`, inside the creation transaction. A retry never re-applies it. A client cannot request a second grant, a larger grant or a different starting bundle.

**NAT-010 — Audit.** *Provisional (REQ-027).* Creation writes an audit row: `account_id`, `nation_id`, timestamp, creation turn, name at creation, starting-state version and idempotency key. The row is permanent; it is not a public record.

**NAT-011 — No partial nation.** *Provisional.* Either the nation, its starting state and its audit row all commit, or nothing does. A nation without a treasury, a treasury without a nation or an audit row without a nation is a defect, not a state the game may present.

### 6.3 First nation and replacement nation

**NAT-012 — Same standard start.** *Approved policy (REQ-072).* A first nation and a replacement nation receive the **same** standard starting state. There is no veteran bonus, no second-nation penalty, no accelerated bundle and no extra resource package. The difference is not in the bundle; it is in **protection eligibility** (first nation only) and in the account's history (§12.3).

**NAT-013 — No inherited assets.** *Approved policy (REQ-068).* A replacement nation inherits nothing from the retired nation: no treasury, materials, buildings, research, military, score, rank, treaties, alliance role, achievements, buffs or stored rewards. The reset boundary is §9.3.

**NAT-014 — No inherited identity.** *Provisional.* A replacement may reuse a name only if the name rules permit it (§7); it does not inherit the old nation's public page, nation number, ranking position or historical entries. The old identity remains attached to the old `nation_id`.

### 6.4 Initial public profile

**NAT-015 — Public at creation.** *Provisional.* A new nation's public page shows its nation name, short name, emblem, founding turn, current status (`active`, `protected`, `dormant`, `retired`), current alliance (if any), public ranking once eligible, and public history. It does **not** show the account's e-mail, account ID, IP, recovery state, enforcement record or pair restrictions.

**NAT-016 — Ranking entry.** *Provisional.* A nation enters public rankings after its **first completed boundary**, not at creation. This avoids a creation-time rank that would be immediately stale and gives the first digest something to explain. Until then the page says "awaiting first turn". Dormant exclusion follows D-028.

**NAT-017 — Initial relationships.** *Provisional.* At creation a nation has: posture `neutral` toward every nation; no treaties; no alliance; no campaigns; no trade offers; no outstanding obligations. It may receive treaty or alliance invitations immediately, subject to the other system's rules.

**NAT-018 — Initial military.** *Provisional, owned by Prompt 10.* At first playable the nation has **no offensive military capability** and no Operations Points beyond the standard **starting value — the national cap** under B-10 `WAR-039`, with one OP regenerated at each later boundary's P3.7 opening up to that cap (Prompt 10B-C3, 2026-11-04); the exact garrison, if any, is Prompt 10's decision. No starting military value may be invented here. This preserves D-023 (warfare is not in the first playable) and avoids a hidden combat advantage.

**NAT-019 — Initial domestic state.** *Provisional, owned by Prompt 06.* The nation starts with the default government and policy preset, a baseline stability value and no active political programme. The preset's effects and values are Prompt 06's; this document fixes only that every nation starts from the same preset.

**NAT-020 — Initial research and development.** *Provisional, owned by Prompt 05.* The nation starts with the five development lines at their baseline level, no completed research programme and no queued construction. The baseline numbers are Prompt 05's; this document fixes the shape and the equality rule.

**NAT-021 — Tutorial progress.** *Provisional (ONB-007).* Tutorial progress belongs to the **account**, not the nation. A first nation starts at step 1. A replacement nation does not replay mandatory tutorials the account has already completed, but it shows a short "what changed" orientation and keeps contextual help available.

**NAT-022 — No geography.** *Approved constraint.* Creation never asks for a continent, region, territory, coordinates or map placement. The world is the symbolic network defined in B-02; a nation's position is its relationships, not a location.

### 6.5 Failure and recovery behaviour

| Situation | Server response | Player sees | State |
|---|---|---|---|
| Not signed in | Reject | Sign in to create a nation | Nothing created |
| E-mail unverified | Reject | Confirm your e-mail first (resend link) | Nothing created |
| Account suspended or banned | Reject | The account cannot create a nation; show the reason category and appeal route | Nothing created |
| Account already has a nation | Reject `AC-03` | You already govern [nation]; open it | Existing nation unchanged |
| Name invalid | Reject `AC-05` | The specific rule that failed, with an example | Nothing created |
| Name unavailable | Reject `AC-04` | That name is already in use; suggest alternatives | Nothing created |
| Duplicate key, same payload | Return the original result | Your nation is ready | Existing nation |
| Duplicate key, different payload | Reject `AC-06` | Refresh and try again; do not reuse the request | Nothing created |
| Concurrent request lost the race | Reject `AC-03` | Your nation was already created; open it | One nation |
| Service interrupted before commit | Retryable error `AC-20` | We could not create the nation; try again | Nothing created |
| Service interrupted after commit | Return the existing nation on retry | Your nation is ready | One nation |
| Free-tier creation pause | Reject with disclosure | New nations are paused; the reason and status are shown | Nothing created |

**NAT-023 — Creation is not a race for names.** *Provisional.* If two accounts submit the same available name in the same instant, the uniqueness constraint decides; the loser receives `AC-04` and may choose another name. The winner is not advantaged in resources or ranking. This is a normal collision, not a punishment.

**NAT-024 — Technical rate limit.** *Provisional.* Nation creation is rate-limited per account and per source to prevent automated account/nation churn (for example a small number of attempts per minute). The limit is disclosed as a technical protection, not a gameplay cooldown, and it never delays a first legitimate creation by more than a few seconds.

**NAT-025 — Creation after administrative removal.** *Provisional.* If a nation was removed by an administrator, the account's eligibility to create a replacement depends on the removal reason and the account's standing. A removal for a rules violation does not automatically grant a clean slate; a removal for a technical error does. Prompt 12 owns the removal categories; the account is told which category applies and whether it may create a replacement.

---

## 7. Nation naming and identity

### 7.1 Two names, one identity

**NAT-026 — Display name and short name.** *Provisional (REQ-071).* Every nation has:

1. a **display name** — the public name used in the world, chronicle and diplomacy, 3–32 characters after normalisation;
2. a **short name** — a compact tag used where space is tight (rankings, war lists), 2–6 characters, uppercase A–Z and digits only.

The two are separate fields. Changing one does not change the other unless the player changes both. Neither is the nation's identity: `nation_id` and the public nation number are.

**NAT-027 — Normalisation.** *Provisional.* Before validation and uniqueness checks, the server applies Unicode NFC, trims leading and trailing whitespace, collapses internal whitespace runs to one space, and rejects zero-width characters, bidirectional control characters, combining-only strings and unpaired surrogates. The stored display name is the normalised form; the short name is uppercased. Normalisation is deterministic and applied identically on create and rename.

**NAT-028 — Allowed characters.** *Provisional.* The display name may contain Unicode letters and combining marks, decimal digits, spaces, hyphen, apostrophe and full stop. It may not contain emoji, pictographs, control characters, angle brackets, braces, backslashes, slashes, markup, URLs, line breaks or characters that render as another player's name through invisible formatting. A name must contain at least one letter. It may not begin or end with a space, hyphen, apostrophe or full stop. The short name is `[A-Z0-9]{2,6}` after uppercasing.

**NAT-029 — Uniqueness.** *Provisional.* The current display name is unique under case folding and diacritic folding (for example `Café` and `CAFE` collide). The short name is unique case-insensitively. Names are compared after normalisation, not by raw bytes. A name held by a retired nation is released under NAT-036; a name held by an active nation is not available.

**NAT-030 — Reserved names.** *Provisional.* The following are reserved and may not be registered: `Nation Supremacy`, `Project X` (internal codename), `Staff`, `Admin`, `Administrator`, `Moderator`, `System`, `Support`, `Game Master`, the names of the game's own officials and any string the operators use to label official communication. The reserved list is maintained privately, is not a public enumeration challenge, and may grow without notice. A reserved-name rejection uses the same neutral message as an unavailable name so the list is not disclosed by probing.

**NAT-031 — Offensive, harassing and deceptive names.** *Provisional.* A name that is hateful, sexually explicit, harassing, threatening, or designed to deceive players about game mechanics is prohibited. The game screens an obvious blocklist at creation and reviews reports contextually, including leetspeak, spacing and homoglyph evasion. A rejected name returns a neutral message and an example of an acceptable name; it does not repeat the offending string in the interface. A player may appeal a name rejection (§7.4).

**NAT-032 — Impersonation.** *Provisional.* A name may not impersonate another player's nation, an alliance's official identity, a staff member or a real-world public figure in a way that implies official authority. Exact-name collision is prevented by uniqueness; near-collisions and deceptive styling are reviewable conduct. A nation that gains a name by rename and uses it to impersonate is subject to a forced rename and the conduct ladder.

**NAT-033 — No markup or external identity.** *Provisional.* Names are plain text. They may not contain HTML, Markdown that renders as a link or image, a URL, an e-mail address, a phone number or a call to contact an external account. The display layer escapes text; it never interprets a name as markup.

### 7.2 Renaming

**NAT-034 — Display-name change.** *Provisional parameter.* A nation may change its display name once per **7 days**. The change is a class-I immediate-with-record action: it applies at once and is recorded. It costs no treasury value at first playable; if a later economy prompt introduces a fee, the fee must be stated before submission and must not be used to hide the limit.

**NAT-035 — Short-name change.** *Provisional parameter.* A nation may change its short name once per **30 days**, because the short name is the compact public identity used in rankings and war lists. The same immediate-record and disclosure rules apply.

**NAT-036 — Released names.** *Provisional parameter.* A display name released by rename or retirement is held unavailable for **30 days** before it can be claimed by another account. This reduces exact-name impersonation immediately after a rename. After 30 days it may be claimed; the historical record still shows which nation used it and when. The hold is a naming rule, not a property right.

**NAT-037 — Renames do not transfer ownership.** *Provisional (INV-019).* A rename changes the display name only. It does not change `nation_id`, the public nation number, the owning `account_id`, the founding turn, the nation's history, its treaties, its alliance membership, its rank or its obligations. A player cannot acquire another nation by taking its old name.

**NAT-038 — Staff force-rename.** *Provisional.* An authorised moderator may force a rename to a neutral placeholder for a name violation, impersonation or a legal requirement. The action is logged with a reason, the player is notified, and the player may choose a compliant replacement through the normal rename flow. A force-rename does not delete the nation or change ownership.

**NAT-039 — Naming enforcement and appeal.** *Provisional.* A name rejection at creation is immediate; a discovered violation is handled by the conduct ladder, with a rename opportunity where the violation is minor. An appeal goes to a reviewer who did not impose the rename where possible. The appeal record and the final name are kept.

### 7.3 Historical identity

**NAT-040 — Stable identity across renames and rerolls.** *Provisional (REQ-071; INV-008).* Every historical record stores `nation_id`, the **name used at the time of the event**, and the public nation number. A later rename does not rewrite the old event; the old page may show "now named X" as a separate, clearly dated note. A rerolled nation's page is marked `retired` and keeps its final name, founding turn and public history; it is not reassigned to the replacement.

**NAT-041 — No name-based lookup of an account.** *Provisional.* A nation name resolves to a public nation page, never to an e-mail address, account ID or recovery state. Searching a name must not reveal whether an account exists behind a retired nation beyond the public historical page.

**NAT-042 — Name history is bounded.** *Provisional.* The game keeps a rename log (old name, new name, date, actor) as a class-P record for integrity. It does not keep a full public list of every name an account has ever used; the public page shows the current name and the names used in public historical events.

---

## 8. Starting state and the progression contract

### 8.1 The standard starting state

**NAT-043 — One standard bundle.** *Provisional (REQ-072).* Every newly created nation — first or replacement — receives the same standard starting state. The bundle's **structure** is fixed here; its **numbers** belong to the owning prompts and Prompt 14.

| Component | Starting condition | Numeric owner | Status |
|---|---|---|---|
| Treasury | A one-time starting grant in the game currency | Prompt 04 (size), Prompt 14 (validation) | Provisional; no value stated here |
| Materials | A small standard stock of the four material classes | Prompt 04/05 | Provisional |
| Development lines | All five lines at their baseline level | Prompt 05 | Provisional |
| Construction | No queued construction | Prompt 05 | Fixed shape |
| Research | No completed programme, no queued programme | Prompt 05 | Fixed shape |
| Domestic politics | Default government and policy preset, baseline stability | Prompt 06 | Provisional |
| Military | No offensive capability; garrison/readiness per Prompt 10 | Prompt 10 | Deferred |
| Operations Points | Standard pool at the standard starting value (the national cap), +1 at each later boundary's P3.7 opening | Prompt 10 (cap), Prompt 14 (value) | Deferred |
| Diplomacy | Neutral posture to all; no treaties | Prompt 08 | Fixed shape |
| Alliances | No membership | Prompt 09 | Fixed shape |
| Trade | No offers, no obligations | Prompt 07 | Fixed shape |
| Ranking | Unranked until the first completed boundary | Prompt 11 | Provisional |
| Protection | First nation only; see §12 | Prompt 03 (this document) | Provisional |
| Tutorial | Account-level progress; first nation starts at step 1 | Prompt 13 (presentation) | Provisional |
| Public profile | Name, short name, emblem, founding turn, status | Prompt 13 | Provisional |

**NAT-044 — No invented numbers.** *Provisional.* This document does **not** set the starting grant, material quantities, line levels, stability value, military size or OP cap. Those values are deliberately absent because they interact with FO-018, ECON-012, ECOQ-003 and the war economy. A later prompt that needs a number must state it in its own document with a status label; it may not cite this document as the source of a value.

**NAT-045 — Equality.** *Provisional.* Two nations created on the same day with the same choices receive the same starting state. There is no differential by account age, nation count, reroll count, referral, purchase, alliance membership, posting activity or time of day. The only permitted difference is an explicitly approved rule that states its reason in a decision entry; none exists.

**NAT-046 — No transferable first-time rewards.** *Provisional (REQ-073).* A new nation receives the standard bundle and nothing else that can be converted into value for another account. Tutorial completion, first-login, first-trade and first-victory rewards are not adopted. If a later prompt introduces a first-time reward, it must be account-scoped, non-transferable, non-convertible and awarded once per account; it may not be re-earned by rerolling.

**NAT-047 — The starter bundle is not a gift to other accounts.** *Provisional.* The starting bundle is spent inside the nation. A new nation is subject to the fresh-nation one-sided transfer restriction (§12.5), which prevents turning the bundle into a transfer to another account during the window. The restriction is a transfer rule, not a reduction of the bundle: the nation still receives the standard start.

**NAT-048 — First digest.** *Provisional.* The first completed boundary after creation produces a digest that explains the starting state, any protection status, the first production and upkeep (once Prompt 04 defines them) and the first available decisions. A new player should not have to infer what the bundle did.

**NAT-049 — No session requirement.** *Provisional (B-02 TR-084).* A nation created just before a boundary resolves normally even if the player closes the browser. Creation does not require the player to be present at the boundary, and no starting benefit is lost by being offline.

**NAT-050 — Starting state version.** *Provisional.* The bundle carries a version identifier. If the approved starting state changes, existing nations are not retroactively re-granted; the change applies to nations created after the recorded effective turn, and the difference is disclosed. This prevents a silent re-grant or a silent clawback.

### 8.2 The first-month arc (contract, not content)

**NAT-051 — Progression is chosen, not handed out.** *Provisional (REQ-038; D-021).* The first month is designed as a sequence of **decisions with visible trade-offs**, not a reward ladder. The contract for later prompts is:

| Horizon | What the player should be able to do | Owning prompt | Reward status |
|---|---|---|---|
| First session | Found a nation, read the world clock, make one meaningful allocation, know how to return | 03/13 | No reward beyond the standard bundle |
| First boundary | See production, upkeep and the first digest; understand one cause-and-effect chain | 02/04 | No bonus |
| First week | Choose an emphasis, complete a first construction or research step, evaluate a first trade or diplomatic contact | 04/05/07/08 | No catch-up bonus |
| First month | Hold a stable economy, participate in one relationship, understand one strategic risk, set a longer-term goal | 04–11 | Milestones are records, not power |

**NAT-052 — Milestones are records.** *Provisional.* A milestone (first trade, first treaty, first alliance, first campaign, first 30 days) is a public or private record and, at most, a cosmetic acknowledgement. It does not grant resources, yield, military power, protection or ranking weight. Prompt 11 owns the achievement framework; this document forbids a transferable or repeatable first-time economic reward.

**NAT-053 — A replacement starts at the beginning of the arc.** *Provisional.* A replacement nation is a new nation for progression purposes: no milestones, no achievements, no research, no rank and no protection. The account keeps its tutorial knowledge and its history, which is the honest form of continuity.

---

## 9. Instant nation rerolling

### 9.1 Definition and required behaviour

**RRL-001 — What a reroll is.** *Approved requirement (REQ-067).* A **reroll** means: a player permanently deletes their existing nation and creates a new nation immediately using the **same eligible player account**. The account remains. The old nation's progress does not. A reroll is not a second account, a transfer of ownership, an account reset or a mechanism for escaping sanctions.

**RRL-002 — Required flow.** *Approved requirement.* The normal flow is:

1. the player signs in to the existing account;
2. the player chooses **Reroll nation** (also labelled **Permanently delete nation**);
3. the game explains that the old nation and all its progress will be permanently lost;
4. the player explicitly confirms the irreversible operation;
5. the old nation is retired through the safe process below;
6. the old nation is no longer the account's active nation;
7. the account may immediately begin creating a replacement;
8. there is **no ordinary gameplay cooldown or mandatory waiting period** between a completed reroll and creating the replacement;
9. the replacement follows the standard creation rules (§6);
10. the account never owns two active nations simultaneously.

**RRL-003 — No new registration.** *Approved requirement.* A reroll never asks the player to register again, confirm a new e-mail, create a new password or wait for operator approval. The account's existing authentication is used. A player who has lost access uses recovery (§10), not a new account.

**RRL-004 — No gameplay cooldown.** *Approved requirement.* A completed reroll does not impose a timer before the replacement can be created. Technical anti-automation limits are permitted only if they are disclosed, measured in seconds, and cannot delay a normal first attempt. A hidden cooldown, a "cooling-off day", a manual approval step or a "one reroll per month" rule would violate this requirement.

### 9.2 Confirmation experience

**RRL-005 — Deliberate confirmation.** *Provisional.* Because deletion is irreversible, confirmation has three parts:

1. a **fresh authentication** check (the session must have re-authenticated within the last 5 minutes, or the player re-enters the password);
2. typing the **exact current nation name** into a confirmation field;
3. pressing a final button labelled with the consequence ("Permanently delete [nation] and create a replacement").

A single click, a swipe, a default-focused button or a pre-checked box is not sufficient. The confirmation is not a timer and does not require waiting.

**RRL-006 — What the confirmation must say.** *Provisional.* The confirmation screen states, in plain language:

- the existing nation's name, short name and founding turn;
- that this is a **permanent nation reset**, not a rename or a pause;
- that there is no ordinary undo and the old nation cannot be restored;
- that the treasury, materials, buildings, development, research, military, score, rank, politics, achievements, counters, buffs, stored rewards, treaties, alliance role and trade position are lost;
- that public historical events may remain recorded under the old nation's identity;
- that account-level restrictions and sanctions do **not** disappear;
- that a replacement nation can be created immediately after the deletion completes;
- that the replacement receives the standard starting state, not the old nation's wealth, and does **not** receive first-nation protection;
- a link to the reroll rules and to support.

**RRL-007 — Irreversible by design.** *Approved requirement.* A completed reroll is not undone by a normal undo, a support ticket or a browser back button. The old nation is retired and its active state is gone. The only exception is a security incident in which the account was compromised and the operator can establish that the reroll was not the owner's act; even then, restoration is an extraordinary, recorded and disclosed operator action, not a normal path (RRL-025).

### 9.3 The operation

**RRL-008 — Operation states.** *Provisional.* The reroll is a state machine, not a single unlogged click:

```
REQUESTED → VALIDATING → RETIRING → RETIRED → REPLACEMENT_AVAILABLE → COMPLETED
                    ↘ REJECTED (no state change)
                    ↘ BLOCKED (a blocking condition, no state change)
```

`RETIRED` means the old nation is no longer active and the account is eligible to create a replacement. `REPLACEMENT_AVAILABLE` means the creation surface is open. `COMPLETED` means a replacement exists. A reroll that is retired but not yet replaced is a valid state; the account simply has no nation.

**RRL-009 — Idempotency.** *Provisional.* The confirmation carries an idempotency key scoped to `(account, 'nation_reroll', active_nation_id)`. A retry with the same key returns the same state; it never retires a second nation or creates two replacements. A different payload under the same key is rejected (`AC-15` if the operation is already complete; `AC-06` otherwise).

**RRL-010 — Interruption and resume.** *Provisional.* If the browser closes, the network fails or the response is lost, the operation resumes from its recorded state on the next authenticated request. The account page shows "your nation was retired; create a replacement" or "your reroll did not complete; nothing was deleted." The player is never left unsure whether the deletion happened. A retry is safe and idempotent.

**RRL-011 — No partial retirement.** *Provisional.* Retirement, reservation release, offer withdrawal, membership termination and the audit record commit as one atomic operation or not at all. A failure leaves the old nation active and unchanged. The operation does not half-delete a nation and leave its assets in limbo.

**RRL-012 — Rate limit.** *Provisional.* A technical limit of one reroll request per account per **60 seconds** prevents double submission and automated churn. It is disclosed and resets immediately after a completed request; it does not delay a first legitimate reroll and is not a gameplay cooldown. Repeated rerolls are governed by the review trigger in RRL-022, not by a hidden timer.

### 9.4 What is lost

**RRL-013 — Reset boundary.** *Approved requirement (REQ-068).* Unless a subsystem has a specific historical or integrity requirement, the old nation loses all nation-specific progression, including:

| Category | Lost? | Note |
|---|---|---|
| Treasury and currency balance | **Yes** | No refund, transfer or conversion |
| Materials and inventory | **Yes** | No storage, escrow or transfer to the replacement |
| Buildings, cities, infrastructure, development levels | **Yes** | The replacement starts at baseline |
| Research, technology and programmes | **Yes** | No carry-over |
| Nation-specific advancement or unlocks | **Yes** | No carry-over |
| Military units, readiness and capabilities | **Yes** | No carry-over |
| Operations Points and military action resources | **Yes** | No transfer or refund; the below-cap carry exists only inside that nation's lifetime and is lost on reroll |
| Nation score, ranks and progression counters | **Yes** | The replacement is unranked until its first boundary |
| Domestic political state, stability, policy choices | **Yes** | Default preset for the replacement |
| Nation-specific achievements and milestones | **Yes** | The old nation's public record may remain; the replacement has none |
| Temporary buffs, benefits and stored rewards | **Yes** | Expire with the nation |
| Treaties, pacts and formal agreements | **Yes** | Terminate with the old nation; the record remains |
| Alliance membership and roles | **Yes** | Membership ends; any office held becomes vacant. The office-succession or vacancy policy is candidate under `UD-043` and is not applied automatically |
| Trade offers, listings and accepted-but-unsettled trades | **See §9.5** | Offers are withdrawn; accepted trades must settle or be cancelled first |
| Campaigns and wars | **Blocked** | Reroll is unavailable while a campaign is active, pending Prompt 10's forfeit rule |
| Scheduled actions and queued orders | **Yes** | Cancelled; reservations released; no value moves |
| Ranking position and public standing | **Yes** | Removed; historical snapshots remain |
| Protection eligibility | **Yes** | Not re-granted (RRL-018) |
| Unread notifications tied to the old nation | **Archived** | A summary remains; security notices are account-level |

**RRL-014 — No asset carry-over.** *Approved requirement (INV-006).* No old nation asset may be carried into the replacement. Assets cannot be converted into cash, stored for later, transferred to the replacement, refunded or otherwise preserved as a way of bypassing the reset. A player who wants to keep value must keep the nation.

**RRL-015 — No pre-deletion laundering.** *Provisional.* A transfer made before a reroll is governed by the normal transfer rules. It is not automatically reversed merely because a reroll followed, and it is not a permitted way to preserve the old nation's value. A pattern of divesting assets to a linked account and then rerolling is a review signal under §5 and §9.7; an unambiguous violation may be reversed or sanctioned under Prompt 12.

### 9.5 What survives

**RRL-016 — Account-level survival.** *Approved requirement (REQ-069).* A reroll does **not** reset:

| Survives | Why |
|---|---|
| Authentication identity, password and sessions | The account is the player |
| Stable `account_id` and account creation history | Identity continuity |
| E-mail verification and recovery codes | Security continuity |
| Prior nation IDs and minimal retirement records | Historical integrity and abuse evidence |
| Nation creation and reroll timestamps | Audit and abuse review |
| Account-level sanctions, warnings and restrictions | A reroll is not an amnesty |
| Shared-network pair restrictions and observations | The same account is still on the same network |
| Moderation history, cases and appeal records | Enforcement continuity |
| Evidence needed to prevent abuse of the reroll mechanic | Integrity |
| Tutorial progress and account settings | Learning belongs to the account |
| Account-level achievements that are explicitly account-scoped | Only if non-transferable and not re-earnable by reroll |

**RRL-017 — Enforcement survives.** *Approved requirement (INV-007/INV-023).* A temporary suspension continues under its existing rules. A permanent ban remains in force; the account cannot create a replacement while banned. A pending moderation case continues; the retirement does not close it. A preservation order blocks the reroll entirely (RRL-021). A reroll never erases the history of violations.

**RRL-018 — Protection is not re-granted.** *Approved requirement (REQ-073).* Newcomer protection is an account-level, once-only benefit (§12). A replacement nation is **not** protected as a new player. It receives the standard starting state and is immediately part of the world. This prevents protection farming and makes the reroll a real choice.

### 9.6 Cross-system consequences

**RRL-019 — Deterministic cleanup.** *Provisional (REQ-085; INV-022).* The following outcomes are mandatory. A later subsystem may refine a detail but may not leave the old nation's state ambiguous.

| System | Required outcome at reroll | Owner |
|---|---|---|
| **Turn engine** | No reroll mid-resolution; the operation is a transaction outside the boundary; no turn is skipped; the account's absence does not stop the clock | 02 |
| **Economy / treasury** | All balances, reservations and stored value are destroyed; no refund or transfer; deficit, if any, dies with the nation | 04 |
| **Cities / infrastructure / research** | All levels, queues and programmes are removed; the replacement starts at baseline | 05 |
| **Domestic politics** | Political state, stability and policy effects end; the replacement uses the default preset | 06 |
| **Trade / market** | Open offers are withdrawn with no fee and no value movement; accepted but unsettled trades must resolve or be cancelled before retirement; listings are removed; no trade history is transferred | 07 |
| **Diplomacy** | Treaties and pacts terminate; the termination is recorded as a class-P event attributed to the old nation; the new nation starts with neutral posture and no treaties; whether a breach-reputation consequence follows the account is Prompt 08's decision, constrained by UD-033 | 08 |
| **Alliances** | Membership ends; any role is vacated; the alliance is notified; no bank balance, permission or asset transfers; the replacement may apply as a new member with no inherited rank | 09 |
| **Warfare / campaigns** | Reroll is blocked while the nation is a participant in an active campaign (RRL-021); battle history remains; the opponent's legitimate outcome is not erased; Prompt 10 may define a forfeit that replaces the block | 10 |
| **Rankings / objectives** | The old nation is removed from current rankings; historical ranking snapshots remain; the replacement is unranked until its first boundary; no objective credit transfers | 11 |
| **Chronicle / news** | A public retirement event is written ("X was retired by its player"); old events remain attributed to the old nation; no private data appears | 11 |
| **Notifications** | Nation-specific open notifications are archived into a retirement summary; security and account notices remain | 13 |
| **Moderation** | Open cases continue against the account; a preservation order blocks the reroll; evidence survives; no case is closed by deletion | 12 |
| **Network restrictions** | Account-level pair restrictions and observations survive; the replacement is the same account and remains restricted with the same pairs | 03/12 |
| **Tutorial** | Account-level progress survives; the replacement gets a short orientation, not a mandatory replay | 13 |
| **Audit** | The retirement, the old nation ID, the account ID, the turn and the reason are written permanently | 12 |

**RRL-020 — Old nation page.** *Provisional.* The old nation's public page becomes a historical page: final name, short name, founding and retirement turns, status `retired — rerolled`, public chronicle entries, public war and treaty records, and no private state. It is not deleted from public history and it is not relabelled as the replacement. A visitor cannot use it to reach the account's private data.

**RRL-021 — Blocking conditions.** *Provisional.* A reroll is **blocked** when:

1. the nation is a participant in an active campaign or war (fail-closed pending Prompt 10's forfeit rule; UD-032);
2. an accepted value transfer or trade is awaiting boundary settlement and cannot be cancelled while its turn is `LOCKED` or `RESOLVING` (wait at most one boundary, then retry);
3. a moderation preservation order or an open case explicitly requires the nation's state to be preserved;
4. the account is suspended or banned in a way that forbids nation creation;
5. a technical operation for the same account is already in progress (idempotent lock).

These are **state conditions**, not a cooldown. The message names the condition and what ends it. No fee, timer or operator approval is added for a normal reroll.

**RRL-022 — Pending activity is not silently erased.** *Provisional.* When a reroll is attempted with an open offer, an unaccepted treaty, a queued construction order or an unread notification, those are withdrawn, cancelled or archived as part of the atomic retirement. The old nation's accepted obligations are not transferred to the replacement. If an obligation cannot be resolved safely, the reroll is blocked under RRL-021 rather than allowed to destroy it silently.

**RRL-023 — No two active nations.** *Approved requirement (INV-002).* Retirement and replacement creation are serialised per account. A retry, a double-click, a second tab or a concurrent request cannot produce two active nations or two replacements. The account may have zero active nations between retirement and replacement; that is a valid, visible state.

### 9.7 Anti-abuse safeguards

**RRL-024 — Starter farming.** *Provisional (REQ-073; INV-018).* The standard bundle is granted per nation, but the fresh-nation one-sided transfer restriction (§12.5) prevents converting it into a transfer to another account during the window. Repeated rerolls are not automatically cheating, but a pattern of creating a nation, extracting transferable value and rerolling is reviewable. The exact transfer window and fair-value band are Prompt 07's, with Prompt 14 validating them.

**RRL-025 — Reroll is not a war escape.** *Provisional (INV-022).* Reroll is blocked during an active campaign. Prompt 10 may replace the block with a forfeit rule that preserves the opponent's legitimate outcome; until it does, the block is the safe default. A player cannot delete a besieged nation to deny an opponent a result.

**RRL-026 — Reroll is not a sanction escape.** *Provisional (INV-007).* Account-level warnings, suspensions, bans, pair restrictions, moderation cases and appeal records survive. A player who rerolls to escape a sanction finds the same account status on the other side.

**RRL-027 — Reroll is not an investigation escape.** *Provisional.* A preservation order blocks retirement while an investigation needs the state. The audit spine is permanent and is not deleted with the nation. Deleting a nation cannot remove transaction records, battle records or enforcement evidence.

**RRL-028 — Reroll is not a protection reset.** *Provisional (INV-018/INV-025).* First-nation protection is consumed once per account (ONB-014). A replacement is not protected. A player cannot obtain a second protected start by deleting a nation.

**RRL-029 — Reroll is not a network-restriction reset.** *Provisional (INV-015).* Network associations and pair restrictions are account-level. The replacement is the same account; it remains restricted with the same pairs and cannot trade with them. Creating a new nation does not create a new network identity.

**RRL-030 — Repeated rerolls are a review signal, not a conviction.** *Provisional (UD-031).* **3 completed rerolls in 30 days** (provisional threshold) opens an internal review flag. It does not suspend, ban or restrict the account by itself. The reviewer looks for value extraction, war evasion, sanction evasion, protection farming and network-restriction evasion. A player who rerolls because they enjoy a fresh start is not cheating; the review is closed with that finding if the evidence supports it.

**RRL-031 — No restoration as a normal path.** *Provisional.* A completed reroll is final. A support request cannot restore the old nation. The only exception is a security incident where the account was compromised and the operator can establish that the reroll was not the owner's act; the restoration is logged, disclosed and limited to the extent the evidence supports. It is not a general undo and it is not promised.

### 9.8 Reroll, closure, removal, dormancy and recovery

**RRL-032 — Six different events.** *Provisional.* The terms are not synonyms:

| Event | What happens | Account | Nation | Reversible? | Owner |
|---|---|---|---|---|---|
| **Reroll** | Player deletes the nation and may immediately create a replacement | Survives | Retired; replaced | No normal undo | 03 |
| **Voluntary account closure** | Player closes the account after a cooling period | Closed | Retired; no replacement | Request may be cancelled during cooling | 03/12 |
| **Permanent account ban** | Operator ends access for a violation | Banned | Frozen/retired per Prompt 12 | Appeal only | 12 |
| **Administrative nation removal** | Operator removes a nation for a rules or technical reason | Survives unless also sanctioned | Removed; replacement eligibility depends on reason | Per removal category | 12 |
| **Dormancy** | No authenticated session for 14 days | Survives | Stays in the world, protected from new offensive actions | Reversible on return | 03 (applies D-028) |
| **Account recovery** | Player regains access to an existing account | Restored | The current nation remains | N/A | 03/06 |

**RRL-033 — Closure is not a reroll.** *Provisional.* A player who wants to leave can request account closure (§10.7). Closure ends the account and does not offer a replacement. A player who wants a fresh nation uses reroll and keeps the account. The interface must present the difference before either confirmation.

**RRL-034 — Recovery is not a reroll.** *Provisional.* Recovering access restores the existing account and its current nation. It never creates a second account, a second nation or a replacement. A player who cannot recover the old e-mail uses the recovery-code path or the review path (§10.5), not a new registration.

---

## 10. Account lifecycle and recovery

### 10.1 States

**ACC-017 — Account states are explicit.** *Provisional (REQ-074).* An account is in exactly one of these states. The nation's own state (`active`, `protected`, `dormant`, `retired`, `removed`) is a separate field; a pair restriction is a separate object (ACC-016).

| State | Meaning | Can sign in? | Can play? | Can create a nation? | Can appeal? |
|---|---|---|---|---|---|
| **REGISTRATION_PENDING** | The sign-up request exists but the auth record is not yet usable | No | No | No | No |
| **UNVERIFIED** | Auth record exists; e-mail not confirmed (D-029) | No (or verification-only, per Supabase configuration) | No | No | Yes, for access problems |
| **ELIGIBLE** | Verified, in good standing, no active nation | Yes | World read-only; no nation actions | **Yes** | Yes |
| **ACTIVE** | Verified, in good standing, zero or one active nation | Yes | Yes, subject to nation and pair state | Yes, if no active nation | Yes |
| **TEMP_RESTRICTION** | A defined limitation short of suspension (for example a trade or creation limit) | Yes | Partially; the notice names the surfaces | Only if the limitation allows it | Yes |
| **SUSPENDED** | Temporary account suspension | Yes, to read the notice and appeal | No; the nation is frozen | No | Yes |
| **BANNED** | Permanent ban | No; a neutral notice with an appeal route | No | No | Yes, once |
| **RECOVERY_LOCKED** | A recovery or contested-ownership review is in progress | Recovery channel only | No; the nation is frozen | No | Yes, for the recovery |
| **CLOSURE_REQUESTED** | Closure requested; cooling period running | Yes, to cancel | Limited; no new offensive actions or bank transfers | No | Yes, to cancel |
| **CLOSED** | Account closed; credentials removed | No | No | No | Privacy request route only |

**ACC-018 — Account state is not a punishment label.** *Provisional.* `TEMP_RESTRICTION` and `SUSPENDED` are not displayed to other players. A suspended nation may be marked `suspended` on its public page only as Prompt 12 decides; the default is a neutral `unavailable` status without a reason. `BANNED` is not published with evidence.

**ACC-019 — The nation state is separate.** *Provisional.* An account in `ACTIVE` may have no nation (after a reroll, before a replacement), and a nation may be `dormant` while the account remains `ACTIVE`. A player returning from dormancy does not need to re-verify or recover the account unless they lost access.

### 10.2 Transitions

**ACC-020 — Permitted transitions.** *Provisional.*

```
REGISTRATION_PENDING → UNVERIFIED → ELIGIBLE ⇄ ACTIVE
                                   │        │
                                   │        ├→ TEMP_RESTRICTION → ACTIVE
                                   │        ├→ SUSPENDED → ACTIVE
                                   │        ├→ BANNED → (appeal) → ACTIVE
                                   │        ├→ RECOVERY_LOCKED → ACTIVE
                                   │        └→ CLOSURE_REQUESTED → CLOSED
                                   └→ CLOSED (abandoned, after cleanup)

ACTIVE → ELIGIBLE   (reroll retired, no replacement yet)
ELIGIBLE → ACTIVE   (nation created)
CLOSED is terminal for normal play; a legal restore is an operator action, not a transition.
```

**ACC-021 — Transition authority.** *Provisional.* Registration and verification are handled by the auth system; nation creation is handled by the creation function; suspension, ban, removal and preservation orders are operator actions with a reason and a record; closure is the player's request plus the cooling period; recovery is the recovery flow. No transition may be triggered by a client-supplied status field.

**ACC-022 — Notifications.** *Provisional.* Every transition that changes what a player can do produces a notification to the verified e-mail and an in-product notice: verification required, account active, restriction applied, suspension applied, ban applied, recovery started, recovery completed, closure requested, closure cancelled, closure completed. A notification never contains a password, a session token, another player's data or an internal evidence detail.

### 10.3 Registration and verification

**ACC-023 — Registration.** *Provisional.* The player supplies an e-mail address, a password and a player handle, and confirms the 13+ statement. The password is handled by Supabase Auth; the game never stores or logs it. The handle is a public display name for the account, not the nation name; it follows the same offensive/impersonation rules as §7. A handle is not a login identifier; the e-mail is.

**ACC-024 — Verification.** *Provisional (D-029).* The account is `UNVERIFIED` until the e-mail confirmation link is used. An unverified account cannot create or control a nation, trade, post or hold office. Supabase's default is that an unconfirmed user cannot sign in; if a deployment allows a limited unverified session, that session may only complete confirmation or request a password reset. The built-in Supabase mail service is development-only; public registration requires custom SMTP (D-029, Stage 6).

**ACC-025 — Verification does not prove personhood.** *Approved policy.* A confirmed e-mail proves control of an address. It does not prove one person, one account. The one-account policy remains behavioural (ACC-006).

**ACC-026 — Abandoned registrations.** *Provisional.* An unverified account with no nation and no sign-in for **30 days** may be removed by a maintenance job after a warning e-mail. The removal is recorded. It does not affect a verified account, a nation or a historical record.

### 10.4 Sessions and credentials

**ACC-027 — Session posture.** *Provisional.* Sign-in issues a short-lived access token and a rotating refresh token. A session has an absolute lifetime and an idle timeout; the exact values are Stage 6 configuration, with a provisional absolute lifetime of **30 days**. Logout revokes the current session; "sign out everywhere" revokes all sessions. A password change revokes all other sessions. A recovery success revokes all sessions except the one performing the recovery where that is technically reliable.

**ACC-028 — Session visibility.** *Provisional.* A player can see their active sessions (coarse device/browser label, last-seen time, approximate location only if the platform supplies it and only at country level; no precise location), revoke any session, and sign out everywhere. This is the main self-service defence against a stolen session.

**ACC-029 — Password change.** *Provisional.* A password change requires the current password (or a recovery session), a new password that meets the declared minimum, and confirmation. It revokes other sessions and sends a security notice. It does not change the account ID, the nation or the pair restrictions.

**ACC-030 — Password reset.** *Provisional.* A reset request sends a time-boxed, single-use link to the verified e-mail. The response is the same whether or not the address belongs to an account, so the endpoint does not become an account-enumeration oracle. Supabase's `resetPasswordForEmail` is documented not to reveal whether an account exists; the interface must preserve that property and must not add a "no such account" message.

**ACC-031 — Recovery codes.** *Provisional.* At account creation the player receives **10 single-use recovery codes**, displayed once and stored only as hashes. A code can be used to regain access when the e-mail is unavailable. Using a code consumes it and triggers a security notice. The player can regenerate the set from a signed-in session; regeneration invalidates the old set. Recovery codes are not a second password and do not bypass a ban or suspension.

**ACC-032 — Contact-address change.** *Provisional.* Changing the registered e-mail requires the current password and confirmation from **both** the old and the new address, using Supabase Auth's secure email-change setting where available. The old address is notified; the change is recorded. Until both confirmations arrive, the old address remains the recovery anchor. A change requested from a recovery-locked account is held for review. Stage 6 verifies the exact Supabase setting (`T03-D06`).

### 10.5 Recovery

**ACC-033 — The recovery anchor.** *Provisional.* The verified e-mail is the primary recovery anchor; the recovery codes are the fallback. Recovery never uses in-game knowledge questions (treasury balance, last trade, nation history): those are things an attacker with a session may also know, and they turn private game state into a password hint.

**ACC-034 — Lost e-mail.** *Provisional.* A player who has lost the registered e-mail can use a recovery code. If no code is available, the player may request a manual review. The review may ask for: the account handle, the nation name, the approximate creation date, the last successful sign-in period, a description of the loss and any evidence of control the player can provide without sensitive documents. The reviewer may decline if control cannot be established. The game does not promise recovery, does not require a government ID and does not create a new account as a consolation.

**ACC-035 — Recovery cannot create a second account.** *Provisional (INV-020).* A recovery restores the existing account and its current nation. It never creates a new account, a new nation or a duplicate identity. If the account has no nation (after a reroll), recovery restores the account and the creation surface; it does not grant protection.

**ACC-036 — Recovery and restrictions.** *Provisional.* A shared-network restriction does not block recovery. A suspension does not block recovery of credentials; the account remains suspended after recovery. A ban does not block a password reset, but the account remains banned and cannot play. A recovery cannot be used to transfer an account to another person; if the review finds a contested ownership claim, the account is locked and the case is reviewed under Prompt 12.

**ACC-037 — Suspicious access.** *Provisional.* On a sign-in from a new network or a new session, the player receives a security notice. If the player reports a compromise, the account is `RECOVERY_LOCKED`, sessions are revoked, the nation is frozen, and the operator reviews the actions in the window. Value restoration is not automatic; it follows the evidence and is recorded. The shared-network policy does not override this flow.

**ACC-038 — Recovery timing.** *Provisional.* Password reset and recovery-code flows are immediate. A manual lost-e-mail review has a target of **7 days**, not a guarantee. The account remains locked until the review decides; the player is told the state and the next step.

### 10.6 Suspension, restriction and ban

**ACC-039 — Temporary restriction.** *Provisional.* A `TEMP_RESTRICTION` names the surfaces it limits (for example trade, nation creation, alliance office, posting) and an end condition. It does not silently become a full suspension. The player can still read the world, manage security and appeal.

**ACC-040 — Suspension.** *Provisional.* A `SUSPENDED` account cannot play or create a nation. Its nation is frozen: no orders, no production changes, no diplomacy, no bank access; the world continues around it. The public page shows a neutral `unavailable` status. The suspension has a stated end condition and an appeal. Whether a suspended nation can be attacked is Prompt 12's decision; the default is **no new offensive targeting while suspended**, to avoid third-party punishment of an unresolved case, and no bank access, to avoid using suspension as a bank shield.

**ACC-041 — Permanent ban.** *Provisional.* A `BANNED` account cannot sign in to play. It can see a neutral notice and an appeal route. The nation is frozen and marked appropriately. The ban is not cleared by reroll, a new e-mail, a new network or a new account. A successful appeal can restore the account; the restoration is recorded and disclosed to the affected player. The ban record is retained under D-026 and UD-017.

**ACC-042 — Ban evasion.** *Provisional.* Creating a new account to evade a ban is a violation and is evidence for the original case. The shared-network policy may detect the new account and restrict it; it is not by itself proof of evasion (a household member may legitimately join). Enforcement requires independent evidence, as in NET-039.

### 10.7 Closure

**ACC-043 — Closure request.** *Provisional.* A player may request account closure. The request starts a **7-day cooling period** during which the player can cancel. The account remains usable for security and cancellation, but the nation cannot initiate offensive actions or bank transfers; it can still be targeted normally, so closure cannot be used as a shield. At the end of the period the account closes.

**ACC-044 — What closure does.** *Provisional.* Closure: ends sign-in; deletes credentials and recovery codes; purges the e-mail and other private account data subject to retention; retires the nation without a replacement; keeps the public historical nation page and class-P records; keeps the audit spine and any enforcement record required by D-026 or an open case; removes the account from active rankings. It does not publish the player's e-mail, account ID or private data.

**ACC-045 — Closure is not a sanction eraser.** *Provisional.* A closure request does not close an open moderation case, erase a ban record, remove a pair restriction record or delete evidence required for an open case. If a legal retention obligation applies, the closure is completed for playable data and the retained record is limited and documented. UD-017 governs the legal analysis.

**ACC-046 — Closure and public history.** *Provisional.* The old nation's public page remains as a historical record with a status such as `closed by owner`; the account link is internal and restricted. Public chronicle events remain. The player's handle and e-mail are not shown. A player who returns later creates a new account; the old one cannot be reopened, and the new account is subject to the one-account policy.

### 10.8 Compromise response

**ACC-047 — Contain, then investigate.** *Provisional.* On a reported or suspected compromise: revoke sessions; lock the account for recovery; freeze the nation; notify the verified e-mail; preserve the audit record; then review the actions in the window. Reversal of value is considered only where the evidence is unambiguous and is recorded and disclosed. The player is told what was done and what was not.

**ACC-048 — No silent rollback of legitimate play.** *Provisional.* A compromise report does not automatically reverse trades, wars or treaties with innocent third parties. The review separates attacker actions from legitimate actions; a reversal that would harm an innocent third party is a last resort with disclosure.

**ACC-049 — Recovery after compromise.** *Provisional.* After recovery, the account is `ACTIVE` with the same nation, unless a suspension or ban applies. The player is prompted to change the password, review sessions and regenerate recovery codes. The compromise record is retained under the enforcement retention rule, not published.

---

## 11. First-session onboarding

### 11.1 The first-session journey

**ONB-001 — The journey.** *Provisional (REQ-038).* A first-time player should be able to complete the following in one short sitting, without external help:

| Step | What the player sees | What the player does | Success signal |
|---|---|---|---|
| 1. Welcome | One sentence on what the game is; no lore wall | Reads or skips | "Start" is visible |
| 2. Registration | E-mail, password, handle, 13+ confirmation | Creates the account | Confirmation e-mail sent |
| 3. Verification | Plain explanation of why the e-mail is needed | Opens the link | Account verified; return to the game |
| 4. The world | A short explanation of the shared world, the 2-hour UTC turn and the next boundary time | Reads one screen | Can state when the next turn closes |
| 5. Naming | Display name and short name, with rules and examples | Chooses a name | Name accepted |
| 6. Creation | Starting posture and a one-line summary of the standard bundle | Confirms creation | Nation exists; public page reachable |
| 7. Initial status | Treasury, materials, development baseline, protection status, next boundary | Reads the status card | Knows what it owns and when the first turn resolves |
| 8. Command centre | A single screen with the nation's current state and three suggested actions | Opens one panel | Can name one action available now |
| 9. First action | One meaningful allocation (for example an emphasis or a first construction choice) | Submits or queues it | The action is accepted or explained |
| 10. Return | How to come back, what will happen while away, where the rules and security pages are | Bookmarks or notes the URL | Knows the next step |

**ONB-002 — No lore wall.** *Provisional.* The first session introduces the fiction in one or two sentences and the mechanics in context. It does not require reading the Bible, the changelog or a glossary before creating a nation. A "how the world works" page is linked, not forced.

**ONB-003 — Registration is not the tutorial.** *Provisional.* Account creation explains only what the player must decide at that moment: the e-mail is for verification and recovery; the handle is public; the password is not recoverable by the game. Nation creation follows as a separate, short step so the player understands that the account survives the nation.

**ONB-004 — Verification is explained, not hidden.** *Provisional.* The player is told that a verified e-mail is required before nation creation, that it is used for recovery and security notices, and that it is not shown to other players. If SMTP is not configured, the project runs only as a supervised preview with pre-provisioned accounts (D-020/D-029); it does not accept public registrations it cannot verify.

**ONB-005 — The clock is taught once.** *Provisional.* The first session explains the fixed 2-hour UTC boundary, shows the next boundary in the player's local time and the server time, and states that actions submitted before the boundary resolve at it. It does not teach every timing rule; it teaches the one that matters for the first action.

**ONB-006 — The first decision is real.** *Provisional.* The first action changes something the player can see (an emphasis, a baseline allocation or a first construction choice). It is not a fake button, a "collect reward" click or a modal that only advances a tour. The player should experience one cause-and-effect chain before the first boundary.

**ONB-007 — Tutorial progress is account-level.** *Provisional (REQ-038).* Tutorial progress, dismissed hints and completed orientation steps belong to the **account**, not the nation. A reroll does not replay mandatory steps the account has already completed. A replacement nation gets a short "what is different now" orientation instead.

### 11.2 Tutorial rules

**ONB-008 — Required versus optional.** *Provisional.* Only three things are required before the first nation exists: a verified e-mail, a valid name and an explicit creation confirmation. Everything else is optional or contextual. A mandatory tour that blocks play is not adopted; the player may dismiss it and reopen it later.

**ONB-009 — Skip and resume.** *Provisional.* Every tutorial step can be skipped. Skipping is recorded as a preference, not as a failure. The player can resume from the point they left, from the help menu or from the relevant screen. A skipped step is not silently marked "completed" in a way that hides a mechanic the player never saw.

**ONB-010 — Contextual help.** *Provisional.* Help is attached to the screen where it is needed: the turn clock, the treasury, the development lines, the trade panel, the diplomacy panel, the alliance panel, the war board and the reroll/security pages. A help entry states the rule, the cost, the timing and one example. It does not require the player to leave the screen.

**ONB-011 — Reopening help.** *Provisional.* Every contextual help entry can be reopened from the screen and from a help index. A "do not show again" preference is per account and reversible. The help index is searchable by the names the interface uses, not only by internal IDs.

**ONB-012 — Accuracy when mechanics change.** *Provisional.* Tutorial and help content carry a version. When a rule changes, the affected step is updated and its version is bumped. A player who completed the old step sees a short "this changed" note the next time the screen is opened; the step is not silently presented as if the old text were still current. A help page that contradicts the owning rulebook is a defect.

**ONB-013 — Immediate versus boundary actions.** *Provisional (B-02 TR-004).* Every tutorial action is labelled **now** or **at the next turn**, with the closing time. The interface never implies that a queued action has already taken effect. The first digest confirms what resolved.

**ONB-014 — No pressure mechanics.** *Provisional (DP-002).* The tutorial does not use countdown pressure, streak language, "act now or lose it" prompts or presence rewards. It may show the next boundary because that is the game's clock, not because the player must be online for it.

**ONB-015 — Tutorial and protection.** *Provisional.* The first-session flow explains newcomer protection in one sentence and links to the rule. It does not promise that protection makes the player safe from every action; it states which actions are restricted and when protection ends.

**ONB-016 — Accessibility and small screens.** *Provisional (Prompt 13 input).* The flow must be completable with a keyboard, at a readable text size and on a small screen. No step depends on hover, drag, colour alone or a precise pointer. Prompt 13 owns the detailed accessibility specification; this document records the requirement so the flow is not designed as a desktop-only tour.

### 11.3 Where the policies live

**ONB-017 — One visible policy surface.** *Provisional.* The first session links to: the one-account and shared-network rules; the reroll warning and confirmation; the privacy notice and data summary; the recovery and security page; the appeal route; and the game rules. The links are present before the player creates a nation, not buried after it. The pages are written in player language and link to this document for the detailed rule.

**ONB-018 — The short version is honest.** *Provisional.* The player-facing summary of this document says: one account and one nation per person; people who share a network may be limited from interacting until reviewed; a nation can be permanently deleted and replaced immediately, but its progress is lost; account sanctions and shared-network limits survive; and no system can prove how many people are behind an account. It does not promise perfect enforcement.

---

## 12. Newcomer protection and progression

### 12.1 Eligibility and duration

**ONB-019 — First-nation protection is account-scoped and once-only.** *Provisional (REQ-073; D-021).* Newcomer protection is granted to an account's **first** nation only. It is consumed when that nation is created and is **not** restored by deleting the nation, rerolling, recovering the account or creating a replacement. A second account is prohibited; a second nation on the same account is a replacement and is not protected.

**ONB-020 — Duration.** *Provisional parameter (`P_prot`).* Protection lasts **7 days (84 turns)** from the nation's creation or until the nation first initiates an offensive action, whichever comes first. It is not extended by logging in, by being attacked, by posting or by any other activity. The end turn is displayed on the nation page.

**ONB-021 — Account age versus nation age.** *Provisional.* **Account age** is the time since the account was verified. **Nation age** is the time since the current nation was created. Protection depends on **account-level first-nation eligibility**, not on nation age alone; a replacement nation may be new but the account is not. Ranking and dormancy use nation age (D-028); recovery and anti-abuse use account age. Conflating the two is how a reroll becomes a protection reset.

**ONB-022 — Start and end are visible.** *Provisional.* The nation page shows `protected until Turn N (date/time)` or `protection ended`. The end is a turn boundary, not a hidden timer. If protection ends because the nation attacked, the page and the digest state that.

### 12.2 What protection does

**ONB-023 — Protected from offensive action.** *Provisional.* While protected, the nation cannot be targeted by a new offensive campaign, raid, espionage operation or hostile event. Existing defensive obligations? The nation has none at creation. A protected nation cannot be dragged into a war by an alliance; alliance membership does not extend protection to allies or remove it from the protected nation.

**ONB-024 — Cannot initiate offensive action.** *Provisional.* A protected nation cannot declare war, launch a campaign operation, raid or conduct offensive espionage. It can defend if attacked, but it should not be attackable in the first place; the defensive path exists for completeness and for a boundary-crossing edge case.

**ONB-025 — Ordinary play continues.** *Provisional.* A protected nation can build, produce, research, trade with third parties (subject to the fresh-nation transfer rule), join an alliance, sign a treaty with a third party, appear in rankings and participate in world events that are not offensive. Protection is not a pause and not a separate world.

**ONB-026 — Diplomacy.** *Provisional.* A protected nation may negotiate, sign and be bound by treaties with third parties. It may not be made a co-belligerent against its will. A treaty that requires it to join an offensive war is suspended for the protected nation until protection ends; the other party is told. Prompt 08 owns the treaty clause.

**ONB-027 — Communication.** *Provisional.* Other players who attempt to target a protected nation see a clear message: the nation is within its first-week protection and cannot be attacked until Turn N. The protected player sees the same end turn. The message does not reveal the player's account age or identity.

**ONB-028 — No catch-up acceleration.** *Approved policy (D-021).* Protection does not grant extra resources, yield, research, military power, score or a faster start. It restricts hostile interaction; it does not accelerate growth. No veteran tax, no newcomer bonus and no "catch-up" bundle is introduced here. Any future catch-up design must satisfy ECON-012 and be recorded separately.

**ONB-029 — No protection farming.** *Provisional (INV-018).* Because protection is consumed at first nation creation and never restored by reroll, a player cannot obtain a second protected start. A player who creates a first nation, deletes it and creates a replacement loses protection with the first nation. If an account's first nation is removed by an administrator for a technical reason, the operator may restore first-nation eligibility; that is a recorded correction, not a normal path.

**ONB-030 — Review of suspected abuse.** *Provisional.* An operator may remove protection early if there is independent evidence that the account is a duplicate, a bot or a coordinated operation. The removal is recorded with a reason, the account is notified, and the normal appeal applies. A shared-network restriction alone does not remove protection.

### 12.3 The fresh-nation transfer restriction

**ONB-031 — One-sided transfers are restricted for new nations.** *Provisional (C-3; REQ-073).* For the first **30 days (360 turns)** of a nation's life, the nation may not send one-sided value to another account: no gifts, aid, subsidies, loans, debt repayments or bank transfers to another account. It may conduct **reciprocal trades at fair value** within the band Prompt 07 defines. The restriction applies to first and replacement nations alike. It is disclosed before creation and shown on the nation page.

**ONB-032 — Why a window.** *Provisional.* The window makes the standard starting bundle difficult to convert into a transfer to another account, without banning legitimate new players from trading. It is not a catch-up penalty and does not reduce the bundle. The exact duration and fair-value band are Prompt 07's, with Prompt 14 validating them; the provisional values here are 30 days/360 turns and a band to be specified.

**ONB-033 — Reroll does not reset the window unfairly.** *Provisional.* A replacement nation starts a new nation-life window because it is a new nation and receives a new standard bundle. This is not a first-time benefit; it applies to every new nation. Repeated rerolls to exploit the window are addressed by RRL-024 and RRL-030, not by a hidden penalty on legitimate players.

### 12.4 Progression milestones

**ONB-034 — Milestones are records.** *Provisional.* The first-week and first-month milestones (first boundary, first trade, first treaty, first alliance, first campaign, first 30 days) are records or cosmetic acknowledgements. They do not grant resources, yield, military power, protection or ranking weight. Prompt 11 owns the achievement framework.

**ONB-035 — No repeatable first-time economic reward.** *Provisional.* Any future first-time reward must be account-scoped, non-transferable, non-convertible and awarded once per account. It may not be re-earned by rerolling. This is the same rule as NAT-046, stated here because progression and protection are where the temptation appears.

**ONB-036 — Progression is legible.** *Provisional.* A player should be able to see, without a spreadsheet, what they have built, what it produces, what it costs and what decision is next. The digest is the primary explanation (B-02 §23); the nation page is the summary; the help entry is the detail. A progression system that requires an external calculator is a design defect.

---

## 13. Dormancy and returning players

### 13.1 Dormancy

**ONB-037 — Dormancy threshold.** *Approved policy (D-028); threshold provisional.* A nation becomes **dormant after 14 consecutive days (168 turns) without an authenticated session** by its owning account. The threshold is measured in turns, not in calendar days alone, so a boundary is never ambiguous. The value is provisional pending playtest; the effects are confirmed policy.

**ONB-038 — Dormant status is visible.** *Provisional.* The nation page shows `dormant since Turn N` and the condition to end it. Other players see that the nation is dormant; they do not see when the player last signed in, the account's e-mail or any private reason.

**ONB-039 — What dormancy does.** *Approved policy (D-028).* While dormant, the nation:

1. **cannot be targeted by new offensive actions** (campaign, raid, espionage, hostile event);
2. **cannot initiate offensive actions**;
3. remains in the world and keeps its alliance membership;
4. is **excluded from public rankings and published aggregates** as a presentation rule, not a penalty;
5. suffers **no resource, progression or ownership loss** beyond the normal economy's own rules;
6. continues to receive its queued and recurring effects under the normal economy rules;
7. retains its treaties and obligations, subject to Prompt 08's rules for a party that cannot act.

**ONB-040 — The world does not wait.** *Approved policy (B-02 TR-084).* The shared 2-hour UTC turn continues while a player is offline. Dormancy changes what can be done to the nation, not whether the turn resolves. No turn is skipped, no production is paused and no player is required to be present.

**ONB-041 — No decay for absence.** *Approved policy (DP-002).* Dormancy adds no decay, no tax, no loss of score, no loss of buildings, no loss of research and no loss of protection eligibility. A dormant nation may fall in the rankings because it is not competing, but the game does not confiscate its state.

### 13.2 Returning

**ONB-042 — Return ends dormancy.** *Approved policy (D-028).* The first authenticated session ends dormancy. Protection from attack lasts **until the first boundary after that session** (at most 2 hours) and is not extended by further logins without play. This gives a returning player one boundary to re-orient without creating a renewable shield.

**ONB-043 — Re-entry summary.** *Provisional (REQ-022).* On return, the player sees a summary of the missed period: turns elapsed, production and upkeep totals, major changes in rankings and alliances, treaties or campaigns that began or ended, open decisions, and a link to the full digest archive. The summary is grouped, not a wall of per-turn rows; the player can open the detail.

**ONB-044 — Continue with the existing nation.** *Provisional.* A returning player continues with the existing nation by default. The game does not force a reroll, a new account or a new registration. The nation's state, history and relationships are intact.

**ONB-045 — Voluntary reroll on return.** *Provisional.* A returning player may choose to reroll (§9) instead of continuing. The reroll is voluntary, uses the same account, requires the same confirmation and loses the same progress. It is not required to "catch up" and it does not grant protection.

**ONB-046 — Returning after archival.** *Approved policy (D-028).* After **12 consecutive months dormant**, a nation is **archived**: removed from the world graph and rankings, data retained, with a notice to its verified e-mail **30 days before** archival. A login within **12 months of archival** restores it. Restoration returns the nation to the world at its stored state; it does not replay the missed turns or grant compensation. After the restoration window, the archived record is retained for history but the nation is not reactivated by a normal login; Prompt 12's deletion policy and UD-017 apply.

**ONB-047 — No automatic deletion.** *Approved policy (D-028).* No nation is deleted at 14 days, at 12 months or by dormancy alone. Deletion occurs only on the owner's request (reroll or closure) or under a separately disclosed policy in Prompt 12. "Dormant" and "archived" are not synonyms for "deleted".

### 13.3 Dormant alliances, treaties and campaigns

**ONB-048 — Alliance membership persists.** *Approved policy (D-028); details Prompt 09.* A dormant nation stays in its alliance. It cannot vote, accept a role, authorise a bank transfer or join a new operation while dormant. Prompt 09 decides whether an inactive member counts for quorum, taxation or succession; the default is that dormancy does not silently expel a member and does not let the alliance spend the dormant nation's reserved value.

**ONB-049 — Treaties persist.** *Provisional; details Prompt 08.* A dormant nation's treaties remain in force. A treaty that requires an action the dormant nation cannot take is suspended for that party rather than breached; the other party is notified. A treaty that requires a decision at a boundary waits for the return or expires under its own terms; it does not silently bind the dormant nation to a new obligation.

**ONB-050 — Campaigns.** *Provisional; details Prompt 10.* A dormant nation cannot be targeted by a **new** offensive action. An existing campaign continues to resolve under Prompt 10's rules; the dormant nation's defensive participation is resolved automatically from its frozen state, and it cannot launch new operations. This prevents a player from parking a nation in a war to avoid consequences while also preventing a returning player from being farmed indefinitely.

**ONB-051 — Shared-network restrictions survive dormancy.** *Provisional.* A pair restriction is account-level and does not expire because a nation went dormant. A returning player finds the same pair status. Dormancy is not a way to clear a network restriction.

**ONB-052 — Recovery is separate from return.** *Provisional.* A player who still controls the account but has not signed in for a long time returns through normal sign-in. A player who lost the password or the e-mail uses recovery (§10.5). Neither path creates a new account or a new nation.

---

## 14. Privacy and data retention

### 14.1 Data classification

**DAT-001 — Every field has a class.** *Provisional (REQ-023/REQ-057).* The following table is the account-and-creation slice of the project's data inventory. It extends [Report 08 §11.2](../stage-1/08_security_privacy_fair_play_and_trust.md) and does not replace the wider inventory. **Classification:** Public, Private (owning account only), Restricted (authorised integrity/moderation role only), Secret (never exposed; credentials and keys).

| # | Data category | Purpose | Sensitivity | Who may access | Class | Retention | Needed at launch? | Deletable / anonymisable? | Needed for one-account rule? | Protection |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Internal account ID | Stable identity for ownership, audit and history | Low alone; linkable | The account; integrity role; server functions | Private | Account lifetime + audit retention | Yes | Replace with a pseudonym in public views; audit link retained | Yes (links events without exposing identity) | Never a client-supplied identity; server-derived |
| 2 | Authentication identity, password hash, MFA/recovery secrets | Sign-in and account control | **Secret** | Auth service; the account; not the game database in plaintext | Secret | Account lifetime; revoked on closure | Yes | Deleted on closure; hashes not reversible | Indirect (one credential path per account) | Supabase Auth; no password logging; no service key in client |
| 3 | E-mail address and verification state | Verification, recovery, security notices | High (personal) | The account; auth service; a restricted support role for recovery | Private | Account lifetime; purged on closure subject to legal hold | Yes | Deleted on closure; history keeps no e-mail | **Yes** (one verified contact per account; evidence in duplicate cases) | Encrypted in transit and at rest; never public; never in a URL |
| 4 | Public handle / display name | Player-facing identity separate from the nation | Low (chosen) | Everyone | Public | While active; historical if used publicly | Yes | Changeable; removed on closure | No | Escaped text; no e-mail or real name |
| 5 | Nation ID and public nation number | Stable public identity for history, links and records | Low | Everyone | Public | Permanent class-P identity | Yes | Not deleted; the page may be marked retired or closed | Yes (distinguishes nations, not people) | Immutable; never reused; no account fields |
| 6 | Nation public identity (name, short name, emblem, founding turn, status) | The game's public world | Low | Everyone | Public | While active; permanent historical page | Yes | Name may be renamed; historical events keep the name used | No | Public by design; no private fields on the page |
| 7 | Nation ownership link (`nation_id` ↔ `account_id`) | Authorisation and ownership checks | High when combined | Server functions; integrity role; never public | Restricted | Permanent for audit; public view omits it | Yes | Public views use the nation, not the account; closure keeps an internal link for audit | **Yes** (core of one-active-nation enforcement) | RLS; server-only access; no client-supplied ownership |
| 8 | Nation creation and reroll history | Integrity, abuse review, historical attribution | Medium | The account; integrity role | Restricted | Permanent for IDs and timestamps; class-S detail per D-026 | Yes | Public history keeps nation IDs; account-level detail can be minimised | **Yes** (detects reroll abuse, protection farming, sanction evasion) | Append-only; no client edit |
| 9 | Account creation and activity timestamps | Dormancy, protection eligibility, abuse review | Medium | The account; integrity role | Restricted | Account lifetime + retention | Yes | Coarsened in public views; deleted/anonymised on closure | Yes (account age vs nation age) | Server timestamps only; no client clock |
| 10 | Network association signals (keyed digest, first/last seen) | Pair matching and review | High (linkable to a network) | Integrity role; server functions | Restricted | **180 days** after last seen (provisional) | Yes | Deleted after retention; digest cannot be reversed without the pepper | **Yes** (shared-network control) | HMAC; no raw IP; pepper outside the database; access logged |
| 11 | Shared-network restriction records (pair state, review status, decisions) | Enforce and review pair restrictions | High | The two accounts (their own status); integrity role | Restricted | Active + **12 months** after closure | Yes | Pair record closed and minimised; audit act retained | **Yes** (prevents restriction evasion by IP change or reroll) | Canonical pair; no raw IP; no public badge |
| 12 | Verification attestations and review notes | Clearance decisions and appeals | High | Integrity role only | Restricted | Case closure + 12 months, or longer if an open case requires | Yes (only when a review is requested) | Deleted after retention; the decision summary remains | Yes (supports a clearance decision) | Restricted access; no sensitive documents collected |
| 13 | Enforcement and appeal records | Fair-play decisions, appeals, ban-evasion evidence | High | Integrity role; the affected account sees its own outcome | Restricted | Class-O floor 12 months after closure; audit spine permanent | Yes | Anonymised where possible; evidence retained for open cases and legal obligations | **Yes** (sanctions survive reroll) | Least privilege; every read logged; no public disclosure |
| 14 | Session and recovery state | Security, revocation, recovery | High | The account (own sessions); auth service; restricted support for recovery | Restricted | Session lifetime; recovery case + retention | Yes | Revoked/deleted on logout, closure or recovery completion | Indirect (prevents credential sharing) | Short-lived tokens; rotation; revocation; no token logging |
| 15 | Private notification data | Tell the player what happened | Medium | The account | Private | Until read + 90 days, unless attached to an open case | Yes | Deleted with the account; security notices retained as audit | No | Per-account access; no other player's data |
| 16 | Public world history (chronicle, rankings, wars, treaties, alliance history) | The shared record; historical integrity | Low–medium (public by design) | Everyone | Public | Class-P permanent; class-S bounded (D-026) | Yes | Not deleted; names are historical; private fields never enter it | **Yes** (attributes acts to the correct nation) | Append-only; corrections are new events; no account/e-mail fields |
| 17 | Audit spine (value mutations, pipeline phases, privileged acts) | Integrity, recovery, security | High | Integrity/operations role only | Restricted | **Permanent** (REQ-027) | Yes | Not deleted; contains IDs, not passwords | **Yes** (evidence for enforcement and reroll review) | Append-only; restricted; access logged |
| 18 | Backups and exports | Disaster recovery | **Secret** (contain everything) | Owner/operator only, off-platform | Secret | 7 daily + 3 monthly (D-025) | Yes, before public launch | Rotated; account deletion propagates by rotation, disclosed | Indirect | Encrypted; off-platform; restore drill (CF-02) unexecuted |

**DAT-002 — No raw IP in the game database.** *Provisional (C-4).* The application stores a keyed digest for matching, not the address. The digest is produced by the Cloudflare Pages Function (§5.2). If an implementation cannot avoid storing a raw address for a specific review, that storage is a separate, documented exception with the shortest possible retention, restricted access and a deletion job; it is not the default and it is not required by this design. **No raw IP, e-mail address or account ID is ever shown to another player.**

**DAT-003 — Retention table.** *Provisional (D-026).* The controlling retention values are:

| Data | Retention | Basis |
|---|---|---|
| Raw IP | **Not stored** by the application | Minimisation; C-4 |
| Network digest / observation | **180 days** after last seen | Pair matching and review; provisional |
| Pair record | Active + **12 months** after closure | Enforcement continuity; provisional |
| Attestation and review notes | Case closure + **12 months**, longer only for an open case | Class-O floor; D-026 |
| Account, e-mail, sessions | Account lifetime; deleted on closure | Service necessity |
| Nation public identity and class-P history | **Permanent** | Historical integrity; D-026 |
| Class-S digest detail | Hot **30 days**, monthly summaries **12 months**, then deleted | D-026 |
| Audit spine | **Permanent** | REQ-027 |
| Enforcement/appeal records | **12 months** after case closure; longer for an open case | D-026 |
| Backups | **7 daily + 3 monthly** | D-025; deletion propagates by rotation |
| Unverified account with no activity | **30 days**, then cleanup with warning | ACC-026 |

The table is a maximum, not a promise to keep everything. A shorter period is allowed where no open case and no legal obligation require the record.

### 14.2 Access and disclosure

**DAT-004 — Least privilege.** *Provisional (REQ-025; SEC-026/027).* Access is role-scoped: a player sees their own account and nation; an integrity reviewer sees the pair record and the evidence needed for the case; a support role sees status but not attestations or evidence; an ordinary administrator does not see private evidence by default. Every privileged read of a restricted record is logged. The game does not have a "see everything" idle role.

**DAT-005 — Public does not mean linked.** *Provisional.* A public nation page may show the nation's name, short name, emblem, founding turn, status, public ranking, public treaties, public alliance and public war history. It may not show the account's e-mail, account ID, IP, network digest, pair status, enforcement record, recovery state, session data or private notifications. A public chronicle entry names the nation, not the account.

**DAT-006 — Deletion, closure and anonymisation.** *Provisional.* On account closure: credentials, recovery codes and e-mail are deleted; sessions are revoked; private notifications and private profile data are deleted; the nation is retired; public historical records remain with the nation identity; the internal account link is retained only where the audit spine or an open case requires it and is restricted. A data-subject deletion request follows the same path subject to UD-017 and any legal hold. The project does not claim that deletion reaches backups before their rotation; that caveat is disclosed (§14.4).

**DAT-007 — No analytics, advertising or sale.** *Provisional (REQ-023).* The game does not run third-party analytics, advertising pixels, behavioural profiling or data sales. Aggregate operational counters are computed from the game's own events and published only under D-027's k = 5 rule. A future proposal to add analytics is a new decision with a privacy review, not a default.

**DAT-008 — E-mail use.** *Provisional.* The e-mail is used for verification, password reset, security notices, closure/archival notices and essential account communication. Marketing requires a separate opt-in and is not part of this design. The address is never sold, published or shown to another player.

**DAT-009 — Review evidence.** *Provisional.* Attestations, review notes and enforcement evidence are restricted. They are not attached to the public nation page, the chronicle or an alliance record. A decision summary may be shown to the affected account; the full evidence is not. A reviewer's personal notes are not a place for sensitive data that the case does not need.

**DAT-010 — Data-subject requests.** *Provisional.* A player may request access to their account data, correction of inaccurate data, or deletion on closure. The request is authenticated; the game does not disclose another player's data or the existence of an account to an unauthenticated requester. A request that would destroy an open case's evidence is handled under Prompt 12's preservation rules and UD-017.

**DAT-011 — Backups.** *Provisional (D-025).* Backups are encrypted, off-platform and rotated; a restore is a disaster-recovery action, not a way to resurrect a rerolled nation. A restored database must not reintroduce a retired nation into the active world. **No backup has been taken and no restore has been performed**; CF-02 remains unexecuted.

**DAT-012 — Legal posture.** *Deferred (UD-017).* The jurisdiction, lawful basis, notice, retention limits, age gate and cross-border transfer position are legal questions. This document records the minimisation intent; it does not claim GDPR, CCPA, COPPA or any other regime's compliance. Prompt 12 prepares the player-facing notice; the owner obtains review before public launch.

### 14.3 What is never collected

| Not collected | Why |
|---|---|
| Government ID, passport, driver's licence | No necessity for a browser strategy game; disproportionate |
| Face photograph or biometric template | Same; the P&W photograph process is explicitly rejected (C-5) |
| Precise home address or GPS location | Not needed; network prefix is already coarse |
| Phone number or SMS | No paid verification dependency; recovery uses e-mail and codes |
| Real name | The nation and handle are the game identity |
| Keystrokes, screen recordings, clipboard, device fingerprint | Surveillance posture; unnecessary for turn-based play |
| Private message content at first playable | No private-channel system is designed; if added, it needs its own inventory entry |
| Third-party analytics identifiers | No analytics or advertising |

### 14.4 Disclosed limitations

- A network digest is pseudonymous, not anonymous: if an attacker obtains the pepper, matching becomes easier. The pepper is a secret and is rotated only with a plan.
- A determined player can use a network that does not match, a second device or an intermediary. The control is not a guarantee.
- Backups can retain closed-account data until rotation; deletion is not instantaneous across backups.
- A public historical record can preserve a nation name that a person later wishes to disassociate from. The page does not contain the person's e-mail or account, but the name remains part of the shared world's history. Prompt 12 and UD-017 must decide any exception.
- No legal compliance is claimed. The table is a design intent, not a legal opinion.

---

## 15. Security invariants

**INV-001 — Every invariant has a test.** *Provisional.* These are design invariants for future database, backend and test work. **None has been tested against running code, because no game code exists.** The test column names the specification test in §19; a test is a plan, not a result.

| ID | Invariant | Requirements and rules | Future test |
|---|---|---|---|
| INV-001 | A person may operate only one game account under the game policy | ACC-001/ACC-003; REQ-043 | T03-A01 (policy and review evidence; not a technical proof) |
| INV-002 | An account owns at most one active nation | ACC-014; REQ-061 | T03-A02, T03-A05 |
| INV-003 | A completed reroll permanently removes the old active nation state | RRL-007/RRL-013; REQ-068 | T03-C02, T03-C03 |
| INV-004 | A normal reroll does not require a waiting period before replacement creation | RRL-004; REQ-067 | T03-C05 |
| INV-005 | Nation creation and reroll are safe under repeated and concurrent requests | NAT-005/NAT-006; RRL-009/RRL-023; REQ-070 | T03-A05, T03-C06, T03-C07 |
| INV-006 | A reroll never transfers old nation assets or progression to the replacement | RRL-014; REQ-068 | T03-C03 |
| INV-007 | Account-level sanctions survive nation deletion | RRL-016/RRL-017; REQ-069 | T03-C09 |
| INV-008 | Prior history remains attributable to the correct historical nation identity | NAT-040; RRL-020; REQ-071 | T03-C10 |
| INV-009 | A shared-IP relationship may restrict interactions between the affected accounts | NET-001/NET-017; REQ-062 | T03-B01 |
| INV-010 | A shared-IP match alone is not sufficient proof for a permanent multi-account ban | NET-039; REQ-066 | T03-B09 |
| INV-011 | Shared-network restrictions are enforced server-side | NET-009/NET-010; REQ-065 | T03-B03, T03-D03 |
| INV-012 | A client cannot falsify its IP association by editing a submitted value | NET-005/NET-012; REQ-065 | T03-D03 |
| INV-013 | Restricted accounts cannot exchange value or coordinate unfair advantages through indirect systems | NET-025/NET-026; REQ-063 | T03-B04, T03-B05, T03-B06 |
| INV-014 | Legitimate shared-network players have a route to verification or review | NET-030…NET-037; REQ-064 | T03-B08 |
| INV-015 | Changing IP addresses does not automatically clear an existing restricted relationship | NET-016; REQ-062 | T03-B07 |
| INV-016 | One player cannot bypass an interaction restriction through an intermediary account | NET-026; REQ-063 | T03-B06 |
| INV-017 | The replacement nation receives only its approved standard starting state | NAT-012/NAT-013; RRL-013; REQ-072 | T03-C03, T03-C04 |
| INV-018 | Rerolls cannot repeatedly generate transferable first-time rewards | NAT-046; RRL-024; ONB-029/ONB-035; REQ-073 | T03-C12, T03-E05 |
| INV-019 | Nation naming or nation-ID changes cannot transfer ownership | NAT-037; REQ-071 | T03-A04 |
| INV-020 | Account recovery restores the existing account without creating a second nation | ACC-035; REQ-074 | T03-D06 |
| INV-021 | Private account information is never exposed through public nation records | DAT-005; REQ-075 | T03-D01 |
| INV-022 | Historical game events cannot be invisibly erased by rerolling | RRL-019/RRL-020; REQ-068/REQ-071 | T03-C10 |
| INV-023 | Account suspension and permanent bans are not bypassed by the normal reroll process | RRL-017; REQ-069 | T03-C09 |
| INV-024 | Player inactivity does not stop the shared two-hour UTC turn clock | ONB-040; B-02 TR-084 | T03-E07 |
| INV-025 | Newcomer catch-up acceleration is not silently introduced through the reroll or protection systems | ONB-028; D-021; REQ-073 | T03-E05 |
| INV-026 | The account ID is stable across credential, e-mail, handle and nation changes | ACC-013; REQ-074 | T03-D07 |
| INV-027 | A pair restriction is not an account suspension or a finding of cheating | NET-024; ACC-016; REQ-062 | T03-B10 |
| INV-028 | Concurrent creation or reroll requests cannot produce two active nations | ACC-014; NAT-006; RRL-023; REQ-070 | T03-A05, T03-C06 |
| INV-029 | Account closure does not delete the audit record or the public historical identity required by policy | ACC-044; DAT-006; REQ-075 | T03-D08 |
| INV-030 | No sensitive identity verification is required by default | ACC-007; C-5; REQ-064 | T03-D04 |
| INV-031 | A blocked interaction moves no value and changes no ownership | NET-029; REQ-063 | T03-B11 |
| INV-032 | Every enforcement action has a recorded reason and an appeal route | NET-038/NET-044; REQ-064 | T03-B12 |

**INV-ENF — Enforcement is layered (closing principle, not one of the numbered invariants).** *Provisional.* INV-001…INV-032 are the numbered set; this paragraph fixes where they must be enforced. A rule that exists only in a document is not enforced. The future implementation must place each invariant in the layer that can actually enforce it: a database constraint for INV-002/INV-028; a server-side authorisation check for INV-011/INV-012/INV-031; an immutable record for INV-008/INV-022/INV-029; a reviewed process for INV-001/INV-010/INV-032. A test that only checks a document is a documentation test, not an implementation test, and must be labelled as such.

---

## 16. Required player journeys

**J-00 — How to read the journeys.** *Provisional.* Each journey states entry conditions, player-visible steps, server-side checks, expected state changes, error handling, recovery, historical records, notifications and rule IDs. "No history" means the event is not a public or permanent record; the audit spine may still record an operational event. The journeys are specifications, not transcripts.

### 16.1 Registration and creation

| ID | Entry and player steps | Server checks | State change and history | Errors and recovery | Notifications | Rules |
|---|---|---|---|---|---|---|
| **J-01** New visitor registers | Opens the public site; reads the one-sentence premise; chooses Register; enters e-mail, password, handle, 13+ confirmation | E-mail format; password policy; handle uniqueness and name rules; rate limit; no existing session | `REGISTRATION_PENDING` → `UNVERIFIED`; auth record created; no nation; audit row | Duplicate e-mail returns a neutral "check your e-mail or sign in" message; invalid handle explains the rule; service failure is retryable | Confirmation e-mail | ACC-023/ACC-024; ONB-001 |
| **J-02** Returning account signs in | Opens the site; signs in; sees the nation and the latest digest | Credential check; session issue; account state; nation state; pair statuses | Session created; no nation change; sign-in timestamp recorded | Wrong password returns a neutral error; lost password goes to reset; `RECOVERY_LOCKED` goes to recovery | Optional security notice for a new network | ACC-027/ACC-030; J-18 |
| **J-03** Player creates their first nation | After verification, opens Create Nation; chooses name, short name, posture; confirms | Session; verified e-mail; account eligible; no active nation; name rules; idempotency; creation pause | `ELIGIBLE` → `ACTIVE`; nation + standard bundle + audit row; public page; protection if first nation | Name collision returns alternatives; unverified returns the verification step; concurrent loss returns the existing nation | Creation success; first-boundary reminder | NAT-001…NAT-025; ONB-019 |
| **J-04** Player submits creation twice | Double-clicks or retries after a lost response with the same key | Idempotency key; existing nation; same payload | One nation; the retry returns the same identity; no second bundle | Same key with a different payload is `AC-06`; a stale tab is told to refresh | Same success message, once | NAT-005/NAT-008 |

### 16.2 Shared networks

| ID | Entry and player steps | Server checks | State change and history | Errors and recovery | Notifications | Rules |
|---|---|---|---|---|---|---|
| **J-05** Two different people at one home IP | Two household members each register and create a nation; each plays independently; they attempt a trade with each other | Same `network_key` within 24h; pair observation; directed trade check | Pair `OBSERVED`; the trade is blocked; the pair becomes `RESTRICTED`; both accounts remain active; no account sanction | Each sees an interaction-limit message and a review link; no value moves; they can keep playing with third parties | Pair restriction notice to both | NET-014/NET-017; NET-025 |
| **J-06** University, office or public network | Many students/colleagues play on one campus or office network; two of them try to trade | Network is `LARGE` (>25 accounts); pair check; second observation rule | No blanket restriction; the attempted trade is blocked; pair `OBSERVED` or `RESTRICTED` per NET-019; no account suspensions | The message explains that large shared networks are common and the block is not an accusation; review is expedited | Pair notice only to the two accounts | NET-019; NET-020 |
| **J-07** A pair receives a restriction | One account attempts a restricted verb against the other | Pair state; verb class; target; idempotency; whether value would move | `RESTRICTED`; blocked event; no value; no ownership change; pair record | The action is rejected with `AC-08`; the player can request review or continue elsewhere | Restriction message; review route | NET-017/NET-021/NET-029 |
| **J-08** Legitimate player requests clearance | One account opens Review; both accounts submit the attestation; they wait | Session; pair membership; attestation completeness; account history; interaction graph; prior cases | `review_status` REQUESTED → IN_REVIEW; pair stays `RESTRICTED` | If the other account does not respond, the request stays open or is decided `INCONCLUSIVE`; the player can add context; no documents are demanded | Request received; decision when made | NET-030…NET-037 |
| **J-09** Restriction lifted after review | Reviewer decides `SEPARATE_PEOPLE` or `FALSE_POSITIVE` | Evidence review; decision record; no open enforcement case | `RESTRICTED` → `CLEARED`; 90-day probation; blocks removed | If the decision is `MAINTAINED`, the player can appeal; the status remains | Clearance notice to both; no public badge | NET-034/NET-036/NET-047 |
| **J-10** An interaction is blocked | A restricted account tries a trade, gift, bank transfer or war declaration | Pair state; verb; target; whether the action is high-risk; network signal present | No value; no war; no reservation; block event recorded | Specific message per verb; `AC-08`/`AC-09`; review link; the player can complete a different action | In-product block message | NET-025/NET-048 |
| **J-11** Suspected multi-account operator investigated | A reviewer sees a pattern: same network, one-directional value flow, coordinated wars, or an admission | Evidence review; pair records; transfer graph; account history; attestations; independent evidence | Pair `MAINTAINED` or `REFERRED`; account-level case opened separately; no automatic ban | The account is notified of any measure; evidence is restricted; appeal route | Notice of the measure with reason category | NET-038…NET-043 |
| **J-12** Appeal an incorrect restriction | A cleared-in-fact player appeals a `MAINTAINED` or a sanction | One appeal; ground; reviewer independence where possible; evidence | `review_status` APPEALED; decision upheld or overturned; record | The restriction remains during the appeal unless interim relief is granted; the decision is written | Appeal received; decision with reasons | NET-044…NET-047 |

### 16.3 Reroll

| ID | Entry and player steps | Server checks | State change and history | Errors and recovery | Notifications | Rules |
|---|---|---|---|---|---|---|
| **J-13** Voluntary reroll | Signed-in player opens Reroll; reads the warning; re-authenticates; types the nation name; confirms | Session; fresh auth; account state; active nation; blocking conditions; idempotency | `REQUESTED` → `RETIRING` → `RETIRED`; old nation retired; assets gone; account eligible | If blocked, the message names the condition; the state is unchanged; retry is safe | Reroll confirmation; retirement summary | RRL-001…RRL-023 |
| **J-14** Reroll with a pending transaction | Player has an accepted trade awaiting settlement and tries to reroll | Pending settlement; turn state (OPEN/LOCKED/RESOLVING) | If OPEN, the player may cancel and retry; if LOCKED/RESOLVING, reroll is blocked until the boundary resolves | `AC-12`; wait for the boundary; no value is lost | Block message with the next boundary | RRL-021/RRL-022 |
| **J-15** Reroll with an account restriction | Player has a pair restriction or a warning and rerolls | Account state; pair records; sanctions; preservation order | Reroll may complete if no blocking condition; account status and pair restriction survive; replacement is restricted with the same pairs | If suspended/banned, creation is blocked; the message names the status and appeal | Reminder that the restriction remains | RRL-016/RRL-017/RRL-029 |
| **J-16** Attempt to use reroll to evade a sanction | A suspended or banned player attempts a reroll, or rerolls after a violation | Account state; case; preservation order; ban | Blocked; no new nation; enforcement record unchanged; attempted evasion recorded | `AC-13`/`AC-18`; appeal route; no new account | Notice; case update | RRL-017/RRL-026/RRL-027 |
| **J-20** Reroll interrupted by a connection failure | The player confirms, the response is lost, the browser closes | Operation state; idempotency key; atomic retirement | On return, the page shows `RETIRED` (create a replacement) or `REQUESTED/BLOCKED` (nothing deleted); retry is safe | The player is never shown an ambiguous half-state; support can read the operation record | State message on return | RRL-008…RRL-011 |

### 16.4 Return, recovery and closure

| ID | Entry and player steps | Server checks | State change and history | Errors and recovery | Notifications | Rules |
|---|---|---|---|---|---|---|
| **J-17** Return after long inactivity | Player signs in after weeks or months | Credential; dormancy threshold; archived status; pair status | Dormancy ends; one-boundary return grace; re-entry summary; no forced reroll | If archived, the restore window is shown; if beyond it, support explains the state | Return summary; security notice | ONB-037…ONB-047 |
| **J-18** Player loses account access | Player cannot sign in; uses password reset or a recovery code; if both fail, requests review | Reset token; code validity; account state; recovery case; no enumeration | `RECOVERY_LOCKED`; sessions revoked; nation frozen; on success `ACTIVE` with the same nation | Invalid/expired token returns a neutral retry; a lost e-mail without a code may be declined; no new account | Recovery started/completed; security notice | ACC-030…ACC-038 |
| **J-19** Player requests account closure | Player opens Account; chooses Close; reads the cooling notice; confirms; may cancel | Session; fresh auth; cooling period; open case; preservation order | `CLOSURE_REQUESTED`; nation limited; after 7 days `CLOSED`; credentials/private data deleted; public history remains | The player can cancel during cooling; an open case may delay closure; the message says why | Closure requested/cancelled/completed | ACC-043…ACC-046 |

### 16.5 Journey coverage check

| Requirement | Journeys |
|---|---|
| Registration and first nation | J-01, J-02, J-03, J-04 |
| Shared network: home, institution, restriction, clearance, block, investigation, appeal | J-05…J-12 |
| Reroll: normal, pending, restricted, evasion, interruption | J-13, J-14, J-15, J-16, J-20 |
| Return, recovery, closure | J-17, J-18, J-19 |

All twenty journeys in the Prompt 03 brief are covered. J-20 is intentionally placed with the reroll group even though it appears after J-16 in the brief's numbering; the ID is stable and the coverage table is authoritative.

---

## 17. Player-facing messages

**MSG-00 — Message rules.** *Provisional.* Every message says what happened, why (without private data), and what the player can do next. Messages never include an IP address, network key, another account's e-mail or account ID, an internal stack trace, a secret, moderation evidence, or a statement that an e-mail address is or is not registered. A shared-network message is an **interaction limit**, never an accusation of cheating.

| ID | Trigger | Message (player text) | Next action | Rules |
|---|---|---|---|---|
| **MSG-01** | Registration / policy notice | "One person may hold one account and one active nation. Households and shared networks are allowed; accounts that share a network may be limited from interacting until reviewed. We cannot prove how many people are behind an account, so this rule is enforced by controls and review, not by scanning you." | Read the full rule | ACC-001/ACC-006; ONB-018 |
| **MSG-02** | Nation created | "[Nation] now exists. Your standard starting state is in place. The next turn closes at [time] UTC. You can queue one action now; it resolves at that boundary." | Open the nation | NAT-004; ONB-001 |
| **MSG-03** | Creation already completed | "This account already governs [nation]. Open it to continue. If you meant to start a new nation, you must reroll the existing one first; that permanently deletes it." | Open nation / Reroll | NAT-008 |
| **MSG-04** | Name unavailable | "That name is already in use or held. Try another name. Names are compared without regard to capitalisation or accents, and a renamed name is held for 30 days." | Choose another name | NAT-029/NAT-036 |
| **MSG-05** | Name invalid | "That name cannot be used: [specific rule]. Use 3–32 letters, digits, spaces, hyphens, apostrophes or full stops, with at least one letter. Example: [example]." | Edit the name | NAT-026…NAT-033 |
| **MSG-06** | Duplicate creation request | "This request was already received. We have not created a second nation. Open your nation, or refresh if you do not see it." | Open / refresh | NAT-005 |
| **MSG-07** | Pair restriction applied | "Interactions between your account and [nation] are limited because both accounts recently used the same network. This is an interaction limit, not a finding that you cheated. You can keep playing, trade with other nations and request a review." | Request review / continue | NET-017/NET-048 |
| **MSG-08** | Restricted transfer or trade | "This transfer is blocked because [nation] and your account are under a shared-network interaction limit. No value moved. You can trade with other nations or request a review of the limit." | Review / choose another counterparty | NET-025/NET-029 |
| **MSG-09** | Restricted warfare interaction | "This war declaration is blocked because [nation] and your account are under a shared-network interaction limit. No war was declared and no Operations Points were spent. You can request a review." | Review / another target | NET-025; RRL-021 |
| **MSG-10** | Shared-network review invitation | "If you and [nation] are different people, each of you can confirm it in your own session and ask for a review. We will look at the interaction history, not at identity documents. The limit stays in place until the review is decided." | Start review | NET-030…NET-033 |
| **MSG-11** | Review request submitted | "Your review request is recorded. The other account has been invited to confirm. The interaction limit remains while the review is open. We aim to decide within 7 days; that is a target, not a guarantee." | Wait / add context | NET-031/NET-059 |
| **MSG-12** | Review cleared | "The review found that the accounts are separate players (or that the match was incorrect). The interaction limit has been removed. A 90-day watch applies; it does not restrict normal play." | Continue | NET-034/NET-036 |
| **MSG-13** | Review maintained | "The interaction limit remains after review because the evidence did not establish separate players. You can appeal once with a reason. The limit is not a ban and normal play with other nations continues." | Appeal / continue | NET-034/NET-044 |
| **MSG-14** | Reroll warning | "Rerolling permanently deletes [nation]. You lose its treasury, materials, buildings, development, research, military, score, rank, politics, achievements, treaties, alliance role and trade position. Public history may remain. Account sanctions and shared-network limits do not disappear. A replacement can be created immediately, but it starts from the standard beginning and does not receive first-nation protection." | Continue / cancel | RRL-006 |
| **MSG-15** | Reroll confirmation | "Type the exact nation name to confirm. This cannot be undone by a normal undo. [nation name]" | Type name / confirm | RRL-005 |
| **MSG-16** | Reroll completed | "[Nation] is retired. The account is unchanged. You can create a replacement now; no waiting period applies. The old nation's page remains as a historical record." | Create replacement | RRL-002/RRL-020 |
| **MSG-17** | Create after reroll | "Your replacement starts with the standard beginning, not the old nation's wealth. It is not covered by first-nation protection. Its first turn closes at [time] UTC." | Create / review start | RRL-018; NAT-012 |
| **MSG-18** | Account restriction remains | "Your account still has [restriction/sanction] after the reroll. Rerolling does not clear account-level measures. The appeal route is [link]." | Appeal / read status | RRL-016/RRL-017 |
| **MSG-19** | Invalid recovery request | "If an account matches that address, a recovery message has been sent. If you do not receive it, check the address and try again, or use a recovery code. For security, we do not confirm whether an address is registered." | Retry / use code | ACC-030/ACC-034 |
| **MSG-20** | Suspended account tries to create | "This account cannot create a nation while it is suspended. The nation, if any, is frozen. You can read the notice and appeal. Rerolling does not clear the suspension." | Appeal / read notice | ACC-040; RRL-017 |
| **MSG-21** | Recovery success | "Your account is restored. Your current nation is unchanged. All other sessions were signed out. Change your password and review your sessions; regenerate recovery codes if you used one." | Security page | ACC-035/ACC-049 |
| **MSG-22** | Closure requested | "Your account is scheduled to close in 7 days. You can cancel until then. The nation will be retired without a replacement; public history remains; credentials and private data are deleted subject to retention rules." | Cancel / confirm | ACC-043/ACC-044 |
| **MSG-23** | Banned account sign-in | "This account is permanently closed for a rules violation. You can appeal once at [route]. Creating another account to return is a separate violation." | Appeal | ACC-041/ACC-042 |
| **MSG-24** | Appeal decision | "Your appeal was [upheld/overturned]. Reason: [category]. [If overturned: the measure has been removed and the record corrected.] [If upheld: the measure remains; this is the final appeal.]" | Continue / read rules | NET-044…NET-047 |

**MSG-25 — No message may be used as an oracle.** *Provisional.* Error messages must not reveal whether an e-mail is registered, whether a nation belongs to an account, whether a player is under investigation, or whether a pair has prior cases. A generic message with a safe next step is preferred to a specific message that enables enumeration.

---

## 18. Cross-system contracts

**CON-001 — Every subsystem must satisfy its row.** *Provisional.* A later prompt may refine a mechanism but may not contradict the contract. If it cannot satisfy a row, it must amend this document and record why (B-02 TR-095/TR-097 discipline).

| Subsystem | Contract from this document | Owner prompt | Acceptance evidence |
|---|---|---|---|
| **Shared turn engine** | Account/nation creation, reroll and recovery happen outside the boundary; no turn is skipped; no reroll during resolution; inactivity does not stop the clock; the account's absence is irrelevant | 02 | Worked boundary; no action required at the boundary |
| **Economy and treasury** | A new nation gets the standard bundle once; a reroll destroys all value and reservations; no negative balance survives; the starting grant size and deficit rule are Prompt 04's | 04 | Worked creation and reroll balance; conservation identity |
| **Cities, infrastructure and research** | A new nation starts at baseline; a reroll removes all levels, queues and programmes; no building or research is transferred | 05 | Creation/reroll state comparison |
| **Domestic politics** | A new nation uses the default preset; a reroll ends political state; no stability or policy benefit carries | 06 | State table; reroll cleanup |
| **Trade and market** | Directed trade is blocked between a restricted pair; a reroll withdraws offers and requires accepted trades to settle or cancel; the fresh-nation one-sided transfer restriction applies; the fair-value band and window are Prompt 07's | 07 | Pair block test; reroll withdrawal test; fresh-nation test |
| **Diplomacy** | A restricted pair cannot sign a treaty with each other; a reroll terminates the old nation's treaties with a recorded event; the replacement starts neutral; breach-reputation scope is Prompt 08's (UD-033) | 08 | Treaty block; reroll termination; neutral restart |
| **Alliances** | A restricted pair may share an alliance but cannot use the bank or hold simultaneous bank-authorising roles; a reroll ends membership and vacates roles without transferring assets; the replacement applies as a new member | 09 | Bank block; role vacation; no asset transfer |
| **Warfare and campaigns** | A restricted pair cannot attack each other, join the same side or support each other; a reroll is blocked during an active campaign until Prompt 10 defines a forfeit; battle history remains | 10 | Pair war block; reroll block; history attribution |
| **World events, rankings and chronicle** | A new nation is unranked until its first boundary; a reroll removes current ranking and writes a retirement event; old events stay attributed to the old nation; dormant nations are excluded under D-028; no first-time reward is transferable | 11 | Ranking entry; retirement event; historical attribution |
| **Moderation and administration** | Every enforcement action has a reason, a record and an appeal; pair restrictions are not sanctions; IP alone cannot support a permanent ban; preservation orders block reroll; least privilege and logged access | 12 | Case record; appeal; access log |
| **Privacy and security** | No raw IP in the app database; no sensitive identity documents by default; private data never public; retention follows D-026; deletion on closure; audit spine permanent | 12 | Data inventory; access matrix; deletion test |
| **Interface** | Messages, journeys, onboarding, reroll confirmation and review surfaces exist as specified; no pressure or presence mechanics; accessibility requirement recorded | 13 | Screen inventory; journey walkthrough |
| **Formulas and balance** | Every number in this document is a provisional anti-abuse parameter or an unset value; no starting value is invented here; Prompt 14 labels and tests each one | 14 | Parameter table; labelled values |
| **Every subsystem** | A value-moving or coordination verb added later must call the pair check, or the subsystem is incomplete; an unclassified verb is a specification defect | All | Contract test in the subsystem's own document |

**CON-002 — The pair check is a shared service, not a copied rule.** *Provisional.* The shared-network check should be one server-side service with one canonical pair model. A subsystem must not re-implement its own IP matching or its own state names; it calls the shared check and maps the result to its own reason code. Duplicated enforcement is how two subsystems end up disagreeing about whether a pair is restricted.

**CON-003 — The economy owns the numbers; this document owns the boundary.** *Provisional.* The starting bundle's size, the fresh-nation window, the fair-value band and the reroll review threshold are numeric parameters. This document fixes their **shape and purpose**; Prompt 04/07/14 own the values. A later prompt may not use a number here as if it were approved.

### 18.1 Shared reason codes used by this document

**CON-004 — One code per failure, stable across subsystems.** *Provisional.* These codes appear in the rules and journeys above. They are the account-and-creation subset of the game's action-failure vocabulary; B-02 owns the turn-level codes and Stage 5 assigns the final enumeration. A message may add player-language detail, but the stored reason is the code.

| Code | Meaning | Player-facing next step | Rule |
|---|---|---|---|
| `AC-03` | This account already has an active nation | Open the existing nation, or reroll it first | NAT-006/NAT-008 |
| `AC-04` | Nation name unavailable | Choose another name | NAT-029 |
| `AC-05` | Nation name invalid | Edit the name to match the stated rule | NAT-027/NAT-028 |
| `AC-06` | Idempotency key reused with a different payload | Refresh and submit once | NAT-005 |
| `AC-08` | Blocked by a shared-network pair restriction (transfer or trade) | Choose another counterparty or request review | NET-029 |
| `AC-09` | Blocked by a shared-network pair restriction (hostile or coordinating action) | Choose another target or request review | NET-025 row 9 |
| `AC-12` | Reroll blocked by an unsettled settlement or a locked turn | Wait for the boundary, then retry | RRL-021 |
| `AC-13` | Reroll or creation blocked by account status | Read the notice; appeal | ACC-040/ACC-041 |
| `AC-15` | Reroll already completed for this key | Create the replacement | RRL-009 |
| `AC-18` | Action blocked by a preservation order or open case | Contact support; the case must resolve | RRL-021 |
| `AC-20` | Retryable technical failure; no state changed | Retry safely | NAT-007; NET-013 |
| `AC-21` | Account unverified | Confirm the e-mail, then continue | ACC-024 |
| `AC-22` | Creation paused under the free-tier posture | Read the disclosure; retry later | NAT-001; D-022 |

A code that is used but not listed, or listed but never used, fails the documentation check in §19 (REQ-094).

---

## 19. Requirements and test matrix

### 19.1 Requirements owned by this document

**REQ-001…REQ-060 already exist** in the [requirements register](03_requirements_traceability.md) and are not renumbered or redefined here. Prompt 01's brief described REQ-01…REQ-043 as "owned by Prompt 03", but the register's REQ-044…REQ-060 were assigned to other prompts, so this document uses the **next free IDs, REQ-061…REQ-097**, for its own testable requirements. The register rows that this document covers — REQ-002, REQ-003, REQ-022, REQ-038, REQ-039, REQ-043 — keep their IDs and meanings; §19.2 records what changed for them.

| ID | Requirement | Level | Invariants |
|---|---|---|---|
| **REQ-061** | Exactly one active nation per account at all times, enforced server-side and safe under concurrency | Must | INV-002, INV-028 |
| **REQ-062** | Each account pair has one relationship state with documented triggers; a restriction continues until reviewed and is not a suspension | Must | INV-009, INV-015, INV-027 |
| **REQ-063** | Every value-moving or coordinating action is classified in the interaction matrix; indirect routes are covered and a blocked attempt moves nothing | Must | INV-013, INV-016, INV-031 |
| **REQ-064** | Verification, review and appeal exist for pairs and accounts; enforcement is graduated, reasoned and never rests on IP alone | Must | INV-014, INV-030, INV-032 |
| **REQ-065** | The network signal is derived server-side in trusted infrastructure; enforcement happens in the committing transaction | Must | INV-011, INV-012 |
| **REQ-066** | A shared address is never sufficient by itself for a permanent ban or an account-level sanction | Must | INV-010 |
| **REQ-067** | A reroll permanently retires the current nation and allows immediate replacement creation on the same account | Must | INV-004 |
| **REQ-068** | The reset boundary is total: no asset, progress or award is carried, converted, refunded or stored | Must | INV-003, INV-006, INV-022 |
| **REQ-069** | Account identity, sanctions, restrictions, cases and evidence survive nation deletion | Must | INV-007, INV-023 |
| **REQ-070** | Creation and reroll are idempotent, owner-scoped, atomic and safe under retry, interruption and concurrency | Must | INV-005, INV-028 |
| **REQ-071** | Historical records stay attributable to the nation identity that acted; a rename never transfers ownership | Must | INV-008, INV-019 |
| **REQ-072** | Every nation receives the same documented standard starting state, with no invented values | Must | INV-017 |
| **REQ-073** | No first-time benefit, protection or reward can be re-earned by rerolling or converted into a transfer | Must | INV-018, INV-025 |
| **REQ-074** | The account lifecycle states, transitions and recovery rules are explicit and recover the existing account only | Must | INV-020, INV-026 |
| **REQ-075** | Private account data is never exposed publicly; closure deletes private data and keeps required history | Must | INV-021, INV-029 |
| **REQ-076** | The account owns the nation; a nation is never re-parented, claimed or transferred | Must | INV-002, INV-019 |
| **REQ-077** | The one-account rule is policy, enforced proportionately; no text may claim perfect person-level identification | Must | INV-001 |
| **REQ-078** | Subsystems call one shared pair check and map its result; no subsystem re-implements IP matching or state names | Must | INV-013 |
| **REQ-079** | A large or carrier-level shared network never produces blanket account suspension or group bans | Must | INV-027 |
| **REQ-080** | No standing co-resident exemption exists; co-residence is reviewed, not self-certified | Should | INV-014 |
| **REQ-081** | Nation creation is eligibility-checked, owner-scoped and writes the starting state exactly once | Must | INV-005, INV-017 |
| **REQ-082** | Nation names are normalised, validated, filtered and conflict-checked atomically | Must | INV-019 |
| **REQ-083** | Renaming follows the same validation class, is rate-limited, charged only if disclosed, and cannot change ownership | Should | INV-019 |
| **REQ-084** | A released name is held for 30 days and never silently reassigned; identity is the immutable nation ID | Should | INV-019 |
| **REQ-085** | Reroll cleanup across warfare, trade, diplomacy, alliances, rankings, operations and notifications is deterministic | Must | INV-022 |
| **REQ-086** | A reroll is blocked, with a stated reason, by an active campaign, unsettled settlement, preservation hold or disqualifying account state | Must | INV-022 |
| **REQ-087** | Reroll abuse controls exist without an undisclosed cooldown: transfer window, fair-value check, audit anomalies, review threshold | Must | INV-018 |
| **REQ-088** | Account closure is a seven-day cancellable request that deletes private data, retires the nation and keeps required records | Must | INV-029 |
| **REQ-089** | First-session onboarding follows the documented journey; tutorial progress belongs to the account | Should | INV-018 |
| **REQ-090** | Newcomer protection is visibility-only, once per account, skipped between a restricted pair, and never an economic multiplier | Must | INV-018, INV-025 |
| **REQ-091** | Dormant nations remain addressable and ranked per D-028; return needs no new account and no forced reroll; the turn clock is unaffected | Must | INV-024 |
| **REQ-092** | The data classification, access and retention table is enforced; special-category identity data is not collected by default | Must | INV-021, INV-030 |
| **REQ-093** | Administrative review is least-privilege, reasoned, appealable and cannot rewrite public history | Must | INV-032 |
| **REQ-094** | Player messages state the outcome and the next step without private data or enumeration risk | Should | INV-021 |
| **REQ-095** | Every invariant INV-001…INV-032 maps to at least one test specification | Must | all |
| **REQ-096** | Every value-moving or coordinating verb added later names its owning prompt and pair-check status; an unclassified verb is a defect | Should | INV-013 |
| **REQ-097** | This document stays consistent with the Bible outline, the traceability register, both decision registers, DECISIONS.md and the continuity files | Should | — |

### 19.2 What changed for the register rows Prompt 03 covers

| Register row | Before Prompt 03 | After Prompt 03 | Evidence |
|---|---|---|---|
| **REQ-002** (ownership checked on every action) | Provisional; design missing | **Specified**, still Provisional | ACC-014/ACC-015; §6.1; T03-A02/A03 |
| **REQ-003** (account lifecycle and security) | Provisional; "follow SEC-001…008" | **Specified** in more detail; mechanism Deferred to Stage 6 | ACC-017…ACC-049; §10; T03-D06/D07 |
| **REQ-022** (absence produces a re-entry summary) | Provisional; D-021 noted | **Specified**; D-028 applied | ONB-037…ONB-047; §13; T03-E06/E07 |
| **REQ-038** (onboarding teaches one real decision) | Provisional; no design | **Specified** as a journey | ONB-001…ONB-018; §11; T03-E01…E03 |
| **REQ-039** (verification within free caps) | Provisional after D-029 | **Specified**; SMTP vendor still Stage 6 (CF-04) | ACC-024; §10.3; T03-D06 |
| **REQ-043** (one account per person, policy) | Approved (policy) | **Approved, unchanged**; enforcement specified, not perfected | ACC-001…ACC-009; §4; T03-A01 |
| **REQ-024** (retention/deletion per category) | Open | **Partially covered** — account-side retention is specified; the wider inventory and deletion procedure stay Prompt 12 | DAT-001…DAT-012; §14 |
| **REQ-031** (multi-account handling) | Open | **Partially covered** — the pair mechanism and enforcement ladder are specified; detection operations, staffing and tooling stay Prompt 12 | NET-001…NET-060; §5 |
| **REQ-013** (alliance roles) | Open | **Partially covered** — only the pair and reroll contracts | §5.5 row 16; §9.6; Prompt 09 owns the rest |
| **REQ-012** (diplomacy) | Provisional | **Partially covered** — treaty block, reroll termination and neutral restart | §5.5 rows 15; §9.6; UD-033 |

### 19.3 Test specification (to be run when implemented)

**T03-00 — These are specifications, not evidence.** *Provisional.* No row here has been executed. Each test names its setup, action, expected result, requirements and owning implementation prompt. A prompt that implements a subsystem must cite the T03 rows it satisfies, and must not report a row as passing until it has actually run.

#### A. Account and nation ownership

| ID | Setup → action | Expected | Reqs | Verification | Impl. prompt |
|---|---|---|---|---|---|
| **T03-A01** | Records review: policy statements across all current documents | One consistent one-account policy; no claim of perfect identification; a review route exists | REQ-077, REQ-043 | Document review against this document | 03 (this prompt's validator) |
| **T03-A02** | Eligible account with no nation → create one | Nation exists, owned by the account, standard start written once | REQ-061, REQ-081 | Integration test; ownership row check | 03/04 |
| **T03-A03** | Account A acts on account B's nation by ID | Rejected; no state change; no existence disclosure beyond the public page | REQ-076 | Authorisation test | 03 |
| **T03-A04** | Nation renamed twice | Owner, `nation_id` and public number unchanged; old names held | REQ-071, REQ-083 | State check | 03 |
| **T03-A05** | Two concurrent creation requests for one account | Exactly one nation and one starting grant; the loser gets a controlled conflict | REQ-061, REQ-070 | Race test with two resolvers | 03 |
| **T03-A06** | Duplicate creation request with the same key after a lost response | Same nation returned; no duplicate starting state | REQ-070 | Idempotency test | 03 |
| **T03-A07** | Creation request at a turn boundary | Creation succeeds, is absent from that resolution, first digest is the next boundary | REQ-061, REQ-091 | Boundary test | 02/03 |
| **T03-A08** | Unverified, suspended, banned or pause-affected account attempts creation | Each is rejected with its own reason code; nothing is created | REQ-081, REQ-074 | Authorisation matrix test | 03/06 |

#### B. Shared-network restrictions

| ID | Setup → action | Expected | Reqs | Verification | Impl. prompt |
|---|---|---|---|---|---|
| **T03-B01** | Two accounts authenticate from the same network within the window | Pair recorded `OBSERVED`; a restricted verb moves it to `RESTRICTED`; no account sanction | REQ-062, REQ-079 | Integration with a stubbed trusted header | 03/12 |
| **T03-B02** | Restricted pair → direct transfer or directed trade | Rejected; no value, no reservation, no order | REQ-063 | Matrix test per verb | 03/07 |
| **T03-B03** | Restricted pair calls the action endpoint directly, bypassing the UI | Same rejection; enforcement is server-side | REQ-065, REQ-063 | API-level test | 03 |
| **T03-B04** | Restricted pair → market order that would match the other side | Order rejected or excluded; no match | REQ-063 | Market integration test | 07 |
| **T03-B05** | Restricted pair → value routed via a third nation or an alliance bank | Route blocked, queued for review, or flagged as a violation per §5.5 | REQ-063, REQ-078 | Route test | 07/09/12 |
| **T03-B06** | Restricted pair → transfer through a cooperating intermediary | Detected as a violation from the transfer graph; case opened, no automatic ban | REQ-063, REQ-064 | Audit-graph test | 12 |
| **T03-B07** | Restricted pair, then one side changes network | State unchanged; no auto-clear | REQ-062 | State-transition test | 03/12 |
| **T03-B08** | Legitimate pair completes both confirmations and a review | `CLEARED`, 90-day watch, restriction removed, no public label | REQ-064 | End-to-end review test | 12 |
| **T03-B09** | A network observation is the only evidence available | Level 1 only; no suspension or ban | REQ-066, REQ-064 | Ladder test | 12 |
| **T03-B10** | Restricted pair attempts ordinary public actions | Allowed; neither account is suspended; status is private | REQ-062, REQ-079 | Negative-control test | 03/13 |
| **T03-B11** | Blocked attempt inspected | No balance, stock, ownership, declaration or reservation changed; a block event exists | REQ-063 | Before/after state diff | 03 |
| **T03-B12** | Every pair decision and sanction inspected | A recorded reason and an appeal route exist | REQ-064, REQ-093 | Case-record test | 12 |
| **T03-B13** | More than 25 accounts observed on one network | No group restriction or suspension; the pair rule and the conflict rule apply; a reason is recorded | REQ-079 | Load/conflict test | 03/12 |
| **T03-B14** | Attestations and pair records pass their retention date | Evidence pruned on schedule; no raw IP anywhere in the store or the bundle | REQ-065, REQ-092 | Retention-job test | 12 |

#### C. Rerolling

| ID | Setup → action | Expected | Reqs | Verification | Impl. prompt |
|---|---|---|---|---|---|
| **T03-C01** | Reroll submitted without re-authentication or the typed name | Blocked; nothing retired | REQ-067 | UI/API test | 03 |
| **T03-C02** | Confirmed reroll | Old nation retired; retirement record written; account eligible immediately | REQ-067 | Integration test | 03 |
| **T03-C03** | Old nation with treasury, materials, infrastructure, research, units, treaties, alliance role and orders | None present in the replacement; nothing refunded, converted or stored | REQ-068 | State-diff test | 04…10 |
| **T03-C04** | Replacement creation immediately after retirement | Succeeds with the standard start; no cooldown; no protection | REQ-067, REQ-072, REQ-090 | Integration test | 03 |
| **T03-C05** | Time between retirement and replacement | No gameplay delay is required or imposed | REQ-067 | Timing assertion | 03 |
| **T03-C06** | Two concurrent reroll confirmations | Exactly one retirement; at most one replacement | REQ-070 | Race test | 03 |
| **T03-C07** | Lost response, then retry with the same key | Same state; no second retirement, no orphan assets | REQ-070 | Idempotency test | 03 |
| **T03-C08** | Browser closed between confirmation and completion | On return the page states either "retired — create a replacement" or "nothing was deleted"; no ambiguous half-state | REQ-070, REQ-085 | Interruption test | 03 |
| **T03-C09** | Reroll attempted while suspended, banned, or under a preservation order | Rejected; sanction or hold unchanged; attempt recorded | REQ-069, REQ-086 | Authorisation test | 03/12 |
| **T03-C10** | Reroll while an alliance, treaty and pending offer exist | Membership ends, roles vacate, treaties terminate with a recorded event, offers withdraw; old chronicle keeps attribution; replacement unranked then ranked at its first boundary | REQ-085, REQ-071 | Cross-system test | 08/09/11 |
| **T03-C11** | Reroll during an active campaign or an accepted unsettled trade | Blocked with the stated condition; nothing destroyed | REQ-086 | War/trade workflow test | 07/10 |
| **T03-C12** | Value moved to a linked account shortly before a reroll | Appears in the Prompt 12 anomaly report; no automatic ban; the fresh-nation transfer window blocks the obvious route | REQ-087, REQ-073 | Audit-report test | 07/12 |
| **T03-C13** | Whole-world accounting around a reroll | No stock created; destroyed value is recorded as destroyed; conservation identity holds | REQ-068, REQ-072 | Ledger reconciliation | 04 |

#### D. Security, privacy and recovery

| ID | Setup → action | Expected | Reqs | Verification | Impl. prompt |
|---|---|---|---|---|---|
| **T03-D01** | Public nation page and public API read | No e-mail, account ID, network digest, pair status, case data or session data | REQ-075, REQ-092 | Response inspection | 03/12 |
| **T03-D02** | Direct anon/authenticated query against the private store | Denied by policy for every non-owner role | REQ-092 | Policy test per role | 03/12 |
| **T03-D03** | Client edits a submitted network value or forges a forwarding header | No effect on pair state; the trust boundary decides | REQ-065 | Security test | 03 |
| **T03-D04** | Player asks to clear a restriction | No photograph, government ID, biometric or precise address is requested | REQ-092, REQ-064 | Process and message review | 03/12 |
| **T03-D05** | Client supplies its own starting resources or ownership fields | Server ignores them; standard start and session-derived owner only | REQ-081, REQ-072 | Input test | 03/04 |
| **T03-D06** | Recovery flow, including a changed e-mail | Same account and nation restored; both old and new addresses confirm; all other sessions revoked | REQ-074 | End-to-end test | 03/06 |
| **T03-D07** | Password, e-mail, handle and nation all change | `account_id` unchanged; history intact | REQ-074, REQ-071 | State test | 03/06 |
| **T03-D08** | Account closure completes | Credentials and private data deleted; nation retired; public history and audit spine retained; no e-mail exposed | REQ-075, REQ-088 | Retention test | 03/12 |

#### E. Onboarding, protection and return

| ID | Setup → action | Expected | Reqs | Verification | Impl. prompt |
|---|---|---|---|---|---|
| **T03-E01** | Visitor registers, verifies, names and creates | The documented first-session journey completes without external help | REQ-089 | End-to-end test | 03/13 |
| **T03-E02** | Tutorial skipped midway and resumed later | Progress persists per account; skipped steps are not marked complete | REQ-089 | Session test | 13 |
| **T03-E03** | Tutorial state after a reroll | Account-level steps persist; a short orientation is shown; nothing mandatory replays | REQ-089, REQ-073 | State test | 13 |
| **T03-E04** | First nation then replacement inspected | First nation protected for the documented window; replacement unprotected | REQ-090 | Eligibility test | 03/10 |
| **T03-E05** | Rerolled account's rewards and protection audited over several rerolls | No second protection, no repeatable first-time reward, no accelerated yield | REQ-073, REQ-090 | Ledger and eligibility audit | 03/04 |
| **T03-E06** | Player returns after dormancy, and after archival | Return summary; one-boundary grace; archived nation restorable inside the window; no new account and no forced reroll | REQ-091 | Dormancy test | 02/03 |
| **T03-E07** | Account offline across several boundaries | Turns resolved by the clock; no missed-turn message, no decay, no penalty | REQ-091 | Turn test | 02 |
| **T03-E08** | Restricted pair where one side is inside protection | Protection does not separate the pair; no new protection is created by the restricted relationship | REQ-090, REQ-062 | Matrix + protection test | 03/10 |

### 19.4 Coverage summary

| Group | Tests | Requirement coverage |
|---|---|---|
| A. Ownership and creation | T03-A01…A08 | REQ-061, 070, 072, 074, 076, 077, 081, 083 |
| B. Shared network | T03-B01…B14 | REQ-062, 063, 064, 065, 066, 078, 079, 092, 093 |
| C. Rerolling | T03-C01…C13 | REQ-067, 068, 069, 070, 071, 072, 073, 085, 086, 087, 090 |
| D. Security, privacy, recovery | T03-D01…D08 | REQ-064, 065, 071, 072, 074, 075, 081, 088, 092 |
| E. Onboarding and return | T03-E01…E08 | REQ-062, 073, 089, 090, 091 |
| **Total** | **51 tests** | every REQ-061…REQ-096 has at least one test; REQ-097 is checked by the document validators, not by a game test |

**T03-99 — Invariant coverage is complete.** Each INV-001…INV-032 appears in §15 with a named test, and every named test exists in the tables above. A future invariant must arrive with its test; an invariant without one fails REQ-095.

---

## 20. Decision register — Prompt 03

**D-032 … D-042** were recorded in [DECISIONS.md](../DECISIONS.md) on 2026-10-24 under [the autonomous decision policy](../AUTONOMOUS_DECISION_POLICY.md) (D-014). They are Category B design decisions: they settle the rule and bind later prompts, but they are **not** owner approval of a requirement, and none of them has been implemented or tested.

| ID | Decision | Status | Why | Supersedes or amends | Consequences |
|---|---|---|---|---|---|
| **D-032** | **One account, one active nation, enforced as ownership.** The policy is unchanged from D-018; this entry fixes the model: an immutable account ID owns 0..1 active nations; nation creation takes a per-account lock plus a transaction-safe uniqueness rule; ownership is resolved from the session on every action; the system never claims to prove how many people stand behind an account | Confirmed (design) | D-018 fixed the policy but not the ownership model; concurrent creation and re-parenting were unspecified; REQ-002/REQ-061 needed a rule | Extends D-018; applies REQ-043 | Implementation in Stage 5/6; tests T03-A02/A03/A05/A08; no perfect-enforcement claim may be published |
| **D-033** | **Shared-network clearance uses attestation plus behavioural review, not identity documents.** No photograph, government ID, biometric or precise address is required to play or to clear a restriction. Each account confirms control in its own session and consents to a review of its interaction history. Decisions are `SEPARATE_PEOPLE`, `FALSE_POSITIVE`, `INCONCLUSIVE`, `LIKELY_DUPLICATE`, `REFERRED_TO_ENFORCEMENT` or `ACCOUNT_CLOSED` | Confirmed (design); mechanism Deferred to Prompt 12 | Politics & War's official process collects a photograph and a signed statement; copying it would import a disproportionate sensitive-data practice into a browser game with minors in its audience | Rejects the P&W pattern (C-5); applies ACC-007 | Prompt 12 writes the review procedure and evidence handling; legal review remains UD-017; tests T03-B08/B09/D04 |
| **D-034** | **The interaction matrix is the policy.** Five relationship states (`NONE`, `OBSERVED`, `RESTRICTED`, `CLEARED`, `MAINTAINED`) plus a separate review status. A pair is observed when both accounts appear on the same normalised network key within 24 hours; a restricted verb moves it to `RESTRICTED`; an observation lapses after 180 days; a restriction never lapses while in force. A network seen for more than 25 accounts in 24 hours is `LARGE` and uses the slower trigger with no blanket restriction | Confirmed (design); thresholds Provisional | The brief requires a state model and a complete matrix; without explicit triggers the restriction would either never apply or apply indiscriminately | Defines NET-014…NET-024; relates to D-027 (aggregates) and D-028 (dormancy) | Prompt 07/09/10/12 must map their verbs to the matrix; Prompt 14 validates the numbers |
| **D-035** | **Indirect routes are covered, and a pair may not use an alliance bank.** Blocked directly means blocked through an alliance, a third nation, a market match, a gift chain, a loan or a timed sequence; where the system cannot see both legs, the act is a violation supported by the audit record. While restricted, neither account may deposit to, withdraw from or transfer through an alliance bank; membership is not revoked | Confirmed (design) | A pairwise check alone is trivially bypassed; bank pools are not pairwise attributable once value enters them, so the safe rule is over-inclusion for the pool only | Extends D-018; implements REQ-063/REQ-078 | Prompt 09 implements the bank rule and notifies alliance leadership; Prompt 12 owns transfer-graph review; no perfect-detection claim |
| **D-036** | **Trusted network signal on Cloudflare Pages + Supabase.** A Pages Function reads Cloudflare's `CF-Connecting-IP` from the incoming request, discards private/loopback/proxy/unparseable values, normalises to the address (IPv4) or /64 (IPv6), computes `HMAC-SHA-256(prefix, pepper)` with a Worker-held secret, and writes only the digest plus timestamp through a server-only Supabase function. The application stores no raw IP. The pepper never enters the repository, the database or the browser. The authoritative pair check runs in the same transaction as the action | Confirmed (design); enforcement Deferred to Stage 5/6 | The brief requires an authoritative server-side mechanism; a client-supplied or proxy-appended value is forgeable. Cloudflare documents `CF-Connecting-IP` as the client address header and warns that subrequests can alter it | Implements REQ-065; refines Report 08 §11.2 (raw-IP retention replaced by digest) | Stage 5/6 implement and test T03-B03/B14/D03; pepper rotation needs a documented plan; no raw IP may appear in logs, exports or evidence bundles |
| **D-037** | **No standing co-resident exemption.** Co-residence is not a permission. Two accounts on one network are cleared only through the review in D-033, and a claim of co-residence is evidence to be weighed, not a switch that unlocks transfers. There is no "family mode", shared-household allowance or auto-clear by repeated login. Accounts that keep sharing a network after clearance stay under the 90-day watch | Confirmed (design) | Any self-certified exemption is the obvious bypass of the whole mechanism; the brief requires a review route, not an exemption route | Applies ACC-005; closes the loophole a literal reading of "households are allowed" would create | Messages must say co-residence is allowed but does not itself permit interaction; Prompt 12 handles repeated claims; UD-031 covers reroll frequency, not this |
| **D-038** | **Nation identity and naming.** Display name 3–32 characters after NFC normalisation, allowed Unicode letters, marks, digits, space, hyphen, apostrophe and full stop, at least one letter, no leading/trailing separator; short name 2–6 characters `A–Z0–9`; uniqueness under case and diacritic folding; a private reserved list; a 30-day hold on a released name; display-name change once per 7 days and short-name change once per 30 days, free at first playable; `nation_id` and public nation number are the identity and never change. No geography is ever requested | Confirmed (design); cooldowns Provisional | The brief requires a coherent rule set; the project needs uniqueness without a name-claim economy or an impersonation channel, and no map placement | Defines NAT-026…NAT-042; applies REQ-082/REQ-083/REQ-084 | Prompt 13 renders validation messages; Prompt 12 owns name enforcement; Prompt 14 may tune cooldowns only with a recorded reason |
| **D-039** | **Instant reroll with a total reset.** A reroll retires the current nation permanently and allows a replacement on the same account with **no gameplay cooldown**. Confirmation requires fresh authentication plus the exact nation name. Everything nation-specific is destroyed; nothing is converted, refunded, stored or transferred. Account identity, sanctions, pair restrictions, cases and evidence survive. A reroll is blocked by an active campaign, an unsettled accepted settlement, a preservation order or a disqualifying account state. Abuse controls are the fresh-nation transfer rule, the fair-value band, audit-anomaly reporting and a review flag at three completed rerolls in 30 days — never a hidden timer | Confirmed (design); thresholds Provisional | The brief makes instant rerolling mandatory and forbids using a cooldown to control abuse; deleting a nation must not become an amnesty or a war escape | Implements REQ-067…REQ-070, REQ-085…REQ-087; applies D-021 | Prompt 07 owns the transfer window and fair-value numbers; Prompt 10 may replace the campaign block with a forfeit rule (UD-032); Prompt 12 owns anomaly review |
| **D-040** | **Onboarding, protection and return.** Onboarding follows the ten-step first-session journey; tutorial progress belongs to the account and survives a reroll. Newcomer protection is **account-scoped and consumed by the first nation only**, lasts 7 days/84 turns or until the nation attacks, is visibility-only (no yield, resource or score bonus), and is skipped between a restricted pair so it cannot be used as a shield. A replacement nation is never protected. Dormancy and archival follow D-028; return needs no new account and no forced reroll | Confirmed (design); 7-day window Provisional | D-021 forbids catch-up acceleration; the brief forbids a repeatable protection benefit. Protection must be a hostile-action rule, not a growth multiplier | Applies D-021 and D-028; implements REQ-089…REQ-091 | Prompt 10 owns protection states in war; Prompt 13 owns presentation; Prompt 14 validates the window |
| **D-041** | **Account lifecycle and recovery.** Ten explicit account states with documented transitions; verified e-mail required before nation creation (D-029); ten single-use recovery codes stored hashed; e-mail change requires confirmation from both old and new addresses; recovery restores the existing account and never creates an account or nation; account closure is a 7-day cancellable request that deletes credentials and private data, retires the nation without replacement and keeps required history; unverified inactive accounts are cleaned after 30 days | Confirmed (design); session lifetimes and the 30-day cleanup Provisional | The brief requires a full lifecycle and a recovery path that cannot become a second-account route; the states had to be explicit to prevent "restricted" being confused with "suspended" | Implements REQ-074/REQ-075/REQ-088; applies D-029 | Stage 6 configures Supabase Auth and tests T03-D06; Prompt 12 owns contested-ownership cases; legal retention remains UD-017 |
| **D-042** | **Data classes, retention and administrative limits.** Eighteen data categories with a class (Public/Private/Restricted/Secret), purpose, access and retention. No raw IP, no special-category identity data, no analytics or advertising. Network digests 180 days; pair records active + 12 months; attestations case + 12 months; account data until closure; public nation history and the audit spine permanent; class-S detail per D-026. Administrative access is least-privilege and logged; no administrator may silently rewrite public history; no enforcement action exists without a reason and an appeal route | Confirmed (design); retention values align with D-026 and are Provisional where marked | The brief requires a data-classification table and a minimum administration policy; the categories must match the mechanism actually designed, not a generic inventory | Applies D-025/D-026/D-027; implements REQ-092/REQ-093 | Prompt 12 publishes the player-facing notice and implements the roles; UD-017 remains the legal question; no compliance claim is made |

**Numbering note.** **D-031** is also recorded by this prompt in [DECISIONS.md](../DECISIONS.md): it fixes the separation of account status, nation status and pair status (§4.2, §5.4, §10.1). It is kept out of the table above only because that table summarises the eleven decisions the rulebook text most often cites. The unresolved register's **UD-031…UD-033** are questions, not decisions. The next free decision ID is **D-043**. No existing entry was edited: D-031 and D-033/D-037 are new entries, and no earlier decision is superseded by Prompt 03 except where a row above says so.

---

## 21. Research log and provisional decisions

### 21.1 What was read, when, and how far it can be trusted

| Read on | Source | Official? | What it can support | What it cannot support |
|---|---|---|---|---|
| 2026-10-24 | P&W Game Rules (`politicsandwar.com/rules/`) | Yes | The one-account rule, shared-network restrictions, the reroll/restart framing, the moderation ladder's existence | Nation Supremacy's rules, values or enforcement quality |
| 2026-10-24 | P&W Privacy Policy (`politicsandwar.com/privacy/`) | Yes | That verification is optional, photograph-based, stored offline and not public | That Nation Supremacy may collect the same data; that the practice is lawful in our jurisdiction |
| 2026-10-24 | P&W Account Verification page (`politicsandwar.com/account/verification/`) | Yes | The renewal cadence (30 days / 6 months / 1 year) and that verification is aimed at shared networks | That the process is proportionate for us; that it is currently enforced as described |
| 2026-10-24 | P&W-pedia Terminology Glossary | Official domain, community-maintained | That "reroll" is a recognised player term for delete-and-recreate | Any rule detail |
| 2026-10-24 | P&W community FAQ (Fandom, via MediaWiki API) | No | Community understanding of shared-network limits, price bands and inactivity | Current official policy; exact mechanics |
| 2026-10-24 | Two P&W forum topics | No | That players discuss shared households and restarting | Reply content (bodies not rendered); current staff policy |
| 2026-10-24 | Search snippets on deletion preconditions | No | Leads only | Anything verifiable; not used for a rule |
| 2026-10-24 | Cloudflare HTTP-headers reference and Pages Functions documentation | Yes | `CF-Connecting-IP` is the client-address header; subrequests can alter forwarding headers; a Pages Function can run server-side code on the game's origin | That our Function is correctly configured; that no proxy sits in front of it |
| 2026-10-24 | Supabase Auth, API-security, RLS and e-mail-change documentation | Yes | `service_role` bypasses RLS and must stay server-side; RLS is the access-control layer; secure e-mail change confirms both addresses; password reset does not reveal account existence | Our policy correctness; our configuration |

**Confidence summary.** High for the official P&W rules, privacy policy and verification page as read on 2026-10-24. Medium for the wiki glossary and the community FAQ, which may lag the live game. Low for forum bodies and search snippets; no rule here depends on them. High for the Cloudflare and Supabase statements quoted, because they are current official documentation — but **no configuration was tested**, so the trust-boundary claims are design intentions until Stage 6 exercises them.

**What this research did not establish.** That P&W's current live behaviour matches its published pages; that its verification process is enforced consistently; that its shared-network restrictions cover the same verbs we cover; that our thresholds are fair; that our review capacity exists; that any jurisdiction permits our retention. Those remain open or assigned.

### 21.2 Provisional parameters and their owners

**PRO-01 — No numeric value in this document is approved.** Each is an anti-abuse parameter chosen to be defensible, not measured. A later prompt may change one only by editing this document or its own, and Prompt 14 must label and test it.

| Parameter | Provisional value | Purpose | Numeric owner / validator | Evidence needed |
|---|---|---|---|---|
| Network observation window `W_obs` | 24 hours | Pair matching | Prompt 12; Prompt 14 | Observed household/campus patterns in playtest |
| Observation life `R_obs` | 180 days | Stop matching stale pairs | Prompt 12 | Data-volume and false-positive review |
| Large-network threshold `L_large` | >25 accounts / 24h | Avoid campus-wide restrictions | Prompt 12 | Distribution of accounts per network |
| Restricted-attempt escalation | Second observation ≥6h apart within 7 days | Reduce accidental blocks | Prompt 12 | Review-queue data |
| Review service target | 7 days (not a guarantee) | Set expectations honestly | Prompt 12 | Actual review throughput |
| Clearance watch | 90 days | Catch immediate re-offence | Prompt 12 | Case outcomes |
| Re-review interval after `MAINTAINED` | 30 days | Allow changed circumstances | Prompt 12 | Case outcomes |
| Network digest retention | 180 days after last seen | Minimisation | Prompt 12 | Data-volume measurement |
| Pair-record retention | Active + 12 months | Enforcement continuity | Prompt 12 | Legal review (UD-017) |
| Newcomer protection `P_prot` | 7 days / 84 turns | Hostile-action shield only | Prompt 10; Prompt 14 | New-player experience evidence |
| Fresh-nation transfer window | 30 days / 360 turns | Stop starter-bundle farming | Prompt 07; Prompt 14 | Legitimate-newcomer trade data |
| Fair-value band | Unspecified here | Allow reciprocal trade, block one-sided extraction | Prompt 07 | Market data |
| Display-name change cooldown | 7 days | Reduce impersonation churn | Prompt 13; Prompt 14 | Abuse reports |
| Short-name change cooldown | 30 days | Protect compact identity | Prompt 13; Prompt 14 | Abuse reports |
| Released-name hold | 30 days | Reduce exact-name impersonation | Prompt 12 | Abuse reports |
| Reroll review flag | 3 completed rerolls / 30 days | Review signal, never a ban | Prompt 12 | Reroll distribution |
| Reroll request rate limit | 1 per 60 seconds | Double-submit protection | Stage 6 | Technical only; not gameplay |
| Account closure cooling | 7 days | Prevent impulsive loss, allow cancellation | Prompt 12 | Support load |
| Unverified-account cleanup | 30 days | Free-tier hygiene | Stage 6 | Signup data |
| Session absolute lifetime | 30 days | Security posture | Stage 6 | Supabase configuration |

### 21.3 Unresolved-question dispositions

| UD | Question | Disposition | Owner | Why not resolved here |
|---|---|---|---|---|
| **UD-031** | Is a reroll-frequency threshold a legitimate review signal, and at what value? | **Deferred** | Prompt 12 (procedure), Prompt 14 (value) | The signal is adopted (D-039) but the fair value needs real reroll distribution; setting it now would be a guess with a ban-adjacent consequence |
| **UD-032** | What happens to an active campaign when a participant rerolls? | **Deferred** | Prompt 10 | Requires the campaign lifecycle and forfeit rules; Prompt 03 fails closed (block) rather than inventing a forfeit |
| **UD-033** | Is in-game diplomatic/treaty reputation account-scoped or nation-scoped after a reroll? | **Deferred** | Prompt 08 | Requires the reputation model; Prompt 03 fixes only that *enforcement* sanctions survive and that old acts stay attributable |
| **UD-017** | Jurisdiction, lawful basis, age gate, retention limits | **Open (owner/legal)** | Owner, prepared by Prompt 12 | Not a design choice; no compliance claim is made |

**Existing rows applied, not reopened:** UD-014 (multi-account policy) → D-018; UD-015 (e-mail verification) → D-029; UD-020 (catch-up) → D-021; UD-025 (dormancy) → D-028; UD-004 (retention volume) → D-026. Prompt 03 **applies** these and does not re-decide them.

---

## 22. Completion and acceptance criteria

### 22.1 Acceptance checklist

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Existing project records and policy decisions read before writing | **Met** | §2.1; conflicts C-1…C-10 |
| 2 | P&W references researched, source types distinguished | **Met** | §3, §21.1 |
| 3 | One-account-per-person explicit | **Met** | ACC-001…ACC-011 |
| 4 | At most one active nation per account | **Met** | ACC-014; NAT-006; D-032 |
| 5 | Shared-IP restrictions fully defined | **Met** | §5; NET-001…NET-061 |
| 6 | Indirect bypasses addressed | **Met** | NET-025/NET-026; D-035 |
| 7 | Legitimate players have a review route | **Met** | NET-030…NET-037; D-033 |
| 8 | Shared IP is not conclusive for a permanent ban | **Met** | NET-039; REQ-066 |
| 9 | Verification and privacy proportionate | **Met** | ACC-007; D-033; §14.3 |
| 10 | Reroll on the existing account | **Met** | RRL-001…RRL-003 |
| 11 | No cooldown before replacement | **Met** | RRL-004; T03-C05 |
| 12 | Reroll removes all old-nation progression and assets | **Met** | RRL-013/RRL-014; T03-C03 |
| 13 | Reroll preserves the account but not its sanctions | **Met** | RRL-016/RRL-017 |
| 14 | Reroll cannot erase war consequences or required history | **Met** | RRL-021/RRL-025; NAT-040 |
| 15 | Protection compatible with D-021 | **Met** | ONB-019…ONB-035 |
| 16 | Lifecycle and creation flows complete | **Met** | §6, §10; J-01…J-04 |
| 17 | Security, privacy, moderation and appeal rules defined | **Met** | §5.7–§5.10, §14.2 |
| 18 | Cross-system contracts documented | **Met** | §18 |
| 19 | Requirements, decisions, tests and handoff updated | **Met in this pass** | §19, §20; register updates listed in §22.3 |
| 20 | Validators pass, or limitations recorded honestly | **See §22.4** | Validator output; no runtime test |
| 21 | No code, database, auth, deployment or infrastructure change | **Met** | §22.5 |
| 22 | Prompt 04 identified as next | **Met** | §22.6 |

### 22.2 What is deliberately incomplete

- Every numeric parameter in §21.2 is provisional and unvalidated.
- The review workflow, tooling, staffing and case management are Prompt 12's.
- The economy's starting-grant size, material stock, upkeep and deficit rule are Prompt 04's.
- The fair-value band and transfer-window mechanics are Prompt 07's.
- The campaign forfeit rule (UD-032) and protection states in war are Prompt 10's.
- Diplomatic reputation scope after a reroll (UD-033) is Prompt 08's.
- Supabase Auth configuration, SMTP vendor and session values are Stage 6.
- The database schema, constraints, RLS policies and functions are Stage 5.
- Legal review, age gate and jurisdiction are owner/legal (UD-017).
- **No rule in this document has been implemented or tested.**

### 22.3 Records updated by this prompt

| File | Change |
|---|---|
| [09_account_onboarding_nation_creation_and_progression.md](09_account_onboarding_nation_creation_and_progression.md) | This document: the authoritative B-03 rulebook |
| [02_master_game_design_bible_outline.md](02_master_game_design_bible_outline.md) | B-03 marked written, with the real path and scope |
| [01_stage_2_prompt_roadmap.md](01_stage_2_prompt_roadmap.md) | A **B-03 carry-in** line added to Prompts 04–15, so every later prompt inherits the reroll and shared-network contracts and knows which detail it owns |
| [03_requirements_traceability.md](03_requirements_traceability.md) | REQ-061…REQ-097 added; the Prompt 03 rows updated |
| [04_approved_and_provisional_decisions.md](04_approved_and_provisional_decisions.md) | DD rows DD-049…DD-060 for D-031…D-042 |
| [05_unresolved_design_decisions.md](05_unresolved_design_decisions.md) | UD-031…UD-033 added as deferred rows |
| [06_stage_2_progress_log.md](06_stage_2_progress_log.md) | Prompt 03 checkpoint and validation record |
| [00_stage_2_handoff.md](00_stage_2_handoff.md) | Next prompt repointed to 04; B-03 added to the state table |
| [DECISIONS.md](../DECISIONS.md) | D-031…D-042 |
| [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) | Status, decision range, prompts complete, next prompt |
| `docs/qa_backups/test_decision_registers.py`, `test_next_action.py` | State expectations advanced to Prompt 04 without weakening any check |

### 22.4 Validation

**What was run on 2026-10-24** (all four document checks in `docs/qa_backups/`, from `docs/`):

| Check | Result |
|---|---|
| `python qa_backups/validate_final.py` | **PASS** — `VALIDATION: ALL CHECKS PASSED`; the B-03 section, the REQ-061…REQ-097 rows and the decision ranges reconcile |
| `python qa_backups/09_validate.py` | **PASS** — 338/338 checks |
| `python qa_backups/test_next_action.py` | **PASS** — 15 tests, OK; no stale next-action statement, and the outline, progress table, historical handoff and market summary agree with the current records |
| `python qa_backups/test_decision_registers.py` | **PASS** — 12 tests, OK; the registers, counts and non-resolved inventory agree |

These inspect documents only.

**What they cannot prove.** No application code exists, so nothing here validates behaviour, concurrency, database constraints, IP handling, authentication or retention jobs. A passing validator means the documents agree with each other and with their registers; it does not mean any rule works. The 51 `T03-` tests and all 32 invariants remain **specifications** until Stages 5–8 implement and run them.

### 22.5 Scope confirmation

No application code, database migration, Supabase setting, authentication configuration, credential, deployment, hosting resource or production data was created or changed by this prompt. The two prototypes under `prototypes/` were not touched. The only files written are documentation and the document-QA tests/validators.

### 22.6 Next action

**Stage 2, Prompt 04 — Economy, Resources, Treasury and Finances.** It owns the starting-grant size, material stocks, income/upkeep ordering (D-019), the deficit rule and the fair-value numbers this document leaves open. Prompt 03 is complete as a specification; Prompt 04 is not started here.
