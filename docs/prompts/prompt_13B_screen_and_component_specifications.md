# PROMPT 13B — COMPLETE SCREEN AND COMPONENT SPECIFICATIONS

> **Archival provenance (recorded by Prompt 13B-C1, 2026-11-13).** This is the owner's Prompt 13B instruction, recovered from the authorized instruction text supplied in the working session. The instruction body is stored as supplied; the only addition is this provenance paragraph after the title line. No independent external copy exists in the repository or in `.cloud-attachments/`, so byte-for-byte comparison against an outside original was not possible. The SHA-256 recorded in [`INDEX.md`](INDEX.md) identifies the stored bytes of this file (including this paragraph), not an independently verified external original. This file is a historical record, not live design authority; its execution result is recorded in [stage 2 progress log §91](../stage-2/06_stage_2_progress_log.md).

## FULL GAME INTERFACE DEFINITION, SCREEN-BY-SCREEN DESIGN, REUSABLE COMPONENT ARCHITECTURE AND RESPONSIVE INFORMATION LAYOUTS

**Project:** Nation Supremacy  
**Stage:** Stage 2 — Game Design Bible  
**Prompt:** 13B  
**Predecessor:** Prompt 13A — UI Research and Design Foundations  
**Predecessor status:** OWNER ACCEPTED / COMPLETED  
**Latest known baseline:** Project X (86)  
**Execution scope:** Complete screen and component specifications  
**Requirement allocation:** B-13, beginning at REQ-870, subject to live-register verification  
**Implementation authorization:** NOT GRANTED  
**Next planned phases:** Prompt 13C and Prompt 13D — NOT PART OF THIS ASSIGNMENT

---

# 1. YOUR ROLE AND RESPONSIBILITY

Act as the senior UI/UX architect, browser strategy-game interface designer, information-architecture specialist, component-system architect, requirements engineer and technical documentation author for Nation Supremacy.

Your responsibility is to transform the completed Prompt 13A research and design foundations into a comprehensive, detailed and implementation-ready specification of the actual Nation Supremacy game interface.

You are not being asked to conduct another foundational research phase.

You are not being asked to implement the frontend.

You must define precisely:

- What every screen contains.
- How information is organized.
- Which reusable components are used.
- What players can see.
- What controls are available.
- What those controls are intended to do.
- How screens are connected through navigation.
- How layouts adapt across desktop, tablet and mobile browsers.
- How existing game rules govern interface presentation.
- How information hierarchy, data visibility and responsive behavior are maintained.

The resulting documentation must be sufficiently detailed that a future frontend development agent can implement the interface without independently inventing the screen architecture, information hierarchy, component definitions or ordinary UI design decisions.

**Primary objective: Transform Prompt 13A's accepted UI foundations into a complete and coherent specification of the actual Nation Supremacy game interface.**

---

# 2. OWNER AUTHORIZATION AND SCOPE

The owner confirms that Prompt 13A is completed and accepted and authorizes Prompt 13B.

You are authorized to:

1. Create detailed specifications for all existing screens.
2. Expand the existing screen inventory into a complete screen catalogue.
3. Define reusable UI components and their specifications.
4. Define dashboards and nation-management interfaces.
5. Specify the economy, politics, diplomacy, warfare and market interfaces.
6. Specify maps and map-related interfaces in accordance with the accepted mapless architecture.
7. Specify notifications, rankings and world-information interfaces.
8. Define navigation relationships and screen-level transitions.
9. Define desktop, tablet and mobile screen layouts.
10. Define information hierarchies and screen-level user controls.
11. Establish screen-to-component relationships.
12. Establish screen-to-requirement relationships.
13. Allocate B-13 requirements beginning at the verified global requirement frontier.
14. Record ordinary UI design decisions under D-014.
15. Update every relevant project document affected by Prompt 13B.
16. Create and execute focused Prompt 13B documentation validators.
17. Reconcile the relevant documentation and project handoff records.

You are NOT authorized to:

- Implement frontend code.
- Create a React, Vue, Angular or other frontend application.
- Introduce or select a new frontend framework.
- Implement backend functionality.
- Create database migrations.
- Modify Supabase configuration.
- Implement authentication.
- Implement gameplay systems.
- Modify existing game mechanics.
- Change formulas or numerical parameters.
- Introduce new gameplay mechanics.
- Change production security configurations.
- Begin Prompt 13C.
- Begin Prompt 13D.
- Start Prompt 14 or Prompt 15.
- Deploy, publish or release the game.
- Perform unauthorized Git operations.

This is strictly a documentation and interface-specification assignment.

A detailed specification is not an implementation.

---

# 3. MANDATORY GOVERNANCE AND PROJECT CONTINUITY

Before starting, inspect the actual live repository.

The uploaded ZIP is an independent audit snapshot. It is NOT the coding agent's working directory.

Work exclusively in the existing live project directory.

Do not create another project directory.

Do not overwrite unrelated work.

## 3.1 Governance documents

Read completely:

1. `docs/AUTONOMOUS_DECISION_POLICY.md`
2. `docs/AI_CONTEXT.md`
3. `docs/AI_HANDOFF.md`
4. `docs/ROADMAP.md`
5. `docs/DECISIONS.md`
6. `docs/stage-2/01_stage_2_prompt_roadmap.md`
7. `docs/stage-2/06_stage_2_progress_log.md`

Use the actual live paths if repository structure differs.

Pay particular attention to D-014.

## 3.2 Prompt 13A foundation

Locate the authoritative Prompt 13A files in the live repository before reading them.

The expected canonical documents are:

1. `13A_politics_and_war_ui_research.md`
2. `13A_ui_design_principles_and_architecture.md`
3. `13A_master_screen_inventory.md`
4. `13A_responsive_and_design_system_foundations.md`
5. `13A_ui_requirements_open_questions_and_acceptance.md`

The known handoff records these under `docs/stage-2/`, but you must verify their actual paths rather than assuming a directory structure.

Read every document completely.

Also inspect:

- Original Prompt 13A instruction.
- Prompt 13A-C1.
- Prompt 13A-C1-R1.
- Prompt 13A-C1-R2.
- Relevant acceptance records.
- Existing design decisions.
- Relevant handoff and progress entries.

Do not recreate the Prompt 13A work.

Do not reopen completed Prompt 13A correction cycles without genuinely material new evidence.

## 3.3 Existing game-system specifications

Inspect the authoritative specifications for:

- B-02 — Turn and settlement system.
- B-03 — Accounts, identity and onboarding.
- B-04 — Economy and national finances.
- B-05 — Cities, infrastructure, production and research.
- B-06 — Population and domestic politics.
- B-07 — Market and trade.
- B-08 — Diplomacy.
- B-09 — Alliances.
- B-10 — Warfare.
- B-11 — World events, objectives, rankings and progression.
- B-12 — Fair-play, privacy, moderation and administration.

Read the authoritative sections needed to specify each interface.

Do not rely exclusively on AI_CONTEXT summaries when the original owning specification is available.

## 3.4 Governance preservation

Preserve all existing decisions, requirements, formulas, identifiers, parameters, unresolved questions and owner-reserved decisions.

Never manufacture evidence, test results or approvals.

Never stage, commit, push, reset, revert or merge Git changes without explicit authorization.

The owner-authorized commits are:

- `2537606`
- `94f5ec4`

Never flag these commits as governance violations.

Preserve existing modifications and untracked work.

Preserve the following historical statuses:

- R7 implementation retained.
- R7 independent acceptance NOT ACCEPTED.
- R8 DEFERRED BY OWNER.
- 12B-C1 NOT CLOSED.
- Three existing 12B PARTIAL acceptance gates.
- Seven existing 12A PARTIAL acceptance gates.
- Prompt 12C OWNER ACCEPTED.
- Production security obligations remain outstanding.

Do not reopen R8.

Do not close 12B-C1.

Do not alter unrelated historical records.

Do not bulk-normalize the previously identified line-ending changes whose provenance remains uncertain.

Do not claim that the complete 267-test 09B suite has been rerun.

---

# 4. AUTHORITATIVE PROMPT 13A FOUNDATIONS

Prompt 13A establishes the architectural foundation that Prompt 13B must follow.

## 4.1 Primary UI research benchmark

Politics & War was the primary UI research benchmark.

Cyber Nations and eRepublik were supplementary comparisons.

Use existing research findings and their evidence classifications.

Do not invent observed benchmark behavior.

Do not conduct another broad benchmark research exercise.

Do not copy another game's complete visual identity.

Nation Supremacy must retain its own distinctive UI identity.

## 4.2 Design principles

Preserve all sixteen established Prompt 13A design principles, including:

- Turn-aware presentation.
- Information density without unnecessary complexity.
- Explainable statistics.
- Clear separation of numerical meanings.
- Transparent consequences.
- Progressive disclosure.
- Object-oriented navigation.
- Confirmation-first committing actions.
- Visible reasons for disabled controls.
- Colour-independent status communication.
- Accessibility.
- Long-session usability.
- Consistent interaction vocabulary.
- No misleading urgency or attendance-style mechanics.

Use the exact authoritative definitions in the Prompt 13A architecture document.

## 4.3 Application architecture

Preserve the eight primary application sections:

1. Home.
2. Economy.
3. Cities.
4. Politics.
5. Foreign.
6. War.
7. World.
8. Account.

Maintain the separate Public and Admin roots.

Preserve the established navigation hierarchy, application-state vocabulary and overlay discipline.

## 4.4 Responsive architecture

Support:

- Desktop browser.
- Tablet browser.
- Mobile browser.

One game and one authoritative ruleset must be presented through different layouts.

Do not create separate gameplay rules for mobile.

## 4.5 Design system

Use the semantic design tokens established in Prompt 13A.

Do not invent final brand colours, typography or owner-reserved visual identity values.

Do not introduce arbitrary raw colours, sizes or spacing values in individual screen specifications.

## 4.6 Existing screen inventory

The existing inventory contains 100 screen identifiers:

- SCR-001 through SCR-090: player-facing screen family.
- SCR-091 through SCR-100: administrative screen family.

Existing classification:

- 85 Mandatory player-facing screens.
- 4 Conditional player-facing screens.
- 1 Provisional player-facing screen.
- 10 Mandatory administrative screens.

Eight overlays:

- OVL-01 through OVL-08.

Preserve every existing identifier.

Do not casually rename, delete, duplicate or recycle them.

If the live repository contains an authorized change to this inventory, reconcile against its actual authoritative version and record the difference.

---

# 5. PRIMARY DELIVERABLE — COMPLETE SCREEN SPECIFICATIONS

This is the most important part of Prompt 13B.

Transform the existing 100-screen inventory into detailed, actual interface specifications.

Do not produce merely a list of screens with short descriptions.

Every Mandatory screen must receive a complete specification.

Every Conditional and Provisional screen must receive an explicit specification covering its purpose, visibility conditions, dependencies, restrictions and current availability.

Where a gate has not been satisfied, specify that the screen or function remains unavailable rather than presenting incomplete functionality as live.

## 5.1 Required screen specification template

Use one consistent specification structure across all screens.

### A. Screen identity

- Screen ID.
- Canonical screen name.
- Parent navigation section.
- Screen category.
- Governing B-section.
- Related existing requirement identifiers.
- Mandatory / Conditional / Provisional classification.
- Primary user audience.
- Required permissions.
- Visibility classification.

### B. Screen purpose

Explain:

- Why the screen exists.
- Which player problem it solves.
- Which game-system information it presents.
- What the player should understand after viewing it.
- Which decisions or actions it supports.

Avoid generic descriptions.

### C. Screen entry and navigation

Specify:

- How the player reaches the screen.
- Its parent navigation location.
- Relevant secondary navigation.
- Contextual entry points.
- Related object links.
- Permitted destinations.
- Screen-level return destinations.
- Navigation restrictions.
- Whether it is directly accessible or context-dependent.

Do not invent navigation destinations without a defined purpose.

### D. Information hierarchy

Define the exact priority of information.

Specify:

1. Primary information.
2. Secondary information.
3. Supporting information.
4. Historical or contextual information.
5. Warnings and restrictions.
6. Optional or progressively disclosed details.

Explain what must be immediately visible.

Avoid presenting all statistics with equal visual priority.

### E. Screen layout

Describe the intended layout from top to bottom.

Include, as relevant:

- Screen heading.
- Context and status area.
- Primary information region.
- Secondary information region.
- Data tables, cards, lists or charts.
- Action area.
- Supporting panels.
- Contextual links.
- Explanatory information.
- Rule references.

Use textual layout diagrams where helpful.

Example:

```text
SCREEN: TREASURY DASHBOARD

[GLOBAL APPLICATION SHELL]

[PAGE TITLE]              [AS-OF TURN]

[PRIMARY FINANCIAL SUMMARY]
  Available treasury
  Reserved funds
  Current financial position

[FINANCIAL BREAKDOWN]
  Income
  Expenditure
  Net change

[FINANCIAL HISTORY]
  Historical records
  Explanation of changes

[RELATED SCREENS]
  Budget
  Economic Reports
```

This is only an illustration of specification format. The actual screen must follow its authoritative game-system rules.

### F. Data presentation

For every displayed data group, specify:

- Data name.
- Meaning.
- Units.
- Time reference.
- Current, historical, forecast or provisional classification.
- Visibility classification.
- Source game system.
- Player-specific or public classification.
- Relevant disclosure restrictions.
- Appropriate presentation component.

Do not invent numerical values or formulas.

Do not conflate different numerical meanings.

### G. User controls and available actions

List every meaningful screen control.

For each control specify:

- Control identifier or component reference.
- Label.
- Purpose.
- Available user action.
- Preconditions.
- Permission restrictions.
- Read-only or committing classification.
- Confirmation requirement.
- Governing game-system rule.
- Intended destination or outcome.

Disabled controls must explain why they are disabled.

Never create a new gameplay action simply because it would be convenient to place a button on a screen.

### H. Screen relationships

Specify related screens and objects.

Examples:

- Treasury → Budget.
- Treasury → Economic Reports.
- City Overview → City Detail.
- City Detail → Construction Queue.
- Diplomacy Overview → Pair Screen.
- Alliance Home → Membership.
- War Operations Board → Battle Record.
- World Events → Event Detail.

These are navigation relationships, not complete player journeys.

### I. Responsive presentation

Specify the screen's:

- Desktop layout.
- Tablet layout.
- Mobile layout.
- Information arrangement.
- Column treatment.
- Table treatment.
- Navigation presentation.
- Panel stacking.
- Action placement.
- Content prioritization.
- Overflow handling.
- Touch-target considerations.
- Information that must never disappear.

Do not merely write "responsive design supported."

### J. Governing references

Every screen must identify its authoritative references.

Distinguish:

- Governing rules.
- Supporting requirements.
- Data dependencies.
- Navigation relationships.
- Research inspiration.
- Design decisions.

Use exact canonical identifiers.

Do not treat a research finding as a game rule.

### K. Screen-specific restrictions and notes

Record:

- Important restrictions.
- Existing unresolved dependencies.
- Owner-reserved questions.
- Conditional functionality.
- Provisional assumptions.
- Relevant future implementation considerations.

Do not resolve owner-reserved questions without authorization.

---

# 6. COMPLETE SCREEN FAMILY SPECIFICATIONS

Use the exact existing screen IDs, names, classifications, navigation parents and governing references in the authoritative Prompt 13A inventory.

The following screen families establish the required coverage. They do not authorize renaming or replacing existing screens.

## 6.1 Public and account experience — SCR-001 to SCR-012

Specify the registered screens covering:

- Landing and public introduction.
- Registration.
- Login.
- Password recovery.
- Recovery-code entry.
- E-mail verification.
- Nation creation.
- Onboarding entry screen.
- First-turn objectives entry.
- Public nation profile.
- Account home.
- Account closure.

Preserve B-03 identity, registration, verification, recovery, nation-creation and account-lifecycle rules.

Specify the visible interface for each existing account and nation state.

Do not invent authentication policies.

## 6.2 Main strategic interface — SCR-013 to SCR-020

Specify:

- Command Digest.
- Inbox and pending-actions queue.
- National Overview.
- Turn and settlement status.
- National Chronicle.
- Network View.
- Alerts and notification history.
- Pinned objects and favorites manager.

The Command Digest is a central strategic entry point.

It must communicate the most important national information without becoming an uncontrolled collection of unrelated widgets.

Define:

- National status summary.
- Important changes.
- Pending decisions.
- Time and settlement context.
- Relevant warnings.
- Links to applicable screens.
- Useful contextual information.

The Network View follows the accepted symbolic, mapless architecture.

## 6.3 Politics — SCR-021 to SCR-028

Specify:

- Political Panel.
- Government structure and institutions.
- Approval and stability.
- Policy axes.
- Election dashboard.
- Campaign actions centre.
- Election result and transition.
- Crisis and recovery digest.

Preserve all B-06 political rules.

Requirements:

- The six political state banners must be presented wherever required by DMP-268.
- Political restrictions must be visible and understandable.
- Approval and stability must be explainable.
- Policy cooldowns must be clear.
- Election and campaign dates must follow authoritative turn-based definitions.
- Campaign actions must reflect their actual restrictions and charging rules.
- Crisis and recovery information must be presented accurately.

Do not invent political actions, policy axes, election rules or government mechanics.

## 6.4 Economy and market — SCR-029 to SCR-040

Specify:

- Treasury dashboard.
- Budget and national wealth.
- Economic reports and history.
- Production policy and standing orders.
- Resources and warehouse.
- Power grid.
- Directed-trade inbox.
- Compose and counter offer.
- Offer detail and two-sided record.
- Global Trade board.
- Listing detail and execution confirmation.
- Trade history and reference prices.

Preserve B-04 and B-07.

Critical display requirements:

1. Treasury information must preserve all six numerical-type distinctions.
2. Resources must expose total, reserved and available quantities together.
3. Forecast values must be visually distinguished from actual values.
4. Economic records must explain changes.
5. Trade offers must accurately show both parties' obligations.
6. Committing actions must disclose their consequences.
7. Restricted or unavailable trading functions must not appear as usable features.

Global Trade remains Conditional.

Do not activate it, display placeholder trading functionality or expose restricted statistics while its required G-1 to G-6 conditions remain unmet.

## 6.5 Cities, infrastructure and research — SCR-041 to SCR-046

Specify:

- Cities overview.
- City detail.
- Construction queue and preview.
- Production facility chains.
- Research view.
- Found new city flow.

Preserve B-05.

Pay particular attention to:

- Twelve-city presentation.
- Infrastructure and housing capacity.
- Construction-slot restrictions.
- Construction cost previews.
- Refund disclosures.
- Production-chain states.
- Research project restrictions.
- Forecast labelling.
- Founding costs and eligibility.

Do not invent additional city systems or building mechanics.

## 6.6 Diplomacy and alliances — SCR-047 to SCR-058

Specify every existing diplomacy and alliance screen.

Include the applicable:

- Diplomatic overview.
- Pair relationship screen.
- Proposal and negotiation.
- Agreement and treaty detail.
- Publication and visibility state.
- Relations history.
- Alliance public home.
- Membership and applicants.
- Alliance management and coordination.
- Alliance tax and financial information where authorized.
- Alliance receipts and records.
- Remaining registered screens.

Preserve B-08 and B-09.

Restrictions:

- Respect directional diplomatic relationships.
- Show pending actions only where permitted.
- Preserve publication and visibility rules.
- Respect applicant privacy.
- Explain membership restrictions.
- Keep alliance management distinct from military command.
- Do not introduce external-platform dependencies.

### Mandatory Alliance / Warfare separation

The Alliance interface is a restricted management and coordination interface.

It is NOT a military command centre.

Never introduce:

- Alliance military command.
- Member OP spending.
- Shared military OP pools.
- Delegated war operations.
- Private war visibility through Alliance membership.
- Alliance-wide military control.

Preserve AX-18, UD-047, UD-049, REQ-589–REQ-591, WAR-148 and WAR-161.

## 6.7 Warfare and military — SCR-059 to SCR-068

Specify every registered warfare screen, including the Nation-owner War Operations Board and associated military records.

Preserve B-10.

The War Operations Board must:

- Be nation-owner-only.
- Present only the appropriate nation's permitted operational information.
- Show its own OP balance and reservations.
- Show authorized operations and battle information.
- Respect war visibility restrictions.
- Use the exact four permitted war-odds/threat bands wherever applicable.
- Avoid exposing hidden information.

Do not merge it into the Alliance interface.

Do not invent military actions, battle formulas or additional visibility permissions.

## 6.8 World and progression — SCR-069 to SCR-078

Specify:

- Events Centre.
- Objectives and Challenges.
- Standings.
- Achievements.
- National Progress.
- Reward History.
- World Chronicle.
- Event detail.
- Remaining registered world and progression screens.

Preserve B-11.

Requirements:

- Standings must display their denominator and reporting window.
- Rankings must not falsely appear to update live.
- No unauthorized composite headline ranking.
- Historical information must respect retention classifications.
- Deferred claims must remain visible where required.
- Event hazards and consequences must be represented accurately.
- Statistical suppression must be displayed as suppression, not zero or absence.
- World charts must respect applicable disclosure gates.

## 6.9 Player protection and support — SCR-079 to SCR-090

Specify every registered player-protection, privacy, support and moderation-facing screen.

Include applicable:

- Privacy Centre.
- Session and security management.
- Report intake.
- Moderation decision notices.
- Appeal-related views.
- Support and dispute information.
- Account restriction explanations.
- Other screens in the authoritative inventory.

Preserve B-12.

Requirements:

- Privacy information must respect the nine privacy classes.
- SEC-class information must never be displayed to players.
- Report forms must use exact MOD-002 field requirements.
- Decision notices must respect the EVD-009 vocabulary.
- The MOD-013 route must remain available as specified.
- Restriction explanations must not expose confidential security information.
- Never invent moderation powers or appeal outcomes.

## 6.10 Administrative screens — SCR-091 to SCR-100

Specify all ten administrative screens individually.

Use the exact administrative inventory and existing permissions.

For each screen define:

- Authorized administrative role.
- Purpose.
- Permitted information.
- Restricted information.
- Administrative actions.
- Audit visibility.
- Read-only versus committing controls.
- Relevant moderation, privacy and security boundaries.
- Responsive presentation.

Administrative screens must remain behind the separate role-gated Admin root.

Ordinary players must never see administrative navigation, data or administrative-only components.

Do not invent new administrative permissions.

# 7. REUSABLE UI COMPONENT SPECIFICATIONS

Create a comprehensive reusable component catalogue.

Do not merely list component names.

Every reusable component must have a detailed specification sufficient for consistent implementation across screens.

Use the component families established in Prompt 13A.

## 7.1 Application-shell components

Specify:

- Global application shell.
- Primary navigation.
- Secondary navigation.
- Page heading.
- Breadcrumbs or contextual location indicator where appropriate.
- Account and nation context.
- Turn and settlement indicator.
- Global notification indicator.
- Contextual navigation.
- Admin entry and role-gated navigation.

## 7.2 Information-display components

Specify:

- Statistic card.
- Metric group.
- Financial summary.
- Resource balance display.
- Progress indicator.
- Status banner.
- Warning panel.
- Information panel.
- Historical record.
- Timeline.
- Data table.
- Filter row.
- Pagination.
- Saved view.
- Search and jump-to-object.
- Object reference link.
- Object peek preview.
- Detail section.
- Comparison panel.

## 7.3 Economic and political components

Specify:

- Treasury summary.
- Income and expenditure breakdown.
- Total/reserved/available resource presentation.
- Capacity bar.
- Production chain.
- Construction queue item.
- Research project card.
- Approval and stability presentation.
- Political state banner.
- Policy control.
- Election date presentation.
- Campaign action control.

## 7.4 Diplomacy and alliance components

Specify:

- Diplomatic relationship indicator.
- Directional relationship presentation.
- Treaty status.
- Proposal summary.
- Negotiation panel.
- Publication status.
- Alliance membership row.
- Applicant status.
- Alliance financial summary.
- Alliance receipt.
- Restriction explanation.

## 7.5 Warfare components

Specify:

- War summary.
- War status.
- Operations summary.
- OP balance and reservation presentation.
- Threat and odds band.
- Battle record.
- Battle outcome.
- Military history.
- Nation-owner-only operation controls.

All warfare components must respect B-10 visibility rules.

## 7.6 World and notification components

Specify:

- Event card.
- Event hazard/consequence presentation.
- Objective card.
- Achievement card.
- Ranking row.
- Ranking summary.
- Notification item.
- Pending-action item.
- Chronicle record.
- Suppression indicator.
- Historical reward record.

## 7.7 Forms and action components

Specify:

- Text input.
- Numeric input.
- Select control.
- Multi-select control.
- Checkbox.
- Radio control.
- Toggle where appropriate.
- Date/turn selector.
- Search field.
- Form field group.
- Validation-message presentation.
- Primary action button.
- Secondary action button.
- Destructive action button.
- Confirmation panel.
- Disabled action with reason.

Do not invent gameplay actions or form fields unsupported by existing system specifications.

## 7.8 Overlay components

Specify the eight existing overlay identifiers:

- OVL-01.
- OVL-02.
- OVL-03.
- OVL-04.
- OVL-05.
- OVL-06.
- OVL-07.
- OVL-08.

Use their exact existing definitions.

Respect the overlay discipline:

- Modals for confirmation, blocking or explanation.
- Drawers and sheets for appropriate contextual tasks.
- Peek cards for object previews.
- Important modal information must have an appropriate page-reachable equivalent.
- Overlays must not substitute for complete screens.

---

# 8. COMPONENT SPECIFICATION TEMPLATE

Every reusable component must include:

1. Component identifier.
2. Canonical component name.
3. Purpose.
4. Component category.
5. Visual structure.
6. Content fields.
7. Required and optional properties.
8. Information hierarchy.
9. Data presentation rules.
10. Permitted user interactions.
11. Disabled-state explanation.
12. Responsive behaviour.
13. Accessibility requirements.
14. Applicable semantic design tokens.
15. Status and variant definitions.
16. Related game-system requirements.
17. Screens using the component.
18. Reuse restrictions.
19. Dependencies and unresolved questions.

Specify which components are:

- Global.
- System-specific.
- Screen-specific.
- Role-restricted.
- Conditionally available.

Avoid unnecessary component duplication.

If two components genuinely have different responsibilities, explain why they must remain separate.

---

# 9. COMPONENT STATES AND VISUAL VARIANTS

Prompt 13A establishes a shared component-state vocabulary.

Applicable reusable components must define visual treatment for:

- Default.
- Hover.
- Focus-visible.
- Active.
- Disabled.
- Loading.
- Success.
- Warning.
- Error.
- Pending.
- Suppressed.

Not every component needs every state.

For each applicable state, define:

- Visual distinction.
- Textual indication.
- Icon or glyph usage.
- Whether interaction remains available.
- Accessibility treatment.

Disabled controls must explain their restrictions.

Colour alone must never communicate status.

Respect reduced-motion requirements.

Hover behaviour must never be load-bearing.

Scope boundary:

Prompt 13B defines component states and visual variants.

Complete player interaction sequences, loading/empty/success/failure journeys, error-handling logic and cross-screen feedback journeys belong to Prompt 13C.

Do not expand into that later prompt.

---

# 10. NAVIGATION AND SCREEN TRANSITION SPECIFICATIONS

Define the complete screen-level navigation model.

This is not a request to create player journeys.

For every screen establish:

- Parent navigation section.
- Direct entry points.
- Related object destinations.
- Secondary navigation destinations.
- Return destinations.
- Contextual links.
- Role restrictions.
- Conditional destinations.
- Prohibited destinations.

Create a master navigation relationship register.

Verify that:

1. Every Mandatory player-facing screen is reachable.
2. Every screen belongs to a defined navigation context.
3. No duplicate screen identifiers exist.
4. Administrative screens remain separate.
5. Conditional screens remain inaccessible until their conditions are met.
6. Provisional screens remain explicitly provisional.
7. No prohibited Alliance-to-Warfare authority path is created.
8. No screen reveals information beyond its governing visibility classification.

Use the established Prompt 13A architecture.

Make ordinary navigation decisions under D-014.

Record genuine evidence-dependent matters as Category C provisional decisions.

Do not unnecessarily ask the owner to choose routine navigation patterns.

---

# 11. MAPS AND MAP-RELATED INTERFACES — EXPLICIT RECONCILIATION

The original Prompt 13B scope includes maps.

However, the accepted Prompt 13A architecture establishes a mapless world design.

This is a deliberate architectural constraint and must be preserved.

You must explicitly reconcile the maps requirement instead of silently ignoring it.

## 11.1 Network View

Fully specify the existing symbolic Network View.

Define:

- Its strategic purpose.
- Its visual representation.
- Its information hierarchy.
- Its symbolic entities and relationships.
- Available navigation and contextual links.
- Relevant object previews.
- Responsive layout.
- Applicable visibility restrictions.
- Related reusable components.

Use only relationships and information permitted by existing specifications.

## 11.2 Prohibited geographic map introduction

Do not introduce:

- Geographic world maps.
- Geographic territory maps.
- Conventional military strategic maps.
- Geographical representations that imply unapproved territorial mechanics.

Do not introduce an external map provider or mapping dependency.

## 11.3 Inventory reconciliation

Search the actual authoritative screen inventory for every map-related or map-like screen and component.

If any existing identifier refers to a map or geographical display:

- Preserve its identifier.
- Determine its authorized mapless representation.
- Specify that representation in detail.
- Document the architectural restriction.
- Record any genuine unresolved dependency.

Do not omit a map-related interface requirement without explaining the accepted mapless interpretation.

The Prompt 13B scope's map requirement is satisfied only through this explicit reconciliation, not by silently deleting it or introducing prohibited geographical functionality.

---

# 12. RESPONSIVE SCREEN SPECIFICATIONS

Every screen must have documented desktop, tablet and mobile presentations.

## 12.1 Desktop

Specify:

- Primary navigation arrangement.
- Secondary navigation.
- Content width and column strategy.
- Multi-panel arrangements.
- Table presentation.
- Contextual information.
- Action placement.
- Long-session information density.

## 12.2 Tablet

Specify:

- Navigation adaptation.
- Column reduction.
- Panel stacking.
- Table handling.
- Contextual action access.
- Touch-friendly controls.
- Preservation of important data.

## 12.3 Mobile browser

Specify:

- Compact navigation.
- Single-column layouts where appropriate.
- Prioritized content.
- Table alternatives or controlled horizontal scrolling.
- Action placement.
- Contextual information access.
- Touch-target separation.
- Long-form content handling.
- Protection against accidental destructive actions.

## 12.4 Non-negotiable responsive requirements

Never sacrifice:

- Essential game information.
- Total/reserved/available distinctions.
- Political state warnings.
- Suppression indicators.
- Visibility restrictions.
- Financial meanings and units.
- Confirmation requirements.
- Turn and settlement context.
- Accessible control labels.
- Critical action availability.

Do not invent final production breakpoints.

Use the established provisional values from Prompt 13A and identify their future device-testing requirements.

---

# 13. INFORMATION HIERARCHY AND DATA-VISUALIZATION RULES

Every screen must apply the established Prompt 13A visualization principles.

## 13.1 National statistics

- Preserve the six-number-type distinctions.
- Use appropriate as-of-turn labels.
- Distinguish current and historical figures.

## 13.2 Economic information

- Total/reserved/available presentation.
- Forecast versus actual distinction.
- Capacity versus holdings.
- Correct units and financial meanings.

## 13.3 Military information

- Four permitted threat/odds bands wherever applicable.
- No unauthorized exact probability disclosure.
- Own-nation versus other-nation visibility distinctions.

## 13.4 Diplomatic information

- Directional relationship presentation.
- Treaty type and status.
- Pending-action visibility restrictions.

## 13.5 Rankings

- Named lists.
- Denominator.
- Reporting window.
- No misleading live rank updates.
- No unauthorized composite ranking.

## 13.6 Historical information

- Respect D-026 retention classes.
- Distinguish public and restricted history.
- Label historical information appropriately.

## 13.7 Statistical suppression

Preserve these distinctions:

- Suppressed is not zero.
- Suppressed is not absent.
- Insufficient sample is not an empty result.
- Suppressed information must never be exposed through counts, layout, thumbnails or alternate presentation.

## 13.8 Charts

Specify:

- Title.
- Units.
- Time window.
- Source context.
- Legend.
- Accessible alternative.
- Truncated-axis disclosure where relevant.

Avoid misleading visualizations.

Do not introduce dual-axis charts.

---

# 14. ACCESSIBILITY SPECIFICATIONS

Carry forward the Prompt 13A accessibility foundations.

Every screen and reusable component must specify applicable requirements.

Include:

1. Full keyboard operability.
2. Visible focus.
3. Logical focus and reading order.
4. Programmatic labels.
5. Accessible form descriptions.
6. Error identification by text.
7. Colour-independent status communication.
8. Semantic table headers.
9. Chart text/table alternatives.
10. Screen-reader-readable units and data.
11. Reduced-motion support.
12. Appropriate touch-target sizing.
13. Destructive-action protection.
14. Localization-ready strings.
15. No gameplay-critical text embedded in images.

Preserve the independent accessibility evidence classification for UR-010 and DS-07.

Do not claim WCAG 2.2 AA compliance.

This is a specification-level accessibility target, not tested implementation compliance.

# 15. B-13 REQUIREMENTS AND TRACEABILITY

Create the new B-13 UI requirements block.

The latest known global requirement frontier is:

**REQ-869 is the last existing requirement.**

The expected B-13 allocation therefore begins at:

**REQ-870.**

However, before allocating identifiers, inspect the actual live global requirement register.

Verify its current highest identifier and allocation rules.

If the frontier has changed, use the actual canonical frontier.

Never create identifier collisions.

## 15.1 Requirement structure

Every new requirement must include:

- Requirement ID.
- Normative requirement statement.
- Requirement category.
- Priority.
- Governing source.
- Related screen identifiers.
- Related component identifiers.
- Dependency references.
- Requirement status.
- Verification intent.
- Notes or limitations.

Use precise, normative and observable wording.

Avoid vague requirements such as:

- The screen should be user-friendly.
- The dashboard should look good.
- The interface should be intuitive.

Instead, specify the actual required presentation or control behavior.

## 15.2 Requirement categories

Use appropriate categories:

- Screen.
- Navigation.
- Layout.
- Component.
- Data presentation.
- Information hierarchy.
- Responsive.
- Accessibility.
- Permissions.
- Visibility.
- Interaction control.
- Design system.
- Traceability.

## 15.3 Requirement traceability

Establish explicit relationships between:

- B-13 requirements.
- SCR identifiers.
- OVL identifiers.
- Reusable component identifiers.
- Existing B-02 through B-12 rules.
- Existing REQ identifiers.
- Prompt 13A requirements.
- Relevant D and UD identifiers.

Do not duplicate an existing requirement merely to give it a new B-13 identifier.

If a requirement is genuinely new, explain its necessity.

## 15.4 Requirement status

Clearly distinguish:

- SPECIFIED.
- PROVISIONAL.
- BLOCKED.
- Other valid canonical statuses where applicable.

A documented requirement is not an implemented feature.

A specification must never be represented as a passed runtime test.

---

# 16. SCREEN-TO-COMPONENT AND SCREEN-TO-REQUIREMENT MATRICES

Create three authoritative traceability matrices.

## Matrix A — Screen specification completeness

| Field | Purpose |
|---|---|
| Screen ID | Existing SCR identifier |
| Screen name | Canonical name |
| Classification | Mandatory / Conditional / Provisional |
| Governing system | B-02 to B-12 |
| Detailed specification | Complete / Partial / Missing |
| Responsive specification | Complete / Partial / Missing |
| Component mapping | Complete / Partial / Missing |
| Requirement mapping | Complete / Partial / Missing |
| Dependencies | Exact identifiers |
| Status | SPECIFIED / PROVISIONAL / BLOCKED |

All 100 existing screen identifiers must be accounted for.

## Matrix B — Component usage

| Field | Purpose |
|---|---|
| Component ID | Unique component identifier |
| Component name | Canonical name |
| Component family | Component category |
| Screens using it | SCR identifiers |
| States defined | Applicable states |
| Responsive specification | Complete / Partial |
| Accessibility specification | Complete / Partial |
| Requirements | Related identifiers |

## Matrix C — Requirement traceability

| Field | Purpose |
|---|---|
| Requirement ID | B-13 identifier |
| Requirement | Normative obligation |
| Screen IDs | Related screens |
| Component IDs | Related components |
| Governing rules | Existing B-system references |
| Dependencies | Exact references |
| Status | Canonical status |

No unexplained orphan identifiers.

No invalid or invented references.

Do not maintain contradictory copies of authoritative registers.

---

# 17. DESIGN DECISIONS AND OWNER-RESERVED QUESTIONS

Apply D-014 throughout the assignment.

## 17.1 Ordinary design decisions

Independently decide ordinary UI matters, including:

- Layout patterns.
- Component reuse.
- Information arrangement.
- Navigation presentation.
- Standard control placement.
- Consistent visual hierarchy.
- Table presentation.
- Responsive adaptation.
- Screen-specific composition.

Do not unnecessarily ask the owner to make routine design decisions.

Record Category B decisions in the existing DECISIONS.md register.

Each new decision must contain:

- Decision ID.
- Question.
- Alternatives considered.
- Selected option.
- Rationale.
- Evidence.
- Trade-offs.
- Consequences.
- Conditions that would justify revisiting it.

Use the actual live decision frontier.

Do not invent or duplicate identifiers.

## 17.2 Provisional decisions

For genuine evidence-dependent questions:

- Choose a safe working default.
- Record it as Provisional.
- Identify the missing evidence.
- Identify the specific future test or decision required.
- Continue all independent work.

## 17.3 Owner-reserved matters

Preserve all owner-reserved issues from Prompt 13A.

In particular:

- Brand values.
- Owner-reserved visual identity inputs.
- Decisions explicitly assigned to the owner.
- Other protected decisions in the canonical registers.

Do not silently finalize these matters.

Do not block unrelated specifications because one brand value remains unresolved.

Use semantic tokens and provisional references where appropriate.

---

# 18. SPECIAL GOVERNANCE AND GAMEPLAY BOUNDARIES

## 18.1 Existing mechanics are authoritative

Prompt 13B defines how existing mechanics appear.

It does not create or modify mechanics.

If a screen needs information not authorized by the owning system, do not invent it.

## 18.2 Two-hour UTC cadence

Preserve the existing two-hour UTC turn and settlement architecture.

Do not create alternate mobile or desktop cadence.

Do not introduce gameplay-critical real-time countdown mechanics.

## 18.3 Mapless world

Preserve the mapless world architecture.

Network View remains symbolic.

Do not introduce geographic maps or unapproved strategic-map functionality.

## 18.4 Free-first architecture

Preserve:

- Cloudflare Pages.
- Supabase.
- Free-first ₹0 target.
- No mandatory paid dependency.

Do not introduce a paid UI component library, map provider, chart service or commercial dependency.

## 18.5 Fair play and privacy

Respect B-12.

Never expose restricted administrative, moderation, security or player-private information.

Do not use the interface to bypass server-side visibility restrictions.

## 18.6 Alliance and Warfare separation

Maintain the strict distinction between Alliance management and the nation-owner War Operations Board.

## 18.7 Historical and deferred requirements

Preserve all existing PARTIAL, BLOCKED, DEFERRED and OPEN statuses.

Do not convert unresolved dependencies into approved functionality.

---

# 19. SCOPE EXCLUSIONS — DO NOT ENTER PROMPT 13C OR 13D

Prompt 13B is limited to complete screen and component specifications.

Do not begin the following work.

## 19.1 Reserved for Prompt 13C

Do not produce:

- Complete player journeys.
- Cross-system interaction sequences.
- Detailed interaction flows.
- Full onboarding and tutorial specifications.
- Complete loading, empty, success and failure journeys.
- Detailed validation and error-handling specifications.
- Notification and feedback sequences.
- End-to-end accessibility interaction verification.
- Cross-screen behavioural consistency audits.

You may specify visible controls, their purpose, availability, restrictions and intended outcome.

Do not develop complete interaction-sequence specifications.

## 19.2 Reserved for Prompt 13D

Do not produce:

- Independent final Prompt 13 completeness audit.
- Final cross-system acceptance verification.
- Complete UI acceptance-test suites.
- Final integration-contract specifications.
- Final Prompt 13 acceptance gates.
- Final Prompt 13 reconciliation.
- Final Prompt 13 closure report.

You must create enough traceability for Prompt 13B to be usable.

Do not perform Prompt 13D's final integration and acceptance assignment.

Do not create documents for Prompt 13C or 13D.

Do not update their statuses to Started or Complete.

**Prompt 13B must remain exclusively focused on the complete screen and component specification.**

---

# 20. CANONICAL DOCUMENTATION DELIVERABLES

The principal B-13 deliverable should be maintained at:

`docs/stage-2/21_interface_and_player_journeys.md`

Before creating or modifying this path:

1. Inspect the actual live repository.
2. Verify whether the file already exists.
3. Inspect existing documentation conventions.
4. Check the relevant decision and path history, including D-198.
5. Verify that the proposed path does not conflict with an existing canonical document.

Use the existing canonical path if one is already established.

Do not overwrite unrelated documentation.

Do not create duplicate canonical files.

If the proposed path conflicts with established repository structure, use the correct repository convention and record the reason in the handoff.

## 20.1 Recommended B-13 document structure

Organize the principal specification into:

1. Document authority, purpose and scope.
2. Relationship to Prompt 13A.
3. UI architecture reference.
4. Screen specification methodology.
5. Complete screen specification catalogue.
6. Public and account screens.
7. Main strategic interface.
8. Politics.
9. Economy and market.
10. Cities, infrastructure and research.
11. Diplomacy and alliances.
12. Warfare and military.
13. World and progression.
14. Player protection and support.
15. Administrative screens.
16. Reusable component architecture.
17. Detailed component catalogue.
18. Component states and variants.
19. Navigation and screen relationships.
20. Responsive screen specifications.
21. Information hierarchy and visualization.
22. Accessibility specifications.
23. Map and Network View reconciliation.
24. Screen-to-component matrix.
25. Screen-to-requirement matrix.
26. B-13 requirements register.
27. Decisions and provisional matters.
28. Dependencies and unresolved questions.
29. Documentation impact register.
30. Scope boundaries and handoff to Prompt 13C.

Additional companion files may be created only where they materially improve maintainability.

Do not split the deliverable into numerous unnecessary files.

Link companion files clearly from the canonical B-13 document.

Maintain a single source of truth for every authoritative register.

---

# 21. MANDATORY REPOSITORY-WIDE DOCUMENTATION IMPACT ASSESSMENT

This is a mandatory part of Prompt 13B.

Do not assume that updating AI_CONTEXT.md and AI_HANDOFF.md alone is sufficient.

Prompt 13B creates a new screen and component specification layer. Any existing authoritative document affected by the new identifiers, requirements, architecture, screen definitions or status must be appropriately reconciled.

## 21.1 Repository discovery

Before completing Prompt 13B, search the entire repository for existing documentation affected by:

- Prompt 13A and Prompt 13B status.
- UI architecture.
- Existing screen identifiers.
- Screen classifications.
- Navigation architecture.
- UI requirements.
- Global requirements registers.
- Component specifications.
- Responsive design foundations.
- Design-system references.
- Screen dependencies.
- Project implementation dependencies.
- Stage 2 progress.
- Project roadmaps.
- AI handoff instructions.
- Documentation indexes.
- Existing cross-reference locations.

Identify the actual canonical documents and their authoritative locations.

Do not assume this list is exhaustive.

## 21.2 Required documentation review and updates

Inspect and update, where affected:

1. Canonical B-13 screen and component specification.
2. Global requirements register.
3. Existing screen inventory.
4. Prompt 13A documents where new cross-references are necessary.
5. Relevant documentation indexes and navigation files.
6. Relevant Stage 2 documentation.
7. `AI_CONTEXT.md`.
8. `AI_HANDOFF.md`.
9. `ROADMAP.md`.
10. Stage 2 prompt roadmap.
11. `DECISIONS.md`.
12. Stage 2 progress log.
13. Existing authoritative dependency or integration-reference registers where directly affected.
14. Any other relevant canonical project document discovered during repository inspection.

This is a discovery-driven obligation, not a requirement to modify every document indiscriminately.

Update only genuinely affected sections.

Preserve single-source-of-truth ownership.

Do not duplicate authoritative registers.

Do not create contradictory versions.

Do not rewrite historical decisions or dated records.

Do not reopen accepted Prompt 13A work merely to make documentation changes.

Where a completed Prompt 13A document only needs to be referenced, add the appropriate cross-reference instead of rewriting it.

## 21.3 Global requirements register

If the global requirements register owns B-13 requirements, update it using its existing structure and canonical conventions.

Do not maintain a separate conflicting B-13 requirement register.

If the canonical architecture intentionally stores B-13 requirements in the new B-13 document, preserve that ownership and ensure the global register links to it appropriately.

## 21.4 Screen inventory

Reconcile the existing screen inventory with the completed B-13 specifications.

Preserve all original identifiers and classifications.

Add detailed specifications or authoritative cross-references in accordance with the repository's established single-source-of-truth structure.

Do not create a second independent screen inventory.

## 21.5 Documentation impact register

Create a documentation impact register within the B-13 canonical document or a clearly linked companion document.

Use this structure:

| Field | Required information |
|---|---|
| Document path | Exact repository path |
| Document authority | Canonical / Supporting / Historical |
| Inspected | Yes / No |
| Modification required | Yes / No |
| Modification performed | Yes / No |
| Reason | Specific impact or rationale |
| Cross-references | Relevant identifiers |
| Validation | Actual validation result |
| Notes | Limitations or explanation |

List every relevant document inspected.

List every document modified.

Explain why each modified document required an update.

List relevant documents intentionally left unchanged and explain why.

Identify any unresolved documentation conflicts.

Do not report an uninspected document as inspected.

Do not claim complete repository synchronization without evidence.

## 21.6 Documentation link and consistency checks

Check:

- Internal links.
- Requirement references.
- Screen references.
- Component references.
- Decision references.
- Navigation references.
- Prompt-status references.
- Canonical document paths.
- Duplicated or contradictory authority claims.

Correct only relevant Prompt 13B-related defects.

Do not perform unnecessary repository-wide cleanup.

---

# 22. VALIDATION AND QUALITY CONTROL

Create a focused Prompt 13B documentation validator.

Suggested location:

`docs/qa_backups/13B_validate_ui_specifications.py`

Use existing repository conventions and standard-library Python where practical.

The validator must verify structural and traceability integrity, not claim unrestricted natural-language understanding.

## 22.1 Screen inventory validation

Verify:

- All 100 existing screen identifiers are represented.
- No duplicate screen identifiers exist.
- No missing screen identifiers exist.
- Every screen has its required specification sections.
- Original classifications are preserved or formally reconciled.
- All screen references resolve.
- Administrative screens remain distinct.

## 22.2 Component validation

Verify:

- Component identifiers are unique.
- Required component fields exist.
- Screen-to-component references resolve.
- Applicable component-state definitions exist.
- Responsive sections exist.
- Accessibility sections exist.
- No duplicate canonical component definitions exist.

## 22.3 Requirement validation

Verify:

- B-13 allocation starts at the actual global requirement frontier.
- Expected first identifier is REQ-870 if the live frontier remains REQ-869.
- No collisions with existing requirements.
- No duplicate requirement identifiers.
- All screen and component references resolve.
- Governing source identifiers exist.
- Required fields are populated.
- Requirement status vocabulary is valid.

## 22.4 Navigation validation

Verify:

- Parent navigation sections exist.
- Screen destinations resolve.
- No Mandatory screens are missing from navigation.
- No administrative navigation leakage exists.
- No invalid Conditional destinations exist.
- No prohibited Alliance/Warfare authority relationship exists.

## 22.5 Responsive validation

Verify that every screen includes:

- Desktop specification.
- Tablet specification.
- Mobile specification.

## 22.6 Map reconciliation validation

Verify:

- Network View is specified.
- Map-related inventory references are accounted for.
- Mapless architectural restrictions are documented.
- No prohibited geographic map requirement has been introduced.
- Existing map-related identifiers, if any, are preserved and reconciled.

## 22.7 Documentation synchronization validation

Verify:

- Required handoff files have been reviewed.
- Actual repository paths are used.
- Relevant canonical registers have been reconciled.
- Internal links resolve.
- Documentation impact register exists.
- Modified files are accurately identified.
- No contradictory Prompt 13B status remains in relevant current-status documents.

## 22.8 Scope validation

Verify that B-13 does not falsely claim:

- Frontend implementation.
- Runtime UI testing.
- Backend implementation.
- Prompt 13C completion.
- Prompt 13D completion.

## 22.9 Regression safety

Do not modify existing Prompt 13A validator behaviour simply to make the new validator pass.

Do not reopen R8.

Do not conduct repository-wide validator hardening.

Do not modify unrelated test suites.

Run the new Prompt 13B validator and relevant existing project validators where appropriate.

Report exact commands and actual results.

Never fabricate passing results.

---

# 23. DOCUMENTATION SYNCHRONIZATION AND PROJECT STATUS

After completing the B-13 specification, synchronize every relevant current-status document discovered through the repository-wide impact assessment.

At minimum, evaluate these documents:

## 23.1 AI_CONTEXT.md

Record:

- Prompt 13A OWNER ACCEPTED / COMPLETED.
- Prompt 13B actual status.
- Canonical B-13 document path.
- Requirement allocation.
- Screen specification coverage.
- Component specification coverage.
- Traceability status.
- Remaining limitations.
- Next authorized project action.

## 23.2 AI_HANDOFF.md

Record:

- Prompt 13A acceptance.
- Prompt 13B status.
- Canonical deliverable.
- New identifiers.
- Major design decisions.
- Remaining provisional and owner-reserved issues.
- Documentation impact assessment.
- Exact validation results.
- Limitations.
- Next authorized action.

## 23.3 ROADMAP.md

Update Prompt 13 status accurately.

Keep Prompt 13C and Prompt 13D unstarted.

## 23.4 Stage 2 prompt roadmap

Update the Prompt 13B row and related status information only where applicable.

Do not mark later phases as started.

## 23.5 DECISIONS.md

Record new Category B and Category C decisions.

Never rewrite historical decisions.

## 23.6 Progress log

Create a dedicated Prompt 13B completion entry.

Include:

- Work completed.
- Deliverables.
- Screen coverage.
- Component coverage.
- Requirements allocated.
- Decisions recorded.
- Documentation impact results.
- Dependencies.
- Validator results.
- Limitations.
- Next action.

Preserve historical entries.

Do not rewrite old dated snapshots to make the project appear more complete.

## 23.7 Other affected documents

Update additional relevant canonical documents discovered during the impact assessment.

Examples include requirements indexes, documentation indexes, screen inventories and dependency references.

Do not update a document merely for the sake of changing it.

Document the reason for every modification.

---

# 24. DEFINITION OF DONE

Prompt 13B may be reported complete only when the actual deliverables satisfy the following conditions.

| ID | Completion criterion |
|---|---|
| 13B-01 | All 100 existing screen identifiers accounted for |
| 13B-02 | Every Mandatory screen has a detailed specification |
| 13B-03 | Every Conditional screen has explicit gate and visibility conditions |
| 13B-04 | Provisional screen status and dependencies documented |
| 13B-05 | All 10 administrative screens have detailed specifications |
| 13B-06 | Reusable component catalogue completed |
| 13B-07 | Every canonical component has its required specification |
| 13B-08 | Component states and variants documented |
| 13B-09 | Navigation relationships documented and traceable |
| 13B-10 | Desktop, tablet and mobile layouts specified for every screen |
| 13B-11 | Information hierarchy defined for every screen |
| 13B-12 | Data presentation follows existing game-system rules |
| 13B-13 | Relevant accessibility requirements carried forward |
| 13B-14 | Alliance and Warfare interfaces remain strictly separated |
| 13B-15 | Mapless world architecture preserved and map requirement explicitly reconciled |
| 13B-16 | B-13 requirements allocated from the correct global REQ frontier |
| 13B-17 | Screen-to-component relationships traceable |
| 13B-18 | Screen-to-requirement relationships traceable |
| 13B-19 | Existing owner-reserved decisions protected |
| 13B-20 | Category B and C decisions recorded correctly |
| 13B-21 | Conditional and suppressed information handled correctly |
| 13B-22 | Focused Prompt 13B validator created and executed |
| 13B-23 | Relevant documentation links and identifiers reconciled |
| 13B-24 | AI_CONTEXT, AI_HANDOFF, ROADMAP and relevant Stage 2 documents synchronized |
| 13B-25 | Repository-wide documentation impact assessment completed |
| 13B-26 | Documentation impact register produced |
| 13B-27 | Global requirements and screen inventory reconciled |
| 13B-28 | No unauthorized implementation or later-prompt work occurred |

Do not automatically mark every gate PASS.

Use PARTIAL or BLOCKED wherever actual evidence warrants it.

A provisional specification must remain explicitly provisional.

A specification is not an implementation.

---

# 25. FINAL EXECUTION REPORT

At completion, provide a detailed and evidence-based report.

## A. Overall status

Choose one:

- COMPLETE.
- COMPLETE WITH DOCUMENTED LIMITATIONS.
- PARTIAL.
- BLOCKED.

Explain the verdict.

## B. Screen specification results

Report:

- Total screen identifiers accounted for.
- Mandatory screens fully specified.
- Conditional screens specified.
- Provisional screens specified.
- Administrative screens specified.
- Remaining incomplete screens.

## C. Component specification results

Report:

- Total reusable components.
- Component categories.
- Components fully specified.
- Components with unresolved dependencies.
- Component state coverage.

## D. Requirements and traceability

Report:

- First B-13 requirement ID.
- Last B-13 requirement ID.
- Total new requirements.
- Screen-to-component mapping status.
- Screen-to-requirement mapping status.
- Unresolved references.

## E. Navigation and map reconciliation

Report:

- Navigation specification coverage.
- Screen relationship coverage.
- Network View specification.
- Map-related identifiers inspected.
- How the map requirement was reconciled with the accepted mapless architecture.

## F. Decisions

Report:

- New Category B decisions.
- New Category C provisional decisions.
- Owner-reserved questions preserved.

## G. Documentation impact assessment

Report:

- Total relevant documents inspected.
- Documents modified.
- Documents intentionally unchanged.
- Canonical registers reconciled.
- Broken links corrected.
- Remaining documentation inconsistencies.
- Location of the documentation impact register.

## H. Validation

List actual commands and results.

Distinguish:

- Structural validation.
- Identifier validation.
- Cross-reference validation.
- Navigation validation.
- Responsive coverage validation.
- Map reconciliation validation.
- Documentation synchronization validation.
- Python syntax.
- Existing regression suites.
- Runtime verification.

Runtime UI verification must be reported as NOT PERFORMED because no UI implementation is authorized.

## I. Remaining limitations

List every unresolved matter without hiding it.

Distinguish between:

- Genuine specification gaps.
- Provisional design decisions.
- Owner-reserved matters.
- Existing external dependencies.
- Historical limitations.
- Documentation limitations.

## J. Next action

Prompt 13C is the next planned phase.

However, Prompt 13C must remain NOT STARTED and NOT AUTHORIZED until separately authorized by the owner.

Do not generate Prompt 13C automatically.

---

# 26. FINAL EXECUTION INSTRUCTIONS

Execute Prompt 13B thoroughly.

Do not rush through 100 screens with generic descriptions.

Do not treat a component list as a component specification.

Do not treat an existing screen inventory as a completed screen catalogue.

Do not invent gameplay mechanics to fill interface space.

Do not duplicate the foundational research already completed in Prompt 13A.

Do not ask the owner to make routine UI design decisions.

Do not silently resolve owner-reserved matters.

Do not introduce geographic maps contrary to the accepted mapless architecture.

Do not omit map-related scope without an explicit documented reconciliation.

Do not update only the obvious handoff documents and assume repository documentation is synchronized.

Inspect the relevant repository documentation and update every genuinely affected canonical document.

Do not enter Prompt 13C or Prompt 13D.

Do not implement actual frontend functionality.

Keep the specifications consistent, traceable, maintainable and suitable for future AI-assisted implementation.

**ULTIMATE ACCEPTANCE TEST**

A future frontend developer should be able to take the B-13 documentation and understand:

1. Exactly what every screen contains.
2. How every screen is structurally arranged.
3. What information each screen presents.
4. Which reusable components each screen uses.
5. What controls each screen exposes.
6. What those controls are intended to do.
7. Which screens are connected through navigation.
8. How every screen adapts to desktop, tablet and mobile.
9. Which existing game rules govern each screen.
10. Which information is public, private, restricted or suppressed.
11. How the visual system remains consistent.
12. Which dependencies and unresolved matters must be preserved.

The developer must not need to invent the missing interface architecture or ordinary screen and component design.

Nation Supremacy must move from UI foundations to a genuinely complete and implementable game-interface specification.

**BEGIN PROMPT 13B.**


