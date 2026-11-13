# B-13 companion — Reusable component specifications (UI-CMP-001…UI-CMP-090 and OVL-01…OVL-08)

**Parent:** [B-13](21_interface_and_player_journeys.md) (authority, registers, matrices and requirements).
**Created:** 2026-11-13 (Prompt 13B). **Status:** specification only; no component, style, framework or code exists.
**Scope:** the 90 reusable components named by the Prompt 13B instruction §7.1–§7.7 plus the eight existing overlays `OVL-01`…`OVL-08`. The component identifier family `UI-CMP-` is new (D-207); overlays keep their 13A identifiers.

---

## 1. Global rules inherited by every component

Every component block below answers the same 19 fields. Where a field says **Inherits G-*x***, the following global rule applies and the block adds only its specifics.

### 1.1 Global fields

| Global ID | Field | Rule |
|---|---|---|
| **G-1** | Visual structure | Four-pt spacing scale, 12-column content grid, semantic surface/border/text tokens, status tone tokens, typography registers (display, text, data). No raw colour, typeface, size or spacing value is permitted (D-203, `13A-DS-01`…`13A-DS-06`). |
| **G-2** | Content fields | Text is localization-ready; numbers carry unit and as-of turn; status carries a text label; no gameplay-critical text inside an image (`13A-DS-15`, `REQ-1087`). |
| **G-3** | Required and optional properties | Required properties are those without which the component cannot be rendered truthfully (identity, state, value, unit, source); optional properties may be omitted but never replaced with an invented default that changes meaning. |
| **G-4** | Information hierarchy | Within a component, the primary value is first in reading order; supporting metadata follows; warnings are not visually subordinate to decoration; progressive explanation uses `OVL-04` or a labelled disclosure. |
| **G-5** | Data presentation | A forecast is visually lighter than a current value; suppressed/insufficient states are named; no bare "balance"; no zero substitute; no dual-axis; no unlabelled aggregate (ECN-177/178, MKT-053, D-027, WEP-324). |
| **G-6** | Permitted interactions | Only interactions the governing rules support. Hover is an enhancement and never load-bearing; every hover-revealed fact is reachable by focus/click (`13A-RD-02`). |
| **G-7** | Disabled state | Every disabled control shows its reason before activation and links the governing rule (`OVL-03`, `13A-PR-10`, `REQ-976`). A disabled control is never hidden to avoid explaining a rule. |
| **G-8** | Responsive | Desktop/tablet/mobile behaviour is defined; the component preserves its non-negotiable fields in the narrowest layout; no horizontal page scroll; touch targets meet `13A-DS-14` (D-211, `REQ-1015`). |
| **G-9** | Accessibility | Keyboard operability, visible focus, programmatic labels, semantic structure, error text, colour+glyph+text, text alternative where visual, reduced motion (D-203, `13A-DS-07`…`13A-DS-15`, `REQ-1081`…`REQ-1087`). |
| **G-10** | Semantic tokens | Surface, text, border, focus, status tones (`informational`, `pending`, `success`, `warning`, `danger`, `locked/denied`, `suppressed`), typography, spacing, radius, elevation, motion. Brand values are owner-reserved (`13A-OQ-001/002`). |
| **G-11** | States and variants | Applicable states come from `default`, `hover`, `focus-visible`, `active`, `disabled(+reason)`, `loading`, `success`, `warning`, `error`, `pending`, `suppressed`; no parallel state names (`REQ-1014`). |
| **G-12** | Related requirements | The exact `REQ-` rows in Matrix B/C. Inheritance from a 13A `UR-` candidate is cited, never re-allocated. |
| **G-13** | Screens using the component | The authoritative sets are Matrix B and the screen bodies; the block lists the owning screens. |
| **G-14** | Reuse restrictions | No component may be reused to display a different number type, a higher visibility class or a state the governing rule does not define. |
| **G-15** | Dependencies and unresolved questions | Exact rule/decision identifiers; owner-reserved and provisional items remain labelled. |

### 1.2 Global state treatment

| State | Visual distinction | Textual/glyph indication | Interaction | Accessibility |
|---|---|---|---|---|
| default | Base surface/border | Normal label | Available | Normal semantics |
| hover | Subtle surface shift | None required | Enhancement only | Never the only reveal |
| focus-visible | Tokenized focus ring ≥3:1 | None | Keyboard available | Focus announced |
| active | Pressed/selected surface | Selected label/`aria-pressed` | Available | State exposed |
| disabled | Muted surface + lock glyph | Reason string via `OVL-03` | Unavailable | `aria-disabled` + described-by reason |
| loading | Skeleton within bounds | "Loading" label | Suspended | Polite live-region; no full-page spinner |
| success | Success tone + check glyph | "Completed"/"Settled" | Follow-up per rule | Announced |
| warning | Warning tone + triangle glyph | Warning text | Available/limited | Announced |
| error | Danger tone + error glyph | Error text linked to field | Retry where safe | `aria-invalid` + message |
| pending | Pending tone + clock glyph | "Pending"/"Reserved"/"Queued" | Limited per rule | Announced as pending |
| suppressed | Suppressed tone + eye-off glyph | "Not disclosed"/"Insufficient sample" | Not expandable to reveal | Announced as suppressed |

Motion: state changes use reduced-motion-safe transitions; no motion is gameplay (`13A-DS-13`). Colour alone never communicates state (`13A-DS-10`).

### 1.3 Overlay discipline (applies to OVL-01…08)

Modals only for confirmation, blocking reason or explanation; drawers/sheets for contextual read-mostly tasks; peek cards for previews. **Every overlay state has a page-reachable equivalent** (`UR-033`, D-215). An overlay never becomes the only place a fact, a state or an action exists. Focus is trapped and restored. Dismissal never commits. `OVL-02` requires the exact phrase and never remembers confirmation across turns.

---

## 2. Application-shell components — UI-CMP-001…UI-CMP-011

### UI-CMP-001 — Global application shell

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-001` |
| 2 | Name | Global application shell |
| 3 | Purpose | Hosts every screen inside one stable frame so location, turn context and pending work remain visible. |
| 4 | Category | Shell; **Global** |
| 5 | Visual structure | Fixed slots: identity strip, primary nav, alert bar, quick-go, breadcrumb, content, context panel, footer (G-1). |
| 6 | Content fields | Nation identity, permitted treasury/stability bands, protection badge, turn indicator, alert count, content slot, context slot, footer links. |
| 7 | Required/optional | Required: content slot, turn indicator, alert bar. Optional: context panel (collapses), identity strip on public screens (reduced). |
| 8 | Hierarchy | Turn/alert context above content; content above footer; context panel secondary. |
| 9 | Data rules | Shell values are visibility-checked; no exact treasury above class; no other player's data (G-5, TR-021). |
| 10 | Interactions | Navigation, quick-go, alert open, context links; no committing action. |
| 11 | Disabled | Shell never disables globally; a denied destination is `UI-CMP-089`. |
| 12 | Responsive | Desktop slots as defined; tablet context → sheet; mobile header band + content + bottom access (G-8). |
| 13 | Accessibility | Landmark roles, skip link, focus order, titled page, polite countdown (G-9). |
| 14 | Tokens | Surface/text/border/focus/status (G-10). |
| 15 | States | default, loading, error, stale, permission-denied, interrupted-turn (G-11). |
| 16 | Requirements | `REQ-970`, `REQ-974`, `REQ-975`, `REQ-976`, `REQ-979`. |
| 17 | Screens | All authenticated; reduced public shell on `SCR-001`…`SCR-007`. |
| 18 | Reuse restrictions | Only one shell instance; never nests inside an overlay; public variant never renders authenticated data. |
| 19 | Dependencies | D-201; `13A-BP-001`; `13A-SRC-017` (frame evidence, bounded). |

### UI-CMP-002 — Primary navigation

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-002` |
| 2 | Name | Primary navigation |
| 3 | Purpose | Switches between the eight authenticated sections. |
| 4 | Category | Shell; **Global** |
| 5 | Visual structure | Horizontal section bar on desktop; icon rail/overflow on tablet; compact menu on mobile. |
| 6 | Content fields | Section labels (Home, Economy, Cities, Politics, Foreign, War, World, Account), active marker, admin entry only if holder. |
| 7 | Required/optional | Required: all eight sections, active state. Optional: overflow group. |
| 8 | Hierarchy | Active section first in emphasis; no metric badges that imply urgency. |
| 9 | Data rules | No live numbers in nav; alert count belongs to `UI-CMP-008`. |
| 10 | Interactions | Navigate; keyboard traversal; overflow open. |
| 11 | Disabled | Conditional routes absent; role routes hidden; denied target explains (G-7). |
| 12 | Responsive | Desktop bar; tablet rail; mobile menu + bottom access (G-8). |
| 13 | Accessibility | `nav` landmark, current-page state, roving focus (G-9). |
| 14 | Tokens | Surface/text/focus (G-10). |
| 15 | States | default, hover, focus-visible, active, disabled+reason, overflow (G-11). |
| 16 | Requirements | `REQ-971`, `REQ-1013`. |
| 17 | Screens | All authenticated; never on Admin root. |
| 18 | Reuse restrictions | No second primary nav; no admin entry in player nav. |
| 19 | Dependencies | D-201, D-209. |

### UI-CMP-003 — Secondary navigation

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-003` |
| 2 | Name | Secondary navigation |
| 3 | Purpose | Switches same-object views without leaving the object. |
| 4 | Category | Shell; **Global** |
| 5 | Visual structure | In-page tab row or section index. |
| 6 | Content fields | Tab labels, active tab, optional count where a rule defines one. |
| 7 | Required/optional | Required: labels, active state. Optional: count. |
| 8 | Hierarchy | Active tab first in emphasis. |
| 9 | Data rules | Counts are exact or absent; no implied urgency. |
| 10 | Interactions | Tab switch, keyboard. |
| 11 | Disabled | A tab the viewer cannot access is absent or disabled with reason. |
| 12 | Responsive | Desktop tabs; tablet scrollable tabs; mobile select or accordion (G-8). |
| 13 | Accessibility | `tablist`/`tab` semantics or section nav; current state. |
| 14 | Tokens | G-10. |
| 15 | States | default, hover, focus-visible, active, disabled+reason. |
| 16 | Requirements | `REQ-972`. |
| 17 | Screens | Section hubs and object pages. |
| 18 | Reuse restrictions | Same-object views only; never duplicates primary nav items. |
| 19 | Dependencies | D-201. |

### UI-CMP-004 — Page heading

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-004` |
| 2 | Name | Page heading |
| 3 | Purpose | Names the screen and anchors its identity and rule context. |
| 4 | Category | Shell; **Global** |
| 5 | Visual structure | Display-register title, optional subtitle, governing-section anchor. |
| 6 | Content fields | Canonical screen name, optional as-of turn, governing rule link. |
| 7 | Required/optional | Required: screen name. Optional: subtitle, anchor. |
| 8 | Hierarchy | First heading in the content region. |
| 9 | Data rules | As-of turn if the screen is data-bearing. |
| 10 | Interactions | Rule anchor link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Title wraps; anchor may move below (G-8). |
| 13 | Accessibility | Exactly one `h1`; focus target on route change (G-9). |
| 14 | Tokens | Display typography (G-10). |
| 15 | States | default, loading title, error title. |
| 16 | Requirements | `REQ-1013`. |
| 17 | Screens | All screens. |
| 18 | Reuse restrictions | One per screen; not used for section subheadings. |
| 19 | Dependencies | `13A-DR-009/010`. |

### UI-CMP-005 — Breadcrumb / context locator

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-005` |
| 2 | Name | Breadcrumb / context locator |
| 3 | Purpose | Shows depth and allows return to an ancestor object. |
| 4 | Category | Shell; **Global** |
| 5 | Visual structure | Ancestor links separated by a locator glyph, current page plain text. |
| 6 | Content fields | Ancestor names/routes, current name. |
| 7 | Required/optional | Required at depth ≥ 2. |
| 8 | Hierarchy | Above the content, below nav. |
| 9 | Data rules | Uses canonical route/name; aliases do not create a second crumb. |
| 10 | Interactions | Ancestor navigation. |
| 11 | Disabled | Denied ancestor not shown; no dead crumb. |
| 12 | Responsive | Collapses to parent + current on mobile (G-8). |
| 13 | Accessibility | `nav` with `aria-label="Breadcrumb"`; current page `aria-current`. |
| 14 | Tokens | G-10. |
| 15 | States | default, truncated-path, permission-limited. |
| 16 | Requirements | `REQ-973`. |
| 17 | Screens | Depth ≥ 2. |
| 18 | Reuse restrictions | Not for multi-step forms; those use step indicators. |
| 19 | Dependencies | D-209. |

### UI-CMP-006 — Account & nation context

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-006` |
| 2 | Name | Account & nation context |
| 3 | Purpose | Shows who is signed in and which nation is active, with state chips. |
| 4 | Category | Shell; **Global** |
| 5 | Visual structure | Nation name/emblem, account menu, state chip. |
| 6 | Content fields | Nation name, short name, account state, verification, closure state. |
| 7 | Required/optional | Required: identity. Optional: state chip when normal. |
| 8 | Hierarchy | Identity before menu. |
| 9 | Data rules | ACC-018 neutral wording; no account ID/IP. |
| 10 | Interactions | Account menu, switch to account home. |
| 11 | Disabled | Restricted states remain navigable to recourse. |
| 12 | Responsive | Collapses to name + menu (G-8). |
| 13 | Accessibility | Labelled menu button, state text (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, unverified, restricted, closed, pending-closure. |
| 16 | Requirements | `REQ-974`. |
| 17 | Screens | All authenticated. |
| 18 | Reuse restrictions | Never shows another player's account context. |
| 19 | Dependencies | ACC-017/018. |

### UI-CMP-007 — Turn & settlement indicator

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-007` |
| 2 | Name | Turn & settlement indicator |
| 3 | Purpose | Communicates turn, boundary, settlement state and phase position. |
| 4 | Category | Shell; **Data presentation**; **Global** |
| 5 | Visual structure | Turn number, UTC boundary, state glyph/tone, optional phase badge. |
| 6 | Content fields | Current turn, next boundary UTC, turns remaining, settlement state, phase. |
| 7 | Required/optional | Required on every authenticated screen. |
| 8 | Hierarchy | Always visible in the header band. |
| 9 | Data rules | Turns+UTC source of truth; wall clock cosmetic only (G-5). |
| 10 | Interactions | Open turn status `SCR-016`. |
| 11 | Disabled | Not applicable; read-only. |
| 12 | Responsive | Full on desktop; compact turn+boundary on mobile (G-8). |
| 13 | Accessibility | Polite live-region; no constant announcements (G-9). |
| 14 | Tokens | Pending/danger tones (G-10). |
| 15 | States | open, locked, resolving, completed, interrupted, failed, stale. |
| 16 | Requirements | `REQ-975`, `REQ-1007`. |
| 17 | Screens | All authenticated. |
| 18 | Reuse restrictions | One per shell; not duplicated inside content. |
| 19 | Dependencies | TR-024/030/035/080. |

### UI-CMP-008 — Global notification indicator

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-008` |
| 2 | Name | Global notification indicator |
| 3 | Purpose | Signals unread/priority notifications without creating one. |
| 4 | Category | Shell; **Interaction control**; **Global** |
| 5 | Visual structure | Bell/alerts glyph + count + highest tone. |
| 6 | Content fields | Count, priority tone, label. |
| 7 | Required/optional | Required. |
| 8 | Hierarchy | Top bar, below identity. |
| 9 | Data rules | Counts from existing events; non-opt-out marked; no fabricated count. |
| 10 | Interactions | Open alerts `SCR-019`; open Inbox `SCR-014`. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Icon + count on mobile (G-8). |
| 13 | Accessibility | Labelled button with count; live-region on change (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | default, pending, danger, muted, non-opt-out. |
| 16 | Requirements | `REQ-976`. |
| 17 | Screens | All authenticated. |
| 18 | Reuse restrictions | Presentation only; never an event author. |
| 19 | Dependencies | REQ-731; DIP-114/116. |

### UI-CMP-009 — Contextual navigation

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-009` |
| 2 | Name | Contextual navigation |
| 3 | Purpose | Links related objects/screens for the current object or task. |
| 4 | Category | Shell; **Navigation**; **Global** |
| 5 | Visual structure | Labelled link list or chips in the context panel. |
| 6 | Content fields | Destination label, object identity, relation reason. |
| 7 | Required/optional | Optional per screen; required where a relationship is specified. |
| 8 | Hierarchy | Supporting tier. |
| 9 | Data rules | Links only to permitted destinations. |
| 10 | Interactions | Navigate, peek. |
| 11 | Disabled | Denied destination absent or explained. |
| 12 | Responsive | Context panel → sheet; inline links remain (G-8). |
| 13 | Accessibility | List semantics; link names not "click here" (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, permission-limited, conditional-absent. |
| 16 | Requirements | `REQ-977`. |
| 17 | Screens | Object/detail/task screens. |
| 18 | Reuse restrictions | Does not replace related-object links in content. |
| 19 | Dependencies | `13A-PR-13`. |

### UI-CMP-010 — Admin entry and role-gated navigation

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-010` |
| 2 | Name | Admin entry and role-gated navigation |
| 3 | Purpose | Provides the separate admin root and only the role-permitted workspaces. |
| 4 | Category | Shell; **Permissions**; **Role-restricted** |
| 5 | Visual structure | Admin-root header, role chip, workspace list. |
| 6 | Content fields | Role(s), permitted workspaces, step-up/emergency posture. |
| 7 | Required/optional | Required for admin sessions. |
| 8 | Hierarchy | Role/scope first; workspaces second. |
| 9 | Data rules | No case data on the index; no `SEC` to unpermitted roles. |
| 10 | Interactions | Navigate; step-up where required. |
| 11 | Disabled | Unheld workspace absent; denied deep link explains without confirming case existence. |
| 12 | Responsive | Desktop sidebar; mobile list (G-8). |
| 13 | Accessibility | `nav` with role context; no hidden focus traps (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, denied, step-up-required, emergency. |
| 16 | Requirements | `REQ-978`, `REQ-1037`. |
| 17 | Screens | `SCR-091`…`SCR-100`. |
| 18 | Reuse restrictions | Never appears in the player shell; never renders player nav. |
| 19 | Dependencies | D-042; ADM-003. |

### UI-CMP-011 — Footer / help access

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-011` |
| 2 | Name | Footer / help access |
| 3 | Purpose | Carries help, support, report, terms and change-disclosure access. |
| 4 | Category | Shell; **Navigation**; **Global** |
| 5 | Visual structure | Compact link row with grouped secondary links. |
| 6 | Content fields | Help index, support, report, terms, privacy, change disclosures, version. |
| 7 | Required/optional | Required on every screen; public variant reduced. |
| 8 | Hierarchy | Below content, visually quiet. |
| 9 | Data rules | No case/report state implied; version is a dated record. |
| 10 | Interactions | Navigation. |
| 11 | Disabled | Degraded support shows a retryable state, never a dead link. |
| 12 | Responsive | Wraps into groups; no hidden links (G-8). |
| 13 | Accessibility | `contentinfo` landmark; link labels (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, degraded-support. |
| 16 | Requirements | `REQ-979`. |
| 17 | Screens | All screens. |
| 18 | Reuse restrictions | Separate support from report routes. |
| 19 | Dependencies | MOD-002; MOD-013; TR-049. |

## 3. Information-display components — UI-CMP-012…UI-CMP-030

### UI-CMP-012 — Statistic card

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-012` |
| 2 | Name | Statistic card |
| 3 | Purpose | Presents one headline figure with its number type, unit and time reference. |
| 4 | Category | Display; **Global**; system-agnostic |
| 5 | Visual structure | Label, data-register value, unit, number-type tag, as-of turn, optional trend. |
| 6 | Content fields | Label, value, unit, number type, as-of turn, state, link. |
| 7 | Required/optional | Required: label, value/state, unit, type, time. Optional: trend, link. |
| 8 | Hierarchy | Value primary; type/time secondary; link tertiary. |
| 9 | Data rules | Six-number-type label mandatory; forecast lighter; suppressed state instead of zero (G-5, ECN-177). |
| 10 | Interactions | Optional link to owning screen; no inline editing. |
| 11 | Disabled | Not applicable; a missing value renders its named state. |
| 12 | Responsive | Grid 3×2 → 2×3 → stacked (G-8). |
| 13 | Accessibility | Value + unit + turn read as one phrase (G-9). |
| 14 | Tokens | Data typography, status tones (G-10). |
| 15 | States | default, loading, zero-real, forecast, suppressed, stale. |
| 16 | Requirements | `REQ-980`, `REQ-1062`, `REQ-1063`. |
| 17 | Screens | `SCR-013/015/021/023/029/041/059/072/074`. |
| 18 | Reuse restrictions | One number type per card; never merges current and forecast. |
| 19 | Dependencies | ECN-177/178; D-056. |

### UI-CMP-013 — Metric group

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-013` |
| 2 | Name | Metric group |
| 3 | Purpose | Groups related metrics for scanning while preserving individual meaning. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Equal-weight cells with individual labels and type tags. |
| 6 | Content fields | Group label, metrics (each label/value/unit/type/time). |
| 7 | Required/optional | Required: group label, at least two metrics. |
| 8 | Hierarchy | Group label; metrics equal; no merged aggregate. |
| 9 | Data rules | No summing across number types; no composite score (G-5). |
| 10 | Interactions | Per-metric links. |
| 11 | Disabled | Missing metric shows state. |
| 12 | Responsive | 4→2→1 columns (G-8). |
| 13 | Accessibility | Group label via `fieldset`/`aria-labelledby` (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, loading, partial, suppressed. |
| 16 | Requirements | `REQ-981`, `REQ-1063`. |
| 17 | Screens | `SCR-013/015/029/041/059/072`. |
| 18 | Reuse restrictions | Never used to create a composite headline. |
| 19 | Dependencies | WEP-361/362. |

### UI-CMP-014 — Financial summary

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-014` |
| 2 | Name | Financial summary |
| 3 | Purpose | Presents opening position, flows and closing position without implying credit. |
| 4 | Category | Display; **Economic** |
| 5 | Visual structure | Stacked ledger rows with signs, units, and a net-change row. |
| 6 | Content fields | Opening balance, income, expenditure, net change, closing, capex/opex split. |
| 7 | Required/optional | Required: all flow rows, units, as-of. |
| 8 | Hierarchy | Closing/available first; flows second; detail links third. |
| 9 | Data rules | No negative balance below zero; unpaid obligations cancelled; forecast labelled (G-5, D-050). |
| 10 | Interactions | Drill to report `SCR-031`; no inline spend. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Table → stacked rows (G-8). |
| 13 | Accessibility | Ledger semantics; signs announced (G-9). |
| 14 | Tokens | Data typography, danger for shortfall (G-10). |
| 15 | States | default, negative-projected, zero, forecast, stale. |
| 16 | Requirements | `REQ-982`, `REQ-1000`. |
| 17 | Screens | `SCR-029/030/031/037/057`. |
| 18 | Reuse restrictions | No credit/overdraft line may be added. |
| 19 | Dependencies | ECN-093/097/098; D-050/D-051. |

### UI-CMP-015 — Resource balance display

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-015` |
| 2 | Name | Resource balance display |
| 3 | Purpose | Shows one resource's quantity within a context that already exposes the triple. |
| 4 | Category | Display; **Economic** |
| 5 | Visual structure | Resource name, quantity, unit, capacity context, optional reserved marker. |
| 6 | Content fields | Resource, total/reserved/available, unit, capacity, state. |
| 7 | Required/optional | Required: the triple when used alone. |
| 8 | Hierarchy | Available first where the task is spending; total first where the task is inventory. |
| 9 | Data rules | Never a bare balance; whole units; no market price pre-gate (G-5, MKT-053). |
| 10 | Interactions | Link to warehouse; no free transfer. |
| 11 | Disabled | Capacity-full state explains blocking. |
| 12 | Responsive | Row → stacked triple (G-8). |
| 13 | Accessibility | Triple read as labelled values (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, reserved, empty, capacity-full, suppressed. |
| 16 | Requirements | `REQ-983`, `REQ-1001`, `REQ-1065`. |
| 17 | Screens | `SCR-033/035/036/037/042/043/056/057`. |
| 18 | Reuse restrictions | Only within a composite context; the standalone triple uses `UI-CMP-033`. |
| 19 | Dependencies | MKT-053; ECN-120. |

### UI-CMP-016 — Progress indicator

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-016` |
| 2 | Name | Progress indicator |
| 3 | Purpose | Shows progress toward a named target or a phase position. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Label, current/total, bar or steps, state glyph. |
| 6 | Content fields | What is progressing, current, total, unit, state. |
| 7 | Required/optional | Required: label, current, total. Optional: steps. |
| 8 | Hierarchy | Label first; current/total second. |
| 9 | Data rules | No fake precision; no progress where the rule defines only states. |
| 10 | Interactions | Optional link to owning screen. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Bar scales; steps wrap (G-8). |
| 13 | Accessibility | `progressbar` with value text; steps announced (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | default, pending, success, warning, error, indeterminate. |
| 16 | Requirements | `REQ-984`. |
| 17 | Screens | `SCR-016/025/043/045/074`. |
| 18 | Reuse restrictions | Not a gamified streak/attendance meter. |
| 19 | Dependencies | AP-001. |

### UI-CMP-017 — Status banner

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-017` |
| 2 | Name | Status banner |
| 3 | Purpose | Announces a screen-level state with cause and end condition. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Tone surface + glyph + title + cause + end turn + action link. |
| 6 | Content fields | State label, cause, end/review turn, what is locked, action. |
| 7 | Required/optional | Required: state label, cause. Optional: end, action. |
| 8 | Hierarchy | Above primary content when action-affecting. |
| 9 | Data rules | State names from the owning system; never a penalty label for a game state (G-5). |
| 10 | Interactions | Action link to the owning surface. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Full width; explanatory text may collapse (G-8). |
| 13 | Accessibility | `role="status"`/`alert` as appropriate; not colour-only (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | informational, pending, success, warning, danger, locked. |
| 16 | Requirements | `REQ-985`, `REQ-1010`. |
| 17 | Screens | Political, state, restriction and admin status surfaces. |
| 18 | Reuse restrictions | No account-penalty framing; no urgency theatrics. |
| 19 | Dependencies | DMP-268; ACC-018. |

### UI-CMP-018 — Warning panel

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-018` |
| 2 | Name | Warning panel |
| 3 | Purpose | Explains a condition, its consequence, its end and the available actions. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Warning title, condition, consequence, end/review, action list. |
| 6 | Content fields | Condition, consequence, end/review turn, actions, rule link. |
| 7 | Required/optional | Required: condition, consequence. Optional: action. |
| 8 | Hierarchy | Above supporting data; never displaces the primary register. |
| 9 | Data rules | No warning without an action or explanation (G-5). |
| 10 | Interactions | Action links. |
| 11 | Disabled | A blocked action explains why. |
| 12 | Responsive | Full width; action list stacks (G-8). |
| 13 | Accessibility | `role="alert"` only for genuinely urgent; otherwise labelled region (G-9). |
| 14 | Tokens | Warning/danger tones (G-10). |
| 15 | States | default, warning, danger, suppressed. |
| 16 | Requirements | `REQ-986`. |
| 17 | Screens | `SCR-015/028/030/043/063/084/089`. |
| 18 | Reuse restrictions | Not for marketing or non-actionable notices. |
| 19 | Dependencies | DMP-163; ECN-182. |

### UI-CMP-019 — Information panel

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-019` |
| 2 | Name | Information panel |
| 3 | Purpose | Holds explanatory or contextual content distinct from the primary data. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Quiet surface, heading, prose, optional rule anchor. |
| 6 | Content fields | Heading, body, state label, rule link. |
| 7 | Required/optional | Required: heading/body. Optional: link. |
| 8 | Hierarchy | Supporting/progressive tier. |
| 9 | Data rules | Distinguishes fact/provisional/forecast/suppressed (G-5). |
| 10 | Interactions | Links; disclosure. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Prose measure; collapsible on mobile (G-8). |
| 13 | Accessibility | Heading hierarchy; readable measure (G-9). |
| 14 | Tokens | Text typography (G-10). |
| 15 | States | default, loading, empty, provisional-block. |
| 16 | Requirements | `REQ-987`. |
| 17 | Screens | All read surfaces. |
| 18 | Reuse restrictions | Not a container for primary data. |
| 19 | Dependencies | `13A-PR-05`. |

### UI-CMP-020 — Historical record

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-020` |
| 2 | Name | Historical record |
| 3 | Purpose | Presents a record with its turn, class and retention boundary. |
| 4 | Category | Display; **Data presentation** |
| 5 | Visual structure | Turn stamp, class label, record body, retention marker. |
| 6 | Content fields | Turn, event/class, participants, outcome, public/restricted, retention. |
| 7 | Required/optional | Required: turn, class, outcome. |
| 8 | Hierarchy | Turn/class first; outcome second. |
| 9 | Data rules | No silent omission; retention labelled (G-5, D-026). |
| 10 | Interactions | Object links; no edit. |
| 11 | Disabled | Restricted content absent/labelled, never blank. |
| 12 | Responsive | Table→card (G-8). |
| 13 | Accessibility | Time/class announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, retention-boundary, restricted, retired. |
| 16 | Requirements | `REQ-988`, `REQ-1008`. |
| 17 | Screens | `SCR-017/031/052/066/075/076/085`. |
| 18 | Reuse restrictions | Cannot be repurposed as a live current-state card. |
| 19 | Dependencies | D-026; TR-092. |

### UI-CMP-021 — Timeline

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-021` |
| 2 | Name | Timeline |
| 3 | Purpose | Shows ordered state transitions for an object or process. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Vertical/horizontal ordered nodes with turn labels and states. |
| 6 | Content fields | Node title, turn, state, description, link. |
| 7 | Required/optional | Required: order, turn, state. Optional: link. |
| 8 | Hierarchy | Current node emphasized; future nodes not implied as certain. |
| 9 | Data rules | Pending vs completed distinct; no future outcome the rules do not determine (G-5). |
| 10 | Interactions | Node link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Vertical on mobile; no horizontal clipping (G-8). |
| 13 | Accessibility | Ordered list semantics; current step announced (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | default, pending, completed, voided, suppressed. |
| 16 | Requirements | `REQ-989`. |
| 17 | Screens | `SCR-017/027/050/051/052/066/070/076`. |
| 18 | Reuse restrictions | Not for non-chronological lists. |
| 19 | Dependencies | TR-004; WAR-125. |

### UI-CMP-022 — Data table

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-022` |
| 2 | Name | Data table |
| 3 | Purpose | Presents comparable rows with stable columns, filters and pagination. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Caption, semantic header row, optional filter row, body rows, pagination. |
| 6 | Content fields | Caption, columns, rows, row links, empty state, exact counts. |
| 7 | Required/optional | Required: caption/name, headers, rows or empty state. |
| 8 | Hierarchy | Identity column first; status near identity; actions last. |
| 9 | Data rules | Exact counts; no hidden rows; suppression states (G-5). |
| 10 | Interactions | Sort, row link, filter, paginate, saved view. |
| 11 | Disabled | Row-level denied action explains. |
| 12 | Responsive | Column priority + pinned identity; mobile card fallback preserving non-negotiables (G-8). |
| 13 | Accessibility | `table` semantics, scope, caption; card fallback equivalent (G-9). |
| 14 | Tokens | Data typography, row tones (G-10). |
| 15 | States | default, loading, empty, sorted, filtered, permission-limited. |
| 16 | Requirements | `REQ-990`, `REQ-992`, `REQ-1083`. |
| 17 | Screens | `SCR-014/019/031/035/040/047/053/062/066/072/092/096`. |
| 18 | Reuse restrictions | One grammar; no bespoke table style per screen. |
| 19 | Dependencies | `13A-BP-004`; MKT-065. |

### UI-CMP-023 — Filter row

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-023` |
| 2 | Name | Filter row |
| 3 | Purpose | Narrows a list visibly and reversibly. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Filter controls above the table; active-filter chips; clear action. |
| 6 | Content fields | Filter name, value, active state, result count. |
| 7 | Required/optional | Required when filtering exists. |
| 8 | Hierarchy | Above the table; active filters visible. |
| 9 | Data rules | Exact counts; no silent exclusion (G-5). |
| 10 | Interactions | Set/clear filter, apply. |
| 11 | Disabled | Invalid filter explains. |
| 12 | Responsive | Drawer on mobile; chips remain visible (G-8). |
| 13 | Accessibility | Labels; active filters announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, active-filter, invalid, clear. |
| 16 | Requirements | `REQ-991`. |
| 17 | Screens | Table screens. |
| 18 | Reuse restrictions | Not a search box substitute. |
| 19 | Dependencies | `13A-BP-004`. |

### UI-CMP-024 — Pagination

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-024` |
| 2 | Name | Pagination |
| 3 | Purpose | Moves through a large result set while reporting exact bounds. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Range label "0–N of M", previous/next, page position. |
| 6 | Content fields | Start, end, total, page, sort/filter state. |
| 7 | Required/optional | Required when results exceed one page. |
| 8 | Hierarchy | Below the table; exact count prominent. |
| 9 | Data rules | Exact totals; preserve filters/sort (G-5). |
| 10 | Interactions | Next/previous/page. |
| 11 | Disabled | First/last boundaries disabled with reason. |
| 12 | Responsive | Compact next/previous + count on mobile (G-8). |
| 13 | Accessibility | Navigation label; current page announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | first, middle, last, exact-count. |
| 16 | Requirements | `REQ-992`. |
| 17 | Screens | Paginated lists. |
| 18 | Reuse restrictions | No infinite scroll that hides the total. |
| 19 | Dependencies | MKT-065. |

### UI-CMP-025 — Saved view

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-025` |
| 2 | Name | Saved view |
| 3 | Purpose | Stores filter/sort state for repeated use. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | View name, dirty indicator, apply/save controls. |
| 6 | Content fields | Name, filter/sort state, owner, dirty flag. |
| 7 | Required/optional | Optional; required only where the table grammar offers it. |
| 8 | Hierarchy | Above the table, secondary to filters. |
| 9 | Data rules | Never widens visibility; invalid view explains (G-5). |
| 10 | Interactions | Apply, save, rename, delete. |
| 11 | Disabled | Invalid/dirty state explains. |
| 12 | Responsive | Select on mobile (G-8). |
| 13 | Accessibility | Labelled select/menu (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, dirty, invalid, permission-denied. |
| 16 | Requirements | `REQ-993`. |
| 17 | Screens | `SCR-019/031/040/047/062/066/072`. |
| 18 | Reuse restrictions | User-scoped only; never shared to bypass visibility. |
| 19 | Dependencies | TR-021. |

### UI-CMP-026 — Search and jump-to-object

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-026` |
| 2 | Name | Search and jump-to-object |
| 3 | Purpose | Jumps to a known object or screen without browsing. |
| 4 | Category | Display; **Navigation**; **Global** |
| 5 | Visual structure | Search field, typeahead results, object type/identity, denied state. |
| 6 | Content fields | Query, result type, identity, route, visibility state. |
| 7 | Required/optional | Required in shell; optional in local tables. |
| 8 | Hierarchy | Results below field; top result not auto-selected. |
| 9 | Data rules | No full-text corpus; denied objects do not reveal data (G-5). |
| 10 | Interactions | Type, select, jump. |
| 11 | Disabled | No-result/denied states explain. |
| 12 | Responsive | Full-screen sheet on mobile (G-8). |
| 13 | Accessibility | Combobox semantics; live result count (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, no-result, loading, denied-object. |
| 16 | Requirements | `REQ-994`, `REQ-1003`. |
| 17 | Screens | Shell; `SCR-010/018/053/072`. |
| 18 | Reuse restrictions | Jump only; never a promised content search. |
| 19 | Dependencies | `13A-OQ-005/009`. |

### UI-CMP-027 — Object reference link

| # | Field | Specification |
|---|---|---|
| 1 | ID | `UI-CMP-027` |
| 2 | Name | Object reference link |
| 3 | Purpose | Turns every object identifier into a stable, permission-aware link. |
| 4 | Category | Display; **Navigation**; **Global** |
| 5 | Visual structure | Inline link with object-type affordance; optional retired/denied marker. |
| 6 | Content fields | Object type, identity, canonical route, visibility state. |
| 7 | Required/optional | Required wherever an object is cited. |
| 8 | Hierarchy | Inline within prose/table; not styled as a button. |
| 9 | Data rules | Link text is the object name, not "click here"; no hidden metadata (G-5). |
| 10 | Interactions | Navigate; peek on focus/click (`OVL-05`). |
| 11 | Disabled | Denied object renders plain text with a reason class, not a dead link. |
| 12 | Responsive | Peek becomes tap sheet (G-8). |
| 13 | Accessibility | Link semantics; peek not required to reach the page (G-9). |
| 14 | Tokens | Link/visited tokens (G-10). |
| 15 | States | default, hover, focus-visible, visited, denied, retired. |
| 16 | Requirements | `REQ-995`. |
| 17 | Screens | Every screen citing an object. |
| 18 | Reuse restrictions | Never used for actions; use buttons. |
| 19 | Dependencies | `13A-PR-13`; D-209. |

### UI-CMP-028 — Object peek preview

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-028` |
| 2 | Name | Object peek preview |
| 3 | Purpose | Shows a small, visibility-safe preview of a linked object. |
| 4 | Category | Display; **Visibility**; overlay-adjacent |
| 5 | Visual structure | Popover/sheet with identity, type, public status and a full-view link. |
| 6 | Content fields | Identity, type, public state, permitted summary, route. |
| 7 | Required/optional | Optional enhancement; never the only source of a fact. |
| 8 | Hierarchy | Identity first; summary second. |
| 9 | Data rules | Only fields already visible; denied/suppressed state (G-5). |
| 10 | Interactions | Open full view; dismiss. |
| 11 | Disabled | Denied peek says restricted, no data. |
| 12 | Responsive | Hover popover → tap sheet (G-8). |
| 13 | Accessibility | `dialog`/tooltip semantics; dismissible; focus restored (G-9). |
| 14 | Tokens | Elevation/surface (G-10). |
| 15 | States | default, loading, denied, suppressed. |
| 16 | Requirements | `REQ-996`. |
| 17 | Screens | Every object-link list. |
| 18 | Reuse restrictions | Never the only place an action exists. |
| 19 | Dependencies | TR-021; D-215. |

### UI-CMP-029 — Detail section

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-029` |
| 2 | Name | Detail section |
| 3 | Purpose | Groups related detail under a stable heading within an object page. |
| 4 | Category | Display; **Global** |
| 5 | Visual structure | Heading, optional disclosure, content region, anchor. |
| 6 | Content fields | Heading, content, collapsed state, anchor. |
| 7 | Required/optional | Required: heading/content. Optional: collapse. |
| 8 | Hierarchy | Heading before content; collapse does not remove content from the page source. |
| 9 | Data rules | Inherits the screen's data rules (G-5). |
| 10 | Interactions | Collapse/expand, anchor link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Accordion on mobile (G-8). |
| 13 | Accessibility | Heading level, `aria-expanded` (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, collapsed, expanded, empty, provisional. |
| 16 | Requirements | `REQ-997`. |
| 17 | Screens | Object pages and detail records. |
| 18 | Reuse restrictions | Not a card substitute for statistics. |
| 19 | Dependencies | `13A-PR-02`. |

### UI-CMP-030 — Comparison panel

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-030` |
| 2 | Name | Comparison panel |
| 3 | Purpose | Compares visibility-legal values with sources rather than predictions. |
| 4 | Category | Display; **Data presentation** |
| 5 | Visual structure | Columns for sources, aligned metrics, difference rows, suppression states. |
| 6 | Content fields | Sources, turns, metrics, differences, suppression. |
| 7 | Required/optional | Required: at least two legal sources. |
| 8 | Hierarchy | Sources first; differences second; interpretation last. |
| 9 | Data rules | k=5 aware; no verdict; no dual-axis; sample counts (G-5). |
| 10 | Interactions | Change sources/turns within rules. |
| 11 | Disabled | Not-comparable state explains. |
| 12 | Responsive | Stacked comparison cards on mobile (G-8). |
| 13 | Accessibility | Table semantics for differences (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, partial, suppressed, not-comparable. |
| 16 | Requirements | `REQ-998`, `REQ-1058`. |
| 17 | Screens | `SCR-015/022/023/042/063/072`. |
| 18 | Reuse restrictions | Never predicts a verdict from a comparison. |
| 19 | Dependencies | `13A-DR-006/020`; D-027. |

## 4. Economic and political components — UI-CMP-031…UI-CMP-042

### UI-CMP-031 — Treasury summary

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-031` |
| 2 | Name | Treasury summary |
| 3 | Purpose | Presents available, reserved and current position as the treasury headline. |
| 4 | Category | Economic; **System-specific (B-04)** |
| 5 | Visual structure | Three labelled registers + current-position line + as-of turn. |
| 6 | Content fields | Available, reserved, total/current position, as-of turn, forecast link. |
| 7 | Required/optional | Required: all three figures. |
| 8 | Hierarchy | Available first; reserved second; total position third. |
| 9 | Data rules | No credit/overdraft; forecast distinct (G-5, D-050). |
| 10 | Interactions | Link to budget/report. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Three columns → stacked registers (G-8). |
| 13 | Accessibility | Each figure read with unit and role (G-9). |
| 14 | Tokens | Data typography, warning for shortfall (G-10). |
| 15 | States | default, zero, projected-negative, stale. |
| 16 | Requirements | `REQ-999`. |
| 17 | Screens | `SCR-029/030/031/057`. |
| 18 | Reuse restrictions | Treasury only; never for resource balances. |
| 19 | Dependencies | ECN-176/177; D-050. |

### UI-CMP-032 — Income & expenditure breakdown

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-032` |
| 2 | Name | Income & expenditure breakdown |
| 3 | Purpose | Separates income, recurring expense and one-time capex with net change. |
| 4 | Category | Economic; **System-specific (B-04)** |
| 5 | Visual structure | Signed rows grouped by type; net row; explanation links. |
| 6 | Content fields | Income lines, opex, capex, net, as-of, source. |
| 7 | Required/optional | Required: totals, net, units. |
| 8 | Hierarchy | Net first where the question is affordability; lines second. |
| 9 | Data rules | Capex excluded from operating income; forecast labelled (G-5). |
| 10 | Interactions | Drill to report. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Table → grouped cards (G-8). |
| 13 | Accessibility | Group labels, signed values announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, capex/opex split, forecast, incomplete. |
| 16 | Requirements | `REQ-1000`. |
| 17 | Screens | `SCR-029/030/031`. |
| 18 | Reuse restrictions | Never merges capex into opex. |
| 19 | Dependencies | D-051; ECN-097/098. |

### UI-CMP-033 — Total/reserved/available register

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-033` |
| 2 | Name | Total/reserved/available register |
| 3 | Purpose | The canonical three-figure balance for any resource or crown amount. |
| 4 | Category | Economic; **System-specific (B-04/B-07)** |
| 5 | Visual structure | Three aligned figures with labels, unit and capacity context. |
| 6 | Content fields | Total, reserved (with committed subset if any), available, unit, as-of. |
| 7 | Required/optional | Required: all three on every use. |
| 8 | Hierarchy | Available emphasized for spending; total for inventory. |
| 9 | Data rules | Sum of reservations ≤ total; no bare balance (G-5, MKT-053). |
| 10 | Interactions | Optional drill to ledger. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Three-inline → stacked with labels (G-8). |
| 13 | Accessibility | "Total X, reserved Y, available Z" phrase (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, reserved, available-zero, suppressed. |
| 16 | Requirements | `REQ-1001`, `REQ-1065`, `REQ-983`. |
| 17 | Screens | Every balance-bearing screen. |
| 18 | Reuse restrictions | Never split across pages or hidden in a tooltip. |
| 19 | Dependencies | MKT-053; TR-069; URB-066. |

### UI-CMP-034 — Capacity bar

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-034` |
| 2 | Name | Capacity bar |
| 3 | Purpose | Shows used versus total capacity with reserved and degraded segments. |
| 4 | Category | Economic; **System-specific (B-04/B-05)** |
| 5 | Visual structure | Labelled bar with used/free/reserved segments and total. |
| 6 | Content fields | Used, total, unit, reserved, state. |
| 7 | Required/optional | Required: used/total/unit. Optional: reserved. |
| 8 | Hierarchy | Used/total text first; bar second. |
| 9 | Data rules | Capacity is per-turn rate or DC, never a stored balance (G-5). |
| 10 | Interactions | Link to capacity detail. |
| 11 | Disabled | Full/derated/unmaintained explains. |
| 12 | Responsive | Bar scales; text survives (G-8). |
| 13 | Accessibility | Text equivalent of the bar (G-9). |
| 14 | Tokens | Success/warning/danger tones (G-10). |
| 15 | States | default, full, reserved, derated, unmaintained. |
| 16 | Requirements | `REQ-1002`. |
| 17 | Screens | `SCR-033/034/042/043/044/045`. |
| 18 | Reuse restrictions | Not for progress toward a reward. |
| 19 | Dependencies | ECN-042/120; URB-052. |

### UI-CMP-035 — Production chain

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-035` |
| 2 | Name | Production chain |
| 3 | Purpose | Presents one chain's inputs, outputs, costs, power, maintenance and blocking state. |
| 4 | Category | Economic; **System-specific (B-04/B-05)** |
| 5 | Visual structure | Chain header, state chip, input/output rows, cost/power/maintenance, reason. |
| 6 | Content fields | Chain, state, batches, inputs, expected output, variable cost, maintenance, power, bonus, reason. |
| 7 | Required/optional | Required: chain, state, key quantities. |
| 8 | Hierarchy | State and blocking reason first; quantities second. |
| 9 | Data rules | `UNMAINTAINED` named; forecasts labelled (G-5). |
| 10 | Interactions | Set policy, view power, build. |
| 11 | Disabled | Blocked reason visible. |
| 12 | Responsive | Table row → card (G-8). |
| 13 | Accessibility | State/reason announced (G-9). |
| 14 | Tokens | Warning/danger (G-10). |
| 15 | States | running, target, idle, unmaintained, power-short. |
| 16 | Requirements | `REQ-1004`. |
| 17 | Screens | `SCR-032/044`. |
| 18 | Reuse restrictions | One chain per instance. |
| 19 | Dependencies | URB-149; ECN-147. |

### UI-CMP-036 — Construction queue item

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-036` |
| 2 | Name | Construction queue item |
| 3 | Purpose | Represents one construction-class action and its slot/refund state. |
| 4 | Category | Economic; **System-specific (B-05)** |
| 5 | Visual structure | Target, cost, slot, availability turn, state, cancel/refund. |
| 6 | Content fields | Action, target, cost, slot, availability, state, refund terms. |
| 7 | Required/optional | Required: action/target/state. |
| 8 | Hierarchy | State first; cost/slot second; cancel third. |
| 9 | Data rules | One slot per city; refund 25% crowns only; no queue illusion (G-5). |
| 10 | Interactions | Cancel where permitted; view detail. |
| 11 | Disabled | Cancel disabled after resolution with reason. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | State/refund announced (G-9). |
| 14 | Tokens | Pending/success/error (G-10). |
| 15 | States | pending, resolving, cancelled, failed, complete. |
| 16 | Requirements | `REQ-1005`. |
| 17 | Screens | `SCR-042/043`. |
| 18 | Reuse restrictions | Cannot represent multiple queued items per city. |
| 19 | Dependencies | D-073/D-074; URB-064/148. |

### UI-CMP-037 — Research project card

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-037` |
| 2 | Name | Research project card |
| 3 | Purpose | Shows a technology or programme, its status, cost, prerequisite and effect. |
| 4 | Category | Economic; **System-specific (B-05)** |
| 5 | Visual structure | Name, branch, status chip, cost, prerequisite, effect, progress. |
| 6 | Content fields | Project, branch, status, RP/crown cost, prerequisite, effect, progress. |
| 7 | Required/optional | Required: name/status/cost/effect. |
| 8 | Hierarchy | Status first; cost/effect second. |
| 9 | Data rules | Status vocabulary exact; forecast completion labelled (G-5). |
| 10 | Interactions | Start, fund programme, view effect. |
| 11 | Disabled | Locked/prerequisite reason. |
| 12 | Responsive | Grid→cards (G-8). |
| 13 | Accessibility | Status text, cost units (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | locked, available, in-progress, complete, prerequisite-missing. |
| 16 | Requirements | `REQ-1006`, `REQ-914`. |
| 17 | Screens | `SCR-045`. |
| 18 | Reuse restrictions | One project; programmes distinct from technologies. |
| 19 | Dependencies | URB-102/150; D-076. |

### UI-CMP-038 — Approval & stability presentation

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-038` |
| 2 | Name | Approval & stability presentation |
| 3 | Purpose | Explains approval and stability through six supports and named terms. |
| 4 | Category | Political; **System-specific (B-06)** |
| 5 | Visual structure | Approval register, six support rows, stability register, cause drawer. |
| 6 | Content fields | Approval, six supports (weight/current/last/contribution), stability, threshold. |
| 7 | Required/optional | Required: approval, six supports, stability. |
| 8 | Hierarchy | Approval/stability first; supports second; terms progressive. |
| 9 | Data rules | No hidden aggregate; no invented bands (G-5, DMP-073). |
| 10 | Interactions | Drill per support (`OVL-04`). |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Table → support cards (G-8). |
| 13 | Accessibility | Weight/contribution announced (G-9). |
| 14 | Tokens | Warning/danger bands (G-10). |
| 15 | States | default, six-supports, warning, crisis, recovery. |
| 16 | Requirements | `REQ-1009`, `REQ-892`. |
| 17 | Screens | `SCR-021/023/028`. |
| 18 | Reuse restrictions | B-06 only; never used as a generic sentiment widget. |
| 19 | Dependencies | DMP-073; F-PD-004…009. |

### UI-CMP-039 — Political state banner

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-039` |
| 2 | Name | Political state banner |
| 3 | Purpose | Shows the six-state leadership state and its consequences on every political screen. |
| 4 | Category | Political; **System-specific (B-06)**; **Global on political surfaces** |
| 5 | Visual structure | Tone banner with state label, cause, end turn, locked/unlocked summary. |
| 6 | Content fields | `NORMAL`/`ELECTORAL`/`SUCCESSION`/`TRANSITION`/`CRISIS`/`RECOVERY`, cause, end turn, locks. |
| 7 | Required/optional | Required on every political and consequence-bearing screen. |
| 8 | Hierarchy | Above content when the state changes permissions. |
| 9 | Data rules | Exact six states; never a ban/suspension framing (G-5, DMP-268). |
| 10 | Interactions | Link to the owning politics screen. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Full width; locks collapse (G-8). |
| 13 | Accessibility | State/cause announced; not colour-only (G-9). |
| 14 | Tokens | Six defined tone pairs (G-10). |
| 15 | States | six states + explanatory transition/crisis variants. |
| 16 | Requirements | `REQ-1010`, `REQ-890`. |
| 17 | Screens | `SCR-021`…`SCR-028`; block surfaces. |
| 18 | Reuse restrictions | Never reused for non-political status. |
| 19 | Dependencies | DMP-128/256/268. |

### UI-CMP-040 — Policy control

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-040` |
| 2 | Name | Policy control |
| 3 | Purpose | Changes one policy axis with effect, cost and cooldown on the control. |
| 4 | Category | Political; **System-specific (B-06)** |
| 5 | Visual structure | Current setting, options, effect preview, cooldown badge, confirm. |
| 6 | Content fields | Axis, current, proposed, effect, cost, next eligible turn. |
| 7 | Required/optional | Required: axis/current/options/cooldown. |
| 8 | Hierarchy | Current first; effect second; cooldown on control. |
| 9 | Data rules | One change per axis per 12 turns; `T+1` effect (G-5, D-087). |
| 10 | Interactions | Select, confirm, cancel. |
| 11 | Disabled | Cooldown/state reason visible. |
| 12 | Responsive | Stacked; cooldown badge remains adjacent (G-8). |
| 13 | Accessibility | Current/proposed/cooldown announced (G-9). |
| 14 | Tokens | Pending/locked tones (G-10). |
| 15 | States | available, cooldown, blocked-by-state, confirmation. |
| 16 | Requirements | `REQ-1011`, `REQ-893`. |
| 17 | Screens | `SCR-024`. |
| 18 | Reuse restrictions | B-06 axes only. |
| 19 | Dependencies | D-087; DMP-101/102. |

### UI-CMP-041 — Election date presentation

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-041` |
| 2 | Name | Election date presentation |
| 3 | Purpose | Shows campaign dates anchored on `campaign_open_turn` and their state. |
| 4 | Category | Political; **System-specific (B-06)** |
| 5 | Visual structure | Date ladder with anchor, offsets, state and end turn. |
| 6 | Content fields | `campaign_open_turn`, `T−24`/`T−12`/`T−2`, resolution turn, state. |
| 7 | Required/optional | Required: anchor, dates, state. |
| 8 | Hierarchy | Current/next date first. |
| 9 | Data rules | On-time values labelled; delays are states (G-5). |
| 10 | Interactions | Link to election/campaign. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Horizontal ladder → stacked (G-8). |
| 13 | Accessibility | Dates read with turn and UTC (G-9). |
| 14 | Tokens | Pending/success (G-10). |
| 15 | States | scheduled, open, closed, delayed, resolved. |
| 16 | Requirements | `REQ-1012`. |
| 17 | Screens | `SCR-025/027/028`. |
| 18 | Reuse restrictions | Not a wall-clock countdown. |
| 19 | Dependencies | D-106/D-107; DMP-178. |

### UI-CMP-042 — Campaign action control

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-042` |
| 2 | Name | Campaign action control |
| 3 | Purpose | Runs one of the three campaign actions with its exact cost/points and charge-once state. |
| 4 | Category | Political; **System-specific (B-06)** |
| 5 | Visual structure | Action card, cost/points, limit, effect, charged state, confirm. |
| 6 | Content fields | Action type, cost, points/effect, remaining uses, charged state. |
| 7 | Required/optional | Required: type, cost, effect, limit. |
| 8 | Hierarchy | Effect first; cost/limit second. |
| 9 | Data rules | Exactly three types; charge-once; no reservation (G-5, D-094). |
| 10 | Interactions | Allocate/submit; confirm. |
| 11 | Disabled | State/limit reason visible. |
| 12 | Responsive | Card→stepped sheet (G-8). |
| 13 | Accessibility | Points/cost announced (G-9). |
| 14 | Tokens | Pending/success (G-10). |
| 15 | States | available, charged, blocked-by-state, limit-reached. |
| 16 | Requirements | `REQ-1018`, `REQ-895`. |
| 17 | Screens | `SCR-026`. |
| 18 | Reuse restrictions | No fourth action; no retroactive edit. |
| 19 | Dependencies | DMP-189/193. |

## 5. Diplomacy and alliance components — UI-CMP-043…UI-CMP-053

### UI-CMP-043 — Diplomatic relationship indicator

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-043` |
| 2 | Name | Diplomatic relationship indicator |
| 3 | Purpose | Shows a posture as a labelled state with glyph and tone. |
| 4 | Category | Diplomacy; **System-specific (B-08)** |
| 5 | Visual structure | Glyph + posture label + direction. |
| 6 | Content fields | Posture (`FRIENDLY`/`NEUTRAL`/`TENSE`/`HOSTILE`), direction. |
| 7 | Required/optional | Required: posture and direction. |
| 8 | Hierarchy | Posture first; direction adjacent. |
| 9 | Data rules | Not war, not a score; no hue-only (G-5). |
| 10 | Interactions | Link to pair screen. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Label survives icon collapse (G-8). |
| 13 | Accessibility | Text label is the accessible name (G-9). |
| 14 | Tokens | Four posture tones (G-10). |
| 15 | States | friendly, neutral, tense, hostile, unknown. |
| 16 | Requirements | `REQ-1019`. |
| 17 | Screens | `SCR-047/048/053/058`, profile. |
| 18 | Reuse restrictions | Never used as a reputation score. |
| 19 | Dependencies | DIP-023/024. |

### UI-CMP-044 — Directional relationship presentation

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-044` |
| 2 | Name | Directional relationship presentation |
| 3 | Purpose | Shows A→B and B→A independently side by side. |
| 4 | Category | Diplomacy; **System-specific (B-08)** |
| 5 | Visual structure | Two labelled direction columns/cards. |
| 6 | Content fields | Holder nation, posture, embargo state. |
| 7 | Required/optional | Required: both directions where both exist. |
| 8 | Hierarchy | Direction labels first. |
| 9 | Data rules | Never symmetric; embargo distinct (G-5). |
| 10 | Interactions | Link to pair. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Two cards → stacked (G-8). |
| 13 | Accessibility | Each direction announced with holder (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | both-directions, one-direction, embargo, suppressed. |
| 16 | Requirements | `REQ-1020`, `REQ-1067`. |
| 17 | Screens | `SCR-047/048`. |
| 18 | Reuse restrictions | Not for alliance treaty coverage (use `UI-CMP-045`). |
| 19 | Dependencies | DIP-023/024; DP-A01. |

### UI-CMP-045 — Treaty status

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-045` |
| 2 | Name | Treaty status |
| 3 | Purpose | Shows the exact agreement type and lifecycle state. |
| 4 | Category | Diplomacy; **System-specific (B-08/B-09)** |
| 5 | Visual structure | Type token, state chip, activation/expiry, parties. |
| 6 | Content fields | Type (`DP-T01`…`T03`, `DP-A01`, `AT-T01`…`T05`), state, dates, parties. |
| 7 | Required/optional | Required: type/state/parties. |
| 8 | Hierarchy | State first; type/date second. |
| 9 | Data rules | No stale active badge; record-only labelled (G-5). |
| 10 | Interactions | Link to agreement. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Chip + dates stack (G-8). |
| 13 | Accessibility | State/type announced (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | proposed, pending, accepted, active, expiring, terminated, expired, record-only. |
| 16 | Requirements | `REQ-1021`. |
| 17 | Screens | `SCR-047/050/051/052/058`. |
| 18 | Reuse restrictions | Nation and alliance treaties remain distinct types. |
| 19 | Dependencies | DP-T01…T03; AT-E00/E01. |

### UI-CMP-046 — Proposal summary

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-046` |
| 2 | Name | Proposal summary |
| 3 | Purpose | Summarises a pending proposal for a party without exposing it to third parties. |
| 4 | Category | Diplomacy; **System-specific (B-08/B-09)** |
| 5 | Visual structure | Counterparty, type, terms summary, created/expiry, state. |
| 6 | Content fields | Counterparty, type, terms, created/expiry turn, state. |
| 7 | Required/optional | Required: counterparty/type/state. |
| 8 | Hierarchy | State first; terms second. |
| 9 | Data rules | Parties-only while pending (G-5, D-030). |
| 10 | Interactions | Open, counter, withdraw. |
| 11 | Disabled | Non-cancellable explains. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | Parties/state announced (G-9). |
| 14 | Tokens | Pending tones (G-10). |
| 15 | States | pending, countered, accepted, rejected, withdrawn, expired. |
| 16 | Requirements | `REQ-1022`. |
| 17 | Screens | `SCR-014/047/049/050`. |
| 18 | Reuse restrictions | Never used for public listing of pending terms. |
| 19 | Dependencies | D-030; DIP-114. |

### UI-CMP-047 — Negotiation panel

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-047` |
| 2 | Name | Negotiation panel |
| 3 | Purpose | Presents the confirmation fields and counter/withdraw paths for a negotiation. |
| 4 | Category | Diplomacy; **Interaction control** |
| 5 | Visual structure | Ten-field confirmation list, cancel path, counter path, confirm. |
| 6 | Content fields | Authorization, acting/affected nations, obligations, duration, reversibility, consent, limit, not-does. |
| 7 | Required/optional | Required: all ten fields. |
| 8 | Hierarchy | What is authorized first; what it does not do last. |
| 9 | Data rules | Exact terms; no preselected confirm (G-5). |
| 10 | Interactions | Confirm/counter/withdraw/cancel. |
| 11 | Disabled | Limit/state reason. |
| 12 | Responsive | Full-screen confirmation on mobile (G-8). |
| 13 | Accessibility | Ordered fields; cancel always present (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, counter, withdraw, blocked, confirmation. |
| 16 | Requirements | `REQ-1023`. |
| 17 | Screens | `SCR-049/067`. |
| 18 | Reuse restrictions | Its field order may not be abbreviated for mobile. |
| 19 | Dependencies | 08C §12.3. |

### UI-CMP-048 — Publication status

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-048` |
| 2 | Name | Publication status |
| 3 | Purpose | Shows what is private, when it becomes public, and the public field set. |
| 4 | Category | Diplomacy; **Visibility** |
| 5 | Visual structure | State matrix + timeline + public field list. |
| 6 | Content fields | State, visibility by party/third party/public, activation moment, fields. |
| 7 | Required/optional | Required: state and visibility. |
| 8 | Hierarchy | Current state first; future moment second. |
| 9 | Data rules | No public pending terms; k=5 aggregates (G-5). |
| 10 | Interactions | Link to agreement. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Matrix → stacked list (G-8). |
| 13 | Accessibility | Visibility announced per audience (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | pending-private, accepted-private, active-public, record-only. |
| 16 | Requirements | `REQ-1024`, `REQ-1068`. |
| 17 | Screens | `SCR-050/051/058`. |
| 18 | Reuse restrictions | Not for privacy-class settings (use `UI-CMP-019`). |
| 19 | Dependencies | DIP-108…113; D-030. |

### UI-CMP-049 — Alliance membership row

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-049` |
| 2 | Name | Alliance membership row |
| 3 | Purpose | Shows a member's identity and role within disclosure rules. |
| 4 | Category | Alliance; **System-specific (B-09)** |
| 5 | Visual structure | Member identity, role, membership state, non-covered marker. |
| 6 | Content fields | Nation identity, role, state, coverage. |
| 7 | Required/optional | Required: identity/role where permitted. |
| 8 | Hierarchy | Identity first; role second. |
| 9 | Data rules | Applicant privacy; no treasury/military data (G-5). |
| 10 | Interactions | Link to profile; role action where permitted. |
| 11 | Disabled | Role action denied explains. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | Role/state announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | member, applicant, non-covered, officer, former. |
| 16 | Requirements | `REQ-1025`. |
| 17 | Screens | `SCR-053/054/055`. |
| 18 | Reuse restrictions | Never carries war/OP data. |
| 19 | Dependencies | ALL-086; D-140. |

### UI-CMP-050 — Applicant status

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-050` |
| 2 | Name | Applicant status |
| 3 | Purpose | Shows an application's state to the permitted administration only. |
| 4 | Category | Alliance; **System-specific (B-09)** |
| 5 | Visual structure | Applicant identity, status, age/expiry, action. |
| 6 | Content fields | Applicant, status, submitted turn, expiry, decision. |
| 7 | Required/optional | Required: applicant/status. |
| 8 | Hierarchy | Status first; decision second. |
| 9 | Data rules | Admin-only; no external hop (G-5). |
| 10 | Interactions | Admit/decline. |
| 11 | Disabled | Permission/expiry reason. |
| 12 | Responsive | Card list (G-8). |
| 13 | Accessibility | Status announced (G-9). |
| 14 | Tokens | Pending/success (G-10). |
| 15 | States | pending, admitted, declined, expired, withdrawn. |
| 16 | Requirements | `REQ-1026`. |
| 17 | Screens | `SCR-054`. |
| 18 | Reuse restrictions | Never visible to ordinary members or outsiders. |
| 19 | Dependencies | ALL-080…086. |

### UI-CMP-051 — Alliance financial summary

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-051` |
| 2 | Name | Alliance financial summary |
| 3 | Purpose | Shows the four ARL categories and the accounting identity. |
| 4 | Category | Alliance; **System-specific (B-09)** |
| 5 | Visual structure | Four labelled registers + identity line + unavailable-purpose note. |
| 6 | Content fields | `RECEIVED`, `AVAILABLE`, `RESERVED`, `EXPENDED`, purposes. |
| 7 | Required/optional | Required: all four. |
| 8 | Hierarchy | Available first; receipts second. |
| 9 | Data rules | `AVAILABLE = RECEIVED − RESERVED − EXPENDED`; no ownership claim (G-5). |
| 10 | Interactions | Receipt drill. |
| 11 | Disabled | No spend control while no purpose is approved. |
| 12 | Responsive | Four → stacked (G-8). |
| 13 | Accessibility | Identity announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | received, available, reserved, expended, zero-fallback. |
| 16 | Requirements | `REQ-1027`. |
| 17 | Screens | `SCR-056/057`. |
| 18 | Reuse restrictions | Not a national treasury; no withdrawal UI. |
| 19 | Dependencies | ALL-187; D-141. |

### UI-CMP-052 — Alliance receipt

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-052` |
| 2 | Name | Alliance receipt |
| 3 | Purpose | Presents an immutable receipt for a tax/donation/transfer event. |
| 4 | Category | Alliance; **System-specific (B-09)** |
| 5 | Visual structure | Receipt header, parties, asset/amount, turn, references. |
| 6 | Content fields | Donor/source, receiving alliance, asset, amount, turn, `transfer_id`, idempotency. |
| 7 | Required/optional | Required: all fields. |
| 8 | Hierarchy | Amount/asset first; references second. |
| 9 | Data rules | Immutable; correction appends; never hidden (G-5). |
| 10 | Interactions | Link to related ledger. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Card (G-8). |
| 13 | Accessibility | All fields labelled (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | issued, immutable, corrected-by-append. |
| 16 | Requirements | `REQ-1028`. |
| 17 | Screens | `SCR-056/057`. |
| 18 | Reuse restrictions | Never editable. |
| 19 | Dependencies | ALL-193; ECN-213. |

### UI-CMP-053 — Restriction explanation

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-053` |
| 2 | Name | Restriction explanation |
| 3 | Purpose | Explains why an action is unavailable without accusation or private data. |
| 4 | Category | Alliance/support; **Permissions** |
| 5 | Visual structure | Reason label, scope, rule link, recourse link. |
| 6 | Content fields | Restriction kind, scope, reason class, rule anchor, appeal/correction route. |
| 7 | Required/optional | Required: kind and reason class. |
| 8 | Hierarchy | Reason before recourse. |
| 9 | Data rules | No another-player data, threshold, method or `SEC` (G-5). |
| 10 | Interactions | Rule link; appeal link where applicable. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Inline message → sheet (G-8). |
| 13 | Accessibility | Described-by on the disabled control (G-9). |
| 14 | Tokens | Locked/denied tone (G-10). |
| 15 | States | role-denied, pair-restricted, NAP-block, same-alliance-block, state-block. |
| 16 | Requirements | `REQ-1029`. |
| 17 | Screens | `SCR-048/055/058/084/086`. |
| 18 | Reuse restrictions | Never a generic "not allowed" with no reason. |
| 19 | Dependencies | NET-023/050; WAR-149; DMP-268. |

## 6. Warfare components — UI-CMP-054…UI-CMP-062

### UI-CMP-054 — War summary

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-054` |
| 2 | Name | War summary |
| 3 | Purpose | Summarises a war's belligerents and public state. |
| 4 | Category | Warfare; **System-specific (B-10)** |
| 5 | Visual structure | Belligerents, state, duration, permitted facts. |
| 6 | Content fields | Aggressor/defender, state, declared turn, public facts. |
| 7 | Required/optional | Required: belligerents/state. |
| 8 | Hierarchy | State first; belligerents second. |
| 9 | Data rules | No exact strength/OP/private operation (G-5, WAR-148). |
| 10 | Interactions | Link to war detail. |
| 11 | Disabled | Restricted detail explains. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | State/belligerents announced (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | declared, active, interrupted, settled, surrendered. |
| 16 | Requirements | `REQ-1030`. |
| 17 | Screens | `SCR-059/061/062/063`. |
| 18 | Reuse restrictions | Never shows another nation's private state. |
| 19 | Dependencies | WAR-085…088. |

### UI-CMP-055 — War status strip

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-055` |
| 2 | Name | War status strip |
| 3 | Purpose | Shows lifecycle state, protection recheck and settlement availability. |
| 4 | Category | Warfare; **System-specific (B-10)** |
| 5 | Visual structure | State chip row with protection/settlement markers. |
| 6 | Content fields | WAR-125 state, protection state, settlement state. |
| 7 | Required/optional | Required: lifecycle state. |
| 8 | Hierarchy | Lifecycle first. |
| 9 | Data rules | Exact WAR-125 vocabulary; no invented state (G-5). |
| 10 | Interactions | Link to settlement/board. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Chips wrap (G-8). |
| 13 | Accessibility | State announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | each WAR-125 state + protection. |
| 16 | Requirements | `REQ-1031`. |
| 17 | Screens | `SCR-061/063`. |
| 18 | Reuse restrictions | War only. |
| 19 | Dependencies | WAR-125; WAR-115…117. |

### UI-CMP-056 — Operations summary

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-056` |
| 2 | Name | Operations summary |
| 3 | Purpose | Lists this nation's authorized operations and their reservation/execution states. |
| 4 | Category | Warfare; **System-specific (B-10)**; **Role-restricted** |
| 5 | Visual structure | Operation rows with type, cost, state, reason. |
| 6 | Content fields | Operation, target, OP/resource cost, state, failure factor. |
| 7 | Required/optional | Required: operation/state. |
| 8 | Hierarchy | State/reason first; cost second. |
| 9 | Data rules | Owner-only; exact own data; no other nation (G-5). |
| 10 | Interactions | View battle; cancel only where permitted. |
| 11 | Disabled | Blocked reason. |
| 12 | Responsive | Table→cards (G-8). |
| 13 | Accessibility | State announced (G-9). |
| 14 | Tokens | Pending/danger (G-10). |
| 15 | States | default, reserved, executing, failed, released. |
| 16 | Requirements | `REQ-1032`. |
| 17 | Screens | `SCR-061`. |
| 18 | Reuse restrictions | Never rendered outside the owner's board. |
| 19 | Dependencies | WAR-039; B10-C20. |

### UI-CMP-057 — OP balance & reservation

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-057` |
| 2 | Name | OP balance & reservation |
| 3 | Purpose | Shows the persistent national OP pool, cap, regeneration, carry and reservations. |
| 4 | Category | Warfare; **Data presentation**; **Role-restricted** |
| 5 | Visual structure | Balance/cap, regeneration marker, reserved, carry state. |
| 6 | Content fields | Balance, cap, reserved, regeneration, carry, as-of turn. |
| 7 | Required/optional | Required: balance/cap/reserved. |
| 8 | Hierarchy | Available OP first; reserved second. |
| 9 | Data rules | One national pool; +1 at P3.7; no alliance/per-war pool (G-5, D-015). |
| 10 | Interactions | Link to operations. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Compact on mobile (G-8). |
| 13 | Accessibility | "X of Y OP available" phrase (G-9). |
| 14 | Tokens | Pending tone for reserved (G-10). |
| 15 | States | default, capped, reserved, regenerated-zero, spend. |
| 16 | Requirements | `REQ-1033`. |
| 17 | Screens | `SCR-059/061`. |
| 18 | Reuse restrictions | Never show another nation's OP or an Alliance pool. |
| 19 | Dependencies | D-015 as 10B-C3; WAR-039/161. |

### UI-CMP-058 — Threat & odds band

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-058` |
| 2 | Name | Threat and odds band |
| 3 | Purpose | Discloses opponent strength only as one of four bands. |
| 4 | Category | Warfare; **Data presentation** |
| 5 | Visual structure | Band label + glyph + short meaning; no numeric ratio. |
| 6 | Content fields | Band (`LOW`/`MODERATE`/`HIGH`/`SEVERE`), meaning. |
| 7 | Required/optional | Required: band. Optional: meaning disclosure. |
| 8 | Hierarchy | Band first. |
| 9 | Data rules | Four bands only; never exact ratio/probability (G-5, WAR-086). |
| 10 | Interactions | Explain-band disclosure. |
| 11 | Disabled | Unknown state explains. |
| 12 | Responsive | Label survives (G-8). |
| 13 | Accessibility | Band read as text, not hue (G-9). |
| 14 | Tokens | Four band tones + glyphs (G-10). |
| 15 | States | low, moderate, high, severe, unknown. |
| 16 | Requirements | `REQ-1034`, `REQ-1074`. |
| 17 | Screens | `SCR-061/063`. |
| 18 | Reuse restrictions | Never used for non-war uncertainty. |
| 19 | Dependencies | WAR-085…088. |

### UI-CMP-059 — Battle record

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-059` |
| 2 | Name | Battle record |
| 3 | Purpose | Presents the WAR-088 fields to a participant and a public summary otherwise. |
| 4 | Category | Warfare; **System-specific (B-10)** |
| 5 | Visual structure | Record table with participant fields; public-summary variant. |
| 6 | Content fields | Battle id/turn/type, engaged strength, readiness, counters, powers, ratio, fortune, tier, losses, progress, reason. |
| 7 | Required/optional | Required: permitted subset per viewer. |
| 8 | Hierarchy | Outcome/tier first; fields second. |
| 9 | Data rules | Field-filtered; no exact opponent strength public (G-5). |
| 10 | Interactions | Link to war/board. |
| 11 | Disabled | Restricted fields absent/labelled. |
| 12 | Responsive | Table→cards (G-8). |
| 13 | Accessibility | Field labels and units (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, public-summary, participant-detail, suppressed. |
| 16 | Requirements | `REQ-1035`, `REQ-1075`. |
| 17 | Screens | `SCR-061/064/065`. |
| 18 | Reuse restrictions | Not from P&W layout memory (`13A-SRC-034`). |
| 19 | Dependencies | WAR-088; WAR-109k. |

### UI-CMP-060 — Battle outcome

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-060` |
| 2 | Name | Battle outcome |
| 3 | Purpose | Shows the outcome and its settlement consequence. |
| 4 | Category | Warfare; **System-specific (B-10)** |
| 5 | Visual structure | Outcome label + reason + consequence link. |
| 6 | Content fields | Win/loss/stalemate/interrupted/voided, reason, consequence. |
| 7 | Required/optional | Required: outcome/reason. |
| 8 | Hierarchy | Outcome first. |
| 9 | Data rules | No implied result before settlement (G-5). |
| 10 | Interactions | Link to settlement. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Label + reason stack (G-8). |
| 13 | Accessibility | Outcome announced (G-9). |
| 14 | Tokens | Success/danger/neutral (G-10). |
| 15 | States | win, loss, stalemate, interrupted, voided. |
| 16 | Requirements | `REQ-1036`. |
| 17 | Screens | `SCR-064/065`. |
| 18 | Reuse restrictions | Not for election/objective outcomes. |
| 19 | Dependencies | WAR-088; TR-043. |

### UI-CMP-061 — Military history

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-061` |
| 2 | Name | Military history |
| 3 | Purpose | Presents permanent war records with retention and visibility labels. |
| 4 | Category | Warfare; **System-specific (B-10/B-11)** |
| 5 | Visual structure | War/battle rows with date, outcome, class. |
| 6 | Content fields | War, turn, outcome, settlement, class, retention. |
| 7 | Required/optional | Required: war/turn/outcome. |
| 8 | Hierarchy | Date and outcome first. |
| 9 | Data rules | Class-P permanent; public/private split (G-5). |
| 10 | Interactions | Open record. |
| 11 | Disabled | Restricted records labelled. |
| 12 | Responsive | Table→cards (G-8). |
| 13 | Accessibility | Dates/classes announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, retention-bound, restricted. |
| 16 | Requirements | `REQ-1038`. |
| 17 | Screens | `SCR-066`. |
| 18 | Reuse restrictions | No deletion. |
| 19 | Dependencies | D-026. |

### UI-CMP-062 — Nation-owner operation controls

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-062` |
| 2 | Name | Nation-owner operation controls |
| 3 | Purpose | Renders the authorized military controls only for the owner's own nation. |
| 4 | Category | Warfare; **Permissions**; **Role-restricted** |
| 5 | Visual structure | Grouped controls with OP cost, supply, readiness effect, confirmation. |
| 6 | Content fields | Operation, target, OP/resource cost, effect, block reason, confirmation. |
| 7 | Required/optional | Required: operation and cost/effect. |
| 8 | Hierarchy | Cost/effect before confirm; block reason adjacent. |
| 9 | Data rules | Owner-only; no delegation; no Alliance path (G-5, WAR-161). |
| 10 | Interactions | Declare/operate/surrender where rules allow; confirm. |
| 11 | Disabled | Protection/NAP/same-alliance/OP/supply reason. |
| 12 | Responsive | Sticky action region; full-screen confirmation (G-8). |
| 13 | Accessibility | Each control labelled; destructive separate (G-9). |
| 14 | Tokens | Danger for irreversible (G-10). |
| 15 | States | default, disabled+reason, confirmation, executing, released. |
| 16 | Requirements | `REQ-1039`, `REQ-1073`. |
| 17 | Screens | `SCR-061` only. |
| 18 | Reuse restrictions | **Never** in the Alliance interface; never for another nation. |
| 19 | Dependencies | WAR-148/161; REQ-589…591; AX-18; WAR-152. |

## 7. World and notification components — UI-CMP-063…UI-CMP-073

### UI-CMP-063 — Event card

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-063` |
| 2 | Name | Event card |
| 3 | Purpose | Presents a registered event's class, state and consequence link. |
| 4 | Category | World; **System-specific (B-11)** |
| 5 | Visual structure | Event title, class, state, duration, eligibility, link. |
| 6 | Content fields | Event, class, state, duration, eligibility, consequence. |
| 7 | Required/optional | Required: event/class/state. |
| 8 | Hierarchy | State first; consequence second. |
| 9 | Data rules | Closed catalogue; no invented event/effect (G-5). |
| 10 | Interactions | Open detail. |
| 11 | Disabled | Ineligible state explains. |
| 12 | Responsive | Grid→cards (G-8). |
| 13 | Accessibility | Class/state announced (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | scheduled, active, resolved, expired, suppressed. |
| 16 | Requirements | `REQ-1040`. |
| 17 | Screens | `SCR-013/069/070`. |
| 18 | Reuse restrictions | Not for player-created notices. |
| 19 | Dependencies | WEP-040/179. |

### UI-CMP-064 — Event consequence presentation

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-064` |
| 2 | Name | Event consequence presentation |
| 3 | Purpose | Pairs cause/hazard with the registered effect and affected quantity. |
| 4 | Category | World; **Data presentation** |
| 5 | Visual structure | Cause column, arrow, consequence column, affected quantity. |
| 6 | Content fields | Cause, effect, affected state/quantity, mitigation, source. |
| 7 | Required/optional | Required: cause/effect/source. |
| 8 | Hierarchy | Cause→effect first; mitigation second. |
| 9 | Data rules | No effect without source; no hidden modifier (G-5). |
| 10 | Interactions | Source link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Two columns → stacked (G-8). |
| 13 | Accessibility | Pair read as cause then effect (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | cause, effect, mitigation, historical. |
| 16 | Requirements | `REQ-1041`, `REQ-1071`. |
| 17 | Screens | `SCR-070`. |
| 18 | Reuse restrictions | B-11 events only. |
| 19 | Dependencies | WEP-179/619. |

### UI-CMP-065 — Objective card

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-065` |
| 2 | Name | Objective card |
| 3 | Purpose | Presents an objective's category, progress, optionality and dismissal. |
| 4 | Category | World; **System-specific (B-11)** |
| 5 | Visual structure | Category, title, progress, tiered credit, accept/dismiss. |
| 6 | Content fields | Category, condition reference, progress, optional, reward class. |
| 7 | Required/optional | Required: category/condition/progress. |
| 8 | Hierarchy | Progress first; reward second. |
| 9 | Data rules | No presence/membership/spend/aggression requirement (G-5). |
| 10 | Interactions | Accept/dismiss/open condition. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Grid→cards (G-8). |
| 13 | Accessibility | Progress and optionality announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | available, accepted, progress, completed, deferred, expired. |
| 16 | Requirements | `REQ-1042`. |
| 17 | Screens | `SCR-009/071`. |
| 18 | Reuse restrictions | No objective created by UI. |
| 19 | Dependencies | WEP-203…215; D-147. |

### UI-CMP-066 — Achievement card

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-066` |
| 2 | Name | Achievement card |
| 3 | Purpose | Presents an achievement and its reward class/state. |
| 4 | Category | World; **System-specific (B-11)** |
| 5 | Visual structure | Achievement name, class, state, grant turn. |
| 6 | Content fields | Achievement, reward class, state, grant turn. |
| 7 | Required/optional | Required: name/state. |
| 8 | Hierarchy | State first; class second. |
| 9 | Data rules | No another nation's reward (G-5). |
| 10 | Interactions | Open reward record. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Grid→cards (G-8). |
| 13 | Accessibility | State announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | locked, earned, historical, deferred-claim. |
| 16 | Requirements | `REQ-1043`. |
| 17 | Screens | `SCR-073/075`. |
| 18 | Reuse restrictions | No fabricated achievement. |
| 19 | Dependencies | WEP-499/663. |

### UI-CMP-067 — Ranking row

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-067` |
| 2 | Name | Ranking row |
| 3 | Purpose | Presents a nation's position/value in a named standing. |
| 4 | Category | World; **Data presentation** |
| 5 | Visual structure | Position/percentile, nation, value, denominator context, state. |
| 6 | Content fields | Position, nation, value, denominator, eligibility, state. |
| 7 | Required/optional | Required: nation/value/position. |
| 8 | Hierarchy | Nation first; value/position second. |
| 9 | Data rules | Denominator required; no live rank (G-5). |
| 10 | Interactions | Open profile. |
| 11 | Disabled | Ineligible state explains. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | Position/value/denominator announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | ranked, tied, ineligible, suppressed, historical. |
| 16 | Requirements | `REQ-1044`. |
| 17 | Screens | `SCR-072/010`. |
| 18 | Reuse restrictions | Never a composite headline. |
| 19 | Dependencies | WEP-324/325. |

### UI-CMP-068 — Ranking summary

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-068` |
| 2 | Name | Ranking summary |
| 3 | Purpose | States the denominator, eligibility, window and compute/publish turns. |
| 4 | Category | World; **Data presentation** |
| 5 | Visual structure | Four labelled facts + computation turn. |
| 6 | Content fields | Population, eligibility set, window, computed/published turn. |
| 7 | Required/optional | Required: all four. |
| 8 | Hierarchy | Denominator first. |
| 9 | Data rules | No display without denominator (G-5). |
| 10 | Interactions | Rule link. |
| 11 | Disabled | Empty state explains. |
| 12 | Responsive | Facts stack (G-8). |
| 13 | Accessibility | Facts announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | denominator-window, no-live, empty. |
| 16 | Requirements | `REQ-1045`, `REQ-1069`, `REQ-1070`. |
| 17 | Screens | `SCR-072`. |
| 18 | Reuse restrictions | Not optional decoration; it is part of the standing. |
| 19 | Dependencies | WEP-324/359. |

### UI-CMP-069 — Notification item

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-069` |
| 2 | Name | Notification item |
| 3 | Purpose | Presents one existing notification event with source and tier. |
| 4 | Category | World; **System-specific (all notification matrices)** |
| 5 | Visual structure | Tier glyph/tone, source, subject, time, object link, mute state. |
| 6 | Content fields | Event source, tier, subject, turn/UTC, object, mutable. |
| 7 | Required/optional | Required: source/tier/subject/time. |
| 8 | Hierarchy | Tier/source first; link second. |
| 9 | Data rules | Presentation only; no new event; non-opt-out marked (G-5). |
| 10 | Interactions | Open, mute where permitted, mark read. |
| 11 | Disabled | Mute disabled for non-opt-out with reason. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | Tier/source announced (G-9). |
| 14 | Tokens | Tier tones (G-10). |
| 15 | States | informational, pending, warning, danger, muted, non-opt-out. |
| 16 | Requirements | `REQ-1046`. |
| 17 | Screens | `SCR-013/019/014`. |
| 18 | Reuse restrictions | Never paraphrases into a different fact. |
| 19 | Dependencies | REQ-731; DIP-114/116. |

### UI-CMP-070 — Pending-action item

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-070` |
| 2 | Name | Pending-action item |
| 3 | Purpose | Presents one pending action with due boundary and permitted paths. |
| 4 | Category | World; **Interaction control** |
| 5 | Visual structure | Owning system, action, state, due turn, act/cancel. |
| 6 | Content fields | System, action, counterparty, due boundary, state, cancellable. |
| 7 | Required/optional | Required: system/action/state/due. |
| 8 | Hierarchy | Due boundary first; action second. |
| 9 | Data rules | Parties-only where required; no implied cancel (G-5). |
| 10 | Interactions | Open owning screen; cancel where rule permits. |
| 11 | Disabled | Cancel disabled explains. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | Due/state announced (G-9). |
| 14 | Tokens | Pending/warning (G-10). |
| 15 | States | pending, due-soon, overdue-boundary, cancellable, non-cancellable. |
| 16 | Requirements | `REQ-1047`, `REQ-883`. |
| 17 | Screens | `SCR-014` and owning screens. |
| 18 | Reuse restrictions | No cross-system bulk commit. |
| 19 | Dependencies | TR-004; D-016/D-030. |

### UI-CMP-071 — Chronicle record

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-071` |
| 2 | Name | Chronicle record |
| 3 | Purpose | Presents a dated chronicle entry with class and retention. |
| 4 | Category | World; **System-specific (B-11)** |
| 5 | Visual structure | Turn, class, participants, outcome, retention label. |
| 6 | Content fields | Turn, class, participants, outcome, public/restricted, retention. |
| 7 | Required/optional | Required: turn/class/outcome. |
| 8 | Hierarchy | Turn/outcome first. |
| 9 | Data rules | No private fact/moderator note/inferred motive (G-5). |
| 10 | Interactions | Object links. |
| 11 | Disabled | Restricted entries labelled/absent. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | Turn/class announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | public, class-P, class-O-boundary, retired. |
| 16 | Requirements | `REQ-1048`. |
| 17 | Screens | `SCR-017/070/075/076`. |
| 18 | Reuse restrictions | Not a live status card. |
| 19 | Dependencies | D-026; TR-049. |

### UI-CMP-072 — Suppression indicator

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-072` |
| 2 | Name | Suppression indicator |
| 3 | Purpose | Renders a suppressed or insufficient-sample state as a named, explanatory state. |
| 4 | Category | World; **Data presentation**; **Conditionally available** |
| 5 | Visual structure | Eye-off glyph, label, explanation sentence, rule link. |
| 6 | Content fields | State (`suppressed`/`insufficient sample`), reason, threshold (not value), link. |
| 7 | Required/optional | Required wherever k=5 or sample rules apply. |
| 8 | Hierarchy | Replaces the value, not appended beneath a fake zero. |
| 9 | Data rules | Never zero, absent, inferable from counts/layout/differences (G-5). |
| 10 | Interactions | Rule explanation only; no "reveal" control. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Same state and text on every device (G-8). |
| 13 | Accessibility | Announced as suppressed, not empty (G-9). |
| 14 | Tokens | Suppressed tone (G-10). |
| 15 | States | suppressed, insufficient-sample, not-disclosed. |
| 16 | Requirements | `REQ-1056`, `REQ-1066`. |
| 17 | Screens | Every aggregate surface. |
| 18 | Reuse restrictions | Never used for ordinary missing data. |
| 19 | Dependencies | D-027; TR-022; WEP-663; MKT-110. |

### UI-CMP-073 — Historical reward record

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-073` |
| 2 | Name | Historical reward record |
| 3 | Purpose | Presents a reward's grant/deferral/correction record. |
| 4 | Category | World; **System-specific (B-11)** |
| 5 | Visual structure | Reward, class, state, turn, source, correction note. |
| 6 | Content fields | Reward, class, quantity, state, turn, source, correction. |
| 7 | Required/optional | Required: reward/state/turn. |
| 8 | Hierarchy | State first; quantity second. |
| 9 | Data rules | Deferred ≠ granted; correction appends (G-5). |
| 10 | Interactions | Open source. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Row→card (G-8). |
| 13 | Accessibility | State/quantity announced (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | granted, deferred, voided, corrected. |
| 16 | Requirements | `REQ-1043`, `REQ-1072`. |
| 17 | Screens | `SCR-073/075`. |
| 18 | Reuse restrictions | Never present a deferred claim as granted. |
| 19 | Dependencies | WEP-705. |

## 8. Forms and action components — UI-CMP-074…UI-CMP-090

All form components inherit G-1…G-15 and `REQ-1049`. Each has a programmatic label, inline text error, disabled reason and keyboard operability. None invents a field; fields come from the owning screen's rule.

### UI-CMP-074 — Text input

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-074` |
| 2 | Name | Text input |
| 3 | Purpose | Captures free text within a rule-defined field. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Label, input, help text, error text, character/format hints. |
| 6 | Content fields | Label, value, placeholder (never sole label), help, error, max length. |
| 7 | Required/optional | Required: label, value binding. |
| 8 | Hierarchy | Label above input; error adjacent. |
| 9 | Data rules | Normalization per rule (NFC/fold where D-038 applies); no silent truncation. |
| 10 | Interactions | Type, paste, clear. |
| 11 | Disabled | Reason via described-by. |
| 12 | Responsive | Full width; input mode appropriate (G-8). |
| 13 | Accessibility | Programmatic label; `aria-invalid`; error linked (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, hover, focus, disabled+reason, error, success, read-only. |
| 16 | Requirements | `REQ-1049`, `REQ-1086`. |
| 17 | Screens | All forms. |
| 18 | Reuse restrictions | Not for numeric or selection data. |
| 19 | Dependencies | `13A-DS-11`. |

### UI-CMP-075 — Numeric input

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-075` |
| 2 | Name | Numeric input |
| 3 | Purpose | Captures an integer or basis-point value with units and bounds. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Label, numeric field, unit/suffix, min/max, step, error. |
| 6 | Content fields | Label, value, unit, min, max, step, error. |
| 7 | Required/optional | Required: label/value/unit/bounds. |
| 8 | Hierarchy | Bounds/unit adjacent to field. |
| 9 | Data rules | Whole units/crowns; bp suffix; no float display (G-5). |
| 10 | Interactions | Type, increment, paste. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Numeric keypad; full width (G-8). |
| 13 | Accessibility | Unit in accessible name; range announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, integer-only, invalid, out-of-range, disabled+reason. |
| 16 | Requirements | `REQ-1049`, `REQ-1086`. |
| 17 | Screens | `SCR-036/043/046/056/072`. |
| 18 | Reuse restrictions | Not for free text. |
| 19 | Dependencies | D-045/D-064. |

### UI-CMP-076 — Select control

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-076` |
| 2 | Name | Select control |
| 3 | Purpose | Chooses one option from a rule-defined closed set. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Label, trigger, option list, selected value, error. |
| 6 | Content fields | Label, options, selected, help, error. |
| 7 | Required/optional | Required: label/options. |
| 8 | Hierarchy | Label above; selected value visible when closed. |
| 9 | Data rules | Closed set from the rule; no invented option. |
| 10 | Interactions | Open, choose, keyboard. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Native select on mobile where possible (G-8). |
| 13 | Accessibility | Combobox/listbox semantics; selected announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, open, selected, disabled+reason, error. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | All filter/form surfaces. |
| 18 | Reuse restrictions | Not for multi-select. |
| 19 | Dependencies | Owning rule sets. |

### UI-CMP-077 — Multi-select control

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-077` |
| 2 | Name | Multi-select control |
| 3 | Purpose | Chooses several options with a visible limit. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Label, checkbox/listbox options, selected chips, limit counter. |
| 6 | Content fields | Label, options, selected set, limit, error. |
| 7 | Required/optional | Required: label/options/limit where a limit exists. |
| 8 | Hierarchy | Limit visible before selection. |
| 9 | Data rules | Limit from the rule; no silent drop. |
| 10 | Interactions | Toggle options, clear. |
| 11 | Disabled | Limit reason. |
| 12 | Responsive | List in a sheet (G-8). |
| 13 | Accessibility | Each option labelled; limit announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, selected-many, limit-reached, disabled. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | `SCR-036/056/077`, filters. |
| 18 | Reuse restrictions | Not for exclusive choices. |
| 19 | Dependencies | Owning limits. |

### UI-CMP-078 — Checkbox

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-078` |
| 2 | Name | Checkbox |
| 3 | Purpose | Captures an independent boolean or acknowledgement. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Box, label, optional help, error. |
| 6 | Content fields | Label, checked, indeterminate, help, error. |
| 7 | Required/optional | Required: label/checked. |
| 8 | Hierarchy | Label clickable, not just the box. |
| 9 | Data rules | No pre-checked consent. |
| 10 | Interactions | Toggle, keyboard. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Touch target includes label (G-8). |
| 13 | Accessibility | Native checkbox semantics (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, checked, indeterminate, disabled+reason, error. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | `SCR-002/026/081/092`. |
| 18 | Reuse restrictions | Not for mutually exclusive choices. |
| 19 | Dependencies | G-9. |

### UI-CMP-079 — Radio control

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-079` |
| 2 | Name | Radio control |
| 3 | Purpose | Chooses exactly one option from a visible set. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Group label, radio options, selected, error. |
| 6 | Content fields | Group label, options, selected, help, error. |
| 7 | Required/optional | Required: group label/options. |
| 8 | Hierarchy | Group label first. |
| 9 | Data rules | No default where the rule requires a deliberate choice (e.g. government). |
| 10 | Interactions | Select, keyboard arrows. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Stacked options (G-8). |
| 13 | Accessibility | `radiogroup` semantics (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, selected, disabled+reason, error. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | `SCR-007/024/049/067`. |
| 18 | Reuse restrictions | Not for multi-select. |
| 19 | Dependencies | DMP-081 where government choice applies. |

### UI-CMP-080 — Toggle

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-080` |
| 2 | Name | Toggle |
| 3 | Purpose | Switches a setting with immediate visible state. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Label, switch, state text. |
| 6 | Content fields | Label, on/off, pending, error. |
| 7 | Required/optional | Required: label/state. |
| 8 | Hierarchy | Label and state together. |
| 9 | Data rules | Only for settings the rule exposes. |
| 10 | Interactions | Toggle; save where required. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Touch target ≥ minimum (G-8). |
| 13 | Accessibility | `switch` semantics with state text (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | on, off, pending, disabled+reason, error. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | `SCR-032/079/080`. |
| 18 | Reuse restrictions | Not for actions that commit a transaction. |
| 19 | Dependencies | Owning settings rules. |

### UI-CMP-081 — Date/turn selector

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-081` |
| 2 | Name | Date/turn selector |
| 3 | Purpose | Selects a turn or turn range for a filter or a rule-defined window. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Turn/range fields with UTC context and preset ranges. |
| 6 | Content fields | Start/end turn, UTC mapping, preset, error. |
| 7 | Required/optional | Required: turn values. |
| 8 | Hierarchy | Range first; presets secondary. |
| 9 | Data rules | Turns+UTC; no device-local assumption (G-5). |
| 10 | Interactions | Choose range, presets. |
| 11 | Disabled | Invalid range reason. |
| 12 | Responsive | Full width; steppers (G-8). |
| 13 | Accessibility | Turn/UTC announced (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, turn-range, invalid, provisional-window. |
| 16 | Requirements | `REQ-1049`, `REQ-1007`. |
| 17 | Screens | `SCR-025/031/040/052/066/072`. |
| 18 | Reuse restrictions | Not a wall-clock date picker for gameplay windows. |
| 19 | Dependencies | TR-024. |

### UI-CMP-082 — Search field

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-082` |
| 2 | Name | Search field |
| 3 | Purpose | Queries within a declared scope. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Label, input, clear, result count, scope hint. |
| 6 | Content fields | Query, scope, results/count, no-result, error. |
| 7 | Required/optional | Required: label/scope. |
| 8 | Hierarchy | Scope hint before typing. |
| 9 | Data rules | No query that discloses a higher class. |
| 10 | Interactions | Type, clear, select result. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Full width/sheet (G-8). |
| 13 | Accessibility | Search landmark; live result count (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, typing, results, no-result, denied, loading. |
| 16 | Requirements | `REQ-1049`, `REQ-1003`. |
| 17 | Screens | `SCR-010/018/026/072/078/092`. |
| 18 | Reuse restrictions | Not a full-text corpus promise. |
| 19 | Dependencies | `13A-OQ-005`. |

### UI-CMP-083 — Form field group

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-083` |
| 2 | Name | Form field group |
| 3 | Purpose | Groups related fields with shared help and error summary. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Group heading, fields, group help, summary error. |
| 6 | Content fields | Group label, fields, required set, help, errors. |
| 7 | Required/optional | Required: group label/fields. |
| 8 | Hierarchy | Group label first; error summary at top of group. |
| 9 | Data rules | No field invented beyond the rule. |
| 10 | Interactions | Per-field interactions. |
| 11 | Disabled | Group reason. |
| 12 | Responsive | Stacked fields (G-8). |
| 13 | Accessibility | `fieldset`/`legend` or equivalent (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, required, optional, error, grouped-help. |
| 16 | Requirements | `REQ-1049`, `REQ-1086`. |
| 17 | Screens | All task screens. |
| 18 | Reuse restrictions | Not for layout-only grouping. |
| 19 | Dependencies | `13A-DS-11`. |

### UI-CMP-084 — Validation message

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-084` |
| 2 | Name | Validation message |
| 3 | Purpose | Communicates an error, warning or success in text linked to its field. |
| 4 | Category | Form; **Global** |
| 5 | Visual structure | Inline text with glyph, field link, summary variant. |
| 6 | Content fields | Message, severity, field, rule hint. |
| 7 | Required/optional | Required: message/severity. |
| 8 | Hierarchy | Adjacent to the field; summary at form top. |
| 9 | Data rules | No colour-only error; no vague message. |
| 10 | Interactions | Focus field link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Inline remains; summary collapsible (G-8). |
| 13 | Accessibility | `aria-live`/described-by; text is the error (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | inline, summary, error, warning, success, provisional. |
| 16 | Requirements | `REQ-1049`, `REQ-1086`. |
| 17 | Screens | All forms. |
| 18 | Reuse restrictions | Not a toast substitute. |
| 19 | Dependencies | `13A-DS-11`. |

### UI-CMP-085 — Primary action button

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-085` |
| 2 | Name | Primary action button |
| 3 | Purpose | Performs the main committing or navigating action of a screen. |
| 4 | Category | Action; **Global** |
| 5 | Visual structure | Filled primary button with label and optional icon. |
| 6 | Content fields | Label, action, state, confirmation requirement. |
| 7 | Required/optional | Required: label/action. |
| 8 | Hierarchy | One primary per action region. |
| 9 | Data rules | No action without a rule; no preselected confirm. |
| 10 | Interactions | Activate, keyboard, loading state. |
| 11 | Disabled | Reason via `OVL-03`. |
| 12 | Responsive | Full width in mobile action bar (G-8). |
| 13 | Accessibility | Button semantics; not a link if it commits (G-9). |
| 14 | Tokens | Primary/status (G-10). |
| 15 | States | default, hover, focus, active, disabled+reason, loading, success, pending. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | All committing screens. |
| 18 | Reuse restrictions | Not for destructive actions. |
| 19 | Dependencies | `13A-PR-09`. |

### UI-CMP-086 — Secondary action button

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-086` |
| 2 | Name | Secondary action button |
| 3 | Purpose | Offers the safe alternative or non-destructive navigation. |
| 4 | Category | Action; **Global** |
| 5 | Visual structure | Outlined/quiet button. |
| 6 | Content fields | Label, action, state. |
| 7 | Required/optional | Required when a cancel/alternative exists. |
| 8 | Hierarchy | Adjacent to primary, visually subordinate. |
| 9 | Data rules | Never the destructive option. |
| 10 | Interactions | Activate. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Full width below primary (G-8). |
| 13 | Accessibility | Button semantics (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, hover, focus, active, disabled+reason, loading. |
| 16 | Requirements | `REQ-1049`. |
| 17 | Screens | All screens with a secondary path. |
| 18 | Reuse restrictions | Not for the primary commit. |
| 19 | Dependencies | 08C §12.3. |

### UI-CMP-087 — Destructive action button

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-087` |
| 2 | Name | Destructive action button |
| 3 | Purpose | Triggers a destructive or irreversible action with barrier styling. |
| 4 | Category | Action; **Global** |
| 5 | Visual structure | Danger-toned button, separated from primary, with warning glyph. |
| 6 | Content fields | Label, action, consequence summary, confirmation requirement. |
| 7 | Required/optional | Required only where a destructive action exists. |
| 8 | Hierarchy | Separated from primary; never adjacent without spacing. |
| 9 | Data rules | Exact consequence before commit; no remembered confirmation. |
| 10 | Interactions | Activate → `OVL-02`/exact phrase. |
| 11 | Disabled | Reason. |
| 12 | Responsive | Bottom of sheet, separated; touch spacing (G-8). |
| 13 | Accessibility | Name includes consequence; not colour-only (G-9). |
| 14 | Tokens | Danger tone (G-10). |
| 15 | States | default, hover, focus, disabled+reason, confirmation-required. |
| 16 | Requirements | `REQ-1049`, `REQ-1055`. |
| 17 | Screens | `SCR-012/043/090`; `SCR-094`. |
| 18 | Reuse restrictions | Never used for reversible actions. |
| 19 | Dependencies | RRL-006; `13A-DS-14`. |

### UI-CMP-088 — Confirmation panel

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-088` |
| 2 | Name | Confirmation panel |
| 3 | Purpose | States the exact effect, cost, cooldown and irreversible consequence before commit. |
| 4 | Category | Action; **Global** |
| 5 | Visual structure | Summary list, consequence, cancel, confirm. |
| 6 | Content fields | Action, effect, cost, cooldown, phase/boundary, irreversible consequence, cancel, confirm. |
| 7 | Required/optional | Required: effect/cost/cancel/confirm. |
| 8 | Hierarchy | Effect first; cancel and confirm last. |
| 9 | Data rules | Exact values; no preselected confirm; no confirm-by-default. |
| 10 | Interactions | Confirm/cancel. |
| 11 | Disabled | Confirm disabled with reason if precondition changes. |
| 12 | Responsive | Full-screen sheet on mobile (G-8). |
| 13 | Accessibility | Dialog semantics; focus trap; cancel first in focus order (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | default, pending, warning, error, success, exact-phrase. |
| 16 | Requirements | `REQ-1049`, `REQ-1023`. |
| 17 | Screens | Every committing control. |
| 18 | Reuse restrictions | Never the only place a state exists (page equivalent required). |
| 19 | Dependencies | `13A-PR-09`; 08C §12.3; WAR-152. |

### UI-CMP-089 — Disabled action with reason

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-089` |
| 2 | Name | Disabled action with reason |
| 3 | Purpose | Explains why an action is unavailable before the click. |
| 4 | Category | Action; **Global** |
| 5 | Visual structure | Disabled control + lock glyph + reason text/link. |
| 6 | Content fields | Action, reason, governing rule, next eligible turn/condition. |
| 7 | Required/optional | Required for every disabled action. |
| 8 | Hierarchy | Reason adjacent to control. |
| 9 | Data rules | Reason must be specific and rule-linked; no "not allowed". |
| 10 | Interactions | Reason popover `OVL-03`; no action. |
| 11 | Disabled | This is the disabled state. |
| 12 | Responsive | Reason text remains visible on tap (G-8). |
| 13 | Accessibility | `aria-disabled` + described-by reason (G-9). |
| 14 | Tokens | Locked/denied tone (G-10). |
| 15 | States | default, reason-visible, rule-linked, permission-denied. |
| 16 | Requirements | `REQ-1049`, `REQ-1088`. |
| 17 | Screens | Every disabled control. |
| 18 | Reuse restrictions | Never hides a rule behind a tooltip only. |
| 19 | Dependencies | `13A-PR-10`; `13A-BP-028`. |

### UI-CMP-090 — Exact-phrase confirmation field

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `UI-CMP-090` |
| 2 | Name | Exact-phrase confirmation field |
| 3 | Purpose | Requires typing an exact phrase for a destructive action. |
| 4 | Category | Action; **Global**; **Conditionally available** |
| 5 | Visual structure | Prompt, input, match indicator, disabled confirm until match. |
| 6 | Content fields | Expected phrase, entered value, match state. |
| 7 | Required/optional | Required where RRL-006/admin exact confirmation applies. |
| 8 | Hierarchy | Phrase instruction before input; confirm after match. |
| 9 | Data rules | Exact current nation name or defined phrase; no case ambiguity beyond rule. |
| 10 | Interactions | Type; match; confirm. |
| 11 | Disabled | Mismatch reason. |
| 12 | Responsive | Full width; no autocomplete (G-8). |
| 13 | Accessibility | Instruction linked; match announced (G-9). |
| 14 | Tokens | Danger tone (G-10). |
| 15 | States | default, mismatch, match, disabled. |
| 16 | Requirements | `REQ-1049`, `REQ-959`. |
| 17 | Screens | `SCR-090`; admin destructive actions. |
| 18 | Reuse restrictions | Not for reversible actions. |
| 19 | Dependencies | RRL-006. |

## 9. Overlay components — OVL-01…OVL-08

All overlays inherit §1.3. Each overlay below answers the same 19 fields; "page equivalent" is mandatory and specified.

### OVL-01 — Confirmation dialog

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-01` |
| 2 | Name | Confirmation dialog |
| 3 | Purpose | Confirms a committing action with exact effect, cost, cooldown and phase. |
| 4 | Category | Overlay; **Global** |
| 5 | Visual structure | Modal with title, summary list, cancel, confirm. |
| 6 | Content fields | Action, effect, cost, cooldown, boundary phase, consequence. |
| 7 | Required/optional | Required for every committing control. |
| 8 | Hierarchy | Effect first; actions last. |
| 9 | Data rules | Exact values; forecast labels; no invented cost. |
| 10 | Interactions | Confirm/cancel/dismiss. |
| 11 | Disabled | Confirm disabled when precondition changes. |
| 12 | Responsive | Full-screen sheet on mobile (G-8). |
| 13 | Accessibility | Dialog focus trap/restore; cancel first (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | open, pending, error, success. |
| 16 | Requirements | `REQ-1049`; `REQ-977` (page equivalence via `UI-CMP-088`). |
| 17 | Screens | Every committing control. |
| 18 | Reuse restrictions | Confirm/block/explain only. |
| 19 | Page equivalent | The owning screen renders the same effect/cost summary in `UI-CMP-088`; no fact exists only here. |

### OVL-02 — Destructive exact-phrase dialog

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-02` |
| 2 | Name | Destructive exact-phrase dialog |
| 3 | Purpose | Blocks an irreversible action behind an exact phrase and consequence list. |
| 4 | Category | Overlay; **Global**; **Conditionally available** |
| 5 | Visual structure | Modal with consequence list, exact-phrase field, cancel, destructive confirm. |
| 6 | Content fields | Consequences, phrase, match state, cancel, confirm. |
| 7 | Required/optional | Required where RRL-006/admin exact confirmation applies. |
| 8 | Hierarchy | Consequences before phrase; cancel before confirm. |
| 9 | Data rules | Exact phrase; no remembered confirmation. |
| 10 | Interactions | Type, confirm, cancel. |
| 11 | Disabled | Mismatch/blocked reason. |
| 12 | Responsive | Full-screen sheet; separated actions (G-8). |
| 13 | Accessibility | Dialog semantics; phrase instruction linked (G-9). |
| 14 | Tokens | Danger (G-10). |
| 15 | States | open, mismatch, match, pending. |
| 16 | Requirements | `REQ-1049`, `REQ-1055`. |
| 17 | Screens | `SCR-090`, `SCR-094`, `SCR-012`. |
| 18 | Reuse restrictions | Irreversible actions only. |
| 19 | Page equivalent | `SCR-090` is the page-reachable confirmation; admin destructive pages retain the same consequence text. |

### OVL-03 — Reason popover

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-03` |
| 2 | Name | Reason popover |
| 3 | Purpose | Explains a disabled control and links the governing rule. |
| 4 | Category | Overlay; **Global** |
| 5 | Visual structure | Popover anchored to control with reason and rule link. |
| 6 | Content fields | Reason, rule anchor, next eligible turn/condition. |
| 7 | Required/optional | Required for every disabled control. |
| 8 | Hierarchy | Reason first; link second. |
| 9 | Data rules | Specific, rule-linked; never "not allowed". |
| 10 | Interactions | Open/dismiss; rule link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Tap sheet on mobile (G-8). |
| 13 | Accessibility | Accessible description; dismissible (G-9). |
| 14 | Tokens | Locked tone (G-10). |
| 15 | States | open, focus-dismiss, rule-link. |
| 16 | Requirements | `REQ-1049`, `REQ-1029`. |
| 17 | Screens | Every disabled control. |
| 18 | Reuse restrictions | Not the only reason channel; `UI-CMP-089` carries text. |
| 19 | Page equivalent | The rule page `SCR-078` and the control's inline reason. |

### OVL-04 — Definition / cause-chain drawer

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-04` |
| 2 | Name | Definition / cause-chain drawer |
| 3 | Purpose | Explains a term or cause chain without losing the parent screen. |
| 4 | Category | Overlay; **Global** |
| 5 | Visual structure | Side drawer/sheet with definition, cause chain, rule anchor. |
| 6 | Content fields | Term, definition, contributing terms/values, source. |
| 7 | Required/optional | Optional enhancement; required where a cause chain is cited. |
| 8 | Hierarchy | Definition first; chain second. |
| 9 | Data rules | No hidden term; no invented cause. |
| 10 | Interactions | Open/dismiss; deep link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Full-screen sheet; page-reachable (G-8). |
| 13 | Accessibility | Dialog/drawer semantics; focus restored (G-9). |
| 14 | Tokens | G-10. |
| 15 | States | open, loading, empty, deep-linked page. |
| 16 | Requirements | `REQ-1049`, `REQ-997`. |
| 17 | Screens | All read surfaces. |
| 18 | Reuse restrictions | Not for confirmation. |
| 19 | Page equivalent | The owning screen's detail section and `SCR-078` glossary. |

### OVL-05 — Object peek card

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-05` |
| 2 | Name | Object peek card |
| 3 | Purpose | Previews a linked object within its visibility class. |
| 4 | Category | Overlay; **Global** |
| 5 | Visual structure | Peek card with identity, type, public state, full-view link. |
| 6 | Content fields | Identity, type, permitted summary, visibility state. |
| 7 | Required/optional | Optional enhancement. |
| 8 | Hierarchy | Identity first. |
| 9 | Data rules | Only already-visible fields (G-5). |
| 10 | Interactions | Open full view; dismiss. |
| 11 | Disabled | Denied state. |
| 12 | Responsive | Tap sheet (G-8). |
| 13 | Accessibility | Dismissible; not focus-trapping if non-modal (G-9). |
| 14 | Tokens | Elevation (G-10). |
| 15 | States | open, loading, denied, suppressed. |
| 16 | Requirements | `REQ-1049`, `REQ-996`. |
| 17 | Screens | Every object link. |
| 18 | Reuse restrictions | Never the only place a fact/action exists. |
| 19 | Page equivalent | The object's full page (`SCR-010`, `SCR-053`, etc.). |

### OVL-06 — Boundary-effect notice

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-06` |
| 2 | Name | Boundary-effect notice |
| 3 | Purpose | Announces a settled, pending, failed or interrupted boundary outcome. |
| 4 | Category | Overlay; **Global** |
| 5 | Visual structure | Small notice/toast with state, object link, dismiss. |
| 6 | Content fields | Outcome state, affected object, turn, link. |
| 7 | Required/optional | Optional presentation; the digest is the durable record. |
| 8 | Hierarchy | State first. |
| 9 | Data rules | Existing event only; no fabricated outcome. |
| 10 | Interactions | Open; dismiss. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Bottom notice (G-8). |
| 13 | Accessibility | Polite live-region; dismissible (G-9). |
| 14 | Tokens | Status tones (G-10). |
| 15 | States | settled, pending, failed, interrupted. |
| 16 | Requirements | `REQ-1049`, `REQ-975`. |
| 17 | Screens | Shell. |
| 18 | Reuse restrictions | Never the only record of a settlement. |
| 19 | Page equivalent | `SCR-013` digest and `SCR-016` settlement status. |

### OVL-07 — Suppression notice

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-07` |
| 2 | Name | Suppression notice |
| 3 | Purpose | Explains a suppressed aggregate with its reason. |
| 4 | Category | Overlay; **Global**; **Conditionally available** |
| 5 | Visual structure | Notice with eye-off glyph, reason, rule link. |
| 6 | Content fields | Suppression state, reason, threshold (not value), link. |
| 7 | Required/optional | Required wherever k=5/sample rules apply. |
| 8 | Hierarchy | Replaces the value. |
| 9 | Data rules | Never zero/absent/inferable (G-5). |
| 10 | Interactions | Rule link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Same state/text on all devices (G-8). |
| 13 | Accessibility | Announced as suppressed (G-9). |
| 14 | Tokens | Suppressed tone (G-10). |
| 15 | States | suppressed, insufficient-sample. |
| 16 | Requirements | `REQ-1049`, `REQ-1056`. |
| 17 | Screens | Every aggregate surface. |
| 18 | Reuse restrictions | Not ordinary missing data. |
| 19 | Page equivalent | `UI-CMP-072` inline state and `SCR-078` rule explanation. |

### OVL-08 — Claim-vocabulary badge

| # | Field | Specification |
| --- | --- | --- |
| 1 | ID | `OVL-08` |
| 2 | Name | Claim-vocabulary badge |
| 3 | Purpose | Displays the EVD-009 claim tier in B-12 contexts. |
| 4 | Category | Overlay; **System-specific (B-12)**; **Role-restricted** |
| 5 | Visual structure | Badge with tier label and glyph. |
| 6 | Content fields | Tier (`suspected`/`under review`/`confirmed`/`inconclusive`). |
| 7 | Required/optional | Required in B-12 notices/cases. |
| 8 | Hierarchy | Adjacent to the claim. |
| 9 | Data rules | Exact four terms; never upgraded silently (G-5). |
| 10 | Interactions | Explanation link. |
| 11 | Disabled | Not applicable. |
| 12 | Responsive | Label survives (G-8). |
| 13 | Accessibility | Text is the accessible name (G-9). |
| 14 | Tokens | Neutral/warning/confirmed tones (G-10). |
| 15 | States | suspected, under-review, confirmed, inconclusive. |
| 16 | Requirements | `REQ-1049`, `REQ-951`. |
| 17 | Screens | `SCR-082/084/086`; admin `SCR-092/093`. |
| 18 | Reuse restrictions | B-12 contexts only; never a game-state label. |
| 19 | Page equivalent | The notice/case page text carries the tier. |

---

**End of component bodies.** All 90 `UI-CMP` components and 8 `OVL` overlays are specified. The authoritative usage register is Matrix B in the [parent document](21_interface_and_player_journeys.md#25-matrix-b--component-usage).