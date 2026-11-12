# 13A — UI requirements register, dependency map, open questions and acceptance gates

**Prompt:** Stage 2 Prompt 13A (Deliverables G, I and the acceptance register).
**Created:** 2026-11-11. **Status:** candidate requirements and design-foundation acceptance. **No `13A-UR-` row is approved as a product commitment; none is implemented.**
**Companions:** [research register](13A_politics_and_war_ui_research.md) · [principles and architecture](13A_ui_design_principles_and_architecture.md) · [screen inventory](13A_master_screen_inventory.md) · [responsive/design-system foundations](13A_responsive_and_design_system_foundations.md)

---

## 1. Identifier and status policy

- Candidate UI requirements: `13A-UR-001`…`13A-UR-048` (the §2 table uses the shorthand `UR-###`; the canonical identifier always carries the `13A-` prefix). **No global `REQ-` row is allocated by this pass**: `REQ-869` remains the frontier and `REQ-870` onward is reserved for Prompt 13B's B-13 requirement block (policy **D-204**, mirroring the 12A precedent that reserved `REQ-764` for 12B).
- Open questions: `13A-OQ-001`…`13A-OQ-016` (§4 shorthand `OQ-###`). **No global `UD-` row is opened**: UI questions that later become owner-blocked must be promoted to UD rows by 13B with the owner-prompt discipline (11A precedent — a research pass may carry a local register).
- Acceptance gates: `P13A-01`…`P13A-24` exactly as mandated by the instruction; grading 13A artefacts only (**D-205** gate separation — no gate here raises, lowers or reinterprets any 12A/12B/12C gate or protected status).
- Approval classifications used: `INHERITED` (existing approved rule restated for surfaces), `CATEGORY B — CONFIRMED (design)` (adopted position under D-014, mirrored in a D-entry), `PROVISIONAL (C)` (named confirming test), `OWNER-RESERVED` (kept open).

## 2. UI requirements register (13A-UR-001…048)

The register is in two parts sharing one identifier spine: **§2.1** carries statement · category · priority · origin · related system · existing-requirement link · research reference · status/approval; **§2.2** carries the dependency and acceptance-intent fields for the same IDs. Together the two parts supply every field the instruction mandates for a requirement row.

### 2.1 Register

Fields: statement · category · priority · origin · related system · existing requirement link · research ref · status · approval.

| ID | Statement | Cat | Pri | Origin | System | Existing link | Research | Status / approval |
|---|---|---|---|---|---|---|---|---|
| UR-001 | Every authenticated screen renders inside the persistent shell (identity strip, nav, alert bar, countdown) and deep-links by stable route | Shell | P0 | NS rules + benchmark | B-02 | REQ-020/022 | `13A-BP-001`, SRC-017 | Candidate / INHERITED-with-D-201 |
| UR-002 | The turn countdown and next-boundary time appear on every authenticated surface in turns + UTC | Shell | P0 | cadence constraint | B-02 | TR lattice | PR-01 | Candidate / Category B |
| UR-003 | All pending actions are aggregated in one Inbox ordered by due boundary; every row deep-links to its action screen | Navigation | P0 | NS lifecycle rules | all | three-class contract | FND-032 gap | Candidate / Category B |
| UR-004 | Home presents the Command Digest as the default landing surface; digest-first is the re-entry guarantee | Navigation | P0 | TR-089 | B-02 | TR-089; REQ-022 | BP-012 | Candidate / INHERITED |
| UR-005 | Six number types render in visually distinct registers; a forecast never shares weight with current state | Data | P0 | ECN-177/178 | B-04/B-05 | ECN-177; REQ-250 region | BP-022 | Candidate / INHERITED |
| UR-006 | Resource presentations always expose total/reserved/available together on every device | Data | P0 | MKT-053 | B-04/B-07 | MKT-053 | RD-04 | Candidate / INHERITED |
| UR-007 | Disabled controls display their reason before activation, linked to the governing rule | Interaction | P0 | 08C §12.7 | all | REQ-257 region | BP-024 | Candidate / INHERITED |
| UR-008 | Every committing action passes the confirmation pattern (effect/cost/cooldown/boundary phase) | Interaction | P0 | PR-09 | all | RRL-006; WAR §12.3; 08C §12.3 | BP-011 | Candidate / Category B |
| UR-009 | All status/affiliation information is colour + glyph + text (colour-independence) | A11y | P0 | PR-12 | all | DMP-164; REQ-321 | FND-037 | Candidate / INHERITED-with-D-203 |
| UR-010 | Every action path is keyboard-operable with visible focus | A11y | P0 | DS-07 | all | REQ-321 | FND-026 | Candidate / Category B |
| UR-011 | Tables, card fallbacks and charts have header semantics and text/table alternatives | A11y | P0 | DS-12 | all | — | BP-004 | Candidate / Category B |
| UR-012 | Suppressed aggregates render as labelled `suppressed` states, never as zero or absence | Data | P0 | D-027 | B-11/B-07/B-08/B-10 | TR-022; WEP-663; MKT-110 | DR-005 | Candidate / INHERITED |
| UR-013 | Visibility classes are enforced server-side; no surface discloses above its class, including layout-only hints (counts, thumbnails) | Security | P0 | TR-021; PRV; WAR | all | REQ-590/670; PRV-009/014/019 | BP-009 | Candidate / INHERITED |
| UR-014 | The Network View is the world-situational surface; no geographic map exists anywhere | Navigation | P0 | fixed constraint | B-02/B-08 | REQ-041 | BP-006/018 | Candidate / INHERITED |
| UR-015 | The War Operations Board is owner-only and never merges data into the Alliance management interface | Permissions | P0 | roadmap Prompt-13 boundary | B-09/B-10 | AX-18; WAR-148; REQ-589–591 | BP-009 | Candidate / INHERITED |
| UR-016 | Alliance screens expose tax-bracket creation/management, receipts, ARL categories and unavailable-purpose failure states exactly as B-09 specifies, each naming its governing section | Screen | P0 | roadmap B-09 dependency | B-09 | REQ-614–617 region | BP-010 | Candidate / INHERITED |
| UR-017 | No membership/coordination flow requires an external platform; block reasons (NAP, same-Alliance ban) are explained in-product | Screen | P0 | D-133 | B-09 | ALL-161/167/168; WAR-149 | BP-020 | Candidate / INHERITED |
| UR-018 | Political state banners (six states) appear on every political and consequence-bearing screen; blocked modes are visibly explained | Screen | P0 | DMP-268 | B-06 | REQ-317–321 region | — | Candidate / INHERITED |
| UR-019 | War odds/threat appear only as the four defined bands, never exact values | Data | P0 | WAR-085…088 | B-10 | REQ-687 region | BP-009 | Candidate / INHERITED |
| UR-020 | Standings appear as named lists with denominator and window; no live-updating rank | Data | P0 | WEP-324/325 | B-11 | REQ-728 region | BP-005/028 | Candidate / INHERITED |
| UR-021 | Onboarding runs inside the real shell with zeros; a rerolled/new nation sees the true frame | Screen | P0 | D-039/040; NAT-016 | B-03 | REQ-089/090 | BP-025 | Candidate / INHERITED |
| UR-022 | Protection states (newcomer/return) display as states with rule links; visibility-only, never re-granted, shown at block moments | Screen | P0 | D-040; ONB-020/022 | B-03/B-10 | REQ-090; REQ-687 region | — | Candidate / INHERITED |
| UR-023 | E-mail/verification/recovery journeys render the D-029/D-041 rules including dual-confirmation states | Screen | P0 | D-029/041 | B-03 | REQ-085/092 | SRC-017/018 | Candidate / INHERITED |
| UR-024 | Multi-account/pair-restriction states are explained player-side without accusation or technical exposure | Screen | P0 | NET-023/050; D-034 | B-03/B-12 | REQ-070/075 region; REQ-865 | BP-016 | Candidate / INHERITED |
| UR-025 | Report intake renders MOD-002 fields exactly and degrades per FR-001/006 | Screen | P0 | B-12 | B-12 | REQ-821/822 | — | Candidate / INHERITED |
| UR-026 | Decision/appeal views render the EVD-009 claim vocabulary and MOD-013 never-blocked route | Screen | P0 | B-12 | B-12 | REQ-826/833/848 | — | Candidate / INHERITED |
| UR-027 | Privacy/security settings expose the class list (PRV-009) and never class-SEC content | Screen | P0 | PRV-014 | B-12 | REQ-801–804 | — | Candidate / INHERITED |
| UR-028 | Admin surfaces sit behind a role-gated separate root; no admin information appears in player chrome | Permissions | P0 | D-042; ADM-021/022 | B-12 | REQ-865 region | DR-018 | Candidate / INHERITED |
| UR-029 | The notification system presents (never creates) events; mutes respect non-opt-out rules (DIP N-series) | Navigation | P0 | REQ-731 | all | REQ-731; AN-01…16 | DR-023 | Candidate / INHERITED |
| UR-030 | Global Trade screens are absent (not stubbed) until their gate evidence passes; no statistic leaks early | Screen | P0 | D-117; G-1…G-6 | B-07 | REQ-513 | — | Candidate / INHERITED |
| UR-031 | One table grammar project-wide: header, filter row, saved views, range pagination with honest totals | Interaction | P1 | BP-004 | all | MKT-065 | FND-004/024 | Candidate / Category B |
| UR-032 | Object identifiers anywhere render as links with peek previews subject to visibility class | Navigation | P1 | PR-13 | all | — | FND-001 | Candidate / Category B |
| UR-033 | Modals are used only for confirm/block/explain; every modal state has a page-reachable equivalent | Interaction | P1 | §5.3 discipline | all | — | FND-026 | Candidate / Category B |
| UR-034 | Search offers jump-to-object and jump-to-screen only; no full-text corpus is promised | Navigation | P2 | OQ-005 | all | — | — | Candidate / PROVISIONAL (C) — test at 13B journey count |
| UR-035 | Every screen defines loading/empty/error/permission-denied/suppressed states from the shared state set | States | P0 | §6 states | all | — | BP-024 | Candidate / Category B |
| UR-036 | Failure displays quote the owning system's failure code family (WPF/DPF/WRF/MKF/ALF/AT/FR) translated to player language | States | P0 | catalogues | all | WRF gaps D-143; TR-075/080 | DR-019 | Candidate / INHERITED |
| UR-037 | PROVISIONAL_BLOCK branches render as specified provisional states, labelled, never resolved silently | States | P0 | D-194 | B-12 region | — | — | Candidate / INHERITED |
| UR-038 | Time-sensitive displays use turns + UTC boundary; wall-clock countdowns are cosmetic only | Shell | P0 | cadence | B-02 | — | PR-01 | Candidate / Category B |
| UR-039 | History browsing respects D-026 class boundaries and labels them | Data | P1 | D-026 | chronicle | — | BP-019; DR-013 | Candidate / INHERITED |
| UR-040 | Cause-chain explanation ("why did it change") is reconstructible on every consequential settlement display | Data | P0 | Report 07 §15.6 | B-02/B-04/B-06 | ECV-001 lineage; DMP-073 | DR-007 | Candidate / INHERITED |
| UR-041 | Desktop/tablet/mobile layouts preserve UR-002/006/012/018/022 and the must-not-simplify list | Responsive | P0 | RD-07 | all | — | RD-02..08 | Candidate / Category B |
| UR-042 | Breakpoints in 13A are provisional exploration values; final values come from real-device testing on a production build | Responsive | P1 | RD-06 | all | — | SRC-035 | PROVISIONAL (C) — named test: Stage 5 device matrix |
| UR-043 | The design system uses semantic tokens; raw colours/sizes are banned in screen specs; brand values are owner inputs | Design system | P0 | §2.8 | all | — | OQ-001/002 | Candidate / Category B, values OWNER-RESERVED |
| UR-044 | Every screen names its governing B-section (rule anchor) on its surface | Traceability | P1 | DR-021 | all | roadmap B-09 para (generalized) | — | Candidate / Category B |
| UR-045 | Every Mandatory screen is reachable and act-capable within ≤3 navigational steps from Home on all device classes | Navigation | P1 | §5 audit | all | — | FND-023 | Candidate / PROVISIONAL (C) — test: 13B journey maps |
| UR-046 | Long-session ergonomics: density levels, sticky context, keyboard-first paths; no attendance-style reward affordances anywhere | Interaction | P2 | PR-14; AP-001 | all | — | FND-026 | Candidate / Category B |
| UR-047 | Localization-ready strings; no gameplay text baked into images | A11y | P2 | DS-15 | all | — | SRC-017 language widget | Candidate / Category B |
| UR-048 | UI performance budgets (payload, image sizes) must respect the ₹0 free-first constraint and Pages/Supabase limits; numbers belong to Stage 3/5 evidence | Technical | P1 | fixed constraint | infra | — | OQ-016 | Candidate / OWNER-STAGE (technical architecture input, not approved) |

### 2.2 Dependency and acceptance-intent ledger

| ID | Depends on | Acceptance intent (what must later be proven, and by whom) |
|---|---|---|
| UR-001 | architecture §4; routing (OQ-015) | 13B screen specs list the shell slots each screen uses; deep-link parity test at Stage 6+ |
| UR-002 | B-02 slot clock | 13B: every authenticated spec includes the countdown component; playtest comprehension check |
| UR-003 | every pending-act lifecycle (D-016/D-030/MKT/ALL/AT) | 13B journey maps show 100% of pending types in the Inbox with correct due ordering |
| UR-004 | TR-089; SYS-017 | 13B: digest content spec enumerates the cited event matrices; re-entry test on paper journeys |
| UR-005 | ECN-177/178; URB-152 | 13B component spec for number registers; adversarial read: no forecast styled as current |
| UR-006 | MKT-053 | 13B: every resource-bearing spec shows the triple; review checklist catches totals-only screens |
| UR-007 | 08C §12.7; ECN-181 | 13B: disabled-control matrix per screen with reason strings and rule links |
| UR-008 | RRL-006; WAR §12.3; 08C §12.3 | 13B: confirmation-content spec; on-paper first-session test (B-13 validation row) |
| UR-009 | DS-10 | Later automated a11y audit on the built UI (Stage 8+); 13B lint rule list |
| UR-010 | DS-07 | Built-UI keyboard walkthrough at Stage 6+ |
| UR-011 | DS-12 | Built-UI screen-reader pass; 13B alt-panel spec per chart |
| UR-012 | D-027; TR-022 | 13B: suppression-state spec; SQL-visible disclosure test at Stage 5 proves server-side enforcement (UI mirrors it) |
| UR-013 | Stage-5 RLS/authority work (outstanding) | Security test suite at Stage 5+; UI cannot pre-empt it — obligation restated, not discharged |
| UR-014 | FO-013; REQ-041 | 13B Network-View spec + audit that no screen renders coordinates; negative text search in specs |
| UR-015 | AX-18; UD-047/UD-049 state | 13B isolation test matrix: which fields appear on board vs alliance screens |
| UR-016 | B-09 tax/ARL rules; UD-040/045/046 | 13B field-by-field spec vs roadmap dependency paragraph (checklist parity) |
| UR-017 | D-133; ALL-161..168 | 13B flow review: zero external hops in membership/coordination journeys |
| UR-018 | DMP-268/256 | 13B banner-component spec; political-state screenshot matrix on paper |
| UR-019 | WAR-085…088 | 13B: band-only components; review that no numeric strength leaks |
| UR-020 | WEP-324/325 | 13B standings spec with denominator+window fields |
| UR-021 | D-039/040; NAT-016 | 13B new-nation journey walkthrough in the real shell on paper |
| UR-022 | ONB-020/022 | 13B protection-state displays; block-moment copy review vs B-12 vocabulary |
| UR-023 | D-029/041 | 13B journey specs for recovery/closure; MSG register parity |
| UR-024 | NET-023/050; EVD-009 | 13B wording audit: no accusation, no technical exposure |
| UR-025 | MOD-002; FR-001/006 | 13B intake spec field parity with MOD-002; degraded-path design |
| UR-026 | MOD-013/017; EVD-009 | 13B notice/appeal templates incl. seven-element notice |
| UR-027 | PRV-009/014 | 13B settings inventory; negative check for class-SEC content |
| UR-028 | D-042; ADM-021/022 | Stage-5 role model; 13B admin-surface separation review |
| UR-029 | REQ-731; all matrices | 13B tier definition consuming only existing event IDs |
| UR-030 | G-1…G-6 evidence | Launch-posture review at gate time; absence-by-construction test in specs |
| UR-031 | BP-004 | 13B table-component spec; per-screen table inventory parity |
| UR-032 | PR-13 | 13B link-grammar checklist |
| UR-033 | overlays discipline | 13B modal/drawer register: every overlay has a page equivalent |
| UR-034 | OQ-005/009 | 13B journey count vs screen inventory decides whether jump-search is needed at all |
| UR-035 | state vocabulary | 13B per-screen state matrix completeness (all 11 states addressed or exempted with reason) |
| UR-036 | failure catalogues | 13B code→language map; parity check against WPF/DPF/WRF/MKF/ALF registers |
| UR-037 | D-194 | 13B: every PROVISIONAL_BLOCK branch's UI copy spec |
| UR-038 | B-02 cadence | 13B time-component spec (turns+UTC) |
| UR-039 | D-026 | 13B boundary-label rule in history components |
| UR-040 | Report 07 §15.6; ECV-001 lineage | 60-second comprehension test on paper journeys; live test at first playable |
| UR-041 | RD set | 13B per-screen responsive spec; device matrix at Stage 5+ |
| UR-042 | real devices | Stage-5 device matrix (named test); no claim now |
| UR-043 | owner brand decisions | 13B spec lint: token references only; palette adoption gated on OQ-001 |
| UR-044 | DR-021 | 13B anchor field per screen |
| UR-045 | journey maps | 13B step-count measurement per Mandatory screen |
| UR-046 | DP-002; AP-001 | 13B density/duplicate-view spec; anti-attendance review |
| UR-047 | DS-15 | Stage-5 build string extraction |
| UR-048 | Stage 3/5 measurements | Budget numbers from evidence, not from this register |

## 3. Dependency map (instruction §12 categories)

- **Inherited from existing systems:** UR-004…UR-030 largely restate B-02…B-12 disclosure/lifecycle rules for surfaces (origin column). No inherited rule is reworded into new behaviour; where a rule lacks a surface, the inventory adds the *surface duty*, never the rule.
- **New UI-specific:** shell composition (UR-001/002/038), Inbox aggregation (UR-003), table grammar + saved views (UR-031), overlay discipline (UR-033), state matrix completeness (UR-035), step-count target (UR-045), anchors (UR-044).
- **Cross-system:** UR-015 depends on B-09 AX-18 + B-10 WAR-148 + UD-047/UD-049 boundaries; UR-029 depends on every notification matrix (08C/16_/17_/19_/MSG); UR-016 depends on B-09 tax/ARL rules + UD-040/UD-045/UD-046 provisional branches.
- **Technical (Stage 5+):** deep-link routing + SSR-vs-shell decision (OQ-015), search infrastructure (OQ-005/UR-034), performance budgets (UR-048/OQ-016), client state staleness handling.
- **Security:** UR-013 depends on Stage-5 RLS/authority work already flagged outstanding (prototype `profiles` grant defect etc. — this pass changes nothing); no UI may soften a B-12/SEC rule.
- **Owner-reserved dependencies:** brand values (OQ-001/002), test/staging parity (OQ-003), UD-040/044/046/047/049 gates inside Alliance screens, UD-017 and the UD-052…060 set touching protection/appeal surfaces.

## 4. Open questions and design-decision frontier (13A-OQ-001…016)

Fields: question · why it matters · options · recommendation · risk · dependency · authority · status.

| ID | Question | Answerable by | Recommendation | Authority | Status |
|---|---|---|---|---|---|
| OQ-001 | Final visual identity (palette, logo, brand finish; direction A-vs-B chosen concretely) | owner (brand) | foundation stays direction-B (administration) pending owner; no values invented | **OWNER-RESERVED** | Open |
| OQ-002 | Typefaces and icon set | owner (brand) + 13B | tokens first; owner selects faces | **OWNER-RESERVED** | Open |
| OQ-003 | Whether NS ships a public test server like P&W (`13A-SRC-028`) | owner + hosting cost | defer; it is a Category A/D territory (infra/cost), not a UI decision | **OWNER** | Open |
| OQ-004 | 13B scope confirmation: screen-spec depth and component specs under this inventory | owner authorization | authorize 13B after this pass is reviewed | **OWNER** | Open |
| OQ-005 | Full-text search over rules/chronicle/help | technical architecture | keep to jump-search until content exists; revisit Stage 5 | Technical | Open |
| OQ-006 | Notification tier policy beyond REQ-731 single-channel rule (priority ladder) | independent design + playtests | 13B defines tiers over existing events only | Design (13B) | Open |
| OQ-007 | Whether the identity strip shows band values or exact values where legal | design reasoning + visibility rules | default bands with exact-value opt-in per rule allowance; 13B confirms | Design (13B) | Provisional |
| OQ-008 | Desktop context-panel default content per section | design reasoning | section-specific defaults in 13B | Design (13B) | Open |
| OQ-009 | Search corpus feasibility | technical architecture | see OQ-005 | Technical | Open |
| OQ-010 | Any future intelligence/espionage surface | **game-design rule decision first** (B-10 excludes espionage) | keep `SCR-068` as placeholder-only; no screens without rules | Design rule (future prompt) | Open |
| OQ-011 | Global Trade UI activation | gate evidence G-1…G-6 | build screen specs only in parallel with gate evidence; absent until MET | Evidence + owner launch posture | Open (gate NOT MET) |
| OQ-012 | Favorites/pins privacy/abuse implications (targeting aids?) | fair-play review | treat as abuse-surface review item before any build | B-12 linkage | Open |
| OQ-013 | Dark mode | owner brand + design | deferred; token architecture preserves the option | Owner (later) | Open |
| OQ-014 | User-selectable mobile/desktop rendering mode (CN pattern `13A-SRC-029`) | real-device evidence | provisional; decide at Stage 5 device matrix | Technical + design | Provisional |
| OQ-015 | Routing model (URL-per-screen guarantees, shared-link permissions) | Stage 5 architecture | 13A fixes the *duty* (PR-13/UR-001), Stage 5 fixes the mechanism | Technical | Open |
| OQ-016 | Performance envelope under ₹0 constraint | Stage 3/5 measurement | UR-048 states the duty; no numbers claimed | Technical + owner cost posture | Open |

## 5. Acceptance-gate register P13A-01…24

| ID | Area | Result | Evidence / limitation |
|---|---|---|---|
| P13A-01 | Research scope compliance | **PASS** | research doc §2/§4: only genre-qualifying titles; §2's prohibited-category paragraph; no off-category convention used |
| P13A-02 | P&W primary benchmark completeness | **PASS** | research doc §10.1: 33 of the 36 numbered rows are P&W — the 28 primary rows split 21 `OBSERVED` live public-interface reads + 2 `DOCUMENTED` official-documentation reads + 5 `NOT-RETRIEVABLE` rows, plus the 5 registered boundaries `13A-SRC-032…036`; coverage A–H (instruction §4.1) with inaccessible areas registered, not skipped silently |
| P13A-03 | P&W evidence & source traceability | **PASS** | every finding cites SRC rows; SRC rows carry URL + date + evidence class; no login-gated behaviour invented (D-199) |
| P13A-04 | Supplementary relevance & restrictions | **PASS** | CN (`13A-SRC-029`: mobile-mode gap + activity-log/density lessons), eRepublik (`13A-SRC-030`: entry corroboration only), NationStates (`13A-SRC-031`, 403) recorded; no displacement of P&W (§4 of the research register) |
| P13A-05 | Independent design reasoning | **PASS** | BP register retains/adapts **rejects** 4 patterns including load-bearing ones (map, Discord-first membership); DR-001…024 are NS-reasoned, five of them corrections *against* the benchmark |
| P13A-06 | Existing game-system coverage | **PASS** | inventory rows trace to B-02…B-12 rule families; the Explore-mapped surface obligations (07C list, 08C six views, DMP-256 seven surfaces, WPC-14 six surfaces, roadmap B-09 paragraph, B-12 intake/appeal) all present as `SCR-` rows |
| P13A-07 | UI design principles | **PASS** | PR-01…16 + visual-direction evaluation of four candidate directions with reasoned recommendation; brand values untouched |
| P13A-08 | UI architecture | **PASS** | shell A–H defined; admin separated; states table 13 entries mapped to existing vocabularies |
| P13A-09 | Navigation architecture | **PASS** | 8-section model, secondary/contextual/breadcrumb/tab/drawer/modal/search rules with rationale vs benchmark |
| P13A-10 | Master screen inventory | **PARTIAL** | 100 screens × 13 documented fields complete; two mandated fields are compressed in some rows (secondary actions folded into primary+actions cells; existing requirement identifiers given at rule-family level where a single REQ id is ambiguous) — 13B must expand field-by-field before screen specs are accepted |
| P13A-11 | Screen hierarchy | **PASS** | mermaid hierarchy + cross-system transition table + §5 quality audit against the instruction's seven named risks |
| P13A-12 | Desktop requirements | **PASS** | RD-02; hover-not-load-bearing; multi-panel; keyboard mandate |
| P13A-13 | Tablet requirements | **PASS** | RD-03; column priority; pinned identity column |
| P13A-14 | Mobile requirements | **PASS** | RD-04/07/08; same-rules guarantee §1.1; must-not-simplify list; breakpoints explicitly provisional (RD-06), not owner-approved |
| P13A-15 | Design-system foundations | **PASS** | DS-01…15 + component-family register + state matrix + info-viz anti-misleading rules; deliberately not a component spec (13B boundary kept) |
| P13A-16 | UI requirement traceability | **PASS** | UR-001…048 twelve-field register with origin/system/existing-link columns; no duplicate identifiers; no global REQ allocated |
| P13A-17 | Dependency identification | **PASS** | §3 seven dependency classes identified including technical/security/owner |
| P13A-18 | Open questions & owner decisions | **PASS** | OQ register §4 with seven buckets (research/ supplementary/ design/ technical/ owner/ future-gameplay/ production) encoded in the Answerable-by column; nothing force-closed; D-014 preserved; **no owner-reserved UD/OSQ touched** |
| P13A-19 | Research evidence integrity | **PASS** | evidence-class vocabulary on all rows; limitations §10 of research doc; retrieval method §1.4 disclosed; no screenshot or unverified interaction claimed |
| P13A-20 | AI handoff synchronization | **PASS** | `AI_CONTEXT.md`, `AI_HANDOFF.md`, `PROJECT_PROGRESS.md`, `ROADMAP.md`, `stage-2/00`, `01`, `02`, `03` (dated note), `04`, `05` (untouched rows), `06` §87, prompt archive/index — all record 13A + owner's 12C acceptance; verified by `validate_final.py` and `test_next_action.py` runs (execution record in §7) |
| P13A-21 | Roadmap/progress-log consistency | **PASS** | STATUS blocks agree (`stage_2_next_prompt: 13B`; `decisions_range: D-001..D-205`); log §87 + roadmap row 13 + outline §5 next-prompt row aligned |
| P13A-22 | Documentation & identifier integrity | **PASS** | new families contiguous (`13A-SRC-001…036`, `FND-001…040`, `BP-001…028`, `DR-001…024`, `SCR-001…100`, `UR-001…048`, `OQ-001…016`, `P13A-01…24`); no collision with existing namespaces (checked repo-wide); links resolve (`validate_links.py`, `13A_validate_ui_foundations.py`) |
| P13A-23 | Governance preservation | **PASS** | §6 checklist: D-014 untouched; 12A 7 PARTIAL, 12B 23/3, `P12B-14/16/23` PARTIAL, 12C 16/2/2, R7/12B-C1/R8-D statuses and security obligations re-verified unchanged; no mechanics/formula/schema/implementation touched; no owner decision manufactured; new decisions D-198…205 are Category B/C only with owner-reserved items kept open |
| P13A-24 | Final documentation validation | **PASS** | suites actually run on the final tree — commands and real counts in §7; known R8-era validator limitations disclosed, not concealed; the 13A validator's own limits stated |

**Tally: 23 PASS / 1 PARTIAL / 0 FAIL / 0 BLOCKED.** (No gate is graded BLOCKED because no gate depended on an outstanding obligation this pass promised to discharge and could not; P13A-10's PARTIAL is a completeness finding owned by 13B.)

## 6. Governance preservation checklist (§6 of this doc = gate P13A-23 evidence)

| Item | Position before | Position after this pass |
|---|---|---|
| D-014 autonomous policy | Confirmed v1.0 | unchanged; used as the decision mechanism for D-198…D-205 |
| Prompt 12A gates | 15 PASS / 7 PARTIAL | untouched; re-asserted in status blocks |
| Prompt 12B acceptance | 23 PASS / 3 PARTIAL (`P12B-14/16/23`) | untouched |
| 12B-C1 | NOT CLOSED | untouched, still NOT CLOSED |
| R7 | implemented, independent acceptance NOT ACCEPTED, five residual weaknesses unfixed | untouched, same wording carried |
| R8 | DEFERRED BY OWNER | untouched; this pass adds no validator hardening beyond its own new focused validator (D-205 precedent D-196) |
| Prompt 12C | complete (log §85/§86); owner acceptance GRANTED per the Prompt 13A instruction — recorded in all continuity files with attribution to the instruction, not invented | recorded; 16 PASS / 2 PARTIAL / 2 BLOCKED tally and 378 specifications stand |
| Production security obligations (0005 migration, restricted UPDATE, SQL tests, audit trigger, tamper-evident audit, digest job) | outstanding, disclosed | still outstanding; this pass implemented nothing and claims nothing |
| Game rules/formulas/mechanics | as accepted | **zero changes** — no `F-` formula, no rule line, no requirement row of any system altered |
| Existing files | — | only additive/dated-synchronization edits to governance and register documents; no deletions; Git used for status inspection only, no staging/committing/pushing/resetting |

## 7. Validation execution record

Executed after every edit, on the final tree, across the 2026-11-11/2026-11-12 boundary; every figure is copied from the console output of the named command and none is quoted from a register. The full sweep, including the adjacent prompt families, is [progress log §87.5](../06_stage_2_progress_log.md).

| Command | Result as printed |
|---|---|
| `python docs/qa_backups/validate_final.py` | `VALIDATION: ALL CHECKS PASSED` |
| `python docs/qa_backups/validate_links.py` | 103 files, 4,035 links, 3,653 checked locally, 382 external skipped, 29 anchors, `Unresolved: 0` |
| `python docs/qa_backups/test_next_action.py` | `Ran 27 tests … OK` |
| `python docs/qa_backups/test_decision_registers.py` | `Ran 12 tests … OK` |
| `python docs/qa_backups/12B_validate_b12.py` | `CHECKS: 87/87 passed; 0 failed` — its code is untouched by 13A |
| `python docs/qa_backups/12C_validate_fair_play_workflows.py` | `CHECKS: 24/24 passed; 0 failed` — unchanged, and it still reports that no `FPA-` specification has been implemented or executed |
| `python docs/qa_backups/12A_validate_foundations.py` | `CHECKS: 45/45 passed; 0 failed`; register line `D=205 DD=253 UD=60 REQ max=869` (its check 31 family constant was advanced with the frontier; the agreement rule itself is unchanged) |
| `python docs/qa_backups/13A_validate_ui_foundations.py` | `CHECKS: 32/32 passed; 0 failed` |
| `python docs/qa_backups/13A_validate_ui_foundations.py --self-test` | `SELF-TEST: 14/14 seeded defects detected` |
| `python docs/qa_backups/11A_validate_research.py` | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — check 29's frozen `REQ-703` frontier; recorded debt since 12A §32, not repaired here |

`P13A-24` grades this sweep; the gate is `PASS` because the commands above were run on the final tree and their printed results are what this section records. The frontier-constant refreshes this pass made in the other checkers, and the reason each is legitimate rather than a manufactured pass, are itemised in [progress log §87.5](../06_stage_2_progress_log.md).

Known historical limitation, disclosed rather than hidden: the R8-era audit recorded five bypass classes in the retained validator family; no validator here (including this pass's own) is claimed immune to adversarial bypass — they are document-QA tools, never acceptance evidence (D-014 §5 discipline).

## 8. Provenance and handoff to Prompt 13B

13B must: (a) read all four 13A companions plus the [research register](13A_politics_and_war_ui_research.md) limitations; (b) expand each Mandatory screen into full field-by-field specifications, resolving the P13A-10 PARTIAL; (c) allocate the B-13 requirement block from `REQ-870`; (d) honour every `OWNER-RESERVED`/`PROVISIONAL` row — none may be silently decided; (e) verify the five rejected/limited benchmark assumptions where NS needs equivalent behaviour; (f) produce the B-13 canonical document at the path fixed by **D-198**. Nothing in 13A authorizes 13B; explicit owner authorization is required (D-002).
