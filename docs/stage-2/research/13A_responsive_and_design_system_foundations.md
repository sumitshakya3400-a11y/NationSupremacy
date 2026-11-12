# 13A — Responsive-design foundations and design-system foundations

**Prompt:** Stage 2 Prompt 13A (Deliverables E and F).
**Created:** 2026-11-11. **Status:** foundations only — **no CSS, no framework, no component implementation**; 13B writes component and screen specifications against these rules.
**Companions:** [research register](13A_politics_and_war_ui_research.md) · [principles and architecture](13A_ui_design_principles_and_architecture.md) · [screen inventory](13A_master_screen_inventory.md) · [requirements and acceptance](13A_ui_requirements_open_questions_and_acceptance.md)

---

## 1. Responsive philosophy (Deliverable E)

### 1.1 One game, one rule set, N layouts (`13A-RD-01`)

Fixed constraint (AI_CONTEXT §2; owner Category A): Nation Supremacy is **a browser game**; a mobile/tablet player plays *the same game with the same rules* — no separate product, no different cadence, no reduced mechanics (13A instruction §10; `13A-RD-01`). What may differ is **layout, density and interaction affordance**, never state truth:

- Data disclosed to a player is identical across devices (visibility classes are server-side rules, not viewport features).
- A capability that exists on desktop must exist on mobile **as a decision**, or be explicitly registered as deferred with its reason — the roadmap Prompt-13 section admits no silent mobile-only omissions. Today every `SCR-` Mandatory screen must be reachable and act-capable on all three device classes; complex *editing* surfaces (e.g. `SCR-056` bracket editor, `SCR-043` queue management) may use stepped layouts but not disabled capability.

### 1.2 Benchmark reading

P&W is the **desktop-oriented genre reference** (`13A-FND-026`): dense tables, minimal adaptation, evidence of mobile menu toggles only via changelog code notes (`13A-SRC-036`, low confidence). The genuinely relevant mobile lesson comes from the supplementary register: Cyber Nations shipped an explicitly **user-selectable** mobile-friendly rendering with per-profile opt-in/opt-out (`13A-SRC-029`, 2025-04-04) — proof that this genre's audiences span phones and that an adaptive *mode*, not a shrunken page, is viable. Nation Supremacy therefore treats responsive layout as a first-class design axis from day one, while recording the CN-style user override as a provisional question (`13A-OQ-014`).

### 1.3 Device-class requirements (13A-RD register)

| ID | Class | Requirements |
|---|---|---|
| `13A-RD-02` | **Desktop** (genre default) | Persistent global nav (shell §4); multi-panel: primary content + context panel; full table grammar with saved views; Network View at full interactivity; comparison surfaces available; keyboard navigation and focus visibility mandatory; hover states are enhancements only — every hover-revealed fact must be reachable by focus/click too |
| `13A-RD-03` | **Tablet** | Section nav collapses to icon rail or labeled overflow menu (never more than one tap to any section); context panel becomes a bottom sheet or drawer that *replaces* nothing permanently; tables keep columns with progressive horizontal scroll **plus** a column-priority setting (the row's identity column pinned); touch targets ≥ the accessibility target size; charts scale without losing labels |
| `13A-RD-04` | **Mobile browser** | Shell reduces to: countdown, alert count, section menu, content, bottom nav for Home/Inbox/World/Account; the **Inbox and Digest remain first-class** (the check-in loop is the core mobile journey, per Report 04's 1–3×5–15-min persona evidence — Mira); long tables convert to card lists preserving total/reserved/available triples (MKT-053 survives layout change — *a card that hides a reservation is a defect*); Network View degrades to a filtered relationship list with graph as opt-in; turn countdown always visible in the header band (PR-01); notifications deep-link directly into task screens |
| `13A-RD-05` | **All devices** | One codebase/route table; identical URL per screen (deep-link parity); text reflow without horizontal page scroll; system font/zoom respect; offline/disconnected state labelled with slot staleness (§ states doc); time-sensitive content expressed in turns+UTC everywhere, never device-local assumptions |
| `13A-RD-06` | **Provisional breakpoints** | *Not owner-approved numbers.* Working defaults for 13B exploration only: phone ≤ ~600 px, tablet ~600–1024 px, desktop > ~1024 px, plus container-query-first where components rather than pages decide. Recorded as Category-C provisional: the confirming evidence is real-browser testing on the production build (Stage 5+), which does not exist yet — no measurement is claimed here |
| `13A-RD-07` | **Must-not-simplify list** | The following may never be reduced away on mobile: turn countdown; pending-action counts; political state banner; protection state; k=5 suppression notices; confirmation dialogs (may move to full-screen sheets); reason strings for disabled actions |
| `13A-RD-08` | **May-simplify list** | Context panel default-collapsed; Network View behind a list-first toggle; multi-column tables to card lists; decorative section headers; secondary sort affordances behind a menu |

## 2. Design-system foundations (Deliverable F)

Namespaces: rules `13A-DS-###`; component families are named but not specified (13B owns specs). Semantic first: *no raw colour/size reference in screen specs; every reference is to a token or state name* (D-203).

### 2.1 Typography

| ID | Rule |
|---|---|
| `13A-DS-01` | Three registers: **display** (screen titles, dashboard headline numbers), **text** (prose, cause chains, rules), **data** (tabular numerals — monospaced figures so ledger columns align; this is a *fairness* feature: value changes must be visually trackable). Concrete families are an owner brand decision (`13A-OQ-002`) |
| `13A-DS-02` | Minimum body size and line-length discipline tuned for long-form cause explanations; no all-caps body text; sentence case headings |
| `13A-DS-03` | Number formatting project-wide: thousand separators, fixed basis-point rendering (`bp` suffix), crown/resource unit labels consistent with B-04 vocabulary; negative/zero/insufficient-sample rendered distinctly per PR-16 |

### 2.2 Spacing, grid, layout

| ID | Rule |
|---|---|
| `13A-DS-04` | 4-pt spacing scale as the only spacing source; density levels (compact / comfortable) map to the responsive device classes, not to user tiers (never a paid density) |
| `13A-DS-05` | 12-column content grid; shell regions (A–H of the architecture) are fixed slots, screens fill F only |
| `13A-DS-06` | Maximum sensible line measures for cause-chain prose; data tables break out of prose measures |

### 2.3 Component families (named here; specified in 13B)

Navigation: global section bar · overflow menu · breadcrumb bar · in-page tabs · object links (identifier → deep-link with peek `OVL-05`) · quick-go palette.
Containers: panel · card · section register (the six-number-type register, PR-03) · stat strip.
Data: **table grammar** (`13A-BP-004`: header row, filter row, saved views, range pagination "0–N of M" mirroring the benchmark's honest counts) · card-list fallback (RD-04) · chart primitives (line for over-time, bar for resource rows per CN lesson `13A-BP-022`, band displays only where a rule defines bands, e.g. WAR-085…088 four bands) · Network View canvas with list alternate · countdown component (turns + UTC boundary, PR-01).
Actions: button ladder (primary/secondary/tertiary/destructive) · form controls with inline validation · confirmation dialog (`OVL-01/02`) · reason popover (`OVL-03`) · disabled-with-explanation state (PR-10) · cooldown-on-control pattern (`13A-BP-011`).
Feedback: banners (political state banner DMP-268 is *the* pattern instance) · toasts (`OVL-06`) · alert bar counts · progress/queued indicators (three-class timing contract displayed) · suppression notice (`OVL-07`) · claim-vocabulary badge (`OVL-08`).
Overlays: modal · drawer/sheet · peek card — with the architecture document's overlays discipline enforced as a lint-able rule later.

### 2.4 Interaction states (mandatory matrix for every component in 13B)

`default · hover · focus-visible · active · disabled(+reason) · loading · success · warning · error · pending · suppressed` — each defined; hover is never load-bearing (RD-02); focus-visible always tokenized.

### 2.5 Status semantics mapping

Every game-system state vocabulary maps 1:1 onto the shell tone register (architecture §3.2): e.g. `PENDING/RESERVED/QUEUED` → pending tone; `UNMAINTAINED` → warning; `FAILED` settlement → danger; `TRANSITION/CRISIS/RECOVERY` → banner with its own defined tone pair; `INSUFFICIENT_SAMPLE` → PR-16 neutral special state; k=5 → suppressed; EVD-009 tiers → `OVL-08` badges only in B-12 contexts. **No new game state may be invented to make a UI convenient** (PR-11).

### 2.6 Information-visualization principles (instruction §11 list)

| Subject | Principle |
|---|---|
| National statistics | six-number-type register separation (PR-03); every figure carries its as-of slot (`13A-SRC-017` calendar-strip lesson, NS version: slot stamps) |
| Economic data | total/reserved/available always together (MKT-053); forecasts visually lighter (ECN-178); book value vs market disclosure only post-gate (D-117) |
| Military strength | **bands, never exact** where rules say bands (WAR-085…088); charts for own nation; others see only disclosed aggregates (WAR-150) |
| Diplomatic relations | edge labels = treaty *type tokens* like the benchmark's filter legend (`13A-SRC-010`), posture shown per direction; pending acts visible only per D-030 |
| Rankings | named lists with denominator + window (WEP-324); no "live" ticking (WEP-325); no composite headline (WEP-361/362) |
| Historical trends | over-time charts anchored to class-P/S retention boundary, labelled (`13A-DR-013`) |
| Resource quantities | capacity vs holding bars with reserved overlay segment; whole-unit/basis-point vocabulary per D-045/D-064 |
| Timelines | election/campaign dates always `campaign_open_turn`-anchored (D-106/D-107 wording law); protection windows as states + expiry turn, not countdowns alone |
| Reports | battle/war/trade receipts: two-sided complete records (ECON-013 lineage), conservation-visible accounting (WAR-109f…m impairment basis stated where shown) |
| Strategic comparisons | comparison canvas restricted to visibility-legal inputs (k=5 aware; `13A-DR-022`); differences displayed as facts with sources, never as predicted verdicts |
| **Anti-misleading rules (all charts)** | truncated axes flagged; "0" never drawn where truth is `suppressed`/`insufficient`/`unknown`; averages shown with sample-count context (MKT-110); every chart title carries units and time window; dual-axis charts banned |

### 2.7 Accessibility foundations (target: WCAG 2.2 AA as *design* intent, verified later — **no compliance claim is made or can be made without implementation**)

| ID | Requirement |
|---|---|
| `13A-DS-07` | Full keyboard operability of every action path (genre power users automate via tools — `13A-FND-012` — so a keyboard-first surface also serves fairness; focus order follows reading order, modals trap and restore focus) |
| `13A-DS-08` | Visible focus indicator tokenized at ≥3:1 against adjacent colours (design intent) |
| `13A-DS-09` | Contrast: text and essential graphics to AA thresholds as *specified tokens*; brand palette selection (`13A-OQ-001`) must pass before adoption |
| `13A-DS-10` | Colour-independence: every status = colour + glyph + text (PR-12; fixes the benchmark's colour-only affiliation columns `13A-FND-037`) |
| `13A-DS-11` | Every form control has a programmatic label; error identification by text linked to the field; the six-number-type and band vocabularies have defined screen-reader announcements (numbers read with units) |
| `13A-DS-12` | Tables have proper header/row-scope semantics; card fallbacks preserve the same accessible structure; charts require a text/table alternative panel (the data exists server-side — this is disclosure, not decoration) |
| `13A-DS-13` | Motion: none is gameplay; transitions respect reduced-motion; countdown updates are polite live-regions, never constant announcements |
| `13A-DS-14` | Touch: minimum target size token; spacing to prevent mis-tap on destructive actions (reroll, sanctions) with the exact-phrase dialog as backstop |
| `13A-DS-15` | Language: the design system keeps all strings localizable (benchmark serves multilingual users — language selector `13A-SRC-017`); no text in images |

### 2.8 What is explicitly **not** decided here

Final brand colours/logo/typefaces (owner-reserved, `13A-OQ-001/002`); framework/component library (Stage 5); iconography set membership (13B, after this vocabulary); dark mode (provisional question `13A-OQ-013`); motion identity; illustration. None of these is hidden inside an adopted token — the token layer names *roles*, and the owner decision supplies *values*.
