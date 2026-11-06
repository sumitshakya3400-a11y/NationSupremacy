# 09A — Alliance Integration Semantic Review Record

**Document ID:** 09A-ALLIANCE-REFERENCE-REVIEW
**Version:** 1.1 (2026-10-31) — corrected by Prompt 09A-D
**Scope:** Human-readable review record for every `AX-01`…`AX-26` requirement reference in `09A_alliance_integration_matrix.md`.
**Status:** Self-review by the project author. **It is not an independent review.**

---

## 1. Why this record exists

The Prompt 09A validators proved that a cited `REQ-` identifier existed; they could not prove that the requirement's rule supported the integration. The 09A audit found eleven such semantic mismatches. This record makes the human judgement explicit, so a later reader can see what was reviewed, what conclusion was reached, and what remains an owner decision.

**Validation honesty.** No script independently proves meaning. An automated check does not prove that a cited requirement supports an integration; it only proves that the identifier exists, the row is classified and an evidence sentence is present. The automated checks in `qa_backups/09A_validate_alliance.py` prove structure, identifier existence, classification vocabulary, required evidence fields, forbidden stale pairs, source-URL shape and handoff agreement. The conclusions below are a document review against the canonical requirement statements.

---

## 2. Method

1. Each `AX` record was read from matrix v1.0 together with its stated capability and owning system.
2. Each cited `REQ-` row was read in `03_requirements_traceability.md`: title, full statement, status, source, Bible section and owning prompt.
3. The requirement was classified as **DIRECT DEPENDENCY**, **RELATED CONSTRAINT**, **SUPPORTING CONTEXT** or **NO VALID RELATIONSHIP**.
4. A replacement was proposed only when another existing requirement's actual rule supported the integration; otherwise the record states **NO EXISTING REQUIREMENT**.
5. Ambiguous cases were resolved conservatively against the owning subsystem. Where a plausible new rule was needed, it stayed a candidate (`REQ-###`) and an open decision (`UD-###`).
6. The result was written into matrix §3 with an evidence sentence for every direct dependency and related constraint.

**Out of scope:** approving a candidate requirement, resolving `UD-039`, changing a decision, or editing an owning subsystem's rule.

---

## 3. Per-AX review conclusions

| AX | Integration | Requirements reviewed | Classification result | Review conclusion | Owner decision |
|---|---|---|---|---|---|
| AX-01 | Founding eligibility | REQ-002, REQ-061, REQ-076, REQ-176, REQ-012 | REQ-002 DIRECT; REQ-061 DIRECT; REQ-076 RELATED; REQ-176 and REQ-012 removed | Ownership is supported; founding eligibility is **not** an existing rule. `REQ-535` is only a candidate. | `UD-040` |
| AX-02 | Identity and role limits | REQ-061, REQ-043, REQ-004, REQ-031, REQ-176 | REQ-061/043/004 DIRECT; REQ-031 RELATED; REQ-176 removed | The identity basis is direct. `REQ-176` is a pool rule and does not establish identity limits. | `UD-045` |
| AX-03 | Dormant leadership | REQ-091, REQ-085, REQ-013, REQ-012 | REQ-091/085 DIRECT; REQ-013 RELATED; REQ-012 removed | Dormancy and reroll events are direct; no requirement defines the vacancy path. | `UD-043` |
| AX-04 | Leadership succession | REQ-013, REQ-085, REQ-091, REQ-012 | REQ-013/085 DIRECT; REQ-091 RELATED; REQ-012 removed | `REQ-013` is the only direct succession obligation and is Open. No existing rule supplies the procedure. | `UD-012`, `UD-043` |
| AX-05 | Permission changes | REQ-013, REQ-004, REQ-027 | All DIRECT | Explicit roles, server-side role resolution and the privileged-act audit spine are all genuine dependencies. | `UD-045` |
| AX-06 | Treasury deposits | REQ-176, REQ-005, REQ-154, REQ-170, REQ-530 | REQ-176/005/154/170 DIRECT; REQ-530 removed | The pool, conservation, ledger and pair-check rules are direct. Diplomatic authority is not a deposit rule. | `UD-046` |
| AX-07 | Treasury withdrawals | REQ-013, REQ-176, REQ-005, REQ-153, REQ-170 | All DIRECT | Audited pool draws, no minting, conservation, append-only ledger and pair checks are direct. | `UD-046` |
| AX-08 | Storage limits | REQ-141, REQ-142, REQ-176, REQ-530 | REQ-176 DIRECT; REQ-141/142 RELATED; REQ-530 removed; NO EXISTING REQUIREMENT for pool capacity | National warehouse rules (REQ-141/142) govern national inventory, not alliance treasury; REQ-176 establishes separate audited pools; pool capacity and deposit overflow remain an open owner decision under UD-046. | `UD-046` |
| AX-09 | Applications | REQ-002, REQ-012, REQ-057 | REQ-002 SUPPORTING; REQ-012 removed; no membership requirement exists | The application lifecycle is entirely new. `REQ-012` and `REQ-057` do not establish it; `REQ-057` belongs to AX-10. | `UD-044` |
| AX-10 | Profile visibility | REQ-057 | DIRECT | The integration is exactly a mapping onto the canonical visibility classes. | `UD-044` (default only) |
| AX-11 | City support | REQ-172, REQ-218, REQ-005, REQ-530 | REQ-172 DIRECT; REQ-218/005 RELATED; REQ-530 removed | City support must use B-05/B-04 costs and ledger. No existing rule authorises an alliance programme. | `UD-046` |
| AX-12 | Readiness declarations | REQ-091, REQ-023, REQ-085 | REQ-091 SUPPORTING; REQ-023 RELATED; no readiness requirement exists | Dormancy and collection limits constrain the feature; they do not establish it. | `UD-044`/`UD-049` |
| AX-13 | Population/approval effect | none | **NO EXISTING REQUIREMENT** | No effect is approved or proposed. A future effect needs a B-06 change and an owner decision. | If proposed |
| AX-14 | Elections/crisis interaction | REQ-326 | SUPPORTING CONTEXT | B-06 owns the election; `REQ-326` does not define the alliance-office interaction. No rule is created. | If proposed |
| AX-15 | Treaty persistence | REQ-530, REQ-523, REQ-531, `DIP-147` | REQ-530/523 DIRECT; REQ-531 RELATED | National-only authority and owner-only consent are direct. Persistence is `DIP-147`, a canonical rule, not a `REQ`. | — |
| AX-16 | Alliance positions | REQ-530, REQ-523, REQ-531, REQ-532 | REQ-530 DIRECT; REQ-523/531 RELATED; REQ-532 removed | The authority boundary is direct; no existing requirement authorises a position. The TRANSITION/CRISIS freeze is not a position rule. | `UD-039`, `UD-047` |
| AX-17 | Embargo checks | REQ-529, REQ-175, REQ-170, REQ-532 | REQ-529/175/170 DIRECT; REQ-532 removed | The embargo, transfer and pair rules are direct. The freeze rule is not an embargo rule. | — |
| AX-18 | War coordination | REQ-014, REQ-518 | Both RELATED | No war rule set exists; Prompt 10 owns the interface. Nothing in 09A grants execution authority. | Prompt 10 |
| AX-19 | Discord link | REQ-057 | RELATED | Visibility applies; no existing link requirement. `D-133`/`DD-147` approve exclusion, `DD-148` is provisional. | `UD-048` |
| AX-20 | Announcements | REQ-057, REQ-021 | RELATED/SUPPORTING | Neither establishes announcements. Asynchronous-only scope is a candidate. | `UD-049` |
| AX-21 | Audit/history | REQ-027, REQ-021, REQ-153, REQ-013 | REQ-027/021/153 DIRECT; REQ-013 RELATED | The audit spine, append-only history and ledger are direct; audited draws are related. | — |
| AX-22 | Rankings | REQ-058 | SUPPORTING CONTEXT | Bounded history constrains a future aggregate; no alliance ranking exists. | Prompt 11 |
| AX-23 | Moderation | REQ-025, REQ-026, REQ-027 | All DIRECT | Evidence-based moderation, appeals and the audit spine are direct. | Prompt 12 |
| AX-24 | Notifications/UI | REQ-020 | SUPPORTING CONTEXT | Provenance applies; the taxonomy is Prompt 13's. | Prompt 13 |
| AX-25 | Formula register | REQ-163, REQ-098, REQ-047 | REQ-163 DIRECT; REQ-098/047 RELATED | Any formula must be registered; no alliance formula exists. | Prompt 14 |
| AX-26 | Global Trade | REQ-513, REQ-010 | Both DIRECT | Approved scope and the gate are direct; Alliance must not create a trade channel. | D-122 (scope) |

---

## 4. Summary

| Measure | Count |
|---|---|
| AX records reviewed | 26 |
| Requirement relationships reviewed | 77 |
| Direct dependencies retained | 39 |
| Related constraints retained | 19 |
| Supporting-context references retained | 6 |
| Invalid references removed | 11 |
| AX records with an explicit no-existing-requirement row | 13 |
| AX records with an owner decision or future-prompt gate | 19 |

The counts are recomputed from matrix §3 by `qa_backups/09A_validate_alliance.py`; a manual edit that changes them must update this table too.

**Residual limitation.** This is a single-author semantic review. It reduces the risk of a plausible-looking but unsupported citation; it does not replace a second reviewer. No second reviewer is claimed.

---

## 5. Owner decisions and unresolved items exposed by the review

| Item | Why it remains open | Route |
|---|---|---|
| Founding eligibility, cost and multi-membership | No existing requirement; `REQ-535` is Proposed | `UD-040`, Prompt 09B |
| Default government and office model | No canonical model; P&W practice is alliance-specific | `UD-041`, Prompt 09B |
| Succession and leader removal | `REQ-013` requires a rule but does not supply one | `UD-012`, `UD-043`, Prompt 09B |
| Capability granularity and delegation | Coarse P&W ranks are evidence of a gap, not a model | `UD-045`, Prompt 09B |
| Treasury authorization, pool storage capacity and dual approval | Economy owns value; Alliance owns authorization; national warehouse rules do not establish alliance pool limits | `UD-046`, Prompt 09B |
| Alliance diplomatic positions and treaty reuse | B-08 refuses delegation; no alliance object exists | `UD-039`, `UD-047`, Prompt 09B |
| Discord link visibility and host allowlist | `DD-148` is Provisional | `UD-048`, Prompt 09B |
| Announcements and native votes | Scope decision, not a design detail | `UD-049`, Prompt 09B |
| Any population/approval effect | No evidence and no B-06 change | Owner decision, not scheduled |
| Any military coordination interface | Prompt 10 owns military rules | Prompt 10 |

**No decision status was changed by this review.** `D-133`, `DD-147`–`DD-150`, `UD-039` and `UD-040`–`UD-049` keep their recorded statuses.
