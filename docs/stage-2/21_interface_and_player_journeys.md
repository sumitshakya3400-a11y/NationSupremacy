# B-13 — Complete screen and component specifications

**Prompt:** Stage 2 Prompt 13B — complete screen and component specifications (2026-11-13).
**Status:** COMPLETE at the specification/documentation level. **No screen, component, framework, route, migration or runtime behaviour exists.** Every statement below is a presentation specification; none is an implementation, a test result, an owner acceptance of a game rule, or evidence of WCAG conformance.
**Authority basis:** the owner's Prompt 13B instruction (2026-11-13), which records Prompt 13A as **OWNER ACCEPTED / COMPLETED**; [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (D-014); the accepted B-02…B-12 rulebooks; the five accepted Prompt 13A deliverables under [`research/13A_*.md`](research/13A_master_screen_inventory.md); decisions **D-198…D-205** and the new **D-206…D-219**.
**Companions (same `21_` serial family; D-206):**
- [`21_screen_specifications.md`](21_screen_specifications.md) — the complete A–K specification of every `SCR-001`…`SCR-100`.
- [`21_component_specifications.md`](21_component_specifications.md) — the complete `UI-CMP-001`…`UI-CMP-090` component catalogue and the eight `OVL-` overlays.

**Reading rule.** This file is the authoritative register for screen identity, classification, navigation, responsive duty, accessibility duty, traceability and the B-13 requirement block. The screen companion is the authoritative field-by-field screen body. The component companion is the authoritative component body. No register is duplicated in two files: each companion links back to the registers here, and this file links out to each screen and component body by anchor.

**Predecessor reconciliation.** Prompt 13A's `P13A-10` PARTIAL recorded compressed inventory fields and rule-family-level requirement links; Prompt 13B resolves that finding by expanding all 100 screens into the A–K template (13B-01…13B-05). The 13A acceptance tally **23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED** and the 13A documents are preserved unchanged; the owner's acceptance of Prompt 13A is recorded by the Prompt 13B instruction, not invented here.

---

## 1. Document authority, purpose and scope

### 1.1 What this document does

It defines, for every registered screen: identity, purpose, entry and navigation, information hierarchy, layout, data presentation, controls and their preconditions, screen relationships, desktop/tablet/mobile presentation, governing references, and restrictions. It defines every reusable component with its structure, fields, states, responsive behaviour, accessibility treatment, token references and reuse restrictions. It defines the B-13 requirement block and the three traceability matrices. It reconciles the original Prompt 13B map scope against the accepted mapless architecture. It records the documentation impact of the pass.

### 1.2 What this document does not do

- It does not implement frontend code, create a frontend project, select a framework, write CSS, define production routes, or touch Supabase, authentication, migrations or gameplay systems.
- It does not create, change or reinterpret a game rule, formula, parameter, numeric value, requirement status or owner-reserved decision.
- It does not define complete player journeys, onboarding tutorials, cross-system interaction sequences, error-handling logic, loading/empty/success/failure flows, notification sequences or end-to-end accessibility interaction verification — those are Prompt 13C (13C-01 boundary).
- It does not perform Prompt 13D's independent completeness audit, acceptance-test suite or final closure.
- It does not claim WCAG 2.2 AA compliance, runtime verification, responsive-device verification or visual QA. The accessibility target is design intent, evidenced later on a built UI.

### 1.3 Scope boundary summary

| Boundary | Position in this pass |
|---|---|
| Frontend implementation | NOT AUTHORIZED and NOT PERFORMED |
| Game-rule change | None; B-02…B-12 remain authoritative |
| New gameplay action | None; every control traces to an existing rule or is a read-only/display control |
| Prompt 13C journey work | NOT STARTED; §30 hands over the boundary |
| Prompt 13D final audit | NOT STARTED |
| Owner-reserved brand values | Preserved open (`13A-OQ-001`, `13A-OQ-002`, `13A-OQ-013`) |
| Global Trade | Gate G-1…G-6 not met; `SCR-038/039` specified as **absent** and BLOCKED |
| Intelligence/espionage | B-10 excludes it; `SCR-068` remains a placeholder with no build authority |
| Geographic maps | Prohibited; see §11 |

---

## 2. Relationship to Prompt 13A

Prompt 13A established the evidence base, 16 design principles, the persistent shell, the eight-section navigation, the 13-state application-state register, the 100-screen inventory, the overlay family, responsive foundations and design-system foundations. Prompt 13B consumes those positions without re-researching and without reopening 13A's correction cycles. The binding inheritance is:

| 13A artefact | How 13B uses it |
|---|---|
| `13A-PR-01`…`13A-PR-16` | Applied as screen and component duties in §8–§10 and the requirement block |
| `13A-RD-01`…`13A-RD-08` | Per-screen responsive fields adopt the must-not-simplify and may-simplify lists |
| `13A-DS-01`…`13A-DS-15` | Components reference semantic tokens only; no raw colour, typeface, size or spacing value appears |
| `SCR-001`…`SCR-100`, `OVL-01`…`OVL-08` | Preserved exactly; no identifier added, removed, renamed or reclassified |
| `13A-UR-001`…`13A-UR-048` | Converted into global B-13 requirements where genuinely UI-specific, otherwise cited |
| `13A-OQ-001`…`13A-OQ-016` | Preserved; the screen/provisional split is recorded in §27 |
| `13A-BP/DR/FND/SRC` | Cited as research inspiration only, never as a rule or observed fact beyond its evidence class |

**Evidence discipline.** No new benchmark observation is claimed. Where a screen pattern echoes Politics & War, the citation names the existing `13A-BP-` or `13A-DR-` row. Where 13A recorded `NOT-RETRIEVABLE`, this document makes no layout claim from the benchmark and derives the layout from B-system rules only (D-199, `13A-DR-024`). In particular `SCR-064` battle-report layout is derived from WAR-088 and the B-10 record fields, not from P&W memory.

---

## 3. UI architecture reference

### 3.1 Persistent shell (D-201, unchanged)

Every authenticated screen renders inside one shell with fixed slots: identity strip; primary navigation; alert bar; quick-go; breadcrumb/context line; primary content; context panel where width allows; footer with help, support, terms and change disclosures. The shell never collapses on mobile; its regions reflow (§8). Administration renders in a separate role-gated root with no player chrome (§3.2; screen companion §10).

### 3.2 Sections and roots

| Root | Screens | Opening surface |
|---|---|---|
| Public | `SCR-001`…`SCR-007`, `SCR-010` | Landing `SCR-001` |
| Home | `SCR-008`, `SCR-009`, `SCR-013`…`SCR-017`, `SCR-019`, `SCR-020`, `SCR-089` | Command Digest `SCR-013` |
| Economy | `SCR-029`…`SCR-040` | Treasury `SCR-029` |
| Cities | `SCR-041`…`SCR-046` | Cities overview `SCR-041` |
| Politics | `SCR-021`…`SCR-028` | Political Panel `SCR-021` |
| Foreign | `SCR-047`…`SCR-058` | Diplomatic overview `SCR-047` |
| War | `SCR-059`…`SCR-068` | Military overview `SCR-059` |
| World | `SCR-018`, `SCR-069`…`SCR-078`, `SCR-088` | Events Centre `SCR-069` |
| Account | `SCR-011`, `SCR-012`, `SCR-079`…`SCR-087`, `SCR-090` | Account home `SCR-011` |
| Admin | `SCR-091`…`SCR-100` | Admin console `SCR-091` |

Four screens carry the inventory's dual parent as a **canonical parent plus a cross-section alias** (D-209): `SCR-010` Public (alias World), `SCR-017` Home (alias World), `SCR-062` War (alias World), `SCR-088` World (alias Home). The canonical parent decides breadcrumb and section highlight; the alias is a deep link and related-object entry, not a second copy.

### 3.3 Application states

The 13-state vocabulary of 13A §6 is adopted per screen where applicable: loading, empty (new nation), empty (no data), error/failed request, permission-denied, blocked-by-rule, disconnected/stale, action success, pending action, confirmation-required, time-sensitive, suppressed-data, `PROVISIONAL_BLOCK`. 13B defines each state's **presentation and visible variants**; the transitions, journeys and feedback sequencing are 13C. Every screen specification names its applicable states or records an exemption with reason (`REQ-1004`).

---

## 4. Screen specification methodology

### 4.1 Template A–K (D-208)

Every `SCR-` body in the companion uses the same eleven fields in the same order:

| Field | Content |
|---|---|
| **A Identity** | ID, canonical name, parent, category, governing B-section, related existing requirement identifiers, class, primary audience, required permissions, visibility classification |
| **B Purpose** | Why the screen exists, the player problem, the system information presented, what the player should understand, supported decisions |
| **C Entry and navigation** | Parent location, direct entries, secondary navigation, contextual entries, permitted destinations, returns, restrictions, direct-vs-context access |
| **D Information hierarchy** | Primary; secondary; supporting; historical/contextual; warnings/restrictions; progressive disclosure |
| **E Layout** | Top-to-bottom textual layout diagram and region purpose |
| **F Data presentation** | Data name, meaning, units, time reference, current/historical/forecast/provisional class, visibility, source system, player/public status, disclosure limits, component |
| **G Controls** | Control, label, purpose, action, preconditions, permissions, read-only vs committing, confirmation, governing rule, outcome; disabled reason where relevant |
| **H Screen relationships** | Related screens and objects with the reason for the relationship |
| **I Responsive presentation** | Desktop, tablet, mobile; columns, tables, navigation, stacking, actions, overflow, touch, never-disappears |
| **J Governing references** | Governing rules, supporting requirements, data dependencies, navigation relationships, research inspiration, design decisions — exact identifiers |
| **K Restrictions and notes** | Restrictions, unresolved dependencies, owner-reserved questions, conditional/provisional assumptions, future implementation notes |

### 4.2 Screen categories

`Public entry` · `Transactional flow` · `Dashboard` · `Register/list` · `Object page` · `Task/compose` · `Detail record` · `Status/state` · `Guide/help` · `Admin workspace`. The category sets the default layout and table/card behaviour; it never overrides the governing rule.

### 4.3 Identity and classification rules

- The 100 identifiers and the existing classes are preserved: 85 Mandatory player-facing, 4 Conditional player-facing (`SCR-020`, `SCR-038`, `SCR-039`, `SCR-077`), 1 Provisional player-facing (`SCR-068`), 10 Mandatory administrative (`SCR-091`…`SCR-100`).
- A Conditional screen is **not reachable** until its named gate is met; it is not stubbed, previewed, partially rendered or hidden behind a teaser. A Provisional screen is a registered placeholder only; it carries no build authority and no simulated functionality.
- A screen's `Status` in Matrix A is the specification/feature state: `SPECIFIED`, `PROVISIONAL` or `BLOCKED`. A `BLOCKED` screen's *absence duty* is nevertheless fully specified.
- No screen may create an action. If a control's governing rule does not exist, the control does not exist.

### 4.4 Requirement allocation (D-217)

`REQ-870`…`REQ-969` are the **one-per-screen presentation requirements**, allocated `REQ = 869 + screen number` (so `REQ-870` ↔ `SCR-001`, `REQ-969` ↔ `SCR-100`). `REQ-970`…`REQ-1049` are cross-cutting shell, navigation, component, data, responsive, accessibility, permission, design-system and traceability requirements. This mirrors the accepted 12B `REQ = 763 + CR` convention. No global `REQ-` row from another block is renumbered, reworded or status-changed.

---

## 5. Complete screen catalogue

The full A–K body of each screen is in [`21_screen_specifications.md`](21_screen_specifications.md), grouped exactly as below. This table is the index; Matrix A in §24 is the authoritative completeness register.

| Catalogue group | Family | Screens | Detailed bodies |
|---|---|---|---|
| 5.1 | Public and account experience | `SCR-001`…`SCR-012` | Companion §1 |
| 5.2 | Main strategic interface | `SCR-013`…`SCR-020` | Companion §2 |
| 5.3 | Politics | `SCR-021`…`SCR-028` | Companion §3 |
| 5.4 | Economy and market | `SCR-029`…`SCR-040` | Companion §4 |
| 5.5 | Cities, infrastructure and research | `SCR-041`…`SCR-046` | Companion §5 |
| 5.6 | Diplomacy and alliances | `SCR-047`…`SCR-058` | Companion §6 |
| 5.7 | Warfare and military | `SCR-059`…`SCR-068` | Companion §7 |
| 5.8 | World and progression | `SCR-069`…`SCR-078` | Companion §8 |
| 5.9 | Player protection and support | `SCR-079`…`SCR-090` | Companion §9 |
| 5.10 | Administration | `SCR-091`…`SCR-100` | Companion §10 |

**Family-level coverage statements.**

- **Public and account (`001`–`012`).** Covers the landing, registration, login, reset, recovery-code entry, e-mail verification, nation creation, onboarding, first-turn objectives, public nation profile, account home and closure. Every visible state maps to the ten ACC states (ACC-017), D-029 verification gate, D-041 recovery/closure, D-039/D-040 reroll/protection and D-038 naming. No authentication policy is invented.
- **Strategic (`013`–`020`).** Digest, Inbox, National Overview, Turn status, Chronicle, Network View, Alerts, Pinned objects. The Digest is a bounded **summary of existing events**, not an open widget board; the Inbox is the sole aggregation of pending acts, ordered by due boundary.
- **Politics (`021`–`028`).** All eight carry the DMP-268 state banner (`NORMAL`, `ELECTORAL`, `SUCCESSION`, `TRANSITION`, `CRISIS`, `RECOVERY`). Approval is the weighted mean of the six supports with per-term cause chains (DMP-073); stability is displayed as integer basis points with a text label, because B-06 defines no named stability bands and 13B may not invent them. Policy cooldown is on the control (D-087, one change per axis per 12 turns). Campaign actions are exactly the three DMP-189 types with charge-once semantics.
- **Economy and market (`029`–`040`).** Six number types are separated everywhere (ECN-177); every balance is total/reserved/available (MKT-053, TR-069, URB-066); forecasts are lighter and labelled (ECN-178, URB-152); capacity is not a resource and power is not stored (D-048). `SCR-038/039` are **absent** until G-1…G-6 pass; `MKT-G01` explains absence. `SCR-040` shows only pre-gate minimal history (D-117).
- **Cities (`041`–`046`).** Twelve-city one-screen premise (URB-031/D-067), `used / total` DC before commitment (URB-052), one construction-class action per city per turn with the slot claimed at acceptance (D-073/URB-064), 25% crown-only demolition refund (D-074/URB-071), `UNMAINTAINED` chain state (ECN-147/147a), one active research project (D-076) and banked-RP versus programme spend separated (URB-095).
- **Diplomacy and alliances (`047`–`058`).** Directional posture shown per direction, two-sided pair screen (DIP-023/024), four posture values, three nation agreement types `DP-T01`…`DP-T03` plus embargo `DP-A01`, publication at activation with k=5 aggregates (DIP-108…113), pending terms parties-only (D-030), private/public history split, and the six-view floor of 08C §12.2. The Alliance interface is management/coordination only: **no** military command, member OP spending, shared OP pool, delegated war operations or private war visibility (AX-18, WAR-148, WAR-161, REQ-589…REQ-591, UD-047/UD-049). Alliance taxes are player-named brackets with separate Crowns and per-resource rates in integer basis points 0–10,000, a visible 0% fallback while UD-040 is open, an effective turn and policy version shown before confirmation, history and receipts. The ARL shows four categories (`RECEIVED`, `AVAILABLE`, `RESERVED`, `EXPENDED`) and no spendable purpose exists today.
- **Warfare (`059`–`068`).** Owner-only War Operations Board (nation-level) shows only this nation's OP balance, reservations, operations and battles; readiness bands `LOW`/`MODERATE`/`HIGH`/`SEVERE` are the only opponent strength disclosure (WAR-086); battle reports derive from WAR-088; surrender is the guaranteed off-ramp (WAR-132); espionage is excluded and `SCR-068` builds nothing.
- **World (`069`–`078`).** The six WPC-14 surfaces (Events Centre, Objectives and Challenges, Standings, Achievements, National Progress, Reward History) plus event detail and World Chronicle; standings carry denominator and window and never update live (WEP-324/325); no composite headline (WEP-361/362); suppression is a named state (WEP-663, D-027); `SCR-077` renders only figures passing k=5 per figure.
- **Player protection (`079`–`090`).** Nine privacy classes `PUB`, `PLAYER`, `ALLIANCE`, `OPS`, `MOD`, `PERSONAL`, `SEC`, `AUDIT`, `LEGAL` (PRV-002/009); `SEC` never rendered (PRV-014); report intake exactly MOD-002; decision notices carry MOD-017's seven elements; appeal route never blocked (MOD-013); restriction text names the kind and reason class without accusation or another player's data (NET-023, NET-050, PRV-019); data access/export and retention disclosed by class (D-026); change disclosures are public and dated (TR-049).
- **Administration (`091`–`100`).** Ten role-scoped workspaces behind the separate Admin root; the eight ADM roles; least privilege (D-042); two-person rule displayed where required (MOD-022); audit visibility separated from player surfaces.

---

## 6. Reusable component architecture

The catalogue is in [`21_component_specifications.md`](21_component_specifications.md). This section records the architecture that governs it.

### 6.1 Identifier and reuse policy (D-207)

- One new family: **`UI-CMP-001`…`UI-CMP-090`**, unique repo-wide, allocated by family order in the 13B instruction §7.1–§7.7.
- The eight overlays keep their existing identifiers `OVL-01`…`OVL-08` and are specified as overlay components; no new `OVL-` identifier is created.
- A component is defined **once**. Screen specs reference it by ID and never restate its internals. Where two components look similar, the separation is justified in the component body (for example `UI-CMP-015` single-resource balance versus `UI-CMP-033` composite total/reserved/available register).
- Components are classified `Global`, `System-specific`, `Screen-specific`, `Role-restricted` or `Conditionally available`. Role-restricted components may render only inside the Admin root or a permissioned Alliance surface; conditionally available components (Global Trade, favorites, world charts) must not render before their gate.

### 6.2 Component families

| Family | Components | Count |
|---|---|---|
| Application shell | `UI-CMP-001`…`UI-CMP-011` | 11 |
| Information display | `UI-CMP-012`…`UI-CMP-030` | 19 |
| Economic and political | `UI-CMP-031`…`UI-CMP-042` | 12 |
| Diplomacy and alliance | `UI-CMP-043`…`UI-CMP-053` | 11 |
| Warfare | `UI-CMP-054`…`UI-CMP-062` | 9 |
| World and notification | `UI-CMP-063`…`UI-CMP-073` | 11 |
| Forms and actions | `UI-CMP-074`…`UI-CMP-090` | 17 |
| Overlays | `OVL-01`…`OVL-08` | 8 |

### 6.3 State vocabulary (D-215 boundary)

Every applicable component defines: `default`, `hover`, `focus-visible`, `active`, `disabled(+reason)`, `loading`, `success`, `warning`, `error`, `pending`, `suppressed`. Not every component carries every state; each body records the applicable set or an exemption. Visual distinction is always paired with a textual or glyph indication (colour is never the only channel), reduced motion is respected, and hover is never load-bearing. Complete interaction sequencing, error recovery and feedback journeys remain 13C.

### 6.4 Token discipline (D-203)

Component bodies reference semantic tokens by role only: surface, text, border, focus, status tones (`informational`, `pending`, `success`, `warning`, `danger`, `locked/denied`, `suppressed`), typography registers (display, text, data), spacing scale, radius, elevation and motion. No hex colour, font family, pixel size or arbitrary spacing value appears in any B-13 document. Brand values remain owner-reserved.

---

## 7. Navigation and screen-transition specifications

### 7.1 Model (D-209)

- One canonical parent per screen (the classification table in §3.2); a dual-parent inventory value becomes a canonical parent plus a cross-section alias.
- One canonical **route key** per screen, independent of the final URL mechanism (OQ-015 is Stage 5). Route keys are stable semantic addresses: `section.object`.
- Every object identifier renders as a link to its canonical route, subject to visibility (`UI-CMP-027`).
- Breadcrumbs appear at depth ≥ 2 and every crumb is a link.
- Section tabs exist only for same-object views; they are not menu items.
- The Inbox is a destination, not a modal; each row deep-links to its owning action screen.
- Conditional screens have no route rendered until their gate passes. Provisional screens have a registered route key only for documentation and must not be linked from production navigation.
- Administrative routes exist only inside the Admin root and are refused for non-holders without disclosing the existence of case data.

### 7.2 Master navigation relationship register

Columns: canonical parent; route key; direct entry points; related destinations (navigation, not a journey); restrictions. Return destination is the canonical parent unless the entry breadcrumb supplies a deeper return; a return never lands on a Conditional or role-denied surface.

| SCR | Parent | Route key | Direct entry | Related destinations | Restrictions |
|---|---|---|---|---|---|
| `SCR-001` | Public | `public.landing` | Any unauthenticated URL | `SCR-002`, `SCR-003`, `SCR-078` (public guide excerpt), terms | Public only |
| `SCR-002` | Public | `public.register` | Landing CTA | `SCR-003`, `SCR-004`, terms/rules | Public; verified e-mail gate to `SCR-007` |
| `SCR-003` | Public | `public.login` | Landing; session expiry | `SCR-002`, `SCR-004`, `SCR-005`, `SCR-013` after auth | Public |
| `SCR-004` | Public | `public.reset` | Login link | `SCR-005`, `SCR-003` | Public; never creates accounts |
| `SCR-005` | Public | `public.recovery` | Reset flow; security settings | `SCR-003`, `SCR-080` after auth | Public; single-use codes |
| `SCR-006` | Public | `public.verify` | Registration; unverified login | `SCR-003`, `SCR-007` | Public; resend gated |
| `SCR-007` | Public | `public.create-nation` | Verified account | `SCR-008`, `SCR-013` | VERIFIED/ELIGIBLE account; no nation yet |
| `SCR-008` | Home | `home.onboarding` | First nation creation | `SCR-009`, `SCR-013`, `SCR-015` | One-time; never re-granted (D-040) |
| `SCR-009` | Home | `home.objectives-entry` | Onboarding; objectives | `SCR-008`, `SCR-071` | Account-scoped entry surface |
| `SCR-010` | Public | `public.nation` | Any object link; search | `SCR-047`, `SCR-062`, `SCR-069`, `SCR-081` | Public fields only; owner sees `SCR-015` |
| `SCR-011` | Account | `account.home` | Account menu | `SCR-012`, `SCR-079`, `SCR-080`, `SCR-084`, `SCR-090` | Authenticated |
| `SCR-012` | Account | `account.closure` | Account home | `SCR-011`, `SCR-085` | Authenticated; 7-day cooling |
| `SCR-013` | Home | `home.digest` | Primary nav Home; post-login | `SCR-014`, `SCR-015`, `SCR-016`, `SCR-019`, `SCR-017` | Authenticated |
| `SCR-014` | Home | `home.inbox` | Shell alert; digest | Owning action screens per row | Authenticated; row permissions apply |
| `SCR-015` | Home | `home.overview` | Primary nav Home; digest | All section dashboards | Authenticated |
| `SCR-016` | Home | `home.turn` | Shell countdown | `SCR-014`, `SCR-013` | Authenticated |
| `SCR-017` | Home | `home.chronicle` | Overview; digest | `SCR-076`, `SCR-010` | Authenticated; class-P/S |
| `SCR-018` | World | `world.network` | World nav; overview | `SCR-010`, `SCR-053`, `SCR-047` | Authenticated; published edges only |
| `SCR-019` | Home | `home.alerts` | Shell alert count | `SCR-014`, owning screens | Authenticated; non-opt-out preserved |
| `SCR-020` | Home | `home.pins` | Overview (when enabled) | Pinned objects | Conditional; absent until `13A-OQ-012` |
| `SCR-021` | Politics | `politics.panel` | Primary nav Politics | `SCR-022`…`SCR-028` | Authenticated; banner always |
| `SCR-022` | Politics | `politics.government` | Panel | `SCR-021`, `SCR-023` | Authenticated; permanent identity |
| `SCR-023` | Politics | `politics.approval` | Panel | `SCR-024`, `SCR-028` | Authenticated |
| `SCR-024` | Politics | `politics.axes` | Panel | `SCR-023`, `SCR-021` | One change per axis per 12 turns |
| `SCR-025` | Politics | `politics.elections` | Panel | `SCR-026`, `SCR-027` | `ELECTORAL` window |
| `SCR-026` | Politics | `politics.campaign` | Election dashboard | `SCR-025`, `SCR-027` | Read-only during `TRANSITION`/`CRISIS` |
| `SCR-027` | Politics | `politics.result` | Election resolution alert | `SCR-025`, `SCR-021` | Post-resolution |
| `SCR-028` | Politics | `politics.crisis` | Banner; warning | `SCR-023`, `SCR-021` | CRISIS/RECOVERY |
| `SCR-029` | Economy | `economy.treasury` | Primary nav Economy | `SCR-030`, `SCR-031`, `SCR-033` | Authenticated |
| `SCR-030` | Economy | `economy.budget` | Treasury | `SCR-029`, `SCR-031` | Authenticated |
| `SCR-031` | Economy | `economy.reports` | Treasury | `SCR-029`, `SCR-030` | Class-P/S |
| `SCR-032` | Economy | `economy.production` | Economy nav | `SCR-033`, `SCR-044` | Authenticated |
| `SCR-033` | Economy | `economy.resources` | Treasury; production | `SCR-034`, `SCR-036` | Authenticated |
| `SCR-034` | Economy | `economy.power` | Economy nav | `SCR-033`, `SCR-044` | Authenticated |
| `SCR-035` | Economy | `economy.offers` | Economy nav; inbox | `SCR-036`, `SCR-037` | Authenticated |
| `SCR-036` | Economy | `economy.offer-compose` | Directed inbox | `SCR-035`, `SCR-037` | Counterparty required |
| `SCR-037` | Economy | `economy.offer-detail` | Inbox; trade history | `SCR-035`, `SCR-036` | Parties only |
| `SCR-038` | Economy | `economy.trade-board` | None until gate | `SCR-039`, `SCR-040` | Conditional; BLOCKED; absent |
| `SCR-039` | Economy | `economy.listing` | None until gate | `SCR-038`, `SCR-040` | Conditional; BLOCKED; absent |
| `SCR-040` | Economy | `economy.trade-history` | Economy nav | `SCR-035`, `SCR-037` | Class-P/S; pre-gate minimal |
| `SCR-041` | Cities | `cities.overview` | Primary nav Cities | `SCR-042`, `SCR-043`, `SCR-046` | Authenticated |
| `SCR-042` | Cities | `cities.city` | Overview row | `SCR-043`, `SCR-044` | City ownership |
| `SCR-043` | Cities | `cities.construction` | City detail | `SCR-042`, `SCR-044` | One slot per city |
| `SCR-044` | Cities | `cities.chains` | Cities nav | `SCR-032`, `SCR-042` | Authenticated |
| `SCR-045` | Cities | `cities.research` | Cities nav | `SCR-042`, `SCR-044` | One active project |
| `SCR-046` | Cities | `cities.found` | Overview CTA | `SCR-041`, `SCR-042` | Cost/eligibility gate |
| `SCR-047` | Foreign | `foreign.diplomacy` | Primary nav Foreign | `SCR-048`, `SCR-049`, `SCR-052` | Authenticated |
| `SCR-048` | Foreign | `foreign.pair` | Overview row; profile | `SCR-049`, `SCR-050`, `SCR-052` | Pair visibility |
| `SCR-049` | Foreign | `foreign.proposal` | Pair screen | `SCR-048`, `SCR-050` | Named counterparty |
| `SCR-050` | Foreign | `foreign.agreement` | Overview; history | `SCR-048`, `SCR-051`, `SCR-052` | Publication rules |
| `SCR-051` | Foreign | `foreign.publication` | Agreement detail | `SCR-050`, `SCR-052` | k=5 aggregates |
| `SCR-052` | Foreign | `foreign.history` | Pair/agreement | `SCR-048`, `SCR-050` | Class P/S split |
| `SCR-053` | Foreign | `foreign.alliance` | Overview; network | `SCR-054`, `SCR-058` | Public fields only |
| `SCR-054` | Foreign | `foreign.alliance-members` | Alliance home | `SCR-055`, `SCR-053` | Member/officer permission |
| `SCR-055` | Foreign | `foreign.alliance-governance` | Alliance home | `SCR-054`, `SCR-056` | Role permission |
| `SCR-056` | Foreign | `foreign.alliance-tax` | Governance | `SCR-057`, `SCR-054` | Tax-management permission |
| `SCR-057` | Foreign | `foreign.alliance-finance` | Alliance home | `SCR-056`, `SCR-029` | ARL permission |
| `SCR-058` | Foreign | `foreign.alliance-diplomacy` | Alliance home | `SCR-053`, `SCR-050` | Management only; no war authority |
| `SCR-059` | War | `war.overview` | Primary nav War | `SCR-060`, `SCR-061`, `SCR-062` | Authenticated |
| `SCR-060` | War | `war.forces` | Overview | `SCR-059`, `SCR-065` | Owner only |
| `SCR-061` | War | `war.board` | Overview | `SCR-063`, `SCR-064`, `SCR-067` | **Nation owner only** |
| `SCR-062` | War | `war.conflicts` | Overview; World alias | `SCR-063`, `SCR-065` | Public fields only |
| `SCR-063` | War | `war.detail` | Conflicts ledger | `SCR-064`, `SCR-067` | Per-field visibility |
| `SCR-064` | War | `war.battle` | Board; war detail | `SCR-063`, `SCR-065` | Participating owner; public summary |
| `SCR-065` | War | `war.reports` | Board; war detail | `SCR-064`, `SCR-066` | Owner only |
| `SCR-066` | War | `war.archive` | Overview | `SCR-063`, `SCR-065` | D-026 retention |
| `SCR-067` | War | `war.settlement` | War detail; board | `SCR-063`, `SCR-050` | Counterparty; surrender always available |
| `SCR-068` | War | `war.intelligence` | None (no route) | None | Provisional; no rule; no build authority; not built |
| `SCR-069` | World | `world.events` | Primary nav World | `SCR-070`, `SCR-018` | Authenticated |
| `SCR-070` | World | `world.event` | Events list | `SCR-069`, `SCR-071` | Event visibility |
| `SCR-071` | World | `world.objectives` | World nav | `SCR-072`, `SCR-073` | Authenticated |
| `SCR-072` | World | `world.standings` | World nav | `SCR-010`, `SCR-074` | Denominator/window; no live rank |
| `SCR-073` | World | `world.achievements` | World nav | `SCR-075`, `SCR-074` | Authenticated |
| `SCR-074` | World | `world.progress` | World nav | `SCR-073`, `SCR-075` | Authenticated |
| `SCR-075` | World | `world.rewards` | World nav | `SCR-073`, `SCR-076` | Deferred claims visible |
| `SCR-076` | World | `world.chronicle` | World nav | `SCR-017`, `SCR-070` | Public/disclosed entries |
| `SCR-077` | World | `world.health` | World nav (when gate passes) | `SCR-072`, `SCR-069` | Conditional; k=5 per figure |
| `SCR-078` | World | `world.guide` | Footer; every screen help | Section screens; `SCR-087` | Public read |
| `SCR-079` | Account | `account.privacy` | Account home | `SCR-080`, `SCR-085` | Authenticated; no SEC |
| `SCR-080` | Account | `account.security` | Account home | `SCR-005`, `SCR-079` | Authenticated |
| `SCR-081` | Account | `account.report` | Footer; nation/profile | `SCR-082`, `SCR-087` | Intake available |
| `SCR-082` | Account | `account.report-status` | Report receipt | `SCR-083`, `SCR-081` | Reporter only |
| `SCR-083` | Account | `account.appeal` | Decision notice | `SCR-082`, `SCR-084` | Never blocked |
| `SCR-084` | Account | `account.restrictions` | Account home; notice | `SCR-083`, `SCR-080` | Own status only |
| `SCR-085` | Account | `account.data` | Privacy centre | `SCR-079`, `SCR-012` | Data-subject routes |
| `SCR-086` | Account | `account.review` | Restriction notice | `SCR-084`, `SCR-083` | Bounded state names only |
| `SCR-087` | Account | `account.support` | Footer | `SCR-078`, `SCR-081` | Intake separate from reports |
| `SCR-088` | World | `world.changes` | Footer; Home alias | `SCR-078`, `SCR-019` | Public dated records |
| `SCR-089` | Home | `home.protection` | Shell badge; block moments | `SCR-063`, `SCR-014` | Visibility-only state |
| `SCR-090` | Account | `account.reroll` | Account home | `SCR-007`, `SCR-012` | Exact-phrase; block conditions |
| `SCR-091` | Admin | `admin.console` | Role-gated admin entry | `SCR-092`…`SCR-100` | ADM role |
| `SCR-092` | Admin | `admin.moderation` | Console | `SCR-093`, `SCR-094` | `R-MOD`/`R-SMOD` |
| `SCR-093` | Admin | `admin.case` | Queue | `SCR-092`, `SCR-094` | Assigned reviewer |
| `SCR-094` | Admin | `admin.sanctions` | Case | `SCR-093`, `SCR-096` | Two-person rule |
| `SCR-095` | Admin | `admin.network` | Console | `SCR-093`, `SCR-096` | `R-INV`/`R-SEC` |
| `SCR-096` | Admin | `admin.audit` | Console | `SCR-093`, `SCR-098` | `R-AUD` scoped |
| `SCR-097` | Admin | `admin.turns` | Console | `SCR-016`, `SCR-096` | `R-OPS` |
| `SCR-098` | Admin | `admin.data` | Console | `SCR-096`, `SCR-085` | `R-SEC`/`R-AUD` |
| `SCR-099` | Admin | `admin.announce` | Console | `SCR-088`, `SCR-092` | Authorized role |
| `SCR-100` | Admin | `admin.roles` | Console | `SCR-091`, `SCR-096` | `R-SEC`; least privilege |

### 7.3 Navigation integrity checks

1. Every Mandatory player-facing screen has a canonical parent and route key.
2. No duplicate screen identifier or route key exists.
3. Administrative routes appear only under `admin.*` and never in player navigation.
4. Conditional routes are absent until their gate; `SCR-038/039` and `SCR-077` render nothing early.
5. `SCR-068` is not linked from any production surface.
6. No Alliance route links to the War Operations Board as an authority path. `SCR-058` may link to public `SCR-062` and to the viewer's own permitted `SCR-059`; it never links to another nation's `SCR-061`, `SCR-064` or `SCR-065`. The permanent prohibition is explicit: no Alliance military command, no member OP spending, no delegated war operations and no private war visibility.
7. No screen reveals data beyond its governing visibility class; see §9 and each screen's field F.

## 8. Responsive screen specifications

### 8.1 Device patterns (D-211)

The 13A device classes and provisional breakpoints are binding in policy: phone ≤ ~600 px, tablet ~600–1024 px, desktop > ~1024 px (`13A-RD-06`; Category C values, confirming test Stage 5 device matrix). 13B does not invent final breakpoints. It assigns each screen one of six **presentation patterns**; the pattern is recorded in the screen body's field I and the concrete per-screen treatment follows from it.

| Pattern | Used by | Desktop | Tablet | Mobile |
|---|---|---|---|---|
| `P-DASH` | Dashboards and digests (`SCR-013/015/021/029/041/059/069`) | Primary region + context panel; 12-column grid; stat strip above registers | Context panel becomes bottom sheet; stat strip wraps 2×; tables keep priority columns | Single column; stat cards stack; context facts inline below the primary register; countdown and banners stay in the header band |
| `P-REG` | Registers and lists (`SCR-019/035/040/047/053/062/066/072/092`) | Full table grammar with filter row, saved views, range pagination | Column-priority table with pinned identity column and horizontal scroll; filters in a drawer | Card list preserving every field marked *never disappears*; filter drawer; pagination as "load next page" with exact counts; no horizontal page scroll |
| `P-OBJ` | Object pages (`SCR-010/042/048/050/053/063/070`) | Sectioned object page with sticky section index and context panel | Section index becomes a select; panels stack | Tabs or accordion; summary first; every section reachable; deep-link parity preserved |
| `P-TASK` | Task/compose/confirmation (`SCR-024/026/036/043/046/049/056/081/090`) | Form region + side preview of consequences; confirmation in `OVL-01` with page equivalent | Form full width; preview above action bar; confirmation sheet | Stepped single column; sticky action bar; destructive actions separated and never adjacent to primary; exact-phrase field full width |
| `P-STATE` | Status/state screens (`SCR-016/028/082/084/086/089`) | One primary state banner + explanation + actions | Same, stacked | Same; banner and reason strings never collapse |
| `P-GUIDE` | Guide/help (`SCR-078/087/088`) | Two-pane index + article | Index drawer + article | Accordion index; in-page search; no gameplay text in images |

### 8.2 Non-negotiable responsive duties

The following never disappear, truncate to ambiguity or move behind an interaction on any device: turn countdown and next boundary; selected-turn context; pending-action counts; political state banner; protection state and end turn; suppression notices; total/reserved/available triples; financial units and as-of slot; the six-number-type label of every figure; confirmation requirements; disabled reasons; accessible control labels; appeal route; own restriction state. Tablet and mobile may reorder these, collapse secondary prose, convert tables to cards and hide decorative headers, but may not remove meaning (`13A-RD-07`, `13A-RD-08`).

### 8.3 Table, card and chart behaviour

- A table's identity column is pinned on tablet; the remaining columns follow a declared priority order. On mobile, each row becomes a card that preserves the identity field and every field marked *never disappears* in field F.
- Range pagination reports exact totals ("0–N of M") and never implies completeness it does not have (MKT-065).
- Charts scale without losing axis labels; a text/table alternative is always available (`UI-CMP-030`); charts never become the only source of a decision-critical figure.
- Long-form cause chains collapse under a labelled "why" disclosure, never behind hover. Hover-only facts are prohibited.

### 8.4 Touch and destructive-action protection

Touch targets meet the DS-14 minimum token; destructive controls (`SCR-090`, admin sanctions, treaty termination, surrender) are separated from adjacent primary controls, use `UI-CMP-087` and `OVL-02`, and require the exact-phrase field where the governing rule demands it (RRL-006). Mobile confirmation may become a full-screen sheet but may not be skipped. Countdown updates are polite live-regions and never announce continuously (`13A-DS-13`).

---

## 9. Information hierarchy and data-visualization rules

### 9.1 Six-tier hierarchy (D-210)

Every screen body orders its information as: **1 primary** (the one register the screen exists to show); **2 secondary** (the figures needed to interpret the primary); **3 supporting** (context, related objects); **4 historical** (prior turns, records, retention-labelled); **5 warnings and restrictions** (state banners, blocks, suppression, protection, role limits); **6 progressive** (definitions, cause chains, assumptions, methodology). A screen may not give every statistic equal weight. Warnings rank above supporting data when they change what the player can do, but they never replace the primary register.

### 9.2 National statistics

Six number types are separate registers with distinct labels and weights: **historical result** (what happened), **current balance** (what exists now), **pending/reserved** (what is claimed), **forecast** (what is expected), **market estimate** (what someone might pay, only where a rule permits), **completed transaction** (what was paid) (ECN-177, D-056). Every figure carries its as-of turn/slot. A forecast never shares current-state weight and states its assumptions and uncertainty; an uncomputable forecast renders "unknown", never zero (ECN-178). Whole crowns and whole units only; percentages in basis points; one published rounding rule per formula (D-045/D-064, ECN-184).

### 9.3 Economic data

- Total, reserved and available appear together everywhere a balance appears; a total-only balance is a specification defect (MKT-053, TR-069, URB-066).
- Capacity is a per-turn batch rate, not a balance; power is a derived grid capacity and is never stored, traded, gifted, reserved or carried (ECN-042/ECN-120, D-048/ECN-056/ECN-065).
- Capex and opex are separated; national wealth is a report statistic, not a spendable balance or credit (D-051, D-062).
- Book value, asking price, offer price and completed price are separate labels with units (MKT-140).
- No market statistic is published before the D-117 gate; pre-gate history is minimal and labelled.

### 9.4 Military information

- Opponent strength is disclosed only as one of the four bands `LOW`, `MODERATE`, `HIGH`, `SEVERE` (WAR-086). No exact opponent strength, readiness, inventory or odds are shown.
- Own exact attack power, own OP balance and own reservations are shown to the nation owner only.
- Battle reports show the WAR-088 record fields to the participants and the public summary (tier, operation type, loss band) elsewhere.
- Public city damage may show infrastructure before/after and removed levels; exact book value, force and inventory remain private (WAR-109k).
- Alliances receive no military visibility (WAR-148/WAR-161).

### 9.5 Diplomatic information

- Posture is directional: A→B is independent of B→A and both directions appear side by side (DIP-023/024).
- Agreement type and lifecycle state are explicit; pending existence/terms are parties-only until activation; public records begin at activation (D-030, DIP-108…113).
- Breach count is a fact with no score and no mechanical effect (DIP-086/088).
- Aggregates obey k=5 and complementary suppression (DIP-113).

### 9.6 Rankings

- A standing is a named list with its denominator population, eligibility set and reporting window; a display without a denominator is a defect (WEP-324/359).
- Standings are computed at P6 and published at P7; no live-updating rank, no ticking, no implied recency beyond the stated turn (WEP-325).
- No composite headline score, "best nation" ladder or single overall rank is published (WEP-361/362).

### 9.7 Historical information

Retention classes are respected and labelled: 30 days hot → 12 monthly summaries → deletion for routine records; class-P permanent; class-O at least 12 months (D-026, TR-092, PRV-001/023). A record no longer hot is labelled with its retention boundary, never silently missing (`13A-DR-020`). Retired nation pages remain reachable and labelled `retired — rerolled`; a replacement is a separate `New nation` identity (RRL-020, 08C §12.6).

### 9.8 Statistical suppression

`suppressed` is a designed state, not an absence: fewer than five contributors, complementary suppression, `INSUFFICIENT_SAMPLE` and "not enough trades to publish" each render their named state. Suppressed is never zero, never "no data" and never inferable from counts, row totals, thumbnails, ordering, sample-size arithmetic or layout (D-027, TR-022, WEP-663, MKT-110, DIP-113). `UI-CMP-072` and `OVL-07` are the only suppression presentations.

### 9.9 Charts

Every chart carries title, units, time window, source/slot context, legend, accessible text/table alternative and a truncated-axis disclosure where applicable. Dual-axis charts are banned. Averages show sample count. "0" is never drawn where truth is suppressed, insufficient or unknown. No chart is the only place a decision-critical value appears (`13A-DS-12`, `13A-DR-006`, `13A-PR-16`).

---

## 10. Accessibility specifications

### 10.1 Inheritance

The target is WCAG 2.2 AA **as design intent**, not a compliance claim (`13A-DS-07`…`13A-DS-15`; `UR-010` remains an `INDEPENDENT_ACCESSIBILITY_REQUIREMENT` grounded in `13A-PR-14`, `DMP-164` and `REQ-321`; no benchmark keyboard observation is claimed).

### 10.2 Requirements carried into every screen and component

1. Full keyboard operability of every action path; focus order follows reading order; overlays trap and restore focus.
2. Visible, tokenized focus at ≥3:1 against adjacent colours (design intent).
3. Programmatic labels on every control; accessible descriptions for forms and grouped controls.
4. Error identification by text linked to the field; no colour-only error.
5. Every status is colour + glyph + text; affiliation and political states are never hue-only.
6. Semantic table headers with row/column scope; card fallbacks preserve the same structure.
7. Every chart has a text/table alternative; every gameplay-critical value is text, not an image.
8. Screen-reader-readable units: crowns, units, basis points, turns, UTC boundary and band labels are announced with the number.
9. Reduced-motion support; no gameplay motion; countdown live-regions are polite.
10. Touch targets meet the DS-14 minimum; destructive actions are spaced and confirmed.
11. Localization-ready strings; no concatenated sentence fragments that cannot be translated; no text in images.
12. Disabled controls expose a reason string and rule link to assistive technology, not only visually.
13. Suppression and `PROVISIONAL_BLOCK` states are announced as states, not as absent content.
14. Route changes update the page title and focus target; deep links land on a titled screen.
15. No accessibility overlay or third-party remediation widget is specified; the requirement is built-in semantics.

### 10.3 Evidence boundary

`UR-010`, `13A-DS-07` and every accessibility statement in this file remain **design requirements**. No keyboard walkthrough, screen-reader pass, contrast measurement or device test has been executed; Prompt 13D/Stage 6+ owns verification. The independent-evidence classification of `UR-010` and `DS-07` is preserved unchanged.

---

## 11. Map and Network View reconciliation

### 11.1 The accepted architecture

The world is a **relationship graph, not a map**. `TR-012` forbids coordinates, distances, borders, provinces and fronts and forbids any visualisation implying real geography; `TR-013`/`TR-014` define entities and typed edges with visibility classes; `NAT-022` forbids asking for a continent, region, territory, coordinates or map placement; `REQ-041` fixes the mapless world; `FO-013` is the keystone concept citation. `SCR-018` Network View is the sole world-situational surface.

### 11.2 Network View specification (the map requirement's authorised satisfaction)

- **Purpose.** Answer "who is connected to whom, how, and what changed" without geography: nations and alliances as **symbolic nodes**, declared/published relations as **typed edges**, filters and a legend by relation class.
- **Representation.** No coordinates in the data model, no basemap, no tile provider, no projection, no distance, no territory, no province, no front. Layout is a force/relationship layout or a list-first equivalent; node position carries no meaning and must never be presented as location.
- **Entities.** Nation node (public identity, protection state where disclosable, alliance membership where public), alliance node (public identity, member count within disclosure rules), conflict node/edge where a public record exists, treaty edge by type (`DP-T01`…`DP-T03`, `DP-A01`, `AT-T00/T01` where an alliance treaty is disclosed), posture edge per direction (`FRIENDLY`/`NEUTRAL`/`TENSE`/`HOSTILE`).
- **Information hierarchy.** Primary: the selected node/edge and its typed relations. Secondary: relation filters and legend. Supporting: related object list. Historical: relation changes within retention. Warnings: protection, pair restriction (own only), suppression. Progressive: edge provenance ("declared at turn N", "public at activation").
- **Interaction.** Select a node to open `UI-CMP-028` peek (public fields only), then deep-link to `SCR-010`/`SCR-053`; filter by relation type; search by name; no drag-to-move meaning, no zoom-dependent data, no hover-only facts. Empty state explains that no published relations exist and links the governing rule.
- **Responsive.** Desktop: full graph with context panel. Tablet: graph with filter drawer and reduced labels. Mobile: **list-first** relationship list grouped by relation type; the graph is an opt-in secondary view; every fact in the graph is reachable in the list (`13A-RD-04`).
- **Visibility.** Edges only from published/declared relations; pending proposals never appear; k=5 suppression applies to counts; own pair restriction is visible to the owner only; no private war data, no alliance military data.
- **Components.** `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-022`, `UI-CMP-023`, `UI-CMP-026`, `UI-CMP-027`, `UI-CMP-028`, `UI-CMP-043`, `UI-CMP-044`, `UI-CMP-045`, `UI-CMP-072`.

### 11.3 Inventory reconciliation

No registered `SCR-` identifier refers to a geographic or map screen. The inventory contains exactly one map-adjacent surface, `SCR-018` Network View, whose row explicitly says "no geographic coordinates anywhere". The only map references in the 13A package are the rejected benchmark observation `13A-SRC-016` (P&W World Map), the rejected pattern `13A-BP-016`, and the contrast finding `13A-FND-018/030`. They are preserved as research evidence and are **not** screen requirements.

### 11.4 Prohibitions

No geographic world map, territory map, military strategic map, continent framing, map provider, tile service, geocoding dependency or coordinate field is introduced. No screen may imply territorial mechanics. No paid mapping dependency is added, preserving the ₹0/free-first constraint. Any future proposal to add geography requires an owner Category-A decision and a B-02 rule change; neither exists.

### 11.5 Residual dependency

The precise graph layout algorithm and its accessibility fallback are Stage 5 implementation choices; the specification fixes the duties (symbolic, non-geographic, list-first on mobile, all facts reachable without graph interaction) and records the algorithm as an open technical matter, not an owner question.

---

## 12. Screen-to-component relationships (summary)

The authoritative mapping is Matrix B (§25) and each screen body's field G/E. The rules:

- Every screen uses the shell components `UI-CMP-001`…`UI-CMP-009` as applicable; public screens use a reduced shell without authenticated identity data.
- Every table screen uses `UI-CMP-022` with `UI-CMP-023` where filtering exists and `UI-CMP-024` when results exceed one page.
- Every balance display uses `UI-CMP-033` (composite) or `UI-CMP-015` (single resource within a composite context); a screen may not use a bare number component for a balance.
- Every committing control pairs with `OVL-01`; destructive controls pair with `OVL-02`; every disabled control pairs with `OVL-03`.
- Every object identifier uses `UI-CMP-027` and `OVL-05`.
- Every aggregate subject to k=5 uses `UI-CMP-072`/`OVL-07` and never a zero.
- Every role-restricted/admin screen uses `UI-CMP-010` inside the Admin root and never the player navigation `UI-CMP-002`.

**Numbering note.** Sections 13–23 of the original thirty-section plan hold the per-family screen bodies in the [screen companion](21_screen_specifications.md) (its §1–§10); this document resumes its own numbering at §24 for Matrices A–C and the closing registers. No section 13–23 content is missing, and no reference in this document points to a non-existent local section.

## 24. Matrix A — Screen specification completeness

All 100 registered identifiers are accounted for. **Detailed specification**, **responsive specification**, **component mapping** and **requirement mapping** are `Complete` for every row because each screen body in the companion carries fields A–K, and each row's requirement is `REQ-(869+n)`. **Status** is the feature/specification state, not implementation: `SPECIFIED` = fully specified and currently authorised; `PROVISIONAL` = specified but gated or evidence-dependent; `BLOCKED` = must not be available until a named gate or rule exists.

| Screen | Name | Class | Governing | Detailed | Responsive | Component map | Requirement map | Dependencies | Status |
|---|---|---|---|---|---|---|---|---|---|
| `SCR-001` | Landing / public introduction | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-007; brand `13A-OQ-001/002`; k=5 | SPECIFIED |
| `SCR-002` | Registration | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-029; D-032; D-018; NAT naming | SPECIFIED |
| `SCR-003` | Login | Mandatory | B-03 | Complete | Complete | Complete | Complete | ACC-018; D-041 | SPECIFIED |
| `SCR-004` | Password reset initiation | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-041 | SPECIFIED |
| `SCR-005` | Recovery-code entry | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-041; ACC-031 | SPECIFIED |
| `SCR-006` | E-mail verification | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-029; ACC-024 | SPECIFIED |
| `SCR-007` | Nation creation | Mandatory | B-03/B-04 | Complete | Complete | Complete | Complete | NAT-002/015/016/026–030; D-038; D-063 | SPECIFIED |
| `SCR-008` | Onboarding guide | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-040; ONB-009…038 | SPECIFIED |
| `SCR-009` | First-turn objectives entry | Mandatory | B-03/B-11 | Complete | Complete | Complete | Complete | ONB surfaces; WEP objective categories | SPECIFIED |
| `SCR-010` | Public nation profile | Mandatory | B-03/B-06/B-10/B-11 | Complete | Complete | Complete | Complete | NAT-015; RRL-020; TR-021/022; D-036 | SPECIFIED |
| `SCR-011` | Account home | Mandatory | B-03 | Complete | Complete | Complete | Complete | ACC-017/018; D-041 | SPECIFIED |
| `SCR-012` | Account closure | Mandatory | B-03 | Complete | Complete | Complete | Complete | D-041; ACC-043; D-026 | SPECIFIED |
| `SCR-013` | Command Digest | Mandatory | B-02 | Complete | Complete | Complete | Complete | TR-088/089/092; REQ-022 | SPECIFIED |
| `SCR-014` | Inbox / pending actions | Mandatory | B-02 + systems | Complete | Complete | Complete | Complete | TR-004; D-016/D-030; MKT/ALL/AT lifecycles | SPECIFIED |
| `SCR-015` | National Overview | Mandatory | B-04/B-05/B-06/B-10 | Complete | Complete | Complete | Complete | ECN-176; URB-052; DMP-073 | SPECIFIED |
| `SCR-016` | Turn & settlement status | Mandatory | B-02 | Complete | Complete | Complete | Complete | TR-027/030/033/035/036/039/075/080 | SPECIFIED |
| `SCR-017` | National Chronicle | Mandatory | B-11/B-02 | Complete | Complete | Complete | Complete | D-026; class-P history | SPECIFIED |
| `SCR-018` | Network View | Mandatory | B-02/B-08/B-09 | Complete | Complete | Complete | Complete | TR-012/013/014; REQ-041; FO-013 | SPECIFIED |
| `SCR-019` | Alerts & notification history | Mandatory | B-02/B-11 | Complete | Complete | Complete | Complete | REQ-731; DIP-114/116 | SPECIFIED |
| `SCR-020` | Pinned objects / favorites | Conditional | cross | Complete | Complete | Complete | Complete | `13A-OQ-012` fair-play review | PROVISIONAL |
| `SCR-021` | Political Panel | Mandatory | B-06 | Complete | Complete | Complete | Complete | DMP-256/268 | SPECIFIED |
| `SCR-022` | Government structure | Mandatory | B-06 | Complete | Complete | Complete | Complete | D-084/D-085; DMP-079…083 | SPECIFIED |
| `SCR-023` | Approval & stability detail | Mandatory | B-06 | Complete | Complete | Complete | Complete | DMP-073; F-PD-004…009 | SPECIFIED |
| `SCR-024` | Policy axes management | Mandatory | B-06 | Complete | Complete | Complete | Complete | D-087; DMP-101/102 | SPECIFIED |
| `SCR-025` | Election dashboard | Mandatory | B-06 | Complete | Complete | Complete | Complete | D-106/D-107; DMP-178/184 | SPECIFIED |
| `SCR-026` | Campaign actions centre | Mandatory | B-06 | Complete | Complete | Complete | Complete | D-094; DMP-189/193 | SPECIFIED |
| `SCR-027` | Election result & transition | Mandatory | B-06 | Complete | Complete | Complete | Complete | DMP-184/205/210; D-097/D-098 | SPECIFIED |
| `SCR-028` | Crisis & recovery digest | Mandatory | B-06 | Complete | Complete | Complete | Complete | DMP-163; DMP-225/229/248 | SPECIFIED |
| `SCR-029` | Treasury dashboard | Mandatory | B-04 | Complete | Complete | Complete | Complete | ECN-176/177/178; D-050/D-051/D-062 | SPECIFIED |
| `SCR-030` | Budget & national wealth | Mandatory | B-04 | Complete | Complete | Complete | Complete | D-051/D-062; ECN-105/107 | SPECIFIED |
| `SCR-031` | Economic reports & history | Mandatory | B-04 | Complete | Complete | Complete | Complete | ECN-142; D-026 | SPECIFIED |
| `SCR-032` | Production policy & standing orders | Mandatory | B-04 | Complete | Complete | Complete | Complete | D-053; ECN-044/045/053/139 | SPECIFIED |
| `SCR-033` | Resources & warehouse | Mandatory | B-04/B-05 | Complete | Complete | Complete | Complete | MKT-053; ECN-120 | SPECIFIED |
| `SCR-034` | Power grid view | Mandatory | B-04/B-05 | Complete | Complete | Complete | Complete | D-048; ECN-056/059/060/061/064 | SPECIFIED |
| `SCR-035` | Directed-trade inbox | Mandatory | B-07 | Complete | Complete | Complete | Complete | MKT-105/125; D-016 | SPECIFIED |
| `SCR-036` | Compose / counter offer | Mandatory | B-07 | Complete | Complete | Complete | Complete | MKT-019/022/037/038/061; D-017 | SPECIFIED |
| `SCR-037` | Offer detail & two-sided record | Mandatory | B-07 | Complete | Complete | Complete | Complete | MKT-056/131; ECON-054; D-017 | SPECIFIED |
| `SCR-038` | Global Trade board | Conditional | B-07 | Complete | Complete | Complete | Complete | G-1…G-6 not met; D-117/D-122; MKT-073…077 | BLOCKED |
| `SCR-039` | Listing detail & execution | Conditional | B-07 | Complete | Complete | Complete | Complete | Same gate; D-111; MKT-108 | BLOCKED |
| `SCR-040` | Trade history & reference prices | Mandatory | B-07 | Complete | Complete | Complete | Complete | D-117; MKT-140; D-026 | SPECIFIED |
| `SCR-041` | Cities overview | Mandatory | B-05 | Complete | Complete | Complete | Complete | URB-031; D-067 | SPECIFIED |
| `SCR-042` | City detail | Mandatory | B-05 | Complete | Complete | Complete | Complete | URB-052/124…127; D-069/D-079 | SPECIFIED |
| `SCR-043` | Construction queue & preview | Mandatory | B-05 | Complete | Complete | Complete | Complete | URB-064/148; D-073/D-074 | SPECIFIED |
| `SCR-044` | Production facility chains | Mandatory | B-05 | Complete | Complete | Complete | Complete | URB-149; ECN-147/147a | SPECIFIED |
| `SCR-045` | Research view | Mandatory | B-05 | Complete | Complete | Complete | Complete | URB-102/150; D-076/077/078; URB-095 | SPECIFIED |
| `SCR-046` | Found new city flow | Mandatory | B-05 | Complete | Complete | Complete | Complete | URB-032/033/034; D-068 | SPECIFIED |
| `SCR-047` | Diplomatic overview | Mandatory | B-08 | Complete | Complete | Complete | Complete | 08C §12.2; DIP-030 | SPECIFIED |
| `SCR-048` | Pair screen | Mandatory | B-08 | Complete | Complete | Complete | Complete | DIP-023/024; NET-023 | SPECIFIED |
| `SCR-049` | Proposal & negotiation | Mandatory | B-08 | Complete | Complete | Complete | Complete | D-030; 08C §12.3 | SPECIFIED |
| `SCR-050` | Agreement / treaty detail | Mandatory | B-08 | Complete | Complete | Complete | Complete | DP-T01…T03; DP-A01 | SPECIFIED |
| `SCR-051` | Publication & visibility state | Mandatory | B-08 | Complete | Complete | Complete | Complete | DIP-108…113 | SPECIFIED |
| `SCR-052` | Relations history | Mandatory | B-08 | Complete | Complete | Complete | Complete | Class P/S; 08C §12.6 | SPECIFIED |
| `SCR-053` | Alliance home | Mandatory | B-09 | Complete | Complete | Complete | Complete | ALL-086 | SPECIFIED |
| `SCR-054` | Alliance membership & applicants | Mandatory | B-09 | Complete | Complete | Complete | Complete | ALL-080…086; UD-040 open | SPECIFIED |
| `SCR-055` | Alliance governance & roles | Mandatory | B-09 | Complete | Complete | Complete | Complete | D-135; AN matrix; REQ-553 | SPECIFIED |
| `SCR-056` | Alliance tax brackets | Mandatory | B-09 | Complete | Complete | Complete | Complete | ALL-179…187; UD-040/UD-045 | SPECIFIED |
| `SCR-057` | Alliance finances | Mandatory | B-09 | Complete | Complete | Complete | Complete | ALL-187/193/220…226; D-141; UD-046 | SPECIFIED |
| `SCR-058` | Alliance diplomacy | Mandatory | B-09 | Complete | Complete | Complete | Complete | D-140; AT-E00/E01; WAR-149; UD-047 | SPECIFIED |
| `SCR-059` | Military overview | Mandatory | B-10 | Complete | Complete | Complete | Complete | D-015 as 10B-C3; WAR-039 | SPECIFIED |
| `SCR-060` | Forces & upkeep | Mandatory | B-10 | Complete | Complete | Complete | Complete | WAR-049…053; WAR-109f…m | SPECIFIED |
| `SCR-061` | War Operations Board | Mandatory | B-10 | Complete | Complete | Complete | Complete | Roadmap boundary; WAR-148/161; REQ-589…591 | SPECIFIED |
| `SCR-062` | Conflicts ledger | Mandatory | B-10 | Complete | Complete | Complete | Complete | WAR-085…088 public fields | SPECIFIED |
| `SCR-063` | War detail | Mandatory | B-10 | Complete | Complete | Complete | Complete | WAR-085…088; WAR-150 | SPECIFIED |
| `SCR-064` | Battle report | Mandatory | B-10 | Complete | Complete | Complete | Complete | WAR-088; WAR-109k | SPECIFIED |
| `SCR-065` | War reports & losses | Mandatory | B-10 | Complete | Complete | Complete | Complete | WAR-109f…m; conservation accounting | SPECIFIED |
| `SCR-066` | Military history archive | Mandatory | B-10/B-11 | Complete | Complete | Complete | Complete | D-026 retention | SPECIFIED |
| `SCR-067` | Settlement & peace proposal | Mandatory | B-10 | Complete | Complete | Complete | Complete | WAR-126…129/131/132; UD-032 Option A | SPECIFIED |
| `SCR-068` | Strategic intelligence | Provisional | B-10 (none) | Complete | Complete | Complete | Complete | Espionage excluded; `13A-OQ-010`; no rule | BLOCKED |
| `SCR-069` | Events Centre | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-633/713; WPC-14 | SPECIFIED |
| `SCR-070` | Event detail & consequence | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-179/619; publication limits | SPECIFIED |
| `SCR-071` | Objectives & Challenges | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-203…215 | SPECIFIED |
| `SCR-072` | Standings | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-324/325/359/361/362 | SPECIFIED |
| `SCR-073` | Achievements & rewards | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-499/663 | SPECIFIED |
| `SCR-074` | National Progress | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-423 eight layers | SPECIFIED |
| `SCR-075` | Reward History | Mandatory | B-11 | Complete | Complete | Complete | Complete | WEP-633/663/705 | SPECIFIED |
| `SCR-076` | World Chronicle | Mandatory | B-11 | Complete | Complete | Complete | Complete | D-026; TR-049 | SPECIFIED |
| `SCR-077` | World Health aggregates | Conditional | B-11 | Complete | Complete | Complete | Complete | D-027 k=5 per figure | PROVISIONAL |
| `SCR-078` | World Guide & glossary | Mandatory | all | Complete | Complete | Complete | Complete | F-010; DP-004; `13A-BP-009` | SPECIFIED |
| `SCR-079` | Privacy settings centre | Mandatory | B-12 | Complete | Complete | Complete | Complete | PRV-002/009/014 | SPECIFIED |
| `SCR-080` | Security settings | Mandatory | B-03/B-12 | Complete | Complete | Complete | Complete | D-029/D-041; ACC-031 | SPECIFIED |
| `SCR-081` | Report creation | Mandatory | B-12 | Complete | Complete | Complete | Complete | MOD-002/007; FR-001/006 | SPECIFIED |
| `SCR-082` | Report status & decision | Mandatory | B-12 | Complete | Complete | Complete | Complete | MOD-017/018; EVD-009 | SPECIFIED |
| `SCR-083` | Appeal view | Mandatory | B-12 | Complete | Complete | Complete | Complete | MOD-013/015 | SPECIFIED |
| `SCR-084` | Restrictions & sanctions | Mandatory | B-03/B-12 | Complete | Complete | Complete | Complete | NET-023/050; PRV-019; MOD-027 | SPECIFIED |
| `SCR-085` | My data | Mandatory | B-03/B-12 | Complete | Complete | Complete | Complete | D-026; DAT-001; PRV-001 | SPECIFIED |
| `SCR-086` | Review explanation | Mandatory | B-03/B-12 | Complete | Complete | Complete | Complete | D-033/D-034; NET-023 | SPECIFIED |
| `SCR-087` | Support centre | Mandatory | B-12 | Complete | Complete | Complete | Complete | Intake taxonomy; FR-001 | SPECIFIED |
| `SCR-088` | Change disclosures | Mandatory | B-02/B-12 | Complete | Complete | Complete | Complete | TR-049; MOD-017 | SPECIFIED |
| `SCR-089` | Protection state | Mandatory | B-03 | Complete | Complete | Complete | Complete | ONB-020/022; D-040; WAR-115…117 | SPECIFIED |
| `SCR-090` | Reroll confirmation | Mandatory | B-03 | Complete | Complete | Complete | Complete | RRL-005/006/012/021; D-039 | SPECIFIED |
| `SCR-091` | Admin console home | Mandatory (admin) | B-12 | Complete | Complete | Complete | Complete | ADM-003/021/022; D-042 | SPECIFIED |
| `SCR-092` | Moderation queue | Mandatory (admin) | B-12 | Complete | Complete | Complete | Complete | ADM-021/022 | SPECIFIED |
| `SCR-093` | Case & evidence workspace | Mandatory (admin) | B-12 | Complete | Complete | Complete | Complete | EVD classes; V-01…V-16 | SPECIFIED |
| `SCR-094` | Sanctions administration | Mandatory (admin) | B-12/B-08 | Complete | Complete | Complete | Complete | MOD-036/037/042; MOD-022 | SPECIFIED |
| `SCR-095` | Shared-network review | Mandatory (admin) | B-03/B-12 | Complete | Complete | Complete | Complete | D-033/D-034 | SPECIFIED |
| `SCR-096` | Audit ledger viewer | Mandatory (admin) | B-12 | Complete | Complete | Complete | Complete | SEC-021/036…040; EVD-026; REQ-851…855 | SPECIFIED |
| `SCR-097` | Turn-engine operations monitor | Mandatory (admin) | B-02 | Complete | Complete | Complete | Complete | TR-035/036/043/075/080 | SPECIFIED |
| `SCR-098` | Data operations | Mandatory (admin) | B-12 | Complete | Complete | Complete | Complete | D-026; PRV-023; COR rules | SPECIFIED |
| `SCR-099` | Announcement composer | Mandatory (admin) | B-12/B-09 | Complete | Complete | Complete | Complete | MOD-017/018; ALL-164 | SPECIFIED |
| `SCR-100` | Admin roles & permissions | Mandatory (admin) | B-12 | Complete | Complete | Complete | Complete | ADM-003; D-042; FR postures | SPECIFIED |

**Tally:** 100 rows; 95 SPECIFIED, 2 PROVISIONAL (`SCR-020`, `SCR-077`), 3 BLOCKED (`SCR-038`, `SCR-039`, `SCR-068`). Classes preserved: 85 Mandatory player, 4 Conditional player (`SCR-020/038/039/077`), 1 Provisional player (`SCR-068`), 10 Mandatory admin.

**Citation reconciliation note.** The 13A inventory's `SCR-096` shorthand "SEC-031 spine" predates the B-12 canonical identifiers. B-13 cites the actual audit-spine rules (`SEC-021`, `SEC-036`…`SEC-040`, `EVD-026`, `REQ-851`…`REQ-855`); `SEC-031` in B-12 is the prototype treasury-grant defect, and no B-13 screen cites it as an audit rule. The 13A text is preserved unchanged; this note is the reconciliation.

## 25. Matrix B — Component usage

Columns: component, name, family, screens using it (representative complete set of owning screens; each screen body also names its components), states defined, responsive, accessibility, requirements. `Global` components are used by all authenticated screens; the screen list names the distinctive users. Overlays are listed separately with their existing IDs.

| Component | Name | Family | Screens using it | States | Responsive | A11y | Requirements |
|---|---|---|---|---|---|---|---|
| `UI-CMP-001` | Global application shell | Shell | All authenticated + public reduced shell | default, loading, error, stale, permission-denied | Complete | Complete | `REQ-970` |
| `UI-CMP-002` | Primary navigation | Shell | All authenticated (not Admin root) | default, hover, focus-visible, active, disabled+reason, overflow | Complete | Complete | `REQ-971`, `REQ-1013` |
| `UI-CMP-003` | Secondary navigation | Shell | `SCR-021`…`SCR-028`, `SCR-029`…`SCR-040`, `SCR-041`…`SCR-046`, `SCR-047`…`SCR-058`, `SCR-059`…`SCR-068`, `SCR-069`…`SCR-078` | default, hover, focus-visible, active, disabled+reason | Complete | Complete | `REQ-972` |
| `UI-CMP-004` | Page heading | Shell | All screens | default, loading title, error title | Complete | Complete | `REQ-1013` |
| `UI-CMP-005` | Breadcrumb / context locator | Shell | Every screen at depth ≥ 2 | default, truncated-path, permission-limited | Complete | Complete | `REQ-973` |
| `UI-CMP-006` | Account & nation context | Shell | All authenticated; reduced on public | default, unverified, restricted, closed, pending-closure | Complete | Complete | `REQ-974` |
| `UI-CMP-007` | Turn & settlement indicator | Shell | All authenticated; public shows cadence only | default, open, locked, resolving, interrupted, failed, stale | Complete | Complete | `REQ-975`, `REQ-1007` |
| `UI-CMP-008` | Global notification indicator | Shell | All authenticated | default, pending, danger, muted, non-opt-out | Complete | Complete | `REQ-976` |
| `UI-CMP-009` | Contextual navigation | Shell | All object/detail/task screens (global scope) | default, permission-limited, conditional-absent | Complete | Complete | `REQ-977` |
| `UI-CMP-010` | Admin entry and role-gated navigation | Shell | `SCR-091`…`SCR-100` only | default, denied, step-up-required, emergency | Complete | Complete | `REQ-978`, `REQ-1037` |
| `UI-CMP-011` | Footer / help access | Shell | All screens | default, degraded-support | Complete | Complete | `REQ-979` |
| `UI-CMP-012` | Statistic card | Display | `SCR-013/015/021/023/029/041/059/072/074` | default, loading, zero-real, forecast, suppressed, stale | Complete | Complete | `REQ-980` |
| `UI-CMP-013` | Metric group | Display | `SCR-013/015/029/041/059/072` | default, loading, partial, suppressed | Complete | Complete | `REQ-981` |
| `UI-CMP-014` | Financial summary | Display | `SCR-029/030/031/037/057` | default, negative-projected, zero, forecast, stale | Complete | Complete | `REQ-982` |
| `UI-CMP-015` | Resource balance display | Display | `SCR-033/035/036/037/042/043/056/057` | default, reserved, empty, capacity-full, suppressed | Complete | Complete | `REQ-983` |
| `UI-CMP-016` | Progress indicator | Display | `SCR-016/025/043/045/074` | default, pending, success, warning, error, indeterminate | Complete | Complete | `REQ-984` |
| `UI-CMP-017` | Status banner | Display | `SCR-021`…`SCR-028`, `SCR-084/089/090`, admin status | default, informational, pending, success, warning, danger, locked | Complete | Complete | `REQ-985` |
| `UI-CMP-018` | Warning panel | Display | `SCR-015/028/030/043/063/084/089` | default, warning, danger, suppressed | Complete | Complete | `REQ-986` |
| `UI-CMP-019` | Information panel | Display | All read surfaces | default, loading, empty, provisional-block | Complete | Complete | `REQ-987` |
| `UI-CMP-020` | Historical record | Display | `SCR-017/031/052/066/075/076/085` | default, retention-boundary, restricted, retired | Complete | Complete | `REQ-988`, `REQ-1008` |
| `UI-CMP-021` | Timeline | Display | `SCR-017/027/050/051/052/066/070/076` | default, pending, completed, voided, suppressed | Complete | Complete | `REQ-989` |
| `UI-CMP-022` | Data table | Display | `SCR-014/019/031/035/040/047/053/062/066/072/092/096` | default, loading, empty, sorted, filtered, permission-limited | Complete | Complete | `REQ-990` |
| `UI-CMP-023` | Filter row | Display | All table screens with filtering (global scope) | default, active-filter, invalid, clear | Complete | Complete | `REQ-991` |
| `UI-CMP-024` | Pagination | Display | Same table screens; all lists > 1 page | default, first, middle, last, exact-count | Complete | Complete | `REQ-992` |
| `UI-CMP-025` | Saved view | Display | `SCR-019/031/040/047/062/066/072` | default, dirty, invalid, permission-denied | Complete | Complete | `REQ-993` |
| `UI-CMP-026` | Search and jump-to-object | Display | Shell quick-go; `SCR-010/018/053/072` | default, no-result, loading, denied-object | Complete | Complete | `REQ-994`, `REQ-1003` |
| `UI-CMP-027` | Object reference link | Display | Every screen citing an object | default, hover, focus-visible, visited, denied, retired | Complete | Complete | `REQ-995` |
| `UI-CMP-028` | Object peek preview | Display | Every object-link list | default, loading, empty, denied, suppressed | Complete | Complete | `REQ-996` |
| `UI-CMP-029` | Detail section | Display | All object pages and detail records (global scope) | default, collapsed, expanded, empty, provisional | Complete | Complete | `REQ-997` |
| `UI-CMP-030` | Comparison panel | Display | `SCR-015/022/023/042/063/072` | default, partial, suppressed, not-comparable | Complete | Complete | `REQ-998` |
| `UI-CMP-031` | Treasury summary | Economic | `SCR-029/030/031/057` | default, zero, projected-negative, stale | Complete | Complete | `REQ-999` |
| `UI-CMP-032` | Income & expenditure breakdown | Economic | `SCR-029/030/031` | default, capex/opex, forecast, incomplete | Complete | Complete | `REQ-1000` |
| `UI-CMP-033` | Total/reserved/available register | Economic | Every balance-bearing screen | default, reserved, available-zero, suppressed | Complete | Complete | `REQ-1001` |
| `UI-CMP-034` | Capacity bar | Economic | `SCR-033/034/042/043/044/045` | default, full, reserved, derated, unmaintained | Complete | Complete | `REQ-1002` |
| `UI-CMP-035` | Production chain | Economic | `SCR-032/044` | default, running, target, idle, unmaintained, power-short | Complete | Complete | `REQ-1004` |
| `UI-CMP-036` | Construction queue item | Economic | `SCR-042/043` | default, pending, resolving, cancelled, failed, complete | Complete | Complete | `REQ-1005` |
| `UI-CMP-037` | Research project card | Economic | `SCR-045` | locked, available, in-progress, complete, prerequisite-missing | Complete | Complete | `REQ-1006` |
| `UI-CMP-038` | Approval & stability presentation | Political | `SCR-021/023/028` | default, six-supports, warning, crisis, recovery | Complete | Complete | `REQ-1009` |
| `UI-CMP-039` | Political state banner | Political | `SCR-021`…`SCR-028` and every consequence-bearing block | six states + transition/crisis explanatory variants | Complete | Complete | `REQ-1010` |
| `UI-CMP-040` | Policy control | Political | `SCR-024` | default, available, cooldown, blocked-by-state, confirmation | Complete | Complete | `REQ-1011` |
| `UI-CMP-041` | Election date presentation | Political | `SCR-025/027/028` | scheduled, open, closed, delayed, resolved | Complete | Complete | `REQ-1012` |
| `UI-CMP-042` | Campaign action control | Political | `SCR-026` | available, charged, blocked-by-state, limit-reached | Complete | Complete | `REQ-1018` |
| `UI-CMP-043` | Diplomatic relationship indicator | Diplomatic | `SCR-047/048/053/058` and profile | friendly, neutral, tense, hostile, unknown | Complete | Complete | `REQ-1019` |
| `UI-CMP-044` | Directional relationship presentation | Diplomatic | `SCR-048/047` | both-directions, one-direction, embargo, suppressed | Complete | Complete | `REQ-1020` |
| `UI-CMP-045` | Treaty status | Diplomatic | `SCR-047/050/051/052/058` | proposed, pending, accepted, active, expiring, terminated, expired, record-only | Complete | Complete | `REQ-1021` |
| `UI-CMP-046` | Proposal summary | Diplomatic | `SCR-014/047/049/050` | pending, countered, accepted, rejected, withdrawn, expired | Complete | Complete | `REQ-1022` |
| `UI-CMP-047` | Negotiation panel | Diplomatic | `SCR-049/067` | default, counter, withdraw, blocked, confirmation | Complete | Complete | `REQ-1023` |
| `UI-CMP-048` | Publication status | Diplomatic | `SCR-050/051/058` | pending-private, accepted-private, active-public, record-only | Complete | Complete | `REQ-1024` |
| `UI-CMP-049` | Alliance membership row | Alliance | `SCR-053/054/055` | member, applicant, non-covered, officer, former | Complete | Complete | `REQ-1025` |
| `UI-CMP-050` | Applicant status | Alliance | `SCR-054` | pending, admitted, declined, expired, withdrawn | Complete | Complete | `REQ-1026` |
| `UI-CMP-051` | Alliance financial summary | Alliance | `SCR-057/056` | received, available, reserved, expended, zero-fallback | Complete | Complete | `REQ-1027` |
| `UI-CMP-052` | Alliance receipt | Alliance | `SCR-057/056` | issued, immutable, corrected-by-append | Complete | Complete | `REQ-1028` |
| `UI-CMP-053` | Restriction explanation | Alliance/support | `SCR-048/055/058/084/086` | role-denied, pair-restricted, nAP-block, same-alliance-block, state-block | Complete | Complete | `REQ-1029` |
| `UI-CMP-054` | War summary | Warfare | `SCR-059/061/062/063` | declared, active, interrupted, settled, surrendered | Complete | Complete | `REQ-1030` |
| `UI-CMP-055` | War status strip | Warfare | `SCR-061/063` | per lifecycle state + protection | Complete | Complete | `REQ-1031` |
| `UI-CMP-056` | Operations summary | Warfare | `SCR-061` | default, reserved, executing, failed, released | Complete | Complete | `REQ-1032` |
| `UI-CMP-057` | OP balance & reservation | Warfare | `SCR-059/061` | default, capped, reserved, regenerated-zero, spend | Complete | Complete | `REQ-1033` |
| `UI-CMP-058` | Threat & odds band | Warfare | `SCR-061/063` | low, moderate, high, severe, unknown | Complete | Complete | `REQ-1034` |
| `UI-CMP-059` | Battle record | Warfare | `SCR-061/064/065` | default, public-summary, participant-detail, suppressed | Complete | Complete | `REQ-1035` |
| `UI-CMP-060` | Battle outcome | Warfare | `SCR-064/065` | win, loss, stalemate, interrupted, voided | Complete | Complete | `REQ-1036` |
| `UI-CMP-061` | Military history | Warfare | `SCR-066` | default, retention-bound, restricted | Complete | Complete | `REQ-1038` |
| `UI-CMP-062` | Nation-owner operation controls | Warfare | `SCR-061` only | default, disabled+reason, confirmation, executing, released | Complete | Complete | `REQ-1039` |
| `UI-CMP-063` | Event card | World | `SCR-013/069/070` | scheduled, active, resolved, expired, suppressed | Complete | Complete | `REQ-1040` |
| `UI-CMP-064` | Event consequence presentation | World | `SCR-070` | cause, effect, mitigation, historical | Complete | Complete | `REQ-1041` |
| `UI-CMP-065` | Objective card | World | `SCR-009/071` | available, accepted, progress, completed, deferred, expired | Complete | Complete | `REQ-1042` |
| `UI-CMP-066` | Achievement card | World | `SCR-073/075` | locked, earned, historical, deferred-claim | Complete | Complete | `REQ-1043` |
| `UI-CMP-067` | Ranking row | World | `SCR-072/010` | ranked, tied, ineligible, suppressed, historical | Complete | Complete | `REQ-1044` |
| `UI-CMP-068` | Ranking summary | World | `SCR-072` | denominator-window, no-live, empty | Complete | Complete | `REQ-1045` |
| `UI-CMP-069` | Notification item | World | `SCR-013/019/014` | informational, pending, warning, danger, muted, non-opt-out | Complete | Complete | `REQ-1046` |
| `UI-CMP-070` | Pending-action item | World | `SCR-014` and owning screens | pending, due-soon, overdue-boundary, cancellable, non-cancellable | Complete | Complete | `REQ-1047` |
| `UI-CMP-071` | Chronicle record | World | `SCR-017/076/070/075` | public, class-P, class-O-boundary, retired | Complete | Complete | `REQ-1048` |
| `UI-CMP-072` | Suppression indicator | World | Every aggregate surface | suppressed, insufficient-sample, not-disclosed | Complete | Complete | `REQ-1056`, `REQ-1066` |
| `UI-CMP-073` | Historical reward record | World | `SCR-075/073` | granted, deferred, voided, corrected | Complete | Complete | `REQ-1043` |
| `UI-CMP-074` | Text input | Form | All forms | default, hover, focus, disabled+reason, error, success, read-only | Complete | Complete | `REQ-1049` |
| `UI-CMP-075` | Numeric input | Form | `SCR-036/043/046/056/072` | default, integer-only, invalid, out-of-range, disabled+reason | Complete | Complete | `REQ-1049` |
| `UI-CMP-076` | Select control | Form | All filter and form surfaces | default, open, selected, disabled+reason, error | Complete | Complete | `REQ-1049` |
| `UI-CMP-077` | Multi-select control | Form | `SCR-036/056/077` and filters | default, selected-many, limit-reached, disabled | Complete | Complete | `REQ-1049` |
| `UI-CMP-078` | Checkbox | Form | `SCR-002/026/081/092` | default, checked, indeterminate, disabled+reason, error | Complete | Complete | `REQ-1049` |
| `UI-CMP-079` | Radio control | Form | `SCR-007/024/049/067` | default, selected, disabled+reason, error | Complete | Complete | `REQ-1049` |
| `UI-CMP-080` | Toggle | Form | `SCR-032/079/080` | on, off, pending, disabled+reason, error | Complete | Complete | `REQ-1049` |
| `UI-CMP-081` | Date/turn selector | Form | `SCR-025/031/040/052/066/072` | default, turn-range, invalid, provisional-window | Complete | Complete | `REQ-1049` |
| `UI-CMP-082` | Search field | Form | `SCR-010/018/026/072/078/092` | default, typing, results, no-result, denied, loading | Complete | Complete | `REQ-1049` |
| `UI-CMP-083` | Form field group | Form | All task screens | default, required, optional, error, grouped-help | Complete | Complete | `REQ-1049` |
| `UI-CMP-084` | Validation message | Form | All forms | inline, summary, error, warning, success, provisional | Complete | Complete | `REQ-1049` |
| `UI-CMP-085` | Primary action button | Action | All committing screens | default, hover, focus, active, disabled+reason, loading, success, pending | Complete | Complete | `REQ-1049` |
| `UI-CMP-086` | Secondary action button | Action | All screens with a secondary path | same as primary minus success | Complete | Complete | `REQ-1049` |
| `UI-CMP-087` | Destructive action button | Action | `SCR-012/043/090`; admin `SCR-094` | default, hover, focus, disabled+reason, confirmation-required | Complete | Complete | `REQ-1049` |
| `UI-CMP-088` | Confirmation panel | Action | Every committing control | default, pending, warning, error, success, exact-phrase | Complete | Complete | `REQ-1049` |
| `UI-CMP-089` | Disabled action with reason | Action | Every disabled control | default, reason-visible, rule-linked, permission-denied | Complete | Complete | `REQ-1049` |
| `UI-CMP-090` | Exact-phrase confirmation field | Action | `SCR-090`; admin destructive actions | default, mismatch, match, disabled | Complete | Complete | `REQ-1049` |
| `OVL-01` | Confirmation dialog | Overlay | Every committing control | open, pending, error, success | Complete | Complete | `REQ-1049` |
| `OVL-02` | Destructive exact-phrase dialog | Overlay | `SCR-090`, `SCR-094`, `SCR-012` | open, mismatch, match, pending | Complete | Complete | `REQ-1049` |
| `OVL-03` | Reason popover | Overlay | Every disabled control | open, focus-dismiss, rule-link | Complete | Complete | `REQ-1049` |
| `OVL-04` | Definition / cause-chain drawer | Overlay | All read surfaces | open, loading, empty, deep-linked page | Complete | Complete | `REQ-1049` |
| `OVL-05` | Object peek card | Overlay | Every object link | open, loading, denied, suppressed | Complete | Complete | `REQ-1049` |
| `OVL-06` | Boundary-effect notice | Overlay | Shell (all authenticated screens) | settled, pending, failed, interrupted | Complete | Complete | `REQ-1049` |
| `OVL-07` | Suppression notice | Overlay | Every aggregate | suppressed, insufficient-sample | Complete | Complete | `REQ-1049` |
| `OVL-08` | Claim-vocabulary badge | Overlay | `SCR-082/084/086` only | suspected, under-review, confirmed, inconclusive | Complete | Complete | `REQ-1049` |

**Component tally:** 90 `UI-CMP` components across seven families + 8 existing overlays; all fully specified in the component companion, all with responsive and accessibility sections, all with defined applicable states. `REQ-970`…`REQ-1049` are the cross-cutting shell and component requirements, and `REQ-1050`…`REQ-1089` are the responsive, accessibility, permission, visualization, design-system and traceability requirements; each component body names its exact requirement set.

### 25.1 Reverse lookup — components by screen (derived from Matrix B)

Matrix B remains authoritative. This derived index inverts it so a developer can see a screen's component set directly; it adds no new mapping. The shell rows cover common components; a screen's body may name a component not repeated here only if the body and Matrix B also name it.

| Screen | Components |
|---|---|
| `SCR-001` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-002` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-003` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-004` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-005` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-006` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-007` | `UI-CMP-001`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-011` |
| `SCR-008` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-009` | `UI-CMP-065`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-010` | `UI-CMP-026`, `UI-CMP-082`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-011` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-012` | `UI-CMP-087`, `OVL-02`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-013` | `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-063`, `UI-CMP-069`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-014` | `UI-CMP-022`, `UI-CMP-046`, `UI-CMP-070`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-015` | `UI-CMP-018`, `UI-CMP-030`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-016` | `UI-CMP-016`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-017` | `UI-CMP-020`, `UI-CMP-021`, `UI-CMP-071`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-018` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-019` | `UI-CMP-025`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-020` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-021` | `UI-CMP-003`, `UI-CMP-017`, `UI-CMP-038`, `UI-CMP-039`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-022` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-023` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-024` | `UI-CMP-040`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-025` | `UI-CMP-041`, `UI-CMP-081`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-026` | `UI-CMP-042`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-027` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-028` | `UI-CMP-003`, `UI-CMP-017`, `UI-CMP-039`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-029` | `UI-CMP-003`, `UI-CMP-014`, `UI-CMP-031`, `UI-CMP-032`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-030` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-031` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-032` | `UI-CMP-035`, `UI-CMP-080`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-033` | `UI-CMP-015`, `UI-CMP-034`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-034` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-035` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-036` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-037` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-038` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-039` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-040` | `UI-CMP-003`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-041` | `UI-CMP-003`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-042` | `UI-CMP-036`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-043` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-044` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-045` | `UI-CMP-037`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-046` | `UI-CMP-003`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-047` | `UI-CMP-003`, `UI-CMP-043`, `UI-CMP-045`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-048` | `UI-CMP-044`, `UI-CMP-053`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-049` | `UI-CMP-047`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-050` | `UI-CMP-048`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-051` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-052` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-053` | `UI-CMP-049`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-054` | `UI-CMP-050`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-055` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-056` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-057` | `UI-CMP-051`, `UI-CMP-052`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-058` | `UI-CMP-003`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-059` | `UI-CMP-003`, `UI-CMP-054`, `UI-CMP-057`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-060` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-061` | `UI-CMP-055`, `UI-CMP-056`, `UI-CMP-058`, `UI-CMP-059`, `UI-CMP-062`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-062` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-063` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-064` | `UI-CMP-060`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-065` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-066` | `UI-CMP-061`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-067` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-068` | None (no rule exists) |
| `SCR-069` | `UI-CMP-003`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-070` | `UI-CMP-064`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-071` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-072` | `UI-CMP-067`, `UI-CMP-068`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-073` | `UI-CMP-066`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-074` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-075` | `UI-CMP-073`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-076` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-077` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-078` | `UI-CMP-003`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-079` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-080` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-081` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-082` | `OVL-08`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-083` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-084` | `UI-CMP-017`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-085` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-086` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-087` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-088` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-089` | `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-090` | `UI-CMP-090`, `OVL-02`, `UI-CMP-001`, `UI-CMP-002`, `UI-CMP-004`, `UI-CMP-005`, `UI-CMP-006`, `UI-CMP-007`, `UI-CMP-008`, `UI-CMP-009`, `UI-CMP-011` |
| `SCR-091` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-092` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-093` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-094` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010`, `OVL-02` |
| `SCR-095` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-096` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-097` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-098` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-099` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |
| `SCR-100` | `UI-CMP-011`, `UI-CMP-004`, `UI-CMP-010` |


## 26. Matrix C — B-13 requirements register

**Allocation:** `REQ-870`…`REQ-1089` (220 requirements). `REQ-870` is the first identifier after the verified global frontier `REQ-869`; no earlier `REQ-` row is renumbered, reworded, duplicated or status-changed. `REQ-870`…`REQ-969` are one-per-screen presentation requirements (`REQ = 869 + SCR number`); `REQ-970`…`REQ-1049` are shell/component requirements; `REQ-1050`…`REQ-1089` are responsive, accessibility, permission, visualization, design-system and traceability requirements. The next free identifier after this block is `REQ-1090`.

**Status vocabulary:** `SPECIFIED` — fully specified presentation duty, currently authorised as a specification; `PROVISIONAL` — specified but gated by named evidence or an owner-reserved question; `BLOCKED` — the surface/feature must not be provided until a named gate or rule exists (the omission duty is specified in the same row). No row is `APPROVED`, `IMPLEMENTED`, `VALIDATED` or `RELEASED`; none of those states has been earned.

**Verification intent vocabulary:** `Structure` (document/specification inspection), `Review` (human semantic review), `Runtime` (future built-UI test — **not performed** in this pass). A `Runtime` intent is a plan, never a result.

### 26.1 Screen-level requirements (REQ-870…REQ-969)

| ID | Requirement | Category | Priority | Governing source | Screens | Components | Dependencies | Status | Verification intent |
|---|---|---|---|---|---|---|---|---|---|
| `REQ-870` | The Landing screen shall state the fictional-world premise, expose exactly the public entry paths (register, login, rules, terms, privacy) and shall not display live player counts or any authenticated data below k=5. | Screen | P0 | B-03; `13A-SRC-001`; TR-022 | `SCR-001` | `UI-CMP-004`, `UI-CMP-011`, `UI-CMP-019` | D-007; `13A-OQ-001/002` | SPECIFIED | Review |
| `REQ-871` | Registration shall collect e-mail and confirmation, optional referrer, and the terms acknowledgement; it shall display the multi-account policy at entry and shall not create a nation before e-mail verification. | Screen | P0 | B-03 ACC; D-029; D-032; `13A-BP-014` | `SCR-002` | `UI-CMP-074`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-085` | D-018; NAT-001.2 | SPECIFIED | Structure |
| `REQ-872` | Login shall present credentials, keep-session and reset entry, shall render only the public reduced shell, and shall never display another account's national data in the shell preview. | Screen | P0 | B-03 ACC-018; D-041; `13A-SRC-017` | `SCR-003` | `UI-CMP-001`, `UI-CMP-074`, `UI-CMP-085`, `UI-CMP-086` | D-029 | SPECIFIED | Structure |
| `REQ-873` | Password reset initiation shall explain the reset route, shall not reveal whether an e-mail exists, and shall never create an account or nation. | Screen | P0 | B-03; D-041 | `SCR-004` | `UI-CMP-074`, `UI-CMP-084`, `UI-CMP-085` | D-041 | SPECIFIED | Review |
| `REQ-874` | Recovery-code entry shall accept a single-use recovery code, show its consumption state, and provide a path to account recovery without bypassing D-041 custody rules. | Screen | P0 | B-03; D-041; ACC-031 | `SCR-005` | `UI-CMP-074`, `UI-CMP-084`, `UI-CMP-085` | ACC-031 | SPECIFIED | Structure |
| `REQ-875` | E-mail verification shall show the pending unverified state, the resend affordance subject to its limit, and the verified transition; it shall not expose the verification token. | Screen | P0 | B-03; D-029; ACC-024 | `SCR-006` | `UI-CMP-017`, `UI-CMP-085`, `UI-CMP-084` | D-029 | SPECIFIED | Review |
| `REQ-876` | Nation creation shall collect name, short name, optional emblem from the game set and starting posture, show the D-038 validation feedback before submission, and display the `awaiting first turn` state after success. | Screen | P0 | B-03/B-04; NAT-002/015/016/026–030; D-038; D-063 | `SCR-007` | `UI-CMP-074`, `UI-CMP-083`, `UI-CMP-084`, `UI-CMP-088` | D-038; NAT-030 | SPECIFIED | Structure |
| `REQ-877` | Onboarding shall run inside the real shell with true zero-state values, present the guided first-session steps once, and never re-grant the one-time completion state. | Screen | P0 | B-03; D-040; ONB-009…038; `13A-BP-001` | `SCR-008` | `UI-CMP-001`, `UI-CMP-016`, `UI-CMP-019` | D-040 | SPECIFIED | Review |
| `REQ-878` | The first-turn objectives entry shall present objective categories and first-session guidance, link each item to its owning surface, and shall not award or complete an objective by the act of viewing it. | Screen | P1 | B-03/B-11; ONB surfaces; WEP-203…215 | `SCR-009` | `UI-CMP-065`, `UI-CMP-019` | ONB-013 | SPECIFIED | Review |
| `REQ-879` | The public nation profile shall render public identity and the twelve-section object structure within TR-021/TR-022 limits, shall show `awaiting first turn` or `retired — rerolled` where applicable, and shall never show e-mail, account ID, IP, recovery/enforcement state or pair restriction. | Screen | P0 | B-03/B-06/B-10/B-11; NAT-015; RRL-020; TR-021/022; D-036 | `SCR-010` | `UI-CMP-029`, `UI-CMP-021`, `UI-CMP-067`, `UI-CMP-027` | NAT-041; D-036 | SPECIFIED | Review |
| `REQ-880` | Account home shall display the account state, nation linkage, sessions/recovery entry, closure entry and support entry, using ACC-018's neutral status wording for restricted or suspended states. | Screen | P0 | B-03; ACC-017/018; D-041 | `SCR-011` | `UI-CMP-006`, `UI-CMP-017`, `UI-CMP-009` | ACC-018 | SPECIFIED | Structure |
| `REQ-881` | Account closure shall disclose the 7-day cooling period, the retained restrictions, the inability to use closure as a shield, and the retention consequence before confirmation. | Screen | P0 | B-03; D-041; ACC-043; D-026 | `SCR-012` | `UI-CMP-017`, `UI-CMP-088`, `OVL-01` | ACC-043 | SPECIFIED | Review |
| `REQ-882` | The Command Digest shall present one bounded digest of settled changes, pending totals and due-boundary items from existing notification events, each with its cause chain and deep link, and shall not create a new event type or an open widget board. | Screen | P0 | B-02; TR-088/089/092; REQ-022 | `SCR-013` | `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-069`, `UI-CMP-021` | TR-089; REQ-731 | SPECIFIED | Review |
| `REQ-883` | The Inbox shall aggregate every pending offer, proposal, invitation, application and confirmation, order them by due boundary, show the owning system and state, and deep-link each row to its permitted action screen. | Screen | P0 | B-02 + B-07…B-09; TR-004; D-016/D-030 | `SCR-014` | `UI-CMP-070`, `UI-CMP-022`, `UI-CMP-023`, `UI-CMP-024` | MKT/ALL/AT lifecycles | SPECIFIED | Structure |
| `REQ-884` | National Overview shall present the headline national state as labelled registers (treasury, stability/approval, readiness, protection, population/housing, power) with six-number-type separation and links to each owning section. | Screen | P0 | B-04/B-05/B-06/B-10; ECN-176/177; URB-052; DMP-073 | `SCR-015` | `UI-CMP-012`, `UI-CMP-013`, `UI-CMP-018`, `UI-CMP-039` | ECN-177 | SPECIFIED | Structure |
| `REQ-885` | Turn and settlement status shall show the current turn, next UTC boundary, phase position, this nation's queued actions and the last settlement state including `unknown — retrying`, `INTERRUPTED` and `FAILED` as named states. | Screen | P0 | B-02; TR-027/030/033/035/036/039/075/080 | `SCR-016` | `UI-CMP-007`, `UI-CMP-022`, `UI-CMP-017` | TR-080 | SPECIFIED | Review |
| `REQ-886` | The National Chronicle shall present permanent class-P history with filters, as-of turns and retention labels, and shall distinguish public from restricted entries without exposing a restricted fact through counts or ordering. | Screen | P1 | B-11; D-026; TR-049 | `SCR-017` | `UI-CMP-020`, `UI-CMP-021`, `UI-CMP-071` | D-026 | SPECIFIED | Review |
| `REQ-887` | Network View shall render the mapless relationship graph with symbolic nation/alliance nodes, typed directional edges, filters, legend and object peeks; it shall contain no coordinates, distances, borders or geographic map anywhere. | Screen | P0 | B-02/B-08/B-09; TR-012/013/014; REQ-041; FO-013 | `SCR-018` | `UI-CMP-026`, `UI-CMP-027`, `UI-CMP-028`, `UI-CMP-043`, `UI-CMP-044` | §11 | SPECIFIED | Structure |
| `REQ-888` | Alerts and notification history shall present the existing notification events with the three presentation tiers, show non-opt-out items as non-mutable, and never mutate, suppress or fabricate an event. | Screen | P0 | B-02/B-11; REQ-731; DIP-114/116 | `SCR-019` | `UI-CMP-069`, `UI-CMP-022`, `UI-CMP-023` | REQ-731 | SPECIFIED | Structure |
| `REQ-889` | Pinned objects shall be absent until the fair-play review closes; when enabled it shall store only user-selected object references, show their current visibility state, and reveal no private fact through the pin list. | Screen | P2 | `13A-OQ-012`; B-12 fair-play review | `SCR-020` | `UI-CMP-027`, `UI-CMP-028` | `13A-OQ-012` | PROVISIONAL | Review |
| `REQ-890` | The Political Panel shall display the DMP-268 state banner, government identity, leader/administration separation, approval/stability summary and the six-support entry, and shall never present a transition or crisis as a ban or account penalty. | Screen | P0 | B-06; DMP-256/268; DMP-079…083 | `SCR-021` | `UI-CMP-039`, `UI-CMP-038`, `UI-CMP-012` | DMP-268 | SPECIFIED | Structure |
| `REQ-891` | Government structure shall present the permanent government identity, its leadership model, the five numeric channels and the policy permissions, with disadvantages shown at equal prominence to advantages before any creation confirmation. | Screen | P0 | B-06; D-084/D-085; D-086; DMP-081–084 | `SCR-022` | `UI-CMP-029`, `UI-CMP-030`, `UI-CMP-088` | D-084/D-085 | SPECIFIED | Review |
| `REQ-892` | Approval and stability shall display each of the six supports with weight, current and last-turn support, every named term and contribution, the derived approval and stability as integers with text labels, and no invented stability bands. | Screen | P0 | B-06; DMP-073; F-PD-004…009; DMP-053/054/056 | `SCR-023` | `UI-CMP-038`, `UI-CMP-030`, `OVL-04` | F-PD-004…009 | SPECIFIED | Structure |
| `REQ-893` | Policy axes shall show both axes' current settings, the per-axis change effect and cost, and the 12-turn cooldown on the control with the next eligible turn, and shall not allow a second change inside the cooldown. | Screen | P0 | B-06; D-087; DMP-101/102; `13A-BP-010` | `SCR-024` | `UI-CMP-040`, `UI-CMP-089`, `OVL-01` | D-087 | SPECIFIED | Structure |
| `REQ-894` | The election dashboard shall anchor every date on `campaign_open_turn` (`T−24`, `T−12`, `T−2` as on-time values), show turnout weights and published challengers, and shall not imply a live or wall-clock countdown. | Screen | P0 | B-06; D-106/D-107; DMP-178/184 | `SCR-025` | `UI-CMP-041`, `UI-CMP-022`, `UI-CMP-012` | D-106/D-107 | SPECIFIED | Review |
| `REQ-895` | The campaign actions centre shall offer exactly the three DMP-189 action types, show each action's points or crown cost and effect before submission, and reflect the charge-once rule with no cancellable reservation. | Screen | P0 | B-06; D-094; DMP-189/193 | `SCR-026` | `UI-CMP-042`, `UI-CMP-089`, `OVL-01` | D-094 | SPECIFIED | Review |
| `REQ-896` | The election result and transition view shall show the outcome-dependent banner, the 12-turn transition, the 800 bp stability penalty disclosure and the fact that the administration changes while the government does not. | Screen | P0 | B-06; DMP-184/205/210; D-097/D-098 | `SCR-027` | `UI-CMP-039`, `UI-CMP-021`, `UI-CMP-017` | DMP-205 | SPECIFIED | Review |
| `REQ-897` | Crisis and recovery shall display the crisis state, its exact end turn, the 18-turn stability-only effect, the recovery window, the immunity/exit rule and at least three concrete recovery actions with projected effects. | Screen | P0 | B-06; DMP-163; DMP-225/229/248 | `SCR-028` | `UI-CMP-039`, `UI-CMP-018`, `UI-CMP-016` | DMP-163 | SPECIFIED | Review |
| `REQ-898` | Treasury shall present the ECN-176 question set as six separated number registers, with current, reserved, forecast, historical and transaction figures visually distinct, and with an as-of turn on every figure. | Screen | P0 | B-04; ECN-176/177/178; D-050/D-051/D-062 | `SCR-029` | `UI-CMP-031`, `UI-CMP-032`, `UI-CMP-014`, `UI-CMP-012` | ECN-177 | SPECIFIED | Structure |
| `REQ-899` | Budget and national wealth shall separate opex from capex, label wealth as a report statistic rather than a spendable balance, and show the austerity order and three recovery options when the projected balance is negative. | Screen | P0 | B-04; D-051/D-062; ECN-105/107 | `SCR-030` | `UI-CMP-014`, `UI-CMP-032`, `UI-CMP-018` | ECN-107 | SPECIFIED | Review |
| `REQ-900` | Economic reports and history shall present append-only records with per-turn aggregates, the cause of each material change, the exact failure factor where applicable, filters and exports within retention classes. | Screen | P0 | B-04; ECN-142; D-026; TR-049 | `SCR-031` | `UI-CMP-020`, `UI-CMP-022`, `UI-CMP-023`, `OVL-04` | ECN-142 | SPECIFIED | Review |
| `REQ-901` | Production policy shall present standing policy, manual batch orders and the reservation preview, show affordability and capacity before submission, and distinguish `RUN_AT_CAPACITY`, `RUN_TO_TARGET` and `IDLE`. | Screen | P0 | B-04; D-053; ECN-044/045/053/139 | `SCR-032` | `UI-CMP-035`, `UI-CMP-075`, `UI-CMP-033` | ECN-053 | SPECIFIED | Structure |
| `REQ-902` | Resources and warehouse shall show total, reserved and available for every resource and for warehouse space, with capacity versus holdings and book values, and shall reject any total-only balance presentation. | Screen | P0 | B-04/B-05; MKT-053; ECN-120; URB-066 | `SCR-033` | `UI-CMP-033`, `UI-CMP-034`, `UI-CMP-022` | MKT-053 | SPECIFIED | Structure |
| `REQ-903` | Power grid shall present grid supply, processing demand, surplus/shortfall, `power_pct` and derated batches as derived capacity only, and shall never display a stored, traded or reserved power balance. | Screen | P0 | B-04/B-05; D-048; ECN-056/059/060/061/064 | `SCR-034` | `UI-CMP-034`, `UI-CMP-012`, `UI-CMP-019` | D-048 | SPECIFIED | Structure |
| `REQ-904` | The directed-trade inbox shall list incoming and outgoing chains with terms, revision, expiry turn, status and total/reserved/available balances, and shall state that creating an offer reserves nothing. | Screen | P0 | B-07; MKT-105/125; D-016; MKT-053 | `SCR-035` | `UI-CMP-022`, `UI-CMP-046`, `UI-CMP-033` | D-016 | SPECIFIED | Structure |
| `REQ-905` | Compose and counter offer shall collect up to five resource/crown lines per side, disclose the pledge and imbalance facts, show the 12-turn action window and rate-limit position, and confirm the exact terms before submission. | Screen | P0 | B-07; MKT-019/022/037/038/061; D-017 | `SCR-036` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-088`, `OVL-01` | MKT-061 | SPECIFIED | Review |
| `REQ-906` | Offer detail shall present the complete two-sided record, both parties' obligations, the atomic all-or-nothing settlement state and the shared transfer reference, visible only to the two parties and restricted audit. | Screen | P0 | B-07; MKT-056/131; ECON-054; D-017 | `SCR-037` | `UI-CMP-029`, `UI-CMP-022`, `UI-CMP-021` | ECON-054 | SPECIFIED | Review |
| `REQ-907` | The Global Trade board is BLOCKED: it shall be absent, with no preview, stub, beta board, partial listing or leaked statistic, until G-1…G-6 all pass; its absence is explained by `MKT-G01` where a user reaches the route. | Screen | P0 | B-07; D-117/D-122; MKT-073…077; G-1…G-6 | `SCR-038` | `UI-CMP-019` | G-1…G-6 all MET | BLOCKED | Structure |
| `REQ-908` | Listing detail and execution confirmation are BLOCKED with `SCR-038`; when the gate passes they shall show posted price, remaining quantity, partial-fill construction, the crossed badge and the exact execution consequence before confirmation. | Screen | P0 | B-07; D-111; MKT-106/107/108; G-1…G-6 | `SCR-039` | `UI-CMP-088`, `UI-CMP-015` | G-1…G-6 all MET | BLOCKED | Structure |
| `REQ-909` | Trade history and reference prices shall show only pre-gate minimal own history, label every post-gate statistic with its 12-turn window and sample count, and render `INSUFFICIENT_SAMPLE` as a named state rather than zero. | Screen | P1 | B-07; D-117; MKT-110/140; D-026 | `SCR-040` | `UI-CMP-020`, `UI-CMP-022`, `UI-CMP-072` | D-117 | SPECIFIED | Structure |
| `REQ-910` | The cities overview shall present all twelve cities and the capital on one screen with per-city infrastructure, development capacity, limits and status, and shall never paginate the twelve-city set into separate screens. | Screen | P0 | B-05; URB-031; D-067 | `SCR-041` | `UI-CMP-012`, `UI-CMP-022`, `UI-CMP-034` | D-067 | SPECIFIED | Structure |
| `REQ-911` | City detail shall show infrastructure within its 10–500 range, the housing formula components and hard/soft capacity, `used / total` DC and per-class breakdown, and the projected post-order capacity before commitment. | Screen | P0 | B-05; URB-052/124…127; D-069/D-079 | `SCR-042` | `UI-CMP-029`, `UI-CMP-034`, `UI-CMP-036` | URB-052 | SPECIFIED | Structure |
| `REQ-912` | The construction queue and preview shall show the one-slot-per-city constraint, the full URB-148 preview (cost after discounts, DC, slot, availability turn, book value, wealth effect), the 25% crown-only demolition refund and the cancel state. | Screen | P0 | B-05; URB-064/148; D-073/D-074; D-080 | `SCR-043` | `UI-CMP-036`, `UI-CMP-088`, `UI-CMP-089` | D-073 | SPECIFIED | Review |
| `REQ-913` | Production facility chains shall present each chain's batches, inputs, expected output, variable cost, maintenance, power draw, blocking reason and research bonus, with `UNMAINTAINED` shown as a named disabling state. | Screen | P0 | B-05; URB-149; ECN-147/147a | `SCR-044` | `UI-CMP-035`, `UI-CMP-034`, `UI-CMP-017` | ECN-147 | SPECIFIED | Structure |
| `REQ-914` | Research shall present the twelve-technology tree by branch, each project's RP/crown cost, prerequisites, effect, status (`locked`/`available`/`in progress`/`complete`), progress, turns, RP pool and generation, one-active-project limit and banked-RP versus programme spend. | Screen | P0 | B-05; URB-102/150/095; D-076/077/078 | `SCR-045` | `UI-CMP-037`, `UI-CMP-016`, `UI-CMP-022` | D-076 | SPECIFIED | Structure |
| `REQ-915` | Found new city shall show the founding cost gate (crowns and 20 steel), the national-infrastructure eligibility threshold, the expansion-slot state, the no-cooldown rule and the new-city starting state before confirmation. | Screen | P0 | B-05; URB-032/033/034; D-068 | `SCR-046` | `UI-CMP-088`, `UI-CMP-084`, `UI-CMP-089` | D-068 | SPECIFIED | Review |
| `REQ-916` | The diplomatic overview shall provide the six required views from 08C §12.2, show directional posture per pair, list agreements and embargoes with lifecycle state, and render the specified empty states without fake statistics or recommendations. | Screen | P0 | B-08; 08C §12.2/§12.5; DIP-023/024/030 | `SCR-047` | `UI-CMP-022`, `UI-CMP-043`, `UI-CMP-045` | 08C §12.2 | SPECIFIED | Structure |
| `REQ-917` | The pair screen shall show both directional postures side by side, bilateral agreements, breach count as a fact with no score, pair-restriction state where the viewer is the subject, and no pending terms of other pairs. | Screen | P0 | B-08; DIP-023/024/086/088; NET-023 | `SCR-048` | `UI-CMP-044`, `UI-CMP-045`, `UI-CMP-053` | NET-023 | SPECIFIED | Review |
| `REQ-918` | Proposal and negotiation shall show the counterparty-named pending state, the ten-field 08C §12.3 confirmation panel, the withdraw/counter paths permitted by the rules, and shall create no delegation of national sovereignty. | Screen | P0 | B-08; D-030; 08C §12.3 | `SCR-049` | `UI-CMP-046`, `UI-CMP-047`, `UI-CMP-088` | 08C §12.3 | SPECIFIED | Review |
| `REQ-919` | Agreement detail shall identify the exact type (`DP-T01`…`DP-T03` or `DP-A01`), lifecycle state, parties, obligations, duration, activation and termination rules, and shall not show an active badge for a pending or expired agreement. | Screen | P0 | B-08; DP-T01…T03; DP-A01; DIP-108…113 | `SCR-050` | `UI-CMP-045`, `UI-CMP-048`, `UI-CMP-021` | DIP-108…113 | SPECIFIED | Structure |
| `REQ-920` | Publication and visibility state shall show the pending-private → accepted-private → active-public progression, the exact public record fields, and k=5 aggregate suppression, with no public pending terms. | Screen | P0 | B-08; DIP-108…113; D-030 | `SCR-051` | `UI-CMP-048`, `UI-CMP-072`, `UI-CMP-021` | DIP-113 | SPECIFIED | Review |
| `REQ-921` | Relations history shall split private and public records by class, label retention boundaries, keep retired pages labelled `Retired`, and never merge a replacement nation's history into the prior identity. | Screen | P1 | B-08; 08C §12.6; D-026 | `SCR-052` | `UI-CMP-020`, `UI-CMP-021`, `UI-CMP-022` | D-026 | SPECIFIED | Review |
| `REQ-922` | Alliance home shall show public alliance identity, leadership roles, member count within disclosure rules, treaties and wars as public records, and shall never expose member internals or applicant identities to non-administrators. | Screen | P0 | B-09; ALL-086; `13A-SRC-006` | `SCR-053` | `UI-CMP-029`, `UI-CMP-049`, `UI-CMP-045` | ALL-086 | SPECIFIED | Review |
| `REQ-923` | Alliance membership and applicants shall show applicants only to the permitted administration, show member states and non-covered-member status, terminate applications in-product, and explain membership restrictions without exposing privacy data. | Screen | P0 | B-09; ALL-080…086; UD-040 open; D-133 | `SCR-054` | `UI-CMP-049`, `UI-CMP-050`, `UI-CMP-053` | ALL-086 | SPECIFIED | Review |
| `REQ-924` | Alliance governance shall present the player-authored constitution, the role/permission matrix with per-role explanations, and permission-denied states; rendering a control never grants the permission. | Screen | P0 | B-09; D-135; AN matrix; REQ-553 | `SCR-055` | `UI-CMP-022`, `UI-CMP-089`, `OVL-03` | REQ-553 | SPECIFIED | Review |
| `REQ-925` | Alliance tax brackets shall allow a player-named bracket with separate Crowns and per-resource integer rates 0–10,000 bp, member assignment, effective turn and policy version shown before confirmation, tax history, receipts and the visible 0% protective fallback while UD-040 is open. | Screen | P0 | B-09; ALL-179…187; UD-040/UD-045; `13A-SRC-021` | `SCR-056` | `UI-CMP-075`, `UI-CMP-077`, `UI-CMP-088`, `UI-CMP-052` | UD-040 Open | SPECIFIED | Review |
| `REQ-926` | Alliance finances shall show the four ARL categories (`RECEIVED`, `AVAILABLE`, `RESERVED`, `EXPENDED`), immutable receipts, the absent approved cost schedule and the explanatory unavailable-purpose state, with no withdrawal or distribution control. | Screen | P0 | B-09; ALL-187/193/220…226; D-141; UD-046 | `SCR-057` | `UI-CMP-051`, `UI-CMP-052`, `UI-CMP-019` | D-141 | SPECIFIED | Structure |
| `REQ-927` | Alliance diplomacy shall show alliance-to-alliance treaty objects with `AT-E00` record-only or `AT-E01` NAP effect, per-nation coverage and non-covered-member state, block reasons without private terms, and no collective military authority. | Screen | P0 | B-09; D-140; AT-E00/E01; WAR-149; UD-047 | `SCR-058` | `UI-CMP-045`, `UI-CMP-048`, `UI-CMP-053` | D-140 | SPECIFIED | Review |
| `REQ-928` | Military overview shall show this nation's OP balance, cap, regeneration and carry state, readiness and the entry to forces and the owner-only operations board, and shall show no other nation's military data. | Screen | P0 | B-10; D-015 as 10B-C3; WAR-039 | `SCR-059` | `UI-CMP-057`, `UI-CMP-012`, `UI-CMP-054` | D-015 | SPECIFIED | Structure |
| `REQ-929` | Forces and upkeep shall show unit roster, military Food demand and paid/short outcome at P3.7, readiness effect, impairment carrying-value basis and `RATION_SHORT`, while never exposing another nation's exact stock. | Screen | P0 | B-10; WAR-049…053; WAR-109f…m | `SCR-060` | `UI-CMP-022`, `UI-CMP-017`, `UI-CMP-012` | WAR-053 | SPECIFIED | Review |
| `REQ-930` | The War Operations Board shall be nation-owner-only and show only this nation's OP balance, reservations, authorized operations, battles and losses; it shall never merge Alliance data, show another nation's private state or offer an Alliance command path. | Screen | P0 | B-10; roadmap Prompt-13 boundary; WAR-148/161; REQ-589…591; AX-18 | `SCR-061` | `UI-CMP-055`, `UI-CMP-056`, `UI-CMP-057`, `UI-CMP-062` | REQ-589…591 | SPECIFIED | Structure |
| `REQ-931` | The conflicts ledger shall show only public declared facts (date, belligerents, state), use the thin-list pattern, and disclose that richer detail requires a permitted view; it shall not imply hidden detail is public. | Screen | P1 | B-10; WAR-085…088 public fields; `13A-BP-008` | `SCR-062` | `UI-CMP-022`, `UI-CMP-054`, `UI-CMP-027` | WAR-085 | SPECIFIED | Structure |
| `REQ-932` | War detail shall filter each field by its visibility class, show opponent strength only as `LOW`/`MODERATE`/`HIGH`/`SEVERE`, show public city-damage facts and keep exact force, inventory and book value private. | Screen | P0 | B-10; WAR-085…088; WAR-109k; WAR-150 | `SCR-063` | `UI-CMP-058`, `UI-CMP-055`, `UI-CMP-030` | WAR-086 | SPECIFIED | Structure |
| `REQ-933` | The battle report shall present the WAR-088 record to participants and the tier/operation/loss-band public summary elsewhere, with no exact opponent strength in the public summary and no P&W-derived layout claim. | Screen | P0 | B-10; WAR-088; `13A-SRC-034` boundary | `SCR-064` | `UI-CMP-059`, `UI-CMP-060`, `UI-CMP-072` | WAR-088 | SPECIFIED | Review |
| `REQ-934` | War reports and losses shall present the conservation-visible loss and settlement records with the named impairment basis and cumulative campaign figures, within retention limits and without leaking restricted values. | Screen | P0 | B-10; WAR-109f…m; Report 07 §22.4 lineage | `SCR-065` | `UI-CMP-022`, `UI-CMP-059`, `UI-CMP-020` | WAR-109g | SPECIFIED | Review |
| `REQ-935` | Military history shall present permanent class-P war records with filters and retention labels, distinguish public from participant-only records, and never expose a restricted record through counts or ordering. | Screen | P1 | B-10/B-11; D-026 | `SCR-066` | `UI-CMP-020`, `UI-CMP-061`, `UI-CMP-071` | D-026 | SPECIFIED | Review |
| `REQ-936` | The settlement and peace flow shall disclose every term, its duration, the immutable one-live-settlement rule, the 12-turn expiry and the guaranteed surrender off-ramp, and shall not accept silence as consent. | Screen | P0 | B-10; WAR-126…129/131/132; UD-032 Option A | `SCR-067` | `UI-CMP-047`, `UI-CMP-088`, `OVL-01` | UD-032 | SPECIFIED | Review |
| `REQ-937` | Strategic intelligence is BLOCKED: no intelligence surface, placeholder data, simulated report or espionage action shall exist until a future owner-authorized game rule creates one; `SCR-068` remains a registered placeholder only. | Screen | P0 | B-10 espionage exclusion; `13A-OQ-010` | `SCR-068` | None | Future B-10 rule | BLOCKED | Structure |
| `REQ-938` | The Events Centre shall present the current and scheduled events from the closed B-11 event catalogue with their states, eligibility and links to detail, and shall not generate a live event or an unregistered effect in the UI. | Screen | P0 | B-11; WEP-633/713; WPC-14 | `SCR-069` | `UI-CMP-063`, `UI-CMP-022`, `UI-CMP-021` | WEP-633 | SPECIFIED | Structure |
| `REQ-939` | Event detail shall pair each event's cause/hazard with its registered consequence, show eligibility and duration, state the exact effect source, and never display an unregistered effect or a hidden modifier. | Screen | P0 | B-11; WEP-179/619 | `SCR-070` | `UI-CMP-064`, `UI-CMP-021`, `OVL-04` | WEP-179 | SPECIFIED | Review |
| `REQ-940` | Objectives and Challenges shall present the twelve registered categories with lifecycle state, progress, optionality and penalty-free dismissal, and shall not require presence, membership, spending or aggression to view or accept. | Screen | P1 | B-11; WEP-203…215 | `SCR-071` | `UI-CMP-065`, `UI-CMP-016`, `UI-CMP-022` | WEP-203…215 | SPECIFIED | Structure |
| `REQ-941` | Standings shall present named lists with their denominator population, eligibility set and reporting window, computed at P6 and published at P7, with no live tick, no composite headline and no rank without a denominator. | Screen | P0 | B-11; WEP-324/325/359/361/362 | `SCR-072` | `UI-CMP-067`, `UI-CMP-068`, `UI-CMP-022` | WEP-324/325 | SPECIFIED | Structure |
| `REQ-942` | Achievements and rewards shall present the six reward classes and their earned/locked states, with material reward notices stating class, quantity and owner key, and never showing another nation's reward. | Screen | P1 | B-11; WEP-499/663 | `SCR-073` | `UI-CMP-066`, `UI-CMP-029`, `UI-CMP-072` | WEP-663 | SPECIFIED | Review |
| `REQ-943` | National Progress shall present the eight progression layers as separate registers with their own state and history, and shall not collapse them into a single composite score or ladder. | Screen | P1 | B-11; WEP-423 | `SCR-074` | `UI-CMP-012`, `UI-CMP-016`, `UI-CMP-029` | WEP-423 | SPECIFIED | Review |
| `REQ-944` | Reward History shall present granted, deferred, voided and corrected rewards with their claim state, keep deferred claims visible where the B-11 flow requires, and never present a deferred claim as granted. | Screen | P1 | B-11; WEP-633/663/705 | `SCR-075` | `UI-CMP-073`, `UI-CMP-022`, `UI-CMP-020` | WEP-705 | SPECIFIED | Review |
| `REQ-945` | The World Chronicle shall present the public world-history record with dated entries, filters and retention labels, and shall contain no restricted fact, no private nation data and no fabricated world event. | Screen | P1 | B-11; D-026; TR-049 | `SCR-076` | `UI-CMP-071`, `UI-CMP-021`, `UI-CMP-022` | D-026 | SPECIFIED | Review |
| `REQ-946` | World Health aggregates are gated: each figure shall render only after passing k=5 with complementary suppression, or render its suppressed state; no pre-gate world chart, placeholder axis or inferred total shall appear. | Screen | P2 | B-11; D-027; WEP-663; `13A-SRC-015` | `SCR-077` | `UI-CMP-072`, `UI-CMP-030` | k=5 per figure | PROVISIONAL | Structure |
| `REQ-947` | The World Guide and glossary shall use the same section vocabulary as the navigation, provide in-context definitions and governing-rule links, and shall not carry gameplay-critical text only in an image or external platform. | Screen | P1 | B-11; F-010; DP-004; `13A-BP-009`; `13A-DR-010` | `SCR-078` | `UI-CMP-019`, `UI-CMP-026`, `OVL-04` | DP-004 | SPECIFIED | Review |
| `REQ-948` | The privacy settings centre shall list the nine privacy classes in player language, show the current player-visible settings, and never render class-`SEC` content or imply that a privacy setting grants visibility. | Screen | P0 | B-12; PRV-002/009/014 | `SCR-079` | `UI-CMP-022`, `UI-CMP-019`, `UI-CMP-080` | PRV-014 | SPECIFIED | Review |
| `REQ-949` | Security settings shall show sessions, recovery-code custody state, e-mail change with dual confirmation and verification state, and shall never display a credential, token, key or recovery code after its one-time presentation. | Screen | P0 | B-03/B-12; D-029/D-041; ACC-031 | `SCR-080` | `UI-CMP-022`, `UI-CMP-088`, `UI-CMP-017` | D-041 | SPECIFIED | Structure |
| `REQ-950` | Report creation shall render exactly the MOD-002 intake fields (category, subject, time window, reporter account, free-text account, separately stored supplied evidence) and shall degrade to a retryable failure when intake is unavailable. | Screen | P0 | B-12; MOD-002/007; FR-001/006 | `SCR-081` | `UI-CMP-074`, `UI-CMP-076`, `UI-CMP-083`, `UI-CMP-084` | MOD-002 | SPECIFIED | Structure |
| `REQ-951` | Report status and decision shall render MOD-017's seven elements, use the EVD-009 claim tiers exactly, withhold methods/thresholds/third-party data, and never upgrade a claim tier silently. | Screen | P0 | B-12; MOD-017/018; EVD-009 | `SCR-082` | `UI-CMP-017`, `OVL-08`, `UI-CMP-029` | EVD-009 | SPECIFIED | Review |
| `REQ-952` | The appeal view shall present the appeal route, status ladder and decision reasons, and shall remain reachable during every restriction, suspension or communication limitation. | Screen | P0 | B-12; MOD-013/015 | `SCR-083` | `UI-CMP-021`, `UI-CMP-017`, `UI-CMP-085` | MOD-013 | SPECIFIED | Structure |
| `REQ-953` | Restrictions and sanctions shall state the kind of restriction, its scope, its end/review turn and the appeal route, without exposing another player's data, an accusation, a detection threshold or a confidential security fact. | Screen | P0 | B-03/B-12; NET-023/050; PRV-019; MOD-027 | `SCR-084` | `UI-CMP-053`, `UI-CMP-017`, `UI-CMP-018` | NET-050 | SPECIFIED | Review |
| `REQ-954` | My data shall present the data categories, access/export request states and retention disclosure by class, and shall separate an erasure request from the audit-spine retention obligation. | Screen | P1 | B-03/B-12; D-026; DAT-001; PRV-001 | `SCR-085` | `UI-CMP-022`, `UI-CMP-020`, `UI-CMP-019` | D-026 | SPECIFIED | Review |
| `REQ-955` | Review explanation shall present the shared-network state names, what clearance means and the review route, using D-033/D-034 vocabulary and no technical exposure of the matching mechanism. | Screen | P0 | B-03/B-12; D-033/D-034; NET-023 | `SCR-086` | `UI-CMP-017`, `UI-CMP-019`, `UI-CMP-053` | D-034 | SPECIFIED | Review |
| `REQ-956` | The support centre shall separate support contact from conduct reporting, present the support route and degraded state, and never convert a support request into a moderation case or vice versa without the user's explicit route choice. | Screen | P1 | B-12; intake taxonomy; FR-001 | `SCR-087` | `UI-CMP-019`, `UI-CMP-085`, `UI-CMP-011` | FR-001 | SPECIFIED | Review |
| `REQ-957` | Change disclosures shall present dated, player-readable rules-affecting changes and security/incident notices within B-12 disclosure limits, and shall not publish a notice that names a private case, a detection method or another player. | Screen | P1 | B-02/B-12; TR-049; MOD-017/018 | `SCR-088` | `UI-CMP-020`, `UI-CMP-021`, `UI-CMP-019` | TR-049 | SPECIFIED | Review |
| `REQ-958` | Protection state shall display `protected until Turn N` or `protection ended` as a state with its end turn, show that it is visibility-only and not re-granted, and never present it as a countdown or a bonus. | Screen | P0 | B-03; ONB-020/022; D-040; WAR-115…117 | `SCR-089` | `UI-CMP-017`, `UI-CMP-041`, `UI-CMP-089` | ONB-020 | SPECIFIED | Review |
| `REQ-959` | Reroll confirmation shall require re-authentication, the exact current nation name and the exact-phrase destructive confirmation; it shall state permanent reset, no undo, losses, surviving sanctions, immediate replacement and no renewed protection, and shall show block reasons where reroll is barred. | Screen | P0 | B-03; RRL-005/006/012/021; D-039 | `SCR-090` | `UI-CMP-090`, `OVL-02`, `UI-CMP-089` | RRL-006 | SPECIFIED | Review |
| `REQ-960` | The Admin console shall present only the workspaces the holder's ADM role permits, deny unheld routes without disclosing case data, and never render player navigation or player-only components. | Screen | P0 | B-12; ADM-003/021/022; D-042 | `SCR-091` | `UI-CMP-010`, `UI-CMP-019` | D-042 | SPECIFIED | Structure |
| `REQ-961` | The moderation queue shall present assigned cases with triage states and reviewer-scoped actions, and shall not expose `SEC` material, export evidence or alter a balance or snapshot. | Screen | P0 | B-12; ADM-021/022 | `SCR-092` | `UI-CMP-022`, `UI-CMP-023`, `UI-CMP-017` | ADM-021 | SPECIFIED | Structure |
| `REQ-962` | The case and evidence workspace shall present the evidence matrix, the sixteen violation classes and the recorded claim tier, with access scoped to the assigned reviewer and every read audited. | Screen | P0 | B-12; EVD; V-01…V-16 | `SCR-093` | `UI-CMP-029`, `OVL-08`, `UI-CMP-022` | EVD classes | SPECIFIED | Review |
| `REQ-963` | Sanctions administration shall present the six-tier ladder, the two-person requirement and the separation-of-duties state, and shall not allow a single reviewer to exceed the assigned tier authority. | Screen | P0 | B-12/B-08; MOD-036/037/042; MOD-022 | `SCR-094` | `UI-CMP-022`, `UI-CMP-088`, `OVL-02` | MOD-022 | SPECIFIED | Review |
| `REQ-964` | The shared-network review workspace shall present the five shared-network states, a separate review status and the observation window in turns, without exposing the matching mechanism or another account's identity. | Screen | P0 | B-03/B-12; D-033/D-034 | `SCR-095` | `UI-CMP-022`, `UI-CMP-017`, `UI-CMP-021` | D-034 | SPECIFIED | Review |
| `REQ-965` | The audit ledger viewer shall present the audit spine and preservation-order state to authorised roles only, never expose content bodies or secrets, and record every access. | Screen | P0 | B-12; SEC-021/036…040; EVD-026; REQ-851…855 | `SCR-096` | `UI-CMP-022`, `UI-CMP-023`, `UI-CMP-017` | REQ-854 | SPECIFIED | Review |
| `REQ-966` | The turn-engine operations monitor shall present slot history, checkpoints, `INTERRUPTED`/`FAILED` states and the operator recovery path, using the B-02 state vocabulary and no invented success state. | Screen | P0 | B-02; TR-035/036/043/075/080 | `SCR-097` | `UI-CMP-007`, `UI-CMP-022`, `UI-CMP-017` | TR-080 | SPECIFIED | Review |
| `REQ-967` | Data operations shall present retention, compaction and preservation operations with their audit consequence and no destructive action without confirmation, and shall never present an operation as reversible when it is not. | Screen | P0 | B-12; D-026; PRV-023; COR rules | `SCR-098` | `UI-CMP-022`, `UI-CMP-088`, `OVL-02` | D-026 | SPECIFIED | Review |
| `REQ-968` | The announcement composer shall enforce MOD-017/018 content limits and ALL-164 moderation, show the publication scope and preview, and never include private case data or a prohibited disclosure. | Screen | P0 | B-12/B-09; MOD-017/018; ALL-164 | `SCR-099` | `UI-CMP-074`, `UI-CMP-088`, `UI-CMP-083` | MOD-018 | SPECIFIED | Review |
| `REQ-969` | Admin roles and permissions shall present the eight-role catalogue, least-privilege checks, step-up state and emergency-authority posture, and shall prevent a holder from granting a permission it does not possess. | Screen | P0 | B-12; ADM-003; D-042; FR postures | `SCR-100` | `UI-CMP-010`, `UI-CMP-022`, `UI-CMP-089` | D-042 | SPECIFIED | Review |

### 26.2 Cross-cutting shell and component requirements (REQ-970…REQ-1049)

| ID | Requirement | Category | Priority | Governing source | Screens | Components | Dependencies | Status | Verification intent |
|---|---|---|---|---|---|---|---|---|---|
| `REQ-970` | Every authenticated screen shall render inside the persistent shell with identity strip, primary navigation, alert indicator, breadcrumb/context line, primary content, context panel where width allows, and footer; the shell shall never be replaced by a full-page spinner. | Component | P0 | D-201; `13A-PR-02`; `UR-001` | All authenticated | `UI-CMP-001` | D-201 | SPECIFIED | Structure |
| `REQ-971` | Primary navigation shall expose the eight authenticated sections in the approved order, mark the active section, and never expose an administrative destination to a non-holder. | Navigation | P0 | D-201; `13A-PR-07` | All authenticated | `UI-CMP-002` | D-201 | SPECIFIED | Structure |
| `REQ-972` | Secondary navigation shall present same-object tabs only, mark the active tab, and not duplicate top-level destinations as menu items. | Navigation | P1 | D-201; `13A-PR-07` | Section screens | `UI-CMP-003` | D-201 | SPECIFIED | Review |
| `REQ-973` | A breadcrumb/context locator shall appear at depth ≥ 2, render every ancestor as a working link, and state the current screen's canonical name. | Navigation | P2 | `13A-PR-13`; D-209 | Depth ≥ 2 | `UI-CMP-005` | D-209 | SPECIFIED | Structure |
| `REQ-974` | The identity strip shall show the nation name, treasury presentation permitted by visibility class, stability, protection badge and turn countdown, and shall show no value above the viewer's visibility class. | Component | P0 | `13A-BP-001`; `13A-DR-002`; TR-021 | All authenticated | `UI-CMP-006`, `UI-CMP-007` | TR-021 | SPECIFIED | Review |
| `REQ-975` | The turn indicator shall show the current turn, next UTC boundary, phase position and settlement state (`OPEN`, `LOCKED`, `RESOLVING`, `COMPLETED`, `INTERRUPTED`, `FAILED`) in turns and UTC, not wall-clock theatrics. | Data presentation | P0 | TR-027/030/033/035/036/039; `13A-PR-01` | All authenticated | `UI-CMP-007` | TR-035 | SPECIFIED | Structure |
| `REQ-976` | The notification indicator shall show counts and priority from existing notification events only, distinguish non-opt-out items, and never create, mutate or silently drop an event. | Interaction control | P0 | REQ-731; DIP-114/116 | All authenticated | `UI-CMP-008` | REQ-731 | SPECIFIED | Review |
| `REQ-977` | Contextual navigation shall link related objects and screens subject to permission, hide a destination the viewer may not reach, and explain a denied destination without exposing the protected fact. | Navigation | P1 | `13A-PR-13`; `13A-DR-016` | Object/detail/task | `UI-CMP-009` | REQ-553 | SPECIFIED | Review |
| `REQ-978` | Administrative entry and navigation shall render only inside the separate Admin root, only for the holder's ADM role, and never inside the player primary navigation. | Permissions | P0 | D-042; ADM-003/021/022; `13A-DR-013` | `SCR-091`…`SCR-100` | `UI-CMP-010` | D-042 | SPECIFIED | Structure |
| `REQ-979` | Footer/help access shall expose the in-context help index, support entry, report entry, terms and change disclosures on every screen without implying a case or a report has been filed. | Navigation | P2 | `13A-PR-04`; MOD-002; TR-049 | All screens | `UI-CMP-011` | MOD-002 | SPECIFIED | Review |
| `REQ-980` | A statistic card shall label its number type (current, reserved, forecast, historical, estimate, transaction), its unit and its as-of turn, and shall not render a forecast with current-state weight. | Component | P0 | ECN-177/178; D-056 | Dashboards | `UI-CMP-012` | ECN-177 | SPECIFIED | Structure |
| `REQ-981` | A metric group shall present a small set of related metrics with equal structural treatment but explicit individual labels, and shall not merge different number types into one aggregate. | Component | P1 | ECN-177; DMP-073 | `SCR-013/015/029/041/059/072` | `UI-CMP-013` | ECN-177 | SPECIFIED | Review |
| `REQ-982` | A financial summary shall separate opening balance, income, expenditure, net change and closing position, label capex versus opex, and link each line to its explanation. | Component | P0 | ECN-093/097/098; D-051; ECN-142 | `SCR-029/030/031/037/057` | `UI-CMP-014` | D-051 | SPECIFIED | Structure |
| `REQ-983` | A resource balance display shall show total, reserved and available as three figures and shall never show a bare "balance" for a resource or crown amount. | Data presentation | P0 | MKT-053; TR-069; URB-066 | Balance screens | `UI-CMP-015`, `UI-CMP-033` | MKT-053 | SPECIFIED | Structure |
| `REQ-984` | A progress indicator shall name what is progressing, its total and its current value, and shall distinguish pending, success, warning, error and indeterminate states without colour alone. | Component | P2 | `13A-PR-12`; `13A-DS-10` | `SCR-016/025/043/045/074` | `UI-CMP-016` | `13A-DS-10` | SPECIFIED | Review |
| `REQ-985` | A status banner shall pair tone, glyph and text, state the cause and end turn where applicable, and never present a game state as an account penalty or suspension. | Component | P0 | DMP-268; `13A-PR-12`; `13A-DS-10` | Political and state screens | `UI-CMP-017` | DMP-268 | SPECIFIED | Structure |
| `REQ-986` | A warning panel shall state the condition, its consequence, its end or review turn, and the available actions, and shall not show a warning without an action or explanation. | Component | P0 | DMP-163; ECN-182; `13A-PR-10` | Warning surfaces | `UI-CMP-018` | DMP-163 | SPECIFIED | Review |
| `REQ-987` | An information panel shall distinguish settled fact from provisional, forecast and suppressed content through label and tone, and shall carry its governing-rule anchor. | Component | P1 | `13A-PR-05`; `13A-PR-16`; `13A-DR-009` | All read surfaces | `UI-CMP-019` | `13A-DR-009` | SPECIFIED | Review |
| `REQ-988` | A historical record shall carry its as-of turn, its retention class and its public/restricted status, and shall not present a hot-window record as permanent or vice versa. | Data presentation | P1 | D-026; TR-092; PRV-001/023 | History surfaces | `UI-CMP-020` | D-026 | SPECIFIED | Structure |
| `REQ-989` | A timeline shall order events by turn, label each state transition and distinguish pending from completed; it shall not imply a future outcome the rules do not determine. | Component | P2 | TR-004; DIP-108…113; WAR-125 | Timeline surfaces | `UI-CMP-021` | TR-004 | SPECIFIED | Review |
| `REQ-990` | A data table shall provide semantic header/row scope, a caption or accessible name, stable column meaning, exact range pagination and a card fallback that preserves every non-negotiable field. | Component | P0 | `13A-BP-004`; `13A-DS-12`; MKT-065 | Table screens | `UI-CMP-022`, `UI-CMP-024` | `13A-DS-12` | SPECIFIED | Structure |
| `REQ-991` | A filter row shall disclose the active filters, offer a clear action, validate its inputs and never silently exclude rows without showing the filter state. | Component | P1 | `13A-BP-004`; MKT-065 | Table screens | `UI-CMP-023` | MKT-065 | SPECIFIED | Review |
| `REQ-992` | Pagination shall report exact bounds and totals ("0–N of M"), preserve sort and filters across pages, and never claim a total it cannot count. | Component | P1 | MKT-065; `13A-BP-004` | Paginated lists | `UI-CMP-024` | MKT-065 | SPECIFIED | Structure |
| `REQ-993` | A saved view shall store filter/sort state per user, show when it is dirty or invalid, and never widen the viewer's visibility class when applied. | Component | P2 | `13A-BP-004`; TR-021 | List screens | `UI-CMP-025` | TR-021 | SPECIFIED | Review |
| `REQ-994` | Search and jump shall provide only jump-to-object and jump-to-screen modes, show no-result and denied-object states, and shall not promise or implement a full-text corpus. | Navigation | P2 | `13A-OQ-005/009`; `UR-034` | Shell; object screens | `UI-CMP-026`, `UI-CMP-082` | `13A-OQ-005` | PROVISIONAL | Review |
| `REQ-995` | Every object identifier shall render as a link to its canonical route, with a peek preview subject to the object's visibility class and a retired/denied state where applicable. | Navigation | P1 | `13A-PR-13`; `13A-DR-017` | All object citations | `UI-CMP-027`, `OVL-05` | D-209 | SPECIFIED | Structure |
| `REQ-996` | An object peek shall reveal only fields already visible to the viewer, show denied or suppressed as a state, and never become the only place a fact or action exists. | Visibility | P0 | TR-021/022; `13A-PR-05` | Lists everywhere | `UI-CMP-028`, `OVL-05` | TR-021 | SPECIFIED | Review |
| `REQ-997` | A detail section shall be collapsible without losing its content from the page, keep a stable heading and anchor, and provide a page-reachable equivalent for any drawer content. | Component | P2 | `13A-PR-02`; `13A-PR-13` | Object pages | `UI-CMP-029`, `OVL-04` | `13A-PR-13` | SPECIFIED | Review |
| `REQ-998` | A comparison panel shall use only visibility-legal inputs, state each source and turn, show suppression rather than absence, and present differences as facts rather than predicted verdicts. | Component | P1 | `13A-DR-006/020`; `13A-BP-020`; D-027 | `SCR-015/022/023/042/063/072` | `UI-CMP-030` | D-027 | SPECIFIED | Review |
| `REQ-999` | The treasury summary component shall present available funds, reserved funds and the current financial position as separate registers, with no implied credit or overdraft. | Component | P0 | ECN-176/177; D-050 | `SCR-029/030/031/057` | `UI-CMP-031` | D-050 | SPECIFIED | Structure |
| `REQ-1000` | The income and expenditure breakdown shall separate recurring operating expense from one-time capital expenditure and label every forecast line as a forecast. | Data presentation | P0 | D-051; ECN-097/098; ECN-178 | `SCR-029/030/031` | `UI-CMP-032` | D-051 | SPECIFIED | Structure |
| `REQ-1001` | The total/reserved/available register shall render the three figures together in one component, with available derived and labelled, on every device and in every card fallback. | Data presentation | P0 | MKT-053; URB-066 | All balance screens | `UI-CMP-033` | MKT-053 | SPECIFIED | Structure |
| `REQ-1002` | A capacity bar shall distinguish capacity from holdings, show the reserved segment and the full/derated/unmaintained states, and never present capacity as a stored resource. | Component | P0 | ECN-042/120; ECN-147; URB-052 | Capacity screens | `UI-CMP-034` | ECN-042 | SPECIFIED | Structure |
| `REQ-1003` | The search field shall announce its scope, show loading/no-result/denied states, and never issue a query whose result would disclose a higher visibility class. | Navigation | P2 | TR-021; `UR-034` | Search surfaces | `UI-CMP-082` | TR-021 | SPECIFIED | Review |
| `REQ-1004` | A production chain shall show batches, inputs at current stock, expected output, variable cost, maintenance, power draw, blocking reason and the applied research bonus as a separate line. | Component | P0 | URB-149; ECN-147a | `SCR-032/044` | `UI-CMP-035` | URB-149 | SPECIFIED | Structure |
| `REQ-1005` | A construction queue item shall show the action state, target, cost, slot, expected availability turn and cancellation/refund terms, and shall not imply a multi-item queue where the rules allow one slot. | Component | P0 | URB-064/148; D-073/D-074 | `SCR-042/043` | `UI-CMP-036` | D-073 | SPECIFIED | Structure |
| `REQ-1006` | A research project card shall show status (`locked`, `available`, `in progress`, `complete`), cost in RP and crowns, prerequisite, effect, progress and the one-active-project limit. | Component | P0 | URB-102/150; D-076 | `SCR-045` | `UI-CMP-037` | D-076 | SPECIFIED | Structure |
| `REQ-1007` | Every time-sensitive display shall express time in turns and the UTC boundary, with a wall-clock element only as a cosmetic aid that is never the source of truth. | Data presentation | P0 | TR-024/030/031; `13A-PR-01`; `UR-038` | All screens | `UI-CMP-007`, `UI-CMP-041` | TR-024 | SPECIFIED | Review |
| `REQ-1008` | Historical displays shall label the retention boundary (hot, monthly summary, permanent, class-O minimum) and shall not silently omit a record that has moved class. | Data presentation | P1 | D-026; TR-092; `13A-DR-020` | History screens | `UI-CMP-020` | D-026 | SPECIFIED | Structure |
| `REQ-1009` | The approval and stability presentation shall show the six supports and their weights, the derived approval and stability, and the cause chain per term, without inventing named stability bands. | Component | P0 | DMP-073; F-PD-004…009; DMP-053/054/056 | `SCR-021/023/028` | `UI-CMP-038` | DMP-073 | SPECIFIED | Structure |
| `REQ-1010` | The political state banner shall show one of the six DMP-268 states, its cause, its end turn, what is locked and what is not, and shall appear on every political and consequence-bearing screen. | Component | P0 | DMP-256/268; DMP-128 | `SCR-021`…`SCR-028`; block surfaces | `UI-CMP-039` | DMP-268 | SPECIFIED | Structure |
| `REQ-1011` | A policy control shall show the current setting, the proposed setting, its effect, its cost and its cooldown with the next eligible turn directly on the control. | Interaction control | P0 | D-087; DMP-101/102; `13A-BP-010` | `SCR-024` | `UI-CMP-040`, `OVL-01` | D-087 | SPECIFIED | Review |
| `REQ-1012` | Election date presentation shall anchor on `campaign_open_turn`, label on-time values as on-time, and show a delayed or interrupted resolution as a state rather than a missed deadline. | Data presentation | P0 | D-106/D-107; DMP-178/184 | `SCR-025/027/028` | `UI-CMP-041` | D-106/D-107 | SPECIFIED | Review |
| `REQ-1013` | Every screen shall have one stable identity: canonical name, page heading, route key and governing-section anchor; aliases render the same screen and never a second copy. | Navigation | P1 | `13A-PR-13`; `UR-044`; D-209 | All screens | `UI-CMP-002`, `UI-CMP-004` | D-209 | SPECIFIED | Structure |
| `REQ-1014` | Every component shall declare its applicable states from the shared eleven-state vocabulary and shall not invent a parallel state name. | Component | P0 | `13A-DS` state matrix; `13A-PR-11` | All components | All `UI-CMP` | `13A-DS-07`…`13A-DS-15` | SPECIFIED | Structure |
| `REQ-1015` | Every component shall define desktop, tablet and mobile behaviour and shall preserve its non-negotiable fields in the narrowest layout. | Responsive | P0 | `13A-RD-02`…`13A-RD-08` | All components | All `UI-CMP` | D-211 | SPECIFIED | Structure |
| `REQ-1016` | Every component shall meet the applicable keyboard, focus, label, semantic and text-alternative duties in §10. | Accessibility | P0 | `13A-DS-07`…`13A-DS-15`; `UR-010` | All components | All `UI-CMP` | `13A-DS-07` | SPECIFIED | Review |
| `REQ-1017` | Every component shall reference semantic tokens only; no raw colour, typeface, size or spacing value may appear in a component or screen specification. | Design system | P0 | D-203; `13A-DS-01`…`13A-DS-06`; `UR-043` | All components | All `UI-CMP` | D-203 | SPECIFIED | Structure |
| `REQ-1018` | A campaign action control shall present exactly the three permitted action types, their cost/effect, the once-only or twice-only limit and the charge-once confirmation state. | Interaction control | P0 | D-094; DMP-189/193 | `SCR-026` | `UI-CMP-042` | D-094 | SPECIFIED | Review |
| `REQ-1019` | A diplomatic relationship indicator shall show posture as a labelled state with glyph and text, not hue alone, and shall not conflate posture with war or with a score. | Component | P0 | DIP-023/024; `13A-PR-12` | Diplomacy surfaces | `UI-CMP-043` | DIP-023/024 | SPECIFIED | Review |
| `REQ-1020` | Directional relationship presentation shall show both directions side by side, identify which nation holds which posture, and keep an embargo visually and textually distinct from a treaty. | Data presentation | P0 | DIP-023/024; DIP-037; DP-A01 | `SCR-047/048` | `UI-CMP-044` | DIP-023/024 | SPECIFIED | Structure |
| `REQ-1021` | Treaty status shall name the exact type and lifecycle state, show activation and expiry turns, and never render a stale `active` badge after termination or expiry. | Component | P0 | DP-T01…T03; DP-A01; DIP-108…113 | `SCR-047/050/051/052/058` | `UI-CMP-045` | DIP-108…113 | SPECIFIED | Structure |
| `REQ-1022` | A proposal summary shall show the counterparty, type, proposed terms, created and expiry turns and current state, visible only to the named parties while pending. | Component | P0 | D-030; DIP-114 | `SCR-014/047/049/050` | `UI-CMP-046` | D-030 | SPECIFIED | Review |
| `REQ-1023` | A negotiation panel shall present the ten 08C §12.3 confirmation fields in order, keep the cancel path non-destructive, never preselect confirm, and show the exact limit consumed. | Interaction control | P0 | 08C §12.3; D-030 | `SCR-049/067` | `UI-CMP-047`, `OVL-01` | 08C §12.3 | SPECIFIED | Review |
| `REQ-1024` | Publication status shall show pending-private, accepted-private, active-public and record-only states, and shall never reveal pending terms to a third party. | Visibility | P0 | DIP-108…113; D-030; D-140; AT-E00/E01 | `SCR-050/051/058` | `UI-CMP-048` | D-030 | SPECIFIED | Review |
| `REQ-1025` | An alliance membership row shall show member identity and role only within disclosure rules, mark non-covered membership explicitly, and never expose an applicant to a non-administrator. | Component | P0 | ALL-086; ALL-199/204; D-140 | `SCR-053/054/055` | `UI-CMP-049` | ALL-086 | SPECIFIED | Review |
| `REQ-1026` | An applicant status row shall show pending/admitted/declined/expired/withdrawn, be visible only to the alliance administration, and terminate in-product without an external platform hop. | Component | P0 | ALL-080…086; D-133 | `SCR-054` | `UI-CMP-050` | ALL-086 | SPECIFIED | Review |
| `REQ-1027` | The alliance financial summary shall show the four ARL categories with the `AVAILABLE = RECEIVED − RESERVED − EXPENDED` identity, the visible 0% fallback and no spendable purpose while none is approved. | Data presentation | P0 | ALL-187; D-141; ALL-220…226 | `SCR-056/057` | `UI-CMP-051` | D-141 | SPECIFIED | Structure |
| `REQ-1028` | An alliance receipt shall be immutable, name donor or source, receiving alliance, asset, amount, turn, transfer reference and idempotency reference, and shall never be hidden or editable. | Component | P0 | ALL-193; ECN-213/213a | `SCR-056/057` | `UI-CMP-052` | ALL-193 | SPECIFIED | Structure |
| `REQ-1029` | A restriction explanation shall name the restriction kind (role, pair, NAP, same-Alliance, political state, protection, security) and a permitted reason class, without accusation, private terms, another player's data or a technical threshold. | Permissions | P0 | NET-023/050; PRV-019; WAR-149; DMP-268; `13A-PR-10` | `SCR-048/055/058/084/086` | `UI-CMP-053`, `OVL-03` | NET-023 | SPECIFIED | Review |
| `REQ-1030` | A war summary shall show declared belligerents, campaign state, public duration and the permitted public facts, and shall not disclose a private operation or another nation's exact strength. | Component | P0 | WAR-085…088; WAR-148/150 | `SCR-059/061/062/063` | `UI-CMP-054` | WAR-148 | SPECIFIED | Structure |
| `REQ-1031` | A war status strip shall show the campaign lifecycle state, protection recheck state and settlement availability, using the WAR-125 vocabulary and no invented state. | Component | P1 | WAR-125; WAR-115…117; WAR-126 | `SCR-061/063` | `UI-CMP-055` | WAR-125 | SPECIFIED | Review |
| `REQ-1032` | An operations summary shall show this nation's authorized operations, their reservation and execution states, and released/failed outcomes with the exact failure factor. | Component | P0 | WAR-039; B10-C20; WAR-152; ECN-142 | `SCR-061` | `UI-CMP-056` | WAR-039 | SPECIFIED | Review |
| `REQ-1033` | The OP balance and reservation presentation shall show the persistent national pool, its cap, regeneration, carry and reservations, and shall never show a second pool, an Alliance pool or another nation's OP. | Data presentation | P0 | D-015 as 10B-C3; WAR-039; ALL-139; WAR-161 | `SCR-059/061` | `UI-CMP-057` | D-015 | SPECIFIED | Structure |
| `REQ-1034` | Threat and odds shall be shown only as `LOW`, `MODERATE`, `HIGH` or `SEVERE`, with the band's meaning stated once, and never as an exact ratio, probability or opponent statistic. | Data presentation | P0 | WAR-085…088 | `SCR-061/063` | `UI-CMP-058` | WAR-086 | SPECIFIED | Structure |
| `REQ-1035` | A battle record shall present the WAR-088 fields to a participant and the public summary (tier, operation type, loss band) otherwise, with no exact opponent strength in the public view. | Component | P0 | WAR-088; WAR-150 | `SCR-061/064/065` | `UI-CMP-059` | WAR-088 | SPECIFIED | Review |
| `REQ-1036` | A battle outcome shall distinguish win, loss, stalemate, interrupted and voided, show the reason and settlement consequence, and never imply a result the settlement has not produced. | Component | P0 | WAR-088; WAR-126; TR-043 | `SCR-064/065` | `UI-CMP-060` | WAR-088 | SPECIFIED | Review |
| `REQ-1037` | No player screen shall display administrative chrome, an administrative-only component, a moderator note, an evidence field or a role-restricted control. | Permissions | P0 | D-042; `13A-DR-013`; ADM-021/022 | All player screens | `UI-CMP-010` | D-042 | SPECIFIED | Structure |
| `REQ-1038` | Military history shall present permanent class-P war records with retention labels, filters and object links, and shall not expose a participant-only record through a public list. | Component | P1 | D-026; WAR-148 | `SCR-066` | `UI-CMP-061` | D-026 | SPECIFIED | Review |
| `REQ-1039` | Nation-owner operation controls shall render only on the owner's own War Operations Board, never inside an Alliance surface, and each control shall carry its OP cost, reservation, confirmation and block reason. | Permissions | P0 | WAR-148/161; REQ-589…591; AX-18; WAR-152 | `SCR-061` | `UI-CMP-062` | REQ-589…591 | SPECIFIED | Structure |
| `REQ-1040` | An event card shall show the event's registered class, state, eligibility, duration and consequence link, and shall not invent an event or an effect. | Component | P1 | WEP-040/081/179/633 | `SCR-013/069/070` | `UI-CMP-063` | WEP-179 | SPECIFIED | Structure |
| `REQ-1041` | Event consequence presentation shall pair cause/hazard with the registered effect, state the exact affected quantity or state, and show mitigation where the rule provides one. | Data presentation | P0 | WEP-179/619 | `SCR-070` | `UI-CMP-064` | WEP-179 | SPECIFIED | Review |
| `REQ-1042` | An objective card shall show category, horizon, progress, tiered partial credit, optionality and penalty-free dismissal, and shall not require presence, membership, spending or aggression to remain visible. | Component | P1 | WEP-203…215; `AP-004` | `SCR-009/071` | `UI-CMP-065` | WEP-203…215 | SPECIFIED | Review |
| `REQ-1043` | Achievement and historical reward cards shall show the reward class, earned state, grant turn and any deferred claim, and shall never present a deferred claim as granted. | Component | P1 | WEP-499/663/705 | `SCR-073/075` | `UI-CMP-066`, `UI-CMP-073` | WEP-705 | SPECIFIED | Review |
| `REQ-1044` | A ranking row shall show the nation, the named standing value, its position or percentile and its ineligible/suppressed state, without an unstated denominator. | Component | P0 | WEP-324/359; WEP-325 | `SCR-072/010` | `UI-CMP-067` | WEP-324 | SPECIFIED | Structure |
| `REQ-1045` | A ranking summary shall state the denominator population, eligibility set, reporting window and computation/publish turns, and shall never imply live updating. | Data presentation | P0 | WEP-324/325/359 | `SCR-072` | `UI-CMP-068` | WEP-325 | SPECIFIED | Structure |
| `REQ-1046` | A notification item shall show the source event, its tier, its object link and its mutable/non-mutable state, and shall not paraphrase the event into a different fact. | Component | P0 | REQ-731; DIP-114/116 | `SCR-013/019/014` | `UI-CMP-069` | REQ-731 | SPECIFIED | Review |
| `REQ-1047` | A pending-action item shall show the owning system, the action state, the due boundary and the permitted act/defer/cancel paths, and shall never imply a cancellation the rules do not allow. | Component | P0 | TR-004; D-016/D-030; MKT/ALL/AT lifecycles | `SCR-014` | `UI-CMP-070` | TR-004 | SPECIFIED | Review |
| `REQ-1048` | A chronicle record shall carry its turn, participants, public/restricted class and retention label, and shall not contain a private fact, a moderator note or an inferred motive. | Component | P1 | D-026; TR-049; PRV-019 | `SCR-017/070/075/076` | `UI-CMP-071` | D-026 | SPECIFIED | Review |
| `REQ-1049` | Form, action and overlay components shall provide programmatic labels, inline text validation, disabled reasons, confirmation with exact effect, and a page-reachable equivalent for every overlay state. | Component | P0 | `13A-PR-09`/`13A-PR-10`; RRL-006; 08C §12.3; WAR §12.3; `13A-DS-11` | All form screens | `UI-CMP-074`…`UI-CMP-090`, `OVL-01`…`OVL-08` | `13A-PR-09` | SPECIFIED | Structure |

### 26.3 Responsive, accessibility, permission and traceability requirements (REQ-1050…REQ-1089)

| ID | Requirement | Category | Priority | Governing source | Screens | Components | Dependencies | Status | Verification intent |
|---|---|---|---|---|---|---|---|---|---|
| `REQ-1050` | Every screen shall order its content by the six-tier hierarchy in §9.1 and shall identify one primary register; warnings shall not displace the primary register and no two unrelated figures shall share primary weight. | Information hierarchy | P0 | `13A-PR-02`; D-210 | All screens | `UI-CMP-012`, `UI-CMP-013` | D-210 | SPECIFIED | Review |
| `REQ-1051` | One game and one authoritative rule set shall be presented on desktop, tablet and mobile; no device class may receive different data, different visibility, different turn cadence or reduced mechanics. | Responsive | P0 | `13A-RD-01`; D-202 | All screens | All `UI-CMP` | D-202 | SPECIFIED | Structure |
| `REQ-1052` | The must-not-simplify list (countdown, pending counts, political banner, protection, suppression, confirmation, disabled reasons, accessible labels, appeal route) shall survive every layout on every device. | Responsive | P0 | `13A-RD-07`; D-202 | All screens | `UI-CMP-007`, `UI-CMP-017`, `UI-CMP-072`, `UI-CMP-089` | `13A-RD-07` | SPECIFIED | Review |
| `REQ-1053` | A table that converts to cards shall preserve the identity column and every field marked non-negotiable, including total/reserved/available triples and units. | Responsive | P0 | `13A-RD-04`/`13A-RD-08`; MKT-053 | Table screens | `UI-CMP-022`, `UI-CMP-033` | MKT-053 | SPECIFIED | Structure |
| `REQ-1054` | Navigation shall adapt by device: persistent section bar on desktop, icon rail or labelled overflow on tablet, compact section menu plus bottom access to Home/Inbox/World/Account on mobile, always with one-step section access. | Layout | P1 | `13A-RD-02`…`13A-RD-04`; D-211 | All screens | `UI-CMP-002`, `UI-CMP-003` | D-211 | SPECIFIED | Review |
| `REQ-1055` | On mobile, committing controls shall be placed in a distinct action region, destructive controls shall be separated from primary controls, and confirmation shall not be reachable by an adjacent mis-tap. | Responsive | P0 | `13A-DS-14`; `13A-RD-07` | Task screens | `UI-CMP-085`, `UI-CMP-087`, `UI-CMP-088` | `13A-DS-14` | SPECIFIED | Review |
| `REQ-1056` | Suppression and insufficient-sample states shall render on every device as their named state, with the same explanation, and shall never collapse to blank space, zero or omitted card. | Data presentation | P0 | D-027; TR-022; WEP-663; MKT-110; `13A-RD-07` | Aggregate surfaces | `UI-CMP-072`, `OVL-07` | D-027 | SPECIFIED | Structure |
| `REQ-1057` | The device breakpoints in §8.1 are provisional Category-C values; no production breakpoint may be treated as approved until the Stage 5 device matrix confirms or replaces it. | Responsive | P1 | `13A-RD-06`; D-202; `UR-042` | All screens | None | Stage 5 device matrix | PROVISIONAL | Review |
| `REQ-1058` | Every chart shall carry title, units, time window, source/slot, legend, accessible alternative and truncated-axis disclosure; it shall not mislead through aspect ratio, omitted baseline or implied precision. | Data presentation | P1 | `13A-DS-12`; §9.9 | Chart surfaces | `UI-CMP-030`, `UI-CMP-019` | `13A-DS-12` | SPECIFIED | Review |
| `REQ-1059` | Every chart shall have a text or table alternative exposing the same values, and the alternative shall be reachable without interacting with the chart. | Accessibility | P0 | `13A-DS-12`; `UR-011` | Chart surfaces | `UI-CMP-030` | `13A-DS-12` | SPECIFIED | Structure |
| `REQ-1060` | Dual-axis charts are prohibited in every screen and component. | Data presentation | P0 | `13A-DS-12`; §9.9 | Chart surfaces | `UI-CMP-030` | `13A-DS-12` | SPECIFIED | Structure |
| `REQ-1061` | Any average, band or aggregate shall show its sample count or contributing-group size; a sample below the disclosure threshold shall render `suppressed` or `INSUFFICIENT_SAMPLE`. | Data presentation | P0 | MKT-110; D-027; DIP-113 | Aggregate surfaces | `UI-CMP-072` | MKT-110 | SPECIFIED | Structure |
| `REQ-1062` | Every displayed figure shall carry its as-of turn/slot and its current/historical/forecast/provisional class; no figure may appear without a time reference. | Data presentation | P0 | `13A-PR-03`; ECN-177; `13A-SRC-017` lesson | All data screens | `UI-CMP-012` | ECN-177 | SPECIFIED | Structure |
| `REQ-1063` | The six number types shall be rendered as separate registers with distinct labels and visual weight; a forecast shall never share current-state weight and no screen may redefine a number. | Data presentation | P0 | ECN-177/178/183; D-056; `UR-005` | All data screens | `UI-CMP-012`, `UI-CMP-013` | ECN-177 | SPECIFIED | Structure |
| `REQ-1064` | Forecast presentation shall state assumptions and uncertainty, render an uncomputable forecast as `unknown`, and never present a projection as a completed balance. | Information hierarchy | P0 | ECN-178; URB-152; `13A-PR-16` | Forecast surfaces | `UI-CMP-012`, `UI-CMP-018` | ECN-178 | SPECIFIED | Review |
| `REQ-1065` | Every resource or crown balance shall be presented as total, reserved and available together; a total-only presentation is a defect and shall fail review. | Data presentation | P0 | MKT-053; TR-069; URB-066; `UR-006` | All balance screens | `UI-CMP-033` | MKT-053 | SPECIFIED | Structure |
| `REQ-1066` | Suppressed is not zero, not absent and not an empty result; insufficient sample is not an empty result; no count, layout, thumbnail or difference may reveal a suppressed value. | Data presentation | P0 | D-027; TR-022; WEP-663; MKT-110; `UR-012` | Aggregate surfaces | `UI-CMP-072`, `OVL-07` | D-027 | SPECIFIED | Review |
| `REQ-1067` | Directional diplomacy shall be presented per direction with the holder named, and a posture shall never be presented as symmetric or as a score. | Data presentation | P0 | DIP-023/024; DIP-086/088 | Diplomacy surfaces | `UI-CMP-044` | DIP-023 | SPECIFIED | Structure |
| `REQ-1068` | Treaty publication shall show the exact lifecycle state and the public activation point, with pending terms private until activation. | Data presentation | P0 | DIP-108…113; D-030 | Diplomacy surfaces | `UI-CMP-048`, `UI-CMP-045` | DIP-108…113 | SPECIFIED | Review |
| `REQ-1069` | Every standing shall display its denominator population, eligibility set and reporting window; a display without a denominator is a defect. | Data presentation | P0 | WEP-324/359; `UR-020` | Standings/profile | `UI-CMP-068` | WEP-324 | SPECIFIED | Structure |
| `REQ-1070` | No ranking may imply live updating, ticking or a composite headline score; standings publish at P7 and carry their computation turn. | Data presentation | P0 | WEP-325/361/362 | Standings | `UI-CMP-068`, `UI-CMP-067` | WEP-325 | SPECIFIED | Structure |
| `REQ-1071` | Every event presentation shall pair cause/hazard with its registered consequence; no screen may display an effect without its source or a hazard without its effect. | Information hierarchy | P1 | WEP-179/619 | Event surfaces | `UI-CMP-064` | WEP-179 | SPECIFIED | Review |
| `REQ-1072` | Deferred claims and deferred rewards shall remain visible in Reward History and in the owning surface, labelled as deferred, and shall not be hidden or presented as settled. | Visibility | P1 | WEP-705/713 | `SCR-075` | `UI-CMP-073` | WEP-705 | SPECIFIED | Review |
| `REQ-1073` | The Alliance interface and the War Operations Board shall remain separate surfaces; no Alliance screen may render member OP spending, military command, delegated operations or private war data. | Permissions | P0 | AX-18; WAR-148/161; REQ-589…591; UD-047/UD-049 | `SCR-053`…`SCR-058`, `SCR-061` | `UI-CMP-062`, `UI-CMP-049` | REQ-589…591 | SPECIFIED | Structure |
| `REQ-1074` | Own-nation military exact figures shall appear only to the nation owner; every other viewer receives only the permitted band or public summary. | Visibility | P0 | WAR-085…088; WAR-148/150; WAR-109k | War surfaces | `UI-CMP-058`, `UI-CMP-059` | WAR-148 | SPECIFIED | Review |
| `REQ-1075` | Battle and war records shall be filtered field by field against the viewer's visibility class; a field not permitted shall be absent or explicitly restricted, never blank in a way that implies zero. | Visibility | P0 | WAR-088/109k/150; TR-021 | War surfaces | `UI-CMP-059`, `UI-CMP-030` | TR-021 | SPECIFIED | Review |
| `REQ-1076` | Player-facing privacy surfaces shall use the nine class names and shall never expose class-`SEC`, another player's private class or an enforcement record. | Visibility | P0 | PRV-002/009/014/019 | Privacy/support/admin | `UI-CMP-019` | PRV-014 | SPECIFIED | Review |
| `REQ-1077` | Credentials, session tokens, keys, detection internals and privileged configuration shall never appear on a player-facing or moderation surface. | Visibility | P0 | PRV-014; D-042 | All player screens | None | PRV-014 | SPECIFIED | Structure |
| `REQ-1078` | The appeal route shall remain available during every restriction, suspension and communication limitation, and no screen shall present an unavailable appeal route. | Permissions | P0 | MOD-013/015; REQ-833/848 | `SCR-083`, `SCR-084` | `UI-CMP-085` | MOD-013 | SPECIFIED | Structure |
| `REQ-1079` | Report intake shall render the exact MOD-002 fields and preserve the separate evidence store; it shall not add a mandatory field the rule does not define. | Permissions | P0 | MOD-002; `UR-025` | `SCR-081` | `UI-CMP-083` | MOD-002 | SPECIFIED | Structure |
| `REQ-1080` | Administrative audit visibility shall be role-scoped, purpose-bound and itself audited; an audit view shall not expose content bodies, secrets or another role's case. | Permissions | P0 | EVD-026/028; REQ-851…855; D-042 | Admin screens | `UI-CMP-010`, `UI-CMP-022` | REQ-854 | SPECIFIED | Review |
| `REQ-1081` | Every action path shall be fully keyboard-operable in reading order, with focus trapped and restored in overlays and no keyboard trap outside a modal. | Accessibility | P0 | `13A-DS-07`; `UR-010` | All screens | All interactive | `13A-DS-07` | SPECIFIED | Review |
| `REQ-1082` | Every interactive element shall have a visible, tokenized focus indicator that is not suppressed by hover or active styling. | Accessibility | P0 | `13A-DS-08` | All screens | All interactive | `13A-DS-08` | SPECIFIED | Review |
| `REQ-1083` | Tables shall expose semantic headers and row/column scope, and card fallbacks shall preserve an equivalent accessible structure. | Accessibility | P0 | `13A-DS-12`; `UR-011` | Table screens | `UI-CMP-022` | `13A-DS-12` | SPECIFIED | Structure |
| `REQ-1084` | Numbers shall be announced with their units, basis-point suffix, turn context and band label; a bare number shall not be the accessible name of a data point. | Accessibility | P1 | `13A-DS-11`; ECN-184 | Data screens | `UI-CMP-012`, `UI-CMP-058` | `13A-DS-11` | SPECIFIED | Review |
| `REQ-1085` | Motion shall be non-essential, respect reduced-motion preferences, and never be the only indication of a state change. | Accessibility | P1 | `13A-DS-13` | All screens | All animated | `13A-DS-13` | SPECIFIED | Review |
| `REQ-1086` | Every form control shall have a programmatic label and text-linked error identification; a placeholder shall not be the only label. | Accessibility | P0 | `13A-DS-11`; `UR-047` | Form screens | `UI-CMP-074`…`UI-CMP-084` | `13A-DS-11` | SPECIFIED | Structure |
| `REQ-1087` | All screen strings shall be localization-ready and no gameplay-critical text shall be embedded in an image or an external platform. | Accessibility | P2 | `13A-DS-15`; `UR-047`; `13A-BP-023` | All screens | All text-bearing | `13A-DS-15` | SPECIFIED | Review |
| `REQ-1088` | Presentation shall never grant permission: every action's availability is server-authoritative, and a rendered control without server permission shall fail closed with a named restriction. | Permissions | P0 | `13A-PR-11`; `13A-DR-016`; REQ-553/645 | All action surfaces | `UI-CMP-089` | REQ-553 | SPECIFIED | Review |
| `REQ-1089` | B-13 shall record traceability between requirements, screens, components, governing rules and decisions, shall label every provisional/blocked item, and shall not claim implementation, runtime validation, WCAG conformance or completion of Prompt 13C or Prompt 13D. | Traceability | P0 | D-014; D-217; `UR-044` | All | All | D-207/D-217 | SPECIFIED | Structure |

**Requirement tally:** 220 rows — 100 screen-level (`REQ-870`…`REQ-969`) and 120 cross-cutting (`REQ-970`…`REQ-1089`). Status: **213 SPECIFIED**, **4 PROVISIONAL** (`REQ-889`, `REQ-946`, `REQ-994`, `REQ-1057`) and **3 BLOCKED** (`REQ-907`, `REQ-908`, `REQ-937`).

**No-duplication statement.** These rows are presentation duties, not restatements of game mechanics. Where a duty derives from an existing rule the rule is cited as the governing source; the requirement adds only the screen/component presentation obligation (for example, `MKT-053` owns the three-balance rule, `REQ-1001` owns the component duty to render it everywhere). No existing `REQ-001`…`REQ-869` row is duplicated, renumbered or reclassified.

## 27. Decisions and provisional matters

### 27.1 New Category B decisions (D-206…D-218)

| ID | Topic | Status |
|---|---|---|
| D-206 | B-13 three-file deliverable architecture | Confirmed (Category B) |
| D-207 | `UI-CMP-001`…`UI-CMP-090` family and overlay reuse | Confirmed (Category B) |
| D-208 | A–K screen template and completeness rule | Confirmed (Category B) |
| D-209 | Canonical parent, route key and alias model | Confirmed (Category B) |
| D-210 | Six-tier information hierarchy | Confirmed (Category B) |
| D-211 | Six responsive presentation patterns; breakpoints provisional | Confirmed (policy) / Provisional (values) |
| D-212 | Number and balance component law | Confirmed (Category B) |
| D-213 | One table grammar, card fallback, saved views | Confirmed (Category B) |
| D-214 | Confirmation-first, disabled-reason, cooldown-on-control | Confirmed (Category B) |
| D-215 | Overlay page-equivalence and 13B/13C boundary | Confirmed (Category B) |
| D-216 | Conditional and prohibited surface absence | Confirmed (Category B) |
| D-217 | B-13 requirement allocation and status policy | Confirmed (Category B) |
| D-218 | Administrative workspace and role-scoping template | Confirmed (Category B) |

### 27.2 New Category C provisional decision and preserved owner-reserved matters (D-219)

The pass records one provisional bundle rather than forcing sixteen owner choices: final palette/logo/typefaces (`13A-OQ-001/002`), dark mode (`13A-OQ-013`), icon-set membership, user-selectable mobile mode (`13A-OQ-014`), production breakpoints (`13A-RD-06`), notification tier defaults (`13A-OQ-006`), context-panel defaults (`13A-OQ-008`), search scope (`13A-OQ-005/009`), favorites (`13A-OQ-012`), public test server (`13A-OQ-003`), performance budgets (`13A-OQ-016`), and all preserved `UD-` rows (`UD-017`, `UD-040`…`UD-060` as carried by B-12). Safe working defaults are specified; every item keeps its named confirming test or owner. No screen may present a provisional default as an approved value.

### 27.3 Preserved historical statuses

R7 implementation retained / independent acceptance NOT ACCEPTED; R8 DEFERRED BY OWNER (not reopened); 12B-C1 NOT CLOSED; the three 12B PARTIAL acceptance gates and seven 12A PARTIAL gates; Prompt 12C OWNER ACCEPTED (16 PASS / 2 PARTIAL / 2 BLOCKED, 378 unexecuted `FPA-` specifications); production security obligations outstanding; `UD-017` and `UD-040`…`UD-060` untouched; `P13A-10` remains PARTIAL as a historical 13A finding now resolved at the B-13 specification level. None of these is altered by B-13.

---

## 28. Dependencies and unresolved questions

### 28.1 External dependencies

| Dependency | Owner | Effect on B-13 |
|---|---|---|
| G-1…G-6 Global Trade release gates | Evidence + owner launch decision | `SCR-038/039` remain BLOCKED and absent; `REQ-907/908` BLOCKED |
| B-10 intelligence rule (no owner named) | Future owner-authorized rule | `SCR-068` placeholder only; `REQ-937` BLOCKED |
| Fair-play review of pins (`13A-OQ-012`) | B-12 linkage | `SCR-020` PROVISIONAL; absent |
| Per-figure k=5 evidence | Disclosure policy D-027 | `SCR-077` PROVISIONAL; no chart pre-gate |
| Stage 5 device matrix | Technical + design | Confirms/replaces provisional breakpoints (`REQ-1057`) |
| Stage 5 routing model (OQ-015) | Technical architecture | Route keys are documentation identifiers, not final URLs |
| Stage 5+ built UI | Implementation phase | All accessibility/responsive verification; no claim now |
| Owner brand decisions | Owner | Palette/type/logo/dark mode; semantic tokens only today |
| UD-040 (multi-membership/attribution) | Owner | Tax screen shows the visible 0% fallback; no resolution |
| UD-045/UD-046/UD-047/UD-049 | Owner | Alliance permissions/ARL/delegation/announcements remain bounded; no invented capability |
| UD-052…UD-060, UD-017 | Owner/legal | Report/appeal/transparency/legal branches remain labelled |

### 28.2 Genuine specification gaps carried forward

1. **Graph layout and its accessible equivalent** — B-13 fixes the symbolic/list-first duties; the algorithm is a Stage 5 technical choice, not an owner question.
2. **Mobile user-selectable mode** — deferred (`13A-OQ-014`), with the same-rules guarantee unaffected.
3. **Notification tier defaults** — 13B defines three presentation tiers over existing events; the default assignment awaits evidence (`13A-OQ-006`).
4. **Context-panel default content per section** — first-pass defaults are specified per pattern; refinement is a later design review (`13A-OQ-008`).
5. **Search scope** — jump-only is specified; a full-text corpus remains unbuilt and unpromised (`13A-OQ-005/009`, `REQ-994` PROVISIONAL).
6. **Iconography** — the icon *roles* are specified (status glyphs, object types); set membership is owner-reserved.
7. **Battle-report layout** — derived from WAR-088 because P&W report internals are `NOT-RETRIEVABLE`; no benchmark imitation is claimed.

---

## 29. Documentation impact register (historical — original Prompt 13B completion)

> **Historical status (labeled by Prompt 13B-C1-R1, 2026-11-13).** This register records the documentation impact assessment as it stood at the original Prompt 13B completion on 2026-11-13. Its findings are preserved unchanged as historical evidence, including the then-absent Prompt 13B archive and INDEX row. The subsequent Prompt 13B-C1 corrections are recorded in [§31](#31-prompt-13b-c1-correction-impact-register-2026-11-13); §31 supersedes only the archive and INDEX status noted here, not the rest of this assessment.

The register records every relevant document inspected, whether it was modified, why, and the actual validation result. `Inspected = Yes` means the file was read in this session; a file not read is not listed as inspected. Validation results are the commands reported in the final execution report; no runtime UI test was performed.

| Document path | Authority | Inspected | Modification required | Modification performed | Reason | Cross-references | Validation | Notes |
|---|---|---|---|---|---|---|---|---|
| `docs/AUTONOMOUS_DECISION_POLICY.md` | Canonical | Yes | No | No | D-014 read and applied; policy unchanged | D-014 | Read only | No edit needed |
| `docs/AI_CONTEXT.md` | Canonical status | Yes | Yes | Yes | Prompt 13B status, requirement frontier, canonical path, coverage | §27.1, §29; D-206…219 | 13B validator + validate_final | Historical snapshots preserved |
| `docs/AI_HANDOFF.md` | Canonical status | Yes | Yes | Yes | Handoff for 13B with exact results and next action | §29 | 13B validator + validate_final | Historical entries preserved |
| `docs/PROJECT_PROGRESS.md` | Canonical status | Yes | Yes | Yes | STATUS block agreement and progress entry pointer | §29; progress log | 13B validator + validate_final | STATUS block must agree |
| `docs/ROADMAP.md` | Canonical | Yes | Yes | Yes | Prompt 13 status and next action | §29 | validate_final | 13C/13D remain unstarted |
| `docs/DECISIONS.md` | Canonical | Yes | Yes | Yes | D-206…D-219 recorded; header updated | §27; DD register | 12A/13A validators + 13B validator | Historical rows untouched |
| `docs/stage-2/01_stage_2_prompt_roadmap.md` | Canonical | Yes | Yes | Yes | Prompt 13B row and B-13 deliverable registration | §29 | validate_final | 13C/13D rows unchanged |
| `docs/stage-2/02_master_game_design_bible_outline.md` | Canonical | Yes | Yes | Yes | B-13 status from Planned to drafted/specification complete | §29 | validate_final | No part added or removed |
| `docs/stage-2/03_requirements_traceability.md` | Canonical requirements | Yes | Yes | Yes | Register frontier note `REQ-870`…`REQ-1089`; B-13 rows referenced, not duplicated | §29 | 13B validator | Single B-13 register remains in the parent doc |
| `docs/stage-2/04_approved_and_provisional_decisions.md` | Canonical mirror | Yes | Yes | Yes | DD-254…DD-267 mirrored; version/header updated | D-206…D-219 | 13B validator | Historical rows untouched |
| `docs/stage-2/05_unresolved_design_decisions.md` | Canonical | Yes | No | No | No B-13 question becomes a new UD; owner-reserved rows preserved | §28 | Read only | No edit needed |
| `docs/stage-2/06_stage_2_progress_log.md` | Canonical history | Yes | Yes | Yes | New progress-log §91 Prompt 13B completion entry | §29 | 13B validator | Historical §§1–90 preserved |
| `docs/stage-2/00_stage_2_handoff.md` | Canonical status | Yes | Yes | Yes | Current handoff pointer and status | §29 | validate_final | Historical snapshots preserved |
| `docs/stage-2/21_interface_and_player_journeys.md` | Canonical B-13 | Created | — | Yes | Principal B-13 deliverable | Whole document | 13B validator | New file |
| `docs/stage-2/21_screen_specifications.md` | Canonical B-13 companion | Created | — | Yes | 100 A–K screen bodies | Whole document | 13B validator | New file |
| `docs/stage-2/21_component_specifications.md` | Canonical B-13 companion | Created | — | Yes | 90 components + 8 overlays | Whole document | 13B validator | New file |
| `docs/stage-2/research/13A_politics_and_war_ui_research.md` | Supporting (accepted 13A) | Yes | No | No | Evidence source cited; no reopening | `13A-SRC/BP/DR/FND` | Read only | Preserved |
| `docs/stage-2/research/13A_ui_design_principles_and_architecture.md` | Supporting (accepted 13A) | Yes | No | No | Principles/shell inherited | `13A-PR`, `13A-UR` | Read only | Preserved |
| `docs/stage-2/research/13A_master_screen_inventory.md` | Supporting (accepted 13A) | Yes | No | No | 100 screens and classes preserved; stale `SEC-031` note reconciled here, not by editing 13A | `SCR-001`…`100`, `OVL-01`…`08` | Read only | Preserved |
| `docs/stage-2/research/13A_responsive_and_design_system_foundations.md` | Supporting (accepted 13A) | Yes | No | No | Responsive/token/state foundations inherited | `13A-RD`, `13A-DS` | Read only | Preserved |
| `docs/stage-2/research/13A_ui_requirements_open_questions_and_acceptance.md` | Supporting (accepted 13A) | Yes | No | No | `13A-UR` converted/cited; OQs preserved | `13A-UR`, `13A-OQ`, P13A | Read only | Preserved |
| `docs/prompts/INDEX.md` | Canonical index | Yes | No | No | The Prompt 13B instruction was not archived verbatim in this pass; its execution is recorded in progress-log §91 | Prompt archive | Not archived (documented limitation) | The 12B/12C/13A archives are unchanged |
| `docs/prompts/prompt_13B_screen_and_component_specifications.md` | Historical archive | Not created | — | No | No verbatim archive was produced in this pass | INDEX | Not applicable | Documented limitation; see §30.5 |
| `docs/qa_backups/13B_validate_ui_specifications.py` | QA tool | Created | — | Yes | Focused 13B validator | §29 | Executed | New file |
| `docs/qa_backups/13A_validate_ui_foundations.py` | QA tool (existing) | Yes | Yes | Yes | Frontier refresh only: DD max 267, current status 13C/D-001..D-219/2026-11-13; no rule or check weakened | D-219 | Executed | Documented in report |
| `docs/qa_backups/12A_validate_foundations.py` | QA tool (existing) | Yes | Yes | Yes | Frontier refresh only: REQ max 1089 and decisions range D-001..D-219 | D-217 | Executed | Precedent: 13A refreshed 12A to the 869 frontier |
| `docs/qa_backups/validate_final.py`, `test_next_action.py`, `test_decision_registers.py`, `status_rules.py`, `09_validate.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`, `10B_validate_warfare.py`, `verify_politics_numbers.py`, `test_09A_alliance_validator.py` | QA tools (existing) | Yes | Yes | Yes | Current-prompt/frontier refresh only; no rule, gate or fixture count changed | D-219 | Executed | Exact commands in final report |
| `docs/stage-2/07_core_gameplay_loop...` … `20_fair_play...` (B-02…B-12 families) | Canonical rulebooks | Yes (targeted) | No | No | Rule extraction only; no rule change | B-02…B-12 IDs | Read only | Governing authority untouched |

**Effectiveness note.** Every "Modification required = Yes" row is updated in this pass; no row is reported modified before the edit is made. Historical documents are not rewritten. The only stale 13A citation found (`SCR-096` "SEC-031 spine") is reconciled by an explicit note in §24 and by citing the correct B-12 audit rules; the 13A file is intentionally left unchanged under the no-reopening rule.

**Documentation conflicts resolved.** (1) The B-13 requirement register is owned here; `03_requirements_traceability.md` carries a pointer and the frontier note, not a duplicate table. (2) The screen register remains `13A_master_screen_inventory.md` for identity/class; B-13 owns the detailed body and Matrix A. (3) The decision register remains `DECISIONS.md`; stage-2/04 mirrors it. No contradictory copy is created.

---

## 30. Scope boundaries and handoff to Prompt 13C

### 30.1 What this pass delivered

- The three B-13 documents (parent, screen catalogue, component catalogue).
- 100 complete A–K screen specifications with all 11 fields.
- 90 component specifications with all 19 fields and 8 overlay specifications with page equivalents.
- The navigation register (100 screens, canonical parents, route keys, aliases, restrictions).
- Desktop/tablet/mobile duties for every screen and component.
- The B-13 requirement block `REQ-870`…`REQ-1089` with Matrix C.
- Matrices A, B and C; the map/Network View reconciliation; decisions D-206…D-219 and DD-254…DD-267.
- The documentation impact register (§29) and the focused 13B validator.

### 30.2 What is explicitly not delivered (13C)

Complete player journeys; cross-system interaction sequences; detailed interaction flows; full onboarding/tutorial specifications; loading/empty/success/failure journeys; validation and error-handling logic; notification/feedback sequences; end-to-end accessibility interaction verification; cross-screen behavioural consistency audits. **13C is NOT STARTED and NOT AUTHORIZED by this document.**

### 30.3 What is explicitly not delivered (13D)

Independent Prompt 13 completeness audit; final cross-system acceptance; complete UI acceptance-test suites; final integration contracts; final Prompt 13 acceptance gates and closure report. **13D is NOT STARTED.**

### 30.4 Next action

**Post-acceptance update (2026-11-13).** Prompt 13B and Prompt 13C are OWNER ACCEPTED (D-233); Prompt 13B-C1 and Prompt 13B-C1-R1 are COMPLETE and Prompt 13C-C1 is COMPLETE AND INDEPENDENTLY VERIFIED. At original 13B completion the next planned phase was Prompt 13C, which required separate owner authorization; that state is superseded by this update. **Prompt 13D is NOT STARTED / NOT AUTHORIZED.** No frontend implementation is authorized by any statement in this file.

### 30.5 Ultimate acceptance test — self-assessment

A future frontend developer can determine from these documents: what every screen contains (screen bodies A–F); how it is arranged (field E); which components it uses (§25 Matrix B and the §25.1 reverse index); what each control does and under which rule (field G, requirement rows); how screens connect (parent §7); how each adapts to desktop/tablet/mobile (field I, §8); which information is public/private/restricted/suppressed (field F, §9); which visual system applies (component catalogue, semantic tokens); and which dependencies and unresolved matters remain (§28). What these documents do **not** provide — complete journeys and interaction sequencing — is the deliberate 13C boundary, not an omission.
---

## 31. Prompt 13B-C1 correction impact register (2026-11-13)

**Relationship to §29.** This register records the subsequent Prompt 13B-C1 corrections to the historical documentation impact assessment in §29. It does not rewrite §29's original findings; the two registers together preserve the chronology: §29 is the assessment at original Prompt 13B completion, and §31 is the later bounded correction record.

**Authority:** the owner's Prompt 13B-C1 instruction. **Scope:** bounded correction of internal references, prompt archival, working-tree reporting and documentation-link reconciliation. No screen or component specification was rewritten; no game rule, requirement status, decision, owner-reserved matter or implementation changed. The decision frontier remains **D-219 / DD-267**; no new decision was necessary because these are corrections to an existing specification, not new design choices.

| Document path | Previous condition | Correction made | Validation performed | Final result |
|---|---|---|---|---|
| `docs/stage-2/21_interface_and_player_journeys.md` | References used the original 30-section prompt map (sections 20–22, 21, 23, 18, 22.10, 23.1–23.7 and 22); the catalogue table labels 5.1–5.10 had no matching local headings | References corrected to the actual structure (`§8`–`§10`, `§9`, `§11`, `§3.2; screen companion §10`, `§29`, `§27.1`); `5.1`–`5.10` retained as catalogue-group labels without the section marker; a numbering note explains that the planned sections 13–23 family bodies live in the screen companion | `13B-25`, `13B-26`; 26/26 checks; self-test 7/7 | **PASS** |
| `docs/stage-2/21_screen_specifications.md` | One ambiguous `12.3` reference next to `WAR-152` could be read as a local section | Rewritten as `WAR §12.3`; no other internal section reference defect found | `13B-25`, `13B-26` | **PASS** |
| `docs/stage-2/21_component_specifications.md` | No broken numbered-section or heading-anchor reference found; `§1.3` is local and valid | None | `13B-25`, `13B-26` | **PASS** |
| `docs/prompts/prompt_13B_screen_and_component_specifications.md` | Absent | Created from the authorized Prompt 13B instruction; one provenance paragraph added after the title; all 26 instruction sections present | Archive section count, stored-bytes SHA-256, `13B-27` | **PASS with recovery limitation**: no independent external original exists for byte-for-byte comparison |
| `docs/prompts/INDEX.md` | No Prompt 13B row | Added the Prompt 13B archive row with source, byte/line counts and stored-bytes SHA-256; appended the scope-note sentence | `13B-27`, `validate_links.py` | **PASS** |
| `docs/qa_backups/13B_validate_ui_specifications.py` | 24 checks; 3 self-tests; no section/anchor checks | Added `13B-25` section-reference validation, `13B-26` heading-anchor validation, and positive/negative fixtures; added archive checks `13B-27`/`13B-28` | `13B_validate_ui_specifications.py`; `--self-test` | **PASS**: 28/28 checks; 7/7 self-tests |
| `docs/stage-2/06_stage_2_progress_log.md` | progress-log §91.6 recorded 106 files / 4,139 links / 3,757 local / 382 external / 0 unresolved from the Prompt 13B run | Added progress-log §91.9 with the 13B-C1 rerun, actual counts and the 24-substantive/116-line-ending classification; progress-log §91.6 preserved as the original dated result | `validate_links.py`; `13B` validator | **PASS** (see progress-log §91.9) |
| `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/PROJECT_PROGRESS.md` | 13B complete; no 13B-C1 correction note | Appended a 13B-C1 correction clause to the existing `ui_foundations` status value in all three files, keeping them identical | `13B-18`; `validate_final.py` | **PASS** |
| `docs/stage-2/00_stage_2_handoff.md`, `docs/stage-2/01_stage_2_prompt_roadmap.md`, `docs/stage-2/02_master_game_design_bible_outline.md` | 13B complete; no 13B-C1 note | Added a correction-complete note; next action remains owner review, Prompt 13C unauthorized | `validate_final.py`; `test_next_action.py` | **PASS** |
| `docs/ROADMAP.md` | 13B status already accurate | No change required; no status or scope changed by a corrective pass | Inspection | **Unchanged** |
| `docs/DECISIONS.md`, `docs/stage-2/04_approved_and_provisional_decisions.md` | D-219 / DD-267 frontier | No new decision; correction register records the changes instead | Inspection | **Unchanged** |
| `docs/stage-2/03_requirements_traceability.md` | `REQ-870`…`REQ-1089` pointer already present | No change required; no requirement allocated or renumbered | Inspection | **Unchanged** |
| Pre-existing line-ending-only tracked files (116) | Byte-different from HEAD, content-identical after CRLF/LF normalization; provenance uncertain | Preserved; not normalized, restored or discarded | Content-normalized classification only | **Preserved** |
| Pre-existing substantive modifications (24) and untracked B-13/validator files | Existing 13B work | Preserved; 13B-C1 added only the corrections listed above; the final tree has 25 substantive tracked modifications (the 24 plus `INDEX.md`) and 5 untracked files (the 4 plus the new archive) | `git status`; content-normalized comparison | **Preserved** |
