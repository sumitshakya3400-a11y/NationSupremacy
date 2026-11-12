# 13A — UI design principles, visual direction and application architecture

**Prompt:** Stage 2 Prompt 13A — UI research, architecture and design foundations (Deliverables A and B).
**Created:** 2026-11-11. **Reconciled:** 2026-11-12 (Prompt 13A-C1 semantic cross-reference reconciliation). **Status:** design foundations; **no implementation, no visual asset, no component built** (roadmap Prompt-13 guardrail: "Specifications only — no frontend code in Stage 2").
**Authority basis:** [13A Politics & War UI research](13A_politics_and_war_ui_research.md) (evidence) · the accepted B-02…B-12 rulebooks (requirements) · [AUTONOMOUS_DECISION_POLICY.md](../../AUTONOMOUS_DECISION_POLICY.md) (D-014) · decisions **D-198…D-205**.
**Companions:** [master screen inventory](13A_master_screen_inventory.md) · [responsive and design-system foundations](13A_responsive_and_design_system_foundations.md) · [requirements, open questions and acceptance](13A_ui_requirements_open_questions_and_acceptance.md)

---

## 1. Scope and standing

This document establishes the authoritative UI *foundation*: principles (§2–§3), the application shell and navigation architecture (§4–§6) and high-level application-state behaviour (§7). It translates the P&W benchmark evidence (`13A-FND/BP/DR` rows) and the existing rulebook obligations into an architecture a later prompt can specify screens against. It approves nothing that belongs to the owner: final brand identity, colours and typography *choices* remain reserved (`13A-OQ-001/002`; D-203). Every structural recommendation here is a Category-B design position (recorded in DECISIONS.md) or a provisional recommendation labelled for 13B/owner review.

**Non-goals:** pixel layouts, component APIs, framework choice, implementation, testing claims, or any change to a game rule. Where this text says a screen "shows" a value, it specifies *presentation duty*, not production behaviour.

## 2. Design principles — primary (13A-PR-01…08)

Derived from the project's own priority order (policy §4: constraints → security/fair play → coherent gameplay → simplicity → free-first → performance → transparency) and P&W evidence read *critically*.

| ID | Principle | Consequence for the UI |
|---|---|---|
| `13A-PR-01` | **The turn is the heartbeat** | Every authenticated surface communicates the two-hour UTC cadence: countdown to next boundary, which phase an action lands in (P0–P7), and whether it is queued, reserved or settled. Nothing may imply real-time urgency (DP-002; no attendance rewards, AP-001). |
| `13A-PR-02` | **Legibility before density, density before decoration** | The data-rich genre is embraced (P&W's long-page density is an observed norm, `13A-FND-003/027`) but each screen must pass the 60-second comprehension test inherited from Report 07 §15.6 and DP-004. Progressive disclosure, never hidden state. |
| `13A-PR-03` | **Every number states what kind of number it is** | The six number types (ECN-177; D-056) are a UI law: current, reserved/committed, submitted order, forecast, completed transaction, historical record are visually distinct registers; a forecast is never rendered with current-state weight (URB-152, DIP-155). |
| `13A-PR-04` | **Explain, don't teach-around** | Rule explanation lives in-context (definitions, cause chains, previews — `13A-DR-010`), because the benchmark shows knowledge spilling off-platform and that spilling is a player-frustration source (F-010, `13A-FND-029`). |
| `13A-PR-05` | **Transparency by rule, opacity by design** | What may be disclosed is decided by visibility classes (TR-021, D-027 k=5, PRV/B-12, WAR-148–150, D-030), never by convenience. Relations transparent, intent opaque (DP-004 boundary). Suppressed aggregates display their suppression state informatively (`13A-DR-006`). |
| `13A-PR-06` | **Absence is a supported mode** | Re-entry surfaces (digest, inbox, "since you last looked") are first-class; every consequential settlement produces a readable explanation whether or not the player watched it (TR-089 digest-first; REQ-022 re-entry summary; F-015/F-016 class). |
| `13A-PR-07` | **One grammar across all systems** | The P&W strength (`13A-FND-024`) formalized: one table/filter/pagination idiom, one status vocabulary, one action lifecycle display (`13A-BP-004`), so learning one screen transfers to all. Consistency is a fairness feature: misreading a state is a player-harm vector. |
| `13A-PR-08` | **Serious tone, plural paths** | The atmosphere is a professional geopolitical *administration* surface — nation records, ledgers, treaties — not arcade chrome; and no path (economic, diplomatic, military, cultural-deferred) may be visually privileged over another (DP-001; CX-5). |

## 3. Secondary principles (13A-PR-09…16) and visual direction

| ID | Principle | Note |
|---|---|---|
| `13A-PR-09` | Confirmation-first | Irreversible or boundary-effective actions show exact effect, cost, cooldown and named failure path before commit (`RRL-006`, `WAR §12.3`, `08C §12.3`; `13A-DR-009`, `13A-DR-018`). |
| `13A-PR-10` | The disabled control explains itself | "Why not" text before the click, not after the error (08C §12.7; CN show-unaffordable pattern `13A-BP-028`). |
| `13A-PR-11` | State never lives only in the UI | Server truth drives presentation; the UI may show pending intent but never grants permission by render (URB-135; consistency audit §4.11). |
| `13A-PR-12` | Colour + glyph + text for every status | Independent NS accessibility requirement (`13A-DR-015`, `DMP-164`, `REQ-321`, WCAG 2.2 AA design intent); bounded against `13A-FND-017/031` (P&W tables pair `Alliance` text with `Color` columns, while visual CSS swatch redundancy is unverified). |
| `13A-PR-13` | Deep-link everything | Every object (nation, alliance, war, treaty, offer, proposal, event instance) has a stable addressable view — P&W's most durable structural asset (`13A-FND-001/023`). |
| `13A-PR-14` | Long-session comfort | Dense default views, persistent context strip, low-glare readable palette direction; keyboard navigation and visible focus from the start (§ design-system doc). |
| `13A-PR-15` | Nothing political happens off-screen — and nothing happens off-screen at all | Every rule that can produce a player-facing consequence must have a screen or digest that discloses it ("Done when: every Stage 2 rule has a place a player can see and act on it", roadmap Prompt 13). |
| `13A-PR-16` | Honesty about uncertainty | Provisional values, insufficient samples and simulation states (`INSUFFICIENT_SAMPLE` MKT-110; PROVISIONAL_BLOCK D-194) render as their named state, never disguised as zero or as fact. |

### 3.1 Visual identity evaluation (alternatives considered, per instruction §6)

| Direction | Reading for NS | Verdict |
|---|---|---|
| **A. Modern geopolitical strategy interface** (dark editorial map-room, newsroom typography) | Matches "community of nations" tone; risks looking like a real-world news product and under-serving the fictional register; heavy styling threatens the ₹0/simple-build constraint (performance) and the genre's data-first users | Candidate *finish layer*, not the foundation |
| **B. Nation administration interface** (records, ledgers, forms, registers — the "state paperwork" idiom) | Directly fits the six number types, chronicle, ledgers, treaties, rankings-as-registers (SIM-012: "standing registers instead of one ladder"); communicates seriousness without arcade noise; cheapest to build accessibly | **Recommended primary direction** |
| **C. Strategic command dashboard** (panels, alerts, ops boards) | Fits the War Operations Board and command surfaces specifically; wrong as the whole product (overstates military centrality against DP-001/DP-006) | Reserved for war/command screens (already named: Nation-owner War Operations Board) |
| **D. Data-rich management interface** (generic enterprise BI) | Describes B and C adequately; adds no identity | Rejected as framing — it is a means, not a brand |

**Recommendation (provisional, owner-reviewable):** foundation = **B (nation administration)** as the pervasive register/ledger grammar; **C** scoped to the command surfaces; **A** treated as a later *theming* question owned by the owner together with brand assets (`13A-OQ-001`: final palette, logo, typographic identity are owner-reserved; this document deliberately proposes no brand colours). Typography, spacing and colour *principles* are in the design-system foundations document and are Category-B provisional; the concrete *choices* are `13A-OQ` items.

### 3.2 Status and alert conventions (project-wide vocabulary)

A single register of tones, each defined semantically and re-used everywhere (full token table in the design-system document):

- `informational` — settled facts, digests, changelog-style notes (P&W changelog pattern `13A-BP-012`).
- `pending` — submitted, reserved, queued, awaiting boundary or counterparty (aligns with the three-class timing contract, B-02 §17; `PENDING` display label per URB-063/066).
- `success` — settlement/commit completed (never confusable with pending).
- `warning` — degradation, low stability/approval bands, maintenance-lacking chains (`UNMAINTAINED`), protection expiry approaching.
- `danger` — active loss, sanctioned state, FAILED-turn player-facing notice (TR-080).
- `locked/denied` — permission, pair-restriction, political-state (`TRANSITION`/`CRISIS`) or security block *with reason* (NET-023 player-visible pair status; MOD/EVD claim vocabulary `suspected / under review / confirmed / inconclusive` is reserved for B-12 notices and may not be reused for game states — FP-033/EVD-009).
- `suppressed` — k=5 non-disclosure state with its explanation (`13A-DR-006`).

## 4. Global application structure (Deliverable B / 7.1)

**The shell (D-201).** One browser application frame, present in every game state including logged-out previews (validated against `13A-BP-001` / `13A-SRC-017`):

```
+---------------------------------------------------------------+
| A. Identity strip : nation crest+name, leader, treasury,      |
|    power summary, protection badge, TURN COUNTDOWN (UTC)      |
| B. Primary nav    : section tabs (bounded set, §5)            |
| C. Alert bar      : global alert count + priority alerts      |
| D. Search / quick-go  (typeahead to objects & screens)        |
+---------------------------------------------------------------+
| E. Breadcrumb / context line (object hierarchy + governing    |
|    rule anchor, 13A-DR-009/010)                               |
| F. PRIMARY CONTENT AREA — one screen; internal tabs for       |
|    same-object views                                          |
| G. CONTEXT PANEL (right, persistent where screen width         |
|    allows): object facts, related objects, recent events      |
+---------------------------------------------------------------+
| H. Footer: help entry, support/report, terms, changelog       |
+---------------------------------------------------------------+
```

- **A** carries persistent strategic information (the P&W resource-strip lesson at zero-state: the frame never collapses). NS contents are visibility-class-checked (e.g. exact treasury is class-P private; band display permitted where rules allow).
- **C** is presentation-tier over the existing notification events (no new notification channel; REQ-731; `13A-DR-011`): counts and priority, never new facts.
- **D** is quick navigation only (§5); deep-link targets come from `SCR` registry.
- **G** keeps cross-system context visible while acting (e.g. composing a trade offer shows pair history within visibility limits; declaring war shows protection/treaty blocks) — the situational-awareness function P&W serves with its profile pages, served here *per task*.
- **Help and support access (instruction 7.1):** every screen carries the in-context explanation affordance (`13A-PR-04`) and a "governing rule" anchor (`13A-DR-009/010`); account-level support/report/appeal entry points sit in the shell footer/account menu regardless of current screen (B-12 intake surfaces, MOD-002/013).
- **Administration surfaces live outside this shell** with separate role-gated entry (`13A-DR-013`; ADM reviewer views) — ordinary players never traverse admin chrome and admin views never replace the player shell (least privilege, D-042; no "admin view" in diplomacy per DIP-121 discipline).

**Why this supports long sessions:** the countdown + alert bar + inbox compress the "check-in" loop to seconds; the context panel avoids page ping-pong for one decision cycle; the frame's stability means the player's mental map (where am I, what changed, what's pending) is answerable without re-reading (NS `13A-DR-001` / `13A-DR-005` / `13A-DR-018` answering `13A-FND-026/027` logged-out catalogue and long-page density observations).

## 5. Navigation architecture (Deliverable B / 7.2)

### 5.1 Primary navigation (D-201)

Bounded top-level set, ordered by decision frequency, each opening on a *task* surface where one exists:

| # | Section | Covers systems | Opening surface |
|---|---|---|---|
| 1 | **Home** | digest, inbox, alerts, world snapshot, quick stats | Command Digest (B-02 TR-089; SYS-017) |
| 2 | **Economy** | treasury, budget, production policy, resources, trade (market + directed) | Treasury dashboard (ECN-176 question list) |
| 3 | **Cities** | city list/selector, infrastructure, buildings, construction queue, research | National development overview (URB-031: twelve cities ≈ one screen) |
| 4 | **Politics** | government structure, approval/stability, policy axes, elections, constituencies | Political panel with state banner (DMP-256/268) |
| 5 | **Foreign** | diplomacy posture, treaties, pair screens, alliance surfaces | Diplomatic overview (six required views, 08C §12.2) |
| 6 | **War** | military readiness, operations, war list, War Operations Board | Military overview (owner visibility classes) |
| 7 | **World** | events, objectives, standings, progression, chronicle, network view | World overview = Events Centre + Network View entry |
| 8 | **Account** | profile, nation management (reroll), privacy, security, reports/appeals, support | Account home |

Rationale vs P&W: keeps its flat findability (`13A-FND-023`) but replaces the 12-item world-catalogue menu with an 8-section *player-role* taxonomy; Trade is folded into Economy and Diplomacy/Alliance into Foreign because NS journeys (10 FPJ + 20 B-03 + 22/17/25 workflow journeys) treat them as one decision context; **no World Map item** (fixed mapless constraint; the Network View lives under World). Section counts and the economy/war split are provisional pending 13B journey-testing.

### 5.2 Secondary, contextual and cross-navigation

- **Section-internal tabs** for same-object views (profile tabs mirror the public-section model of `13A-SRC-004` in NS ordering).
- **Breadcrumbs** whenever depth ≥ 2 (`World > Conflicts > War 2739562 > Battle`) — each crumb deep-links (PR-13).
- **Contextual side panel** (shell G) for related objects; never carries data above its visibility class.
- **Cross-system links** are first-class object links: any nation/alliance/war/treaty/offer/event identifier renders as a link to its view subject to permissions (the deep-link grammar from `13A-FND-001`).
- **Search/quick-go:** two modes only — jump-to-object (typeahead over IDs/names) and jump-to-screen (command palette of section destinations). *Not* a full-text engine; the corpus that would need indexing doesn't exist (§13A-OQ-009).
- **Inbox/queue** is a destination, not a modal: ordered by due-boundary, grouped by type, each row deep-links to its action screen (`13A-DR-001`).

### 5.3 Overlays discipline

- **Modal dialogs** only for: confirmation-before-commit (PR-09), destructive-action exact-phrase confirmation (RRL-006 reroll pattern), recovery-code entry (D-041), and blocking reason disclosures. A modal may never be the *only* place a state or history exists (P&W modal lessons inverted: modal content must remain reachable on a page).
- **Drawers** for read-mostly context without losing the parent screen (member picker, cause-chain detail). Drawer content must be deep-linkable as a page on small viewports (responsive doc).
- **Non-modal popovers** for definitions/tooltips only.

## 6. Application states (Deliverable B / 7.3)

High-level behaviour only; per-screen states are 13B work. Grounded in existing failure/posture vocabularies (WPF/DPF/WRF/MKF/ALF/AT-E/FR postures) — the UI maps onto them, never invents parallel ones.

| State | Shell behaviour | Rule anchors |
|---|---|---|
| **Loading** | Frame renders skeleton *within* the persistent shell; no full-page spinner that hides context | PR-02 |
| **Empty (new nation)** | Real frame with zeros ("awaiting first turn" NAT-016), guided objectives panel, no stub UI | `13A-BP-001`, `13A-SRC-017` (`0.00` real frame), D-063 start, ONB windows |
| **Empty (no data in section)** | Explanation of why it's empty + what would populate it + governing rule link | `13A-PR-10` |
| **Error / failed request** | Named failure code from the owning system's catalogue + player-language cause + safe retry (idempotency SEC-014 discipline; "unknown — retrying" TR-075) | B-02/B-07/B-08/B-09/B-10/B-11 catalogues |
| **Permission-denied** | Distinct from error: state *kind* of restriction (role, visibility class, pair restriction, political state, suspension) with the disclosure text the owning rules mandate — never more precise than the rules allow (NET-050 no public accusation; PRV-019) | D-034 states, REQ-553/645 |
| **Blocked-by-rule** | Disabled control + inline reason + link to rule ("requires 60-turn cooldown since…") — the CN show-with-reason pattern (`13A-BP-028`) | PR-10 |
| **Disconnected / stale** | Explicit "data as of slot N" staleness label; reads allowed where visibility permits; writes clearly disabled | TR-049 published/readable; cadence honesty |
| **Action success** | Receipt view: submitted state, where it lands in the phase order (P-phase badge), and what will *not* change until the boundary | B-02 §17 timing contract; ECN-134-138 |
| **Pending action** | Persistently visible in inbox + on its object page with `pending` tone; cancellable exactly where rules allow, with the cancellation state named | three-class contract; MKT/DIP lifecycles |
| **Confirmation-required** | Modal with exact effect, cost, cooldown, irreversible-phrase where destructive | PR-09, RRL-006 |
| **Time-sensitive** | Expressed in **turns and boundary UTC**, never wall-clock countdown theatrics; protection/expiry bands shown as states, with the *state* not a timer as the source of truth | PR-01; ONB-020/022 protection visibility-only; WAR execution-time protection |
| **Suppressed-data** | `suppressed` tone with k=5 explanation sentence; counts that would leak are hidden as "not disclosed" not "0" | D-027, MKT-110 discipline |
| **PROVISIONAL_BLOCK** | Where a rule branch awaits an owner/legal/Prompt-14 value, the UI shows the *specified provisional branch* exactly as the register defines it, labelled provisional | D-194 |

## 7. How this section-level architecture honours the boundaries already owned by other systems

- The **War Operations Board** (owner-only, B-10 visibility) and the **restricted Alliance management interface** (management/coordination only, no military command, no member OP spending, no private war visibility) remain *separate surfaces*; the shell offers both but never merges data across them (roadmap Prompt-13 boundary paragraph; AX-18; UD-047/UD-049 preserved).
- **Screen ≠ rule:** every presentation duty here traces to an existing rule; where no rule authorizes a disclosure, the disclosure does not exist (`13A-PR-15` runs one way: rules create surfaces; surfaces never create rules — 16 audit §4.11).
- **No chat, no Discord, no external coordination surfaces** (D-133; `13A-BP-017`): announcements/notice-board candidates remain governed by UD-049 and ALL-162..168, i.e. UI may present what B-09 allows, nothing more.
- **Accessibility and responsive** obligations attach at architecture level (§4 layout priorities; see companion document) from day one (`13A-DR-012`, `13A-DR-015`): visual CSS swatch redundancy and P&W mobile rendering were unverified in logged-out HTML (`13A-FND-031`, `13A-SRC-036`), while Cyber Nations shipped a mobile-friendly mode later via opt-in update (`13A-SRC-029`).
