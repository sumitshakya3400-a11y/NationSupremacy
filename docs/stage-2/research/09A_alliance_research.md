# 09A — Alliance System Research, Politics & War Analysis and Requirements Baseline

**Document ID:** 09A-ALLIANCE-RESEARCH
**Stage:** Stage 2, Prompt 09A (research and requirements baseline only)
**Version:** 1.4 — corrected through Prompt 09A-F (2026-10-31)
**Created:** 2026-10-31
**Status:** Research complete for 09A purposes and accepted after Prompt 09A-F; **no rule in this document is approved gameplay**, and no Alliance feature is implemented. The correction passes added the complete 15-permission Politics & War inventory, corrected the Black Knights recruitment example, replaced the two forum-root citations, re-audited every AX reference (§23), completed the AX-08 treasury storage traceability correction (§24), completed the final AX-08 wording, deposit policy, handoff and validator reconciliations (§25), and completed final project status reconciliation and acceptance closure (§26).
**Canonical successors:** Prompt 09B (`docs/stage-2/16_alliances.md`, B-09) and Prompt 09C (alliance workflows and acceptance). **Current-design cross-reference (2026-11-01):** this report's no-object recommendation is preserved as historical evidence. `D-137` adopted the no-object path for B-08; `D-140` later authorized a **separate** B-09 Alliance-to-Alliance treaty object (`AT-T01`–`AT-T05`) with explicit per-nation consent and zero diplomatic delegation. The recommendation below is not current scope.
**Companions:** `09A_alliance_sources_findings.md` (source and finding registers), `09A_alliance_integration_matrix.md` (Prompts 01–08C matrix).

---

## 1. Purpose and scope

This document establishes the evidence base, candidate requirements and system boundaries for the Alliance System. It does **not** write the B-09 rulebook (09B) and does **not** write player workflows or acceptance scenarios (09C).

In scope:

- Politics & War (P&W) alliance mechanics, permissions, economy, diplomacy, military coordination and Discord practice.
- Comparative evidence from eRepublik, Stellaris, EVE Online and Call of War.
- Integration analysis against Stage 2 Prompts 01–08C and their canonical documents.
- A candidate requirement baseline (`REQ-534`–`REQ-617`) and owner-decision backlog (`UD-040`–`UD-049`).
- Risk register, cost classification and 09B handoff.

Out of scope and explicitly not performed: code, schema, APIs, events, scheduled jobs, front-end screens, Discord bots/API/OAuth/role sync, real-time chat of any kind, and any change to the canonical rules of Diplomacy, Market, Economy, Military or Global Trade.

---

## 2. Method and evidence rules

1. **Read the project first.** Canonical Stage 2 documents for Prompts 01–08C were read before requirements were drafted (see §3 and the integration matrix).
2. **Multiple source classes.** P&W evidence was collected from official game documentation, official rules, live alliance pages, alliance-owned recruitment sites, third-party alliance tooling and community forums. Each is classified `PRIMARY/OFFICIAL`, `COMMUNITY DOCUMENTATION`, `LIVE COMMUNITY PRACTICE`, `THIRD-PARTY TOOLING` or `ANECDOTAL` in the source register.
3. **More than one alliance.** Live evidence covers Rose, GLOB, Weebunism, Ragnarok, United Ummah and Black Knights. No single alliance is treated as universal.
4. **Native vs. community vs. tool.** Every P&W observation is labelled with what actually provides it. A Discord bot is never described as a P&W feature.
5. **No invented numbers.** No tax rate, withdrawal cap, fee, member cap, cost or timeline is invented. Financial figures are absent by design; costs are classified qualitatively in §14.
6. **Findings are not decisions.** A finding (`ALR-###`) can support a candidate requirement (`REQ-###`) but cannot approve it. Owner decisions are `D-###`/`DD-###`; open questions are `UD-###`.

**Access limitation (updated 2026-10-31 by 09A-C).** The Fandom `Alliance_Permissions` page is now directly retrievable (HTTP 200) and was re-read for Correction B; it remains `COMMUNITY DOCUMENTATION`, not an official matrix. `stellaris.paradoxwikis.com` still returns HTTP 427, so its evidence remains indirect. The P&W in-game join flow was not executed; the applicant state is evidenced by native applicant lists and by the Black Knights page's instruction to use the official join screen. No Discord server was joined, scraped or monitored.

---

## 3. Project baseline inspected

| Prompt | Canonical material read | What the Alliance System must respect |
|---|---|---|
| 01 | Stage 2 roadmap and scope documents | Stage ownership; no implementation before specification acceptance. |
| 02 | Foundations, turn/order and visibility rules | Single authoritative state; deterministic ordering; visibility classes `public`/`alliance`/`private`/`restricted` (REQ-057). |
| 03 | Nation, player identity, dormancy | One nation per player; player is the only authority over their nation; dormancy 14 days/168 turns (D-028). |
| 04 | Economy, resources, ledger | Economy owns resource creation, storage, transfer and ledger rules; no minting (ECN-213, DD-067). |
| 05 | Cities, development, research | Development costs and caps are owned outside Alliance; support programmes may only move already-owned value. |
| 06 | Population, approval, elections, crisis | Nation-level politics is owned by B-06; alliance governance must not overwrite elections or crisis states. |
| 07A/07B/07C | Market research, market rules, Global Trade gates | D-122, DD-136, REQ-513, G-1…G-6. Approved Global Trade scope remains release-gated; Alliance must not bypass it. |
| 08A | Diplomacy research and interface matrix | Diplomacy owns relationship states, proposals, consent, treaties, embargoes, war-risk formulas. |
| 08B | `15_diplomacy.md` incl. §18 DIP-146…149 | Bilateral consent is mandatory; alliance is never a party or guarantor of a nation treaty; nation treaties persist through alliance changes; no delegation granted by B-08. |
| 08C, 08C-C/D/E | `15_diplomacy_workflows_acceptance.md` | 30 workflows, 54 edge cases, acceptance matrix and traceability are closed. Alliance must integrate through the declared interface, not reopen it. |
| 09 pre-work | `01_stage_2_prompt_roadmap.md`, B-09 outline, UD-039 | B-09 is `16_alliances.md`; 09 splits into 09A/09B/09C; UD-039 is owned by Prompt 09. |

**Consequence.** Several attractive P&W features (alliance tax brackets, alliance bank, alliance-wide treaties, alliance war declarations) touch systems whose ownership and approval status are already fixed. They are recorded as **candidate** requirements with explicit owner decisions, never as assumed rules.

---

## 4. Executive summary

1. P&W's native alliance layer is deliberately thin: identity, a bank, tax brackets, ranks/permissions and a membership list. Almost all governance, recruitment process, departmental work and day-to-day coordination live in **Discord and third-party sites**, not in the game.
2. Native permissions are **discrete but bundled**: the community wiki lists **15** permissions (view/withdraw bank, change permissions, see spies, see reset timers, tax brackets, post/manage announcements, manage applicants, remove members, edit alliance info, manage treaties, manage market share, manage embargoes, promote self to leader), and the default Leader/Heir/Officer positions bundle broad subsets of them. Custom positions can carry any subset, including `Promote Self to Leader`. The primitives are per-action; the default roles are not least-privilege.
3. P&W alliance economy is a **shared bank plus percentage tax brackets** with a `Bank Access` gate. Official documentation confirms monetary and resource percentages, a default bracket, bulk city-count moves, and that gray nations are not taxed. Official rules prohibit using alliance banks to evade same-network trade restrictions and prohibit bank protection via vacation mode or new nations.
4. P&W diplomacy at alliance level is **not a first-class treaty object**. Alliances publish treaty lists (MDoAP, ODoAP, NAP, ODP, protectorate, extension) on their pages, but the enforceable diplomatic machinery in the evidence is nation-to-nation and community-enforced. This matters directly for UD-039.
5. P&W military coordination is organisational, not automatic: departments, war rooms, readiness tracking and Discord pings. No evidence supports an alliance officer gaining execution authority over a member's military.
6. Recruitment is a **hybrid of native applicant state and external Discord** for the alliances inspected. Rose states Discord is mandatory and runs a timed interview. Black Knights' current live protocol is three verified stages: become an Applicant through the in-game join screen, join the alliance Discord (stated as a joining requirement), then run `/apply nationid:<id>` so an alliance-operated bot opens an interview workflow. This is `LIVE COMMUNITY PRACTICE` plus `THIRD-PARTY TOOLING`, not a game rule.
7. The transferable pattern for Nation Supremacy is **authoritative in-game records + external conversation**, not "build Discord into the game". That is exactly the owner's constraint.
8. The cheapest credible native feature set is: alliance profile, membership lifecycle, rank/permission model, asynchronous announcements, treasury with double-entry history and approvals, formal proposals/votes, and a validated static Discord invite link. None requires a socket, a bot, a queue or message storage.
9. Diplomacy integration is the hardest boundary. B-08 grants no delegation; nation treaties persist through alliance changes; an alliance cannot be a party or guarantor. 09A therefore recommends **no alliance-level treaty object in the initial release**, with alliance diplomacy expressed as non-binding public positions plus member-nation consent. This no-object path is **outside UD-039's recorded a/b/c options** (all of which create an alliance-level treaty route); it is a recommendation for the owner, not a resolution.
10. Economy integration must be additive: the alliance treasury is a segregated, audited pool of already-owned resources, never a mint, never a way around same-network/trade rules, and never a substitute for member consent.
11. Comparative evidence (eRepublik, Stellaris, EVE, Call of War) consistently shows that **leadership succession and membership-change handling** are the two features that generate the most disputes; both need explicit rules earlier than treasury features.
12. Cost risk is concentrated in governance edge cases and audit history, not in storage. The design must cap history retention and notification fan-out deliberately, and must not acquire any recurring real-time messaging dependency.

---

## 5. Politics & War — alliance foundation and identity

**Official position.** P&W alliance pages expose name, ID, flag, description, member count, rank, founding date, external links (including Discord), recruitment status, applicant list, departments, treatises and a bank. The alliance directory lists alliances with member counts and ranks. Creating an alliance is an in-game action by a nation that pays the creation cost and becomes Leader; the join page itself was not retrievable (404), so the exact current form and cost are **not asserted** here (`ALS-014`, limitation).

**What is verifiable and relevant:**

- Identity is public by default: name, flag, description, member count, rank, founding date, recruitment status and external link are visible on the public page (Rose, `ALS-006`).
- Entry requirements are declared by the alliance, not enforced by the game. Rose publishes "Accepting Members: Yes", an applicant list, and a Discord-mandatory interview process.
- External links are alliance-maintained free text/URLs. The game does not validate or host the destination.
- Alliances can be searched and browsed; discoverability is a directory function, not a recruitment system.

**Implication for Nation Supremacy.** Founding should be an explicit, auditable action by an eligible nation owner, with a unique name and a public profile whose fields are individually classified public/member-only. The game should not model "recruitment" as a chat funnel; it should model an application object whose status is authoritative.

Candidates: `REQ-534`–`REQ-541`.

---

## 6. Politics & War — membership and recruitment

**Native mechanics.** Membership is join/leave plus accept/remove by someone holding Manage Applicants or Remove Members. Applicant lists are visible on alliance pages; an Applicant does not count toward alliance statistics and has no powers. There is no native interview, application essay, onboarding checklist or trial period. The native object is the applicant/membership status, not a recruitment workflow.

**Live practice.** Across the alliances inspected, recruitment is a hybrid: the applicant state starts in-game and the conversation continues externally.

- Rose: application is Discord-first; an interview is scheduled, expected to last about 30 minutes and to be completed within 24 hours; the applicant list is public; raiding applicants is prohibited by alliance policy (`ALS-006`).
- GLOB, Weebunism, Ragnarok, United Ummah: public pages advertise a Discord server and an `#apply`-style route; several state or imply that Discord is required (`ALS-007`–`ALS-010`, search-indexed).
- Black Knights: the live protocol and the alliance-owned application page give a specific three-stage process, documented below (`ALS-011`, `ALS-026`).
- AEGIS (third-party) adds a recruitment pipeline with applicant isolation, verification and role assignment (`ALS-012`). It exists precisely because the native game does not provide this.

### 6.1 Black Knights — verified current process

The earlier 09A text called `bkpw.net/apply` a shell page. That was inaccurate: the page is client-rendered, so a plain HTML fetch returns only the generic CMS placeholder used for the *requirements* panel, while the rendered page and the live alliance page both publish a real application flow. The corrected evidence, read and rendered on **2026-10-31**, is:

| Stage | What the source actually says | Who provides it |
|---|---|---|
| 1. In-game application | Become an Applicant through the official alliance join screen. The nation must appear in Black Knights with the Applicant position before the bot will accept it (`ALS-011`). The live alliance page gives the same first step (`ALS-026`). | Politics & War (native applicant state) |
| 2. Join the alliance Discord | Use the Discord account recruitment staff should recognise; that Discord identity owns the application and its status. The live page states: “Most alliance communication happens on Discord, and it is a requirement for joining the Black Knights” (`ALS-011`, `ALS-026`). | Black Knights (alliance policy); Discord (external venue) |
| 3. Run the application command | In Discord, run `/apply nationid:<your nation ID>`. If the nation is not eligible, the bot explains what must change without submitting. The page then says the bot creates “the configured interview workflow for recruitment staff”; progress is checked with `/applications status` (`ALS-011`). | Third-party application bot operated for Black Knights (the page is “Powered by Nexus AMS”) |
| 4. Interview and decision | An interview workflow exists in Discord. The public page does **not** publish the questions, minimum requirements, acceptance threshold or review duration; its “Requirements and policies” panel is unpublished placeholder text (`ALS-011`, `ALR-049`). | Black Knights recruitment staff (external) |
| 5. Acceptance and onboarding | Acceptance is an in-game membership decision; the Discord bot records the application, but the authoritative membership state is the P&W alliance membership. The page does not document an onboarding checklist (`ALS-011`, `ALS-026`). | Politics & War (membership state); Black Knights (onboarding practice, not published) |

**What must not be claimed.** Black Knights does not publish a minimum city count, nation age, activity rule or review time. The earlier report's timed 24-hour process belongs to Rose, not Black Knights, and is not transferred. The `/apply` command is not a P&W feature; it is a third-party bot. The interview is not a native P&W mechanic.

### 6.2 Native vs. alliance-specific vs. third-party

| Element | Politics & War native feature | Black Knights-specific practice | Third-party tooling |
|---|---|---|---|
| Applicant status | **Yes** — join screen, Applicant position, applicant list | Uses it as step 1 | — |
| Accept/reject | **Yes** — Manage Applicants permission | Decides who to accept | — |
| Interview | No | Yes — recruitment workflow | The workflow is created by the bot |
| Discord requirement | No | **Yes** — stated requirement for joining BK | Discord is the venue |
| `/apply` slash command | No | Configured for BK | **Yes** — BK Net / Nexus AMS application bot |
| Membership record | **Yes** — authoritative in-game membership | — | The bot mirrors status but is not authoritative |
| Minimum requirements / review time | No native equivalent | **Not published** — placeholder panel | — |

**Implication for Nation Supremacy.** Native application status is authoritative. An alliance may optionally publish a Discord invite and may conduct recruitment discussion externally. Acceptance, rejection, withdrawal and official membership remain in Nation Supremacy. A Discord message, interview or bot status does not change membership. Players are never required to have a Discord account to use the game normally.

Candidates: `REQ-562`–`REQ-570`; `REQ-617` preserves the no-Discord-required path.

---

## 7. Politics & War — leadership, departments and permissions

### 7.1 Positions and default bundles

Official PWPedia (`ALS-001`) describes Leader/second-in-command, High Government (department heads), Low Government (officers) and, in some alliances, Mid Government. Appointment and naming vary by alliance; the game does not impose a constitutional model. Live BK uses Emperor, Viceroy and Archdukes (`ALS-026`); Rose uses a command tier, deputies, department heads, a Speaker and a council (`ALS-006`).

The current community wiki (`ALS-013`, accessed **2026-10-31**) documents five default position states:

| Position | Level | Documented powers | Important limitation |
|---|---|---|---|
| Leader | 9 | Unrestricted; appoint officers, heirs and additional leaders; approve applicants; remove members; edit alliance information | No native dual control or removal procedure is documented |
| Heir | 8 | “All the same powers as leaders”; can appoint themselves Leader when the alliance has no leader | The source calls the position “mostly for aesthetic purposes” outside that vacancy case |
| Officer | 5 | View Bank; Change Permissions; Post Announcements; Manage Announcements; Edit Alliance Info; Manage Treaties; Manage Applicants; Remove Members | Cannot appoint officers, heirs or leaders; the bundle still combines membership, treaty, profile and permission control |
| Member | 3 | No powers; contributes to alliance statistics | — |
| Applicant | — | No powers; does not contribute to statistics; shown as pending | — |

### 7.2 Complete permission inventory

The wiki states: “Alliance positions currently have **15 possible permissions**.” The table reproduces every one, with the source's exact scope. The “default holder” column distinguishes what the source actually assigns from what it does not state.

| # | Permission | Exact documented description | What it allows | Default holder (as documented) |
|---|---|---|---|---|
| 1 | View Bank | “nations with this permission can view the contents of the alliance's bank” | Read the pool's money and resource contents | Leader and Heir unrestricted; Officer explicitly has it |
| 2 | Withdraw Bank | “nations with this permission can withdraw resources from the alliance's bank to nations or other alliances” | Move pooled value out to a nation or another alliance | Leader and Heir; the source does not list it in the Officer bundle |
| 3 | Change Permissions | “nations with this permission can add, delete, and edit permissions of custom positions” | Create, edit and delete custom positions and their permission sets | Leader, Heir and Officer |
| 4 | See Spies | “nations with this permission can see the spy counts of every other nation in the alliance” | Read every member's spy count | Leader and Heir; not listed for Officer |
| 5 | See Reset Timers | “nations with this permission can see the reset times of every other nation in the alliance” | Read every member's reset timing | Leader and Heir; not listed for Officer |
| 6 | Tax Brackets | “nations with this permission can see, edit, and delete tax brackets as well as move members between brackets” | Change who pays which monetary/resource percentage | Leader and Heir; not listed for Officer |
| 7 | Post Announcements | “nations with this permission can post alliance announcements” | Publish a notice as the alliance | Leader, Heir and Officer |
| 8 | Manage Announcements | “nations with this permission can manage pre-existing alliance announcements” | Edit or remove existing notices | Leader, Heir and Officer |
| 9 | Manage Applicants | “nations with this permission can accept or reject applicants to the alliance” | Decide membership applications | Leader, Heir and Officer |
| 10 | Remove Members | “nations with this permission can remove members from the alliance” | Expel a member | Leader, Heir and Officer |
| 11 | Edit Alliance Info | “nations with this permission can edit the alliance's information (description, flag, Discord link, etc.)” | Change public identity and the external link | Leader, Heir and Officer |
| 12 | Manage Treaties | “nations with this permission can send, accept, or reject treaties” | Act on alliance treaty records | Leader, Heir and Officer |
| 13 | Manage Market Share | “nations with this permission can manage which alliances to share your alliance's market with” | Change which alliances share the market | Leader and Heir; not listed for Officer |
| 14 | Manage Embargoes | “nations with this permission can place or remove embargoes on behalf of your alliance” | Impose or lift an alliance embargo | Leader and Heir; not listed for Officer |
| 15 | Promote Self to Leader | “nations with this permission can promote themselves to the Leader position at any time” | Take the Leader office unilaterally | Leader and Heir; the source does not list it for Officer, but Officer can define custom positions |

**Currency caveat.** The page says “currently” but publishes no revision date and is community-maintained. The 15-item list is the best available current inventory, not an official game contract. It is classified `COMMUNITY DOCUMENTATION` and is not promoted to `PRIMARY/OFFICIAL`.

### 7.3 Per-permission risk and governance assessment

| # | Permission | Abuse / failure mode | Moves money or resources? | Affects another player's rights? | Affects treaties or diplomacy? | Security-sensitive information? | Separate into narrower permissions? | Confirmation / audit history? | Default or explicit grant? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | View Bank | Financial reconnaissance; leak of pool strength | No (read) | No | No | **Yes** — pool contents | Keep separate from withdrawal | Log privileged reads | Default for finance roles |
| 2 | Withdraw Bank | Theft, unilateral spending, laundering, alt funding | **Yes** | Indirectly, through pooled member assets | Can interact with embargo/transfer rules | **Yes** | **Yes** — split propose, approve, execute, and set a published limit | **Yes** — reason, recipient, approval, immutable history | Explicit grant only |
| 3 | Change Permissions | Privilege escalation; self-grant; lockout of the legitimate leader | Indirectly (controls access to money) | **Yes** — changes what others may do | Indirectly | **Yes** | **Yes** — separate office creation from permission granting; a grantor cannot exceed their own rights | **Yes** — before/after, actor, re-auth | Explicit grant only; not a default officer power |
| 4 | See Spies | Surveillance; leak of defensive intelligence | No | **Yes** — privacy of every member | No | **Yes** — spy counts | Keep separate from any operational order | Log access; disclose to members | Explicit grant |
| 5 | See Reset Timers | Inference of play/activity patterns; targeting | No | **Yes** — privacy | No | **Yes** — timing | Keep separate; aggregate if possible | Log access | Explicit grant |
| 6 | Tax Brackets | Unilateral fiscal change; member targeting; evasion | **Yes** — changes member obligations | **Yes** | No (domestic fiscal) | No | **Yes** — view, edit, move-member | **Yes** — publish changes and effective turn | Explicit grant |
| 7 | Post Announcements | Spam, impersonation, misinformation | No | Indirectly (reputation) | Can be diplomatic signalling | No | Keep separate from Manage Announcements | Record author and edit history | Default for communications role |
| 8 | Manage Announcements | Silent rewrite or deletion of official notices | No | Indirectly (record integrity) | Indirectly | No | Keep separate from posting | **Yes** — append-only edit history | Explicit grant |
| 9 | Manage Applicants | Coercion, bait alliances, discriminatory admission, data misuse | No | **Yes** — controls entry | No | **Yes** — applicant data | Keep separate from Remove Members | **Yes** — reason and decision record | Default for recruitment role |
| 10 | Remove Members | Mass expulsion, asset access loss, retaliation | Indirectly (pool access) | **Yes** | No | No | Keep separate from Manage Applicants | **Yes** — reason, notice, rate limit, audit | Explicit grant; not a default officer power |
| 11 | Edit Alliance Info | Impersonation, phishing link swap, brand damage | No | Indirectly (all members) | Publicly diplomatic | No | **Yes** — split profile text from external-link editing | **Yes** — before/after and link audit | Split; link edit explicit only |
| 12 | Manage Treaties | Unauthorised diplomatic commitment; treaty laundering | No | **Yes** — binds other nations politically | **Yes** | No | **Yes** — separate send, accept, reject; national consent must remain with each owner | **Yes** — record actor, text and turn | Explicit grant only |
| 13 | Manage Market Share | Preferential market access; exclusion of rivals | Indirectly (trade access) | **Yes** — other alliances | **Yes** — economic diplomacy | No | Keep separate from trade/embargo | Record the changed sharing set | Explicit grant |
| 14 | Manage Embargoes | Sanctions abuse; collective punishment; trade denial | **Yes** — blocks trade | **Yes** — other nations/alliances | **Yes** | No | Keep separate; national consent cannot be replaced | **Yes** — public record and reason | Explicit grant only |
| 15 | Promote Self to Leader | **Leadership capture at any time**; treasury and permission takeover | Indirectly (gains all Leader powers) | **Yes** — every member | **Yes** — gains treaty/embargo powers | **Yes** — gains all privileged views | **Never copy as one permission**; leadership transfer is a separate procedure | **Yes** — mandatory confirmation, notice and audit; ideally a delay | **Do not ship**; only an explicit, approved transfer procedure |

### 7.4 Governance-risk analysis

**Bank and treasury.** P&W separates View Bank from Withdraw Bank, which is better than a single “bank” flag, but there is no documented per-actor withdrawal limit, no propose/approve split and no dual-control permission. Withdraw Bank can move resources to another alliance, so a compromised officer can externalise the pool. The 2015 “Tiered Bank Access” proposal describes the model as “all or nothing” and asks for tiered officer limits (`ALS-016`) — evidence of a gap, not of a feature. Nation Supremacy must add a published limit, independent approval above a threshold, a named recipient and an immutable transaction history. Economy remains the owner of the value movement; Alliance owns only the authorization.

**Change Permissions.** This is the most dangerous ordinary permission. It can create a custom position carrying any permission from the list, including Withdraw Bank and Promote Self to Leader. The wiki recommends least privilege and specifically warns about granting Promote Self to Leader (`ALS-013`). A holder can therefore manufacture authority rather than merely exercise it. Nation Supremacy must separate `roles.manage` from the capabilities it grants, forbid a grantor from granting beyond their own rights, require re-authentication, and record before/after state. **Do not** make `roles.manage` a default officer power.

**Promote Self to Leader.** The exact documented effect is that a nation with the permission “can promote themselves to the Leader position at any time”. There is no election, no cooldown, no second approver and no notice requirement in the source. Heirs have a second path: when the alliance has no Leader, an Heir can appoint themselves Leader and gain full permissions. This is a designed capture route, not a hypothetical exploit. Nation Supremacy must not copy it. Leadership transfer should be an explicit procedure with a recorded actor, target, turn, reason and confirmation; removal of a captured Leader needs its own approved path (`UD-043`).

**Treaties and embargoes.** `Manage Treaties` lets a holder send, accept or reject treaties “on behalf of” the alliance; `Manage Embargoes` lets a holder place or remove embargoes on behalf of the alliance. These are alliance-level powers. Nation Supremacy's B-08 gives the active nation's authenticated owner sole diplomatic authority and refuses delegation (`REQ-530`, `DIP-148`). The P&W permissions are evidence of a different governance model, not a rule to copy. An alliance may publish a non-binding position; it may not consent to a treaty or impose a B-08 embargo for a member.

**Tax brackets.** `Tax Brackets` lets a holder see, edit and delete brackets and move members between them. P&W collects monetary and resource percentages automatically. This combines fiscal policy, member targeting and a recurring economic effect behind one permission with no documented approval step. Nation Supremacy has no alliance taxation model and 09A does not invent one; automatic taxation remains excluded from the first release (`REQ-578`). Any future model needs an Economy decision, a formula-register entry and member-visible rules.

### 7.5 Custom positions and permission separation

What the source establishes:

1. A **position** is a named slot with a position level and a permission set; its title is displayed on the nation and alliance pages (`ALS-013`).
2. A **permission** is one of the 15 discrete capabilities.
3. A **custom position** is created, edited or deleted by a holder of Change Permissions, with permissions chosen from the same 15-item list and any positive position level.
4. The default Leader/Heir/Officer positions are **bundles**, not single permissions; Heir duplicates Leader's powers, and Officer carries a broad subset.
5. The source does **not** document individual per-member permission overrides, temporary delegation, or a separate “leader authority” object. Those must not be claimed as P&W mechanics.
6. The source does **not** state whether a holder can assign a custom position to themselves; it only says they can create/edit/delete positions. The risk analysis treats self-assignment as a possibility to defend against, not as a verified P&W action.

**Implication.** Nation Supremacy should distinguish a *rank/title* (cosmetic ordering), an *office* (a named position), a *capability* (one checked permission), and a *temporary delegation* (time-bounded, explicit, revocable). Only the capability is checked at execution. A custom office is a bundle, never a source of authority beyond its creator's own rights.

### 7.6 Comparison table

| Politics & War permission | Actual observed scope | Risk | Nation Supremacy implication | Proposed 09B investigation |
|---|---|---|---|---|
| View Bank | Read pool contents | Financial reconnaissance | Separate `treasury.view`; log privileged reads | Whether members see aggregate balances and who sees detail |
| Withdraw Bank | Move pool value to a nation or alliance | Theft, unilateral spending, laundering | `treasury.propose` / `treasury.approve` / `treasury.execute`, published limit, audit | Threshold, dual approval, recipient allowlist, grant vs loan |
| Change Permissions | Create/edit/delete custom positions with any subset | Privilege escalation, lockout | Separate `roles.manage`; no grant beyond own rights; re-auth; audit | Whether custom offices ship at launch and who may create them |
| See Spies | Read every member's spy count | Surveillance, intelligence leak | Do not create this capability in 09B; Military owns spy data | Whether an alliance reads any military aggregate at all |
| See Reset Timers | Read every member's reset timing | Activity inference, targeting | Do not create; readiness is voluntary, never inferred | Whether any timing signal is shown, and at what aggregation |
| Tax Brackets | See/edit/delete brackets; move members | Fiscal coercion, targeting | No alliance tax model; automatic taxation excluded | Whether any alliance fee exists at all (requires Economy decision) |
| Post Announcements | Publish alliance notices | Spam, misinformation | `announcements.publish`, asynchronous, rate-limited | Length, rate, retention, edit policy |
| Manage Announcements | Edit/remove existing notices | Silent rewrite of record | `announcements.manage` plus append-only history | Whether deletion is allowed or only superseding |
| Manage Applicants | Accept/reject applicants | Coercion, discrimination, data misuse | `members.applications.manage`; applicant sees own record | Appeal path, reason codes, reapply cooldown |
| Remove Members | Expel a member | Mass expulsion, retaliation | `members.remove` with reason, notice, rate limit, audit | Notice period, appeal, asset-access effect |
| Edit Alliance Info | Edit description, flag, Discord link | Impersonation, phishing | Split `profile.edit` from `profile.link.manage`; URL validation | Link host allowlist and visibility default |
| Manage Treaties | Send/accept/reject alliance treaties | Unauthorised diplomatic commitment | No alliance treaty object; national consent remains | UD-039: positions only vs any alliance treaty |
| Manage Market Share | Choose which alliances share the market | Preferential access, exclusion | No alliance market channel; Global Trade gates unchanged | Whether an alliance may publish trade preferences only |
| Manage Embargoes | Place/remove alliance embargoes | Sanctions abuse, collective punishment | Only a nation owner may impose a B-08 embargo | UD-047: position vs binding collective act |
| Promote Self to Leader | Promote self to Leader at any time | Leadership and treasury capture | **Do not copy**; explicit transfer/removal procedure with confirmation and audit | UD-043: who may transfer, who may remove, what delay applies |

### 7.7 Least-privilege conclusion

P&W now has **per-action primitives**, not a single “officer” flag, but its default bundles are broad and its most dangerous permission can be placed in a custom position by any Change Permissions holder. The transferable lesson is not “copy the 15 permissions”; it is “separate the primitives, separate the power to grant them, and never make self-promotion a permission.” Nation Supremacy should model independent capabilities with roles as named bundles, and should never create a single unrestricted “officer” capability (`REQ-552`–`REQ-561`).

---

## 8. Politics & War — economy, bank and taxes

Official PWPedia (`ALS-002`) establishes:

- Tax brackets carry a **monetary percentage** and a **resource percentage**; the game collects them automatically each turn.
- Changing brackets requires **Bank Access**.
- A **Default** bracket exists, cannot be renamed or deleted, and receives new members.
- Members can be bulk-moved between brackets by city count.
- Deleting a bracket moves its members to Default.
- **Gray nations are not taxed.**

Official rules (`ALS-005`) establish, among other things:

- One nation per player; shared-network nations are restricted from interacting in specified ways.
- Using alliance banks to evade trade restrictions imposed on same-network nations is a **bannable offence**.
- Same-network nations may coexist in an alliance but may not jointly declare on the same target.
- New nations may not send all or most of their money/resources away.
- Automated banking is prohibited; a Discord bot that merely offers an alternative interface to a **manually triggered** withdrawal is described as generally acceptable in the rules example.
- Protecting an alliance bank via vacation mode or a disposable new nation is prohibited.
- Moderation actions require two moderators.

Live evidence: Rose's bank and tax structure is not publicly enumerated, but third-party tooling (AEGIS) documents grants, loans, safekeeping and "offshore" holdings, plus approval limits and audit history (`ALS-012`). That is **third-party tooling**, and its existence demonstrates demand for controls the native game does not supply.

**Implications.**

- A shared treasury is only legitimate if value is **already owned** by the depositing nation; the pool must never mint (`ECN-213`, `DD-067`).
- View and withdrawal are separate capabilities in P&W; Nation Supremacy should go further and separate propose, approve and execute, with a published limit and dual approval above a threshold.
- Withdrawals need capability checks, policy limits, dual approval where the owner decides, and an immutable, member-visible history.
- `Tax Brackets` is a single permission that changes member obligations with no documented approval step; automatic taxation is not adopted in the first release (`REQ-578`).
- Alliance banks must not be usable to circumvent same-network, trade, or transfer restrictions already in force.
- "Offshore" and "safekeeping" patterns are external workarounds; they should not become native features without an explicit decision.
- National warehouse storage rules (`ECN-120` / `REQ-141`) and overflow blocking (`ECN-124` / `REQ-142`) govern national inventory operations. They do not automatically establish storage capacity or deposit limits for a separate Alliance Treasury pool (`REQ-176`). Alliance treasury storage limits, deposit rejection/capping behaviour, and over-capacity handling remain an unresolved design decision (`UD-046`) for Prompt 09B.

Candidates: `REQ-571`–`REQ-578`; decisions `UD-046`.

---

## 9. Politics & War — diplomacy and military coordination

**Diplomacy.** Official foreign-affairs guidance (`ALS-004`) covers embassies, treaty negotiation and peace terms, and explicitly suggests hosting an embassy area "on your alliance Discord server or somewhere else". Live alliance pages publish treaty lists using community treaty vocabulary: MDoAP, ODoAP, NAP, ODP, protectorate and extension (Rose, `ALS-006`). The game does not appear to provide alliance-level treaty objects with binding mechanics in the evidence gathered; enforcement is political.

**Military.** Official internal-affairs guidance (`ALS-003`) covers activity management (including moving a nation to applicant status to avoid bank looting), training, MMR/infrastructure audits, and removing leaks. Actual war coordination happens in Discord war rooms, pings and spreadsheets; AEGIS formalises this with operations rooms and readiness data (`ALS-012`). None of this grants an officer the right to move another player's army.

**Implications.**

- Alliance diplomacy must be **expressive, not authoritative**: publish positions, record internal approval, but never bind a member nation's diplomatic rights or create a treaty the Diplomacy system did not authorize.
- Alliance military features must be **coordination and information**: rosters, readiness declarations, operation notices, defence requests. Execution remains with each nation owner under Military rules.
- This directly supports UD-039's recommendation (§17).

Candidates: `REQ-579`–`REQ-591`; decisions `UD-047`.

---

## 10. Native vs. community vs. third-party — P&W map

| Capability | Provided natively by P&W | Community practice | Third-party tooling |
|---|---|---|---|
| Alliance identity/profile | Yes | Custom flags, propaganda, branding | Alliance websites |
| Membership list/applications | Yes (basic) | Interviews, trials, onboarding docs | Recruitment pipelines (AEGIS) |
| Ranks and powers | Yes (coarse) | Department titles, custom hierarchies | Role mapping and audits |
| Bank and tax brackets | Yes | Grants, loans, "offshores", safekeeping | Treasury dashboards, approval limits |
| Treaties | Published on page; political enforcement | Treaty lists, bloc charters | Treaty trackers |
| War coordination | War system is nation-level | War rooms, pings, readiness sheets | Operations rooms, compliance checks |
| Announcements | Alliance page text | Discord announcements, forums | Notification bridges |
| Discussion | **No** | **Discord is the venue** | Bots, relays, verification |
| Account linking | **No** | Manual nickname conventions | `/link` verification (AEGIS) |

**Reading:** the columns are the argument. Nation Supremacy's native layer should cover the first column and the *records* implied by the third, and should deliberately leave the middle column to players.

---

## 11. Discord model — evidence and boundary

### 11.1 Observed practice

- Invite links are published openly on alliance pages and recruitment sites (Rose, GLOB, Weebunism, Ragnarok, United Ummah; Black Knights' apply page).
- Discord is used for interviews, onboarding, announcements, departmental channels, war rooms and diplomacy.
- Some alliances make Discord mandatory for membership (Rose states this explicitly); others present it as strongly expected.
- Verification is manual (nickname = nation name) or bot-assisted (`/link`), the latter only via third-party tooling.
- The game itself neither knows nor verifies any of this.

### 11.2 Research conclusion

A **static invite URL plus visibility and edit permissions** reproduces the entire legitimate in-game surface of this practice. Everything beyond that (roles, verification, relays, message mirroring, presence) is either a Discord-side concern or a paid/complex integration that the product constraint excludes. No evidence shows that players need the game to broker Discord identity.

### 11.3 Required boundary (refined)

| Function | Nation Supremacy | Discord |
|---|---|---|
| Membership, ranks, permissions | Authoritative | Discussion only |
| Applications and outcomes | Authoritative status | Interview/discussion venue |
| Treasury and transactions | Authoritative ledger | Discussion only |
| Formal votes | Authoritative record where approved | Campaigning/discussion |
| Treaty consent | Player action in-game | Cannot substitute |
| Military orders/execution | Military rules; player consent | Coordination talk |
| Announcements | Candidate async native notices | Community announcements |
| Member discussion | **Not provided** | Primary venue |
| Identity/account | Nation account only | Optional, unlinked |

### 11.4 Static link rules to research in 09B

Candidates: optional per alliance; `https` only; host allowlist for known invite domains (`discord.gg`, `discord.com/invite`); length cap; no redirects; visible to `public` or `alliance` per visibility setting; editable only with a dedicated capability; change recorded in audit history; displayed with an external-link warning; never fetched or validated by the server beyond syntax; broken/expired links are the alliance's responsibility with a "report broken link" path. `REQ-598`–`REQ-603`.

### 11.5 Security and privacy

The game must not collect Discord identifiers, messages, membership or presence. Risks that remain are phishing via lookalike domains, leaked invites, impersonation and players treating chat as official. Controls are disclosure, allowlisted hosts, clear "external" labelling, and an explicit rule that chat never constitutes consent or authorization (see `ALRK-14`–`ALRK-18`).

---

## 12. Comparative strategy games

| Game | Native feature | Community practice | Third-party / external | Transferable pattern | Risk |
|---|---|---|---|---|---|
| **eRepublik** (`ALS-018`–`ALS-021`) | Country president proposes alliance membership and MPPs; congress votes; alliance leader invites a country; MU commander can take over a unit | Party charters, elected HQ, council approval thresholds | Party forums, Discord | **Collective decisions need explicit quorum and approval records**; membership changes are politically contested | Leader capture; coup mechanics; vote gaming |
| **Stellaris** (`ALS-022`, indirect) | Federations with types, rotating presidency, cohesion, federation laws, federal fleets | Role-play rules, house rules | Mods, wikis | **Rotating/term-limited leadership and law levels** reduce permanent capture | Abstraction hides accountability; AI members |
| **EVE Online** (via `08A`, `DPS` IDs) | Corporations/alliances, roles, offices, war mechanics | SRP, fleets, diplomacy blocs | Forums, Discord, third-party tools | **Office/role-based authority with explicit revocation**; wars follow membership changes | Espionage, theft via roles, war-copy abuse |
| **Call of War** (via `08A`, secondary) | Coalitions and shared war conduct | Team play, external comms | Discord | Coalition coordination without ownership transfer | Coalition leader overreach |

**Cross-cutting findings.**

1. Every comparator that allows leadership change also has a **succession or removal** rule; Nation Supremacy cannot defer this.
2. Every comparator with shared assets eventually needs **audit history and separation of duties**, whether native or via tools.
3. No comparator makes external chat authoritative; even where tools bridge chat, the game state remains the record.
4. Where alliances can bind members' diplomacy, disputes follow. The safer pattern is **member consent plus alliance position**, which aligns with B-08.

---

## 13. Proposed feature set and cost classification

Classification is qualitative and evidence-based. No currency figures are asserted.

| # | Feature | Dev complexity | Hosting/DB | Ongoing processing | Third-party | Maintenance | Security/moderation | Necessity | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Alliance profile + directory | Medium | Low | Read-only | None | Low | Low | Core | Include |
| 2 | Founding/dissolution | Medium | Low | Low | None | Medium | Medium | Core | Include |
| 3 | Membership lifecycle + applications | High | Low | Low (event-driven) | None | Medium | Medium | Core | Include |
| 4 | Ranks/roles/permission matrix | High | Low | Negligible | None | Medium | **High** | Core | Include, least privilege |
| 5 | Audit/history log | Medium | Medium (bounded) | Low | None | Medium | High | Core | Include |
| 6 | Announcements (async) | Low | Low | Low | None | Low | Low | High | Include |
| 7 | Treasury + ledger + approvals | High | Medium | Low | None | High | **Very high** | High | Include, gated on decisions |
| 8 | Formal proposals/votes | Medium | Low | Low | None | Medium | Medium | Medium | Include if UD-049 approved |
| 9 | Static Discord link | **Very low** | Negligible | None | None | Very low | Low | Medium | Include |
| 10 | Alliance diplomacy positions | Medium | Low | Low | None | Medium | Medium | Medium | Position only; no treaty object |
| 11 | Military coordination notices | Medium | Low | Low | None | Medium | Medium | Medium | Information only |
| 12 | Alliance stats/history page | Low | Low | Low | None | Low | Low | Nice | Include if cheap |
| 13 | Real-time chat / DMs / presence | **Very high** | **High** | **High** | Possibly | **Very high** | **Very high** | **None** | **Excluded** |
| 14 | Discord bot / OAuth / role sync / mirroring | High | Medium | Medium | **Yes** | High | High | **None** | **Excluded** |
| 15 | Hosted chat subscription | n/a | n/a | Recurring | **Yes** | n/a | High | **None** | **Excluded** |

**Cost conclusions.**

- Features 1–6 and 12 are ordinary CRUD with small rows; their cost is dominated by correctness and moderation policy, not infrastructure.
- Feature 7 is the expensive one: double-entry ledger, approval workflow, reconciliation, dispute handling, fraud review. It must be release-gated on `UD-046` and must reuse the Economy ledger rather than invent a second one.
- Feature 8 is cheap technically but politically expensive; it needs tie-breaking, quorum, eligibility and dissolution rules.
- Feature 9 is the cheapest feature in the entire document and delivers most of the observed Discord value.
- Features 13–15 have **recurring** cost and are excluded by owner decision `D-133`.

---

## 14. Risk register (initial)

| ID | Scenario | Affected | Impact | Existing rule | Potential control | Authority | Stage |
|---|---|---|---|---|---|---|---|
| ALRK-01 | Leader drains treasury via standing withdraw right | Members | Economic loss, trust collapse | REQ-013; ECN-213 | Capability split, limits, dual approval, public ledger | 09B / owner | 09B |
| ALRK-02 | Officer silently changes permissions then grants self access | Members | Privilege escalation | None yet | Permission-change audit, re-auth, owner notice | 09B | 09B |
| ALRK-03 | Leadership capture via inactivity or absent succession | All | Alliance freeze | UD-012 | Explicit succession + inactivity trigger | Owner | 09B |
| ALRK-04 | Mass expulsion before dissolution | Members | Loss of access/assets | — | Notice period, appeal, asset freeze on dissolution | Owner | 09B |
| ALRK-05 | Fake alliance impersonating a known brand | Applicants | Fraud/phishing | — | Name uniqueness, verified profile badges later | 09B | 09B |
| ALRK-06 | Discord invite points to phishing clone | Applicants | Account compromise | — | Host allowlist, external warning, report path | 09B | 09B |
| ALRK-07 | Players treat Discord vote as binding | Members | Governance disputes | D-133 | Repeated in-game disclosure; no chat authority | 09B | 09B |
| ALRK-08 | Alliance used to evade same-network/trade limits | Economy | Rule violation/exploit | P&W rules analogue; project transfer rules | Reuse Economy checks; no bypass path | Economy owner | 09B |
| ALRK-09 | Alliance bank used to launder restricted transfers | Economy | Exploit | DD-052 | Membership-aware transfer checks | Economy owner | 09C |
| ALRK-10 | Applicant data exposed publicly | Applicants | Privacy | REQ-057 | Field-level visibility; applicant-only view | 09B | 09B |
| ALRK-11 | Vote manipulation via alts | Polity | Illegitimate outcome | One-nation rule | Eligibility snapshot, turnout record | 09B | 09C |
| ALRK-12 | Leader claims authority over member military | Members | Sovereignty violation | B-08, Military | Explicit non-authority statement + UI | 09B | 09B |
| ALRK-13 | Treaty "signed" by alliance binds member | Members | Diplomacy conflict | DIP-146…149 | No alliance treaty object | Owner | 09B |
| ALRK-14 | Member leaves with granted assets | Economy | Dispute | — | Grant vs. loan semantics; clawback policy | Owner | 09B |
| ALRK-15 | Dissolution strands treasury | Members | Loss | — | Distribution rule before dissolution | Owner | 09B |
| ALRK-16 | Announcement spam / notification flood | All | Cost, abuse | — | Rate limits, length caps, retention caps | 09B | 09C |
| ALRK-17 | Audit log growth | Ops | Storage cost | — | Bounded retention + aggregates | 09B | 09C |
| ALRK-18 | Compromised leader account | Members | Broad damage | — | Sensitive-action confirmation, delay, notice | 09B | 09C |
| ALRK-19 | Collusion to manipulate rankings | All | Fairness | — | Ranking inputs exclude alliance-controlled transfers | 09B | 09C |
| ALRK-20 | Retroactive rule changes harm members | Members | Disputes | — | Amendment recording, effective dates | 09B | 09B |
| ALRK-21 | Applicant coerced into external platform | Applicants | Accessibility | D-133 | Explicit "Discord not required by game" | 09B | 09B |
| ALRK-22 | Alliance becomes mandatory for progress | All | Violates AP-004 | AP-004 | Keep alliance membership optional; no alliance-only power | 09B | 09B |

No enforcement power or numeric limit is created here.

---

## 15. Candidate requirements baseline

84 candidate requirements were added as `REQ-534`–`REQ-617` in `03_requirements_traceability.md`, all with status **Proposed** (the register's term for a candidate with no design commitment). They are grouped:

| Group | IDs | Count | Priority mix |
|---|---|---|---|
| Functional (identity, founding, profile, dissolution) | REQ-534–541 | 8 | P1 × 5, P2 × 3 |
| Governance | REQ-542–551 | 10 | P1 × 4, P2 × 5, P3 × 1 |
| Permission and authority | REQ-552–561 | 10 | P1 × 7, P2 × 3 |
| Membership | REQ-562–570 | 9 | P1 × 5, P2 × 3, P3 × 1 |
| Economic | REQ-571–578 | 8 | P1 × 4, P2 × 3, P3 × 1 |
| Diplomatic | REQ-579–585 | 7 | P1 × 3, P2 × 4 |
| Military integration | REQ-586–591 | 6 | P2 × 5, P3 × 1 |
| Privacy and security | REQ-592–597 | 6 | P1 × 4, P2 × 2 |
| External communication | REQ-598–603 | 6 | P1 × 2, P2 × 3, P3 × 1 |
| Performance and low cost | REQ-604–608 | 5 | P1 × 3, P2 × 2 |
| Audit and accountability | REQ-609–613 | 5 | P1 × 4, P2 × 1 |
| Accessibility and usability | REQ-614–617 | 4 | P2 × 3, P3 × 1 |

**Priority meaning.** P1 = required for a coherent first alliance release; P2 = required before the feature is called complete; P3 = valuable, deferrable.

Status discipline: none is Approved; none is Provisional (no design commitment yet); decisions referenced are `UD-###`, not resolved `D-###`.

---

## 16. Cross-system integration findings

Full 20-field matrix: `09A_alliance_integration_matrix.md` (`AX-01`–`AX-26`). Every requirement reference now carries a classification (`DIRECT DEPENDENCY`, `RELATED CONSTRAINT`, `SUPPORTING CONTEXT`, `NO VALID RELATIONSHIP` or `NO EXISTING REQUIREMENT`) and an evidence sentence; the per-AX human review is in `09A_alliance_reference_review.md`. Summary of the hard boundaries:

1. **Player sovereignty (P03/B-08).** Alliance office never transfers a member's nation authority. Treaties persist through membership changes; an alliance cannot consent for a nation (`DIP-146`–`149`).
2. **Economy (P04).** Treasury is a segregated pool of already-owned value with double-entry history. No minting (`ECN-213`, `DD-067`). No path around restricted-pair rules (`D-035`, `DD-052`).
3. **Global Trade (P07C).** Approved scope stays release-gated (`D-122`, `DD-136`, `REQ-513`, `G-1`…`G-6`). Alliance features must not create an alternate trade channel.
4. **Visibility (P02).** Alliance-scoped visibility must use the existing classes (`REQ-057`), not a parallel privacy model; aggregate disclosure still respects `D-027` (k=5).
5. **Turn/order (P02).** Membership, permission and treasury actions must declare their position in the turn order and be idempotent; no real-time semantics.
6. **Dormancy (D-028).** A dormant leader must not freeze an alliance; succession interacts with the 14-day/168-turn rule.
7. **Elections/crisis (B-06).** Alliance governance must not override nation elections or crisis states; an officeholder in crisis retains/lerps nation authority per B-06, not alliance rules.
8. **Market (B-07).** Alliance support programmes must respect fair-value and fresh-nation restrictions; no alliance-only price or transfer channel.
9. **Military (future B-10).** Coordination is informational; execution stays national.
10. **Rankings/chronicle (future).** Alliance aggregates may be displayed but must not let controlled transfers inflate standings.

---

## 17. UD-039 analysis and recommendation

**Current text (preserved):** whether alliance-level treaties reuse the B-08 treaty object, and whether an alliance may delegate diplomatic authority for a member. The register records three options: **(a)** 09 reuses the B-08 object for alliance-level treaties and adds no delegation; **(b)** 09 reuses the object and defines an explicit, revocable, audited delegation model; **(c)** 09 defines a separate alliance-treaty object with its own lifecycle. Status: **Deferred to Prompt 09**; Class B; owner approval outstanding.

**Evidence.**

- P&W publishes alliance treaty lists and its 15-permission inventory gives a holder `Manage Treaties` and `Manage Embargoes` "on behalf of your alliance" (`ALS-013`), but the available evidence does not establish binding alliance-treaty mechanics; enforcement is political (`ALS-004`, `ALS-006`). The existence of an alliance-level permission is evidence of a different model, not proof of a binding alliance treaty object.
- eRepublik makes alliance membership and MPPs **country-level decisions requiring congressional votes** (`ALS-018`–`ALS-020`) — i.e., the polity, not a supra-national alliance, consents.
- B-08 already establishes bilateral consent, persistence through alliance changes, and that an alliance is never a party or guarantor (`DIP-146`–`149`).
- Building option (c) would require new Diplomacy states, new consent semantics, new war-risk inputs and new dissolution handling — a rewrite of closed 08C rules, which 09A is forbidden to do.

**Recommendation (not a resolution):** for the initial release, adopt **no alliance-level treaty object at all**: the B-08 object remains nation-only, alliance diplomacy is a non-binding published *position*, and any binding act is a nation-level B-08 treaty consented to by each member's owner. This is **not option (a)**: option (a) still creates alliance-level treaties under the B-08 object. It is a **no-object path outside UD-039's three recorded options**, and 09A records it as a research recommendation only. Option (b) or (c) may be considered later, but either would be a Diplomacy-owned object with explicit member consent, not a power of an alliance office.

**Why not mark resolved:** the decision is Class B and requires owner approval; 09A can only recommend. The no-object path must be put to the owner in 09B as an additional option (or as an explicit clarification of the existing choices) before any alliance diplomacy feature is specified. UD-039 therefore stays `Deferred to Prompt 09`; its status and recorded a/b/c text are unchanged.

**Historical-status note (2026-11-01):** 09A's recommendation above is retained as the research record and is **not current design**. `D-137` resolved UD-039 by adopting the no-object path for B-08 with zero diplomatic delegation; `D-140` then amended only the no-object component by authorizing a separate B-09 Alliance-to-Alliance object under explicit per-nation consent. No B-08 object is reused, and no delegation is created.

---

## 18. Unresolved decisions opened by 09A

| ID | Question | Class | Stage |
|---|---|---|---|
| UD-012 | Roles, shared pool and succession (existing) | B | 09B |
| UD-039 | Alliance diplomatic agreements (existing) | B | 09B |
| UD-040 | Who may found an alliance and under what eligibility | B | 09B |
| UD-041 | Default government model and leadership structure | B | 09B |
| UD-042 | Constitution/charter and voting model | B | 09B |
| UD-043 | Succession, resignation, removal, inactivity | B | 09B |
| UD-044 | Membership rights, appeals, rejoin, expulsion | B | 09B |
| UD-045 | Permission granularity and delegation limits | B | 09B |
| UD-046 | Treasury ownership, withdrawal authorization, dual approval | B | 09B |
| UD-047 | Collective diplomatic authority and delegation | B | 09B |
| UD-048 | Discord link visibility and validation | B | 09B |
| UD-049 | Announcements and formal votes in the initial release | B | 09B |

---

## 19. Prompt 09B handoff

**Carry forward as evidence (not rules):** the native/external split (§10), the complete 15-permission inventory and its risk assessment (§7.2–§7.6), the Black Knights three-stage recruitment evidence (§6.1), the Discord boundary (§11.3), the static-link rule candidate set (§11.4), the cost classification (§13), the risk register (§14), the 84 candidate requirements, and the AX matrix with its per-requirement classifications.

**Governance models to evaluate in 09B (all unapproved):**

1. Founder-led with appointed officers (simplest; highest capture risk).
2. Leader + heir + department heads (P&W-like; familiar; needs succession).
3. Council of elected officers with a chair (moderate complexity; needs quorum).
4. Bicameral/member vote on constitutional changes (highest complexity; strongest legitimacy).
5. Merit/appointment hybrid with recorded criteria (medium; opaque without records).

**Defaults proposed for 09B to confirm or reject (not approved):** unique name; public profile with field-level visibility; founder = first Leader; Leader/Heir/Department Head/Councillor/Member as default roles; permissions as independent capabilities; `roles.manage` separated from every capability it grants and never a default officer power; no self-promotion capability; treasury segregated and double-entry; view, deposit, propose, approve and execute separated; withdrawals with a published limit and optional dual approval; announcements asynchronous and rate-limited; Discord link optional, static, allowlisted, audited; no alliance treaty object (a no-object path outside UD-039's recorded a/b/c options); no chat.

**Questions 09B must settle:** founding cost/eligibility; member cap; whether an alliance can be destroyed and what happens to assets; default role set; how a Leader is removed; inactivity threshold (consistent with D-028); whether votes are native; quorum and tie-break; whether announcements are in the first release; Discord visibility default; appeal path; how alliance history survives dissolution; alliance treasury storage capacity and over-capacity deposit behaviour (UD-046 / AX-08).

**Excluded permanently unless the owner changes D-133:** chat, DMs, presence, typing, read receipts, message storage/moderation, voice/video, bots, OAuth, role sync, mirroring, hosted chat, and any feature whose main effect is real-time conversation.

---

## 20. Limitations

- The Fandom `Alliance_Permissions` page was directly retrievable on 2026-10-31 and is used directly; it remains community documentation with no published revision date. The Stellaris wiki still returns 427, so its claims rely on search-indexed excerpts.
- The live P&W join flow was not executed; founding mechanics are described at the level the official wiki supports, and the applicant state is evidenced by native applicant lists and the Black Knights instruction.
- The Black Knights requirements/interview panel is unpublished placeholder text; no minimum requirement or review duration is asserted. The claimed 24-hour interview belongs to Rose, not Black Knights.
- No P&W alliance bank contents or tax rates are reproduced; those are alliance-specific and not needed.
- EVE and Call of War evidence is inherited from 08A (`DPS` findings), not re-researched here; it is treated as secondary.
- No player survey or interview was conducted; "players want X" claims are avoided.
- Cost classification is qualitative; no vendor quotes or currency estimates exist.

---

## 21. Acceptance self-check (30 criteria)

PASS = evidence in this document or its companions. PARTIAL = done with a stated limitation. FAIL = not done.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Project docs inspected first | PASS | §3; matrix §2 |
| 2 | P&W multi-source research | PASS | §5–§10; source register 27 entries, 5 classes (09A-C added ALS-026/027) |
| 3 | Founding/membership documented | PASS | §5, §6 |
| 4 | Leadership/permissions documented | PASS | §7; all 15 permissions, default bundles, custom positions and risk analysis (09A-C) |
| 5 | Economy/treasury documented | PASS | §8 |
| 6 | Diplomacy/military documented | PASS | §9 |
| 7 | Recruitment/Discord, multiple alliances | PASS | §6, §11; 6 alliances; Black Knights three-stage process verified 2026-10-31 |
| 8 | Native vs. external distinguished | PASS | §10 |
| 9 | Third-party vs. official distinguished | PASS | §10, `ALS-012` |
| 10 | Additional game comparisons | PASS | §12 |
| 11 | No chat proposed | PASS | §11, §19; D-133 |
| 12 | Discord external, not authority | PASS | §11.3 |
| 13 | Minimal link model investigated | PASS | §11.4 |
| 14 | Budget/cost documented | PASS | §13 |
| 15 | Low-cost non-chat alternatives | PASS | §13 features 1–9, 12 |
| 16 | Prompts 01–06 inspected | PASS | §3 |
| 17 | Prompts 07A–07C/Global Trade inspected | PASS | §3, §16 |
| 18 | Prompts 08A–08C + corrections inspected | PASS | §3, §16 |
| 19 | Integration matrix complete | PASS | `09A_alliance_integration_matrix.md` v1.2; 26 AX records, 77 requirement relationships, each classified |
| 20 | Player authority boundaries preserved | PASS | §9, §16, §17 |
| 21 | UD-039 handled correctly | PASS | §17 (recommended, not resolved) |
| 22 | Candidate requirements with unique IDs | PASS | §15; REQ-534–617 |
| 23 | No duplication/overwrite | PASS | §3, matrix §3; Diplomacy/Market untouched |
| 24 | Security/abuse risks | PASS | §7.4, §14; self-promotion and Change Permissions escalation analysed |
| 25 | Traceable sources/findings | PASS | companion registers; forum permalinks corrected; `ALR-041`–`ALR-049` added |
| 26 | Owner decisions/questions | PASS | §17–§19 |
| 27 | Docs/handoff updated | PASS | see §22 |
| 28 | No implementation/real-time infra | PASS | no code, schema or config changed |
| 29 | 09B handoff complete | PASS | §19 |
| 30 | Validators pass | PASS | The earlier general validators passed at 09A; after 09A-C the targeted validator and its negative self-tests are the evidence for the corrected matrix (§23). See §23.4 for exact commands. |

**Overall: PASS for the research scope after 09A-C**, with the disclosed source-access limitations in §20 (recorded, not hidden). The earlier version of this table overstated the permissions and Black Knights findings; §23 records the correction. Nothing in this document implements gameplay or approves a rule.

---

## 22. Files produced or updated

| Path | Change |
|---|---|
| `docs/stage-2/research/09A_alliance_research.md` | This report (new in 09A; v1.1 corrected by 09A-C: full permission inventory, Black Knights process, source corrections, correction record). |
| `docs/stage-2/research/09A_alliance_sources_findings.md` | Source register `ALS-001`–`ALS-027`, findings `ALR-001`–`ALR-049`, conflicts, candidate recommendations (v1.1). |
| `docs/stage-2/research/09A_alliance_integration_matrix.md` | `AX-01`–`AX-26` 20-field matrix (v1.1; per-requirement classification and evidence). |
| `docs/stage-2/research/09A_alliance_reference_review.md` | Structured semantic review record for all 26 AX records (new in 09A-C). |
| `docs/stage-2/03_requirements_traceability.md` | REQ-534–617 appended; counts updated. |
| `docs/stage-2/04_approved_and_provisional_decisions.md` | DD-147–DD-150 recorded. |
| `docs/stage-2/05_unresolved_design_decisions.md` | UD-012/UD-039 notes; UD-040–049 added; counts updated. |
| `docs/DECISIONS.md` | D-133, D-134. |
| `docs/ROADMAP.md`, `docs/PROJECT_PROGRESS.md`, `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md` | 09A status, next action 09B. |
| `docs/stage-2/00_stage_2_handoff.md`, `01_…roadmap.md`, `02_…bible_outline.md`, `06_…progress_log.md` | 09A completion and 09B handoff. |
| `docs/qa_backups/*.py` | Hard-coded register counts/next-action expectations updated to the new canonical numbers. |
| `docs/qa_backups/09A_validate_alliance.py` | Targeted Alliance integration/source/handoff validator (new in 09A-C). |
| `docs/qa_backups/test_09A_alliance_validator.py` | Clean and 15 negative self-tests for the Alliance validator (new in 09A-C). |

---

## 23. Prompt 09A-C correction record

**Scope:** focused correction of the 09A research package. No gameplay, schema, API, screen, Discord integration or communication infrastructure was created. No existing Diplomacy, Economy, City, Market, Global Trade or Military rule was changed.

### 23.1 Defects corrected

| # | Defect found by the 09A audit | Correction | Where |
|---|---|---|---|
| 1 | AX-01 through AX-26 contained requirement references that existed but did not support the stated integration. | Every AX-to-REQ pair was re-read and classified; eleven invalid references were removed and replaced with requirements whose actual rule supports the integration. | Matrix §3, §6; review record |
| 2 | The Politics & War permissions research described only a subset of the native permissions. | The complete 15-permission inventory, the default position bundles, custom-position rules, per-permission risk and a comparison table were added. | §7 |
| 3 | The Black Knights recruitment example called the alliance site a placeholder shell and did not describe the actual process. | The current three-stage process (in-game Applicant → Discord → `/apply` bot interview workflow) was verified from the live alliance page and alliance-owned application page; the unpublished requirements panel is recorded as a limitation. | §6.1–§6.2 |
| 4 | Two forum sources cited the forum root rather than a thread. | Exact permalinks were recovered: `topic/9902-tiered-bank-access/` and `topic/6269-alliance-heirarchy-permissions-member-titles-and-seniority/`; a third thread was added for self-promotion evidence. | Source register ALS-016/017/027 |
| 5 | The Stage 2 handoff opening said Prompt 09 had not started while later sections said 09A was complete and 09B next. | All current-status and next-action records now say 09A accepted after 09A-C and 09B next; historical dated entries are retained. | Handoff, roadmap, progress, continuity files |
| 6 | General validators checked identifier existence but not semantic support. | A targeted Alliance validator now checks AX structure, classifications, evidence presence, forbidden stale pairs, ownership claims, Discord exclusions, permission-source coverage, forum URLs and handoff agreement, with 15 negative self-tests. | `qa_backups/09A_validate_alliance.py`, `test_09A_alliance_validator.py` |

### 23.2 What did not change

- `D-133` and `DD-147` remain the no-real-time-chat and no-Discord-integration constraints.
- `DD-148` remains **Provisional**; `DD-149` and `DD-150` are unchanged.
- `UD-039` remains deferred to Prompt 09B; `UD-040`–`UD-049` remain open with the same questions.
- `REQ-534`–`REQ-617` remain 84 **Proposed** requirements; none was approved, deleted or renumbered. Only clearly invalid dependency cells were corrected.
- Global Trade remains approved scope (`D-122`, `DD-136`, `REQ-513`) and release-gated by `G-1`…`G-6`.
- No owning system's rule was edited.

### 23.3 Acceptance criteria (09A-C)

| # | Condition | Result | Evidence |
|---|---|---|---|
| 1 | Current research and project documents inspected | PASS | §3; matrix §1.2 |
| 2 | All 26 AX records semantically audited | PASS | Matrix §3; review record §3 |
| 3 | Invalid references corrected or removed | PASS | Matrix §6 |
| 4 | Every AX-to-REQ reference classified | PASS | Matrix §3; validator group 3 |
| 5 | Every direct dependency has evidence | PASS | Matrix §3; validator group 4 |
| 6 | Related/supporting not presented as direct | PASS | Matrix §3; validator group 4 |
| 7 | Subsystem ownership boundaries correct | PASS | Matrix §5; validator group 5 |
| 8 | Complete P&W permission inventory documented | PASS | §7.2 |
| 9 | Permission risks analysed, including self-promotion, treasury and treaties | PASS | §7.3–§7.4 |
| 10 | Custom positions and permission separation investigated | PASS | §7.5 |
| 11 | Black Knights process described from current evidence | PASS | §6.1 |
| 12 | Native vs. alliance-specific vs. third-party distinguished | PASS | §6.2 |
| 13 | Forum sources have exact thread references | PASS | ALS-016/017/027 |
| 14 | Source classifications and access dates accurate | PASS | Source register |
| 15 | No real-time in-game chat introduced | PASS | §11, §19; validator group 6 |
| 16 | No Discord bot/API/OAuth/linking/role sync introduced | PASS | §11; `DD-147`; validator group 6 |
| 17 | Discord remains external to authoritative game-state decisions | PASS | §11.3; §6.2 |
| 18 | `D-133` and `DD-147`–`DD-150` consistent | PASS | 04 register; validator group 6 |
| 19 | `REQ-534`–`REQ-617` classified and traceable | PASS | Register count; validator group 7 |
| 20 | `UD-039`, `UD-040`–`UD-049` recorded | PASS | 05 register; validator group 7 |
| 21 | Stage 2 handoff has one next action | PASS | Handoff §1/§10; validator group 8 |
| 22 | Other handoff and roadmap files agree | PASS | Continuity set; validator group 8 |
| 23 | Alliance-specific validator implemented and documented | PASS | `09A_validate_alliance.py` |
| 24 | Negative and clean self-tests run | PASS | §23.4 |
| 25 | Prompts 01–08C and Global Trade intact | PASS | No owning document edited; validator group 5 |
| 26 | Required documentation updated | PASS | §22 and project change log |
| 27 | No gameplay or communication implementation introduced | PASS | No code outside `qa_backups` |
| 28 | 09B authorized only after 09A acceptance | PASS | Handoff marks 09A accepted, 09B next |

### 23.4 Validation record

**Automated checks** (run 2026-10-31; full list in [log §33](../../stage-2/06_stage_2_progress_log.md)):

- `python docs/qa_backups/09A_validate_alliance.py` — **790 checks, 0 failed**. It checks structure, identifier existence, classification, evidence presence, stale pairs, ownership, Discord exclusions, permissions, sources and handoff agreement.
- `python docs/qa_backups/test_09A_alliance_validator.py` — **16 tests, OK**: one clean fixture and 15 declared negative fixtures (AX-01/REQ-012, AX-06/REQ-530, AX-09/REQ-012, AX-16/REQ-532, nonexistent REQ, supporting-as-direct, missing evidence, Economy-to-Alliance, leader-consents, Discord bot, real-time chat, two next prompts, unsourced permission, forum root marked primary, UD-039 no-object path mislabelled as option (a)).
- Existing validators after the documentation edits: `09_validate.py` **358/358**; `validate_final.py` **ALL CHECKS PASSED**; `test_decision_registers.py` **12 tests OK**; `test_next_action.py` **23 tests OK**; `verify_politics_numbers.py` **879/879**; `verify_market_workflows.py` **ALL CHECKS PASSED**; `verify_diplomacy_numbers.py` **9 groups, 0 failed**; `verify_diplomacy_workflows.py` **17 groups, 0 failed**; `verify_market_numbers.py` **ALL CHECKS PASSED**; `verify_economy_numbers.py` **164/164**; `verify_city_numbers.py` **267/267**.

**Honest limit.** The validator proves structure and the presence of evidence text. It does not prove that a sentence is a correct reading of a requirement. That judgement is recorded per AX in `09A_alliance_reference_review.md` and is a single-author self-review, not an independent review.

---

## 24. Prompt 09A-D correction record — Final Alliance Treasury Storage Traceability Correction

**Scope:** Focused correction pass on AX-08 requirement classifications, relationship count reconciliation, and validation hardening. No gameplay, schema, API, screen, Discord integration or communication infrastructure was created. No existing Diplomacy, Economy, City, Market, Global Trade or Military rule was changed.

### 24.1 Defects corrected

| # | Defect identified | Correction | Where |
|---|---|---|---|
| 1 | AX-08 misclassified national warehouse requirements `REQ-141` and `REQ-142` as `DIRECT DEPENDENCY` for Alliance Treasury storage limits. | `REQ-141` (ECN-120) and `REQ-142` (ECN-124) reclassified as `RELATED CONSTRAINT`. They govern national inventory storage and overflow blocking, not Alliance Treasury capacity. `REQ-176` retained as `DIRECT DEPENDENCY` for separate audited pools, no minting, and integrity. An explicit `NO EXISTING REQUIREMENT` row was added for alliance pool capacity under `UD-046`. | Matrix §2, §3, §4, §5.2, §6, §7; review record §3, §4 |
| 2 | Stale relationship totals across documentation. | Reconciled all relationship counts to 77 total: 39 DIRECT DEPENDENCY, 19 RELATED CONSTRAINT, 6 SUPPORTING CONTEXT, 13 NO EXISTING REQUIREMENT rows across 13 AX records. | Matrix §3; review record §4; roadmaps, logs and handoffs |
| 3 | Treasury capacity owner decision traceability gap. | Preserved `UD-046` as Open for Prompt 09B; clarified description to explicitly cover alliance-pool storage capacity, over-capacity deposit handling, withdrawals, and dual approval; added `AX-08` cross-reference. | `05_unresolved_design_decisions.md` UD-046 |
| 4 | Validator did not detect the AX-08 semantic error. | Added group `12-treasury-storage` in `09A_validate_alliance.py` verifying AX-08 structure, classifications, evidence, open `UD-046` reference, prohibited national-warehouse substitution, and exact count reconciliations. Added 11 negative self-test fixtures in `test_09A_alliance_validator.py`. | `09A_validate_alliance.py`, `test_09A_alliance_validator.py` |

### 24.2 National warehouse versus Alliance Treasury distinction

1. **National warehouse (`ECN-120` / `REQ-141`):** Governs national inventory with shared capacity `W` across 11 resources for a single nation. It informs future design but does not establish Alliance Treasury capacity.
2. **National overflow blocking (`ECN-124` / `REQ-142`):** Governs national production batches and market purchases, blocking them when `free_space < output`. It does not govern alliance deposits, which are member-to-pool value transfers.
3. **Alliance Treasury (`REQ-176`):** Establishes that alliance pools are separate audited pools with their own ledger and permissions, and may not mint or bypass restrictions. It does not define a numerical capacity limit or deposit overflow behaviour.
4. **Alliance pool capacity decision (`UD-046`):** The question of whether an alliance pool has a capacity limit, what that limit is, and how over-capacity deposits are handled is an unresolved design decision scheduled for Prompt 09B in coordination with Economy.

### 24.3 Acceptance criteria (09A-D)

All 25 mandatory acceptance conditions are satisfied:
1. Current canonical Economy, City and Alliance documents inspected.
2. REQ-141 checked against actual scope (national warehouse).
3. REQ-142 checked against actual scope (national overflow).
4. REQ-176 checked against actual scope (separate audited pool).
5. AX-08 distinguishes national warehouse storage from Alliance Treasury capacity.
6. REQ-141 classified correctly as RELATED CONSTRAINT.
7. REQ-142 classified correctly as RELATED CONSTRAINT.
8. REQ-176 remains DIRECT DEPENDENCY for separate-pool integrity.
9. Alliance-pool capacity explicitly recorded as NO EXISTING REQUIREMENT under UD-046.
10. UD-046 preserved as Open and unresolved for Prompt 09B.
11. Wider economic integrations (AX-06, AX-07, AX-10, AX-11, AX-12, AX-17, AX-18, AX-26) verified.
12. No unsupported Alliance Treasury behaviour invented.
13. Relationship totals recalculated: 39 DIRECT, 19 RELATED, 6 SUPPORTING, 13 NO EXISTING REQUIREMENT (77 total).
14. All summaries and cross-references agree.
15. Validator detects AX-08 defects.
16. Negative and clean validator fixtures pass.
17. D-133 and DD-147 through DD-150 remain consistent.
18. REQ-534 through REQ-617 remain Proposed. *(09B-E reconciliation note, 2026-11-01: this records the 09A-time status only. After Prompt 09B and the 09B-E correction the 84 rows are 71 Provisional, 12 Open and 1 Deferred; none is approved.)*
19. UD-039 and UD-040 through UD-049 preserved.
20. Prompts 01–08C and Global Trade intact.
21. All required project documentation updated.
22. Roadmap and handoff agree on Prompt 09A acceptance.
23. Prompt 09B remains blocked until Prompt 09A-D acceptance.
24. No gameplay or communication implementation introduced.
25. All reported validation commands reproducible.

### 24.4 Validation record

- `python docs/qa_backups/09A_validate_alliance.py` — all checks PASS.
- `python docs/qa_backups/test_09A_alliance_validator.py` — 27 tests, OK (1 clean fixture + 26 negative fixtures).
- Existing regression validators run and pass clean.

---

## 25. Prompt 09A-E correction record — Final AX-08 Wording Corrections, Treasury Policy Status, Handoff Reconciliation, and Acceptance Closure

**Scope:** Narrowly scoped final correction pass on Prompt 09A addressing four issues identified in the archive audit: (1) correcting the AX-08 summary to remove the implication that national warehouse capacity applies to Alliance Treasury pools; (2) removing the unapproved failure/recovery claim that over-capacity deposits are cleanly rejected and clarifying that deposit policy and capacity remain unresolved under `UD-046` for Prompt 09B; (3) reconciling four stale current-status references in the Stage 2 handoff and Master Game Design Bible outline that cited Prompt 09A acceptance after 09A-C; and (4) reconciling the validator check count from the stale 829 to the actual measured count. No gameplay, schema, API, screen, Discord integration or communication infrastructure was created. No existing Diplomacy, Economy, City, Market, Global Trade or Military rule was changed.

### 25.1 Defects corrected

| # | Defect identified | Correction | Where |
|---|---|---|---|
| 1 | AX-08 summary in integration matrix §2 stated "Hold pooled resources within Economy capacity", which could imply national warehouse limits govern Alliance Treasury pools. | Replaced with explicit statement: "Determine whether a separately approved Alliance Treasury capacity rule is required; national warehouse capacity does not establish Alliance-pool capacity." | `09A_alliance_integration_matrix.md` §2 row AX-08 |
| 2 | AX-08 failure/recovery field stated "Reject over-capacity deposit cleanly", assuming an unapproved deposit policy. Resource impact was abbreviated as "Capacity only". | Replaced failure/recovery with explicit statement that over-capacity deposit behaviour is unresolved under `UD-046` (do not assume rejection, partial acceptance, queuing, resource loss or any other outcome; Prompt 09B must define policy). Replaced resource impact with clarification that pool capacity is unestablished, national warehouse capacity cannot be substituted, and impact is subject to `UD-046`. | `09A_alliance_integration_matrix.md` §4 row AX-08 |
| 3 | Four stale current-status references in Stage 2 handoff and Master Game Design Bible outline cited Prompt 09A acceptance after 09A-C instead of current baseline. | Reconciled all current-status references across `00_stage_2_handoff.md`, `02_master_game_design_bible_outline.md`, `AI_CONTEXT.md`, `AI_HANDOFF.md`, `ROADMAP.md`, `PROJECT_PROGRESS.md`, and `01_stage_2_prompt_roadmap.md` to reflect Prompt 09A acceptance after Prompt 09A-E (with 09A-D substantive treasury storage correction), while preserving historical completion entries. | Handoff and continuity files |
| 4 | Stale validator check count (829) reported in handoff and progress log. | Re-ran validator, measured actual check count, and reconciled all occurrences across the progress log, Stage 2 handoff, and research records to match the exact measured execution count. | Progress log §34/§35, handoff §2/§10 |

### 25.2 Treasury policy status under UD-046

- **National warehouse capacity (`ECN-120` / `REQ-141`):** Governs national inventory. It does not establish Alliance Treasury capacity.
- **National overflow blocking (`ECN-124` / `REQ-142`):** Governs national production and trade purchases. It does not govern alliance deposits.
- **Alliance Treasury separate pool (`REQ-176`):** Governs separate audited pools and resource integrity. It does not define numerical storage limits or deposit overflow behaviour.
- **Over-capacity deposit policy (`UD-046`):** Unresolved. Prompt 09B is responsible for defining the policy under `UD-046` in coordination with the Economy system owner. No outcome (rejection, partial acceptance, queuing, loss, redirection, auto-expansion) is approved.

### 25.3 Acceptance criteria (09A-E)

All 23 mandatory acceptance conditions from Prompt 09A-E are satisfied:
1. Current AX-08 and canonical Economy requirements inspected.
2. AX-08 summary no longer implies national warehouse capacity governs Alliance Treasury capacity.
3. AX-08 over-capacity deposit behaviour explicitly marked unresolved.
4. AX-08 resource impact field does not present unapproved capacity rules as established.
5. REQ-141, REQ-142, and REQ-176 classifications remain correct (RELATED, RELATED, DIRECT).
6. UD-046 remains Open and referenced correctly.
7. All relevant AX-08 wording searched and reconciled.
8. Stale current-status references to 09A-C corrected in Stage 2 handoff.
9. Stale current-status references to 09A-C corrected in Master Game Design Bible outline.
10. Historical completion entries preserved accurately.
11. AI_CONTEXT and other current-state documents checked and reconciled.
12. Alliance validator rerun and actual count recorded.
13. Stale 829 count corrected wherever it represents current validation evidence.
14. Validator catches AX-08 wording and approval-state errors.
15. Negative and clean self-tests pass.
16. Relationship counts remain accurate and reconciled (77 total: 39 direct, 19 related, 6 supporting, 13 no-existing across 13 AX records).
17. No-chat and Discord decisions remain intact (D-133, DD-147..DD-150).
18. Candidate Alliance requirements remain correctly classified (84 Proposed, REQ-534..REQ-617).
19. Earlier Prompts 01–08C and Global Trade remain intact.
20. All affected documentation and handoff files updated.
21. Every project current-status record agrees on Prompt 09A completion and Prompt 09B next.
22. No gameplay or communication implementation introduced.
23. All reported validator commands and results reproducible.

---

## 26. Prompt 09A-F correction record — Final Project Status Reconciliation, Handoff Validation, and Alliance Research Acceptance Closure

**Scope:** Final project-wide status reconciliation and handoff validation pass for Prompt 09A. Addressed remaining stale current-status references identified in the project audit: reconciled all current-state handoff and continuity references to reflect Prompt 09A acceptance after Prompt 09A-F (with 09A-D and 09A-E substantive corrections), preserved all historical completion records (§23 09A-C, §24 09A-D, §25 09A-E), strengthened documentation validator protection with negative self-tests, and established formal acceptance closure authorizing Prompt 09B as next. No gameplay, schema, API, UI, Discord integration or communication infrastructure was created. No existing Diplomacy, Economy, City, Market, Global Trade or Military rule was changed.

### 26.1 Defects corrected

| # | Defect identified | Correction | Where |
|---|---|---|---|
| 1 | Stale current-status references in `AI_CONTEXT.md` (lines 3, 20, 33, 118, 128) cited Prompt 09A acceptance after 09A-D. | Reconciled all current-status lines in `AI_CONTEXT.md` to reflect Prompt 09A acceptance after Prompt 09A-F, Prompt 09B next, and updated progress-log index to include §36. | `AI_CONTEXT.md` lines 3, 20, 33, 118, 128 |
| 2 | Stale current-status references in `AI_HANDOFF.md` (lines 3, 22, 286, 290, 392, 404, 438) cited Prompt 09A acceptance after 09A-D or 09A-E without complete handoff instructions. | Reconciled all current-status lines in `AI_HANDOFF.md` to reflect Prompt 09A acceptance after Prompt 09A-F, Prompt 09B next; added explicit Prompt 09B instructions regarding research inheritance, UD-046, AX-08, and communication boundaries. | `AI_HANDOFF.md` lines 3, 22, 286, 290, 392, 404, 438 |
| 3 | Stale current-status statement in `01_stage_2_prompt_roadmap.md` line 4 cited Prompt 09A acceptance after 09A-D. | Reconciled opening status and row 09 to reflect Prompt 09A acceptance after Prompt 09A-F, Prompt 09B next, citing log sections `[§32]–[§36]`. | `01_stage_2_prompt_roadmap.md` lines 4, 24, 242 |
| 4 | Stale current-status statements in `06_stage_2_progress_log.md` header lines 4, 6, 8, 34 cited 09A-D. | Reconciled opening summary and prompt status table to Prompt 09A accepted after Prompt 09A-F, Prompt 09B next; added Section 36 for Prompt 09A-F completion. | `06_stage_2_progress_log.md` lines 4, 6, 8, 34, §36 |
| 5 | Validator lacked automated detection for stale current-status discrepancies across continuity files. | Extended validator with group `13-current-status` verifying cross-document status agreement, presence of 09A-F closure, and absence of stale acceptance claims; added 10 negative self-test fixtures. | `09A_validate_alliance.py`, `test_09A_alliance_validator.py` |

### 26.2 Preserved Alliance research baseline

- **AX-08:** REQ-141 RELATED CONSTRAINT, REQ-142 RELATED CONSTRAINT, REQ-176 DIRECT DEPENDENCY, alliance pool capacity NO EXISTING REQUIREMENT, UD-046 OPEN, over-capacity deposit behaviour UNRESOLVED.
- **Relationship Totals:** Exactly 77 relationship rows (39 direct, 19 related, 6 supporting, 13 no-existing across 13 AX records).
- **Candidate Requirements:** 84 Proposed requirements (`REQ-534`–`REQ-617`), none approved. *(09B-E reconciliation note, 2026-11-01: this records the 09A-time baseline. After Prompt 09B and the 09B-E correction the same 84 rows are 71 Provisional, 12 Open and 1 Deferred; none is approved and none was deleted or renumbered.)*
- **External Communication Boundary:** `D-133` and `DD-147`–`DD-150` strictly preserved (no in-game chat, no DM, no Discord bot, no API sync).

### 26.3 Acceptance criteria (09A-F)

All 27 mandatory acceptance conditions from Prompt 09A-F are satisfied:
1. Current project documents and validators inspected.
2. AI_CONTEXT current-status references reconciled.
3. AI_HANDOFF current-status references reconciled.
4. Stage 2 prompt roadmap reconciled.
5. Stage 2 progress-log summary reconciled.
6. Stage 2 handoff reconciled.
7. Master Game Design Bible B-09 status reconciled.
8. Main roadmap next-action status reconciled.
9. Project progress next-action status reconciled.
10. Historical Prompt 09A-C, 09A-D and 09A-E entries remain intact.
11. No stale current-status statement remains in project documentation.
12. Prompt 09A accepted status has actual 09A-F completion record.
13. Prompt 09B is authorized only after successful acceptance.
14. AX-08 classifications and wording remain correct.
15. UD-046 remains OPEN.
16. Over-capacity deposit behaviour remains unresolved.
17. No-chat and Discord decisions remain intact.
18. All candidate Alliance requirements remain accurately classified.
19. Existing Prompt 01–08C work remains preserved.
20. Global Trade scope and gates remain intact.
21. Validator detects stale current-status discrepancies.
22. Historical records do not generate false-positive stale-status failures.
23. Negative self-tests pass.
24. Clean fixture passes.
25. Validator commands and actual measurements reported accurately.
26. All affected documentation files updated.
27. No gameplay or communication implementation introduced.
