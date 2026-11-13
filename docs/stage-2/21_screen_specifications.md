# B-13 companion — Complete screen specifications (SCR-001…SCR-100)

**Parent:** [B-13](21_interface_and_player_journeys.md) (authority, registers, navigation model, matrices and requirements).
**Created:** 2026-11-13 (Prompt 13B). **Status:** specification only; no screen, component, route or behaviour exists.
**Method:** every screen uses the eleven-field template A–K fixed by D-208. Field I uses the presentation patterns `P-DASH`, `P-REG`, `P-OBJ`, `P-TASK`, `P-STATE`, `P-GUIDE` defined in the parent §8.1. Components are referenced by `UI-CMP-` identifier and specified only in [the component companion](21_component_specifications.md). Tokens are semantic only (D-203). No field may assert a rule that B-02…B-12 does not own; governing references are exact identifiers.

**Reading rules.** (1) The parent's Matrix A is authoritative for classification and status. (2) A Conditional or Provisional screen's *absence duty* is part of its specification. (3) "Player can" means "the server would permit the action under the governing rule"; the specification does not grant permission. (4) Every committing control carries `OVL-01`; every disabled control carries `OVL-03`; every object identifier carries `UI-CMP-027`/`OVL-05`.

---

## 1. Public and account experience — SCR-001…SCR-012

### SCR-001 — Landing / public introduction

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public**; category `Public entry`; governing **B-03**; related existing requirements `REQ-070` family; new requirement `REQ-870`; class **Mandatory**; audience unauthenticated visitor; permissions none; visibility public. |
| **B Purpose** | Introduces the fictional world and the browser game, and routes a visitor to registration or login without exposing any player's data. It solves "what is this and how do I start" and supports exactly one decision: enter or leave. |
| **C Entry and navigation** | Reached by any unauthenticated URL. Destinations: registration `SCR-002`, login `SCR-003`, rules/terms/privacy, public guide excerpt `SCR-078`. Return: none (root). No authenticated data, no dashboard preview with real values. |
| **D Information hierarchy** | 1) Premise and start/login actions. 2) What the game is (nation administration, economy, diplomacy, war, progression) in short factual sections. 3) Browser-only and cadence statement. 4) Public rules/terms/privacy links. 5) A fictional-world statement and the multi-account policy notice. 6) Full rules/guide behind `SCR-078`. |
| **E Layout** | `P-GUIDE`. Public reduced shell: brand area, start/login, premise, four feature sections, fictional-world statement, terms/privacy, language selector placeholder. No identity strip, no treasury, no player counts. |
| **F Data presentation** | • Game name and premise — static text, no time reference, public. • Feature summaries — static text, public, no live numbers. • Cadence statement — "turns every two hours UTC", public, no countdown because no session. • Aggregate player counts — **not shown** (k=5 and no need). • Version/change link — public dated record via `SCR-088`. |
| **G Controls** | • `Start Playing` — link to `SCR-002`; public; read-only navigation. • `Login` — link to `SCR-003`. • `Rules`, `Terms`, `Privacy` — links to public documents; no account required. No other control exists. |
| **H Screen relationships** | `SCR-002` registration; `SCR-003` login; `SCR-078` public guide; `SCR-088` change disclosures; `SCR-001` is the marketing and entry surface, not the world catalogue. |
| **I Responsive** | Desktop: two-column premise/actions with feature sections beneath. Tablet: single column, actions above the fold. Mobile: single column, start action first, sections accordion; footer links remain; no horizontal scroll. |
| **J Governing references** | Governing: B-03 ACC entry; D-007 brand rule. Supporting: `13A-SRC-001`, `13A-BP-001`, `13A-PR-08`. Research inspiration: `13A-SRC-001` only. Decisions: D-007, D-201, D-203. |
| **K Restrictions and notes** | Brand values (palette, logo, typeface) are owner-reserved (`13A-OQ-001/002`); this screen specifies structure only. No live-player count, testimonial, fabricated activity or urgency device. No account is created here. |

### SCR-002 — Registration

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public**; category `Transactional flow`; governing **B-03**; related `REQ-070` family; new `REQ-871`; class **Mandatory**; audience unauthenticated visitor; permissions none; visibility public. |
| **B Purpose** | Creates the account identity and records policy consent. It solves "how do I get an account safely" and supports the decision to register, without creating a nation yet. |
| **C Entry and navigation** | From `SCR-001`. Destinations: `SCR-003` login, `SCR-004` reset, `SCR-006` verification after success, then `SCR-007` nation creation only after verification. Return: `SCR-001`. |
| **D Information hierarchy** | 1) E-mail, confirm e-mail, password and terms acknowledgement. 2) The multi-account policy notice at entry. 3) Optional referrer display. 4) Verification expectation ("you will verify before creating a nation"). 5) Field-level validation. 6) Rules/privacy links. |
| **E Layout** | `P-TASK`. Public shell, single form card: heading, policy notice, fields, terms checkbox, primary create action, login/reset links, validation summary. |
| **F Data presentation** | • E-mail — personal, current input, not displayed after submission except masked confirmation. • Referrer — public identity if supplied, no private data. • Account state — derived `REGISTRATION_PENDING`/`UNVERIFIED`, shown as text. • Policy version — current, public. |
| **G Controls** | • `Create account` — committing; preconditions: valid e-mail pair, password policy, terms accepted; `OVL-01` plain confirmation (no destructive phrase); outcome account in `REGISTRATION_PENDING`/`UNVERIFIED`. • `Log in` / `Reset password` — navigation. • Terms checkbox — required; disabled submit explains why (`OVL-03`). |
| **H Screen relationships** | `SCR-001`; `SCR-003`; `SCR-004`; `SCR-006`; `SCR-007` only after verification. |
| **I Responsive** | Desktop: centred form, policy notice visible. Tablet: same. Mobile: single column, full-width fields, policy notice above the checkbox, submit in a sticky action region; no hidden terms. |
| **J Governing references** | Governing: B-03 ACC; D-029; D-032; D-018. Supporting: `13A-BP-014`; `13A-SRC-018`. Decisions: D-018, D-029, D-032. |
| **K Restrictions and notes** | No third-party login is specified (eRepublik evidence is not a rule). No nation fields here. No password, token or secret is displayed. Multi-account disclosure is mandatory at entry. |

### SCR-003 — Login

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public**; category `Public entry`; governing **B-03**; related `REQ-070`/`REQ-085` family; new `REQ-872`; class **Mandatory**; audience account holder; permissions none; visibility public reduced shell. |
| **B Purpose** | Authenticates an existing account and routes to the account's own surfaces. It solves "return to my game" and supports login, reset and recovery entry. |
| **C Entry and navigation** | From `SCR-001`, session expiry, or a direct URL. Destinations: `SCR-002`, `SCR-004`, `SCR-005`, and on success the Home Command Digest `SCR-013` or the pre-nation path `SCR-007` if no nation exists. Return: `SCR-001`. |
| **D Information hierarchy** | 1) Credentials. 2) Keep-session option and reset/recovery links. 3) Account-state message after a failed or restricted login (`UNVERIFIED`, `TEMP_RESTRICTION`, `SUSPENDED`, `RECOVERY_LOCKED`) in neutral wording. 4) Language selector placeholder. 5) Help link. |
| **E Layout** | `P-TASK`. Reduced public shell; form card with e-mail, password, keep-session, primary login, reset/recovery links. No treasury, nation name or other player's values. |
| **F Data presentation** | • Credentials — never echoed. • Session state — current, shown only as "signed in" after success. • Account state — neutral text on failure; `ACC-018` wording. • Cadence — public statement in footer, no live countdown before auth. |
| **G Controls** | • `Log in` — committing; preconditions: credentials; outcome session or neutral failure. • `Forgot password?` → `SCR-004`. • `Use a recovery code` → `SCR-005`. • `Keep me signed in` — optional toggle. |
| **H Screen relationships** | `SCR-013` on success; `SCR-007` when no nation; `SCR-004`; `SCR-005`; `SCR-002`. |
| **I Responsive** | Desktop: centred form. Tablet: same. Mobile: single column, large touch targets, password reveal as an accessible toggle, no auto-zoom, submit full width. |
| **J Governing references** | Governing: B-03 ACC-018; D-041. Supporting: `13A-SRC-017` (frame persistence lesson, bounded). Decisions: D-029, D-041, D-201. |
| **K Restrictions and notes** | The shell may show the **frame**, never another player's data, and never real treasury values at zero-state as if authenticated. Failed login does not disclose whether the e-mail exists. |

### SCR-004 — Password reset initiation

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public**; category `Transactional flow`; governing **B-03**; related `REQ-085` family; new `REQ-873`; class **Mandatory**; audience account holder; permissions none; visibility public. |
| **B Purpose** | Starts the account-recovery route without disclosing account existence. It solves "I cannot sign in" and supports requesting a reset and understanding what happens next. |
| **C Entry and navigation** | From `SCR-003` or `SCR-001`. Destinations: `SCR-005` recovery-code entry, `SCR-003` login, `SCR-006` if verification is the blocker. Return: `SCR-003`. |
| **D Information hierarchy** | 1) E-mail field. 2) Neutral submission result ("if an account exists, a reset message will be sent"). 3) Recovery-code alternative. 4) Security note (no account creation, no password disclosure). 5) Support link. |
| **E Layout** | `P-TASK`. Public shell; form card with e-mail, submit, recovery alternative, neutral result panel. |
| **F Data presentation** | • E-mail — input, never echoed back in full. • Request state — pending/neutral, current. • Reset expiry — described in turns/UTC if the rule states it; no invented duration. • No account-existence flag. |
| **G Controls** | • `Send reset` — committing but non-mutating account state; neutral result regardless of existence. • `Use recovery code` → `SCR-005`. • `Back to login` → `SCR-003`. |
| **H Screen relationships** | `SCR-003`; `SCR-005`; `SCR-006`. |
| **I Responsive** | Desktop/tablet: centred card. Mobile: single column, full-width field and action, neutral result readable without scrolling. |
| **J Governing references** | Governing: B-03; D-041. Supporting: `13A-SRC-017` link pattern. Decisions: D-041. |
| **K Restrictions and notes** | Recovery never creates an account. The screen must not become an account-enumeration oracle. |

### SCR-005 — Recovery-code entry

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public**; category `Transactional flow`; governing **B-03**; related `REQ-085`/`REQ-089` family; new `REQ-874`; class **Mandatory**; audience account holder; permissions none; visibility public. |
| **B Purpose** | Consumes a single-use recovery code to restore access when the normal route is unavailable. It solves "I lost access but hold a code" and supports exactly one decision: use one code. |
| **C Entry and navigation** | From `SCR-003`/`SCR-004`/`SCR-080`. Destinations: `SCR-003` on success, `SCR-080` after auth to view remaining-custody guidance, `SCR-004` alternative. Return: `SCR-003`. |
| **D Information hierarchy** | 1) Code field. 2) Single-use warning. 3) Remaining-code custody guidance (not the codes themselves). 4) Result state (accepted/rejected/expired). 5) Support link if all codes are lost. |
| **E Layout** | `P-STATE`. Public shell; code form, single-use notice, result banner, next-step links. |
| **F Data presentation** | • Code — input only, masked, never displayed after use. • Code state — unused/used/expired, current. • Remaining count — shown only as a count, never values. • Account state — neutral. |
| **G Controls** | • `Use code` — committing; precondition unused code; confirmation explains single-use; outcome access restored or neutral rejection. • `Back` → `SCR-003`. |
| **H Screen relationships** | `SCR-003`; `SCR-004`; `SCR-080`. |
| **I Responsive** | Desktop/tablet: centred form. Mobile: numeric-friendly field where applicable, full-width action, result banner above the fold. |
| **J Governing references** | Governing: B-03; D-041; ACC-031. Decisions: D-041. |
| **K Restrictions and notes** | Codes are displayed once at generation and stored only as hashes; no surface may re-display a code or list unused codes. |

### SCR-006 — E-mail verification / pending state

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public**; category `Status/state`; governing **B-03**; related `REQ-085` family; new `REQ-875`; class **Mandatory**; audience unverified account holder; permissions none; visibility public. |
| **B Purpose** | Shows the unverified state and the verification route, and explains what is blocked until verification. It solves "why can I not play yet" and supports resend or correction. |
| **C Entry and navigation** | From `SCR-002`, an unverified login, or a verification link. Destinations: `SCR-003`, `SCR-007` after verification. Return: `SCR-003`. |
| **D Information hierarchy** | 1) Verification state. 2) The blocked capabilities (`UNVERIFIED` cannot create/control a nation, trade, post or hold office). 3) Resend action and its limit. 4) Change-e-mail route if the address is wrong. 5) Support link. |
| **E Layout** | `P-STATE`. Public shell; state banner, explanation list, resend action, change-address link. |
| **F Data presentation** | • Account state `UNVERIFIED`/verified — current, text label. • Masked e-mail — personal, current. • Resend availability — current with limit. • No token value. |
| **G Controls** | • `Resend verification` — available subject to the rule's limit; disabled with reason when exhausted. • `Change e-mail` — navigates to the account-security route after auth or the registration correction path. • `Log in` — navigation. |
| **H Screen relationships** | `SCR-002`; `SCR-003`; `SCR-007`; `SCR-080`. |
| **I Responsive** | Desktop/tablet: state card. Mobile: state first, resend in the action region, masked e-mail readable. |
| **J Governing references** | Governing: B-03; D-029; ACC-024. Decisions: D-029. |
| **K Restrictions and notes** | Verification is a gate, not a penalty; wording must not imply the account is suspect. No verification token in the DOM or copy. |

### SCR-007 — Nation creation

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public** (flow ends in Home); category `Transactional flow`; governing **B-03/B-04**; related `REQ-089`/`REQ-090` family; new `REQ-876`; class **Mandatory**; audience verified eligible account holder with no active nation; permissions verified account; visibility private until public profile exists. |
| **B Purpose** | Creates the player's nation identity and starting state. It solves "how do I enter the world" and supports the one-time decisions of name, short name, emblem and starting posture, with the D-038 naming rules and D-063 start state disclosed. |
| **C Entry and navigation** | From a verified account, `SCR-006`, or account home when eligible. Destinations: `SCR-008` onboarding, `SCR-013` digest, `SCR-015` overview. Return: `SCR-003`/`SCR-011` before creation. |
| **D Information hierarchy** | 1) Name and short name with live validation. 2) Emblem choice from the game set. 3) Starting posture. 4) Start-state summary (1,500 crowns, 50,000 people, 310 units, stated capacity — B-04 owns the values). 5) Naming rules and reserved-word feedback. 6) Confirmation. |
| **E Layout** | `P-TASK`. Public-to-authenticated transition: form with name/short name, emblem picker, posture selector, start summary panel, confirmation. |
| **F Data presentation** | • Nation name — player input, normalized NFC + fold, 3–32; public after creation. • Short name — `[A-Z0-9]{2,6}`, public. • Emblem — game-set choice, public. • Start values — current at creation, private until profile, sourced B-04. • Founding turn — historical from creation. • `awaiting first turn` state — current. |
| **G Controls** | • `Create nation` — committing; preconditions verified account, no active nation, valid unique name/short name; confirmation lists name, short name, emblem, posture, start state; outcome nation created, onboarding available. • Name/short-name fields — validation with neutral unavailable/reserved message. • `Cancel` — returns without creating. |
| **H Screen relationships** | `SCR-008`; `SCR-013`; `SCR-010` (public profile); `SCR-090` (reroll later). |
| **I Responsive** | Desktop: two-column form + start summary. Tablet: form above summary. Mobile: stepped single column, emblem grid touch-sized, summary before confirm, no accidental submit. |
| **J Governing references** | Governing: B-03/B-04; NAT-002/015/016/026–030; D-038; D-063. Supporting: `13A-SRC-001` entry funnel. Decisions: D-038, D-063. |
| **K Restrictions and notes** | No continent, region, territory, coordinates or map placement is requested (NAT-022). No uploaded image at first playable. Reserved-name rejection uses the same neutral message as unavailable. Government choice, if required by B-06 at creation, is a separate confirmed step and never defaulted. |

### SCR-008 — Onboarding guide (account-level, in real shell)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Guide/help`; governing **B-03**; related `REQ-089`/`REQ-090` family; new `REQ-877`; class **Mandatory**; audience newly created nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Guides the first session inside the real shell with true zero-state values, teaching the loop without a separate tutorial product. It solves "what do I do first" and supports completing the first-session steps without gating the game. |
| **C Entry and navigation** | Automatically after `SCR-007`; from `SCR-013` while incomplete; from the guide index. Destinations: `SCR-009`, `SCR-013`, `SCR-015`, each guided task's owning screen. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Current step and why it matters. 2) The real value or zero-state that step concerns. 3) The action and its outcome. 4) Progress through the one-time guide. 5) Skip (does not remove protection). 6) Rule links. |
| **E Layout** | `P-DASH`. Real shell with an onboarding panel above the primary digest; checklist, current step card, contextual link, progress. No stub UI, no fake values. |
| **F Data presentation** | • Step state — current, not started/complete. • Real national values — current or true zero, labelled. • Protection state — `protected until Turn N` where applicable. • Completion — one-time historical. |
| **G Controls** | • `Go to step` — navigation to the owning screen. • `Mark step done` only where the rule treats a view/action as completion; otherwise completion is server-derived and the control is absent. • `Skip guide` — dismisses the guide once; does not re-grant protection or reset state. |
| **H Screen relationships** | `SCR-009`; `SCR-013`; `SCR-015`; `SCR-089`; owning task screens. |
| **I Responsive** | Desktop: side panel + real digest. Tablet: panel above content. Mobile: step card first, one action, progress compact; skip reachable but not prominent. |
| **J Governing references** | Governing: B-03; D-040; ONB-009…038. Supporting: `13A-BP-001`, `13A-SRC-017`, `13A-PR-04`. Decisions: D-040. |
| **K Restrictions and notes** | Onboarding is one-time and never re-granted on reroll, recovery or replacement. The guide may not award a mechanic or bypass a rule. No attendance reward or streak. |

### SCR-009 — First-turn objectives entry

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Guide/help`; governing **B-03/B-11**; related `REQ-089`/`REQ-704–763`; new `REQ-878`; class **Mandatory**; audience new nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Presents the entry point to objectives and first-turn guidance without duplicating the full Objectives screen. It solves "what should I aim for first" and supports choosing a first objective and understanding it is optional. |
| **C Entry and navigation** | From `SCR-008`, the Home section, or `SCR-071`. Destinations: `SCR-071`, `SCR-008`, the owning screen of any objective condition. Return: `SCR-013`. |
| **D Information hierarchy** | 1) First-session guidance. 2) A small entry set of objective categories. 3) Optionality and penalty-free dismissal. 4) Progress and next step. 5) Full objectives link. 6) Definitions. |
| **E Layout** | `P-DASH`. Onboarding entry band, objective category cards, optionality notice, link to full Objectives. |
| **F Data presentation** | • Objective categories — `OBJ-FOLLOW`…`OBJ-LONG` names, public taxonomy. • State — available/accepted/progress. • Conditions — references to owning state, never action counts invented by UI. • Rewards — only where B-11 defines a class. |
| **G Controls** | • `View objectives` → `SCR-071`. • `Accept` only where the objective flow supports it; otherwise read-only. • `Dismiss` where penalty-free dismissal applies; outcome returns the item without forfeiture. |
| **H Screen relationships** | `SCR-071`; `SCR-008`; `SCR-013`; owning condition screens. |
| **I Responsive** | Desktop: three-card row. Tablet: two columns. Mobile: single column cards; optionality text never collapsed. |
| **J Governing references** | Governing: B-03/B-11; ONB surfaces; WEP-203…215. Supporting: `13A-BP-009`. Decisions: D-040, D-147. |
| **K Restrictions and notes** | No objective may require presence, group membership, spending or aggression. The UI does not create an objective, condition or reward. |

### SCR-010 — Public nation profile (12-section object page)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Public** (alias World); category `Object page`; governing **B-03/B-06/B-10/B-11**; related `REQ-070`/`REQ-704–763`; new `REQ-879`; class **Mandatory**; audience any viewer; permissions none for public fields; visibility public fields only, filtered by TR-021. |
| **B Purpose** | The central diplomatic object: identity, public relations, economy aggregates, domestic facts, military bands, standings and history. It solves "who is this nation, what is it like, how do I relate to it" and supports diplomacy/reporting/navigation. |
| **C Entry and navigation** | From any object link, search, Network View, standings, conflicts or reports. Destinations: `SCR-047` pair view, `SCR-062` conflicts, `SCR-069` events, `SCR-081` report, `SCR-053` alliance. Return: the entry list or the owning section. |
| **D Information hierarchy** | 1) Identity, status, alliance, protection badge, standing. 2) International relations summary. 3) Economic/domestic aggregates permitted. 4) Military bands and war record. 5) Historical charts with as-of turns. 6) Restricted/private fields explained as "not disclosed". 7) Report action. |
| **E Layout** | `P-OBJ`. Sticky section index; identity header; sections: Basic Information, International Relations, Economic, Domestic, Military, Standings, Activity, History, Wars, Treaties, Chronicle, Report. Progressive collapse. |
| **F Data presentation** | • Nation/leader names, short name, emblem — public. • Founding turn — historical. • Alliance — public membership. • Population/GDP/score — only where B-11/visibility permits; exact or band per rule. • Protection — state and end turn, visibility-only. • Military — bands only. • Breach count — public fact, no score. • Charts — public aggregates with k=5. • Never: e-mail, account ID, IP, recovery/enforcement state, pair restriction. |
| **G Controls** | • `Report this nation` → `SCR-081` (public intake). • `View diplomatic pair` → `SCR-048` when authenticated. • `View alliance` → `SCR-053`. • `Pin` only if `SCR-020` is enabled. • No private action (trade, attack, treaty) is initiated from a public page without its own permissioned screen. |
| **H Screen relationships** | `SCR-047`; `SCR-048`; `SCR-053`; `SCR-062`; `SCR-069`; `SCR-081`; `SCR-072`; `SCR-017` when the viewer owns the nation. |
| **I Responsive** | Desktop: section index + content + context panel. Tablet: section select + stacked panels. Mobile: accordion sections, identity first, standings and protection visible without expanding, report action in the footer region. |
| **J Governing references** | Governing: B-03 NAT-015/RRL-020; B-06/B-10/B-11 public fields; TR-021/022; D-036. Supporting: `13A-FND-003`, `13A-BP-003`, `13A-DR-005`. Decisions: D-026, D-036, D-210. |
| **K Restrictions and notes** | The twelve-section structure mirrors the 13A inventory; it is not a claim that P&W's exact section list was observed authenticated. A retired nation shows `retired — rerolled`; a replacement is labelled `New nation` and does not inherit treaties or breach count. No raw network data ever. |

### SCR-011 — Account home

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Dashboard`; governing **B-03**; related `REQ-038`/`REQ-070`/`REQ-075`; new `REQ-880`; class **Mandatory**; audience account holder; permissions authenticated; visibility private. |
| **B Purpose** | The account-level hub: identity, nation linkage, security, privacy, restrictions and closure. It solves "manage my account, not my nation" and supports security and lifecycle decisions. |
| **C Entry and navigation** | Account menu from any authenticated screen. Destinations: `SCR-012`, `SCR-079`, `SCR-080`, `SCR-084`, `SCR-085`, `SCR-090`, `SCR-007` when no nation. Return: previous screen. |
| **D Information hierarchy** | 1) Account state and nation linkage. 2) Security summary (verification, sessions, recovery-code custody). 3) Privacy and data links. 4) Restrictions/status and appeal link. 5) Closure and reroll entries. 6) Support. |
| **E Layout** | `P-DASH`. Account identity card, state chip, action list, security/privacy panels, danger zone separated at the bottom. |
| **F Data presentation** | • Account state — one of the ten ACC states, text label, private. • Linked nation — name/short name, public identity. • Verification — verified/unverified. • Sessions — current count/summary, never tokens. • Recovery codes — custody count only. • Closure state — cooling period/end turn. |
| **G Controls** | • `Security settings` → `SCR-080`. • `Privacy centre` → `SCR-079`. • `My data` → `SCR-085`. • `Appeal` → `SCR-083` when a decision exists. • `Close account` → `SCR-012`. • `Reroll nation` → `SCR-090`. Delete/close controls are destructive-styled and separated. |
| **H Screen relationships** | `SCR-012`; `SCR-079`; `SCR-080`; `SCR-084`; `SCR-085`; `SCR-090`; `SCR-007`. |
| **I Responsive** | Desktop: two columns. Tablet: stacked. Mobile: state + nation first, action list; danger zone below a labelled separator; no accidental destructive tap. |
| **J Governing references** | Governing: B-03 ACC-017/018; D-041. Supporting: `13A-SRC-018`. Decisions: D-029, D-041, D-042. |
| **K Restrictions and notes** | No account ID, IP, raw enforcement record or another player's data. Restriction wording is neutral and never public. |

### SCR-012 — Account closure flow

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Transactional flow`; governing **B-03**; related `REQ-038`/`REQ-070`/`REQ-075`; new `REQ-881`; class **Mandatory**; audience account holder; permissions authenticated; visibility private. |
| **B Purpose** | Starts account closure with full consequence disclosure and a cooling period. It solves "how do I leave safely" and supports close or cancel without accidental loss. |
| **C Entry and navigation** | From `SCR-011`. Destinations: `SCR-011` cancel, `SCR-085` retention explanation, support `SCR-087`. Return: `SCR-011`. |
| **D Information hierarchy** | 1) What closure does and does not do. 2) The 7-day cooling period and its end turn. 3) Blocked offensive actions and bank transfers during closure, and that the nation can still be targeted. 4) Retention and what survives. 5) Confirmation. 6) Support alternative. |
| **E Layout** | `P-TASK`. Consequence panel, cooling-period state, irreversible-confirmation block, cancel path styled as the safe option. |
| **F Data presentation** | • Closure state — requested/cooling/closed, current. • End turn — current/target. • Retained records — by class, private. • Nation state — active/closure-requested. |
| **G Controls** | • `Request closure` — committing; preconditions account not already closing; confirmation with consequence list; outcome `CLOSURE_REQUESTED` and cooling period. • `Cancel closure` — available during cooling; outcome active again. • `Withdraw request` absent after `CLOSED`. |
| **H Screen relationships** | `SCR-011`; `SCR-085`; `SCR-087`; login/closure state surfaces. |
| **I Responsive** | Desktop: consequence list + confirmation. Tablet: stacked. Mobile: stepped confirmation with cooling-period explanation, full-width actions, destructive action separated. |
| **J Governing references** | Governing: B-03 D-041; ACC-043; D-026. Decisions: D-041, D-026. |
| **K Restrictions and notes** | Closure is not a shield; offensive actions and bank transfers are barred during cooling while the nation remains targetable. No hidden deletion of audit/permanent records. |

## 2. Main strategic interface — SCR-013…SCR-020

### SCR-013 — Command Digest (home)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Dashboard`; governing **B-02**; related `REQ-020`/`REQ-022`; new `REQ-882`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The default landing surface after login: a bounded summary of what settled since the player last looked and what needs them before the next boundary. It solves re-entry without requiring attendance and supports "read the situation, then act". |
| **C Entry and navigation** | Primary nav Home; post-login; from any alert. Destinations: Inbox `SCR-014`, Overview `SCR-015`, Turn status `SCR-016`, Alerts `SCR-019`, Chronicle `SCR-017`, and each cited object's owning screen. Return: none (Home root). |
| **D Information hierarchy** | 1) Since-last-look summary of settled changes with cause chains. 2) Pending totals and due-this-boundary items. 3) Turn and next boundary. 4) Priority alerts. 5) Quick national state. 6) Links to full history. |
| **E Layout** | `P-DASH`. Header: page title + as-of turn. Primary digest register (grouped rows, not a widget grid). Secondary: pending summary + turn strip. Supporting: alert tier and quick stats. Context panel: recent objects. |
| **F Data presentation** | • Digest rows — settled facts, one bounded row per nation per turn (TR-089), with cause and deep link; current/historical. • Pending totals — counts by type, current. • Due-boundary items — turns+UTC, current. • Quick stats — six-number-type labels, bands where visibility requires. • Alert tier — informational/pending/warning/danger. |
| **G Controls** | • Digest row — link to cited object; read-only. • `Open Inbox` — link. • `Dismiss` only where the owning event permits; non-opt-out items show no dismiss. • `View all alerts` → `SCR-019`. No committing action originates here. |
| **H Screen relationships** | `SCR-014`; `SCR-015`; `SCR-016`; `SCR-017`; `SCR-019`; all cited object screens. |
| **I Responsive** | Desktop: digest main column + context panel. Tablet: digest, then pending/turn stacked. Mobile: digest first, pending count and countdown pinned in the header band; each row expands inline; no widget carousel. |
| **J Governing references** | Governing: B-02 TR-088/089/092; REQ-022; REQ-731. Supporting: `13A-DR-001`, `13A-BP-018`, `13A-PR-06`. Decisions: D-201, D-210. |
| **K Restrictions and notes** | The digest consumes existing notification events only; it may not invent a new event, a new metric or an open widget board. Absence is allowed: an empty digest explains the last settlement and links the history. No streak/FOMO. |

### SCR-014 — Inbox / pending actions queue

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Register/list`; governing **B-02 + B-07…B-09**; related `REQ-022`; new `REQ-883`; class **Mandatory**; audience nation owner; permissions authenticated plus per-row permissions; visibility private. |
| **B Purpose** | One place where every pending action waits: offers, proposals, invitations, applications and confirmations, ordered by due boundary. It solves "what is waiting on me" and supports act/defer/cancel within each owning rule. |
| **C Entry and navigation** | Shell alert, digest, direct route. Destinations: the owning action screen for each row, `SCR-013`, `SCR-019`. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Rows due before the next boundary. 2) Other pending rows by due turn. 3) Type grouping and counterparty. 4) Current state and time remaining in turns. 5) Row-level permission and cancellation state. 6) History/filter. |
| **E Layout** | `P-REG`. Filter row (type, due, state), pending table/cards grouped by due boundary, row actions, empty state, exact pagination. |
| **F Data presentation** | • Action type — trade offer, proposal, invitation, application, confirmation; current. • Counterparty — public identity, only where the rule permits. • Due boundary — turns/UTC, current. • State — pending/countered/accepted/etc.; six-number/type label not applicable. • Cancellable — yes/no with rule reason. • Ownership — system + rule anchor. |
| **G Controls** | • Row link — opens owning screen. • `Cancel` only where the owning rule permits; confirmation and outcome per rule. • `Defer` only where a defer action exists; no invented snooze. • Filter and saved view. No bulk commit across systems. |
| **H Screen relationships** | `SCR-035`/`SCR-036`/`SCR-037` (trade); `SCR-049`/`SCR-050` (diplomacy); `SCR-054` (alliance applications); `SCR-067` (settlement); owning screens generally. |
| **I Responsive** | Desktop: full table. Tablet: priority columns + pinned row identity. Mobile: card per pending action, due boundary and state visible; actions in a row menu; exact counts retained. |
| **J Governing references** | Governing: TR-004; D-016; D-030; MKT/ALL/AT lifecycles; `UR-003`. Supporting: `13A-DR-001`, `13A-BP-018`. Decisions: D-211, D-213. |
| **K Restrictions and notes** | Pending diplomatic terms are visible only to named parties (D-030). Applicant identities are private to alliance administration (ALL-086). The Inbox does not grant a permission the owning screen would deny. |

### SCR-015 — National Overview dashboard

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Dashboard`; governing **B-04/B-05/B-06/B-10**; related `REQ-250`/`REQ-317–321`/`REQ-654–703`; new `REQ-884`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The integrated national situation: treasury, stability/approval, readiness, protection, population/housing and power. It solves "how is my nation doing" and routes each concern to its owning section. |
| **C Entry and navigation** | Home nav, digest, section back-links. Destinations: `SCR-029` treasury, `SCR-021` politics, `SCR-059` war, `SCR-041` cities, `SCR-089` protection, `SCR-023` approval. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Headline national state (six labelled registers). 2) Warnings and political banner. 3) Trends since last turn. 4) Supporting section links. 5) Historical comparison. 6) Definitions. |
| **E Layout** | `P-DASH`. Stat strip (treasury, stability/approval, readiness, protection, population/housing, power), political banner, warning panel, section cards, context panel. |
| **F Data presentation** | • Treasury — available/reserved/current position, crowns, current, private. • Stability/approval — integer bp + text label, current, private; no invented bands. • Readiness — own exact state or band where rule defines; private. • Protection — state/end turn, private. • Population/housing — current, private. • Power — supply/demand/surplus, current, private. |
| **G Controls** | • Each card links to its owning section. • `Open political panel` → `SCR-021`. • `View protection` → `SCR-089`. No committing action on the overview itself. |
| **H Screen relationships** | `SCR-029`; `SCR-021`; `SCR-023`; `SCR-041`; `SCR-059`; `SCR-089`; `SCR-013`. |
| **I Responsive** | Desktop: 3×2 stat grid + context. Tablet: 2×3. Mobile: stacked cards in priority order; treasury and political state first; each card retains units and as-of turn. |
| **J Governing references** | Governing: ECN-176/177; URB-052; DMP-073/268; B-10 readiness. Supporting: `13A-BP-026`, `13A-DR-005`. Decisions: D-210, D-212. |
| **K Restrictions and notes** | Exact values only where the viewer's class allows; public viewers use `SCR-010`. No aggregate "national score" (WEP-361/362). No invented stability bands. |

### SCR-016 — Turn & settlement status

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Status/state`; governing **B-02**; related `REQ-020`/`REQ-022`; new `REQ-885`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Answers "what turn is it, when is the boundary, where are my orders, and did the last settlement succeed". It solves timing uncertainty and supports deciding whether to act now or next turn. |
| **C Entry and navigation** | Shell countdown, digest, Home nav. Destinations: `SCR-014` queued actions, `SCR-019` alerts, owning screens of queued actions. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Current turn and next boundary UTC. 2) Turn state (`OPEN`/`LOCKED`/`RESOLVING`/`COMPLETED`/`INTERRUPTED`/`FAILED`). 3) This nation's queued actions and target phase. 4) Last settlement summary and reason. 5) Historical turn log. 6) Definitions of phases. |
| **E Layout** | `P-STATE`. Turn clock panel, state banner, phase ladder, queued-actions table, last-settlement panel, history. |
| **F Data presentation** | • Current turn — display turn and UTC window, current. • Boundary — UTC time and turns remaining, current. • Phase position — P0–P7 label, current. • Queued actions — pending, target phase. • Last settlement — completed/interrupted/failed, historical, with cause. • `unknown — retrying` — current state when the client cannot confirm. |
| **G Controls** | Read-only. • `View queued action` — link. • `View alerts` — link. No cancel or resubmit is offered here; cancellation lives on the owning action. |
| **H Screen relationships** | `SCR-014`; `SCR-019`; owning action screens; admin `SCR-097` is separate and not linked to players. |
| **I Responsive** | Desktop: clock + phase ladder + table. Tablet: stacked. Mobile: turn and boundary pinned at top, state banner, queued list; no countdown theatrics. |
| **J Governing references** | Governing: TR-024/027/030/031/033/035/036/039/075/080. Supporting: `13A-PR-01`, `13A-DR-002`. Decisions: D-210. |
| **K Restrictions and notes** | `PENDING` is a display label for `ACCEPTED`, not a new state. A `FAILED` turn is a delay, not a lost turn; accepted actions remain pending and no cost is charged unless the turn completes (TR-080). |

### SCR-017 — National Chronicle (history browser)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home** (alias World); category `Register/list`; governing **B-11/B-02**; related `REQ-704–763`; new `REQ-886`; class **Mandatory**; audience nation owner; permissions authenticated; visibility class-P private, public entries where disclosed. |
| **B Purpose** | The permanent national history stream: settlements, decisions, wars, treaties, elections and milestones. It solves "what has my nation done" and supports auditing and nostalgia without exposing restricted facts. |
| **C Entry and navigation** | Home nav, digest, overview, World chronicle cross-link. Destinations: cited object screens, `SCR-076` world chronicle, `SCR-010` public profile. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Reverse-chronological permanent entries. 2) Turn and event class. 3) Cause and outcome. 4) Public/restricted label. 5) Filters by type and turn range. 6) Export/share where permitted. |
| **E Layout** | `P-REG`. Filter row (class, turn range, public/private), timeline/list, entry detail drawer, exact pagination. |
| **F Data presentation** | • Entry — class-P record, historical, permanent. • Turn — historical. • Participants — public identities. • Outcome — settled fact or pending state. • Public/restricted — label; restricted content not rendered. • Retention — permanent/hot class label. |
| **G Controls** | • Filter/saved view. • `Open object` — link. • `Export` only where an export duty exists; never export restricted content. • No delete or rewrite control. |
| **H Screen relationships** | `SCR-076`; `SCR-010`; object screens; `SCR-075` rewards; `SCR-066` military history. |
| **I Responsive** | Desktop: table/timeline + context. Tablet: priority columns. Mobile: card list with turn and class visible; filters in a drawer. |
| **J Governing references** | Governing: B-11 chronicle; D-026; TR-049. Supporting: `13A-BP-024`, `13A-DR-020`, `13A-FND-019`. Decisions: D-026. |
| **K Restrictions and notes** | No silent history rewrite. Restricted entries are absent or labelled, never inferred through counts. A retired page keeps its public record; the replacement does not inherit it. |

### SCR-018 — Network View (mapless world surface)

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Dashboard`; governing **B-02/B-08/B-09**; related `REQ-041`; new `REQ-887`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility published relations only. |
| **B Purpose** | The world-situational surface: who is connected to whom, by what relation, and what changed. It replaces a geographic map with a typed relationship graph. |
| **C Entry and navigation** | World nav, overview, profile links. Destinations: `SCR-010` nation, `SCR-053` alliance, `SCR-047` diplomacy, `SCR-048` pair. Return: `SCR-069` or entry surface. |
| **D Information hierarchy** | 1) Selected node/edge and its typed relations. 2) Filters and legend. 3) Related object list. 4) Relation changes within retention. 5) Protection/restriction/suppression warnings. 6) Edge provenance. |
| **E Layout** | `P-DASH`. Graph canvas or list-first view; filter row; legend; selected-node context panel; object list. No map, coordinates or geography labels. |
| **F Data presentation** | • Nation node — public identity, alliance, protection state if disclosable. • Alliance node — public identity, member count within disclosure. • Posture edge — directional, four states. • Treaty edge — type and active/record-only. • Conflict edge — public conflict only. • Suppressed counts — named state. • No coordinate, distance, region or territory. |
| **G Controls** | • Select node/edge — peek + context. • Filter by relation type — read-only. • Search by name — jump. • `Open profile` / `Open alliance` — permitted destinations. No drag-to-move meaning. |
| **H Screen relationships** | `SCR-010`; `SCR-053`; `SCR-047`; `SCR-048`; `SCR-069`; `SCR-052`. |
| **I Responsive** | Desktop: graph + context panel. Tablet: graph with filter drawer, fewer labels. Mobile: list-first grouped by relation; graph opt-in; every fact reachable in the list. |
| **J Governing references** | Governing: TR-012/013/014; REQ-041; FO-013. Supporting: `13A-BP-006`, `13A-BP-016`, `13A-DR-003`. Decisions: D-218, D-209. |
| **K Restrictions and notes** | No geographic map, coordinates, borders, provinces or fronts. Pending proposals never appear. Own pair restriction visible only to the owner. No alliance military data. |

### SCR-019 — Alerts & notification history

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Register/list`; governing **B-02/B-11**; related `REQ-731`; new `REQ-888`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The complete alert history with tiers and mute states. It solves "what happened and which alerts can I manage" and supports triage without losing non-opt-out notices. |
| **C Entry and navigation** | Shell alert indicator, digest, `SCR-013`. Destinations: the owning object/action screen. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Unread/priority alerts. 2) Alert tier and source. 3) Object link and time. 4) Mute state and non-opt-out marker. 5) History and filters. 6) Definitions of tiers. |
| **E Layout** | `P-REG`. Tier summary, alert table, filter row, mute controls where permitted, exact pagination. |
| **F Data presentation** | • Alert tier — blocking/digest/ambient over existing events. • Source — DIP N1–N9, WAR catalogue, B-11, MSG; no invented source. • Time — turn and UTC, historical. • Mutable — yes/no; non-opt-out marked. • Object — public/private per rule. |
| **G Controls** | • `Open` — link to owning surface. • `Mute` only where the owning rule permits; non-opt-out controls are absent or disabled with reason. • `Mark read` where supported. • Filter/saved view. |
| **H Screen relationships** | `SCR-013`; `SCR-014`; all owning screens; `SCR-088`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: card list with tier and source, mute in row menu; non-opt-out items still visible. |
| **J Governing references** | Governing: REQ-731; DIP-114/116; WAR notification catalogue; MSG. Supporting: `13A-DR-011`, `13A-BP-027`. Decisions: D-201. |
| **K Restrictions and notes** | Notification presentation only; the UI never creates an event. DIP N2/N7 cannot be suppressed while an open decision exists. No second channel is created. |

### SCR-020 — Pinned objects / favorites manager (Conditional)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Register/list`; governing **cross-system convenience**; related none; new `REQ-889`; class **Conditional**; audience authenticated player; permissions authenticated; visibility pin list private. |
| **B Purpose** | Would let a player pin nations, alliances, wars or offers for quick return. It solves navigation convenience only; no rule compels it. |
| **C Entry and navigation** | None until enabled. When enabled: Overview or account menu. Destinations: pinned objects subject to visibility. Return: `SCR-013`. |
| **D Information hierarchy** | 1) Pinned objects. 2) Current visibility/state. 3) Add/remove. 4) Empty explanation. 5) Privacy/abuse note. |
| **E Layout** | `P-REG` list. **Not rendered while Conditional.** |
| **F Data presentation** | • Pin reference — object identity, private to the pinning player. • Object state — current public/visible state. • No private fact is revealed by the pin. |
| **G Controls** | • `Pin`/`Unpin` — read-only preference; no gameplay effect. No control exists while the screen is disabled. |
| **H Screen relationships** | Object screens; `SCR-011`. |
| **I Responsive** | Desktop/tablet/mobile: list of pins with object links; no layout is deployed while Conditional. |
| **J Governing references** | Supporting: `13A-OQ-012`. Decisions: D-216. |
| **K Restrictions and notes** | **Conditional — not built.** The fair-play review must assess whether a pin list becomes a targeting/tracking aid and what privacy/abuse controls are required (`13A-OQ-012`). Until that review closes, the route, navigation entry and component do not exist. A pin may never reveal a private object or aggregate. |

## 3. Politics — SCR-021…SCR-028

All eight screens carry the DMP-268 political state banner (`NORMAL`, `ELECTORAL`, `SUCCESSION`, `TRANSITION`, `CRISIS`, `RECOVERY`) with cause, end turn, what is locked and what is not. The banner is a state, never an account penalty or a ban.

### SCR-021 — Political Panel (with state banner)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Dashboard`; governing **B-06**; related `REQ-269`/`REQ-276`/`REQ-317–321`; new `REQ-890`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The politics home: government identity, leadership, approval/stability summary, six supports and state banner. It solves "who governs and how stable is it" and routes to the seven DMP-256 surfaces. |
| **C Entry and navigation** | Primary nav Politics, overview. Destinations: `SCR-022`…`SCR-028`. Return: `SCR-015`. |
| **D Information hierarchy** | 1) State banner. 2) Government identity + leader/administration. 3) Approval and stability summary. 4) Six-support entry. 5) Pressure/threshold and election context. 6) Definitions. |
| **E Layout** | `P-DASH`. Banner, government card, approval/stability registers, support strip, politics section links, context panel. |
| **F Data presentation** | • `leadership_state` — six states, current. • Government identity — permanent, private/public identity. • Leader and administration — current. • Approval — weighted mean of six supports, integer, private. • Stability — integer bp + text label, current, private. • `pressure_turns/12` — current. • Threshold — current rule value. |
| **G Controls** | • Navigate to each politics surface. • `View approval detail` → `SCR-023`. • No government-change control exists; government identity is permanent (D-084). |
| **H Screen relationships** | `SCR-022`; `SCR-023`; `SCR-024`; `SCR-025`; `SCR-026`; `SCR-027`; `SCR-028`. |
| **I Responsive** | Desktop: government + approval columns. Tablet: stacked. Mobile: banner and government first, approval summary, supports collapsed behind a labelled disclosure. |
| **J Governing references** | Governing: DMP-256/268; DMP-079…083; D-084/D-085. Supporting: `13A-DR-009`. Decisions: D-210. |
| **K Restrictions and notes** | No stability bands are defined by B-06; the UI uses integer basis points plus a text label. No `SET_GOVERNMENT`/`REVOLUTION`/`COUP` verb exists. The banner never implies suspension. |

### SCR-022 — Government structure & institutions

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Object page`; governing **B-06**; related `REQ-269`/`REQ-276`/`REQ-317–321`; new `REQ-891`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Documents the permanent government identity, its leadership model, channels and policy permissions. It solves "what kind of government do I have and what does it permit" and supports understanding, not changing, it. |
| **C Entry and navigation** | `SCR-021`. Destinations: `SCR-023`, `SCR-024`, `SCR-021`. Return: `SCR-021`. |
| **D Information hierarchy** | 1) Government identity and permanence statement. 2) Leadership model and administration. 3) Five numeric channels. 4) Policy permissions. 5) Comparison/creation context where applicable. 6) Rule definitions. |
| **E Layout** | `P-OBJ`. Identity header, permanence notice, channel table, permissions table, comparison panel where creation context exists. |
| **F Data presentation** | • Government name/identity — permanent, private. • Leadership model — interface description, current. • `approval_weight_bp`, `stability_shift_bp`, `stability_cap_bp`, `service_cost_mod_bp`, `research_adjustment` — integer/bp, current. • Policy permissions — categorical, current. • No invented sixth numeric channel. |
| **G Controls** | Read-only in normal play. During creation only, the selection control and confirmation exist, with disadvantages shown at equal prominence; after creation no change control exists. |
| **H Screen relationships** | `SCR-021`; `SCR-023`; `SCR-024`; `SCR-007` (creation step where applicable). |
| **I Responsive** | Desktop: two-column identity/channels. Tablet: stacked. Mobile: identity and permanence first, channels as labelled cards, permissions list; long prose collapses. |
| **J Governing references** | Governing: B-06; D-084/D-085; D-086; DMP-079…084. Decisions: D-084, D-085. |
| **K Restrictions and notes** | Government identity never changes; no verb changes it. The screen must not present the administration as the government. Creation comparison must not favour one option visually. |

### SCR-023 — Approval & stability detail (six supports)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Detail record`; governing **B-06**; related `REQ-269`/`REQ-317–321`; new `REQ-892`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Explains approval and stability through the six support groups and every named term. It solves "why is my approval what it is" and supports choosing a lever without hidden aggregates. |
| **C Entry and navigation** | `SCR-021`, `SCR-028`. Destinations: `SCR-024` policy axes, `SCR-028` crisis, `SCR-021`. Return: `SCR-021`. |
| **D Information hierarchy** | 1) Approval and stability values with as-of turn. 2) Six supports with weight, current/last-turn support and contribution. 3) Named terms per support. 4) Threshold and pressure. 5) Historical movement. 6) Definitions/formula references. |
| **E Layout** | `P-DASH`. Approval register, six-support table, per-support cause-chain drawer, stability register, history chart, threshold panel. |
| **F Data presentation** | • Approval — weighted mean, integer, current. • Six supports — Labour `F-PD-004`, Rural `F-PD-005`, Industry `F-PD-006`, Commerce `F-PD-007`, Scholars `F-PD-008`, Security `F-PD-009`; weight and support current/last turn. • Each named term — value and contribution, current. • Stability — bp clamp 5,000…cap, movement ≤250 bp/turn, current. • Threshold — removal threshold, current. • History — per-turn, historical. |
| **G Controls** | • Drill each support — opens `OVL-04` drawer with terms. • `Open policy axes` → `SCR-024`. • `Open crisis view` when in crisis/recovery. Read-only otherwise. |
| **H Screen relationships** | `SCR-021`; `SCR-024`; `SCR-028`; `SCR-022`. |
| **I Responsive** | Desktop: six-row table + cause drawer. Tablet: table with pinned support name. Mobile: support cards, each expanding to terms; approval/stability summary pinned at top. |
| **J Governing references** | Governing: DMP-073; F-PD-004…009; DMP-053/054/056; DMP-064. Supporting: `13A-DR-010`. Decisions: D-210. |
| **K Restrictions and notes** | No term may be hidden behind an aggregate. No invented stability bands or composite "support score". Numbers are integer/bp with text labels, not colour alone. |

### SCR-024 — Policy axes management

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Task/compose`; governing **B-06**; related `REQ-269`/`REQ-317–321`; new `REQ-893`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Lets the player change one of two policy axes within the 12-turn cooldown, with the effect and cost visible before commitment. It solves "how do I shift policy" and supports a single, deliberate change. |
| **C Entry and navigation** | `SCR-021`, `SCR-023`. Destinations: `SCR-023`, `SCR-021`. Return: `SCR-021`. |
| **D Information hierarchy** | 1) Two axes and current settings. 2) Per-axis effect and cost of the proposed setting. 3) Cooldown and next eligible turn on the control. 4) Confirmation. 5) Historical changes. 6) Rule definitions. |
| **E Layout** | `P-TASK`. Axis panels with three settings each, effect preview, cooldown indicator, confirmation panel, history. |
| **F Data presentation** | • Axis A/B — name, current setting. • Proposed setting — preview, forecast/effect. • Cost — crowns or rule cost, current. • Cooldown — turns remaining and next eligible turn, current. • Effective turn — `T+1` resolution statement. • History — past changes, historical. |
| **G Controls** | • Setting selector — available when cooldown elapsed and state permits; disabled with reason otherwise. • `Confirm change` — committing; `OVL-01` lists effect, cost, cooldown and effective turn; outcome one change recorded, cooldown restarts. |
| **H Screen relationships** | `SCR-023`; `SCR-021`; `SCR-026` (both blocked during transition/crisis where the state forbids). |
| **I Responsive** | Desktop: two axis columns. Tablet: stacked. Mobile: one axis per step, cooldown on the control, confirmation as a sheet with the same fields. |
| **J Governing references** | Governing: D-087; DMP-101/102. Supporting: `13A-BP-010`, `13A-DR-009`, `13A-PR-09`. Decisions: D-214. |
| **K Restrictions and notes** | One change per axis per 12 turns, counted from resolution. No third axis, no free re-set. Cooldown is displayed on the control, not in a help note. |

### SCR-025 — Election dashboard

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Dashboard`; governing **B-06**; related `REQ-352`/`REQ-358`/`REQ-361`/`REQ-367`; new `REQ-894`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Shows the election cycle, campaign window, ballot, projected vote and budget/actions. It solves "when is the election and where do I stand" and supports entering the campaign. |
| **C Entry and navigation** | `SCR-021`. Destinations: `SCR-026` campaign actions, `SCR-027` result, `SCR-021`. Return: `SCR-021`. |
| **D Information hierarchy** | 1) Term and `campaign_open_turn`-anchored dates. 2) Ballot/challengers. 3) Projected vote with uncertainty. 4) Campaign budget and remaining actions. 5) Pressure to reset. 6) Definitions. |
| **E Layout** | `P-DASH`. Term strip, date ladder (open, registration close, final notice), ballot table, projection panel, campaign summary. |
| **F Data presentation** | • Term — 240-turn cycle, current. • `campaign_open_turn` — anchor, current. • Offsets — `T−24`, `T−12`, `T−2` labelled on-time only. • Challengers — published rows. • Projected vote — forecast, with assumptions; not a result. • Turnout weights — published. • Campaign budget/remaining actions — current. |
| **G Controls** | • `Open campaign actions` → `SCR-026` when `ELECTORAL`. • `View result` → `SCR-027` after resolution. Read-only outside the window. |
| **H Screen relationships** | `SCR-026`; `SCR-027`; `SCR-021`; `SCR-028`. |
| **I Responsive** | Desktop: date ladder + ballot + projection. Tablet: stacked. Mobile: dates and state first, ballot cards, projection labelled forecast; no wall-clock countdown. |
| **J Governing references** | Governing: D-106/D-107; DMP-178/184; DMP-213. Supporting: `13A-PR-03`. Decisions: D-210. |
| **K Restrictions and notes** | Dates are anchored on `campaign_open_turn`; on-time values are labelled. An interrupted or delayed resolution is a state, not a missed deadline. Projected vote is never presented as the result. |

### SCR-026 — Campaign actions centre

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Task/compose`; governing **B-06**; related `REQ-352`/`REQ-361`; new `REQ-895`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Runs the three permitted campaign actions with exact points or crown costs and charge-once semantics. It solves "what can I do in the campaign" without inventing a fourth action. |
| **C Entry and navigation** | `SCR-025` during `ELECTORAL`. Destinations: `SCR-025`, `SCR-027`. Return: `SCR-025`. |
| **D Information hierarchy** | 1) The three action types and their effects. 2) Cost/points and limits. 3) Current campaign budget. 4) Charge-once state and remaining availability. 5) Read-only state during `TRANSITION`/`CRISIS`. 6) Rule definitions. |
| **E Layout** | `P-TASK`. Three action cards (`CAMPAIGN_PLATFORM`, `CAMPAIGN_RALLY`, `CAMPAIGN_ADVERTISE`), effect/cost table, confirmation, state banner. |
| **F Data presentation** | • `CAMPAIGN_PLATFORM` — 6 points, max 2 per group, at least 3 groups, once per contest, 0 crowns, current. • `CAMPAIGN_RALLY` — once, `2 × ceil(population/1,000)` crowns, +3 Labour/+2 Rural, current. • `CAMPAIGN_ADVERTISE` — up to 2, `3 × ceil(population/1,000)` crowns each, +2 Commerce/+2 Industry/+1 Scholars, current. • Budget — current/reserved. • Charged state — recorded, historical within contest. |
| **G Controls** | • `Allocate platform points` — committing; validates 6 points, 2/group, ≥3 groups; `OVL-01`; outcome charged once. • `Run rally` — committing; once; confirmation. • `Run advertisement` — committing; up to 2; confirmation. • All disabled with reason when the state blocks or the limit is reached. |
| **H Screen relationships** | `SCR-025`; `SCR-027`; `SCR-021`. |
| **I Responsive** | Desktop: three cards in a row + budget. Tablet: two columns. Mobile: one action per card, points allocator as a stepped control, confirmation sheet; destructive styling not used (these are not destructive). |
| **J Governing references** | Governing: D-094; DMP-189/193. Supporting: `13A-PR-09`. Decisions: D-214. |
| **K Restrictions and notes** | Exactly three actions; no fourth. Charge-once: no reservation, no cancellation; a retry with the same key returns the stored row and does not charge twice. Read-only during `TRANSITION`/`CRISIS` as B-06 provides. |

### SCR-027 — Election result & transition view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Status/state`; governing **B-06**; related `REQ-358`/`REQ-367`; new `REQ-896`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Presents the election outcome, the resulting transition and its effects. It solves "what happened and what changes now" and supports acknowledgment and planning through the 12-turn transition. |
| **C Entry and navigation** | Resolution alert, `SCR-025`. Destinations: `SCR-021`, `SCR-025`, `SCR-028` if crisis. Return: `SCR-021`. |
| **D Information hierarchy** | 1) Outcome banner (DMP-184). 2) What changed (administration, not government). 3) Transition length and end turn. 4) Stability penalty figure. 5) Causes. 6) Historical record. |
| **E Layout** | `P-STATE`. Outcome banner, change summary, transition countdown in turns, penalty panel, cause list, history link. |
| **F Data presentation** | • Outcome — elected/continued/other defined outcome, current. • Administration — replaced or retained; government identity unchanged. • Transition — 12 turns, current/end turn. • Stability penalty — 800 bp disclosed, current. • Result record — historical, permanent. |
| **G Controls** | • `Acknowledge` — marks the notice read; no state change. • `View political panel` → `SCR-021`. No control changes the outcome. |
| **H Screen relationships** | `SCR-021`; `SCR-025`; `SCR-028`; `SCR-017`. |
| **I Responsive** | Desktop/tablet: banner + change panel. Mobile: banner first, change summary, end turn visible; cause list collapsible. |
| **J Governing references** | Governing: DMP-184/205/210; D-097/D-098; DMP-213. Supporting: `13A-PR-12`. Decisions: D-210. |
| **K Restrictions and notes** | The administration changes; the government does not. The penalty is disclosed as a figure, not implied. No "election stolen" or urgency framing. |

### SCR-028 — Crisis & recovery digest view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Politics**; category `Status/state`; governing **B-06**; related `REQ-317–321`; new `REQ-897`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Explains the crisis/recovery state and gives concrete recovery actions. It solves "why is this happening and what can I do" and supports acting on approval levers, not a new mechanic. |
| **C Entry and navigation** | Banner, `SCR-021`, `SCR-023`. Destinations: `SCR-023` approval detail, `SCR-024` policy axes, `SCR-021`. Return: `SCR-021`. |
| **D Information hierarchy** | 1) Crisis/recovery state and end turn. 2) The stability-only effect. 3) Retention-threshold proximity. 4) At least three recovery actions with projected effect. 5) Immunity/early-exit rule. 6) History. |
| **E Layout** | `P-STATE`. State banner, effect panel, threshold meter, recovery action list, timeline, definitions. |
| **F Data presentation** | • State — `CRISIS`/`RECOVERY`, current. • Crisis duration — 18 turns, current/end. • Effect — stability-only `1,500 bp` penalty, current. • Recovery — 12 turns at `400 bp`, current. • Early exit — turn ≥6 if legitimacy ≥ threshold+5, rule. • Recovery actions — projected effects, forecast. |
| **G Controls** | • `Open approval levers` → `SCR-023`. • `Open policy axes` → `SCR-024`. • Recovery actions link to their owning screens; no new action is created. |
| **H Screen relationships** | `SCR-023`; `SCR-024`; `SCR-021`; `SCR-027`. |
| **I Responsive** | Desktop: state + actions columns. Tablet: stacked. Mobile: state and end turn pinned, action cards, projected effect labelled forecast. |
| **J Governing references** | Governing: DMP-163; DMP-225/228/229/248; D-099/D-100. Supporting: `13A-DR-010`. Decisions: D-210. |
| **K Restrictions and notes** | Recovery must be actionable, not a warning alone. No new formula, no dice, no invented crisis action. 12-turn recovery and 18-turn crisis are distinct states (D-100). |

## 4. Economy and market — SCR-029…SCR-040

Every balance on these screens renders total, reserved and available together (MKT-053) and every figure carries its number type and as-of turn (ECN-177). `SCR-038` and `SCR-039` are **absent** until Global Trade gates G-1…G-6 all pass; no preview, stub or statistic is permitted.

### SCR-029 — Treasury dashboard

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Dashboard`; governing **B-04**; related `REQ-250` region; new `REQ-898`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Answers the ECN-176 money questions: what I have, what is reserved, what I expect, what I owe, why it changed. It solves treasury opacity and supports allocation and reserve decisions. |
| **C Entry and navigation** | Primary nav Economy. Destinations: `SCR-030` budget, `SCR-031` reports, `SCR-033` resources, `SCR-032` production, `SCR-035` offers. Return: `SCR-015`. |
| **D Information hierarchy** | 1) Available treasury and current position. 2) Reserved funds and pending commitments. 3) Income/expenditure summary and net change. 4) Forecast with assumptions. 5) Historical trend. 6) Explanations. |
| **E Layout** | `P-DASH`. Headline financial registers, six-number-type legend, breakdown panel, forecast panel, history chart, related links, context panel. |
| **F Data presentation** | • Available treasury — crowns, current, private. • Reserved — crowns, current, private. • Total = available + reserved — derived, labelled. • Income/expenditure — per-turn, current/historical. • Net change — historical. • Forecast — next turn, labelled forecast with assumptions. • National wealth — report statistic, not spendable. • No credit/overdraft line. |
| **G Controls** | • Links to budget/reports/resources. • `Set reserve` only where a reserve action exists in B-04; otherwise read-only. No direct "spend" control on the dashboard. |
| **H Screen relationships** | `SCR-030`; `SCR-031`; `SCR-033`; `SCR-032`; `SCR-057` (alliance receipts affecting crown flows); `SCR-015`. |
| **I Responsive** | Desktop: registers + breakdown + context. Tablet: stacked. Mobile: available/reserved/current position first, forecast labelled, history collapsible; no hidden reserve. |
| **J Governing references** | Governing: ECN-176/177/178; D-050/D-051/D-062. Supporting: `13A-BP-026`, `13A-DR-009`. Decisions: D-210, D-212. |
| **K Restrictions and notes** | No debt, credit, overdraft, interest or bond. Treasury floors at zero; unpaid obligations are cancelled, not deferred. Forecast is never shown as a balance. |

### SCR-030 — Budget & national wealth

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Detail record`; governing **B-04**; related `REQ-250` region; new `REQ-899`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Separates operating expense from capital expenditure and explains national wealth. It solves "what recurs, what I invested, and what my nation is worth" without implying credit. |
| **C Entry and navigation** | `SCR-029`. Destinations: `SCR-031`, `SCR-029`, `SCR-043` (capex), `SCR-044` (opex). Return: `SCR-029`. |
| **D Information hierarchy** | 1) Recurring operating expense. 2) One-time capital expenditure. 3) National wealth composition. 4) Austerity order if triggered. 5) History. 6) Definitions. |
| **E Layout** | `P-DASH`. Opex panel, capex panel, wealth table, austerity panel, history. |
| **F Data presentation** | • Opex — recurring per-turn, current/forecast. • Capex — one-time, historical/committed. • `national_wealth` — treasury + inventory book value + fixed-asset book value, report statistic; current. • Austerity order — ECN-105 sequence, current when triggered. • Recovery options — at least three when projected negative. |
| **G Controls** | • Links to the owning capex/opex screens. • No "borrow" control exists. • Disabled allocation controls explain the shortfall. |
| **H Screen relationships** | `SCR-029`; `SCR-031`; `SCR-043`; `SCR-044`; `SCR-045`. |
| **I Responsive** | Desktop: opex/capex columns + wealth. Tablet: stacked. Mobile: opex first, capex second, wealth as a labelled report card; austerity actions visible. |
| **J Governing references** | Governing: D-051; D-062; ECN-093/097/098/105/107. Decisions: D-212. |
| **K Restrictions and notes** | Capex is excluded from net operating income. Wealth is not spendable, not a score and not a credit rating. Austerity cancels, never defers. |

### SCR-031 — Economic reports & history

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Register/list`; governing **B-04**; related `REQ-250` region; new `REQ-900`; class **Mandatory**; audience nation owner; permissions authenticated; visibility class-P/S. |
| **B Purpose** | The append-only economic record with per-turn aggregates and explanations. It solves "what happened and why" and supports audit, export and planning. |
| **C Entry and navigation** | `SCR-029`/`SCR-030`/Economy nav. Destinations: cited object screens, `SCR-029`, `SCR-033`. Return: `SCR-029`. |
| **D Information hierarchy** | 1) Per-turn aggregate and material change. 2) Cause of each change. 3) Failure factor where applicable. 4) Filters and export. 5) Retention label. 6) Definitions. |
| **E Layout** | `P-REG`. Filter row (turn range, category), report table, cause drawer, export, pagination. |
| **F Data presentation** | • Report rows — append-only ledger, historical. • Per-turn aggregates — production, consumption, income, expenditure, historical. • Cause — rule/term reference. • Failure factor — money/input/power/space/capacity/technology/target. • Retention — hot/monthly/permanent. |
| **G Controls** | • Filter/saved view. • `Open cause` — drawer. • `Export` — permitted own data only; no restricted content. No edit/delete. |
| **H Screen relationships** | `SCR-029`; `SCR-030`; `SCR-033`; `SCR-017`; `SCR-085`. |
| **I Responsive** | Desktop: table + cause panel. Tablet: priority columns. Mobile: card list by turn, cause in expandable section, export in overflow. |
| **J Governing references** | Governing: ECN-142; D-026; TR-049. Supporting: `13A-BP-024`, `13A-DR-020`. Decisions: D-210. |
| **K Restrictions and notes** | No silent rewrite. "Something went wrong" is unacceptable; the limiting factor must be named. Export respects privacy classes and retention. |

### SCR-032 — Production policy & standing orders

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Task/compose`; governing **B-04**; related `REQ-250` region; new `REQ-901`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Sets the recurring production policy and manual batch orders with reservation preview. It solves "how do my chains run" and supports predictable production without overbooking. |
| **C Entry and navigation** | Economy nav, `SCR-029`, `SCR-044`. Destinations: `SCR-044` chains, `SCR-033` resources. Return: `SCR-029`. |
| **D Information hierarchy** | 1) Per-chain standing policy. 2) Manual order entry and capacity limit. 3) Reservation preview (money, inputs, capacity). 4) Affordability/limit checks. 5) Batch history. 6) Rule definitions. |
| **E Layout** | `P-TASK`. Chain policy cards, order form, reservation preview, validation, history. |
| **F Data presentation** | • Policy — `RUN_AT_CAPACITY`/`RUN_TO_TARGET`/`IDLE`, current. • Target — stored target for `RUN_TO_TARGET`, current. • Capacity — batches/turn, current. • Manual order — batch count, pending. • Reservation — money/inputs/capacity, pending. • Affordability — available vs required, current. |
| **G Controls** | • `Set policy` — committing once at resolution; reserves nothing; confirmation explains recurring nature. • `Submit manual order` — committing; `OVL-01` shows cost, reservation, capacity and effect on next turn's opex; outcome accepted/reserved or rejected with `F5`/limit reason. • `Cancel` only where the rule permits. |
| **H Screen relationships** | `SCR-044`; `SCR-033`; `SCR-034`; `SCR-031`. |
| **I Responsive** | Desktop: policy table + form. Tablet: stacked. Mobile: chain card → order sheet; reservation preview before confirm; no accidental batch increment. |
| **J Governing references** | Governing: D-053; ECN-044/045/053/139; ECN-181. Supporting: `13A-BP-028`. Decisions: D-214. |
| **K Restrictions and notes** | Manual orders reserve at acceptance and run fully or fail atomically; no partial execution. Standing policy reserves nothing. Total reserved capacity may not exceed chain capacity. |

### SCR-033 — Resources & warehouse view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Register/list`; governing **B-04/B-05**; related `REQ-250` region; new `REQ-902`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Shows every resource's total, reserved and available quantities, warehouse space and book values. It solves "what do I actually have free to use" and supports production, trade and construction decisions. |
| **C Entry and navigation** | `SCR-029`, Economy nav, `SCR-032`. Destinations: `SCR-034` power, `SCR-036` compose offer, `SCR-044` chains. Return: `SCR-029`. |
| **D Information hierarchy** | 1) Resource rows with total/reserved/available. 2) Warehouse capacity vs holdings. 3) Book values. 4) Blocking reasons/capacity full. 5) History. 6) Definitions. |
| **E Layout** | `P-REG`. Capacity bar, resource table, book-value column, status chips, history link. |
| **F Data presentation** | • Each resource — total/reserved/available, whole units, current. • Warehouse — used/total `W`, current. • Book value — crowns at reference price, current. • Capacity status — full/blocked. • No market price pre-gate (D-117). |
| **G Controls** | • `Compose offer` → `SCR-036` (uses available only). • Filter/sort. No direct resource deletion or free transfer. |
| **H Screen relationships** | `SCR-034`; `SCR-036`; `SCR-044`; `SCR-032`; `SCR-030`. |
| **I Responsive** | Desktop: full table. Tablet: pinned resource column, scroll. Mobile: cards per resource with the triple on one line; capacity bar above; no total-only card. |
| **J Governing references** | Governing: MKT-053; ECN-120/127; URB-066; D-045/D-064. Supporting: `13A-BP-026`. Decisions: D-212, D-213. |
| **K Restrictions and notes** | "Balance" without total/reserved/available is a defect. Reserved includes "committed to a pending operation" as a labelled subset where applicable. No market value appears before the gate. |

### SCR-034 — Power grid view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Detail record`; governing **B-04/B-05**; related `REQ-250` region; new `REQ-903`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Shows generation, demand, surplus/shortfall and derating. It solves "why are my processing batches not running" and supports generator/processing decisions. |
| **C Entry and navigation** | Economy nav, `SCR-033`, `SCR-044`. Destinations: `SCR-044`, `SCR-043` (generator construction), `SCR-033`. Return: `SCR-029`. |
| **D Information hierarchy** | 1) Grid supply vs processing demand. 2) Surplus/shortfall and `power_pct`. 3) Derated batches. 4) Generator levels/fuel. 5) History. 6) Definition that power is not stored. |
| **E Layout** | `P-DASH`. Supply/demand registers, `power_pct` meter, derating table, generator list, history. |
| **F Data presentation** | • `power_generated` — GU, current. • `power_used` — GU, current. • `power_surplus`/`power_shortfall` — GU, current. • `power_pct` — integer %, current. • Derated batches — current. • Generator levels — current. No stored balance. |
| **G Controls** | • `Open chains` → `SCR-044`. • `Build generator` → `SCR-043` when eligible. No power transfer/trade control. |
| **H Screen relationships** | `SCR-044`; `SCR-043`; `SCR-033`; `SCR-042`. |
| **I Responsive** | Desktop: meters + generator table. Tablet: stacked. Mobile: supply/demand and `power_pct` first, generator list cards. |
| **J Governing references** | Governing: D-048; ECN-056/059/060/061/064/065. Decisions: D-212. |
| **K Restrictions and notes** | Power is derived capacity, never stored, traded, gifted, reserved or banked. Surplus is discarded and reported, not banked. No priority chain; pro-rata derating only. |

### SCR-035 — Directed-trade inbox

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Register/list`; governing **B-07**; related `REQ-465`; new `REQ-904`; class **Mandatory**; audience nation owner; permissions authenticated; visibility parties-only. |
| **B Purpose** | The directed-offer workspace: incoming and outgoing chains with terms, status and expiry. It solves "who has offered what to me" and supports accept/decline/counter/cancel. |
| **C Entry and navigation** | Economy nav, Inbox, Treasury. Destinations: `SCR-036` compose/counter, `SCR-037` detail, `SCR-040` history. Return: `SCR-029`. |
| **D Information hierarchy** | 1) Incoming offers awaiting action. 2) Outgoing offers and their state. 3) Terms summary and expiry. 4) Total/reserved/available of the assets concerned. 5) No-reservation notice. 6) History/filter. |
| **E Layout** | `P-REG`. Incoming/outgoing tabs, offer table, status chips, action column, filter, pagination. |
| **F Data presentation** | • Offer author — public identity, parties-only context. • Terms — up to five lines per side, parties-only. • Created/expiry turn — current/historical. • Status — pending/countered/accepted/declined/withdrawn/expired. • Assets — total/reserved/available, current. • Rate-limit position — 20 actions/12 turns, current. |
| **G Controls** | • `Accept` — committing; preconditions both sides re-checked; confirmation; outcome atomic trade or failure. • `Decline` — committing; private. • `Counter` → `SCR-036`. • `Cancel` outgoing where permitted. • `Open detail` → `SCR-037`. |
| **H Screen relationships** | `SCR-036`; `SCR-037`; `SCR-040`; `SCR-014`; `SCR-033`. |
| **I Responsive** | Desktop: table + actions. Tablet: priority columns. Mobile: offer cards with terms summary and expiry; accept/decline in a row menu; confirmation sheet. |
| **J Governing references** | Governing: MKT-105/125; D-016; MKT-053/061; D-017. Supporting: `13A-PR-10`. Decisions: D-213. |
| **K Restrictions and notes** | Creating an offer reserves nothing; reservation begins at acceptance. Terms visible only to the two parties and restricted audit. A third party cannot see that the chain exists. |

### SCR-036 — Compose / counter offer

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Task/compose`; governing **B-07**; related `REQ-465`; new `REQ-905`; class **Mandatory**; audience nation owner; permissions authenticated; visibility parties-only. |
| **B Purpose** | Builds or counters a directed offer with up to five lines per side, showing the pledge and imbalance before commitment. It solves "how do I propose a fair trade" without hidden terms. |
| **C Entry and navigation** | `SCR-035` compose or counter. Destinations: `SCR-035`, `SCR-037`. Return: `SCR-035`. |
| **D Information hierarchy** | 1) Counterparty and direction. 2) Your lines and their lines (max 5 each). 3) Pledge/imbalance disclosure. 4) Available balances for each line. 5) Expiry and rate-limit position. 6) Confirmation. |
| **E Layout** | `P-TASK`. Two-column offer builder, resource pickers, amount fields, pledge panel, preview, confirmation. |
| **F Data presentation** | • Counterparty — public identity. • Lines — resource/crowns, quantity, up to 5 per side, proposed. • Available — total/reserved/available for each offered asset. • Pledge — acceptance re-checks both sides; no guarantee language. • Expiry — 12-turn window, target. • Imbalance — factual disclosure for the weaker side. • Rate limit — actions remaining/window. |
| **G Controls** | • `Add line` — up to 5 per side; limit reached disables with reason. • `Submit offer` — committing; `OVL-01` lists both sides, expiry, no-reservation fact; outcome chain created, nothing reserved. • `Remove line`, `Cancel`. |
| **H Screen relationships** | `SCR-035`; `SCR-037`; `SCR-033`; `SCR-014`. |
| **I Responsive** | Desktop: side-by-side builder. Tablet: stacked but with a summary bar. Mobile: stepped builder (you / them / review); amounts numeric; limit and pledge visible at review; confirmation sheet. |
| **J Governing references** | Governing: MKT-019/022/037/038/061; D-016/D-017; MKT-060 (five-active-offer rationale). Supporting: `13A-PR-09`. Decisions: D-214. |
| **K Restrictions and notes** | Five lines per side, five active offers, one per counterparty (MKT-059/060). No reserve at create. No partial fill of a directed offer. No external platform. |

### SCR-037 — Offer detail & two-sided record

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Detail record`; governing **B-07**; related `REQ-465`; new `REQ-906`; class **Mandatory**; audience the two parties and restricted audit; permissions parties-only; visibility private. |
| **B Purpose** | The complete record of one trade chain: both obligations, revisions, settlement and failure. It solves "what exactly did each side owe and what happened" and supports dispute-free records. |
| **C Entry and navigation** | `SCR-035`, `SCR-040`, Inbox. Destinations: `SCR-035`, `SCR-036` counter, `SCR-031` ledger. Return: `SCR-035`. |
| **D Information hierarchy** | 1) Parties and status. 2) Both sides' full obligations. 3) Revision history. 4) Settlement state and transfer reference. 5) Failure reason if any. 6) Rule/definition links. |
| **E Layout** | `P-TASK`/object hybrid. Header, two-sided obligation table, revision timeline, settlement panel, failure panel. |
| **F Data presentation** | • Parties — public identities, parties-only context. • Each side's lines — exact assets/quantities, historical/proposed. • Status — pending/accepted/settled/failed/etc. • Transfer reference — shared `transfer_id`, historical. • Ledger: `TRADE_SELL`/`TRADE_BUY` with deltas summing to zero. • Failure — exact code/reason. |
| **G Controls** | • `Counter` → `SCR-036` where permitted. • `Cancel` where permitted. • No edit of an accepted offer; a revision is a new chain/revision with its own record. |
| **H Screen relationships** | `SCR-035`; `SCR-036`; `SCR-031`; `SCR-014`; `SCR-083` if a dispute route applies. |
| **I Responsive** | Desktop: two-column obligations. Tablet: stacked. Mobile: status and parties first, obligation cards per side, revision timeline collapsible. |
| **J Governing references** | Governing: MKT-056/131; ECON-054; D-017; MKT-034. Decisions: D-213. |
| **K Restrictions and notes** | A partially applied trade is prohibited; settlement is atomic. Both-sided records are immutable; a correction is an appended record, never an edit. Visibility is parties + restricted audit only. |

### SCR-038 — Global Trade board (Conditional)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Register/list`; governing **B-07**; related `REQ-513`; new `REQ-907`; class **Conditional**; audience nation owner when gate passes; permissions authenticated + gate; visibility public board within k=5. |
| **B Purpose** | Would present the public listing board after the release gate. Today it must not exist. |
| **C Entry and navigation** | **No route is rendered.** No navigation entry, no deep link, no direct URL content. When the gate passes, the route would appear in Economy and link `SCR-039`/`SCR-040`. |
| **D Information hierarchy** | **None rendered.** When authorised: primary listings, secondary band/reference, supporting filters, warnings `INSUFFICIENT_SAMPLE`, history, progressive methodology. |
| **E Layout** | `P-REG`. **Not rendered.** |
| **F Data presentation** | **No data may be displayed.** When authorised: listings, posted price, quantity remaining, 3,000 bp band, `INSUFFICIENT_SAMPLE`, sample count, window. Pre-gate, no statistic, count, thumbnail or placeholder. |
| **G Controls** | **No controls.** No post/take/preview/beta action exists. |
| **H Screen relationships** | None while BLOCKED. `MKT-G01` explains absence if a user reaches a stale link. |
| **I Responsive** | Desktop: no layout is deployed (screen absent). Tablet: no layout is deployed (screen absent). Mobile: no layout is deployed (screen absent). |
| **J Governing references** | Governing: B-07; D-117/D-122; MKT-073…077; G-1…G-6. Decisions: D-216. |
| **K Restrictions and notes** | **BLOCKED.** G-1 NOT MET, G-2 NOT MET, G-3 NOT MET, G-4 PARTIAL (not a pass), G-5 NOT MET, G-6 NOT MET. No beta board, no read-only preview, no placeholder trading UI. Activation requires all gates MET and an owner launch decision. |

### SCR-039 — Listing detail & execution confirmation (Conditional)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Detail record`; governing **B-07**; related `REQ-513`; new `REQ-908`; class **Conditional**; audience nation owner when gate passes; permissions authenticated + gate; visibility public listing, private execution. |
| **B Purpose** | Would show one listing and its execution confirmation. Today it must not exist. |
| **C Entry and navigation** | **No route.** When authorised: from `SCR-038`, back to `SCR-038`; related `SCR-040`. |
| **D Information hierarchy** | **None rendered.** When authorised: listing terms, remaining quantity, partial-fill construction, crossed badge, execution consequence, confirmation, history. |
| **E Layout** | `P-TASK`. **Not rendered.** |
| **F Data presentation** | **No data.** When authorised: posted price, `quantity_remaining`, `posted = filled + locked + remaining`, "Filled x of y", execution price, fees only if an approved fee policy exists. |
| **G Controls** | **No controls.** No take/preview action. When authorised: `Take` with exact quantity and confirmation. |
| **H Screen relationships** | None while BLOCKED. |
| **I Responsive** | Desktop: no layout is deployed (screen absent). Tablet: no layout is deployed (screen absent). Mobile: no layout is deployed (screen absent). |
| **J Governing references** | Governing: B-07; D-111; MKT-106/107/108; G-1…G-6. Decisions: D-216. |
| **K Restrictions and notes** | **BLOCKED** with `SCR-038`. No partial-fill representation may be deployed before the gate. No automatic matching, price-time priority or crossing. |

### SCR-040 — Trade history & reference prices

| Field | Specification |
|---|---|
| **A Identity** | Parent **Economy**; category `Register/list`; governing **B-07**; related `REQ-465`; new `REQ-909`; class **Mandatory**; audience nation owner; permissions authenticated; visibility class-P/S. |
| **B Purpose** | The player's own trade history and, only after the gate, disclosed reference prices. It solves "what have I traded and at what price" without early statistics. |
| **C Entry and navigation** | Economy nav, `SCR-035`, `SCR-037`. Destinations: `SCR-037`, `SCR-035`, `SCR-031`. Return: `SCR-029`. |
| **D Information hierarchy** | 1) Own completed/pending/failed trades. 2) Counterparty and assets. 3) Price and window where disclosed. 4) Reference price state (pre-gate minimal). 5) Retention label. 6) Methodology. |
| **E Layout** | `P-REG`. Trade table, price column with disclosure state, filter, export, methodology drawer. |
| **F Data presentation** | • Own trades — historical, private. • Counterparty — public identity, parties context. • Price — completed price, historical. • Reference price — post-gate only, 12-turn VWAP, rounded band, sample count. • `INSUFFICIENT_SAMPLE` — named state. • Pre-gate — no market statistic (D-117). |
| **G Controls** | • Filter/saved view. • `Open offer` → `SCR-037`. • `Export` own history only. No price-invention control. |
| **H Screen relationships** | `SCR-035`; `SCR-037`; `SCR-031`; `SCR-038` only after gate. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: cards with assets/price/window; reference-price state visible; methodology collapsible. |
| **J Governing references** | Governing: D-117; MKT-110/140; D-026. Supporting: `13A-PR-16`. Decisions: D-212. |
| **K Restrictions and notes** | No statistic before the gate. `INSUFFICIENT_SAMPLE` is not zero. Book value is labelled "an accounting value, not an offer". Dual-axis charts banned. |

## 5. Cities, infrastructure and research — SCR-041…SCR-046

### SCR-041 — Cities overview (twelve-city single screen)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Cities**; category `Dashboard`; governing **B-05**; related `REQ-269` region; new `REQ-910`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Presents all twelve cities and the capital in one view with their infrastructure, development capacity, limits and status. It solves "how is my nation built" without paging through cities. |
| **C Entry and navigation** | Primary nav Cities. Destinations: `SCR-042` city detail, `SCR-043` construction, `SCR-046` found city, `SCR-045` research. Return: `SCR-015`. |
| **D Information hierarchy** | 1) City rows with identity, infrastructure and DC. 2) Capital marker and limits. 3) Status chips (unmaintained, capacity full, housing pressure). 4) Found-city eligibility. 5) History. 6) Definitions. |
| **E Layout** | `P-DASH`. National city summary (count, total infrastructure, total housing), city table, found-city CTA, context panel. |
| **F Data presentation** | • City name/ID — public identity. • Infrastructure — integer 10–500, current. • Development capacity — `used / total`, current. • Housing — current, with hard cap context. • Facilities by class — counts. • Status — `UNMAINTAINED`, capacity full, housing pressure. • Found-city eligibility — current. |
| **G Controls** | • `Open city` → `SCR-042`. • `Found new city` → `SCR-046` when eligible; disabled with reason otherwise. • No delete, sell or transfer city control exists. |
| **H Screen relationships** | `SCR-042`; `SCR-043`; `SCR-044`; `SCR-046`; `SCR-045`; `SCR-015`. |
| **I Responsive** | Desktop: one table with all twelve. Tablet: pinned city column, scroll. Mobile: city cards in a single list, infrastructure/DC/housing on each card; the twelve-city set remains one screen. |
| **J Governing references** | Governing: URB-031; D-067; URB-052. Supporting: `13A-BP-026`. Decisions: D-213. |
| **K Restrictions and notes** | At most twelve cities; one capital; no deletion, sale or transfer. A screen that paginates cities into separate pages violates URB-031. |

### SCR-042 — City detail (infrastructure, housing, slots)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Cities**; category `Object page`; governing **B-05**; related `REQ-269` region; new `REQ-911`; class **Mandatory**; audience nation owner; permissions city ownership; visibility private. |
| **B Purpose** | Details one city: infrastructure, housing formula, development capacity, facilities and slots. It solves "what is in this city and what can it hold" and supports construction decisions. |
| **C Entry and navigation** | `SCR-041`. Destinations: `SCR-043` construction, `SCR-044` chains, `SCR-041`, `SCR-046` if expansion. Return: `SCR-041`. |
| **D Information hierarchy** | 1) City identity, infrastructure, housing. 2) `used / total` DC and per-class breakdown. 3) Facilities and slots. 4) Projected post-order capacity. 5) History. 6) Definitions. |
| **E Layout** | `P-OBJ`. Identity header, infrastructure/housing registers, DC panel, facility list by class, slot table, construction CTA. |
| **F Data presentation** | • Infrastructure — 10–500, current. • Housing — `45,000 + 100 × infrastructure + 25,000 × civic_centres`, current; `housing_capacity`, `civic_centres`, `CIVIC_UNFUNDED` state. • DC — `used / total`, current; per-class breakdown. • Facilities — counts/levels, current. • Slots — one construction-class action per turn, current. • Projection — forecast, labelled. |
| **G Controls** | • `Construct` → `SCR-043`; disabled with reason if no slot/DC/affordability. • `Demolish` only where the rule permits, with 25% crown refund disclosure and confirmation. • No infrastructure decrease control (owner cannot reduce). |
| **H Screen relationships** | `SCR-043`; `SCR-044`; `SCR-041`; `SCR-045`; `SCR-046`. |
| **I Responsive** | Desktop: two columns. Tablet: stacked. Mobile: identity/infrastructure/housing first, DC meter, facility accordion, construction action in a sticky region. |
| **J Governing references** | Governing: URB-052/124…127; D-069/D-079; URB-045/042. Decisions: D-210. |
| **K Restrictions and notes** | Housing is hard-capped for growth only. A player must never discover a capacity problem after paying. Only `OP-05` damage reduces infrastructure. |

### SCR-043 — Construction queue & preview

| Field | Specification |
|---|---|
| **A Identity** | Parent **Cities**; category `Task/compose`; governing **B-05**; related `REQ-269` region; new `REQ-912`; class **Mandatory**; audience nation owner; permissions city ownership; visibility private. |
| **B Purpose** | Previews and commits one construction-class action for a city, with cost, capacity, slot, availability and refund terms. It solves "what will this build do and cost" and supports a single deliberate order. |
| **C Entry and navigation** | `SCR-042`, `SCR-041`, `SCR-044` (build chain asset). Destinations: `SCR-042`, `SCR-041`, `SCR-045` for programmes. Return: `SCR-042`. |
| **D Information hierarchy** | 1) Selected facility and effect. 2) Full URB-148 preview. 3) Slot state and next availability turn. 4) Affordability and DC limit. 5) Refund/demolition terms. 6) Confirmation. |
| **E Layout** | `P-TASK`. Facility catalogue, preview panel, DC/slot/affordability checks, confirmation, queue/cancel state. |
| **F Data presentation** | • Facility — name, class, effect, limit. • Crown/material cost after every discount — forecast/committed. • DC — projected `used / total`. • Slot — one per city per turn, current. • Availability turn — target. • Book value added — forecast. • Wealth effect — forecast. • Generator supply/demand — forecast. • Demolition refund — 25% crown cost actually paid, rule. |
| **G Controls** | • `Preview` — read-only. • `Confirm construction` — committing; preconditions slot free, DC available, affordable; `OVL-01` lists cost, slot, availability, book value, wealth effect; outcome order accepted/reserved. • `Cancel` where the rule permits; refund terms shown. • `Demolish` present only as a separate destructive control with confirmation and 25% disclosure. |
| **H Screen relationships** | `SCR-042`; `SCR-044`; `SCR-045`; `SCR-041`; `SCR-031`. |
| **I Responsive** | Desktop: catalogue + preview. Tablet: preview above action bar. Mobile: stepped catalogue → preview → confirm; sticky action bar; destructive separated. |
| **J Governing references** | Governing: URB-064/148; D-073/D-074; D-080; URB-152. Supporting: `13A-BP-028`. Decisions: D-214. |
| **K Restrictions and notes** | One construction-class action per city per turn, slot claimed at acceptance; no queue object. Materials are never refunded. Every projection is labelled a projection. No projection is presented as a completed balance. |

### SCR-044 — Production facility chains

| Field | Specification |
|---|---|
| **A Identity** | Parent **Cities**; category `Detail record`; governing **B-05**; related `REQ-269` region; new `REQ-913`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Shows each extraction/processing chain's health and operation. It solves "which chain is blocked and why" and supports maintenance, power and production decisions. |
| **C Entry and navigation** | Cities nav, `SCR-032`, `SCR-042`. Destinations: `SCR-032` policy, `SCR-034` power, `SCR-043` build, `SCR-033` resources. Return: `SCR-041`. |
| **D Information hierarchy** | 1) Chain name and state. 2) Batches, inputs, output, cost, maintenance, power. 3) Blocking reason and `UNMAINTAINED`. 4) Research bonus as a separate line. 5) History. 6) Definitions. |
| **E Layout** | `P-REG`. Chain cards/table, maintenance status, blocking reason, power draw, research bonus, policy link. |
| **F Data presentation** | • Chain — extraction/processing, current. • Batches — current/planned. • Inputs — available stock, current. • Expected output — forecast. • Variable cost — current. • Maintenance — paid/unpaid, `UNMAINTAINED`. • Power draw — GU. • Research bonus — separate modifier line. |
| **G Controls** | • `Set policy` → `SCR-032`. • `View power` → `SCR-034`. • `Build/upgrade` → `SCR-043` where eligible. No direct "repair" action beyond paying maintenance through the owning rule. |
| **H Screen relationships** | `SCR-032`; `SCR-034`; `SCR-043`; `SCR-033`; `SCR-041`. |
| **I Responsive** | Desktop: table by chain. Tablet: priority columns. Mobile: chain cards with state/blocking reason; details expandable. |
| **J Governing references** | Governing: URB-149; ECN-147/147a. Decisions: D-210. |
| **K Restrictions and notes** | A capacity whose maintenance is unpaid is `UNMAINTAINED` and cannot run. No partial `UNMAINTAINED` chain. Maintenance obligation is whole. |

### SCR-045 — Research view (projects, technologies, programmes)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Cities**; category `Register/list`; governing **B-05**; related `REQ-269` region; new `REQ-914`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The twelve-technology tree and research programmes with status, cost, progress and RP accounting. It solves "what can I research and what will it do" and supports one active project and programme spend. |
| **C Entry and navigation** | Cities nav, `SCR-041`, `SCR-042`. Destinations: `SCR-044` chains (effects), `SCR-041`. Return: `SCR-045` root. |
| **D Information hierarchy** | 1) Active project and progress. 2) RP pool/generation and available. 3) Branch tree with statuses. 4) Project cost/effect/prerequisite. 5) Programmes and banked-RP spend. 6) Definitions. |
| **E Layout** | `P-REG`/tree. Research header (RP pool, generation, active project), branch tree, project cards, programme list, history. |
| **F Data presentation** | • RP pool — `rp_pool`, current. • RP available — `rp_pool − rp_reserved`, current. • RP generation — per turn, current. • Active project — one, current, progress. • Each tech — status `locked`/`available`/`in progress`/`complete`, cost in RP/crowns, prerequisite, effect. • Programme — cost/whether banked RP only. • Predictions — forecasts, labelled. |
| **G Controls** | • `Start research` — committing; precondition no other active project, prerequisite met, RP/crowns available; confirmation lists cost, effect, completion forecast; outcome active project. • `Fund programme` — committing; spends banked RP only; confirmation and availability check. • `Cancel` only where the rule permits. |
| **H Screen relationships** | `SCR-044`; `SCR-042`; `SCR-043`; `SCR-041`. |
| **I Responsive** | Desktop: branch tree + detail panel. Tablet: tree list + detail. Mobile: branch accordion, project cards, RP pool pinned; programme spend in a separate section. |
| **J Governing references** | Governing: URB-102/150/095; D-076/077/078. Decisions: D-210. |
| **K Restrictions and notes** | One active project only. Programmes spend banked RP only and cannot be funded by same-turn generation. Predictive completion is a forecast, not a promise. |

### SCR-046 — Found new city flow

| Field | Specification |
|---|---|
| **A Identity** | Parent **Cities**; category `Task/compose`; governing **B-05**; related `REQ-269` region; new `REQ-915`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Creates a new city through the cost and eligibility gate. It solves "how do I expand" and supports a one-time, fully disclosed commitment. |
| **C Entry and navigation** | `SCR-041` CTA, `SCR-042` expansion link. Destinations: `SCR-041`, `SCR-042`. Return: `SCR-041`. |
| **D Information hierarchy** | 1) Eligibility (city count ≤12, national infrastructure threshold, expansion slot). 2) Cost gate (crowns, 20 steel). 3) New-city starting state. 4) Name validation. 5) Confirmation. 6) No-cooldown statement. |
| **E Layout** | `P-TASK`. Eligibility checklist, cost panel, new-city preview, name field, confirmation. |
| **F Data presentation** | • City count k — current. • Threshold `100 × (k−1)` — current. • Expansion slot — current. • `city_cost(k) = 400 + 150 × k²` crowns — current/forecast. • Steel — 20 unreserved, current. • New city — infrastructure 10, 11 DC, housing 46,000, current preview. • No cooldown. |
| **G Controls** | • `Found city` — committing; preconditions all eligibility checks, 20 steel unreserved, crowns available; `OVL-01` lists cost, slot, new-city state; outcome city created. • `Cancel`. Name field uses D-038 rules. |
| **H Screen relationships** | `SCR-041`; `SCR-042`; `SCR-043`; `SCR-033`. |
| **I Responsive** | Desktop: checklist + cost + preview. Tablet: stacked. Mobile: stepped eligibility → cost → confirm; sticky action; no accidental double-submit. |
| **J Governing references** | Governing: URB-032/033/034; D-068. Decisions: D-214. |
| **K Restrictions and notes** | No real-time cooldown; the gate is cost and infrastructure. Steel must be unreserved. The new city starts at the fixed state; the UI may not invent a bonus. |

## 6. Diplomacy and alliances — SCR-047…SCR-058

The Foreign section holds two distinct contexts: nation diplomacy (B-08) and alliance management (B-09). Each screen names its governing B-section. The Alliance interface is **management and coordination only** — never a military command surface.

### SCR-047 — Diplomatic overview (posture register)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Dashboard`; governing **B-08**; related `REQ-530` region; new `REQ-916`; class **Mandatory**; audience nation owner; permissions authenticated; visibility mixed (public + private pair facts). |
| **B Purpose** | The diplomacy home: the six required views' entry, the posture register per pair, agreements and embargoes. It solves "where do I stand with the world" and supports choosing a pair to act on. |
| **C Entry and navigation** | Primary nav Foreign. Destinations: `SCR-048` pair, `SCR-049` proposal, `SCR-050` agreement, `SCR-052` history. Return: `SCR-015`. |
| **D Information hierarchy** | 1) Posture register for pairs of interest. 2) Active agreements and embargoes. 3) Pending items. 4) Six-view entries. 5) History. 6) Definitions. |
| **E Layout** | `P-DASH`. Posture summary, agreement list, embargo list, pending band, six-view links, context panel. |
| **F Data presentation** | • Pair posture — two directions, `FRIENDLY`/`NEUTRAL`/`TENSE`/`HOSTILE`, current. • Agreements — type/state, public/private per publication. • Embargo — one direction per pair, public at declaration. • Pending proposals — parties only. • Breach count — public fact where applicable. • Aggregates — k=5. |
| **G Controls** | • `Open pair` → `SCR-048`. • `Propose` → `SCR-049` for a named counterparty. • `Open agreement` → `SCR-050`. • Filters. No declaration-of-war control (War section owns it). |
| **H Screen relationships** | `SCR-048`; `SCR-049`; `SCR-050`; `SCR-051`; `SCR-052`; `SCR-018`; `SCR-010`. |
| **I Responsive** | Desktop: register + agreement list. Tablet: stacked. Mobile: posture cards, pending band first, agreements accordion. |
| **J Governing references** | Governing: 08C §12.2/§12.5; DIP-023/024/030. Supporting: `13A-BP-006`. Decisions: D-210. |
| **K Restrictions and notes** | No score, no reputation, no pending terms of other pairs. Empty states are specified and honest. An embargo is not a treaty. |

### SCR-048 — Pair screen (relationship detail)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Object page`; governing **B-08**; related `REQ-530` region; new `REQ-917`; class **Mandatory**; audience nation owner; permissions authenticated; visibility mixed pair facts. |
| **B Purpose** | The bilateral relationship in one place: both postures, agreements, breach count and restrictions. It solves "what is between us" and supports proposing, amending or terminating. |
| **C Entry and navigation** | `SCR-047`, profile, Network View. Destinations: `SCR-049` proposal, `SCR-050` agreement, `SCR-052` history. Return: `SCR-047`. |
| **D Information hierarchy** | 1) Both directional postures. 2) Active agreements and embargo. 3) Pending proposals. 4) Breach count as fact. 5) Pair-restriction state where the viewer is subject. 6) History. |
| **E Layout** | `P-OBJ`. Two-direction header, agreement list, pending band, breach record, restriction panel, history link. |
| **F Data presentation** | • A→B and B→A posture — independent, current. • Agreements — type/state, public/private. • Embargo — direction, public. • Breach count — fact, no score, historical. • Pair restriction — own status, private. • No other pair's terms. |
| **G Controls** | • `Propose agreement` → `SCR-049`. • `View agreement` → `SCR-050`. • `Declare embargo` only where B-08 permits and with confirmation; outcome public declaration. • No delegation control. |
| **H Screen relationships** | `SCR-047`; `SCR-049`; `SCR-050`; `SCR-052`; `SCR-010`. |
| **I Responsive** | Desktop: two-direction columns. Tablet: stacked. Mobile: directions as two labelled cards, agreements below; restriction reason visible. |
| **J Governing references** | Governing: DIP-023/024/086/088; NET-023; DP-A01. Supporting: 08C §12.7. Decisions: D-210. |
| **K Restrictions and notes** | Posture is not war. Breach count dies with the nation and has no mechanical effect. Pair restriction is private to the two accounts; no public accusation. |

### SCR-049 — Proposal & negotiation flow

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Task/compose`; governing **B-08**; related `REQ-530` region; new `REQ-918`; class **Mandatory**; audience nation owner; permissions authenticated; visibility parties-only. |
| **B Purpose** | Creates, counters, withdraws or accepts a diplomatic proposal with full consequences. It solves "how do I formalise a relationship" and supports a sovereign, non-delegated decision. |
| **C Entry and navigation** | `SCR-047`, `SCR-048`, Inbox. Destinations: `SCR-050` on acceptance, `SCR-048`, `SCR-047`. Return: `SCR-048`. |
| **D Information hierarchy** | 1) Counterparty and type. 2) Terms and obligations. 3) The ten 08C §12.3 confirmation fields. 4) Duration/activation/expiry. 5) Reversibility and limits. 6) What it does not do. |
| **E Layout** | `P-TASK`. Proposal builder, terms summary, confirmation panel (ten fields), withdraw/counter paths. |
| **F Data presentation** | • Type — `DP-T01` NAP / `DP-T02` consultation / `DP-T03` aid, proposed. • Terms — obligations, amounts, parties. • Duration — activation/expiry, proposed. • Limit — proposal cap and next eligible turn. • Pending state — parties only. • Aid amount — crowns and reservation if applicable. |
| **G Controls** | • `Send proposal` — committing; `OVL-01` ten fields; outcome pending, parties only. • `Counter` — committing; outcome new pending terms, parties only. • `Withdraw` — permitted before acceptance. • `Accept` — committing; confirmation; outcome accepted then active at boundary (or record-only where applicable). |
| **H Screen relationships** | `SCR-048`; `SCR-050`; `SCR-014`; `SCR-051`. |
| **I Responsive** | Desktop: form + confirmation side panel. Tablet: preview above action bar. Mobile: stepped type → terms → review; ten fields retained; cancel always present and non-destructive. |
| **J Governing references** | Governing: D-030; 08C §12.3; DP-T01…T03. Supporting: `13A-PR-09`. Decisions: D-214. |
| **K Restrictions and notes** | Pending terms are visible only to the named parties. No delegation, no preselected accept, no countdown that decides. Rejection/withdrawal are private. |

### SCR-050 — Agreement / treaty detail

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Detail record`; governing **B-08**; related `REQ-530` region; new `REQ-919`; class **Mandatory**; audience parties and public where active; permissions per publication; visibility mixed. |
| **B Purpose** | The authoritative record of one agreement: type, parties, obligations, lifecycle and public record. It solves "what did we agree" and supports amendment/renewal/termination. |
| **C Entry and navigation** | `SCR-047`, `SCR-048`, `SCR-049` on acceptance, history. Destinations: `SCR-051` publication, `SCR-052` history, `SCR-048`. Return: `SCR-047`. |
| **D Information hierarchy** | 1) Type and state. 2) Parties and obligations. 3) Activation/expiry/termination. 4) Public record status. 5) Amendment/renewal history. 6) Rule links. |
| **E Layout** | `P-OBJ`. Agreement header, obligations table, lifecycle timeline, publication panel, history. |
| **F Data presentation** | • Type — `DP-T01`…`DP-T03` or `DP-A01`, exact. • State — proposed/pending/accepted/active/expiring/terminated/expired. • Parties — public identities. • Obligations — exact terms. • Activation/expiry — turns. • Public record — fields since activation, k=5 aggregates. |
| **G Controls** | • `Amend`/`Renew` only where the type permits; committing with confirmation. • `Terminate` — committing, destructive-styled, confirmation explains obligations. • `View publication` → `SCR-051`. |
| **H Screen relationships** | `SCR-051`; `SCR-052`; `SCR-048`; `SCR-047`; `SCR-014`. |
| **I Responsive** | Desktop: obligations + timeline. Tablet: stacked. Mobile: type/state first, obligations cards, termination separated and confirmed. |
| **J Governing references** | Governing: DP-T01…T03; DP-A01; DIP-108…113. Decisions: D-210. |
| **K Restrictions and notes** | No stale active badge. An embargo is one-directional and not a treaty. Record-only alliance treaties execute no mechanic. |

### SCR-051 — Publication & visibility state view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Status/state`; governing **B-08**; related `REQ-530` region; new `REQ-920`; class **Mandatory**; audience parties and public where active; permissions per publication; visibility mixed. |
| **B Purpose** | Explains exactly what is private, what became public and when. It solves "who can see this" and supports informed consent before activation. |
| **C Entry and navigation** | `SCR-050`. Destinations: `SCR-050`, `SCR-052`. Return: `SCR-050`. |
| **D Information hierarchy** | 1) Current publication state. 2) What is private (pending existence/terms). 3) What is public and at which moment. 4) Public record field list. 5) k=5 aggregates. 6) Definitions. |
| **E Layout** | `P-STATE`. State banner, private/public matrix, publication timeline, public-field list, aggregate suppression. |
| **F Data presentation** | • Pending existence/terms — parties only. • Accepted — parties only. • Active — public at boundary. • Embargo — public at declaration. • Public fields — DIP-109 list. • Aggregates — k=5 with complementary suppression. |
| **G Controls** | Read-only. • `Back to agreement` → `SCR-050`. No control changes publication state outside the owning action. |
| **H Screen relationships** | `SCR-050`; `SCR-052`; `SCR-047`. |
| **I Responsive** | Desktop: matrix + timeline. Tablet: stacked. Mobile: state and "who sees what" first; timeline collapsible. |
| **J Governing references** | Governing: DIP-108…113; D-030. Decisions: D-210. |
| **K Restrictions and notes** | No public pending terms. k=5 applies to every aggregate. The publication moment is a rule event, not a UI choice. |

### SCR-052 — Relations history (class P/S split)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Register/list`; governing **B-08**; related `REQ-530` region; new `REQ-921`; class **Mandatory**; audience nation owner and public where disclosed; permissions per class; visibility class P/S split. |
| **B Purpose** | The historical record of a relationship or agreement, split by private and public classes. It solves "what happened between us over time" without leaking private terms. |
| **C Entry and navigation** | `SCR-047`, `SCR-048`, `SCR-050`. Destinations: `SCR-048`, `SCR-050`, `SCR-017` own chronicle. Return: `SCR-048`. |
| **D Information hierarchy** | 1) Private history (owner only). 2) Public history (as disclosed). 3) Breach record. 4) Retired-page link. 5) Retention label. 6) Definitions. |
| **E Layout** | `P-REG`. Class tabs, timeline/table, filter, retired-page panel, retention label. |
| **F Data presentation** | • Private entries — owner only, class-P. • Public entries — disclosed facts. • Breach count — fact. • Retired page — labelled `Retired`, terminal records. • Replacement — `New nation`, separate identity. • Retention — class boundary. |
| **G Controls** | • Filter/saved view. • `Open object` — link. • No edit/delete. |
| **H Screen relationships** | `SCR-048`; `SCR-050`; `SCR-010`; `SCR-017`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: timeline cards with class label; public/private tabs preserved. |
| **J Governing references** | Governing: 08C §12.6; D-026; DIP-086/088. Decisions: D-210. |
| **K Restrictions and notes** | A replacement does not inherit treaties or breach count. Retired pages remain reachable. Private history never appears in public history. |

### SCR-053 — Alliance home (public page)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Object page`; governing **B-09**; related `REQ-534–653`; new `REQ-922`; class **Mandatory**; audience any viewer; permissions none for public fields, role permission for management links; visibility public fields. |
| **B Purpose** | The public identity of an alliance: name, acronym, colour, leadership, member count, treaties and wars. It solves "what is this alliance" and supports recruitment/diplomacy. |
| **C Entry and navigation** | Network View, profile, search, Foreign nav. Destinations: `SCR-054` membership (permissioned), `SCR-055` governance, `SCR-058` diplomacy, `SCR-010` member profile. Return: `SCR-047` or entry. |
| **D Information hierarchy** | 1) Identity and leadership. 2) Member count and public member list where permitted. 3) Treaties and wars. 4) Applicant privacy notice. 5) Management entries if permitted. 6) History. |
| **E Layout** | `P-OBJ`. Identity header, leadership, member summary, treaty/war panels, management links, context panel. |
| **F Data presentation** | • Name/acronym/colour — public. • Leadership roles — public. • Member count — public within disclosure. • Members — permissioned list; applicant identities private. • Treaties/wars — public records. • No treasury, tax, applicant or private war data. |
| **G Controls** | • `Apply` only where the alliance's membership flow permits; terminates in-product. • `View governance`/`Tax`/`Finance` only with role permission; otherwise absent with explanation. • `View diplomacy` → `SCR-058`. |
| **H Screen relationships** | `SCR-054`; `SCR-055`; `SCR-056`; `SCR-057`; `SCR-058`; `SCR-010`; `SCR-018`. |
| **I Responsive** | Desktop: identity + panels. Tablet: stacked. Mobile: identity and leadership first, member summary, treaties/wars accordion; management entries only if permitted. |
| **J Governing references** | Governing: B-09; ALL-086; `13A-SRC-006` shape only. Decisions: D-210. |
| **K Restrictions and notes** | Applicant identities are private to administration. No external Discord/chat requirement or link is presented as mandatory. No military command exists on this page. |

### SCR-054 — Alliance membership & applicants

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Register/list`; governing **B-09**; related `REQ-534–653`; new `REQ-923`; class **Mandatory**; audience alliance members/officers with permission; permissions `VIEW_APPLICANTS`/`ACCEPT_APPLICANTS` as applicable; visibility alliance-private. |
| **B Purpose** | Manages members and applications entirely in-product. It solves "who is in and who wants in" and supports admission/removal within the alliance's own rules. |
| **C Entry and navigation** | `SCR-053`, `SCR-055`. Destinations: `SCR-053`, `SCR-055`, `SCR-057`. Return: `SCR-053`. |
| **D Information hierarchy** | 1) Pending applicants. 2) Current members and roles. 3) Non-covered-member status. 4) Membership restrictions. 5) History. 6) Permission explanations. |
| **E Layout** | `P-REG`. Applicant table, member table, role column, action column, restriction panel, history. |
| **F Data presentation** | • Applicant — identity visible only to administration; status pending/admitted/declined/expired/withdrawn. • Member — public identity, role. • Non-covered — explicit D-140 status. • Application expiry — 36-turn candidate; rule-labelled. • No private account/enforcement data. |
| **G Controls** | • `Admit`/`Decline` — committing; permissioned; confirmation; outcome status change and in-product notice. • `Remove member` only where B-09 permits; destructive-styled and confirmed. • No control delegates military or treasury authority. |
| **H Screen relationships** | `SCR-053`; `SCR-055`; `SCR-057`; `SCR-049` for alliance diplomacy. |
| **I Responsive** | Desktop: two tables. Tablet: stacked. Mobile: applicant cards first, member list; actions in row menu; destructive removal separated. |
| **J Governing references** | Governing: B-09; ALL-080…086; UD-040 open; D-133. Decisions: D-210. |
| **K Restrictions and notes** | No external platform hop. Applicant privacy is absolute. Membership is not military authority. UD-040 remains open on founding/membership policy details. |

### SCR-055 — Alliance governance & roles

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Object page`; governing **B-09**; related `REQ-534–653`; new `REQ-924`; class **Mandatory**; audience alliance administration; permissions role/permission matrix; visibility alliance-private. |
| **B Purpose** | Records the player-authored constitution and the role/permission matrix. It solves "how is this alliance governed" and supports lawful role management. |
| **C Entry and navigation** | `SCR-053`, `SCR-054`. Destinations: `SCR-056` tax, `SCR-057` finance, `SCR-058` diplomacy. Return: `SCR-053`. |
| **D Information hierarchy** | 1) Constitution. 2) Roles and permissions. 3) Permission-denied explanation per role. 4) Tax/finance/diplomacy entries where permitted. 5) Change history. 6) Definitions. |
| **E Layout** | `P-OBJ`. Constitution panel, role matrix, permission explanations, management links, history. |
| **F Data presentation** | • Constitution — player-authored text, current. • Roles — names/definitions. • Permissions — matrix, current. • Effective permission for viewer — current. • No game-prescribed hierarchy or ideology. |
| **G Controls** | • `Edit constitution` — committing; permissioned; confirmation; audit record. • `Manage roles` — committing; anti-escalation: cannot grant a permission the holder lacks. Denied controls explain why. |
| **H Screen relationships** | `SCR-054`; `SCR-056`; `SCR-057`; `SCR-058`. |
| **I Responsive** | Desktop: constitution + matrix. Tablet: stacked. Mobile: constitution accordion, role cards; editing in a stepped flow. |
| **J Governing references** | Governing: D-135; AN matrix; REQ-553; D-042. Decisions: D-210. |
| **K Restrictions and notes** | Open-ended player-authored governance; no template or ideology prescribed. Rendering a control never grants a permission. No military command. |

### SCR-056 — Alliance tax brackets & member assignment

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Task/compose`; governing **B-09**; related `REQ-614–617` region; new `REQ-925`; class **Mandatory**; audience alliance tax managers; permissions narrow tax-management set (UD-045); visibility alliance-private. |
| **B Purpose** | Creates and assigns player-named tax brackets with separate Crowns and resource rates. It solves "how does our alliance tax work" and supports transparent, versioned policy. |
| **C Entry and navigation** | `SCR-055`, `SCR-053`. Destinations: `SCR-057` receipts, `SCR-054` members. Return: `SCR-055`. |
| **D Information hierarchy** | 1) Current brackets and rates. 2) Member assignments. 3) Effective turn and policy version before confirmation. 4) 0% fallback explanation. 5) History/receipts. 6) Definitions. |
| **E Layout** | `P-TASK`. Bracket editor, Crowns rate, per-resource rates, member assignment table, version/effective panel, history. |
| **F Data presentation** | • Bracket name — player-authored. • Crowns rate — integer basis points 0–10,000. • Resource rates — per asset, integer bp. • Assignment — member → bracket. • Effective turn/policy version — shown before confirmation. • 0% fallback — visible for unassigned/deleted/ambiguous. • Tax history — versioned. • Receipts — per-turn. |
| **G Controls** | • `Create/edit bracket` — committing; validation 0–10,000 bp, unique name; confirmation shows rates, assignment and effective turn. • `Assign member` — committing; confirmation. • Delete/disable bracket only where the rule permits; explicit fallback shown. |
| **H Screen relationships** | `SCR-057`; `SCR-054`; `SCR-055`; `SCR-029` (cross-boundary receipt reference). |
| **I Responsive** | Desktop: editor + assignment table. Tablet: stacked. Mobile: stepped bracket editor, rates as numeric fields with bp suffix, assignment list; effective turn on the confirm screen. |
| **J Governing references** | Governing: ALL-179…187; UD-040/UD-045; ECN-213/213a. Supporting: `13A-SRC-021`, `13A-DR-022`. Decisions: D-214. |
| **K Restrictions and notes** | Rates are integer bp 0–100%; no 10% increments. UD-040 remains open on multi-membership/attribution; the 0% protective fallback is shown, not hidden. No general treasury power. |

### SCR-057 — Alliance finances (ARL receipts, contributions, operational funding)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Register/list`; governing **B-09**; related `REQ-614–653`; new `REQ-926`; class **Mandatory**; audience alliance finance roles; permissions ARL receipt/accounting set; visibility alliance-private. |
| **B Purpose** | The four-category ARL record and immutable receipts. It solves "what has the alliance received and what is available" without implying ownership or withdrawal. |
| **C Entry and navigation** | `SCR-053`, `SCR-055`, `SCR-056`. Destinations: `SCR-056` tax, `SCR-029` own treasury receipt. Return: `SCR-053`. |
| **D Information hierarchy** | 1) ARL categories. 2) Receipts with source/turn. 3) Reserved/expended state. 4) Unavailable-purpose explanation. 5) History. 6) Boundary definitions. |
| **E Layout** | `P-REG`. ARL summary (`RECEIVED`, `AVAILABLE`, `RESERVED`, `EXPENDED`), receipt table, purpose panel, history. |
| **F Data presentation** | • `RECEIVED` — cumulative, current. • `AVAILABLE = RECEIVED − RESERVED − EXPENDED` — derived. • `RESERVED` — current. • `EXPENDED` — current. • Receipt — donor, alliance, asset, amount, turn, `transfer_id`, idempotency. • AOP purposes — `AOP-01`…`AOP-04` labelled provisional; `Valid(q)=0`, unavailable. • No ownership/capacity claim. |
| **G Controls** | • `Record donation` only where the B-04 transfer route initiates it; committing with confirmation and receipt. • `View receipt` — read-only. • **No withdrawal, distribution, grant, loan, salary or player-payment control exists.** |
| **H Screen relationships** | `SCR-056`; `SCR-029`; `SCR-054`; `SCR-055`. |
| **I Responsive** | Desktop: summary + receipts. Tablet: stacked. Mobile: four-category summary first, receipt cards; unavailable purpose clearly stated. |
| **J Governing references** | Governing: ALL-187/193/220…226; D-141; UD-046. Decisions: D-210. |
| **K Restrictions and notes** | Receipts are immutable; corrections append. No purpose is currently spendable. The ARL is not ownership, custody or capacity. UD-046 remains Open. |

### SCR-058 — Alliance diplomacy (treaty offers, NAP coverage)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Foreign**; category `Object page`; governing **B-09**; related `REQ-588–597`; new `REQ-927`; class **Mandatory**; audience alliance diplomacy roles; permissions alliance-diplomacy permission; visibility per publication and coverage. |
| **B Purpose** | Manages alliance-to-alliance treaty objects, record-only or NAP effect, and per-nation coverage. It solves "what has our alliance signed and who is covered" with no delegation of national sovereignty. |
| **C Entry and navigation** | `SCR-053`, `SCR-055`. Destinations: `SCR-050` nation agreement, `SCR-054` members/coverage, `SCR-053`. Return: `SCR-053`. |
| **D Information hierarchy** | 1) Active alliance treaties and type. 2) Coverage per member nation, including non-covered. 3) Pending offers. 4) Block reasons (NAP/same-alliance). 5) History. 6) Boundary notice. |
| **E Layout** | `P-OBJ`. Treaty list, coverage table, pending band, block-reason panel, boundary notice. |
| **F Data presentation** | • Treaty type — `AT-T01` NAP / `AT-T02`…`AT-T05` record-only. • Effect — `AT-E01` no-attack / `AT-E00` record-only. • Coverage — consenting members only; non-covered labelled. • Pending offer — parties only. • Block reason — "blocked by active NAP" without private terms. • Same-alliance ban — explanation. |
| **G Controls** | • `Propose alliance treaty` — committing; permissioned; confirmation lists type, effect, coverage and duration. • `Consent for my nation` — nation-owner only; declining leaves non-covered status. • `Terminate` where permitted. • No collective military position, no war command. |
| **H Screen relationships** | `SCR-053`; `SCR-054`; `SCR-050`; `SCR-062` (public conflict only). |
| **I Responsive** | Desktop: treaties + coverage. Tablet: stacked. Mobile: treaty cards, coverage per member, consent control clearly nation-owner-only. |
| **J Governing references** | Governing: D-140; AT-E00/E01; ALL-196/199/204; WAR-149; UD-047. Decisions: D-210. |
| **K Restrictions and notes** | Zero diplomatic delegation; no collective position until UD-047 is decided. A member declining consent remains a non-covered member and is never punished. No private war visibility, no Alliance military command, no member OP spending. |

## 7. Warfare and military — SCR-059…SCR-068

The War section splits exactly along B-10 visibility: public conflict ledger, owner-only War Operations Board, participant records. No Alliance membership grants military visibility (WAR-148/WAR-161). Opponent strength is only ever a band (`LOW`, `MODERATE`, `HIGH`, `SEVERE`).

### SCR-059 — Military overview (readiness, OP balance)

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Dashboard`; governing **B-10**; related `REQ-654–703`; new `REQ-928`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The military home: own OP pool, readiness, forces and active wars. It solves "what can my military do now" and routes to forces and the owner-only board. |
| **C Entry and navigation** | Primary nav War. Destinations: `SCR-060` forces, `SCR-061` board, `SCR-062` conflicts, `SCR-067` settlement. Return: `SCR-015`. |
| **D Information hierarchy** | 1) OP balance/cap/regeneration. 2) Readiness state. 3) Active wars summary. 4) Forces entry. 5) Protection and ration warnings. 6) Definitions. |
| **E Layout** | `P-DASH`. OP register, readiness register, war summary list, warnings, forces link, context panel. |
| **F Data presentation** | • OP balance — national pool, current. • OP cap — 10, current. • Regeneration — +1 at P3.7, current. • Readiness — own exact or defined state, private. • Active wars — public/private fields per role. • Protection state — private. • No opponent exact data. |
| **G Controls** | • `View forces` → `SCR-060`. • `Open operations board` → `SCR-061` (owner only). • `Open conflicts` → `SCR-062`. • No attack control here; offensive controls live in the board with confirmation. |
| **H Screen relationships** | `SCR-060`; `SCR-061`; `SCR-062`; `SCR-063`; `SCR-067`; `SCR-089`. |
| **I Responsive** | Desktop: OP/readiness + wars. Tablet: stacked. Mobile: OP and readiness first, war cards, warnings visible. |
| **J Governing references** | Governing: D-015 as 10B-C3; WAR-039/049…052; WAR-148. Decisions: D-210. |
| **K Restrictions and notes** | One persistent national OP pool; no Alliance pool, no per-war pool, no transfer. Readiness is own-nation info. No hidden OP anywhere. |

### SCR-060 — Forces & upkeep

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Register/list`; governing **B-10**; related `REQ-654–703`; new `REQ-929`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | Shows the unit roster, military Food upkeep, readiness and impairment basis. It solves "what do I maintain and what does it cost" and supports readiness/ration decisions. |
| **C Entry and navigation** | `SCR-059`, `SCR-061`. Destinations: `SCR-059`, `SCR-061`, `SCR-065` losses. Return: `SCR-059`. |
| **D Information hierarchy** | 1) Unit roster and strength. 2) Military Food demand/paid/short. 3) Readiness effect. 4) Impairment carrying value. 5) History. 6) Definitions. |
| **E Layout** | `P-REG`. Roster table, upkeep panel, readiness panel, impairment panel, history. |
| **F Data presentation** | • Units — `UNIT-INF`/`UNIT-ARM`/`UNIT-AIR`/`UNIT-NAV` counts/strength, private. • Food demand — `ceil(ration_equivalents/1,000)`, current. • Paid/short — current. • Readiness — +50 paid / −100 unpaid, current. • `RATION_SHORT` — state. • Impairment — gross minus accumulated, current. • No opponent stock. |
| **G Controls** | • `Disband` — destructive, confirmation lists OP/resource/readiness effects. • No purchase control here unless B-10 defines one; the UI does not invent recruitment. • `View board` → `SCR-061`. |
| **H Screen relationships** | `SCR-059`; `SCR-061`; `SCR-065`; `SCR-033` (Food). |
| **I Responsive** | Desktop: roster + upkeep. Tablet: stacked. Mobile: roster cards with strength; upkeep and readiness above; `RATION_SHORT` visible. |
| **J Governing references** | Governing: WAR-049…053; WAR-109f…m. Decisions: D-210. |
| **K Restrictions and notes** | Military Food is paid at P3.7 after civilian Food; civilian Food is never reduced to feed the military. Shortfall blocks offensives only. Opponents see only the readiness band. |

### SCR-061 — War Operations Board (nation-owner, owner-only)

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Dashboard`; governing **B-10**; related `REQ-654–703`; new `REQ-930`; class **Mandatory**; audience **nation owner only**; permissions owner-only; visibility private, this nation only. |
| **B Purpose** | The owner's operational command record: this nation's OP, reservations, authorized operations, battles and losses. It solves "what are my operations doing" and supports authorized military decisions within B-10. |
| **C Entry and navigation** | `SCR-059`, war detail (own war), `SCR-064`. Destinations: `SCR-063` war detail, `SCR-064` battle, `SCR-065` losses, `SCR-067` settlement, `SCR-060` forces. Return: `SCR-059`. |
| **D Information hierarchy** | 1) Own OP balance/reservations. 2) Authorized operations and their phase. 3) Active battles and outcomes. 4) Losses/readiness. 5) Block reasons/protection. 6) Confirmation controls. |
| **E Layout** | `P-DASH`. OP panel, operations table, battles list, losses summary, action panel, warnings. |
| **F Data presentation** | • OP — own balance/reserved/cap, current. • Operation — type, OP cost, supply bundle, readiness effect, state. • Battle — own participants, tier/type/loss band to self; exact own strength. • Opponent — band only. • Block reason — protection, NAP, same-alliance, OP, supply. • No other nation's private data. |
| **G Controls** | • Offensive operation controls — committing; confirmation per WAR-152 and the WAR §12.3 minimum (counterparty, OP/resource cost, objective, expected effect, irreversible consequence); disabled with reason when blocked. • `Declare war` only where B-10 permits, 2 OP/500 crowns/one outgoing slot/public record. • `View battle` → `SCR-064`. • No Alliance-visible or delegated control. |
| **H Screen relationships** | `SCR-060`; `SCR-063`; `SCR-064`; `SCR-065`; `SCR-067`; `SCR-089`. |
| **I Responsive** | Desktop: OP + operations + battles. Tablet: stacked. Mobile: OP and operations first; confirmation sheet retains every required field; destructive/irreversible actions separated. |
| **J Governing references** | Governing: B-10; roadmap Prompt-13 boundary; WAR-148/161; REQ-589…591; AX-18; WAR-152; WAR §12.3. Decisions: D-210, D-214. |
| **K Restrictions and notes** | **Owner-only.** The board never merges Alliance data, never shows a member's private state, never offers an Alliance command path, and never exposes another nation's OP. Surrender is the guaranteed off-ramp on `SCR-067`. Espionage is excluded. |

### SCR-062 — Conflicts ledger (public war list)

| Field | Specification |
|---|---|
| **A Identity** | Parent **War** (alias World); category `Register/list`; governing **B-10**; related `REQ-654–703`; new `REQ-931`; class **Mandatory**; audience any viewer; permissions none for public facts; visibility public only. |
| **B Purpose** | The public list of conflicts: date, belligerents, declared state. It solves "what wars exist" and routes to permitted detail without implying hidden data is public. |
| **C Entry and navigation** | War nav, World alias, profile links. Destinations: `SCR-063` war detail, `SCR-010` nation profile. Return: `SCR-059`/`SCR-069`. |
| **D Information hierarchy** | 1) Active conflicts. 2) Date and belligerents. 3) Declared state. 4) Detail availability notice. 5) History/filter. 6) Definitions. |
| **E Layout** | `P-REG`. Scope tabs (active/public), conflict table, filter, pagination, context panel. |
| **F Data presentation** | • Date — declared turn, historical. • Aggressor/defender — public identities. • State — declared/active/settled/surrendered public state. • Detail — permitted link or "restricted" explanation. • No exact strength, OP or private operation. |
| **G Controls** | • `Open war` → `SCR-063` where permitted. • Filter/saved view. No attack/declare control from the public ledger. |
| **H Screen relationships** | `SCR-063`; `SCR-010`; `SCR-061` (own only); `SCR-069`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: conflict cards with date/belligerents/state; detail action per row. |
| **J Governing references** | Governing: WAR-085…088 public fields; `13A-BP-008`. Decisions: D-213. |
| **K Restrictions and notes** | Public list shows only public facts. It does not imply that a restricted detail does not exist. No alliance-private war data. |

### SCR-063 — War detail (declared facts, visibility-filtered)

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Object page`; governing **B-10**; related `REQ-654–703`; new `REQ-932`; class **Mandatory**; audience participants and public per field; permissions per visibility; visibility field-filtered. |
| **B Purpose** | The war record: belligerents, declared facts, operations summary, battles and settlement. It solves "what is this war" with each field filtered to the viewer. |
| **C Entry and navigation** | `SCR-062`, `SCR-061`, battle report. Destinations: `SCR-064` battle, `SCR-067` settlement, `SCR-065` losses (owner), `SCR-050` treaty. Return: `SCR-062`. |
| **D Information hierarchy** | 1) Belligerents and state. 2) Declared facts and duration. 3) Public damage/outcome facts. 4) Battles and permitted bands. 5) Settlement state. 6) Restricted-field explanations. |
| **E Layout** | `P-OBJ`. War header, belligerents, facts table, damage panel, battle list, settlement panel, history. |
| **F Data presentation** | • Belligerents — public identities. • State — WAR-125 lifecycle. • Threat/odds — band only to permitted viewer. • City damage — infrastructure before/after/removed, public at P6. • Book value/force/inventory — private. • Settlement — terms public/private per stage. • Protection — state. |
| **G Controls** | • `View battle` → `SCR-064`. • `Open settlement` → `SCR-067` where participant. • `Surrender` only on the participant's own settlement surface. No attack control. |
| **H Screen relationships** | `SCR-061`; `SCR-062`; `SCR-064`; `SCR-065`; `SCR-067`; `SCR-050`. |
| **I Responsive** | Desktop: facts + battles. Tablet: stacked. Mobile: belligerents and state first, damage facts, battle cards; restricted fields labelled. |
| **J Governing references** | Governing: WAR-085…088; WAR-109k; WAR-125/150. Decisions: D-210. |
| **K Restrictions and notes** | A restricted field is absent or explicitly restricted, never a blank that implies zero. No exact opponent strength. No alliance war room. |

### SCR-064 — Battle report view

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Detail record`; governing **B-10**; related `REQ-654–703`; new `REQ-933`; class **Mandatory**; audience participants; public summary otherwise; permissions participant or public summary; visibility filtered. |
| **B Purpose** | The record of one battle: participants' engaged strength, readiness, counters, powers, ratio, fortune, tier and losses; a public summary otherwise. It solves "what happened in this battle" from the B-10 rules, not benchmark imitation. |
| **C Entry and navigation** | `SCR-061`, `SCR-063`, `SCR-065`. Destinations: `SCR-063`, `SCR-061` own board, `SCR-065` losses. Return: `SCR-063`. |
| **D Information hierarchy** | 1) Outcome and tier. 2) Operation type and turn. 3) Participants' permitted detail. 4) Losses/progress. 5) Public summary for non-participants. 6) Methodology/definitions. |
| **E Layout** | `P-OBJ`. Outcome header, battle record table (WAR-088 fields), losses panel, public-summary variant, methodology drawer. |
| **F Data presentation** | • Battle id/turn — historical. • Operation type — exact. • Engaged strength by type — participant only. • Readiness/counters/powers/ratios — participant only. • Fortune roll/tier — participant; tier public. • Losses — participant detail; public loss band only. • No P&W-derived field claim (`13A-SRC-034`). |
| **G Controls** | Read-only. • `Back to war` → `SCR-063`. • `Open operations board` only for the owner's own nation → `SCR-061`. No re-fight control. |
| **H Screen relationships** | `SCR-061`; `SCR-063`; `SCR-065`; `SCR-066`. |
| **I Responsive** | Desktop: record table + losses. Tablet: stacked. Mobile: outcome and tier first, record fields as labelled rows, losses cards. |
| **J Governing references** | Governing: WAR-088; WAR-109k; `13A-SRC-034` boundary. Decisions: D-210. |
| **K Restrictions and notes** | The layout is derived from B-10's field list; no observed P&W report was available. Public summary shows tier, operation type and loss band only. No exact opponent strength. |

### SCR-065 — War reports & losses summary

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Register/list`; governing **B-10**; related `REQ-654–703`; new `REQ-934`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The conservation-visible loss and settlement ledger for the owner's wars. It solves "what did this war cost" and supports settlement and planning. |
| **C Entry and navigation** | `SCR-061`, `SCR-063`, `SCR-064`. Destinations: `SCR-064`, `SCR-066`, `SCR-067`, `SCR-031`. Return: `SCR-061`. |
| **D Information hierarchy** | 1) Losses by category. 2) Cumulative campaign figures. 3) Settlement ledger. 4) Impairment basis. 5) History/retention. 6) Definitions. |
| **E Layout** | `P-REG`. Loss table, cumulative panel, settlement ledger, impairment note, history. |
| **F Data presentation** | • Losses — units/resources/cities, historical. • Cumulative — campaign total. • Settlement — terms and transfer records. • Impairment — carrying value basis `WAR-109g`. • Conservation — deltas visible. • Retention — class boundary. |
| **G Controls** | • Filter. • `Open battle` → `SCR-064`. • `Open settlement` → `SCR-067`. No edit/rewrite. |
| **H Screen relationships** | `SCR-064`; `SCR-066`; `SCR-067`; `SCR-031`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: loss cards by category; cumulative summary pinned. |
| **J Governing references** | Governing: WAR-109f…m; conservation accounting lineage. Decisions: D-210. |
| **K Restrictions and notes** | Exact book value, force and inventory are private. Public facts remain public at `SCR-063`. No loss may disappear through rounding without disclosure. |

### SCR-066 — Military history archive

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Register/list`; governing **B-10/B-11**; related `REQ-654–763`; new `REQ-935`; class **Mandatory**; audience nation owner; permissions authenticated; visibility class-P private plus public records. |
| **B Purpose** | The permanent war archive. It solves "what wars has my nation fought" and preserves history within retention classes. |
| **C Entry and navigation** | War nav, `SCR-059`, `SCR-065`. Destinations: `SCR-063`, `SCR-064`, `SCR-017`. Return: `SCR-059`. |
| **D Information hierarchy** | 1) Own wars by date. 2) Outcome and settlement. 3) Battles. 4) Public/private split. 5) Retention. 6) Filters. |
| **E Layout** | `P-REG`. War table/timeline, filter, retention label, object links. |
| **F Data presentation** | • War — historical, class-P. • Outcome — win/loss/stalemate/surrender. • Settlement — public terms/private detail. • Battle links. • Retention — permanent/class-O. • No restricted record through counts. |
| **G Controls** | • Filter/saved view. • `Open war` → `SCR-063`. No delete. |
| **H Screen relationships** | `SCR-063`; `SCR-064`; `SCR-017`; `SCR-076`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: war cards with date/outcome; filters in a drawer. |
| **J Governing references** | Governing: D-026; WAR-148. Decisions: D-210. |
| **K Restrictions and notes** | Permanent records are not deleted. A public archive shows only public facts. Alliance membership never grants access to a member's private archive. |

### SCR-067 — Settlement & peace proposal flow

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Task/compose`; governing **B-10**; related `REQ-691`/`REQ-692`; new `REQ-936`; class **Mandatory**; audience war participants; permissions participant; visibility parties-only until public terms. |
| **B Purpose** | The peace/settlement record and the guaranteed surrender path. It solves "how does this war end" and supports an honourable off-ramp. |
| **C Entry and navigation** | `SCR-063`, `SCR-061`, `SCR-065`. Destinations: `SCR-063`, `SCR-050` (treaty objects where applicable). Return: `SCR-063`. |
| **D Information hierarchy** | 1) Current settlement state. 2) Terms and durations. 3) Expiry and acceptance rule. 4) Surrender option. 5) History. 6) Definitions. |
| **E Layout** | `P-TASK`. Settlement terms table, acceptance panel, 12-turn expiry notice, surrender panel (separated), history. |
| **F Data presentation** | • Settlement — one live, current. • Terms — six `TERM_` types, exact. • Duration — turns. • Expiry — 12 turns; silence never accepts. • Surrender — `TERM_CEASEFIRE`, campaign ends `SURRENDER`, opponent `LIMITED_VICTORY`. • Prohibited terms — absent. |
| **G Controls** | • `Propose settlement` — committing; `OVL-01` lists each term and duration. • `Accept settlement` — committing; confirmation. • `Surrender` — committing, destructive-styled, guaranteed available; confirmation explains outcome. • `Decline` — private. |
| **H Screen relationships** | `SCR-063`; `SCR-061`; `SCR-065`; `SCR-050`. |
| **I Responsive** | Desktop: terms + actions. Tablet: stacked. Mobile: terms first, surrender separated at the bottom, confirmation sheet. |
| **J Governing references** | Governing: WAR-126…129/131/132; UD-032 Option A. Decisions: D-214. |
| **K Restrictions and notes** | Surrender cannot be refused; it is the guaranteed off-ramp out of the reroll block. Settlement terms are immutable once accepted; only one live settlement exists. No loot or prohibited term. |

### SCR-068 — Strategic intelligence view (Provisional placeholder)

| Field | Specification |
|---|---|
| **A Identity** | Parent **War**; category `Status/state`; governing **B-10 (no rule)**; related none; new `REQ-937`; class **Provisional**; audience none; permissions none; visibility none. |
| **B Purpose** | Records that any intelligence/espionage surface is a **future rule frontier**, not a product feature. It solves no player problem today; it exists so the absence is explicit. |
| **C Entry and navigation** | **No route, no navigation entry, no link.** |
| **D Information hierarchy** | None. The only recorded information is that no intelligence rule exists. |
| **E Layout** | None. **Not rendered.** |
| **F Data presentation** | No data, no simulated report, no placeholder chart. |
| **G Controls** | None. |
| **H Screen relationships** | None. `SCR-061` may state that espionage is excluded, but must not link here as a feature. |
| **I Responsive** | Desktop: no layout is deployed (screen absent). Tablet: no layout is deployed (screen absent). Mobile: no layout is deployed (screen absent). |
| **J Governing references** | Governing: B-10 §13.3 espionage exclusion; `13A-OQ-010`. Decisions: D-216. |
| **K Restrictions and notes** | **Provisional placeholder with no build authority.** B-10 excludes espionage and names no owner prompt. A future owner-authorized B-10 rule is required before any intelligence surface, and this row must then be respecified rather than assumed. |

## 8. World and progression — SCR-069…SCR-078

### SCR-069 — Events Centre

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Dashboard`; governing **B-11**; related `REQ-704–763`; new `REQ-938`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility public/eligible per event. |
| **B Purpose** | The world's current and scheduled events from the closed B-11 catalogue. It solves "what is happening in the world" and routes to event detail without generating or simulating an event. |
| **C Entry and navigation** | Primary nav World. Destinations: `SCR-070` event detail, `SCR-018` Network View, `SCR-071` objectives. Return: `SCR-015`. |
| **D Information hierarchy** | 1) Active events and their states. 2) Scheduled events. 3) Eligibility and duration. 4) Consequences summary. 5) History. 6) Definitions. |
| **E Layout** | `P-DASH`. Active event cards, schedule strip, world summary, context panel. |
| **F Data presentation** | • Event class — calendar/state/challenge/commemorative, current. • State — scheduled/active/resolved/expired. • Eligibility — current. • Duration — turns. • Consequence — registered effect link. • No invented event or effect. |
| **G Controls** | • `Open event` → `SCR-070`. • Filter by class/state. No create-event control exists. |
| **H Screen relationships** | `SCR-070`; `SCR-018`; `SCR-071`; `SCR-076`; `SCR-013`. |
| **I Responsive** | Desktop: active cards + schedule. Tablet: stacked. Mobile: active events first, schedule compact; eligibility visible per card. |
| **J Governing references** | Governing: WEP-633/713; WPC-14; WEP-040/081. Decisions: D-210. |
| **K Restrictions and notes** | The UI never creates an event or an effect. No live-ops authoring surface exists for players. Event frequency and payout remain outside B-13. |

### SCR-070 — Event detail & consequence view

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Object page`; governing **B-11**; related `REQ-704–763`; new `REQ-939`; class **Mandatory**; audience eligible players; permissions per event; visibility per event. |
| **B Purpose** | Explains one event: cause/hazard, registered consequence, eligibility, duration and history. It solves "what does this event do to me" and supports preparation. |
| **C Entry and navigation** | `SCR-069`, digest, alert. Destinations: `SCR-069`, owning affected screens, `SCR-076`. Return: `SCR-069`. |
| **D Information hierarchy** | 1) Event identity and state. 2) Cause/hazard. 3) Registered consequence. 4) Eligibility and duration. 5) Affected quantities. 6) History/definitions. |
| **E Layout** | `P-OBJ`. Event header, cause→consequence pair, effect table, eligibility panel, timeline, methodology. |
| **F Data presentation** | • Event identity — registered ID/class. • Cause — published state or calendar. • Consequence — exact registered effect. • Affected quantity — current/forecast. • Duration — turns. • No hidden modifier. |
| **G Controls** | • Links to affected screens where the player can respond. • `Dismiss` only where the event permits; no effect-cancelling control unless a rule provides one. |
| **H Screen relationships** | `SCR-069`; affected economic/political/war screens; `SCR-076`; `SCR-071`. |
| **I Responsive** | Desktop: cause/consequence columns. Tablet: stacked. Mobile: cause then consequence, effect table as cards; duration visible. |
| **J Governing references** | Governing: WEP-179/619. Decisions: D-210. |
| **K Restrictions and notes** | No unregistered effect. No hidden modifier. The screen does not reveal a suppressed aggregate through the effect quantity. |

### SCR-071 — Objectives & Challenges

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Register/list`; governing **B-11**; related `REQ-704–763`; new `REQ-940`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility own objectives private, public taxonomy. |
| **B Purpose** | The full objectives surface across twelve categories. It solves "what can I aim for" and supports accepting, progressing or dismissing optional objectives. |
| **C Entry and navigation** | World nav, `SCR-009`. Destinations: owning condition screens, `SCR-073` achievements, `SCR-074` progress. Return: `SCR-069`. |
| **D Information hierarchy** | 1) Active objectives and progress. 2) Available categories. 3) Optionality/dismissal. 4) Rewards by class. 5) History. 6) Definitions. |
| **E Layout** | `P-REG`. Category tabs, objective cards/table, progress, dismissal, history. |
| **F Data presentation** | • Category — `OBJ-FOLLOW`…`OBJ-LONG`. • Condition — owning-state reference. • Progress — current, tiered partial credit. • Optionality — true/false. • Reward — class, not a promise beyond the rule. • Expiry/grace — turns. |
| **G Controls** | • `Accept` where the flow supports it. • `Dismiss` — penalty-free; outcome may return. • `Open condition` → owning screen. No control forces another player's participation. |
| **H Screen relationships** | `SCR-009`; `SCR-073`; `SCR-074`; owning condition screens. |
| **I Responsive** | Desktop: category columns/list. Tablet: tabs. Mobile: category accordion, objective cards; dismissal reachable. |
| **J Governing references** | Governing: WEP-203…215; D-147; AP-004. Decisions: D-210. |
| **K Restrictions and notes** | No objective may require presence, membership, spending or aggression. No mandatory sequence beyond B-03's first session. No penalty for absence. |

### SCR-072 — Standings (named lists)

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Register/list`; governing **B-11**; related `REQ-728` region; new `REQ-941`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility public/disclosed aggregates. |
| **B Purpose** | The named standings with denominator and window. It solves "where does a nation stand in a named measure" without a live or composite rank. |
| **C Entry and navigation** | World nav, profile, `SCR-074`. Destinations: `SCR-010` profile, `SCR-018` network, `SCR-074`. Return: `SCR-015`. |
| **D Information hierarchy** | 1) Named list and value. 2) Denominator, eligibility and window. 3) Rank/percentile within the list. 4) Computation/publish turn. 5) Historical. 6) Definitions. |
| **E Layout** | `P-REG`. Standings tabs (`ST-DEV`…`ST-SEA`), ranking table, summary panel, filters, history. |
| **F Data presentation** | • Standing — named, exact value. • Rank/percentile — within the denominator. • Denominator — population. • Eligibility — set. • Window — turns. • Computed/published — P6/P7 turns. • Suppression — k=5. • No composite score. |
| **G Controls** | • Tab/filter. • `Open nation` → `SCR-010`. • `Compare` only within visibility-legal inputs. No "my rank" widget that implies live refresh. |
| **H Screen relationships** | `SCR-010`; `SCR-074`; `SCR-018`; `SCR-077` (after gate). |
| **I Responsive** | Desktop: table + summary. Tablet: pinned nation column. Mobile: list cards with rank/value; denominator/window pinned at top. |
| **J Governing references** | Governing: WEP-324/325/359/361/362. Supporting: `13A-BP-005`, `13A-DR-007`. Decisions: D-210. |
| **K Restrictions and notes** | A display without a denominator is a defect. No live-updating rank. No overall "best nation" ladder. Ties and ineligible states are explicit. |

### SCR-073 — Achievements & rewards

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Register/list`; governing **B-11**; related `REQ-704–763`; new `REQ-942`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility own rewards private; public disclosed rewards. |
| **B Purpose** | The achievements and reward classes, earned and locked. It solves "what have I achieved" and supports recognition without a material advantage fantasy. |
| **C Entry and navigation** | World nav, `SCR-071`, `SCR-075`. Destinations: `SCR-074` progress, `SCR-075` history. Return: `SCR-069`. |
| **D Information hierarchy** | 1) Earned achievements. 2) Available/locked achievements. 3) Reward class and grant state. 4) Progress. 5) History. 6) Definitions. |
| **E Layout** | `P-REG`. Earned grid, locked list, reward class panel, history link. |
| **F Data presentation** | • Achievement — name, class, state. • Reward class — `RECOGNITION`/`RECORD`/`AUTHORSHIP`/`COSMETIC`/`TITLE`/`MATERIAL`. • Grant — turn, owner key. • No another nation's reward. • Public list — disclosed only, k=5. |
| **G Controls** | • `Open reward` where a record exists. • Filter. No claim control unless a deferred claim flow exists. |
| **H Screen relationships** | `SCR-075`; `SCR-074`; `SCR-071`. |
| **I Responsive** | Desktop: grid + list. Tablet: grid wraps. Mobile: earned cards first, locked list; reward class visible. |
| **J Governing references** | Governing: WEP-499/663. Decisions: D-210. |
| **K Restrictions and notes** | No reward grants a power not defined by B-11. Material reward notice states class, quantity and owner key. No another nation's private reward. |

### SCR-074 — National Progress (eight layers)

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Dashboard`; governing **B-11**; related `REQ-704–763`; new `REQ-943`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility private plus public milestones. |
| **B Purpose** | The eight progression layers as separate registers. It solves "how is my nation progressing" without collapsing it into a single score. |
| **C Entry and navigation** | World nav, `SCR-073`. Destinations: `SCR-073`, `SCR-072`, `SCR-075`, `SCR-017`. Return: `SCR-069`. |
| **D Information hierarchy** | 1) The eight layers and current state. 2) Milestones/achievements within each. 3) Historical records. 4) Next available progression. 5) History. 6) Definitions. |
| **E Layout** | `P-DASH`. Layer cards, milestone list, historical record panel, next-step links. |
| **F Data presentation** | • Layer — permanent achievements, national milestones, historical records/chronicle, seasonal achievements, temporary competitive recognition, honour classes, authorship unlocks, cosmetic recognition. • State — current. • Progress — where defined. • No composite score. |
| **G Controls** | • `Open layer` → owning surface. • `View achievements` → `SCR-073`. No control purchases progression. |
| **H Screen relationships** | `SCR-073`; `SCR-075`; `SCR-072`; `SCR-017`. |
| **I Responsive** | Desktop: layer cards 2×4. Tablet: 2 columns. Mobile: stacked layer cards; no merged score. |
| **J Governing references** | Governing: WEP-423. Decisions: D-210. |
| **K Restrictions and notes** | No composite headline. No progression by attendance. No purchased progression. The eight layers remain separate. |

### SCR-075 — Reward History

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Register/list`; governing **B-11**; related `REQ-704–763`; new `REQ-944`; class **Mandatory**; audience authenticated players; permissions authenticated; visibility private. |
| **B Purpose** | The full reward record including deferred claims and corrections. It solves "what did I receive, when, and is anything still deferred" and supports audit. |
| **C Entry and navigation** | World nav, `SCR-073`, `SCR-074`. Destinations: `SCR-073`, `SCR-017`. Return: `SCR-069`. |
| **D Information hierarchy** | 1) Deferred claims (visible). 2) Granted rewards. 3) Voided/corrected records. 4) Turn and source. 5) Retention. 6) Definitions. |
| **E Layout** | `P-REG`. Deferred panel, history table, filter, retention label. |
| **F Data presentation** | • Reward — class, quantity, source. • State — granted/deferred/voided/corrected. • Turn — historical. • Deferred — visible, not granted. • Correction — appended, not edited. |
| **G Controls** | • Filter. • `Open source` — link. No manual claim/undo unless the rule provides one. |
| **H Screen relationships** | `SCR-073`; `SCR-074`; `SCR-017`; `SCR-031` for material ledger. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: reward cards with state; deferred section first. |
| **J Governing references** | Governing: WEP-633/663/705. Decisions: D-210. |
| **K Restrictions and notes** | Deferred claims stay visible. Voiding never deletes the record; corrections append. No reward is silently granted or removed. |

### SCR-076 — World Chronicle

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Register/list`; governing **B-11**; related `REQ-704–763`; new `REQ-945`; class **Mandatory**; audience any viewer; permissions per record; visibility public/disclosed. |
| **B Purpose** | The public world-history record. It solves "what has happened in the world" and supports context and lore without private data. |
| **C Entry and navigation** | World nav, event/war/reward records. Destinations: cited objects, `SCR-017` own chronicle. Return: `SCR-069`. |
| **D Information hierarchy** | 1) Dated world entries. 2) Event/war/milestone class. 3) Participants and outcome. 4) Public/restricted label. 5) Filters. 6) Definitions. |
| **E Layout** | `P-REG`. Timeline/table, filter, entry detail, retention label. |
| **F Data presentation** | • Entry — public world record, historical. • Class — event/war/treaty/progression. • Participants — public identities. • Outcome — settled. • Restricted — absent or labelled. • Retention — public/permanent. |
| **G Controls** | • Filter/saved view. • `Open object` — link. No edit/delete. |
| **H Screen relationships** | `SCR-017`; `SCR-069`; `SCR-070`; `SCR-063`; `SCR-050`. |
| **I Responsive** | Desktop: timeline + detail. Tablet: list. Mobile: dated cards; class filter in a drawer. |
| **J Governing references** | Governing: B-11 chronicle; D-026; TR-049. Decisions: D-210. |
| **K Restrictions and notes** | No private nation data, moderator note or inferred motive. A restricted fact is never inferable from a gap in the record. |

### SCR-077 — World Health aggregates (Conditional)

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Dashboard`; governing **B-11**; related `REQ-704–763`; new `REQ-946`; class **Conditional**; audience authenticated players when gate passes; permissions authenticated; visibility public aggregates with k=5 per figure. |
| **B Purpose** | Would present world-health aggregates only after each figure passes the disclosure gate. It solves "how healthy is the world" without leaking small groups. |
| **C Entry and navigation** | None until the per-figure k=5 check passes; then World nav. Destinations: `SCR-072`, `SCR-069`. Return: `SCR-069`. |
| **D Information hierarchy** | **When enabled:** 1) Figures passing k=5. 2) Window and sample count. 3) Suppressed figures as named states. 4) Source/methodology. 5) History. 6) Definitions. |
| **E Layout** | `P-DASH`. Chart/graph cards with suppression states. **Not rendered while Conditional.** |
| **F Data presentation** | • Aggregate — per figure, only if ≥5 contributors with complementary suppression. • Window — turns. • Sample count — contributors. • Suppressed — named state, not zero. • No pre-gate chart or axis. |
| **G Controls** | • Period selector where the rule defines windows. • No drill-down that would reveal a suppressed group. |
| **H Screen relationships** | `SCR-072`; `SCR-069`; `SCR-018`. |
| **I Responsive** | Desktop: chart grid. Tablet: stacked. Mobile: chart cards with text alternative; suppression visible. **No layout deployed pre-gate.** |
| **J Governing references** | Governing: D-027; WEP-663; `13A-SRC-015` pattern only. Decisions: D-216. |
| **K Restrictions and notes** | **Conditional.** Every figure must pass k=5 independently; complementary suppression applies; no differencing. A figure that fails is suppressed, not zero. No world chart before the gate. |

### SCR-078 — World Guide & glossary (in-context help index)

| Field | Specification |
|---|---|
| **A Identity** | Parent **World**; category `Guide/help`; governing **all B-systems**; related `REQ-044` region; new `REQ-947`; class **Mandatory**; audience any viewer; permissions public read; visibility public. |
| **B Purpose** | The in-product help layer keyed to the same section vocabulary as the navigation. It solves "what does this mean" without sending players to a wiki or Discord. |
| **C Entry and navigation** | Footer, every governing-rule anchor, `SCR-001` excerpt, `SCR-087`. Destinations: the screen being explained, glossary entries, `SCR-088`. Return: the originating screen. |
| **D Information hierarchy** | 1) Search/jump by section or term. 2) The explanation. 3) The governing rule anchor and exact ID. 4) Related screens. 5) Examples. 6) Change history. |
| **E Layout** | `P-GUIDE`. Index by the eight sections + Public/Admin exclusion; article pane; rule anchor; related links. |
| **F Data presentation** | • Term — definition, public. • Rule anchor — canonical ID, public. • Section — nav name. • Change — dated record. • No gameplay-critical value only in the guide. |
| **G Controls** | • Search field. • Section index. • `Go to screen` — permitted destination. No action control; the guide never grants a capability. |
| **H Screen relationships** | All screens via help; `SCR-087`; `SCR-088`; `SCR-001`. |
| **I Responsive** | Desktop: index + article. Tablet: drawer index. Mobile: accordion index, search, readable measure. |
| **J Governing references** | Governing: F-010; DP-004; `13A-BP-009`, `13A-DR-010`. Decisions: D-210. |
| **K Restrictions and notes** | No external wiki/Discord dependency. No proprietary benchmark text. Help uses the same section names as navigation. No gameplay text only in an image. |

## 9. Player protection and support — SCR-079…SCR-090

Privacy classes are `PUB`, `PLAYER`, `ALLIANCE`, `OPS`, `MOD`, `PERSONAL`, `SEC`, `AUDIT`, `LEGAL` (PRV-002/009). Class `SEC` is never displayed. Claim vocabulary is exactly `suspected`, `under review`, `confirmed`, `inconclusive` (EVD-009) and appears only in B-12 contexts.

### SCR-079 — Privacy settings centre

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Object page`; governing **B-12**; related `REQ-801`…`REQ-804`; new `REQ-948`; class **Mandatory**; audience account holder; permissions authenticated; visibility private. |
| **B Purpose** | Lists the nine privacy classes in player language and the settings the player controls. It solves "who can see what about me" and supports informed privacy choices. |
| **C Entry and navigation** | `SCR-011`, footer privacy link. Destinations: `SCR-080` security, `SCR-085` my data, `SCR-087` support. Return: `SCR-011`. |
| **D Information hierarchy** | 1) What each privacy class means. 2) Which settings the player controls. 3) What is fixed by rule (not a setting). 4) Data/export. 5) Change history. 6) Definitions. |
| **E Layout** | `P-OBJ`. Class list, setting controls, fixed-by-rule panel, data link, history. |
| **F Data presentation** | • Each class — name, meaning, what it covers. • Setting — current. • Fixed-by-rule facts — labelled, not toggleable. • No `SEC` content, examples or values. • Change history — dated. |
| **G Controls** | • Toggle/select only for settings the rules actually expose; disabled controls explain. • `My data` → `SCR-085`. • No control can widen another player's visibility. |
| **H Screen relationships** | `SCR-011`; `SCR-080`; `SCR-085`; `SCR-084`. |
| **I Responsive** | Desktop: class list + settings. Tablet: stacked. Mobile: class accordion, settings as cards; fixed-by-rule panel visible. |
| **J Governing references** | Governing: PRV-002/009/014. Decisions: D-203. |
| **K Restrictions and notes** | `SEC` never appears. A privacy setting is not a security control. No dark pattern default. No hidden change to another player's visibility. |

### SCR-080 — Security settings (sessions, recovery codes, e-mail change)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Object page`; governing **B-03/B-12**; related `REQ-768` region; new `REQ-949`; class **Mandatory**; audience account holder; permissions authenticated; visibility private. |
| **B Purpose** | Manages sessions, recovery-code custody and e-mail change. It solves "keep my account secure" and supports safe credential lifecycle. |
| **C Entry and navigation** | `SCR-011`, `SCR-079`, `SCR-005` after recovery. Destinations: `SCR-005`, `SCR-079`, `SCR-011`. Return: `SCR-011`. |
| **D Information hierarchy** | 1) Current sessions. 2) Recovery-code custody state. 3) E-mail change with dual confirmation. 4) Verification state. 5) Security notices. 6) Definitions. |
| **E Layout** | `P-OBJ`. Session table, recovery-code panel, e-mail change form, verification state, notices. |
| **F Data presentation** | • Sessions — device/date summary, never tokens. • Recovery codes — count/custody state, never values after generation. • E-mail — masked; verification state. • Changes — dated history. • No passwords/keys. |
| **G Controls** | • `Revoke session` — committing; confirmation. • `Generate recovery codes` — one-time display, confirmation; outcome codes shown once, then only hashes. • `Change e-mail` — dual confirmation; committing. Every control requires re-authentication where D-041 requires it. |
| **H Screen relationships** | `SCR-011`; `SCR-005`; `SCR-079`; `SCR-012`. |
| **I Responsive** | Desktop: sessions + panels. Tablet: stacked. Mobile: sessions first, recovery/e-mail in cards; one-time codes in a protected view with a copy warning. |
| **J Governing references** | Governing: D-029; D-041; ACC-031; REQ-768. Decisions: D-041. |
| **K Restrictions and notes** | Never re-display a recovery code. Dual confirmation for e-mail change. No raw token, key or session secret. Verification is shown as a state, not a score. |

### SCR-081 — Report creation

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Task/compose`; governing **B-12**; related `REQ-821`/`REQ-822`; new `REQ-950`; class **Mandatory**; audience authenticated player; permissions authenticated; visibility private; intake may be degraded. |
| **B Purpose** | Submits a conduct report with exactly the MOD-002 fields. It solves "how do I report a problem safely" and supports a traceable accusation with evidence. |
| **C Entry and navigation** | `SCR-010` report action, footer, `SCR-087`. Destinations: `SCR-082` after submission, `SCR-087` support (separate route). Return: originating screen. |
| **D Information hierarchy** | 1) Category and subject. 2) Time window and free-text account. 3) Separately stored supplied evidence. 4) Reporter account (implicit). 5) Acknowledgement/retry state. 6) What happens next. |
| **E Layout** | `P-TASK`. Intake form, evidence upload/reference, acknowledgement panel, intake-availability state. |
| **F Data presentation** | • Category — controlled list. • Subject — public identity or content reference. • Time window — turns/UTC. • Reporter — own account, private. • Free text — private. • Evidence — separate store, private. • Case reference — generated after submission. |
| **G Controls** | • `Submit report` — committing; preconditions required fields; confirmation states the report is an accusation and the process; outcome acknowledgement + case reference. • `Cancel`. • Degraded intake: submit disabled with retryable failure, report not silently lost. |
| **H Screen relationships** | `SCR-082`; `SCR-087`; `SCR-010`; `SCR-083`. |
| **I Responsive** | Desktop: form + guidance. Tablet: stacked. Mobile: stepped form, evidence picker accessible, acknowledgement visible. |
| **J Governing references** | Governing: MOD-002/007; FR-001/006. Supporting: `13A-PR-10`. Decisions: D-214. |
| **K Restrictions and notes** | Exactly MOD-002 fields; no extra mandatory field. Support and conduct reporting are separate routes. No report is silently lost. No public accusation. |

### SCR-082 — Report status & decision view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Detail record`; governing **B-12**; related `REQ-826`/`REQ-831`; new `REQ-951`; class **Mandatory**; audience reporter; permissions reporter; visibility private. |
| **B Purpose** | Shows the report's status and the decision notice with MOD-017's seven elements. It solves "what happened to my report" with honest claim tiers. |
| **C Entry and navigation** | Report receipt, `SCR-084`, `SCR-083`. Destinations: `SCR-083` appeal, `SCR-081` new report. Return: `SCR-011`. |
| **D Information hierarchy** | 1) Status and claim tier. 2) The seven notice elements. 3) What is withheld and why. 4) Appeal route. 5) Case timeline. 6) Definitions. |
| **E Layout** | `P-STATE`. Status banner, seven-element notice, claim badge, appeal action, timeline. |
| **F Data presentation** | • `V-` class — violation class. • Rule element. • Evidence class. • Tier `T0`…`T5` where applicable. • End condition. • Appeal route. • Correction if any. • Claim tier — `suspected`/`under review`/`confirmed`/`inconclusive`. • Methods/thresholds/third-party data — withheld. |
| **G Controls** | • `Appeal` → `SCR-083` when the tier permits. • `View timeline`. No control changes a decision. |
| **H Screen relationships** | `SCR-083`; `SCR-084`; `SCR-081`; `SCR-087`. |
| **I Responsive** | Desktop: notice + timeline. Tablet: stacked. Mobile: status and seven elements first; appeal action visible; withheld explanation collapsible. |
| **J Governing references** | Governing: MOD-017/018; EVD-009. Decisions: D-210. |
| **K Restrictions and notes** | Seven elements exactly. Claim tiers never upgraded silently. `T0` has no appeal; `T1`+ appeal route. No detection method, threshold or third-party data. |

### SCR-083 — Appeal view

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Task/compose`; governing **B-12**; related `REQ-833`/`REQ-848`; new `REQ-952`; class **Mandatory**; audience sanctioned player; permissions authenticated; visibility private. |
| **B Purpose** | Files and tracks an appeal, and remains reachable under every restriction. It solves "how do I challenge this" with a never-blocked route. |
| **C Entry and navigation** | Decision notice, `SCR-084`, account home. Destinations: `SCR-082` case, `SCR-087` support, `SCR-011`. Return: `SCR-084`/`SCR-011`. |
| **D Information hierarchy** | 1) Appeal eligibility and route. 2) Grounds and statement. 3) Status ladder. 4) Decision reasons. 5) What happens next. 6) Definitions. |
| **E Layout** | `P-TASK`. Eligibility panel, appeal form, status ladder, decision panel. |
| **F Data presentation** | • Appeal status — submitted/under review/decided/remanded. • Grounds — player text. • Decision — outcome and reasons. • Ladder — tiers permitted. • Never: another player's data or a security method. |
| **G Controls** | • `Submit appeal` — committing; confirmation; outcome status update. • `Withdraw` only if permitted. • The route is present even when other channels are restricted. |
| **H Screen relationships** | `SCR-082`; `SCR-084`; `SCR-087`; `SCR-011`. |
| **I Responsive** | Desktop: form + ladder. Tablet: stacked. Mobile: eligibility and form first; status ladder compact; submit not hidden by a restriction banner. |
| **J Governing references** | Governing: MOD-013/015; MOD-042; REQ-833/848. Decisions: D-210. |
| **K Restrictions and notes** | A communication restriction never blocks the appeal route or security notices. No invented appeal outcome or extra tier. No retaliation surface. |

### SCR-084 — Restrictions & sanctions view (player-visible)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Status/state`; governing **B-03/B-12**; related `REQ-865` region; new `REQ-953`; class **Mandatory**; audience restricted account holder; permissions authenticated; visibility private to the subject. |
| **B Purpose** | Explains a restriction's kind, scope, end/review turn and appeal route without accusation or confidential detail. It solves "why am I limited" and supports recourse. |
| **C Entry and navigation** | Account home, decision/restriction notice, login state. Destinations: `SCR-083` appeal, `SCR-086` review explanation, `SCR-080` security. Return: `SCR-011`. |
| **D Information hierarchy** | 1) Restriction kind. 2) Scope (what is limited) and end/review turn. 3) Reason class permitted by rule. 4) Appeal route. 5) Review explanation. 6) Support. |
| **E Layout** | `P-STATE`. Restriction banner, scope table, review/end panel, appeal action, review-explanation link. |
| **F Data presentation** | • Restriction kind — communication, capability, suspension, pair restriction, security hold. • Scope — named channels/actions. • End/review — turns. • Reason class — permitted text, no method/threshold. • No other player's data, no public accusation, no `SEC` content. |
| **G Controls** | • `Appeal` → `SCR-083`. • `View review explanation` → `SCR-086`. • No control lifts the restriction. |
| **H Screen relationships** | `SCR-083`; `SCR-086`; `SCR-080`; `SCR-011`. |
| **I Responsive** | Desktop: banner + scope. Tablet: stacked. Mobile: kind/scope/end first; appeal visible; no hidden restriction. |
| **J Governing references** | Governing: NET-023/050; PRV-019; MOD-027; ACC-018. Decisions: D-210. |
| **K Restrictions and notes** | A pair restriction is not a suspension (D-031). No public accusation. No technical exposure. The restriction is never published on a nation page, ranking or feed. |

### SCR-085 — My data: access, export, retention disclosures

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Register/list`; governing **B-03/B-12**; related `REQ-805` region; new `REQ-954`; class **Mandatory**; audience account holder; permissions authenticated; visibility private. |
| **B Purpose** | Lists the player's data categories, access/export requests and retention. It solves "what do you hold about me and for how long" and supports data-subject routes. |
| **C Entry and navigation** | `SCR-011`, `SCR-079`. Destinations: `SCR-079`, `SCR-012`, `SCR-087`. Return: `SCR-011`. |
| **D Information hierarchy** | 1) Data categories. 2) Access/export request state. 3) Retention by class. 4) Erasure vs audit-spine obligation. 5) Correction route. 6) Definitions. |
| **E Layout** | `P-REG`. Category table, request panel, retention table, correction link. |
| **F Data presentation** | • Category — `S`, `P`, `O`, `SPINE` purpose classes. • Retention — 30 days hot/12 monthly/permanent/class-O ≥12 months. • Request state — pending/fulfilled. • Erasure — what can be erased vs spine retained. • No `SEC` content. |
| **G Controls** | • `Request export` — committing; confirmation; outcome request registered. • `Request correction` — committing. • `Request erasure` where the rule permits; explains the audit-spine exception. |
| **H Screen relationships** | `SCR-079`; `SCR-012`; `SCR-087`; `SCR-084`. |
| **I Responsive** | Desktop: tables. Tablet: stacked. Mobile: category cards, retention table; request actions in a separate section. |
| **J Governing references** | Governing: D-026; DAT-001; PRV-001/023; REQ-805. Decisions: D-026. |
| **K Restrictions and notes** | No invented day-count. Erasure never deletes the audit spine. No export of another player's data. No security internals. |

### SCR-086 — Review explanation surfaces (shared-network)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Status/state`; governing **B-03/B-12**; related `REQ-865` region; new `REQ-955`; class **Mandatory**; audience player under shared-network review; permissions authenticated; visibility private. |
| **B Purpose** | Explains a shared-network state and what clearance means. It solves "why am I under review and what happens" without exposing the matching mechanism. |
| **C Entry and navigation** | `SCR-084`, restriction notice. Destinations: `SCR-083` appeal, `SCR-084`, `SCR-087`. Return: `SCR-084`. |
| **D Information hierarchy** | 1) State name (`NONE`/`OBSERVED`/`RESTRICTED`/`CLEARED`/`MAINTAINED`). 2) What it means. 3) What is limited. 4) Review status and observation window in turns. 5) Appeal/correction route. 6) Definitions. |
| **E Layout** | `P-STATE`. State banner, meaning panel, limitation scope, observation window, recourse. |
| **F Data presentation** | • Pair/network state — five D-034 states. • Review status — separate field. • Observation window — turns. • Limitations — named. • No network key, IP, matching threshold or other account identity. |
| **G Controls** | • `Appeal` → `SCR-083`. • `Request correction` where a wrong association is suspected. No control clears the state. |
| **H Screen relationships** | `SCR-084`; `SCR-083`; `SCR-087`. |
| **I Responsive** | Desktop: state + scope. Tablet: stacked. Mobile: state and review status first; recourse visible. |
| **J Governing references** | Governing: D-033/D-034; NET-023; REQ-865. Decisions: D-210. |
| **K Restrictions and notes** | No technical exposure. A wrong-account association has a correction path. A pair state is private and never published. No accusation. |

### SCR-087 — Support centre (help shell and contact)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Guide/help`; governing **B-12**; related `REQ-821` region; new `REQ-956`; class **Mandatory**; audience authenticated player; permissions authenticated; visibility private. |
| **B Purpose** | Separates support contact from conduct reporting and hosts the help shell. It solves "I need help, not a report" and supports safe intake routing. |
| **C Entry and navigation** | Footer, `SCR-011`, `SCR-078`. Destinations: `SCR-078` guide, `SCR-081` report, `SCR-011`. Return: origin. |
| **D Information hierarchy** | 1) Support categories. 2) Contact/request form. 3) Distinction from a conduct report. 4) Status of an existing request. 5) Help index. 6) Definitions. |
| **E Layout** | `P-GUIDE`. Support category list, form, report-vs-support notice, existing-request link, help index. |
| **F Data presentation** | • Category — account, technical, billing-if-any, other. • Request state — open/answered. • No moderation case data. • No security internals. |
| **G Controls** | • `Contact support` — committing; confirmation; outcome request registered. • `Open guide` → `SCR-078`. • `Report conduct` → `SCR-081` (explicit route change). |
| **H Screen relationships** | `SCR-078`; `SCR-081`; `SCR-011`; `SCR-082`. |
| **I Responsive** | Desktop: categories + form. Tablet: stacked. Mobile: category cards, form, clear route separation. |
| **J Governing references** | Governing: B-12 intake taxonomy; FR-001. Decisions: D-210. |
| **K Restrictions and notes** | Support is not moderation. A support request does not create a case. The UI never promises an outcome. |

### SCR-088 — Change disclosures (changelog-grade)

| Field | Specification |
|---|---|
| **A Identity** | Parent **World** (alias Home); category `Register/list`; governing **B-02/B-12**; related `TR-049`; new `REQ-957`; class **Mandatory**; audience any viewer; permissions public where disclosure permits; visibility public. |
| **B Purpose** | Publishes dated, player-readable changes and incident notices. It solves "what changed and when" with an official record. |
| **C Entry and navigation** | Footer, `SCR-019`, Home alias. Destinations: affected guide entries, `SCR-078`, `SCR-001`. Return: origin. |
| **D Information hierarchy** | 1) Recent dated changes. 2) Rule-affecting changes. 3) Security/incident notices within limits. 4) Affected systems. 5) Archive. 6) Definitions. |
| **E Layout** | `P-GUIDE`. Dated entries, expandable detail, category filter, archive. |
| **F Data presentation** | • Date — publication, historical. • Change — player-readable description. • Affected system — section. • Incident notice — disclosure-limited. • No private case, method or player identity. |
| **G Controls** | • Expand entry. • Filter. • `Open affected screen` where applicable. No edit control. |
| **H Screen relationships** | `SCR-078`; `SCR-019`; `SCR-001`; `SCR-087`. |
| **I Responsive** | Desktop: list + detail. Tablet: list. Mobile: dated accordion. |
| **J Governing references** | Governing: TR-049; MOD-017/018; `13A-BP-012`, `13A-DR-014`. Decisions: D-210. |
| **K Restrictions and notes** | No private case, detection method, security secret or another player's identity. The changelog is an official record, not a marketing feed. |

### SCR-089 — Protection state view (newcomer/return protection)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Home**; category `Status/state`; governing **B-03**; related `REQ-090`; new `REQ-958`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private (state may be public where the rule allows). |
| **B Purpose** | Displays protection as a state with an end turn and explains its limits. It solves "am I protected and until when" without a countdown or a bonus claim. |
| **C Entry and navigation** | Shell badge, `SCR-015`, block moments (`SCR-061`/`SCR-063`). Destinations: `SCR-015`, `SCR-061`, `SCR-011`. Return: origin. |
| **D Information hierarchy** | 1) Protection state. 2) End turn/date. 3) What protection does and does not do. 4) How it ends. 5) Historical protection. 6) Definitions. |
| **E Layout** | `P-STATE`. State banner, `protected until Turn N` / `protection ended`, effect panel, end conditions, history. |
| **F Data presentation** | • State — active/ended, current. • End turn — target. • Effect — visibility-only, no yield/resource/score bonus. • End conditions — 7 days/84 turns or first offensive action; not extended by login/attack/posting. • Pair-skip — rule note. • Never re-granted after reroll/recovery/replacement. |
| **G Controls** | Read-only. • `View wars` → `SCR-062`. • `View protection rule` → `SCR-078`. No control extends protection. |
| **H Screen relationships** | `SCR-015`; `SCR-061`; `SCR-063`; `SCR-090`; `SCR-009`. |
| **I Responsive** | Desktop: state + effect. Tablet: stacked. Mobile: state and end turn pinned; explanation collapsible. |
| **J Governing references** | Governing: ONB-020/022; D-040; WAR-115…117. Decisions: D-210. |
| **K Restrictions and notes** | Protection is visibility-only and not re-granted. It ends at a turn boundary, not a hidden timer. It is not a bonus and not a shield from all consequences. Execution-time protection is authoritative (WAR-116). |

### SCR-090 — Reroll confirmation (exact-phrase destructive page)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Account**; category `Task/compose`; governing **B-03**; related `REQ-089`/`REQ-090`; new `REQ-959`; class **Mandatory**; audience nation owner; permissions authenticated; visibility private. |
| **B Purpose** | The guarded reroll/destructive reset flow. It solves "start over" with full consequence disclosure and an exact-phrase barrier. |
| **C Entry and navigation** | `SCR-011`, account menu. Destinations: `SCR-007` replacement creation on success, `SCR-011` cancel. Return: `SCR-011`. |
| **D Information hierarchy** | 1) What reroll destroys permanently. 2) What survives (sanctions, retention). 3) Replacement and protection facts. 4) Block conditions. 5) Exact-phrase confirmation. 6) Cancel path. |
| **E Layout** | `P-TASK`. Consequence list, block-condition panel, exact-phrase field, destructive confirm, cancel as the safe primary. |
| **F Data presentation** | • Permanent reset — name, nation, history, assets, relationships. • No undo. • Losses — enumerated. • Sanctions survive. • Immediate replacement — allowed. • No first-nation protection renewal. • Block conditions — active campaign, settlement, hold. |
| **G Controls** | • Re-authentication within 5 minutes — required. • Exact current nation name — required. • `Permanently delete [nation] and create a replacement` — committing, destructive; `OVL-02`; disabled with reason if blocked. • `Cancel` — always present, never destructive-styled. |
| **H Screen relationships** | `SCR-011`; `SCR-007`; `SCR-089`; `SCR-084`. |
| **I Responsive** | Desktop: consequence list + field + confirm. Tablet: stacked. Mobile: full-screen stepped confirmation; exact phrase full width; confirm separated; no accidental tap. |
| **J Governing references** | Governing: RRL-005/006/012/021; D-039; D-040. Decisions: D-214. |
| **K Restrictions and notes** | Exact-phrase confirmation; no remembered confirmation across turns. Reroll does not restore protection. Blocked while campaign/settlement/hold with the reason displayed. Surrender remains the in-war off-ramp. |

## 10. Administration — SCR-091…SCR-100

All ten screens live behind the separate role-gated Admin root (`UI-CMP-010`), outside the player shell navigation. Roles are `R-MOD`, `R-SMOD`, `R-APL`, `R-INV`, `R-SEC`, `R-OPS`, `R-AUD`, `R-EMG` (ADM-003). Least privilege, purpose-bound access, step-up and audited reads apply. No admin screen exposes `SEC` material to a role that may not read it; no player screen exposes admin chrome.

### SCR-091 — Admin console home (role-scoped index)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12**; related `REQ-838`…`REQ-846`; new `REQ-960`; class **Mandatory (admin)**; audience role holders; permissions any ADM role; visibility admin-only. |
| **B Purpose** | The role-scoped index of admin workspaces. It solves "what can I do with my role" and prevents traversal beyond it. |
| **C Entry and navigation** | Role-gated admin entry only. Destinations: only workspaces the role permits. Return: admin root. |
| **D Information hierarchy** | 1) Holder's role(s) and scope. 2) Permitted workspaces. 3) Step-up/emergency posture. 4) Audit notice. 5) Help/contact. 6) Definitions. |
| **E Layout** | `P-DASH` admin variant. Role card, workspace tiles, posture banner, audit notice. |
| **F Data presentation** | • Role — role name/scope. • Permitted workspaces — filtered. • Step-up/emergency — state. • No case data on the index. • No player data. |
| **G Controls** | • Workspace navigation only where permitted. • No control grants a role. |
| **H Screen relationships** | `SCR-092`…`SCR-100` as permitted. |
| **I Responsive** | Desktop: tile grid. Tablet: two columns. Mobile: single column tiles; role scope visible. |
| **J Governing references** | Governing: ADM-003/021/022; D-042; `13A-DR-013`. Decisions: D-218. |
| **K Restrictions and notes** | Role-gated; no player navigation; no case data on the index; denied routes do not confirm existence. Every workspace entry is audited where the rule requires. |

### SCR-092 — Moderation queue

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12**; related `REQ-865` region; new `REQ-961`; class **Mandatory (admin)**; audience `R-MOD`/`R-SMOD`; permissions moderator scope; visibility admin-only. |
| **B Purpose** | The triage queue of reports and cases assigned to the reviewer. It solves "what needs moderation attention" within role scope. |
| **C Entry and navigation** | `SCR-091`, case links. Destinations: `SCR-093` case, `SCR-094` sanctions where permitted, `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Assigned/unassigned cases. 2) Triage state and age. 3) Case class and claim tier. 4) Assignment. 5) Queue filters. 6) Definitions. |
| **E Layout** | `P-REG` admin. Queue table, filters, assignment, triage controls. |
| **F Data presentation** | • Case — identifier, class, claim tier. • Triage — new/assigned/under review/closed. • Age — turns. • Reporter/accused — only as permitted. • No `SEC` material. |
| **G Controls** | • `Assign to me` — permissioned, audited. • `Open case` → `SCR-093`. • `Escalate` — permissioned. No sanction decision on the queue. |
| **H Screen relationships** | `SCR-093`; `SCR-094`; `SCR-091`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: case cards with triage state; assignment in menu. |
| **J Governing references** | Governing: ADM-021/022; MOD ladder. Decisions: D-218. |
| **K Restrictions and notes** | No `SEC` read, evidence export, balance change or snapshot alteration for `R-MOD`. Queue access is purpose-bound and audited. |

### SCR-093 — Case & evidence workspace

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12**; related `REQ-822`…`REQ-832`; new `REQ-962`; class **Mandatory (admin)**; audience assigned reviewer and permitted roles; permissions case scope; visibility admin-only. |
| **B Purpose** | The case record and evidence matrix. It solves "what is the evidence and what does it support" with claim-tier discipline. |
| **C Entry and navigation** | `SCR-092`, `SCR-095`, `SCR-096`. Destinations: `SCR-094` sanctions, `SCR-092`, `SCR-096` audit. Return: `SCR-092`. |
| **D Information hierarchy** | 1) Case identity and claim tier. 2) Evidence matrix. 3) Violation class `V-01`…`V-16`. 4) Rule element. 5) History/notes. 6) Withheld data. |
| **E Layout** | `P-OBJ` admin. Case header, evidence matrix, violation panel, notes, action panel. |
| **F Data presentation** | • Case — identifier, class, state. • Claim tier — EVD-009 four terms. • Evidence — class and source, no raw `SEC`. • Violation class — exact. • Third-party data — withheld. • Notes — role-visible. |
| **G Controls** | • `Request escalation` — permissioned. • `Open sanctions` → `SCR-094` if permitted. • `Close/record` — permissioned; audited. No evidence export unless the role permits. |
| **H Screen relationships** | `SCR-092`; `SCR-094`; `SCR-096`; `SCR-095`. |
| **I Responsive** | Desktop: case + evidence columns. Tablet: stacked. Mobile: case header, evidence cards, actions in a menu. |
| **J Governing references** | Governing: EVD matrix; V-01…V-16; MOD-017/018. Decisions: D-218. |
| **K Restrictions and notes** | Methods and thresholds withheld by rule. Evidence read is audited. `R-MOD` cannot export or read `SEC`. The case record is not rewritten; corrections append. |

### SCR-094 — Sanctions administration (ladder, two-person rule)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12/B-08**; related `REQ-838`…`REQ-846`; new `REQ-963`; class **Mandatory (admin)**; audience `R-SMOD`, `R-APL`, `R-SEC` as permitted; permissions tier authority; visibility admin-only. |
| **B Purpose** | Applies and reviews sanctions on the six-tier ladder with separation of duties. It solves "apply the right measure lawfully" and prevents unilateral overreach. |
| **C Entry and navigation** | `SCR-093`, `SCR-092`. Destinations: `SCR-096` audit, `SCR-093`, `SCR-091`. Return: `SCR-093`. |
| **D Information hierarchy** | 1) Proposed tier and scope. 2) Evidence class required. 3) Two-person requirement. 4) End/review turn. 5) Appeal route. 6) Audit record. |
| **E Layout** | `P-TASK` admin. Tier ladder, scope panel, second-reviewer panel, effect/end panel, audit note. |
| **F Data presentation** | • Tier — `T0`…`T5` exact. • Scope — named capabilities/channels. • End — turns. • Review — second reviewer or `unsegregated`. • Appeal — route. • No `SEC` exposure to non-permitted roles. |
| **G Controls** | • `Propose measure` — committing; permissioned; confirmation. • `Second review` — required where staffing exists; outcome recorded. • `Apply` — committing; audited. No control exceeds the holder's tier authority. |
| **H Screen relationships** | `SCR-093`; `SCR-096`; `SCR-092`; `SCR-091`. |
| **I Responsive** | Desktop: ladder + scope + review. Tablet: stacked. Mobile: tier and scope first; destructive apply separated and confirmed. |
| **J Governing references** | Governing: MOD-036/037/042; MOD-022; ADM-009/010/011/013. Decisions: D-218. |
| **K Restrictions and notes** | Exactly six tiers; no parallel ladder or letter grade. Two-person rule where staffing exists; `unsegregated` otherwise. `T0` has no appeal; `T1`+ does. No sanction without evidence class. |

### SCR-095 — Shared-network review workspace

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-03/B-12**; related `REQ-777`…`REQ-783`; new `REQ-964`; class **Mandatory (admin)**; audience `R-INV`/`R-SEC`; permissions investigation scope; visibility admin-only. |
| **B Purpose** | Reviews shared-network associations with the five states and a separate review status. It solves "is this association legitimate" without exposing the matching mechanism. |
| **C Entry and navigation** | `SCR-091`, case links. Destinations: `SCR-093`, `SCR-096`, `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Five-state classification. 2) Separate review status. 3) Observation window in turns. 4) Evidence class. 5) Corrective path. 6) Definitions. |
| **E Layout** | `P-REG` admin. State table, review-status panel, window, corrective actions, audit note. |
| **F Data presentation** | • State — `NONE`/`OBSERVED`/`RESTRICTED`/`CLEARED`/`MAINTAINED`. • Review — separate status. • Window — turns. • Evidence — class only. • No raw IP, network key or threshold. |
| **G Controls** | • `Set review status` — permissioned, audited. • `Correct wrong association` — permissioned; separates accounts, lifts restrictions, records and notifies. • No control exposes the matching mechanism. |
| **H Screen relationships** | `SCR-093`; `SCR-094`; `SCR-096`; `SCR-091`. |
| **I Responsive** | Desktop: state + review. Tablet: stacked. Mobile: state cards; corrective action separated and confirmed. |
| **J Governing references** | Governing: D-033/D-034; NET-023; REQ-865. Decisions: D-218. |
| **K Restrictions and notes** | `RESTRICTED` is not automatically a suspension. Correcting a wrong association has a recorded correction path. No technical exposure, no public accusation. |

### SCR-096 — Audit ledger viewer

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12**; related `REQ-851`…`REQ-855`; new `REQ-965`; class **Mandatory (admin)**; audience `R-AUD` plus scoped roles; permissions audit read; visibility admin-only. |
| **B Purpose** | Reads the audit spine and preservation-order state. It solves "what happened and who did it" without exposing content bodies or secrets. |
| **C Entry and navigation** | `SCR-091`, case links. Destinations: `SCR-093`, `SCR-098`, `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Event set and time. 2) Actor/role and decision. 3) Object reference. 4) Preservation orders. 5) Access log of the audit read. 6) Definitions. |
| **E Layout** | `P-REG` admin. Event set filter, audit table, preservation panel, access log. |
| **F Data presentation** | • Event — identifier, time, actor, role, decision. • Object — reference, no content body. • No secret, credential or raw personal content. • Preservation — order state. • Access — itself recorded. |
| **G Controls** | • Filter/saved view. • `Open object` → permitted case/object. • `Apply preservation order` — permissioned, audited. No edit/delete of audit rows. |
| **H Screen relationships** | `SCR-093`; `SCR-098`; `SCR-094`; `SCR-091`. |
| **I Responsive** | Desktop: table. Tablet: priority columns. Mobile: audit cards with event/actor/decision; filters in a drawer. |
| **J Governing references** | Governing: SEC-021/036…040; EVD-026/028; REQ-851…855; D-042. Decisions: D-218. |
| **K Restrictions and notes** | Audit records contain identifiers, decisions and reasons, never content bodies, secrets or raw credentials. Correction appends. Access is purpose-bound and itself audited. |

### SCR-097 — Turn-engine operations monitor

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-02**; related `REQ-020`/`REQ-022`; new `REQ-966`; class **Mandatory (admin)**; audience `R-OPS`; permissions operations; visibility admin-only. |
| **B Purpose** | Monitors turn settlement, checkpoints and FAILED/INTERRUPTED recovery. It solves "is the turn engine healthy and how do we recover" without inventing success. |
| **C Entry and navigation** | `SCR-091`. Destinations: `SCR-096` audit, `SCR-016` player status (read-only), `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Current turn state. 2) Phase/checkpoint. 3) FAILED/INTERRUPTED state and recovery path. 4) Slot history. 5) Audit. 6) Definitions. |
| **E Layout** | `P-DASH` admin. Turn state, phase ladder, checkpoint list, failure panel, slot history. |
| **F Data presentation** | • Turn — display turn + UTC window. • State — `SCHEDULED`…`FAILED`. • Checkpoint — last completed. • Failure — code/reason. • Slot history — record. • No player data. |
| **G Controls** | • `Open incident` — permissioned. • Recovery action only where the B-02 operator path defines one; confirmation and audit. No silent re-run or state invention. |
| **H Screen relationships** | `SCR-096`; `SCR-016`; `SCR-091`. |
| **I Responsive** | Desktop: state + phases. Tablet: stacked. Mobile: state and failure first; actions separated. |
| **J Governing references** | Governing: TR-035/036/043/075/080. Decisions: D-218. |
| **K Restrictions and notes** | `FAILED` is a delay, not a lost turn. No phase effect is published before `COMPLETED`. The monitor does not grant gameplay powers. |

### SCR-098 — Data operations (retention, compaction, preservation)

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12**; related `REQ-805`…`REQ-809`; new `REQ-967`; class **Mandatory (admin)**; audience `R-SEC`/`R-AUD` as permitted; permissions data operations; visibility admin-only. |
| **B Purpose** | Runs retention, compaction and preservation operations with audit consequences. It solves "keep records lawful and recoverable" without destructive ambiguity. |
| **C Entry and navigation** | `SCR-091`, `SCR-096`. Destinations: `SCR-096`, `SCR-085` policy reference, `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Retention schedule by class. 2) Pending compaction. 3) Preservation orders. 4) Destructive-action consequences. 5) Audit. 6) Definitions. |
| **E Layout** | `P-REG` admin. Retention table, compaction queue, preservation panel, confirmation, audit. |
| **F Data presentation** | • Class — `S`/`P`/`O`/`SPINE`. • Retention — hot/12-month/permanent/class-O. • Compaction — pending/completed. • Preservation — active order. • No content bodies. |
| **G Controls** | • `Run compaction` — committing; permissioned; confirmation; idempotent; audited. • `Apply preservation order` — committing; audited. • Destructive operations require exact confirmation. |
| **H Screen relationships** | `SCR-096`; `SCR-085`; `SCR-091`. |
| **I Responsive** | Desktop: tables + action. Tablet: stacked. Mobile: retention cards; destructive action separated and confirmed. |
| **J Governing references** | Governing: D-026; PRV-023; COR rules; REQ-805…809. Decisions: D-218. |
| **K Restrictions and notes** | Compaction is idempotent. The audit spine is not compacted away. No operation is presented as reversible when it is not. No new day-count is invented. |

### SCR-099 — Announcement / global notice composer

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12/B-09**; related `REQ-826` region; new `REQ-968`; class **Mandatory (admin)**; audience authorised announcement role; permissions announcement; visibility admin-only composer, public output where published. |
| **B Purpose** | Composes official global notices within MOD-017/018 content rules. It solves "how do we announce a change" without leaking case data. |
| **C Entry and navigation** | `SCR-091`. Destinations: `SCR-088` published changes, `SCR-092` if moderation is needed, `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Audience/scope. 2) Content and limits. 3) Publication preview. 4) Moderation requirement. 5) Audit. 6) Definitions. |
| **E Layout** | `P-TASK` admin. Scope selector, content editor, preview, moderation panel, publish action. |
| **F Data presentation** | • Scope — global/section. • Content — player-readable text. • Prohibited — private case, method, security secret. • Publication — turn/time. • Moderation — ALL-164 state. |
| **G Controls** | • `Preview` — read-only. • `Publish` — committing; permissioned; confirmation; audited. • Moderation path where required. |
| **H Screen relationships** | `SCR-088`; `SCR-092`; `SCR-077` (if announcing world data, gated); `SCR-091`. |
| **I Responsive** | Desktop: editor + preview. Tablet: stacked. Mobile: editor, preview, publish separated. |
| **J Governing references** | Governing: MOD-017/018; ALL-164; TR-049. Decisions: D-218. |
| **K Restrictions and notes** | No private case data, detection method, security secret or another player's identity. Publication is an official record, not a marketing channel. No announcements feature exists for players (UD-049). |

### SCR-100 — Admin roles & permission management

| Field | Specification |
|---|---|
| **A Identity** | Parent **Admin**; category `Admin workspace`; governing **B-12**; related `REQ-838`…`REQ-846`; new `REQ-969`; class **Mandatory (admin)**; audience `R-SEC`/`R-EMG` as permitted; permissions role management; visibility admin-only. |
| **B Purpose** | Manages roles and permissions with least privilege and anti-escalation. It solves "who can do what" without a superuser. |
| **C Entry and navigation** | `SCR-091`. Destinations: `SCR-096` audit, `SCR-091`. Return: `SCR-091`. |
| **D Information hierarchy** | 1) Role catalogue. 2) Permission matrix. 3) Holder assignments. 4) Step-up/emergency posture. 5) Audit. 6) Definitions. |
| **E Layout** | `P-OBJ` admin. Role cards, permission matrix, assignment table, emergency posture panel, audit note. |
| **F Data presentation** | • Roles — eight ADM roles. • Permissions — matrix. • Holder — identity summary. • Step-up — current. • Emergency — posture/authority. • No `SEC` content. |
| **G Controls** | • `Assign role` — committing; permissioned; anti-escalation; confirmation; audited. • `Revoke role` — committing; confirmation; audited. • No control creates a superuser. |
| **H Screen relationships** | `SCR-096`; `SCR-091`; `SCR-094`. |
| **I Responsive** | Desktop: matrix + assignments. Tablet: stacked. Mobile: role cards; assignment in a stepped flow; destructive revoke separated. |
| **J Governing references** | Governing: ADM-003; D-042; FR postures; REQ-838…846. Decisions: D-218. |
| **K Restrictions and notes** | Eight roles only; no superuser; least privilege; step-up for sensitive actions; emergency authority is a recorded posture, not unbounded power. No permission may be granted by a holder who lacks it. |

---

**End of screen bodies.** All 100 identifiers are specified. The authoritative completeness status is Matrix A in the [parent document](21_interface_and_player_journeys.md#24-matrix-a--screen-specification-completeness).
