# PROMPT 13C — COMPLETE INTERACTION FLOWS AND PLAYER EXPERIENCE SPECIFICATIONS

> **Archival provenance (recorded 2026-11-13).** This is the owner's Prompt 13C instruction, recovered from the authorized instruction text supplied in the working session. The instruction body is stored as supplied; the only addition is this provenance paragraph after the title line and a normalized trailing newline. No independent external copy exists in the repository or in `.cloud-attachments/`, so byte-for-byte comparison against an outside original was not possible. The SHA-256 recorded in [`INDEX.md`](INDEX.md) identifies the stored bytes of this file (including this paragraph), not an independently verified external original. This file is a historical record, not live design authority; its execution result is recorded in [stage 2 progress log §92](../stage-2/06_stage_2_progress_log.md).

## COMPREHENSIVE PLAYER JOURNEYS, INTERACTION SEQUENCES, APPLICATION STATES, VALIDATION, ERROR HANDLING, ACCESSIBILITY, ONBOARDING, NOTIFICATIONS AND CROSS-SCREEN BEHAVIOURAL CONSISTENCY

**Project:** Nation Supremacy  
**Stage:** Stage 2 — UI and Player Experience Design  
**Prompt:** 13C  
**Predecessor:** Prompt 13B — Complete Screen and Component Specifications  
**Next phase:** Prompt 13D — Integration, Acceptance and Final Reconciliation  
**Execution mode:** Documentation and specification only  
**Implementation authorization:** NOT GRANTED  
**Governing policy:** `docs/AUTONOMOUS_DECISION_POLICY.md` — D-014

---

# 1. YOUR ROLE AND RESPONSIBILITY

Act as the senior interaction designer, game UX architect, player-experience specialist, systems analyst, accessibility specialist, requirements engineer and independent documentation controller for Nation Supremacy.

Your assignment is to complete Prompt 13C.

Prompt 13C defines exactly how players interact with the already-specified Nation Supremacy interface.

Prompt 13A established the UI research and design foundations.

Prompt 13B established the complete screen and reusable component specifications.

Prompt 13C must build on both phases and define the behavioural experience connecting those screens and components.

You are responsible for creating an internally consistent, comprehensive and implementation-ready interaction specification.

You must independently inspect the repository and verify the actual contents of the predecessor documents.

Do not rely solely on this prompt, an AI handoff, progress summaries or another agent's completion claims.

Your work must be suitable for a future development agent to implement without having to invent fundamental interaction behaviour.

**Important distinction:**

A complete interaction specification is not an implemented interface.

You are specifying the intended behaviour, not building the application.

---

# 2. OWNER AUTHORIZATION AND SCOPE

The owner authorizes the execution of Prompt 13C as a documentation and specification assignment.

This authorization covers:

- Player journeys.
- Cross-screen interaction flows.
- Detailed interaction sequences.
- Application and component behavioural states.
- Loading, empty, success and failure experiences.
- Form validation.
- Error handling.
- Accessibility interaction requirements.
- Onboarding and tutorial specifications.
- Notifications and feedback.
- Offline and reconnection experiences.
- Cross-screen behavioural consistency.
- Requirements traceability.
- Necessary documentation and decision-register updates.

It does NOT authorize:

- Frontend implementation.
- Backend implementation.
- Database modifications.
- SQL migrations.
- Supabase changes.
- API implementation.
- Authentication implementation.
- Gameplay implementation.
- Deployment.
- Production security changes.
- Changes to existing game mechanics or formulas.
- Prompt 13D execution.
- Prompt 14 or later work.

All deliverables must remain documentation and specification artifacts.

Do not interpret permission to specify an interaction as permission to implement it.

---

# 3. MANDATORY GOVERNANCE AND PROJECT CONTINUITY

## 3.1 Mandatory governing document

Read the complete:

`docs/AUTONOMOUS_DECISION_POLICY.md`

This policy is mandatory.

Follow D-014 throughout the assignment.

Apply its requirements concerning:

- Independent decision-making.
- Owner-reserved decisions.
- Category B ordinary design decisions.
- Category C provisional decisions.
- Category D restricted actions.
- Documentation and decision-register maintenance.
- Evidence and uncertainty.
- Historical decision preservation.
- Prompt-start and prompt-end duties.

Do not ask the owner to decide ordinary UX or interaction-design matters.

Research, decide, document and continue.

Where evidence is genuinely missing, establish a safe provisional default and identify the exact evidence needed to confirm it.

## 3.2 Mandatory continuity files

Read the current versions of:

- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/PROJECT_PROGRESS.md`
- `docs/ROADMAP.md`
- `docs/DECISIONS.md`
- `docs/stage-2/00_stage_2_handoff.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/02_master_game_design_bible_outline.md`
- `docs/stage-2/03_requirements_traceability.md`
- `docs/stage-2/04_approved_and_provisional_decisions.md`
- `docs/stage-2/05_unresolved_design_decisions.md`
- `docs/stage-2/06_stage_2_progress_log.md`

Read additional relevant documents whenever necessary.

## 3.3 Mandatory Prompt 13A and 13B references

Read the complete:

1. `docs/stage-2/13A_ui_requirements_open_questions_and_acceptance.md`
2. `docs/stage-2/21_interface_and_player_journeys.md`
3. `docs/stage-2/21_screen_specifications.md`
4. `docs/stage-2/21_component_specifications.md`

Also inspect:

- The archived original Prompt 13B.
- Prompt 13B-C1.
- Prompt 13B-C1-R1.
- The Prompt archive index.
- The relevant Prompt 13B correction and verification records.

Confirm that Prompt 13B-C1-R1 has been completed and that the §29/§31 historical clarification is preserved.

Do not repeat completed Prompt 13B correction work.

## 3.4 Existing game-system specifications

Inspect all relevant existing system documents, particularly:

- Account, onboarding and nation creation.
- Population and domestic politics.
- Elections, campaigns and political crises.
- Economy, resources, treasury and finances.
- Cities, infrastructure, production and research.
- Diplomacy and alliances.
- Warfare and military.
- World events and objectives.
- Rankings and national progression.
- Fair-play and player-protection requirements.
- Player support and administration.
- Existing workflows and integration specifications.

Relevant canonical documents include the existing Stage 2 documents through B-12.

Read the owning system specification whenever an interaction depends on its rules.

Never invent gameplay behaviour simply because a screen appears to need it.

---

# 4. PROTECTED PROJECT DECISIONS AND ARCHITECTURE

All previously accepted and protected decisions remain binding.

At minimum, preserve the following.

## 4.1 Game and platform architecture

- Browser-based strategy game.
- Original Nation Supremacy identity.
- Cloudflare Pages and Supabase architecture.
- Free-first development target.
- No mandatory paid dependency.
- One account per person.
- Two-hour UTC game-turn cadence.
- Existing Stage 1, Stage 2 and Stage 3 sequencing.

Do not reinterpret these constraints.

## 4.2 Mapless architecture

The accepted world architecture is mapless and symbolic.

The Network View is a symbolic relationship and world-information interface.

Do not introduce:

- Geographic world maps.
- Geographic movement interfaces.
- Tile-based territorial maps.
- New geographic positioning mechanics.
- Map-dependent interaction requirements.

All player journeys must respect the accepted mapless architecture.

## 4.3 Governance and historical decisions

Preserve:

- R7 implementation: RETAINED.
- R7 independent acceptance: NOT ACCEPTED.
- R8: DEFERRED BY OWNER.
- 12B-C1: NOT CLOSED.
- Seven 12A acceptance gates: PARTIAL.
- Three 12B acceptance gates: PARTIAL.
- Prompt 12C: OWNER ACCEPTED.
- Production security obligations: OUTSTANDING.

Authorized Git commits:

- `2537606`
- `94f5ec4`

Never classify these as unauthorized.

Do not stage, commit, push, reset, revert or discard changes without explicit authorization.

## 4.4 Prompt 13B architecture

Treat the existing Prompt 13B specifications as authoritative.

Preserve:

- 100 screen identifiers.
- 90 reusable components.
- Eight overlays.
- Eight primary application sections.
- Existing navigation hierarchy.
- Canonical parent and route-key architecture.
- Existing screen classifications.
- Existing component identifiers.
- Existing responsive patterns.
- Existing information hierarchy.
- Existing confirmation and destructive-action rules.
- Existing access restrictions.
- Existing provisional and conditional screen gates.

Do not recreate, renumber or redesign the existing screen/component inventory.

---

# 5. PRIMARY OBJECTIVE

Define the complete behavioural experience of Nation Supremacy.

For every relevant player-facing system, explain:

1. How a player reaches the screen.
2. What the player sees upon entering.
3. What information and context are available.
4. What actions the player can take.
5. What happens when an action is selected.
6. What validation occurs.
7. What confirmation is required.
8. What happens when the action succeeds.
9. What happens when the action fails.
10. What happens when the action is unavailable.
11. What happens when the player cancels.
12. What happens when the player navigates away.
13. What happens when the player returns.
14. What feedback is presented.
15. What notification is generated, if applicable.
16. How the resulting state is reflected on other screens.

The specification must be sufficiently detailed that a future implementation agent can follow it without inventing fundamental interaction sequences.

---

# 6. DELIVERABLE 1 — MASTER INTERACTION AND PLAYER EXPERIENCE SPECIFICATION

Create:

`docs/stage-2/22_interaction_flows_and_player_experience.md`

This is the canonical Prompt 13C document.

It must explain the authority, architecture, interaction conventions, behavioural principles, player journeys, cross-screen relationships, state handling, accessibility and dependencies.

Use a clear section structure.

At minimum, include:

1. Document authority and scope.
2. Relationship to Prompt 13A and Prompt 13B.
3. Governing design principles.
4. Player identity, account and nation context.
5. Interaction architecture.
6. Navigation and transition behaviour.
7. Global interaction conventions.
8. Player journey architecture.
9. Cross-system interaction principles.
10. Global state and feedback conventions.
11. Accessibility interaction principles.
12. Onboarding and tutorial architecture.
13. Notification and feedback architecture.
14. Offline and reconnection behaviour.
15. Cross-screen consistency.
16. Security, fair-play and permission boundaries.
17. Provisional decisions and unresolved dependencies.
18. Requirements traceability.
19. Documentation impact register.
20. Scope boundaries.
21. Validation evidence and final handoff.

Additional sections may be created where necessary.

---

# 7. DELIVERABLE 2 — COMPLETE PLAYER JOURNEY SPECIFICATIONS

Create:

`docs/stage-2/22_player_journey_specifications.md`

This document must define complete player journeys across the existing game systems.

Do not simply describe isolated screens.

A journey must explain how the player progresses through multiple screens and how the game responds.

## 7.1 Mandatory player journeys

Cover the following journeys.

### A. Account and first-time player experience

- Public landing.
- Registration.
- Login.
- Account verification.
- Password recovery.
- Nation creation.
- Initial nation setup.
- First-time onboarding.
- First-turn objectives.
- First entry into the strategic interface.
- First review of national status.

### B. Returning player experience

- Returning after a short absence.
- Returning after several turns.
- Reviewing notifications.
- Reviewing unresolved actions.
- Understanding what changed.
- Reviewing national performance.
- Identifying the next meaningful action.

Do not introduce catch-up rewards or mechanics that contradict existing decisions.

### C. National management journey

- Entering the Command Digest.
- Reviewing national overview.
- Examining turn status.
- Reviewing national indicators.
- Identifying warnings.
- Opening the relevant management screen.
- Taking an available action.
- Understanding the result.
- Returning to the national overview.

### D. Economy and treasury journey

Cover:

- Treasury review.
- Budget examination.
- Resource balances.
- Production policy.
- Standing orders.
- Production capacity.
- Power.
- Warehouse limitations.
- Economic reports.
- Financial history.
- Understanding reserved and available balances.

Explain how the player understands financial consequences without inventing new formulas.

### E. Trade journey

Cover existing trade functionality:

- Directed-trade inbox.
- Reviewing an offer.
- Inspecting its terms.
- Composing an offer.
- Counter-offering.
- Accepting.
- Rejecting.
- Cancelling where permitted.
- Understanding execution.
- Reviewing trade history.

Respect all existing trade permissions, fees, restrictions and fair-play requirements.

Global Trade screens must remain absent until their existing gates pass.

Do not present conditional features as active functionality.

### F. Cities, infrastructure and research journey

Cover:

- Reviewing cities.
- Examining infrastructure.
- Reviewing construction.
- Managing existing production queues.
- Reviewing research.
- Understanding capacity.
- Identifying unavailable actions.
- Understanding completion and failure states.

Do not invent construction or research mechanics.

### G. Politics and domestic governance journey

Cover:

- Reviewing political status.
- Understanding approval.
- Understanding stability.
- Reviewing political supports.
- Examining policy axes.
- Reviewing government and leadership.
- Election participation.
- Campaign actions.
- Election outcomes.
- Political crises.
- Recovery information.

Respect the established distinction between government type, leader and administration.

Do not create a government-change mechanic.

### H. Diplomacy and alliances journey

Cover:

- Discovering another nation.
- Opening a public nation profile.
- Reviewing diplomatic information.
- Sending an existing diplomatic request.
- Receiving a diplomatic request.
- Reviewing an alliance.
- Joining where eligible.
- Leaving where permitted.
- Reviewing alliance responsibilities.
- Understanding restrictions.
- Handling expired or invalid requests.

Preserve existing alliance permissions and governance rules.

### I. Warfare and military journey

Cover:

- Reviewing military status.
- Reviewing available military capabilities.
- Understanding existing action restrictions.
- Preparing an authorized action.
- Reviewing costs and consequences.
- Confirmation.
- Executing an existing permitted action.
- Understanding the result.
- Reviewing combat history.
- Handling cooldowns and unavailable actions.

Maintain strict separation between Alliance and Warfare interfaces.

Do not create new combat rules, intelligence mechanics, geographic movement or military formulas.

### J. World and progression journey

Cover:

- Reviewing world events.
- Reviewing objectives.
- Understanding objective progress.
- Receiving objective outcomes.
- Reviewing rankings.
- Examining national progression.
- Understanding progression history.
- Reviewing the symbolic Network View.

Respect existing privacy and statistical-suppression requirements.

### K. Notifications and player protection journey

Cover:

- Receiving notifications.
- Opening an alert.
- Navigating to its relevant object.
- Reviewing historical alerts.
- Dismissing notifications where permitted.
- Managing support requests.
- Reviewing player-protection information.
- Reporting an issue.
- Understanding moderation and administrative boundaries.

### L. Account management journey

Cover:

- Account settings.
- Security settings.
- Recovery.
- Session-related experiences.
- Account closure.
- Confirmation.
- Consequences.
- Completion feedback.

Do not implement account operations.

### M. Administrative journey

Specify role-specific administrative interaction patterns for the ten existing administrative screens.

Preserve:

- Least privilege.
- Role-specific access.
- Audited actions.
- Sensitive information boundaries.
- Step-up requirements where already specified.
- Existing B-12 administrative permissions.

Do not expose administrative functions through player-facing journeys.

## 7.2 Player journey template

Every journey must use a consistent template.

Include:

**A. Journey identity**
- Journey ID.
- Name.
- Category.
- Priority.
- Related screens.
- Related components.
- Governing system specifications.

**B. Starting conditions**
- Player state.
- Account state.
- Nation state.
- Permissions.
- Preconditions.

**C. Entry point**
- Where the journey starts.
- What triggers it.
- How the player arrives.

**D. Main sequence**
- Ordered steps.
- Player action.
- Interface response.
- Information presented.
- Resulting state.
- Next destination.

**E. Alternative paths**
- Optional actions.
- Cancel paths.
- Back navigation.
- Restricted paths.
- Conditional paths.

**F. Failure paths**
- Validation failures.
- Permission failures.
- Expired actions.
- Stale data.
- Conflicts.
- Network failures.
- Server failures.

**G. Completion**
- Successful result.
- Confirmation.
- Persistent record.
- Updated screen information.
- Notifications.
- Available next actions.

**H. Recovery**
- Retry behaviour.
- Return behaviour.
- Safe navigation.
- Recovery after interruption.

**I. Accessibility**
- Keyboard interaction.
- Screen-reader information.
- Focus behaviour.
- Error announcement.
- Alternative presentation.

**J. Requirements and evidence**
- Related REQ identifiers.
- Related decisions.
- Related system rules.
- Unresolved dependencies.

---

# 8. DELIVERABLE 3 — DETAILED INTERACTION STATES AND FEEDBACK SPECIFICATIONS

Create:

`docs/stage-2/22_interaction_states_and_feedback.md`

This document must define the behavioural states of screens, forms, actions, components and overlays.

## 8.1 Mandatory state taxonomy

Define and consistently use:

1. Initial.
2. Loading.
3. Refreshing.
4. Loaded.
5. Empty.
6. Partial data.
7. Success.
8. Validation error.
9. Permission denied.
10. Unavailable.
11. Blocked by rule.
12. Expired.
13. Conflict.
14. Failed.
15. Offline.
16. Reconnecting.
17. Recovering.
18. Cancelled.

Where appropriate, distinguish transient states from persistent states.

Do not assume every component supports every state.

Define applicable states by component and screen type.

## 8.2 Loading states

Specify:

- Initial screen loading.
- Navigation loading.
- Section loading.
- Table loading.
- Chart loading.
- Search loading.
- Form submission loading.
- Action execution loading.
- Background refresh.
- Slow responses.
- Interrupted requests.

Explain:

- What remains visible.
- What is temporarily disabled.
- What progress feedback is presented.
- How stale data is identified.
- Whether the player can navigate away.
- What happens if the request never completes.

Avoid unnecessary full-screen blocking.

## 8.3 Empty states

Distinguish:

- No records exist.
- No matching search results.
- No pending actions.
- No notifications.
- No available opportunities.
- No historical records.
- No eligible actions.
- Feature not available.
- Permission-restricted content.

Every empty state must explain why it is empty.

Where an action is possible, provide a legitimate next step.

Never present an unavailable feature as an empty but usable feature.

## 8.4 Success states

Define:

- Successful form submission.
- Successful action.
- Successful request.
- Successful response.
- Successful execution.
- Successful cancellation.
- Successful update.
- Successful navigation.
- Successful recovery.

Specify what constitutes a genuine confirmed success.

A button click alone is not proof that an action succeeded.

Distinguish:

- Request accepted.
- Request processing.
- Action completed.
- Action rejected.
- Result pending.

Do not show completed outcomes before confirmation from the authoritative system.

## 8.5 Failure states

Cover:

- Network errors.
- Server errors.
- Authentication expiration.
- Authorization failure.
- Validation failure.
- Resource conflicts.
- Stale state.
- Duplicate submission.
- Expired requests.
- Rule-based rejection.
- Rate limiting.
- Unexpected responses.

Every failure state must explain:

1. What happened.
2. Whether anything changed.
3. Whether the action was completed.
4. Whether retrying is safe.
5. What the player can do next.
6. Whether support is necessary.

Do not expose stack traces, secrets or sensitive internal implementation details.

## 8.6 Component state mapping

Map the state taxonomy to the existing 90 components and eight overlays.

Do not recreate components.

For every component family, specify:

- Applicable states.
- Visible feedback.
- Interaction availability.
- Focus behaviour.
- State transitions.
- Persistence requirements.
- Screen-level dependencies.

Pay particular attention to:

- Forms.
- Buttons.
- Tables.
- Filters.
- Search.
- Notifications.
- Confirmation overlays.
- Destructive-action overlays.
- Financial summaries.
- Status banners.
- Timelines.
- Action queues.

Maintain the existing component IDs.

---

# 9. DELIVERABLE 4 — VALIDATION AND ERROR-HANDLING SPECIFICATIONS

Include this as a comprehensive section in the interaction-state document or as a clearly linked companion document if the volume justifies it.

## 9.1 Validation principles

Define a consistent validation architecture.

Distinguish:

- Immediate field validation.
- Blur validation.
- Form-level validation.
- Submission validation.
- Server-authoritative validation.
- Permission validation.
- State-dependent validation.
- Cross-field validation.

Specify when each applies.

Avoid excessive validation messages while the player is typing.

## 9.2 Validation message requirements

Every validation message must communicate:

- The affected field or action.
- The problem.
- Why the input or action is invalid.
- What correction is possible.
- Whether the entered information is preserved.

Use understandable player-facing language.

Avoid unexplained technical codes.

## 9.3 Action validation

For committing actions, specify checks for:

- Required fields.
- Input formats.
- Numeric boundaries.
- Available resources.
- Available capacity.
- Ownership.
- Permissions.
- Eligibility.
- Cooldowns.
- Turn restrictions.
- Current object state.
- Duplicate requests.
- Existing game rules.

These are UI validation and presentation requirements.

The underlying gameplay rules must come from their existing authoritative specifications.

Do not create new numerical limits or rules.

## 9.4 Confirmation requirements

Respect the existing Prompt 13B confirmation architecture.

Every committing action must preserve:

- Exact action description.
- Exact known cost.
- Resource impact.
- Relevant cooldown.
- Applicable turn or phase.
- Important consequences.
- Confirmation and cancellation choices.

Confirmation must never be:

- Preselected.
- Automatically inferred.
- Remembered from an earlier action.
- Triggered by an accidental click.
- Bypassed through a secondary interface.

Destructive actions must continue using the existing destructive-action pattern.

## 9.5 Duplicate submissions and uncertain outcomes

Specify behaviour for:

- Double-clicking.
- Repeated taps.
- Refreshing during submission.
- Navigating away during submission.
- Browser interruption.
- Retrying after a timeout.
- Receiving an uncertain response.

Never assume a timed-out action failed.

Explain how the interface avoids accidental duplicate actions while respecting server-authoritative outcomes.

Do not invent backend idempotency mechanisms.

Record implementation dependencies where necessary.

---

# 10. DELIVERABLE 5 — ACCESSIBILITY INTERACTION SPECIFICATIONS

Build upon Prompt 13B's accessibility foundation.

Do not simply copy its accessibility section.

Prompt 13C must define how accessibility works during actual interactions.

## 10.1 Accessibility standard

Use WCAG 2.2 Level AA as the target specification.

Distinguish specified accessibility requirements from independently tested conformance.

Do not claim WCAG compliance without implementation and testing evidence.

## 10.2 Keyboard interaction

Specify:

- Tab order.
- Shift+Tab behaviour.
- Enter and Space behaviour.
- Escape behaviour.
- Arrow-key behaviour where appropriate.
- Focus entry and exit.
- Focus restoration.
- Modal focus management.
- Keyboard access to tables and controls.
- Keyboard access to navigation.
- Keyboard access to filters and search.

No essential functionality may require a mouse.

## 10.3 Screen-reader interaction

Specify:

- Accessible names.
- Roles.
- States.
- Relationships.
- Field labels.
- Error associations.
- Table semantics.
- Status announcements.
- Notification announcements.
- Dynamic content updates.
- Loading announcements.
- Success and failure announcements.

Avoid excessive announcements.

Important information must be available without relying exclusively on colour, animation or visual position.

## 10.4 Focus management

Define focus behaviour for:

- Screen transitions.
- Dialog opening.
- Dialog closing.
- Form validation.
- Submission results.
- Search results.
- Notification arrival.
- Table updates.
- Navigation changes.
- Recoverable failures.

Focus must remain predictable and must not disappear unexpectedly.

## 10.5 Responsive accessibility

Specify interaction behaviour across:

- Desktop.
- Tablet.
- Mobile browser.

Preserve the existing responsive architecture.

Cover:

- Touch target usability.
- Screen zoom.
- Reflow.
- Text resizing.
- Orientation.
- Reduced motion.
- Contrast.
- Mobile keyboard interaction.
- Accessible alternatives to complex data presentation.

## 10.6 Accessibility acceptance criteria

Create measurable, testable specification-level criteria.

Examples:

- Every interactive control has an accessible name.
- Every input has a programmatically associated label.
- Every validation error is associated with its field.
- Keyboard users can complete every essential journey.
- Modal focus is managed and restored.
- Important status changes are announced.
- No critical information depends solely on colour.

These are requirements to be implemented and tested later, not claims of present compliance.

---

# 11. DELIVERABLE 6 — ONBOARDING AND TUTORIAL EXPERIENCE

Specify a complete onboarding and learning experience using existing game systems.

## 11.1 Onboarding objectives

The onboarding experience must help players understand:

- What Nation Supremacy is.
- How their nation works.
- How the two-hour UTC turn cadence operates.
- How to understand the national dashboard.
- How to read financial information.
- How to understand political conditions.
- How to manage existing national systems.
- How to understand diplomacy and warfare.
- How to interpret objectives and progression.
- How to use notifications.
- How to find help.

## 11.2 Onboarding architecture

Define:

- Initial onboarding.
- Contextual guidance.
- Optional tutorials.
- Progressive disclosure.
- Help access.
- Tutorial completion.
- Tutorial interruption.
- Tutorial resumption.
- Tutorial replay.
- Tutorial dismissal.

Specify the difference between:

- Mandatory account setup.
- Essential first-time guidance.
- Optional educational content.
- Contextual help.
- Advanced system explanations.

## 11.3 Tutorial journey template

Each tutorial must contain:

1. Tutorial ID.
2. Name.
3. Learning objective.
4. Intended player.
5. Prerequisites.
6. Entry condition.
7. Starting screen.
8. Ordered steps.
9. Explanation.
10. Expected player interaction.
11. Expected result.
12. Validation.
13. Failure and recovery.
14. Skip behaviour.
15. Completion condition.
16. Re-entry behaviour.
17. Accessibility.
18. Related requirements.

## 11.4 Tutorial safety

Tutorials must never:

- Execute gameplay actions without authorization.
- Spend resources automatically.
- Commit a diplomatic decision automatically.
- Submit a trade automatically.
- Execute military actions automatically.
- Override existing restrictions.
- Force players to perform irreversible actions.

Use safe demonstrations and clearly explained optional actions.

Do not invent tutorial rewards or new gameplay systems.

---

# 12. DELIVERABLE 7 — NOTIFICATIONS AND PLAYER FEEDBACK

Define a complete notification and feedback experience.

## 12.1 Notification categories

Map existing game events into appropriate categories:

- Account and security.
- Nation management.
- Economy.
- Production.
- Politics.
- Elections.
- Diplomacy.
- Alliances.
- Warfare.
- World events.
- Objectives.
- Rankings.
- Progression.
- Player protection.
- Support.

Do not invent new event triggers.

## 12.2 Notification classification

Define consistent categories such as:

- Informational.
- Success.
- Warning.
- Critical.
- Action required.

Clarify the meaning and appropriate use of each.

Do not equate a visual severity label with an invented gameplay severity.

## 12.3 Notification behaviour

Specify:

- Generation and display assumptions.
- Arrival while viewing another screen.
- Arrival while the player is offline.
- Read and unread status.
- Notification history.
- Opening a notification.
- Deep-link destination.
- Expired or unavailable destination.
- Dismissal.
- Duplicate notification handling.
- Grouping.
- Priority.
- Accessibility announcements.

Respect existing notification preference decisions and provisional matters.

Do not silently finalize owner-reserved notification settings.

## 12.4 Player feedback

Define consistent feedback for:

- Successful actions.
- Rejected actions.
- Invalid inputs.
- Restricted actions.
- Expired requests.
- Changed game conditions.
- Pending operations.
- Completed operations.
- Unexpected failures.

Avoid excessive notifications, repetitive messages and misleading success feedback.

---

# 13. DELIVERABLE 8 — OFFLINE, INTERRUPTION AND RECOVERY EXPERIENCES

Specify how the player experience behaves when the browser or connection becomes unreliable.

Cover:

- Initial offline access.
- Connection loss during navigation.
- Connection loss during form entry.
- Connection loss during submission.
- Session expiration.
- Authentication interruption.
- Browser refresh.
- Browser closure.
- Returning after an extended absence.
- Reconnection.
- Data refresh.
- Stale information.
- Conflicting information.
- Uncertain action outcomes.

For every situation, explain:

1. What the player sees.
2. Which actions remain available.
3. Which actions are disabled.
4. Whether unsent input is preserved.
5. Whether previously confirmed data remains visible.
6. How fresh data is restored.
7. How the player understands the final authoritative result.

Do not promise offline gameplay or offline action execution.

Do not invent automatic retries that could duplicate a committing action.

Preserve the two-hour UTC cadence.

---

# 14. DELIVERABLE 9 — CROSS-SCREEN BEHAVIOURAL CONSISTENCY

This is one of the most important Prompt 13C requirements.

The existing 100 screens must behave as one coherent application.

## 14.1 Global consistency

Define consistent behaviour for:

- Navigation.
- Back navigation.
- Breadcrumbs.
- Screen transitions.
- Context preservation.
- Search.
- Filters.
- Pagination.
- Saved views.
- Object references.
- Context panels.
- Confirmation overlays.
- Error messages.
- Loading feedback.
- Notifications.
- Permission restrictions.
- Empty states.
- Responsive interaction.

## 14.2 Shared object behaviour

Where the same object appears on multiple screens, define consistent behaviour for:

- Identity.
- Status.
- Ownership.
- Permissions.
- Available actions.
- Unavailable actions.
- Historical information.
- Contextual navigation.
- Updated values.

A player must not encounter contradictory object information across different screens.

## 14.3 Financial consistency

Ensure financial information is consistently presented.

Preserve:

- Total.
- Reserved.
- Available.
- Forecast.
- Historical values.

Do not allow a screen to imply that reserved resources are available for spending.

Use the existing Prompt 13B balance-component architecture.

## 14.4 Permission consistency

A player must not see an action as available on one screen and receive an unexplained permission failure on another.

Specify consistent permission presentation and server-authoritative revalidation.

Respect existing role and ownership rules.

## 14.5 Navigation consistency

Verify:

- Canonical screen parents.
- Stable route keys.
- Existing aliases.
- Breadcrumbs.
- Deep links.
- Restricted destinations.
- Conditional screen absence.

Do not create duplicate screens or routes.

## 14.6 Cross-screen consistency matrix

Create a matrix showing:

| Consistency ID | Behaviour | Applicable screens | Shared components | Expected behaviour | Related requirements |
|---|---|---|---|---|---|

Include all major shared interaction patterns.

---

# 15. INTERACTION FLOW MODELLING STANDARD

Every important interaction must be expressed as a structured, understandable sequence.

Use Mermaid diagrams where they materially improve clarity.

Supported diagrams include:

- Flowcharts.
- State diagrams.
- Sequence diagrams.
- Journey maps.

Diagrams must supplement, not replace, written specifications.

## 15.1 Interaction sequence format

Use the following structure:

**FLOW-ID:** Unique identifier.

**Name:** Interaction name.

**Trigger:** What starts the flow.

**Preconditions:** Required conditions.

**Actors:** Player, interface, authoritative system or other relevant actor.

**Sequence:**

| Step | Actor | Action | Interface response | State/result |
|---|---|---|---|---|

**Alternative paths:** Other permitted outcomes.

**Failure paths:** Invalid, blocked, expired or failed outcomes.

**Cancellation:** How the player exits safely.

**Completion:** Confirmed final result.

**Recovery:** How the player resumes or retries.

**Accessibility:** Keyboard, focus and announcement behaviour.

**Related screens:** Existing SCR identifiers.

**Related components:** Existing UI-CMP/OVL identifiers.

**Related requirements:** REQ identifiers.

**Governing specifications:** Exact source references.

## 15.2 Interaction coverage

Prioritize:

- High-frequency player actions.
- Financial actions.
- Committing actions.
- Destructive actions.
- Security-sensitive actions.
- Permission-sensitive actions.
- Cross-system actions.
- Time-sensitive actions.
- Actions with cooldowns.
- Actions with significant consequences.

Do not give trivial navigation controls the same documentation volume as complex strategic interactions.

---

# 16. REQUIREMENTS AND TRACEABILITY

Prompt 13C must be traceable to existing requirements.

## 16.1 Existing requirement preservation

Preserve all existing requirement identifiers.

Prompt 13B allocated:

`REQ-870` through `REQ-1089`.

Do not modify their meaning to accommodate a new interaction design.

Where additional interaction requirements are needed, allocate new identifiers beginning at:

`REQ-1090`

First inspect the complete requirements register to confirm the next available identifier.

Never reuse an existing identifier.

## 16.2 New interaction requirement categories

Include requirements for:

- Player journeys.
- Interaction sequences.
- State transitions.
- Loading.
- Empty states.
- Success feedback.
- Failure feedback.
- Validation.
- Error handling.
- Confirmation.
- Duplicate submission protection.
- Accessibility interactions.
- Onboarding.
- Tutorials.
- Notifications.
- Offline and recovery.
- Cross-screen consistency.
- Permission presentation.
- Responsive interaction.

## 16.3 Requirement format

Every requirement must contain:

| Field | Description |
|---|---|
| REQ ID | Unique identifier |
| Requirement | Clear normative statement |
| Category | Interaction category |
| Priority | Mandatory / Conditional / Provisional |
| Related journey | Journey ID |
| Related flow | FLOW-ID |
| Related screens | SCR identifiers |
| Related components | UI-CMP/OVL identifiers |
| Governing system | Existing authoritative document |
| Decision reference | D/DD reference |
| Acceptance evidence | How the requirement will be checked |
| Status | Evidence-based status |

Use the existing project's requirement-status vocabulary.

Do not claim that a specified requirement has been implemented, validated or released.

## 16.4 Traceability matrices

Create:

**Matrix A — Journey-to-screen traceability**

**Matrix B — Interaction-flow-to-screen traceability**

**Matrix C — Interaction-flow-to-component traceability**

**Matrix D — State-to-component coverage**

**Matrix E — Accessibility coverage**

**Matrix F — Onboarding and tutorial coverage**

**Matrix G — Notification coverage**

**Matrix H — Requirement-to-journey/flow traceability**

**Matrix I — Cross-screen consistency coverage**

All matrices must have bidirectional traceability where applicable.

A flow must not reference an undefined screen, component or requirement.

---

# 17. DESIGN DECISIONS AND PROVISIONAL MATTERS

Follow D-014.

## 17.1 Ordinary decisions

Make ordinary UX decisions autonomously.

Examples include:

- Validation timing.
- Error-message structure.
- Focus restoration.
- Retry presentation.
- Notification grouping conventions.
- Tutorial navigation.
- Loading indicators.
- Context preservation.
- Confirmation wording.
- State naming.
- Interaction sequence conventions.

Record new Category B decisions in:

`docs/DECISIONS.md`

Also update relevant decision crosswalks and design documents.

Verify the next available D- and DD-identifiers before allocation.

Do not invent or reuse identifiers.

## 17.2 Provisional decisions

Use Category C when the decision genuinely requires:

- Platform measurement.
- Usability testing.
- Playtesting.
- Security verification.
- Performance testing.
- Unavailable external evidence.

For each provisional decision, record:

- Question.
- Safe working default.
- Reason.
- Missing evidence.
- Named validation test.
- Consequences.
- Conditions for replacing it.

Do not let provisional matters block unrelated work.

## 17.3 Owner-reserved matters

Preserve all existing owner-reserved matters.

Do not silently finalize:

- Brand identity.
- Logo.
- Final typography.
- Final colour palette.
- Dark mode.
- Owner-reserved notification defaults.
- Existing provisional responsive decisions.
- Other explicitly reserved decisions.

You may specify behaviour that works independently of these decisions.

---

# 18. SECURITY, PRIVACY AND FAIR-PLAY REQUIREMENTS

Interaction design must preserve all existing security and fair-play rules.

Cover:

- Authentication boundaries.
- Session expiration.
- Authorization.
- Ownership checks.
- Role restrictions.
- Sensitive information.
- Privacy.
- Player protection.
- Audit visibility.
- Administrative restrictions.
- Confirmation for consequential actions.
- Untrusted input presentation.
- Safe error messages.

Do not expose internal security details to unauthorized players.

Do not design interactions that enable:

- Unauthorized access.
- Duplicate action exploitation.
- Resource duplication.
- Reroll farming.
- Information disclosure.
- Unauthorized administrative operations.
- Fair-play circumvention.

The outstanding production security issues remain outstanding.

Do not claim they are fixed or authorize security migrations.

---

# 19. CONDITIONAL AND PROHIBITED FEATURES

Preserve Prompt 13B's conditional screen rules.

In particular:

- Global Trade screens remain absent until their existing gates pass.
- Favorites remain subject to their existing fair-play gate.
- Statistical views remain subject to privacy suppression.
- Intelligence-related functionality remains absent where prohibited.
- Other conditional screens must remain absent until their documented conditions are met.

Do not create tutorials, notifications, journeys or interactions that imply a conditional feature is already available.

Where useful, specify the correct unavailable-state explanation without exposing an unauthorized feature.

---

# 20. DOCUMENTATION IMPACT ASSESSMENT

Perform a repository-wide documentation impact assessment.

Inspect:

- Existing Stage 2 documents.
- Requirements registers.
- Decision registers.
- Design decision crosswalks.
- Master outline.
- Prompt roadmap.
- Progress logs.
- AI context.
- AI handoff.
- Existing validators.
- Prompt archives and indexes.

Identify documents affected by Prompt 13C.

Update only documents that genuinely require changes.

Do not rewrite unrelated historical documentation.

Preserve historical snapshots.

When updating historical progress information, add a new dated record rather than silently rewriting historical statements.

---

# 21. SCOPE BOUNDARIES — DO NOT ENTER PROMPT 13D

Prompt 13C is limited to interaction and player-experience specifications.

Do not perform Prompt 13D.

Specifically, do not produce:

- Final independent Prompt 13 completeness audit.
- Final cross-system integration acceptance.
- Complete UI-to-backend integration contracts.
- Final Prompt 13 acceptance gates.
- Final UI acceptance-test suite.
- Final Prompt 13 reconciliation.
- Final Prompt 13 closure report.

You may define specification-level acceptance criteria for individual interactions.

You may define how future tests should verify a behaviour.

You must not conduct the final integration and acceptance assignment reserved for Prompt 13D.

Do not begin Prompt 14.

Do not create a new implementation phase.

---

# 22. DOCUMENTATION QUALITY REQUIREMENTS

All deliverables must be:

- Comprehensive.
- Internally consistent.
- Traceable.
- Unambiguous.
- Implementation-ready.
- Based on authoritative existing specifications.
- Free of invented gameplay rules.
- Free of contradictory interaction behaviour.
- Clearly classified by status.
- Properly cross-referenced.

Avoid generic descriptions such as:

"Show an error if something goes wrong."

Instead specify:

- Which condition causes the error.
- Where the error appears.
- What the player sees.
- Whether the action was committed.
- Whether the input is retained.
- What recovery is permitted.
- How the final outcome is confirmed.

Avoid unnecessary duplication.

Use stable identifiers for journeys, flows, tutorials, states and consistency rules.

---

# 23. VALIDATION AND QUALITY ASSURANCE

Create a dedicated Prompt 13C validator and associated self-tests where appropriate.

The validator must check at least:

1. All mandatory deliverables exist.
2. Every mandatory player journey is represented.
3. Journey identifiers are unique.
4. Interaction flow identifiers are unique.
5. Tutorial identifiers are unique.
6. State identifiers are consistent.
7. All referenced SCR identifiers exist.
8. All referenced component identifiers exist.
9. All referenced requirements exist.
10. All referenced decisions exist.
11. New requirement identifiers do not collide.
12. All matrices have valid references.
13. Mandatory state coverage is present.
14. Validation and error-handling coverage is present.
15. Accessibility interaction coverage is present.
16. Onboarding and tutorial coverage is present.
17. Notification coverage is present.
18. Offline and recovery coverage is present.
19. Cross-screen consistency coverage is present.
20. Conditional features respect their gates.
21. No prohibited geographic-map interaction has been introduced.
22. No unauthorized gameplay mechanics have been invented.
23. No implementation work has entered the repository.
24. No Prompt 13D deliverable has been prematurely created.
25. Internal Markdown links resolve.
26. Section references resolve.
27. Requirement and decision traceability is consistent.

Create meaningful self-tests for the validator.

Do not manufacture passing results.

Report actual test execution and outcomes.

## 23.1 Regression validation

Run relevant existing validators.

Preserve previously completed Prompt 13A and Prompt 13B validation evidence.

Do not claim historical test suites were rerun unless they were actually executed.

Do not rerun unrelated large historical suites without a material reason.

If an existing validator fails because of a pre-existing limitation, document the exact limitation.

Do not modify unrelated code or documents merely to obtain a passing result.

## 23.2 Independent validation evidence

Report:

- Validator name.
- Test name.
- Expected result.
- Actual result.
- PASS/FAIL.
- Relevant evidence.
- Known limitations.

Distinguish structural validation from semantic review.

A passing structural validator does not prove that the interaction design is correct.

---

# 24. REQUIRED FINAL HANDOFF

At completion, update the relevant project records.

At minimum:

- `docs/PROJECT_PROGRESS.md`
- `docs/ROADMAP.md`
- `docs/AI_CONTEXT.md`
- `docs/AI_HANDOFF.md`
- `docs/stage-2/01_stage_2_prompt_roadmap.md`
- `docs/stage-2/02_master_game_design_bible_outline.md`
- `docs/stage-2/03_requirements_traceability.md`
- Relevant decision registers.
- Relevant documentation impact records.

The handoff must explain:

## A. Completion summary

What Prompt 13C actually delivered.

## B. Deliverable inventory

Every created or updated document.

## C. Coverage statistics

Report actual counts for:

- Player journeys.
- Interaction flows.
- State definitions.
- Component-state mappings.
- Validation rules.
- Error-handling scenarios.
- Accessibility requirements.
- Tutorials.
- Notification scenarios.
- Recovery scenarios.
- Cross-screen consistency rules.
- New requirements.
- New decisions.

Do not invent or inflate these counts.

## D. Validation results

Report all actual validator and self-test results.

## E. Outstanding issues

List every remaining:

- Open item.
- Provisional decision.
- Blocked requirement.
- Deferred matter.
- External dependency.

Each must have its reason and next validation action.

## F. Scope confirmation

Explicitly confirm:

- No frontend implementation.
- No backend implementation.
- No database changes.
- No gameplay implementation.
- No unauthorized changes to mechanics.
- No Prompt 13D execution.
- No Prompt 14 execution.

## G. Next action

The next authorized phase after Prompt 13C is Prompt 13D, subject to its own authorization and predecessor-status requirements.

Do not automatically begin it.

---

# 25. FINAL ACCEPTANCE CRITERIA FOR PROMPT 13C

Prompt 13C may be reported COMPLETE only when all applicable criteria have been satisfied.

| ID | Acceptance criterion |
|---|---|
| 13C-AC-01 | All mandatory predecessor documents were inspected. |
| 13C-AC-02 | Mandatory governance policy was followed. |
| 13C-AC-03 | Complete player journey specifications exist. |
| 13C-AC-04 | Major existing game-system journeys are covered. |
| 13C-AC-05 | Detailed interaction sequences exist. |
| 13C-AC-06 | Alternative and failure paths are documented. |
| 13C-AC-07 | Loading states are specified. |
| 13C-AC-08 | Empty states are specified. |
| 13C-AC-09 | Success states are specified. |
| 13C-AC-10 | Failure states are specified. |
| 13C-AC-11 | Validation rules are documented. |
| 13C-AC-12 | Error handling and recovery are documented. |
| 13C-AC-13 | Confirmation and duplicate-submission behaviour are documented. |
| 13C-AC-14 | Accessibility interaction specifications exist. |
| 13C-AC-15 | Onboarding and tutorial specifications exist. |
| 13C-AC-16 | Notification and feedback specifications exist. |
| 13C-AC-17 | Offline and reconnection experiences are specified. |
| 13C-AC-18 | Cross-screen behavioural consistency is documented. |
| 13C-AC-19 | Existing game mechanics and restrictions are preserved. |
| 13C-AC-20 | Conditional feature restrictions are preserved. |
| 13C-AC-21 | Requirements and decisions have complete traceability. |
| 13C-AC-22 | Documentation impact assessment is complete. |
| 13C-AC-23 | Dedicated validator and self-tests have actual results. |
| 13C-AC-24 | Relevant documentation links and references are verified. |
| 13C-AC-25 | Project handoff and roadmap are updated accurately. |
| 13C-AC-26 | No unauthorized implementation or later-phase work occurred. |

For each criterion, report:

- PASS.
- PARTIAL.
- BLOCKED.
- NOT APPLICABLE.

Provide evidence for every result.

Do not report full completion when mandatory acceptance criteria remain incomplete.

Where a genuine external dependency prevents completion, classify it precisely and continue all independent work.

---

# 26. FINAL EXECUTION INSTRUCTIONS

Execute Prompt 13C systematically.

Follow this order:

**Phase 1 — Repository inspection**
- Read mandatory governance documents.
- Inspect the complete Prompt 13A and Prompt 13B specifications.
- Verify existing decisions and requirements.
- Identify the next available identifiers.

**Phase 2 — Interaction architecture**
- Establish global interaction conventions.
- Define the state model.
- Establish journey and flow templates.
- Establish traceability conventions.

**Phase 3 — Player journeys**
- Document all mandatory journeys.
- Define primary and alternative paths.
- Specify cross-system transitions.

**Phase 4 — Interaction states**
- Define loading, empty, success, failure and recovery states.
- Map applicable states to existing components.

**Phase 5 — Validation and accessibility**
- Specify input and action validation.
- Define error handling.
- Complete accessibility interaction specifications.

**Phase 6 — Player experience**
- Complete onboarding and tutorials.
- Define notifications and feedback.
- Define offline and recovery experiences.

**Phase 7 — Consistency and traceability**
- Build all required matrices.
- Reconcile screen and component references.
- Record decisions and requirements.
- Complete documentation impact assessment.

**Phase 8 — Validation and handoff**
- Run dedicated validators.
- Run self-tests.
- Review scope compliance.
- Update project records.
- Produce the final completion report.

Do not stop merely because a document has been created.

Complete the actual specification work and verify it.

Do not create unnecessary correction cycles. Resolve genuine defects within the current assignment whenever possible.

Do not rewrite already accepted specifications without a demonstrable contradiction.

Do not make implementation claims.

Do not begin Prompt 13D.

**FINAL OBJECTIVE: Deliver a complete, coherent, traceable and implementation-ready interaction and player-experience blueprint that connects every relevant Nation Supremacy screen and existing game system into one understandable, accessible and consistent player experience.**
