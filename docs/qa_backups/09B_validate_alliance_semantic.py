#!/usr/bin/env python3
"""
09B_validate_alliance_semantic.py - semantic validator for the Prompt 09B-J
Alliance correction, completed by Prompt 09B-L.

The validator checks meaning and authority, not keyword presence. It is built
around four questions:

  1. Does the rulebook still contain the full, identified rule and contract set?
  2. Is every cross-reference real, and does every status agree across registers?
  3. Is any owner-reserved decision presented as approved, enforced or settled?
  4. Did any owner-approved boundary regress (diplomatic sovereignty, open-ended
     constitutions, trade gates, the Discord and chat scope, non-minting)?

It deliberately does NOT require any particular numeric threshold. A clean
project with UD-046 still owner-reserved passes when every threshold value is
removed, because no value is approved content.

Usage:
    python docs/qa_backups/09B_validate_alliance_semantic.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

STATUS_SENTENCE = (
    "Phase 09B Alliance specification and documentation: ACCEPTED."
)
STALE_STATUS_SENTENCE = (
    "Prompt 09B: correction completed by the writing agent; "
    "independent acceptance review pending. Prompt 09C: blocked pending acceptance."
)

EXPECTED_AX = {
    "AX-01": "Alliance Founding Requires an Eligible Nation Owner",
    "AX-02": "One-Player-One-Nation and Multi-Identity Limits Apply to Alliance Roles",
    "AX-03": "Dormant or Retired Founder/Leader Does Not Freeze Alliance",
    "AX-04": "Leadership, Succession and Office Vacancy",
    "AX-05": "Permission Changes and Role Grants",
    "AX-06": "Treasury Deposits of Already-Owned Resources",
    "AX-07": "Treasury Withdrawals, Grants and Loans",
    "AX-08": "Alliance Resource Storage Limits",
    "AX-09": "Applications, Acceptance, Rejection and Withdrawal",
    "AX-10": "Field-Level Visibility of Profile and Applicant Data",
    "AX-11": "City/Development Support Programmes",
    "AX-12": "Readiness/Activity Declarations for Members",
    "AX-13": "Population/Approval Effects of Alliance Membership",
    "AX-14": "Elections/Crisis Interaction with Alliance Offices",
    "AX-15": "National Treaties Persist Through Alliance Join/Leave/Removal",
    "AX-16": "Alliance Diplomatic Positions (Non-Binding)",
    "AX-17": "Embargo and Restricted-Pair Checks on Alliance Transfers",
    "AX-18": "War/Coordination Information",
    "AX-19": "Static Discord Invite Link",
    "AX-20": "Announcements and Formal Notices",
    "AX-21": "Audit and History of Alliance Actions",
    "AX-22": "Rankings/Chronicle Aggregates",
    "AX-23": "Fair-Play/Moderation of Alliance Conduct",
    "AX-24": "Notifications and UI Surfaces",
    "AX-25": "Formula and Balance Registration",
    "AX-26": "Global Trade Interaction",
    "AX-27": "Automatic Per-Turn Member Taxation",
    "AX-28": "Voluntary Donations and Receipts",
    "AX-29": "Alliance-to-Alliance Treaties and NAP Consent",
    "AX-30": "Same-Alliance and Alliance-NAP Attack Validation",
}

EXPECTED_FIELDS = [
    "AX ID",
    "Integration Title",
    "Alliance Capability",
    "Owning Subsystem",
    "Canonical External Rule",
    "Alliance Internal Rule",
    "Relevant REQ IDs",
    "Related Decision IDs",
    "Related Formula IDs",
    "Inputs Received",
    "Outputs Provided",
    "State Ownership",
    "Authorized Actors",
    "Permission Requirement",
    "National Player Consent",
    "Resource Impact",
    "Security Boundary",
    "Failure Behaviour",
    "Recovery Responsibility",
    "Unresolved Decision",
    "Status",
]

# Status authority expected for each contract. "candidate/Open" contracts must
# name the owning owner-reserved decision; only AX-26 may claim an approval.
AX_STATUS_RULES = {
    "AX-01": (["Open under UD-040", "Candidate"], []),
    "AX-02": (["Open under UD-045", "Candidate"], []),
    "AX-03": (["Open under UD-043", "Candidate"], []),
    "AX-04": (["UD-012", "Open under UD-043", "Candidate"], []),
    "AX-05": (["Open under UD-045", "Candidate"], []),
    "AX-06": (["Open under UD-046", "Candidate"], []),
    "AX-07": (["Open under UD-046", "Candidate"], []),
    "AX-08": (["Open under UD-046", "Candidate"], []),
    "AX-09": (["Open under UD-044", "Candidate"], []),
    "AX-10": (["Binding Inherited", "REQ-057"], []),
    "AX-11": (["Open under UD-046", "Candidate"], []),
    "AX-12": (["Candidate"], ["UD-049"]),
    "AX-13": (["Deferred"], []),
    "AX-14": (["Deferred"], []),
    "AX-15": (["Binding Inherited", "D-137"], []),
    "AX-16": (["Open under UD-047", "no delegation"], []),
    "AX-17": (["Binding Inherited", "REQ-529"], []),
    "AX-18": (["Deferred to Prompt 10"], []),
    "AX-19": (["Provisional", "Open under UD-048"], []),
    "AX-20": (["Open under UD-049", "Candidate"], []),
    "AX-21": (["Binding Inherited", "D-026"], []),
    "AX-22": (["Deferred to Prompt 11"], []),
    "AX-23": (["Deferred to Prompt 12"], []),
    "AX-24": (["Deferred to Prompt 13"], []),
    "AX-25": (["Candidate"], ["Prompt 14"]),
    "AX-26": (["Approved Mandatory Constraint", "D-122", "DD-136", "REQ-513"], []),
    "AX-27": (["Binding Owner-Authorized Constraint", "D-140", "D-141", "UD-046"], []),
    "AX-28": (["Binding Owner-Authorized Constraint", "D-140", "UD-046"], []),
    "AX-29": (["Binding Owner-Authorized Constraint", "D-140", "UD-047"], []),
    "AX-30": (["Binding Design Contract", "D-140", "Prompt 10"], []),
}

ALLIANCE_OPEN_SET = {
    "REQ-548",
    "REQ-549",
    "REQ-556",
    "REQ-573",
    "REQ-574",
    "REQ-575",
    "REQ-579",
    "REQ-580",
    "REQ-586",
    "REQ-598",
    "REQ-599",
    "REQ-600",
}

CONTINUITY_FILES = [
    "AI_CONTEXT.md",
    "AI_HANDOFF.md",
    "PROJECT_PROGRESS.md",
    "ROADMAP.md",
    "stage-2/00_stage_2_handoff.md",
    "stage-2/01_stage_2_prompt_roadmap.md",
    "stage-2/02_master_game_design_bible_outline.md",
    "stage-2/06_stage_2_progress_log.md",
    "stage-2/16_alliances.md",
    "stage-2/16_alliances_integration_contracts.md",
    "stage-2/16_alliances_formula_register.md",
]

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+|(?<=;)\s+|\n+")
NEGATION = re.compile(
    r"\b(?:no|not|never|none|nobody|neither|nor|cannot|can't|doesn't|don't|"
    r"without|refuses?|refused|prohibits?|prohibited|forbids?|forbidden|"
    r"excludes?|excluded|zero|nothing|unapproved|unsanctioned)\b",
    re.I,
)
CONDITIONAL = re.compile(
    r"\b(?:if|unless|whether|would|could|might|ever|eventually|candidate|"
    r"proposal|proposed|awaiting|pending|may\s+approve|may\s+decide)\b",
    re.I,
)
# A disclaimer in one clause must not immunise a mandate in another. Split
# contrastive and coordinated compounds before evaluating authority.
CLAUSE_SPLIT = re.compile(
    r"\b(?:but|however|yet|nevertheless|nonetheless|whereas|although|though|and)\b",
    re.I,
)
# Exception, unless and save clauses can grant an entitlement that the main
# clause appears to disclaim. They are separate policy assertions and must be
# evaluated on their own as well as inside the complete clause.
EXCEPTION_SPLIT = re.compile(
    r"\b(?:except(?:\s+that|\s+for|\s+when|\s+where|\s+if)?|unless|"
    r"save\s+that|other\s+than)\b",
    re.I,
)


def clauses(text: str) -> list[str]:
    return [
        part.strip(" ,;:")
        for part in CLAUSE_SPLIT.split(text)
        if part.strip(" ,;:")
    ]


def policy_segments(clause: str) -> list[str]:
    """Return the complete clause plus each exception/unless policy branch."""
    parts = [clause]
    pieces = [
        part.strip(" ,;:")
        for part in EXCEPTION_SPLIT.split(clause)
        if part.strip(" ,;:")
    ]
    if len(pieces) > 1:
        parts.extend(pieces)
    return parts


RULE_ID = re.compile(
    r"\b(?:ALL|AX|F-AL|REQ|DD|D|TR|ACC|ONB|DIP|DMP|ECN|URB|MKT)-\d{2,3}\b",
    re.I,
)


def nearest_id(document: str, clause: str) -> str:
    """Return the rule/requirement id in the clause, else the nearest preceding one."""
    inside = RULE_ID.findall(clause)
    if inside:
        return inside[0]
    idx = document.lower().find(clause.lower())
    if idx < 0:
        return ""
    found = RULE_ID.findall(document[:idx])
    return found[-1] if found else ""


# Negative polarity does not automatically make a policy statement harmless.
# These patterns classify the policy actually asserted, before any negation or
# conditional exemption is applied.
APPEAL_NEUTRAL_PATTERNS = [
    re.compile(r"\bno appeal (?:or dispute resolution )?mechanism\b.{0,60}\b(?:approved|required|enforced|in force)\b"),
    re.compile(r"\bappeal (?:mechanism|procedure)\b.{0,30}\bnot\b.{0,20}\b(?:approved|required|enforced|in force)\b"),
    # A bare "must not create appeal rights" is a neutral holding statement.
    # "Must not create or deny appeal rights" is neutral only when no
    # beneficiary or operative branch follows, as in "until UD-044 receives an
    # owner decision". Any other form falls through to the violation patterns.
    re.compile(r"\bmust not (?:create|introduce)\b.{0,30}\bappeal rights?\b"),
    re.compile(
        r"\bmust not (?:create or deny|deny or create)\b.{0,20}\bappeal rights?\b"
        r"(?=\s*(?:$|[.;,]|until|while|pending|before|absent|without|unless|except))"
    ),
    re.compile(r"\bmust not be interpreted as an appeal entitlement\b"),
    re.compile(r"\bwithout (?:deciding|determining|establishing) appeal rights?\b"),
    re.compile(r"\bdoes not (?:establish|create|determine|decide) (?:an? )?appeal\b"),
    re.compile(r"\bcreate[sd]? no appeal (?:right|mechanism)\b"),
    re.compile(r"\b(?:could|may) be proposed\b.{0,60}\b(?:owner review|owner approval|not currently enforced)\b"),
    re.compile(r"\bnot currently enforced\b"),
    re.compile(r"\bcannot be enforced before owner approval\b"),
    re.compile(r"\bappeals? (?:are|is) generally not required\b"),
    re.compile(r"\bawaiting\b.{0,30}\bowner\b"),
    re.compile(r"\b(?:confers?|creates?|grants?)\s+no\s+appeal\s+(?:right|entitlement)\b"),
    re.compile(r"\bno\s+(?:appeal\s+right|right\s+(?:to|of)\s+appeal|appeal\s+entitlement)\b.{0,30}\b(?:approved|in\s+force|enacted|adopted|resolved)\b"),
    re.compile(r"\bno\s+(?:appeal\s+right|right\s+to\s+appeal)\s+exists?\s+(?:under|while|because|until|pending|absent)\b"),
    # A reservation or undecided question is not a positive grant merely
    # because it names appeals or review. Active grants in a separate branch
    # are still evaluated on their own.
    re.compile(r"\b(?:whether|if)\b.{0,110}\b(?:appeal|review)\b.{0,70}\b(?:owner[- ]reserved|remains?\s+open|open\s+under\s+ud-044|undecided|not\s+approved|not\s+decided)\b"),
    re.compile(r"\b(?:appeal|review)\w*\b.{0,60}\b(?:owner[- ]reserved|remains?\s+open\s+under\s+ud-044|open\s+under\s+ud-044|undecided|not\s+approved|not\s+in\s+force|not\s+decided)\b"),
    # Indicative "does not decide/establish" forms describe a holding record.
    # An operative "must not grant/confer" is a negative policy decision and is
    # left to the violation patterns; only the coordinated create-or-deny form
    # above is neutral.
    re.compile(r"\b(?:does|do)\s+not\s+(?:decide|determine|establish|create|grant|confer|specify|address|change)\b.{0,45}\b(?:appeal|review)\b"),
    re.compile(r"\b(?:does|do)\s+not\s+(?:create|establish|confer|grant)\b.{0,30}\b(?:a\s+|the\s+)?right\b.{0,25}\b(?:redress|remed(?:y|ies))\b"),
    re.compile(r"\b(?:must|shall)\s+not\s+(?:decide|determine|establish|specify|address|change)\b.{0,45}\b(?:appeal|review)\b"),
    re.compile(r"\bwithout\s+(?:deciding|determining|establishing|specifying|addressing)\b.{0,45}\b(?:appeal|review)\b"),
    re.compile(r"\b(?:creates?|establishes?|confers?|grants?)\s+no\s+(?:appeal|review)\s+(?:right|avenue|route|mechanism|procedure|process|entitlement)\b"),
    re.compile(r"\bno\s+(?:appeal|review)\s+(?:right|policy|mechanism|procedure|process|avenue|route|entitlement)\b.{0,60}\b(?:is|are|has|have|remains?)\s+(?:approved|required|been\s+approved|been\s+established|in\s+force|not\s+approved)\b"),
]

# A statement can mention an appeal without deciding the policy: a historical
# note, a rejected or withdrawn proposal, an illustrative example or a test
# fixture. That framing is exempt only when it is not negated and does not
# coexist with an active in-force frame in the same clause.
APPEAL_NON_POLICY_CONTEXT = re.compile(
    r"\b(?:rejected|withdrawn|superseded|repealed|retired|historical(?:ly)?|earlier|"
    r"previous|prior|former|old|draft|proposal|proposed|candidate|example|illustrative|"
    r"illustration|hypothetical|fixture|test fixture|sample|specimen|not adopted|"
    r"never adopted|no longer in force|owner rejected|was rejected|were rejected|"
    r"disclaimer|non[- ]normative|not normative|background|for context only|"
    r"informational(?:ly)?|historical note)\b",
    re.I,
)
APPEAL_ACTIVE_FRAME = re.compile(
    r"\b(?:currently|now|today|in force|is approved|are approved|is adopted|are adopted|"
    r"applies|apply|shall apply|remains? in force|becomes? effective|effective)\b",
    re.I,
)
# A historical or disclaimer label immunises only the clause it frames. An
# operative assertion after a comma or coordinating conjunction is a separate
# policy statement and must still be evaluated.
APPEAL_ACTIVE_ASSERTION = re.compile(
    r"(?:[;,]\s*|\b(?:but|yet|however|nevertheless)\b\s*)"
    r"(?:(?:the\s+)?(?:alliance|alliances|member|members|nation|nations|player|players|"
    r"applicant|applicants|expelled\s+(?:member|nation|player))\b|"
    r"(?:expulsion|removal|appeal|review|reconsideration)\b).{0,100}"
    r"\b(?:may|can|must|shall|is|are|has|have|retains?|preserves?|is\s+entitled\s+to|"
    r"are\s+entitled\s+to|has\s+the\s+right\s+to|have\s+the\s+right\s+to|reviewable|"
    r"appealable|available|provided|granted)\b.{0,60}"
    r"\b(?:appeal|review|reconsideration|reviewable|appealable)\b",
    re.I,
)
APPEAL_CONTEXT_NEGATED = re.compile(
    r"\b(?:not|never|no)\s+(?:just\s+|merely\s+|only\s+)?(?:an?\s+)?"
    r"(?:historical\s+|illustrative\s+|rejected\s+|withdrawn\s+|superseded\s+)?"
    r"(?:proposal|draft|example|illustration|hypothetical|fixture|candidate)\b",
    re.I,
)

APPEAL_VIOLATION_PATTERNS = [
    # A duty on the alliance or platform to provide an appeal is a mandate,
    # not merely a passive entitlement. Label it before the generic grant
    # families claim it, but never treat "must not provide" as a mandate.
    (re.compile(r"\b(?:alliance|platform|constitution|rulebook|charter|tribunal|council)\b.{0,30}\b(?:must|shall)\s+(?!not\b).{0,15}\b(?:provide|afford|offer|establish|create|make available)\b.{0,20}\bappeal\b"), "mandates an alliance appeal"),
    # A right protected by barring deprivation or denial. A bare prohibition
    # on denial asserts that the entitlement exists; it is not neutral. The
    # coordinated "must not create or deny" form is handled by the neutral
    # holding pattern instead.
    (re.compile(r"\b(?:must|shall|may|can)\s+not\s+(?:deny|refuse|withhold|remove|strip)\b.{0,45}\bappeal\b"), "protects an appeal entitlement from denial"),
    (re.compile(r"\bdeny\b.{0,30}\bappeal rights?\s+to\b"), "protects an appeal entitlement from denial"),
    (re.compile(r"\bdeny\b.{0,40}\b(?:an?|the)\s+appeal\b"), "protects an appeal entitlement from denial"),
    (re.compile(r"\b(?:must|shall|may|can)\s+not\s+be\s+(?:deprived|denied)\b.{0,40}\bappeal\b"), "protects an appeal entitlement from deprivation"),
    (re.compile(r"\b(?:cannot|can not)\s+be\s+(?:deprived|denied)\b.{0,40}\bappeal\b"), "protects an appeal entitlement from deprivation"),
    (re.compile(r"\b(?:cannot|can not|may not|must not|shall not)\s+be\s+denied\s+(?:an?|the)\s+appeal\b"), "protects an appeal entitlement from denial"),
    # An appeal made a condition of expulsion.
    (re.compile(r"\b(?:cannot|can not|may not|must not|shall not)\s+be\s+expelled\b.{0,40}\bwithout\b.{0,50}\bappeal\b"), "makes an appeal a condition of expulsion"),
    (re.compile(r"\bexpelled\b.{0,40}\bwithout\b.{0,40}\bappeal\b"), "makes an appeal a condition of expulsion"),
    (re.compile(r"\bno\b.{0,40}\b(?:may|can|shall|must)\s+be\s+expelled\b.{0,40}\bunless\b.{0,50}\bappeal\b"), "makes an appeal a condition of expulsion"),
    (re.compile(r"\bexpulsion\b.{0,30}\b(?:invalid|void|unlawful|not valid)\b.{0,30}\bunless\b.{0,50}\bappeal\b"), "makes an appeal a condition of expulsion"),
    (re.compile(r"\bunless\b.{0,50}\bappeal\b.{0,30}\b(?:is|has been)\s+(?:provided|offered|made available)\b"), "makes an appeal a condition of expulsion"),
    # Denial or prohibition of appeal rights.
    (re.compile(r"\bno\b.{0,40}\b(?:member|nation|player)\b.{0,30}\b(?:may|can|shall|must|is entitled to|has the right to)\b.{0,10}\bappeal\b"), "denies an appeal right"),
    (re.compile(r"\bno\b.{0,40}\b(?:has|have)\b.{0,15}\b(?:a |the )?right to appeal\b"), "denies an appeal right"),
    (re.compile(r"\b(?:is|are)\s+prohibited from appealing\b"), "prohibits appeals"),
    (re.compile(r"\b(?:may not|must not|shall not|cannot|can not)\s+appeal\b"), "prohibits appeals"),
    (re.compile(r"\bmust not be (?:allowed|permitted) to appeal\b"), "prohibits appeals"),
    (re.compile(r"\bappeal\w*\b.{0,25}\b(?:is|are)\s+(?:prohibited|forbidden|barred|unavailable|not permitted)\b"), "prohibits appeals"),
    (re.compile(r"\b(?:waives?|forfeits?)\b.{0,30}\b(?:right to )?appeal\b"), "denies an appeal right"),
    (re.compile(r"\bno\s+(?:right|access|opportunity)\s+(?:of|to)\s+appeal\b"), "denies an appeal right"),
    (re.compile(r"\bno\s+appeal\b.{0,20}\b(?:is|are|shall\s+be|remains?)\s+(?:available|permitted|allowed|provided|possible|open|afforded)\b"), "denies an appeal right"),
    (re.compile(r"\b(?:is|are)\s+not\s+(?:entitled|permitted|allowed)\s+to\s+appeal\b"), "denies an appeal right"),
    (re.compile(r"\b(?:denies|deny|refuses|refuse|withholds|withhold)\b.{0,25}\b(?:an?\s+|the\s+|any\s+)?appeal\b"), "denies an appeal right"),
    (re.compile(r"\b(?:must|shall|may|can)\s+not\s+(?:grant|give|provide|afford|allow|permit|recognise|recognize|confer|create|establish)\b(?!\s+(?:or|and)\s+(?:deny|refuse|withhold))\b.{0,30}\b(?:any\s+)?(?:appeal|appeal\s+(?:right|opportunity|access|procedure|process))\b"), "denies an appeal right"),
    (re.compile(r"\bneither\b.{0,40}\bnor\b.{0,40}\b(?:may|can|shall|must)\s+(?:grant|provide|offer|afford)\b.{0,20}\bappeal\b"), "denies an appeal right"),
    (re.compile(r"\bappeals?\b.{0,30}\b(?:is|are|shall\s+be|must\s+be|remains?)\s+(?:limited|restricted|confined)\s+to\b"), "restricts an appeal entitlement"),
    (re.compile(r"\bonly\b.{0,30}\b(?:may|can|is\s+entitled\s+to|are\s+entitled\s+to)\s+(?:appeal|file|submit|lodge|bring)\b"), "restricts an appeal entitlement"),
    # A positive grant or entitlement. Plain permissive modals ("may appeal",
    # "can appeal") and procedural access ("an appeal may be lodged", "has
    # access to an appeal process") decide that an appeal right exists just as
    # surely as "must" or "shall"; they cannot be left to the bare mandate
    # fallback, which only recognises mandatory wording. The families below
    # cover receive/be given/be afforded, establishment and existence,
    # availability to a beneficiary, and provision by an institution.
    (re.compile(r"\b(?:receives?|gains?|obtains?|gets?|is\s+given|are\s+given|is\s+afforded|are\s+afforded|is\s+granted|are\s+granted|is\s+accorded|are\s+accorded)\b.{0,25}\b(?:an?\s+|the\s+)?(?:appeal|opportunity\s+to\s+appeal|right\s+(?:to|of)\s+appeal|access\s+to\s+(?:an?\s+)?appeal(?:\s+(?:procedure|process|mechanism))?)\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:right\s+(?:to|of)\s+appeal|appeal\s+right|appeal\s+entitlement)\b.{0,40}\b(?:is|are|shall\s+be|must\s+be|remains?)\s+(?:established|created|recognised|recognized|guaranteed|protected|enshrined|secured|conferred|granted|provided|available)\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:an?\s+|the\s+|every\s+|each\s+)?(?:appeal\s+right|appeal\s+entitlement|right\s+(?:to|of)\s+appeal)\b.{0,30}\b(?:exists?|shall\s+exist|must\s+exist|remains?\s+in\s+force|is\s+in\s+force)\b"), "grants an appeal entitlement"),
    (re.compile(r"\bappeals?\b.{0,25}\b(?:are|is|shall\s+be|must\s+be|remains?)\s+(?:available|open)\s+to\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:an?\s+)?(?:appeal\s+opportunity|opportunity\s+to\s+appeal|appeal\s+procedure|appeal\s+process|appeal\s+mechanism|appeal\s+path)\b.{0,30}\b(?:exists?|is\s+(?:available|established|provided|guaranteed|open)|are\s+(?:available|established|provided|guaranteed|open))\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:alliance|platform|constitution|rulebook|charter|tribunal|council|this\s+rule|these\s+rules)\b.{0,30}\b(?:affords?|provides?|offers?|grants?|confers?|guarantees?)\b(?!\s+(?:no|not)\b).{0,25}\bappeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:affords?|provides?|offers?|grants?|gives?|allows?|permits?)\b\s+(?:every\s+|each\s+|an?\s+|the\s+|all\s+)?(?:expelled\s+)?(?:member|members|nation|nations|player|players|applicant|applicants)\b(?:(?!\bno\b).){0,25}\b(?:an?\s+)?appeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:must|shall|may|is|are)\b.{0,30}\b(?:allowed|permitted|entitled)\b.{0,40}\bappeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:members?|nations?|players?|applicants?|every\s+(?:expelled\s+)?(?:member|nation|player)|each\s+(?:expelled\s+)?(?:member|nation|player)|an?\s+(?:expelled\s+)?(?:member|nation|player)|the\s+(?:expelled\s+)?(?:member|nation|player))\b.{0,60}\b(?:may|can|is\s+entitled\s+to|are\s+entitled\s+to|has\s+the\s+right\s+to|have\s+the\s+right\s+to)\b.{0,25}\bappeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:has|have|is|are|must|shall|may)\b.{0,20}\b(?:a |the )?right to appeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:right to appeal|appeal right|appeal opportunity)\b.{0,30}\b(?:must|shall|is|are)\b.{0,20}\b(?:provided|offered|available|guaranteed)\b"), "grants an appeal entitlement"),
    (re.compile(r"\bentitled to appeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\bguarantee[sd]?\b.{0,30}\bappeal\b"), "grants an appeal entitlement"),
    (re.compile(r"\bappeal\w*\b.{0,50}\b(?:may|can|shall|must)\s+be\s+(?:lodged|filed|made|submitted|brought|raised|heard)\b"), "provides an appeal procedure"),
    (re.compile(r"\b(?:has|have|is\s+given|are\s+given|is\s+granted|are\s+granted|has\s+access\s+to|have\s+access\s+to)\b.{0,40}\bappeal\b"), "grants access to an appeal procedure"),
    # A refusal of access or a fixed denial is a policy decision too.
    (re.compile(r"\b(?:denied|refused|withheld)\b.{0,30}\b(?:access\s+to\s+)?(?:an?|the|any)\s+appeal\b"), "denies an appeal right"),
    (re.compile(r"\b(?:deny|denies|refuse|refuses)\b.{0,30}\baccess\b.{0,20}\bappeal\b"), "denies an appeal right"),
    (re.compile(r"\b(?:has|have)\s+no\s+(?:right|access|opportunity)\b.{0,20}\bappeal\b"), "denies an appeal right"),
    # Negative-polarity denials of an appeal avenue or review route. These
    # decide the policy even though they are phrased as an absence.
    (re.compile(r"\bno\s+(?:avenue|route|path|channel|mechanism|procedure|process|opportunity|right|access|entitlement|review)\b.{0,30}\b(?:of|to|for)\s+(?:an?\s+)?(?:appeal|review)\b"), "denies an appeal right"),
    (re.compile(r"\bno\s+(?:avenue|route|path|channel)\s+(?:of|to|for)\s+(?:an?\s+)?appeal\b"), "denies an appeal right"),
    (re.compile(r"\b(?:must|shall|may|can)\s+not\s+(?:allow|permit|recogni[sz]e|accept|entertain|hear)\b.{0,30}\b(?:an?\s+|any\s+)?appeal\b"), "prohibits appeals"),
    (re.compile(r"\b(?:must|shall|may|can)\s+not\s+(?:allow|permit)\b.{0,20}\b(?:expelled\s+)?(?:member|nation|player)s?\b.{0,20}\b(?:to\s+appeal|to\s+(?:request|seek)\s+(?:a\s+)?review)\b"), "prohibits appeals"),
    # Retention, preservation, availability and enablement all assert a live
    # appeal entitlement even without a modal "must" or "shall".
    (re.compile(r"\b(?:retain|retains|retained|preserve|preserves|preserved|maintain|maintains|maintained|keep|keeps|kept|safeguard|safeguards|safeguarded|uphold|upholds|upheld)\b.{0,55}\b(?:ability|right|entitlement|access|opportunity|avenue|route|path|channel|mechanism|procedure|process)\b.{0,40}\b(?:to\s+)?(?:appeal|seek\s+(?:a\s+)?review|request\s+(?:a\s+)?review|submit\s+(?:an?\s+)?appeal|file\s+(?:an?\s+)?appeal|lodge\s+(?:an?\s+)?appeal|bring\s+(?:an?\s+)?appeal)\b"), "preserves an appeal entitlement"),
    (re.compile(r"\b(?:appeal\s+rights?|appeal\s+entitlements?|rights?\s+(?:to|of)\s+appeal)\b.{0,35}\b(?:is|are|shall\s+be|must\s+be|remains?|continues?\s+to\s+be)\s+(?:preserved|retained|maintained|protected|safeguarded|upheld|available|in\s+force)\b"), "preserves an appeal entitlement"),
    (re.compile(r"\b(?:alliance|platform|constitution|rulebook|charter|tribunal|council|this\s+rule|these\s+rules|the\s+rules)\b.{0,40}\b(?:preserves?|retains?|maintains?|protects?|safeguards?|upholds?|provides?|affords?|offers?|establishes?|creates?|makes?\s+available)\b.{0,30}\b(?:an?\s+)?(?:avenue|route|path|channel|mechanism|procedure|process|opportunity|right)\b.{0,25}\b(?:of|to|for)\s+(?:an?\s+)?(?:appeal|review)\b"), "provides an appeal avenue"),
    (re.compile(r"\b(?:alliance|platform|constitution|rulebook|charter|tribunal|council|this\s+rule|these\s+rules|the\s+rules)\b.{0,40}\b(?:preserves?|retains?|maintains?|provides?|affords?|offers?|grants?|guarantees?)\b.{0,20}\baccess\s+to\s+(?:an?\s+)?(?:appeal|review)\b"), "provides an appeal avenue"),
    (re.compile(r"\b(?:is|are|becomes?|remains?)\s+able\s+to\b.{0,30}\b(?:request|seek|submit|file|lodge|pursue|initiate|obtain)\b.{0,25}\b(?:an?\s+)?(?:review|appeal)\b"), "grants an appeal opportunity"),
    (re.compile(r"\b(?:may|can|is\s+entitled\s+to|are\s+entitled\s+to|has\s+the\s+right\s+to|have\s+the\s+right\s+to|is\s+free\s+to|are\s+free\s+to|has\s+recourse\s+to|have\s+recourse\s+to)\b.{0,35}\b(?:seek|request|obtain|pursue|initiate|have\s+recourse\s+to|resort\s+to)\b.{0,30}\b(?:appellate\s+review|review\s+of\s+(?:the\s+)?(?:expulsion|removal|decision)|a\s+review|an?\s+appeal)\b"), "grants an appeal opportunity"),
    (re.compile(r"\b(?:expulsion|removal|disciplinary|sanction)\b.{0,35}\b(?:decisions?|orders?|actions?|measures?)\b.{0,30}\b(?:is|are|shall\s+be|must\s+be|remains?)\s+(?:reviewable|appealable|subject\s+to\s+(?:an?\s+)?appeal|open\s+to\s+challenge)\b"), "makes expulsion reviewable on appeal"),
    (re.compile(r"\b(?:reviewable|appealable)\s+(?:on|by|through|via)\s+(?:an?\s+)?appeal\b"), "makes expulsion reviewable on appeal"),
    (re.compile(r"\b(?:expulsion|removal)\b.{0,30}\b(?:is|are)\s+subject\s+to\s+(?:an?\s+)?appeal\b"), "makes expulsion reviewable on appeal"),
    (re.compile(r"\b(?:every|each|any|an?|the)\s+(?:expelled\s+)?(?:member|nation|player)\b.{0,45}\b(?:has|have|retains?|possesses?|is\s+given|are\s+given)\b.{0,25}\b(?:an?\s+)?(?:appeal\s+(?:avenue|route|right|opportunity|mechanism|procedure|process)|avenue\s+of\s+appeal|right\s+(?:to|of)\s+appeal|access\s+to\s+(?:an?\s+)?appeal|right\s+of\s+review)\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:cannot|can\s+not|may\s+not|must\s+not|shall\s+not)\s+be\s+(?:prevented|barred|restricted|blocked)\s+from\s+(?:appealing|seeking\s+(?:a\s+)?review|requesting\s+(?:a\s+)?review)\b"), "protects an appeal entitlement"),
    (re.compile(r"\b(?:shall|must|may|can)\s+not\s+(?:lack|be\s+without)\b.{0,30}\b(?:an?\s+)?(?:appeal|appeal\s+right|avenue\s+of\s+appeal|review)\b"), "grants an appeal entitlement"),
    (re.compile(r"\bno\b.{0,25}\b(?:expelled\s+)?(?:member|nation|player)\b.{0,25}\b(?:is|are)\s+without\b.{0,25}\b(?:an?\s+)?(?:appeal|avenue\s+of\s+appeal|review)\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:nothing|no\s+provision|no\s+part\s+of\s+this)\b.{0,45}\b(?:prevents?|prohibits?|bars?)\b.{0,35}\b(?:member|nation|player|expelled)\w*\b.{0,35}\b(?:retain|preserv|maintain|exercise|seek|request)\w*\b.{0,25}\b(?:appeal|review)\b"), "grants an appeal entitlement"),
    (re.compile(r"\b(?:alliance|platform|constitution|rulebook|charter|tribunal|council)\b.{0,30}\b(?:must|shall)\s+(?!not\b).{0,15}\b(?:hear|consider|entertain|decide|review)\b.{0,25}\bappeal\b"), "mandates an alliance appeal"),
    # Appellate review, reconsideration, challenge and procedural access.
    # These are policy decisions whether they are phrased as a right, an
    # eligibility, a procedural avenue or a passive reviewability.
    (re.compile(r"\beligible\s+for\s+(?:an?\s+)?appellate\s+review\b"), "grants an appellate review entitlement"),
    (re.compile(r"\b(?:may|can|is\s+entitled\s+to|are\s+entitled\s+to|has\s+the\s+right\s+to|have\s+the\s+right\s+to)\b.{0,30}\bappellate\s+review\b"), "grants an appellate review entitlement"),
    (re.compile(r"\bappellate\s+review\b.{0,35}\b(?:is|are|shall\s+be|must\s+be|remains?)\s+(?:available|open|provided|guaranteed|permitted)\b"), "provides appellate review"),
    # "Have recourse to" is a direct grant, not an uncertain request: the
    # beneficiary can invoke the review avenue itself. The earlier patterns
    # only recognised "have recourse to seek/request review".
    (re.compile(r"\b(?:has|have|had|gains?|gets?|obtains?|is\s+given|are\s+given)\s+recourse\s+to\s+(?:an?\s+|the\s+)?(?:appellate\s+review|review|appeal|reconsideration)\b"), "grants recourse to review"),
    (re.compile(r"\b(?:right|entitlement)\s+(?:of|to)\s+recourse\s+to\s+(?:an?\s+|the\s+)?(?:appellate\s+review|review|appeal|reconsideration)\b"), "grants a right of recourse to review"),
    # An express entitlement to a formal remedy tied to expulsion decides a
    # procedural policy. A bare "may seek redress" without that context is
    # still ambiguous and routes to manual review.
    (re.compile(r"\b(?:right|entitlement)\b.{0,25}\b(?:to|of)\b\s+(?:seek|request|pursue|obtain|apply\s+for)\s+(?:redress|a\s+remedy|remedies)\b.{0,45}\b(?:expulsion|expelled|removal|disciplinary\s+decision|sanction)\b"), "grants a right to seek redress for an expulsion"),
    (re.compile(r"\b(?:right|entitlement|opportunity|avenue|route|path|process|procedure)\b.{0,30}\b(?:of|to|for)\s+reconsideration\b"), "grants a reconsideration entitlement"),
    (re.compile(r"\b(?:may|can|is\s+entitled\s+to|are\s+entitled\s+to|has\s+the\s+right\s+to|have\s+the\s+right\s+to)\b.{0,30}\b(?:request|seek|obtain|pursue)\s+reconsideration\b"), "grants reconsideration"),
    (re.compile(r"\breconsideration\b.{0,30}\b(?:is|are|shall\s+be|must\s+be|remains?)\s+(?:available|open|provided|guaranteed|permitted)\b"), "provides reconsideration"),
    (re.compile(r"\b(?:may|can|is\s+entitled\s+to|are\s+entitled\s+to|has\s+the\s+right\s+to|have\s+the\s+right\s+to)\b.{0,35}\bchallenge\b.{0,35}\b(?:expulsion|removal|disciplinary\s+decision|sanction)\b"), "grants a challenge to expulsion"),
    (re.compile(r"\b(?:expulsion|removal|disciplinary\s+decision|sanction)\b.{0,35}\b(?:may|can|shall|must)\s+be\s+challenged\b"), "makes expulsion challengeable"),
    (re.compile(r"\bchallenge\s+(?:an?\s+)?(?:expulsion|removal)\b.{0,30}\b(?:by|through|via)\s+(?:an?\s+)?(?:review|appeal|reconsideration)\b"), "grants a challenge to expulsion"),
    (re.compile(r"\b(?:procedural\s+(?:right|access|avenue|route|path)|access\s+to\s+(?:an?\s+)?(?:review|appeal)\s+(?:procedure|process|mechanism))\b"), "provides procedural access to review"),
    (re.compile(r"\b(?:opportunity|ability)\b.{0,25}\b(?:to\s+)?(?:seek|request|obtain|pursue|initiate|exercise)\b.{0,25}\b(?:review|appeal|reconsideration)\b"), "grants an opportunity to seek review"),
    (re.compile(r"\b(?:opportunity|ability)\b.{0,12}\b(?:for|of)\s+(?:an?\s+)?(?:review|appeal|reconsideration)\b"), "grants an opportunity for review"),
    (re.compile(r"\b(?:expulsion|removal|disciplinary\s+decision|sanction)\b.{0,35}\b(?:is|are|may\s+be|can\s+be|shall\s+be|must\s+be)\s+(?:reviewed|reconsidered|appealed|challenged)\b"), "makes expulsion reviewable"),
    (re.compile(r"\b(?:review|reconsideration)\b.{0,25}\b(?:is|are|shall\s+be|must\s+be|remains?)\s+(?:available|open|provided|permitted|guaranteed)\b"), "provides review"),
    (re.compile(r"\b(?:only|solely|exclusively)\b.{0,35}\b(?:appeal|review|reconsideration)\b"), "restricts an appeal or review entitlement"),
    (re.compile(r"\b(?:appeal|review|reconsideration)\b.{0,30}\b(?:is|are)\s+(?:limited|restricted|confined)\s+to\b"), "restricts an appeal or review entitlement"),
    (re.compile(r"\b(?:waives?|forfeits?|surrenders?)\b.{0,25}\b(?:right\s+(?:to|of)\s+)?(?:appeal|review|reconsideration)\b"), "denies an appeal or review right"),
    (re.compile(r"\bno\s+(?:right|avenue|route|path|opportunity|ability|access|procedure|process)\b.{0,30}\b(?:to|of|for)\s+(?:review|reconsideration|appeal)\b"), "denies review or reconsideration"),
    (re.compile(r"\b(?:retains?|preserves?|maintains?)\b.{0,30}\b(?:appeal|review|reconsideration)\s+rights?\b"), "preserves appeal or review rights"),
    (re.compile(r"\b(?:retains?|preserves?|maintains?)\b.{0,30}\b(?:review\s+rights?|rights?\s+(?:to|of)\s+review|reconsideration\s+rights?)\b"), "preserves review rights"),
    (re.compile(r"\b(?:has|have|is\s+given|are\s+given|is\s+granted|are\s+granted)\b.{0,30}\b(?:appeal\s+rights?|rights?\s+(?:to|of)\s+appeal|review\s+rights?|rights?\s+(?:to|of)\s+review)\b"), "grants appeal or review rights"),
]

# Uncertain active wording is not a confirmed policy assertion and is not a
# neutral holding either. It must be surfaced for manual review rather than
# silently passing or being promoted to a failure by an over-broad pattern.
APPEAL_REVIEW_PATTERNS = [
    (re.compile(r"\b(?:appeal|review|reconsideration)\b.{0,70}\b(?:under\s+(?:consideration|review|discussion)|being\s+(?:considered|reviewed|discussed|evaluated|assessed)|to\s+be\s+(?:determined|decided|considered|reviewed|evaluated)|will\s+(?:consider|review|evaluate|assess|discuss|determine|decide)|may\s+(?:consider|introduce|create|adopt|establish|propose)|could\s+(?:consider|introduce|create|adopt|establish|propose)|remains?\s+(?:unclear|undetermined|undecided|open\s+for\s+discussion))\b"), "uncertain appeal/review policy wording"),
    (re.compile(r"\b(?:will\s+(?:consider|review|evaluate|assess|discuss|determine|decide)|may\s+(?:consider|introduce|create|adopt|establish|propose)|could\s+(?:consider|introduce|create|adopt|establish|propose)|is\s+considering|are\s+considering)\b.{0,80}\b(?:appeal|review|reconsideration)\b"), "uncertain appeal/review policy wording"),
    (re.compile(r"\b(?:appeal|review|reconsideration)\b.{0,45}\b(?:perhaps|possibly|potentially|maybe|might|could\s+be)\b"), "uncertain appeal/review policy wording"),
    (re.compile(r"\b(?:perhaps|possibly|potentially|maybe|might|could)\b.{0,70}\b(?:appeal|review|reconsideration)\b"), "uncertain appeal/review policy wording"),
    (re.compile(r"\beligible\s+for\s+(?:an?\s+)?review\b"), "uncertain review eligibility wording"),
    # "Redress" and "remedy" plausibly describe an appeal-type entitlement,
    # but the words also cover unrelated complaint or compensation policies.
    # A confident failure would over-claim, so these route to manual review.
    (re.compile(r"\b(?:is|are|was|were|becomes?|remains?)\s+(?:entitled|eligible)\s+to\s+(?:seek|request|pursue|obtain|apply\s+for)\s+(?:redress|a\s+remedy|remedies)\b"), "uncertain redress entitlement"),
    (re.compile(r"\b(?:may|can|might|could)\s+(?:seek|request|pursue|obtain|apply\s+for)\s+(?:redress|a\s+remedy|remedies)\b"), "uncertain redress entitlement"),
    (re.compile(r"\b(?:right|entitlement|opportunity|avenue|route|access|recourse)\b.{0,30}\b(?:to|of|for)\s+(?:redress|a\s+remedy|remedies)\b"), "uncertain redress entitlement"),
    (re.compile(r"\b(?:has|have|retains?|preserves?|maintains?)\s+(?:a\s+|the\s+)?(?:right\s+(?:to|of)\s+)?(?:redress|remedy|remedies)\b"), "uncertain redress wording"),
]

SUCCESSION_ENTITLEMENT_PATTERNS = [
    (re.compile(r"\b(?:cannot|can not|may not|must not|shall not)\s+be\s+denied\s+(?:succession|the office|leadership|stewardship)\b"), "protects a succession entitlement"),
    (re.compile(r"\b(?:cannot|can not|may not|must not|shall not)\b.{0,20}\bdenied\b.{0,20}\b(?:succession|the office|leadership|stewardship)\b"), "protects a succession entitlement"),
    (re.compile(r"\bno\b.{0,30}\b(?:claimant|successor)\b.{0,30}\b(?:may|can|shall|must)\b.{0,20}\b(?:prevail|win|take office|become (?:the )?(?:successor|leader|steward))\b"), "protects a succession entitlement"),
]

SUCCESSION_ORDER_ENTITLEMENT_PATTERNS = [
    (re.compile(r"\b(?:cannot|can not|may not|must not|shall not)\s+be\s+(?:bypassed|displaced|overlooked|replaced|removed)\b"), "protects a claimant from displacement"),
    (re.compile(r"\bno\b.{0,30}\b(?:claimant|successor|leader|steward)\b.{0,30}\b(?:may|can|shall|must)\s+be\s+(?:displaced|bypassed|removed|denied)\b"), "protects a claimant from displacement"),
    (re.compile(r"\b(?:cannot|can not|may not|must not|shall not)\s+be\s+denied\s+(?:the\s+)?(?:office|succession)\b"), "protects a succession entitlement"),
]


def first_policy_match(patterns, text: str) -> str:
    for pattern, reason in patterns:
        if pattern.search(text):
            return reason
    return ""


def read_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_SPLIT.split(text) if part.strip()]


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def get_row(text: str, first_cell: str) -> list[str] | None:
    wanted = first_cell.strip("*` ")
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = split_row(line)
        if cells and cells[0].strip("*` ").strip() == wanted:
            return cells
    return None


def get_rule(text: str, rule_id: str) -> str:
    match = re.search(
        rf"\*\*`{rule_id}`.*?(?=\n\s*-\s+\*\*`ALL-\d{{3}}`|\n## |\Z)",
        text,
        re.S,
    )
    return match.group(0) if match else ""


def get_ax_sections(text: str) -> dict[str, tuple[str, str]]:
    headings = list(
        re.finditer(r"^### (AX-\d{2})\s+[—–-]\s+(.+)$", text, re.M)
    )
    sections: dict[str, tuple[str, str]] = {}
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        sections[match.group(1)] = (match.group(2).strip(), text[match.end() : end])
    return sections


def field_value(body: str, field: str) -> str:
    match = re.search(
        rf"^\|\s*\*\*{re.escape(field)}\*\*\s*\|\s*(.*?)\s*\|$", body, re.M
    )
    return match.group(1).strip() if match else ""


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def plain(text: str) -> str:
    return text.replace("**", "").replace("`", "").replace("*", "")


def title_tokens(title: str) -> set[str]:
    stop = {"a", "an", "the", "and", "or", "of", "on", "for", "to", "with", "does", "not"}
    return {token for token in norm(title).split() if token not in stop}


def status_word(cell: str) -> str:
    clean = cell.replace("*", "").strip()
    match = re.match(r"([A-Za-z]+)", clean)
    return match.group(1) if match else ""


def status_phrase(cell: str) -> str:
    return cell.replace("*", "").strip()


def overclaim_hits(
    documents: list[tuple[str, str]],
    subject: str,
    approval: str,
    label: str,
) -> list[str]:
    hits: list[str] = []
    subject_re = re.compile(subject, re.I)
    approval_re = re.compile(approval, re.I)
    for doc_name, text in documents:
        for sentence in sentences(text):
            if not subject_re.search(sentence):
                continue
            if not approval_re.search(sentence):
                continue
            if NEGATION.search(sentence) or CONDITIONAL.search(sentence):
                continue
            hits.append(f"[C14] {label} presented as settled in {doc_name}: {sentence[:180]}")
    return hits


def run_checks(base_dir: Path | None = None, reviews: list[str] | None = None) -> list[str]:
    review_findings = reviews if reviews is not None else []
    if base_dir is None:
        base_dir = Path(__file__).resolve().parent.parent.parent

    docs = base_dir / "docs"
    stage2 = docs / "stage-2"
    qa = docs / "qa_backups"

    paths = {
        "b09": stage2 / "16_alliances.md",
        "contracts": stage2 / "16_alliances_integration_contracts.md",
        "formulas": stage2 / "16_alliances_formula_register.md",
        "trace": stage2 / "03_requirements_traceability.md",
        "dd": stage2 / "04_approved_and_provisional_decisions.md",
        "ud": stage2 / "05_unresolved_design_decisions.md",
        "log": stage2 / "06_stage_2_progress_log.md",
        "b02": stage2 / "07_core_gameplay_loop_symbolic_world_and_turn_system.md",
        "b03": stage2 / "09_account_onboarding_nation_creation_and_progression.md",
        "b04": stage2 / "10_economy_resources_treasury_and_finances.md",
        "b05": stage2 / "11_cities_infrastructure_production_and_research.md",
        "b06": stage2 / "12_population_and_domestic_politics.md",
        "b07": stage2 / "13_trade_and_markets.md",
        "b08": stage2 / "15_diplomacy.md",
        "b08_workflows": stage2 / "15_diplomacy_workflows_acceptance.md",
        "decisions": docs / "DECISIONS.md",
        "ai_context": docs / "AI_CONTEXT.md",
        "ai_handoff": docs / "AI_HANDOFF.md",
        "progress": docs / "PROJECT_PROGRESS.md",
        "s2_handoff": stage2 / "00_stage_2_handoff.md",
        "roadmap": stage2 / "01_stage_2_prompt_roadmap.md",
        "outline": stage2 / "02_master_game_design_bible_outline.md",
        "top_roadmap": docs / "ROADMAP.md",
        "autonomy": docs / "AUTONOMOUS_DECISION_POLICY.md",
    }
    text = {name: read_file(path) for name, path in paths.items()}

    b09 = text["b09"]
    contracts = text["contracts"]
    formulas = text["formulas"]
    trace = text["trace"]
    dd = text["dd"]
    ud = text["ud"]
    log = text["log"]
    decisions = text["decisions"]

    failures: list[str] = []

    # ------------------------------------------------------------------
    # C01 - Rulebook completeness and mandated status
    # ------------------------------------------------------------------
    section_count = len(re.findall(r"^## \d+\.", b09, re.M))
    if section_count != 29:
        failures.append(f"[C01] B-09 has {section_count} numbered sections, expected 29")
    rule_ids = re.findall(r"^\s*-\s+\*\*`(ALL-\d{3})`", b09, re.M)
    expected_rules = [f"ALL-{i:03d}" for i in range(1, 227)]
    if rule_ids != expected_rules:
        missing = sorted(set(expected_rules) - set(rule_ids))
        duplicated = sorted({rid for rid in rule_ids if rule_ids.count(rid) > 1})
        failures.append(
            f"[C01] B-09 rule set is not exactly ALL-001..ALL-226 "
            f"({len(rule_ids)} definitions; missing={missing[:5]}; duplicated={duplicated[:5]})"
        )
    header = "\n".join(b09.splitlines()[:12])
    if "**Version:** 2.8" not in header or "Prompt 09B-M" not in header:
        failures.append("[C01] B-09 header is not v2.8 / Prompt 09B-M")
    if STATUS_SENTENCE not in b09:
        failures.append("[C01] B-09 does not carry the exact mandated 09B/09C status sentence")
    if STATUS_SENTENCE not in get_rule(b09, "ALL-178"):
        failures.append("[C01] ALL-178 does not carry the exact mandated 09B/09C status sentence")
    if not get_rule(b09, "ALL-174"):
        failures.append("[C01] ALL-174 (numerical tuning authority) is missing")

    # ------------------------------------------------------------------
    # C02 - AX inventory and 21 non-empty fields
    # ------------------------------------------------------------------
    ax = get_ax_sections(contracts)
    if set(ax) != set(EXPECTED_AX):
        failures.append(
            f"[C02] Contract inventory mismatch: missing={sorted(set(EXPECTED_AX) - set(ax))}, "
            f"unexpected={sorted(set(ax) - set(EXPECTED_AX))}"
        )
    for ax_id, expected_title in EXPECTED_AX.items():
        if ax_id not in ax:
            continue
        title, body = ax[ax_id]
        expected_tokens = title_tokens(expected_title)
        actual_tokens = set(norm(title).split())
        missing_tokens = sorted(expected_tokens - actual_tokens)
        if missing_tokens:
            failures.append(
                f"[C02] {ax_id} title drifted from its canonical 09A identity; "
                f"missing tokens {missing_tokens}"
            )
        empty_fields = [name for name in EXPECTED_FIELDS if not field_value(body, name)]
        if empty_fields:
            failures.append(
                f"[C02] {ax_id} has {len(empty_fields)} missing/empty fields: {empty_fields[:6]}"
            )
        if field_value(body, "AX ID").strip("`") != ax_id:
            failures.append(f"[C02] {ax_id} AX ID field does not match its section")
        field_title = re.sub(r"\s*\([^)]*\)\s*$", "", field_value(body, "Integration Title").strip())
        heading_title = re.sub(r"\s*\([^)]*\)\s*$", "", title.strip())
        if field_title != heading_title:
            failures.append(f"[C02] {ax_id} Integration Title disagrees with its heading")

    # ------------------------------------------------------------------
    # C03 - AX status/authority mapping
    # ------------------------------------------------------------------
    approved_status = []
    for ax_id, (must_have, must_have_body) in AX_STATUS_RULES.items():
        if ax_id not in ax:
            continue
        _, body = ax[ax_id]
        status = field_value(body, "Status")
        for token in must_have:
            if token.lower() not in status.lower():
                failures.append(
                    f"[C03] {ax_id} status missing authority token '{token}': {status[:140]}"
                )
        for token in must_have_body:
            if token.lower() not in body.lower():
                failures.append(f"[C03] {ax_id} body missing authority token '{token}'")
        if re.search(r"\bApproved\b", status):
            approved_status.append(ax_id)
    if approved_status != ["AX-26"]:
        failures.append(
            f"[C03] Approved status may appear only on AX-26; found {approved_status}"
        )
    if status_word(field_value(ax["AX-26"][1], "Status")) != "Approved":
        failures.append("[C03] AX-26 must retain its owner-approved Global Trade status")
    for ax_id in ax:
        status = field_value(ax[ax_id][1], "Status")
        for sentence in sentences(status):
            if re.search(r"\bUD-04\d\b", sentence) and re.search(
                r"\b(?:resolved|approved|decided|closed)\b", sentence, re.I
            ):
                if not NEGATION.search(sentence) and not CONDITIONAL.search(sentence):
                    failures.append(
                        f"[C03] {ax_id} status appears to resolve an owner-reserved UD: {sentence[:140]}"
                    )

    # ------------------------------------------------------------------
    # C04 - AX-08 boundary
    # ------------------------------------------------------------------
    if "AX-08" in ax:
        ax08 = ax["AX-08"][1]
        for token in ["REQ-141", "REQ-142", "REQ-176", "UD-046"]:
            if token not in ax08:
                failures.append(f"[C04] AX-08 lost its required link to {token}")
        if not re.search(r"do not (?:define|establish|govern)", ax08, re.I):
            failures.append("[C04] AX-08 no longer states that warehouse limits do not govern pool capacity")
        if not re.search(r"(?:no|not|neither)[^.\n]{0,80}(?:capacity|storage)[^.\n]{0,60}(?:approved|enforced|in force)", ax08, re.I):
            failures.append("[C04] AX-08 does not state that no capacity rule is approved or in force")
        for sentence in sentences(ax08):
            if re.search(r"\b(?:capacity|storage limit|overflow|ownership)\b", sentence, re.I) and re.search(
                r"\b(?:is|are)\s+(?:approved|enforced|in force|mandatory)\b", sentence, re.I
            ):
                if not NEGATION.search(sentence) and not CONDITIONAL.search(sentence):
                    failures.append(f"[C04] AX-08 presents pool capacity/ownership as settled: {sentence[:160]}")

    # ------------------------------------------------------------------
    # C05 - Deferred / provisional contract scope
    # ------------------------------------------------------------------
    def ax_status(ax_id: str) -> str:
        return field_value(ax[ax_id][1], "Status") if ax_id in ax else ""

    if ax_status("AX-16") and "non-binding" not in ax["AX-16"][1].lower():
        failures.append("[C05] AX-16 lost the non-binding character of collective positions")
    if ax_status("AX-18") and "deferred to prompt 10" not in ax_status("AX-18").lower():
        failures.append("[C05] AX-18 must stay deferred to Prompt 10")
    for sentence in sentences(ax.get("AX-18", ("", ""))[1]):
        if re.search(r"\bapproved\b", sentence, re.I) and not NEGATION.search(sentence):
            failures.append(f"[C05] AX-18 claims an approved coordination/bulletin feature: {sentence[:160]}")
    if ax_status("AX-19"):
        if "provisional" not in ax_status("AX-19").lower() or "ud-048" not in ax_status("AX-19").lower():
            failures.append("[C05] AX-19 must remain a Provisional recommendation under UD-048")
        if "not an approved security baseline" not in ax["AX-19"][1]:
            failures.append("[C05] AX-19 no longer states that DD-148 is not an approved security baseline")
    if ax_status("AX-20"):
        if "ud-049" not in ax_status("AX-20").lower() or "candidate" not in ax_status("AX-20").lower():
            failures.append("[C05] AX-20 bulletins must remain candidate scope under UD-049")
        for sentence in sentences(ax["AX-20"][1]):
            if re.search(r"\bapproved\b\s+(?:announcement|bulletin|notice)", sentence, re.I):
                if not NEGATION.search(sentence):
                    failures.append(f"[C05] AX-20 claims approved announcements: {sentence[:160]}")
    if "AX-26" in ax:
        ax26 = ax["AX-26"][1]
        for token in ["D-122", "DD-136", "REQ-513", "G-1", "G-6"]:
            if token not in ax26:
                failures.append(f"[C05] AX-26 lost its Global Trade anchor {token}")

    # ------------------------------------------------------------------
    # C06 - Deep traceability and reference resolution
    # ------------------------------------------------------------------
    id_universe: dict[str, set[str]] = {}
    id_universe["ALL"] = set(re.findall(r"ALL-\d{3}", b09))
    id_universe["REQ"] = set(re.findall(r"REQ-\d{3}", trace))
    id_universe["D"] = set(re.findall(r"(?<!D)D-\d{3}", decisions))
    id_universe["DD"] = set(re.findall(r"DD-\d{3}", dd))
    id_universe["UD"] = set(re.findall(r"UD-\d{3}", ud))
    id_universe["F-AL"] = set(re.findall(r"F-AL-\d{3}", formulas))
    id_universe["AX"] = {f"AX-{i:02d}" for i in range(1, 31)}
    external_sources = {
        "TR": "b02",
        "ACC": "b03",
        "ECN": "b04",
        "URB": "b05",
        "DMP": "b06",
        "MKT": "b07",
        "DIP": "b08",
    }
    for prefix, source in external_sources.items():
        id_universe[prefix] = set(re.findall(rf"\b{prefix}-\d{{3}}\b", text[source]))

    def check_refs(label: str, content: str) -> None:
        patterns = {
            "ALL": r"ALL-\d{3}",
            "REQ": r"REQ-\d{3}",
            "D": r"(?<!D)D-\d{3}",
            "DD": r"DD-\d{3}",
            "UD": r"UD-\d{3}",
            "F-AL": r"F-AL-\d{3}",
            "AX": r"AX-\d{2}",
            "TR": r"\bTR-\d{3}\b",
            "ACC": r"\bACC-\d{3}\b",
            "ECN": r"\bECN-\d{3}\b",
            "URB": r"\bURB-\d{3}\b",
            "DMP": r"\bDMP-\d{3}\b",
            "MKT": r"\bMKT-\d{3}\b",
            "DIP": r"\bDIP-\d{3}\b",
        }
        for prefix, pattern in patterns.items():
            for ref in set(re.findall(pattern, content)):
                if ref not in id_universe[prefix]:
                    failures.append(f"[C06] {label} references non-existent {prefix} id {ref}")

    if "TRN-" in b09 or "TRN-" in contracts:
        failures.append("[C06] Phantom 'TRN-' rule prefix found; B-02 defines TR-### rules")
    for ax_id, (_, body) in ax.items():
        check_refs(ax_id, body)
        if not field_value(body, "Canonical External Rule"):
            failures.append(f"[C06] {ax_id} has no canonical external rule")
        if not field_value(body, "Relevant REQ IDs"):
            failures.append(f"[C06] {ax_id} has no REQ traceability")
        if not field_value(body, "Owning Subsystem"):
            failures.append(f"[C06] {ax_id} has no owning subsystem")
    check_refs("B-09", b09)
    check_refs("formula register", formulas)
    for req_num in range(534, 618):
        req_id = f"REQ-{req_num:03d}"
        row = get_row(trace, req_id)
        if row is None:
            continue
        row_text = "|".join(row)
        if "B-09" not in row_text:
            failures.append(f"[C06] {req_id} is not mapped to B-09")
        if not re.search(r"ALL-\d{3}|AX-\d{2}", row_text):
            failures.append(f"[C06] {req_id} has no ALL/AX implementation mapping")
        check_refs(req_id, row_text)

    # ------------------------------------------------------------------
    # C07 - Global Trade product scope and release gate
    # ------------------------------------------------------------------
    d122 = get_row(decisions, "D-122")
    dd136 = get_row(dd, "DD-136")
    req513 = get_row(trace, "REQ-513")
    if not d122 or "global trade" not in " ".join(d122).lower():
        failures.append("[C07] D-122 Global Trade product-scope decision is missing")
    if not dd136 or status_word(dd136[2]) != "Approved":
        failures.append("[C07] DD-136 is missing or no longer Approved")
    if not req513 or status_word(req513[3]) != "Approved":
        failures.append("[C07] REQ-513 is missing or no longer Approved")
    for label, content in [("B-09", b09), ("contracts", contracts)]:
        for token in ["D-122", "DD-136", "G-1", "G-6"]:
            if token not in content:
                failures.append(f"[C07] {label} lost Global Trade anchor {token}")
    if "REQ-513" not in contracts:
        failures.append("[C07] AX-26 no longer cites REQ-513")
    for sentence in sentences(b09):
        if re.search(r"global trade", sentence, re.I) and re.search(
            r"\b(?:optional|not required|descoped|removed|cut)\b", sentence, re.I
        ):
            if not NEGATION.search(sentence) and not CONDITIONAL.search(sentence):
                failures.append(f"[C07] Global Trade scope appears weakened: {sentence[:160]}")

    # ------------------------------------------------------------------
    # C08 - UD-039 reconciliation
    # ------------------------------------------------------------------
    ud039 = get_row(ud, "UD-039")
    if not ud039:
        failures.append("[C08] UD-039 row missing from the unresolved-decision register")
    else:
        status = ud039[-1].lower()
        if "resolved by d-137" not in status:
            failures.append(f"[C08] UD-039 is not recorded as resolved by D-137: {ud039[-1][:140]}")
        if not (("no alliance-level treaty object" in status) or ("separate" in status and "does not reuse" in status)):
            failures.append("[C08] UD-039 row lost the no-treaty-object resolution")
        if "zero diplomatic delegation" not in status:
            failures.append("[C08] UD-039 row lost the zero-delegation resolution")
    d137 = get_row(decisions, "D-137")
    if not d137:
        failures.append("[C08] D-137 is missing")
    else:
        joined = " ".join(d137).lower()
        for token in ["ud-039", "no collective", "zero delegation", "sole diplomatic authority"]:
            if token not in joined:
                failures.append(f"[C08] D-137 lost '{token}'")
        if status_word(d137[4]) != "Confirmed":
            failures.append("[C08] D-137 must remain Confirmed")
    dd160 = get_row(dd, "DD-160")
    if not dd160 or "resolved by d-137" not in " ".join(dd160).lower():
        failures.append("[C08] DD-160 does not record UD-039 as resolved by D-137")
    req585 = get_row(trace, "REQ-585")
    if not req585 or "d-137" not in " ".join(req585).lower():
        failures.append("[C08] REQ-585 no longer records the D-137 resolution")
    b09_row = get_row(b09, "UD-039")
    if not b09_row or len(b09_row) < 4 or "resolved" not in b09_row[3].lower():
        failures.append("[C08] B-09 Section 27 no longer marks UD-039 resolved")
    for label, content in [("B-09", b09), ("contracts", contracts), ("D-137", " ".join(d137 or []))]:
        for sentence in sentences(content):
            if sentence.rstrip().endswith("?"):
                continue
            if re.search(r"ud-039", sentence, re.I) and re.search(
                r"\b(?:delegat|representative|proxy)\w*\b", sentence, re.I
            ):
                if not NEGATION.search(sentence):
                    failures.append(f"[C08] {label} appears to authorize delegation via UD-039: {sentence[:160]}")

    # ------------------------------------------------------------------
    # C09 - UD-040..UD-049 owner reservation
    # ------------------------------------------------------------------
    for number in range(40, 50):
        ud_id = f"UD-{number:03d}"
        row = get_row(ud, ud_id)
        if not row:
            failures.append(f"[C09] {ud_id} missing from the unresolved-decision register")
            continue
        if len(row) < 9:
            failures.append(f"[C09] {ud_id} row is malformed")
            continue
        owner_cell = row[6].replace("*", "")
        status_cell = row[8].replace("*", "")
        if "owner" not in owner_cell.lower():
            failures.append(f"[C09] {ud_id} is not marked 'Yes - owner' (found '{owner_cell}')")
        if status_word(status_cell) != "Open":
            failures.append(f"[C09] {ud_id} is falsely marked '{status_cell[:80]}' instead of Open")
        b09_ledger = get_row(b09, ud_id)
        if not b09_ledger:
            failures.append(f"[C09] {ud_id} missing from B-09 Section 27 ledger")
        elif len(b09_ledger) >= 4 and status_word(b09_ledger[3]) != "Open":
            failures.append(
                f"[C09] B-09 Section 27 marks {ud_id} as '{b09_ledger[3]}' instead of Open"
            )
    for line in decisions.splitlines():
        if re.match(r"^\|\s*D-\d{3}\s*\|", line):
            for match in re.finditer(
                r"(?<!\bnot\s)(?<!\bnever\s)(?<!\bcannot\s)\bresolves?\s+(UD-04\d)\b",
                line,
                re.I,
            ):
                failures.append(f"[C09] DECISIONS.md falsely resolves owner decision {match.group(1)}")
    false_resolution_patterns = [
        r"\bUD-04\d\b[^.\n]{0,60}\b(?:is|are|was|were|has been|have been)\s+(?:now\s+)?(?:resolved|approved|decided|closed|adopted)\b",
        r"\b(?:resolved|approved|decided|closed|adopted)\b\s+(?:the\s+)?\*{0,2}UD-04\d\b",
    ]
    for label, content in [("B-09", b09), ("contracts", contracts), ("DD register", dd), ("DECISIONS", decisions)]:
        for sentence in sentences(content):
            if not any(re.search(p, sentence, re.I) for p in false_resolution_patterns):
                continue
            if NEGATION.search(sentence) or CONDITIONAL.search(sentence):
                continue
            failures.append(f"[C09] {label} presents an owner-reserved decision as settled: {sentence[:180]}")
    for number in range(153, 161):
        dd_id = f"DD-{number:03d}"
        row = get_row(dd, dd_id)
        if not row:
            failures.append(f"[C09] historical row {dd_id} was deleted")
            continue
        joined = " ".join(row).lower()
        if "ud-04" not in joined:
            failures.append(f"[C09] {dd_id} does not name its owning owner-reserved decision")
        if number in (153, 157) and not status_phrase(row[2]).lower().startswith("binding inherited"):
            failures.append(f"[C09] {dd_id} must remain Binding inherited")
        if number in (154, 156, 160) and not status_phrase(row[2]).lower().startswith("confirmed"):
            failures.append(f"[C09] {dd_id} must remain Confirmed")
        if number in (158, 159) and not status_phrase(row[2]).lower().startswith(("candidate", "open")):
            failures.append(f"[C09] {dd_id} must remain Candidate/Open")
        if number == 155:
            if not status_phrase(row[2]).lower().startswith("approved") or "open under ud-041" not in joined:
                failures.append("[C09] DD-155 must remain Approved for the open-ended model with UD-041 Open")

    # ------------------------------------------------------------------
    # C10 - Sensitive B-09 rules
    # ------------------------------------------------------------------
    sensitive_requirements = {
        "ALL-011": ["authenticated owner", "does not thereby acquire authority"],
        "ALL-015": ["technical communication endpoint", "not a political office"],
        "ALL-051": ["no mandatory", "technical"],
        "ALL-054": ["UD-043", "candidate"],
        "ALL-100": ["UD-046", "none of these controls is approved", "enforced"],
        "ALL-111": ["UD-046", "no such rule is enforced"],
        "ALL-124": ["UD-047", "unapproved"],
        "ALL-125": ["sole diplomatic authority", "zero diplomatic agency", "silence never constitutes consent"],
        "ALL-166": ["UD-048", "unapproved", "provisional"],
        "ALL-176": ["UD-046", "owner-reserved", "must not be described as settled"],
    }
    for rule_id, tokens in sensitive_requirements.items():
        rule = get_rule(b09, rule_id)
        if not rule:
            failures.append(f"[C10] Sensitive rule {rule_id} is missing")
            continue
        lowered = rule.lower().replace("*", "")
        for token in tokens:
            if token.lower() not in lowered:
                failures.append(f"[C10] {rule_id} lost its authority anchor '{token}'")

    # ------------------------------------------------------------------
    # C11 - Constitutional neutrality: no imposed political model
    # ------------------------------------------------------------------
    hierarchy_patterns = [
        (r"\b(?:imposes?|requires?|mandates?|must\s+have|shall\s+have)\s+(?:a\s+|an\s+)?(?:mandatory\s+)?(?:leader|heir)\s+office\b", "mandatory leader/heir office"),
        (r"\b(?:imposes?|requires?|mandates?)\s+(?:a\s+)?(?:mandatory\s+)?(?:council|office\s+structure|government\s+model|succession\s+model|amendment\s+procedure)\b", "mandatory council/office/government model"),
        (r"\bevery\s+alliance\s+must\s+(?:have|adopt|use|follow)\s+(?:a\s+|an\s+)?(?:leader|heir|council|constitution|office)\b", "alliance must adopt a fixed office/model"),
        (r"\b(?:fixed\s+(?:number\s+of\s+)?(?:political\s+)?rank\s+tiers?|rank\s+tiers\s+1\s*[-\u2013]\s*9|tier\s+10\s+is\s+reserved|rank\s+9\s+and\s+leader\s+only)\b", "fixed rank tiers"),
        (r"\b(?:fixed\s+cap\s+of|maximum\s+of|capped\s+at)\s+20\s+(?:custom\s+)?positions\b", "20-position cap"),
        (r"\b(?:constitution|charter)\s+(?:must|shall)\s+be\s+(?:created|adopted|published|drafted)\s+within\s+\d+\s+turns?\b", "constitution deadline"),
        (r"\bmandatory\s+75\s*%\s+impeachment\b", "mandatory 75% impeachment"),
        (r"\b(?:mandatory\s+80\s*%\s+dissolution|80\s*%\s+member\s+vote\s+to\s+dissolve)\b", "mandatory 80% dissolution"),
    ]
    for label, content in [("B-09", b09), ("contracts", contracts)]:
        for sentence in sentences(content):
            for pattern, description in hierarchy_patterns:
                if re.search(pattern, sentence, re.I) and not NEGATION.search(sentence):
                    failures.append(
                        f"[C11] {label} imposes {description}: {sentence[:180]}"
                    )
    for forbidden in ["ALL-278", "ALL-282"]:
        if forbidden in b09 or forbidden in contracts:
            failures.append(f"[C11] Non-existent/forbidden rule id {forbidden} is cited")
    neutrality_anchors = [
        "open-ended",
        "player-authored",
        "no mandatory",
        "never prescribes",
    ]
    for token in neutrality_anchors:
        if token.lower() not in b09.lower():
            failures.append(f"[C11] B-09 lost its constitutional-neutrality anchor '{token}'")

    # ------------------------------------------------------------------
    # C12 - Diplomatic sovereignty and zero delegation
    # ------------------------------------------------------------------
    for label, content in [
        ("B-09", b09),
        ("contracts", contracts),
        ("formula register", formulas),
        ("DECISIONS", decisions),
        ("DD register", dd),
        ("UD register", ud),
        ("requirements", trace),
    ]:
        if "DELEGATE_DIPLOMACY" in content:
            failures.append(f"[C12] Prohibited DELEGATE_DIPLOMACY capability found in {label}")
    delegation_patterns = [
        r"\b(?:may|can|shall|is\s+permitted\s+to|is\s+allowed\s+to)\s+delegate\b[^.\n]{0,80}\b(?:diplomat|treaty|foreign\s+policy)\b",
        r"\b(?:may|can|shall)\s+be\s+delegated\b[^.\n]{0,60}\b(?:diplomat|treaty)\b",
        r"\bdelegation\s+of\s+(?:diplomatic|treaty)\b[^.\n]{0,40}\b(?:is|are)\s+(?:permitted|allowed|authorized|authorised|valid)\b",
        r"\b(?:alliance\s+leader|alliance\s+office|representative)\b[^.\n]{0,60}\b(?:negotiate|sign|accept|conclude|break)\s+(?:a\s+)?treat(?:y|ies)\b",
    ]
    for label, content in [("B-09", b09), ("contracts", contracts)]:
        for sentence in sentences(content):
            for pattern in delegation_patterns:
                if re.search(pattern, sentence, re.I) and not NEGATION.search(sentence):
                    failures.append(
                        f"[C12] {label} permits diplomatic delegation: {sentence[:180]}"
                    )
    for label, content in [("B-09", b09), ("contracts", contracts)]:
        for sentence in sentences(content):
            if re.search(
                r"\bsilence\s+(?:is\s+)?(?:treated\s+as|constitutes?|equals?|counts\s+as|means?|implies?)\s+(?:consent|approval)\b"
                r"|\bsilence\s+is\s+(?:consent|approval)\b",
                sentence,
                re.I,
            ) and not NEGATION.search(sentence):
                failures.append(f"[C12] {label} treats silence as consent: {sentence[:160]}")
            if re.search(
                r"\bmajorit(?:y|ies)\b[^.\n]{0,80}\b(?:binds?|commits?|overrides?)\b[^.\n]{0,60}\b(?:sovereign|nation|member)\b",
                sentence,
                re.I,
            ) and not NEGATION.search(sentence):
                failures.append(f"[C12] {label} lets a majority bind a sovereign nation: {sentence[:160]}")
    req530 = get_row(trace, "REQ-530")
    if not req530:
        failures.append("[C12] REQ-530 is missing")
    else:
        joined = " ".join(req530).lower()
        for token in ["only diplomatic authority", "no delegation", "administrator may not"]:
            if token not in joined:
                failures.append(f"[C12] REQ-530 lost '{token}'")
    for token in ["sole diplomatic authority", "silence never constitutes consent", "never automatically bind"]:
        if token not in b09.lower():
            failures.append(f"[C12] B-09 lost its sovereignty anchor '{token}'")
    for token in ["zero delegation", "collective", "treaty"]:
        if token not in " ".join(get_row(decisions, "D-137") or []).lower():
            failures.append(f"[C12] D-137 lost '{token}'")
    for token in ["resolved for the alliance scope", "zero diplomatic delegation"]:
        if token not in text["b08"].lower():
            failures.append(f"[C12] B-08 lost its delegation resolution '{token}'")

    # ------------------------------------------------------------------
    # C13 - Discord and chat boundary
    # ------------------------------------------------------------------
    for token in ["ALL-161", "ALL-165", "ALL-167", "D-133", "DD-147", "UD-048"]:
        if token not in b09:
            failures.append(f"[C13] B-09 lost Discord/chat boundary anchor {token}")
    if "discord.gg" not in b09 and "discord.com/invite" not in b09:
        failures.append("[C13] B-09 lost the optional static invite-link boundary")
    for label, content in [("B-09", b09), ("contracts", contracts), ("DECISIONS", decisions)]:
        for sentence in sentences(content):
            if re.search(
                r"\b(?:discord\s+(?:is\s+)?(?:mandatory|required)|requires?\s+(?:a\s+)?discord\s+account|must\s+(?:join|use)\s+discord)\b",
                sentence,
                re.I,
            ) and not NEGATION.search(sentence):
                failures.append(f"[C13] {label} makes Discord mandatory: {sentence[:160]}")
            if re.search(
                r"\b(?:integrates?|implements?|provides?|uses?|requires?)\s+(?:a\s+)?discord\s+(?:api|bot|webhook)\b",
                sentence,
                re.I,
            ) and not NEGATION.search(sentence):
                failures.append(f"[C13] {label} adds Discord integration scope: {sentence[:160]}")
            if re.search(r"\boauth\b", sentence, re.I) and re.search(
                r"\b(?:implements?|provides?|requires?|supports?|enables?|uses?|integrates?)\b",
                sentence,
                re.I,
            ) and re.search(
                r"\b(?:link\w*|sync\w*|login\w*)\b", sentence, re.I
            ) and not NEGATION.search(sentence):
                failures.append(f"[C13] {label} adds Discord OAuth account linking: {sentence[:160]}")
    req617 = get_row(trace, "REQ-617")
    if not req617 or "cannot or will not use discord" not in " ".join(req617).lower():
        failures.append("[C13] REQ-617 (Discord is never required) is missing or weakened")
    req598 = get_row(trace, "REQ-598")
    if not req598 or status_word(req598[3]) != "Open":
        failures.append("[C13] REQ-598 must remain Open under UD-048")

    # ------------------------------------------------------------------
    # C14 - Treasury neutrality
    # ------------------------------------------------------------------
    treasury_docs = [
        ("B-09", b09),
        ("contracts", contracts),
        ("formulas", formulas),
        ("DECISIONS", decisions),
        ("DD register", dd),
    ]
    capacity_hits = overclaim_hits(
        treasury_docs,
        r"\b(?:pool|alliance)\b[^.\n]{0,60}\b(?:capacity|storage\s+limit|ownership)\b",
        r"\b(?:is|are)\s+(?:now\s+|officially\s+)?(?:approved|enforced|in\s+force|mandatory)\b",
        "Alliance pool capacity/ownership",
    )
    threshold_hits = overclaim_hits(
        treasury_docs,
        r"\b(?:dual\s+(?:signature|authorization|approval)|multi-?sig|two-phase\s+withdrawal|threshold)\b",
        r"\b(?:is|are)\s+(?:now\s+|officially\s+)?(?:approved|enforced|in\s+force|mandatory)\b",
        "Treasury threshold/dual approval",
    )
    overflow_hits = overclaim_hits(
        treasury_docs,
        r"\boverflow\b",
        r"\b(?:is|are)\s+(?:now\s+)?(?:rejected|blocked|enforced|approved)\b",
        "Overflow rejection",
    )
    ownership_hits = overclaim_hits(
        treasury_docs,
        r"\b(?:entity|alliance)[- ](?:owned|ownership)\b",
        r"\b(?:approved|enforced|in\s+force)\b",
        "Entity/Alliance ownership",
    )
    failures.extend(capacity_hits + threshold_hits + overflow_hits + ownership_hits)
    for sentence in sentences(formulas):
        if re.search(r"\b(?:50,000|10\s*%)\b", sentence) and re.search(
            r"\b(?:approved|enforced|in force|mandatory)\b", sentence, re.I
        ):
            if not NEGATION.search(sentence) and not CONDITIONAL.search(sentence):
                failures.append(
                    f"[C14] A specific treasury threshold is presented as settled: {sentence[:180]}"
                )
    if "No number in this register is required content" not in formulas:
        failures.append("[C14] Formula register no longer states that no number is required content")
    for token in ["Candidate, not approved", "general withdrawal, general spending", "any threshold"]:
        if token.lower() not in b09.lower():
            failures.append(f"[C14] B-09 UD-046 treatment lost '{token}'")

    # ------------------------------------------------------------------
    # C15 - Formula register
    # ------------------------------------------------------------------
    for index in range(1, 8):
        fid = f"F-AL-{index:03d}"
        match = re.search(rf"###\s+{fid}\b[\s\S]*?(?=\n###|\Z)", formulas)
        if not match:
            failures.append(f"[C15] Formula {fid} is missing")
            continue
        section = match.group(0)
        if "$$" not in section:
            failures.append(f"[C15] {fid} has no display-math block")
        decision = ""
        for line in section.splitlines():
            if line.startswith("| **Decision Status**"):
                decision = line
                break
        if not decision:
            failures.append(f"[C15] {fid} has no Decision Status row")
        else:
            if re.search(r"\bApproved\b", decision):
                failures.append(f"[C15] {fid} is presented as Approved")
            if not re.search(r"Candidate|Provisional|Open", decision, re.I):
                failures.append(f"[C15] {fid} lacks a Candidate/Provisional/Open classification")
        if "UD-04" not in section:
            failures.append(f"[C15] {fid} does not name an owner-reserved decision")
    if "D-028" not in formulas or "168" not in formulas:
        failures.append("[C15] F-AL-003 no longer consumes D-028 dormancy (168 turns)")
    if "churn" not in formulas.lower():
        failures.append("[C15] F-AL-004 lost its anti-churning objective")
    if "multi-sig" not in formulas.lower() and "multi-signature" not in formulas.lower():
        failures.append("[C15] F-AL-005 lost its multi-signature candidate subject")
    if "F-AL-005" in formulas and "not required by any validator or release condition" not in formulas:
        failures.append("[C15] F-AL-005 no longer states that its values are not validator requirements")
    if STATUS_SENTENCE not in formulas:
        failures.append("[C15] Formula register lacks the exact mandated status sentence")

    # ------------------------------------------------------------------
    # C16 - Requirements register
    # ------------------------------------------------------------------
    req_rows = [line for line in trace.splitlines() if re.match(r"\|\s*REQ-\d{3}\s*\|", line)]
    req_ids = [split_row(line)[0] for line in req_rows]
    expected_req_ids = [f"REQ-{i:03d}" for i in range(1, 870)]
    if req_ids != expected_req_ids:
        failures.append(
            f"[C16] Requirement continuity broken: {len(req_ids)} rows, expected 869 contiguous rows"
        )
    status_counts = {"Approved": 0, "Provisional": 0, "Open": 0, "Deferred": 0, "Proposed": 0}
    unknown_status = []
    for row in req_rows:
        cells = split_row(row)
        if len(cells) < 4:
            unknown_status.append(cells[0])
            continue
        word = status_word(cells[3])
        if word in status_counts:
            status_counts[word] += 1
        else:
            unknown_status.append(f"{cells[0]}:{cells[3][:24]}")
    expected_counts = {"Approved": 55, "Provisional": 774, "Open": 39, "Deferred": 1, "Proposed": 0}
    if status_counts != expected_counts:
        failures.append(f"[C16] Requirement status counts {status_counts} != {expected_counts}")
    if unknown_status:
        failures.append(f"[C16] Unrecognized requirement statuses: {unknown_status[:6]}")
    open_rows = {
        split_row(row)[0]
        for row in req_rows
        if status_word(split_row(row)[3]) == "Open"
    }
    if not ALLIANCE_OPEN_SET.issubset(open_rows):
        failures.append(
            f"[C16] Alliance owner-reserved requirements no longer Open: {sorted(ALLIANCE_OPEN_SET - open_rows)}"
        )
    alliance_rows = [row for row in req_rows if 534 <= int(split_row(row)[0].split("-")[1]) <= 653]
    if len(alliance_rows) != 120:
        failures.append(f"[C16] Expected 120 Alliance requirements, found {len(alliance_rows)}")
    alliance_counts = {"Approved": 0, "Provisional": 0, "Open": 0, "Deferred": 0}
    for row in alliance_rows:
        word = status_word(split_row(row)[3])
        if word in alliance_counts:
            alliance_counts[word] += 1
    if alliance_counts != {"Approved": 36, "Provisional": 72, "Open": 12, "Deferred": 0}:
        failures.append(f"[C16] Alliance requirement status split changed: {alliance_counts}")
    key_texts = {
        "REQ-099": ["seven raw goods", "four manufactured goods", "gasoline", "aluminum"],
        "REQ-513": ["global trade is required", "g-1", "g-6"],
        "REQ-530": ["only diplomatic authority", "no delegation", "administrator may not"],
        "REQ-535": ["first leader", "founding creates no office", "ud-040"],
        "REQ-542": ["no mandatory leader", "heir", "council", "ud-041"],
        "REQ-543": ["no office is mandatory", "recognises no universal leader"],
        "REQ-548": ["168-turn", "open under ud-043", "no value is in force"],
        "REQ-549": ["no removal procedure", "open under ud-043"],
        "REQ-556": ["no treasury propose/approve/execute split", "owner-reserved under ud-046"],
        "REQ-566": ["candidate baseline under ud-040", "not approved"],
        "REQ-585": ["d-137 resolves ud-039", "no delegation"],
        "REQ-591": ["provisional", "b-10"],
        "REQ-593": ["all-086", "all-156", "ax-10"],
        "REQ-598": ["open under ud-048", "no discord account"],
        "REQ-617": ["cannot or will not use discord"],
    }
    for req_id, tokens in key_texts.items():
        row = get_row(trace, req_id)
        if not row:
            failures.append(f"[C16] Key requirement {req_id} is missing")
            continue
        joined = " ".join(row).lower()
        for token in tokens:
            if token not in joined:
                failures.append(f"[C16] {req_id} lost its meaning anchor '{token}'")
    if status_word(get_row(trace, "REQ-099")[3]) != "Approved":
        failures.append("[C16] REQ-099 (11-resource roster) must remain Approved")
    if status_word(get_row(trace, "REQ-591")[3]) != "Provisional":
        failures.append("[C16] REQ-591 must be Provisional after Prompt 10B supplies the B-10 rule")

    # ------------------------------------------------------------------
    # C17 - Decision registers
    # ------------------------------------------------------------------
    d_ids = [split_row(line)[0] for line in decisions.splitlines() if re.match(r"\|\s*D-\d{3}\s*\|", line)]
    # 2026-11-06 (Prompt 11C): D-162 / DD-210 record the authorization-code reuse
    # decision. 2026-11-06 (Prompt 12A): D-163…D-177 / DD-211…DD-225 are the fifteen B-12
    # research-and-design-foundation positions and UD-052…UD-060 were opened, so the
    # registers now run to D-177, DD-225 and UD-060. These are frontier counts, not
    # owner-status assertions: UD-040…UD-051 are untouched and still Open.
    # 2026-11-11 (Prompt 13A): the frontier advanced through 12B/12C (D-178…D-197 /
    # DD-226…DD-245) to D-198…D-205 / DD-246…DD-253, with UD-001…UD-060 unchanged
    # and no UD row resolved. Still frontier counts, not owner-status assertions.
    if d_ids != [f"D-{i:03d}" for i in range(1, 220)]:
        failures.append(f"[C17] DECISIONS.md IDs are not exactly D-001..D-219 ({len(d_ids)} rows)")
    dd_ids = [split_row(line)[0] for line in dd.splitlines() if re.match(r"\|\s*DD-\d{3}\s*\|", line)]
    if dd_ids != [f"DD-{i:03d}" for i in range(1, 268)]:
        failures.append(f"[C17] DD rows are not exactly DD-001..DD-267 ({len(dd_ids)} rows)")
    ud_ids = [split_row(line)[0] for line in ud.splitlines() if re.match(r"\|\s*UD-\d{3}\s*\|", line)]
    if ud_ids != [f"UD-{i:03d}" for i in range(1, 61)]:
        failures.append(f"[C17] UD rows are not exactly UD-001..UD-060 ({len(ud_ids)} rows)")
    ud_counts = {"Resolved": 0, "Open": 0, "Deferred": 0}
    for line in ud.splitlines():
        if re.match(r"\|\s*UD-\d{3}\s*\|", line):
            word = status_word(split_row(line)[-1])
            if word in ud_counts:
                ud_counts[word] += 1
    if ud_counts != {"Resolved": 28, "Open": 29, "Deferred": 3}:
        failures.append(f"[C17] UD status counts changed: {ud_counts}")
    dd_counts = {"Approved": 0, "Provisional": 0, "Confirmed": 0, "Binding inherited": 0, "Candidate": 0, "Superseded": 0, "Deferred": 0}
    for line in dd.splitlines():
        if re.match(r"\|\s*DD-\d{3}\s*\|", line):
            cells = split_row(line)
            clean = cells[2].replace("*", "").strip()
            # DD-165 records Phase 09B acceptance; the register's tally groups
            # it with Approved without converting it into an owner approval.
            if clean.startswith("Approved") or clean.startswith("Accepted"):
                dd_counts["Approved"] += 1
            elif clean.startswith("Provisional"):
                dd_counts["Provisional"] += 1
            elif clean.startswith("Confirmed"):
                dd_counts["Confirmed"] += 1
            elif clean.startswith("Binding inherited"):
                dd_counts["Binding inherited"] += 1
            elif clean.startswith("Candidate"):
                dd_counts["Candidate"] += 1
            elif clean.startswith("Superseded"):
                dd_counts["Superseded"] += 1
            elif clean.startswith("Deferred"):
                dd_counts["Deferred"] += 1
            else:
                failures.append(f"[C17] DD status is unclassified: {cells[0]} '{cells[2][:50]}'")
    # 2026-11-11 (Prompt 13A): Confirmed is 66 because DD-246…DD-253 are recorded as
    # Confirmed Category B/C design positions; no Phase-09B row changed class.
    expected_dd_counts = {"Approved": 130, "Provisional": 52, "Confirmed": 79, "Binding inherited": 2, "Candidate": 2, "Superseded": 1, "Deferred": 1}
    if dd_counts != expected_dd_counts:
        failures.append(f"[C17] DD status counts changed: {dd_counts}")
    tally_section = dd.split("## 6. Current tallies", 1)[-1]
    tally_expectations = {
        "Approved": 130,
        "Provisional": 52,
        # 2026-11-13 (Prompt 13B): the register's own tally rows moved with the
        # thirteen Confirmed 13B positions and the one Provisional bundle.
        "Confirmed": 79,
        "Binding inherited": 2,
        "Candidate / Open": 2,
        "Superseded": 1,
        "Deferred": 1,
    }
    for label, expected in tally_expectations.items():
        match = re.search(rf"^\|\s*{re.escape(label)}\s*\|\s*(\d+)\s*\|", tally_section, re.M)
        if not match or int(match.group(1)) != expected:
            failures.append(f"[C17] DD tally row '{label}' missing or not {expected}")
    if "| **Total** | **267** |" not in tally_section:
        failures.append("[C17] DD tally total is not 267")
    if "Project decisions: **219**" not in dd:
        failures.append("[C17] DD register no longer records 219 project decisions")
    if status_word(get_row(decisions, "D-135")[4]) != "Confirmed":
        failures.append("[C17] D-135 (open-ended constitutions) must remain Confirmed")
    if status_word(get_row(dd, "DD-151")[2]) != "Approved":
        failures.append("[C17] DD-151 (open-ended constitutions) must remain Approved")
    if status_word(get_row(decisions, "D-137")[4]) != "Confirmed":
        failures.append("[C17] D-137 (zero delegation) must remain Confirmed")
    for did in ("D-136", "D-138", "D-139"):
        row = get_row(decisions, did)
        if not row or status_word(row[4]) != "Candidate":
            failures.append(f"[C17] {did} must remain a Candidate architecture")
    # The guard is against D-106 citing the election-register identifier as if it
    # were a project decision (`D-204` instead of `DMP-204`). It used to test the
    # whole file because D-204 could not exist; Prompt 13A legitimately allocated
    # D-198…D-205, so the substring test would now flag the real D-204 row. Scope
    # the test to the row it protects and the assertion is unchanged in substance.
    d106_row = get_row(decisions, "D-106")
    if d106_row and re.search(r"(?<![A-Z])D-204(?![\d])", " ".join(d106_row)):
        failures.append("[C17] D-106 still cites non-existent D-204 (should be DMP-204)")

    # ------------------------------------------------------------------
    # C18 - Continuity and status
    # ------------------------------------------------------------------
    for relative in CONTINUITY_FILES:
        path = docs / relative
        content = read_file(path)
        if STATUS_SENTENCE not in content:
            failures.append(f"[C18] {relative} lacks the exact mandated 09B/09C status sentence")
    # 2026-11-03 (Prompt 10A): the next Stage 2 prompt is now the 10 family;
    # the bare "10" remains valid so this validator still says what it checked.
    # 2026-11-05 (Prompt 11A): Prompt 11 is split, so 11A/11B/11C are valid values.
    # 2026-11-06 (Prompt 11C): the 11C companion closed Prompt 11 at the design
    # level, so 12 is the live prompt and 10/11 remain valid history.
    # 2026-11-07 (Prompt 12A review remediation): 12A closed, so 12B is live.
    # 2026-11-11 (Prompt 13A): 12C closed on 2026-11-10 (owner-accepted
    # 2026-11-11) and Prompt 13 split with 13A complete, so 13B is the live value.
    if not re.search(r"^stage_2_next_prompt:\s*(?:10[ABC]?|11[ABC]?|12[ABC]?|13[ABC])\s*$", text["ai_context"], re.M):
        failures.append("[C18] AI_CONTEXT does not set stage_2_next_prompt: 10/10A/10B/10C/11/11A/11B/11C/12/12A/12B/12C/13A/13B/13C")
    current_state_files = {
        "AI_CONTEXT": text["ai_context"],
        "AI_HANDOFF": text["ai_handoff"],
        "PROJECT_PROGRESS": text["progress"],
        "ROADMAP": text["top_roadmap"],
        "stage-2 handoff": text["s2_handoff"],
        "stage-2 roadmap": text["roadmap"],
        "outline": text["outline"],
        "B-09": b09,
        "contracts": contracts,
        "formula register": formulas,
    }
    for label, content in current_state_files.items():
        if STALE_STATUS_SENTENCE in content:
            failures.append(f"[C18] {label} still carries the stale 09B-D status sentence")
        for line in content.splitlines():
            if re.search(r"09C\s+(?:is\s+)?(?:authorized|authorised|unblocked|started)\b", line, re.I):
                if not re.search(r"not\s+started|blocked|superseded|historical", line, re.I):
                    failures.append(f"[C18] {label} claims Prompt 09C is authorized or started: {line[:150]}")
            if re.search(r"09C[^.]{0,100}\bcomplete\b", line, re.I):
                if not re.search(r"specification|documentation|workflow", line, re.I):
                    failures.append(f"[C18] {label} claims Prompt 09C is complete without a specification-level qualifier: {line[:150]}")
            if "09B Complete" in line and not re.search(r"superseded|historical|at that time", line, re.I):
                failures.append(f"[C18] {label} still claims 09B Complete: {line[:150]}")
    if "Prompt 09B-M" not in "\n".join(b09.splitlines()[:10]):
        failures.append("[C18] B-09 does not name Prompt 09B-M in its header")
    if "Prompt 09B-M" not in "\n".join(contracts.splitlines()[:10]):
        failures.append("[C18] Contracts do not name Prompt 09B-M in their header")
    if "Prompt 09B-M" not in "\n".join(formulas.splitlines()[:10]):
        failures.append("[C18] Formula register does not name Prompt 09B-M in its header")

    # ------------------------------------------------------------------
    # C19 - Canonical Prompt 09C companion, specification boundary, no production code
    # ------------------------------------------------------------------
    canonical = stage2 / "16_alliances_workflows_acceptance.md"
    if not canonical.exists():
        failures.append("[C19] Canonical Prompt 09C companion is missing: 16_alliances_workflows_acceptance.md")
    else:
        companion = read_file(canonical)
        if "not a functioning Alliance system" not in companion or "No gameplay code" not in companion:
            failures.append("[C19] 09C companion does not state the specification-only boundary")
    for filename in [
        "16_alliances_workflows_and_acceptance.md",
        "16_alliances_acceptance_matrix.md",
        "16_alliances_qa_suite.md",
        "09C_validate_alliance.py",
    ]:
        if (stage2 / filename).exists():
            failures.append(f"[C19] Competing Prompt 09C deliverable exists: {filename}")
    for directory in ["src", "app", "components", "migrations"]:
        target = base_dir / directory
        if target.exists() and any(target.iterdir()):
            failures.append(f"[C19] Premature production-code directory exists: {directory}")
    if (base_dir / "supabase" / "migrations").exists():
        failures.append("[C19] Premature Supabase migrations directory exists")
    code_suffixes = {".ts", ".tsx", ".js", ".jsx", ".sql", ".vue", ".svelte"}
    for path in base_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in code_suffixes:
            continue
        relative = path.relative_to(base_dir)
        if relative.parts and relative.parts[0] == "prototypes":
            continue
        if "node_modules" in relative.parts or ".git" in relative.parts:
            continue
        if "docs" in relative.parts and "qa_backups" in relative.parts:
            continue
        failures.append(f"[C19] Production-like source file outside sanctioned areas: {relative}")
    if "Prompt 09C" not in log or "complete at the specification/documentation level" not in log:
        failures.append("[C19] Progress log does not record Prompt 09C as complete at the specification/documentation level")
    if "Prompt 10" not in log or "next and not started" not in log:
        failures.append("[C19] Progress log does not record Prompt 10 as next and not started")

    # ------------------------------------------------------------------
    # C20 - Cross-system anchors
    # ------------------------------------------------------------------
    if "168" not in " ".join(get_row(decisions, "D-028") or []):
        failures.append("[C20] D-028 dormancy (168 turns) anchor is missing")
    if not text["autonomy"]:
        failures.append("[C20] AUTONOMOUS_DECISION_POLICY.md is missing")
    for token in ["TR-024", "TR-029", "TR-060"]:
        if token not in text["b02"]:
            failures.append(f"[C20] B-02 no longer defines {token}")
    for doc_name in ["b04", "b07", "b08"]:
        if "alliance" not in text[doc_name].lower():
            failures.append(f"[C20] {paths[doc_name].name} no longer acknowledges the Alliance interface")
    for token in ["D-122", "DD-136", "D-133", "DD-147", "D-135", "DD-151", "REQ-530", "TR-024"]:
        if token not in b09 and token not in contracts:
            failures.append(f"[C20] Cross-system anchor {token} is missing from the Alliance documents")

    # ------------------------------------------------------------------
    # C21 - Progress log and historical preservation
    # ------------------------------------------------------------------
    for section in ["## 37.", "## 38.", "## 39.", "## 40.", "## 41.", "## 42.", "## 43.", "## 44.", "## 45.", "## 46.", "## 47.", "## 48.", "## 49.", "## 50.", "## 51.", "## 52.", "## 53."]:
        if section not in log:
            failures.append(f"[C21] Progress log lost historical section {section}")
    if "Prompt 09B-F correction" not in log:
        failures.append("[C21] Progress log has no Prompt 09B-F correction entry")
    if "Prompt 09B-I correction" not in log:
        failures.append("[C21] Progress log has no Prompt 09B-I correction entry")
    if "Prompt 09B-J" not in log:
        failures.append("[C21] Progress log has no Prompt 09B-J correction entry")
    if "Prompt 09B-K" not in log:
        failures.append("[C21] Progress log has no Prompt 09B-K correction entry")
    if "Prompt 09B-L" not in log:
        failures.append("[C21] Progress log has no Prompt 09B-L correction entry")
    if "Prompt 09B-M" not in log:
        failures.append("[C21] Progress log has no Prompt 09B-M correction entry")
    if "D-141" not in log or "D-142" not in log:
        failures.append("[C21] Progress log does not record D-141 and D-142")
    if "independent acceptance review pending" not in log.lower():
        failures.append("[C21] Progress log does not record that independent acceptance is pending")
    if "superseded by Prompt 09B-E" not in log:
        failures.append("[C21] Historical 09B/09B-C/09B-D authorization claims were not marked superseded")
    for did in ["D-135", "D-136", "D-137", "D-138", "D-139"]:
        if did not in log:
            failures.append(f"[C21] Historical decision {did} was deleted from the progress record")
    for version_file, label in [(b09, "B-09"), (contracts, "contracts"), (formulas, "formula register")]:
        if "**Version:** 2.8" not in "\n".join(version_file.splitlines()[:5]):
            failures.append(f"[C21] {label} version is not 2.8")

    # ------------------------------------------------------------------
    # C22 - Numeric neutrality (no threshold is required content)
    # ------------------------------------------------------------------
    if "No number in this register is required content" not in formulas:
        failures.append("[C22] Formula register no longer states that numeric values are optional content")
    if "is valid" not in formulas:
        failures.append("[C22] Formula register no longer states that omitting values is valid")
    all174 = get_rule(b09, "ALL-174")
    if "illustrative candidate parameter" not in all174 or "not an approved rule" not in all174:
        failures.append("[C22] ALL-174 no longer classifies every number as an illustrative candidate")
    for line in formulas.splitlines():
        if line.startswith("| **Decision Status**") and re.search(r"\bApproved\b", line):
            failures.append(f"[C22] A formula Decision Status row claims approval: {line[:140]}")
    if re.search(r"\b(?:50,000|10\s*%)\b[^.\n]{0,60}\b(?:required content|must be present)\b", formulas, re.I):
        failures.append("[C22] Formula register reintroduced a required numeric threshold")

    # ------------------------------------------------------------------
    # C23 - Cross-document consistency
    # ------------------------------------------------------------------
    for number in range(40, 50):
        ud_id = f"UD-{number:03d}"
        ud_row = get_row(ud, ud_id)
        b09_row = get_row(b09, ud_id)
        if ud_row and b09_row:
            if status_word(ud_row[-1]) != status_word(b09_row[3]):
                failures.append(
                    f"[C23] {ud_id} status disagrees between UD register and B-09 ledger"
                )
    for ax_id, (must_have, _) in AX_STATUS_RULES.items():
        if ax_id not in ax:
            continue
        ud_refs = re.findall(r"UD-04\d", field_value(ax[ax_id][1], "Unresolved Decision"))
        for ud_ref in ud_refs:
            row = get_row(ud, ud_ref)
            if row and status_word(row[-1]) != "Open":
                failures.append(f"[C23] {ax_id} cites {ud_ref} but the decision is not Open")
    if "UD-046" in " ".join(get_row(dd, "DD-157") or []) and status_word(get_row(ud, "UD-046")[-1]) != "Open":
        failures.append("[C23] DD-157 and the UD-046 register disagree")
    if status_word(get_row(trace, "REQ-530")[3]) != "Provisional":
        failures.append("[C23] REQ-530 must remain Provisional")
    if "REQ-530" in b09 and "provisional" not in b09.lower():
        failures.append("[C23] B-09 no longer acknowledges REQ-530's Provisional status")

    # ------------------------------------------------------------------
    # C24 - Succession and vacancy authority remain owner-reserved (UD-043)
    # ------------------------------------------------------------------
    all057 = plain(get_rule(b09, "ALL-057")).lower()
    for token in [
        "audit evidence only",
        "does not decide which claim prevails",
        "assign or transfer any office",
        "owner-reserved under ud-043",
        "does not adjudicate",
    ]:
        if token not in all057:
            failures.append(f"[C24] ALL-057 lost its audit-evidence-only anchor '{token}'")
    ax03 = plain(ax.get("AX-03", ("", ""))[1]).lower()
    for token in [
        "no office, authority or seat transfers automatically",
        "none while ud-043 is open",
        "prevents the platform from inventing a succession outcome",
        "no fallback stewardship, caretaker appointment or dissolution executes",
    ]:
        if token not in ax03:
            failures.append(f"[C24] AX-03 lost its no-automatic-succession anchor '{token}'")
    ax04 = plain(ax.get("AX-04", ("", ""))[1]).lower()
    for token in [
        "any succession or vacancy rule is candidate under ud-043",
        "the platform prescribes no role or threshold",
    ]:
        if token not in ax04:
            failures.append(f"[C24] AX-04 lost its candidate-succession anchor '{token}'")
    fal003 = ""
    match_fal003 = re.search(r"###\s+F-AL-003\b[\s\S]*?(?=\n###|\Z)", formulas)
    if match_fal003:
        fal003 = plain(match_fal003.group(0)).lower()
    for token in [
        "no declaration or consequence is in force",
        "no automatic dissolution or authority transfer is in force",
    ]:
        if token not in fal003:
            failures.append(f"[C24] F-AL-003 lost its candidate-status anchor '{token}'")
    b03_plain = plain(text["b03"]).lower()
    if "candidate under ud-043 and is not applied automatically" not in b03_plain:
        failures.append("[C24] B-03 no longer keeps office succession candidate and non-automatic")

    order_re = re.compile(
        r"\b(?:timestamp|transaction\s+order|earliest\s+(?:valid\s+|recorded\s+)?claimant|"
        r"earlier\s+(?:recorded\s+|valid\s+)?(?:timestamp|record|claim|claimant)|"
        r"chronological\s+order|first\s+(?:valid\s+|recorded\s+)?(?:claim|claimant|transaction)|"
        r"order\s+of\s+(?:the\s+)?(?:record|transaction|claim)s?|"
        r"time\s+of\s+(?:the\s+)?(?:record|transaction))\b",
        re.I,
    )
    succession_re = re.compile(
        r"\b(?:succession|successor|steward(?:ship)?|vacan(?:cy|t)|leaders?|leadership|"
        r"office|claim|claims|prevails?)\b",
        re.I,
    )
    succession_verb_re = re.compile(
        r"\b(?:decides?|determines?|establishes?|confirms?|recognis\w*|recogniz\w*|"
        r"assigns?|transfers?|grants?|vests?|awards?|prevails?|wins?|"
        r"is\s+(?:the\s+)?(?:valid|authoritative|decisive|prevailing)|"
        r"takes?\s+(?:the\s+)?office|becomes?\s+(?:the\s+)?(?:successor|leader|steward))\b",
        re.I,
    )
    automatic_re = re.compile(
        r"\b(?:automatic(?:ally)?|by\s+default|fallback|system\s+caretaker|"
        r"auto[- ]appoint\w*)\b",
        re.I,
    )
    automatic_verb_re = re.compile(
        r"\b(?:transfers?|assigns?|appoints?|elevates?|promotes?|grants?|vests?|"
        r"passes?|assumes?|becomes?|installs?|recognis\w*|recogniz\w*|awards?|"
        r"enters?\s+office)\b",
        re.I,
    )
    succession_documents = [
        ("B-09", b09),
        ("contracts", contracts),
        ("formula register", formulas),
        ("requirements", trace),
        ("DD register", dd),
        ("DECISIONS", decisions),
        ("B-02", text["b02"]),
        ("B-03", text["b03"]),
        ("B-08", text["b08"]),
        ("08C workflows", text["b08_workflows"]),
    ]
    for label, content in succession_documents:
        document = plain(content)
        for sentence in sentences(document):
            if len(sentence) > 700:
                continue
            for clause in clauses(sentence):
                policy = norm(clause)
                if succession_re.search(policy):
                    issue = first_policy_match(SUCCESSION_ENTITLEMENT_PATTERNS, policy)
                    if not issue and order_re.search(policy):
                        issue = first_policy_match(SUCCESSION_ORDER_ENTITLEMENT_PATTERNS, policy)
                    if issue:
                        source = f"{label} {nearest_id(document, clause)}".strip()
                        failures.append(
                            f"[C24] {source} establishes an unauthorized succession entitlement "
                            f"under owner-reserved UD-043 ({issue}): {clause[:180]}"
                        )
                        continue
                if NEGATION.search(clause) or CONDITIONAL.search(clause):
                    continue
                if (
                    order_re.search(clause)
                    and succession_re.search(clause)
                    and succession_verb_re.search(clause)
                ):
                    source = f"{label} {nearest_id(document, clause)}".strip()
                    failures.append(
                        f"[C24] {source} imposes an unauthorized succession outcome "
                        f"under owner-reserved UD-043: {clause[:180]}"
                    )
                if (
                    automatic_re.search(clause)
                    and succession_re.search(clause)
                    and automatic_verb_re.search(clause)
                ):
                    source = f"{label} {nearest_id(document, clause)}".strip()
                    failures.append(
                        f"[C24] {source} transfers succession authority automatically "
                        f"under owner-reserved UD-043: {clause[:180]}"
                    )

    # ------------------------------------------------------------------
    # C25 - Membership appeals, expulsion and rejoin remain owner-reserved (UD-044)
    # ------------------------------------------------------------------
    req551 = plain(" ".join(get_row(trace, "REQ-551") or [])).lower()
    for token in [
        "no appeal or dispute-resolution mechanism is required or approved while ud-044 is open",
        "never adjudicates the merits",
        "declared path",
        "recorded decision",
    ]:
        if token not in req551:
            failures.append(f"[C25] REQ-551 lost its conditional-appeal anchor '{token}'")
    req568 = plain(" ".join(get_row(trace, "REQ-568") or [])).lower()
    if "no expulsion mechanism is approved while ud-044 is open" not in req568:
        failures.append("[C25] REQ-568 no longer keeps expulsion unapproved under UD-044")
    req569 = plain(" ".join(get_row(trace, "REQ-569") or [])).lower()
    if "no rejoin cooldown, blacklist or rejoin rule is in force" not in req569:
        failures.append("[C25] REQ-569 no longer keeps rejoin policy unapproved under UD-044")
    all079 = plain(get_rule(b09, "ALL-079")).lower()
    if "member rights and protections are owner-reserved under ud-044" not in all079:
        failures.append("[C25] ALL-079 lost its UD-044 member-rights reservation")
    ax09 = plain(ax.get("AX-09", ("", ""))[1]).lower()
    if "neither is enforced while ud-040/ud-044 are open" not in ax09:
        failures.append("[C25] AX-09 no longer keeps single-alliance and cooldown unenforced")

    appeal_re = re.compile(
        r"\b(?:appeal\w*|grievance\w*|tribunal\w*|dispute[- ]resolution|"
        r"arbitrat\w*|adjudicat\w*)\b",
        re.I,
    )
    # "Review" is only appeal-related when it is tied to expulsion, removal
    # or another disciplinary decision. A generic document review is not a
    # membership appeal and must not be flagged.
    review_re = re.compile(
        r"\b(?:review|reviews|reviewed|reviewable|reviewability|reconsider\w*|"
        r"appellate)\b",
        re.I,
    )
    discipline_re = re.compile(
        r"\b(?:expel\w*|expulsion|remov\w*|disciplinary|discipline|sanction\w*)\b",
        re.I,
    )
    mandate_re = re.compile(
        r"\b(?:must|shall|required?|mandatory|entitled|guarantee[sd]?|"
        r"has\s+(?:a|the)\s+right|has\s+access\s+to|cannot\s+be\s+(?:removed|expelled)\s+without|"
        r"(?:is|are)\s+entitled\s+to\s+due\s+process|due\s+process\s+(?:is|must|shall)|"
        r"may|can)\b",
        re.I,
    )
    alliance_member_re = re.compile(
        r"\b(?:alliance|member|expel\w*|expulsion|removal|officer|council|"
        r"constitution|tribunal)\b",
        re.I,
    )
    external_moderation_re = re.compile(
        r"\b(?:account|platform\s+moderation|moderation|sanction\w*|enforcement|"
        r"ban(?:ned)?|NET-\d|ACC-\d|REQ-093|REQ-064)\b",
        re.I,
    )
    expel_re = re.compile(r"\b(?:expel\w*|expulsion)\b", re.I)
    redress_re = re.compile(r"\b(?:redress|remed(?:y|ies))\b", re.I)
    # Bounded procedural-domain gate. C25 should not grow an unbounded list of
    # exact sentences, so a membership policy is recognised from three signals:
    # an affected person (or an expulsion/removal context), a procedural
    # action, and a normative force. A generic "review" without a disciplinary
    # context is not membership policy, and "challenge"/"reopen" only count
    # when their object is an expulsion, removal or review decision.
    procedural_review_re = re.compile(
        r"\b(?:reviews?|reviewed|reviewable)\b", re.I
    )
    procedural_challenge_re = re.compile(
        r"\bchalleng\w*\b.{0,30}\b(?:expulsion|expelled|removal|removed|"
        r"disciplinary\s+decision|sanction\w*|review|appeal|reconsideration|"
        r"dismiss\w*)\b",
        re.I,
    )
    # "Dismissal" may mean expulsion or an unrelated removal. It is a policy
    # context, but not one C25 can resolve without owner context.
    procedural_dismissal_re = re.compile(r"\bdismiss\w*\b", re.I)
    # A grievance process is a potential member remedy or review procedure.
    # It is treated as a procedural action, but a passive or unspecified
    # grievance route is not a confirmed appeal policy.
    procedural_grievance_re = re.compile(r"\bgrievance\w*\b", re.I)
    procedural_reopen_re = re.compile(
        r"\b(?:reopen\w*|revers\w*)\b.{0,30}\b(?:expulsion|expelled|removal|"
        r"removed|decision|review|appeal|reconsideration)\b",
        re.I,
    )
    procedural_appeal_only_re = re.compile(
        r"\b(?:appeals?|appell(?:ate|ant)|reconsider\w*|petition\w*|hearings?|"
        r"redress|remed(?:y|ies))\b",
        re.I,
    )
    procedural_clear_action_re = re.compile(
        r"\b(?:appeals?|appell(?:ate|ant)|reconsider\w*|reviews?|reviewed|"
        r"reviewable|hearings?)\b",
        re.I,
    )
    procedural_person_re = re.compile(
        r"\b(?:members?|expelled|former\s+members?|removed\s+members?|"
        r"applicants?|nations?|players?|officers?)\b",
        re.I,
    )
    procedural_force_re = re.compile(
        r"\b(?:may|can|is\s+permitted|are\s+permitted|is\s+entitled|are\s+entitled|"
        r"has\s+(?:a\s+|the\s+)?right|have\s+(?:a\s+|the\s+)?right|must|shall|"
        r"required?|mandatory|guarantee[sd]?|subject\s+to|available|open\s+to|"
        r"access\s+to|final|cannot|can\s+not|may\s+not|shall\s+not|must\s+not|"
        r"not\s+(?:be\s+)?(?:reviewed|appealed|reconsidered|challenged)|"
        r"no\s+(?:right|avenue|route|opportunity|access))\b",
        re.I,
    )
    procedural_remedy_re = re.compile(r"\b(?:redress|remed(?:y|ies))\b", re.I)
    procedural_reserved_re = re.compile(
        r"\b(?:whether|if)\b.{0,120}\b(?:appeal|review|reconsider\w*|petition\w*|"
        r"challeng\w*|redress|remed(?:y|ies))\b.{0,80}\b(?:owner[- ]reserved|"
        r"remains?\s+open|open\s+under\s+ud\s*0?44|undecided|not\s+approved|"
        r"not\s+decided|not\s+in\s+force)\b",
        re.I,
    )

    def procedural_policy_signal(text: str) -> str:
        """Return 'fail', 'review' or '' for a bounded membership-procedure policy."""
        c = norm(text)
        if not c:
            return ""
        has_review = bool(procedural_review_re.search(c))
        has_appeal = bool(procedural_appeal_only_re.search(c))
        has_grievance = bool(procedural_grievance_re.search(c))
        has_dismissal = bool(procedural_dismissal_re.search(c))
        has_challenge = bool(procedural_challenge_re.search(c))
        has_reopen = bool(procedural_reopen_re.search(c))
        if not (
            has_review
            or has_appeal
            or has_grievance
            or has_challenge
            or has_reopen
        ):
            return ""
        has_person = bool(procedural_person_re.search(c))
        has_discipline = bool(discipline_re.search(c))
        if not (has_person or has_discipline):
            return ""
        # A generic "review" needs a disciplinary context or another clear
        # procedural action; a budget or document review is not an appeal.
        if has_review and not has_discipline and not (has_appeal or has_challenge or has_reopen):
            return ""
        if not procedural_force_re.search(c):
            return ""
        # An explicit reservation is not an operative policy, but a separate
        # active assertion in the same clause still controls.
        if (
            not APPEAL_ACTIVE_ASSERTION.search(c)
            and procedural_reserved_re.search(c)
        ):
            return ""
        # A grievance route without a named appeal or review action is a
        # potential member remedy, not a confirmed one. A guarantee or other
        # explicit entitlement decides the policy; a passive "is available"
        # still needs owner context.
        if has_grievance and not (
            procedural_clear_action_re.search(c) or has_challenge or has_reopen
        ):
            if re.search(
                r"\b(?:guarantee[sd]?|entitled|has\s+(?:a\s+|the\s+)?right|"
                r"have\s+(?:a\s+|the\s+)?right|must|shall|mandatory|"
                r"provides?|establishes?|creates?)\b",
                c,
            ):
                return "fail"
            return "review"
        # "Dismissal" alone cannot be read as expulsion. A challenge to it is
        # surfaced for context unless the clause also names expulsion, removal
        # or another disciplinary decision.
        if has_dismissal and not has_discipline:
            return "review"
        # Petition/redress wording can describe an appeal remedy or an
        # unrelated complaint route. Route it to review rather than guessing.
        if procedural_remedy_re.search(c) and not (
            procedural_clear_action_re.search(c) or has_challenge or has_reopen
        ):
            return "review"
        return "fail"

    rejoin_re = re.compile(
        r"\b(?:rejoin\w*|re-?entry|return(?:ing)?\s+to\s+(?:the\s+)?alliance)\b", re.I
    )
    rejoin_restriction_re = re.compile(
        r"\b(?:cooldown|cooling[- ]off|wait(?:ing)?\s+period|wait|delay|"
        r"blacklist|blocklist|ban(?:ned)?|barred|ineligib\w*|den(?:y|ied)|"
        r"refus\w*|prevent\w*|prohibit\w*|\d+\s*[- ]?\s*turns?)\b",
        re.I,
    )
    # C25 owns Alliance membership policy (UD-044). B-12's account-level
    # appeals (REQ-764 onward) are a different subsystem and must not be read
    # as an Alliance appeal entitlement, so restrict this scan to the Alliance
    # requirement block REQ-534..REQ-653.
    trace_alliance = "\n".join(
        line for line in trace.splitlines()
        if not re.match(r"^\|\s*REQ-\d{3}\s*\|", line)
        or 534 <= int(re.match(r"^\|\s*REQ-(\d{3})", line).group(1)) <= 653
    )
    membership_documents = [
        ("B-09", b09),
        ("contracts", contracts),
        ("requirements", trace_alliance),
        ("DD register", dd),
        ("DECISIONS", decisions),
        ("08C workflows", text["b08_workflows"]),
    ]

    example_frame_re = re.compile(
        r"\b(?:example|illustrative|illustration|hypothetical|fixture|"
        r"test fixture|sample|specimen)\b",
        re.I,
    )
    # A quoted sample introduced as "the fixture reads:" is exempt only when
    # the same sentence explicitly marks it non-operative. The exemption is
    # limited to the clause carrying the example label; a separate live-sounding
    # grant elsewhere in the sentence is still evaluated.
    quoted_example_re = re.compile(
        r"\b(?:example|illustrative|illustration|hypothetical|fixture|sample|specimen)\b"
        r"[^.;:]{0,40}\b(?:reads?|states?|says?|shows?|depicts?|contains?)\s*:",
        re.I,
    )
    meta_rejection_re = re.compile(
        r"\b(?:fails?|failed|rejects?|rejected|invalid|not accepted|"
        r"does not pass|expected to fail|negative control|validator|"
        r"test case|used to test|would fail|not part of (?:this|the) design|"
        r"not operative|non-operative)\b",
        re.I,
    )
    framing_split_re = re.compile(r"\s*:\s*|\s+[—–]\s+", re.I)

    def neutral_holding(text: str) -> bool:
        c = norm(text)
        return any(pattern.search(c) for pattern in APPEAL_NEUTRAL_PATTERNS)

    def non_policy_context(text: str) -> bool:
        c = norm(text)
        # "Former members", "rejected applicants" and similar phrases name
        # people, not a historical rule or a rejected proposal. The adjective
        # must not immunise a live-sounding entitlement held by those people.
        label_on_people = re.compile(
            r"\b(?:rejected|withdrawn|superseded|retired|earlier|previous|prior|"
            r"former|old)\s+(?:(?:alliance)\s+)?(?:members?|nations?|players?|"
            r"applicants?|officers?)\b"
        )
        scrubbed = label_on_people.sub(" ", c)
        if not APPEAL_NON_POLICY_CONTEXT.search(scrubbed):
            return False
        if (
            APPEAL_CONTEXT_NEGATED.search(scrubbed)
            or APPEAL_ACTIVE_FRAME.search(scrubbed)
            or APPEAL_ACTIVE_ASSERTION.search(scrubbed)
        ):
            return False
        # "Example" and "fixture" are not blanket exemptions: a document that
        # states a live-sounding grant after an example label still asserts
        # it. The label exempts only when the same clause marks the sample as
        # rejected, invalid or a tested negative control.
        if example_frame_re.search(scrubbed) and not meta_rejection_re.search(scrubbed):
            return False
        return True

    def neutral_residual(text: str) -> str:
        residual = text
        for pattern in APPEAL_NEUTRAL_PATTERNS:
            residual = pattern.sub(" ", residual)
        return residual

    def appeal_subject(text: str) -> bool:
        has_person = bool(
            re.search(
                r"\b(?:member|members|nation|nations|player|players|officer|"
                r"applicants?|expelled|expulsion|removal)\b",
                text,
            )
        )
        has_discipline = bool(discipline_re.search(text))
        return bool(
            appeal_re.search(text)
            or expel_re.search(text)
            or re.search(r"\bappellate\b", text)
            or (
                procedural_appeal_only_re.search(text)
                and (has_person or has_discipline)
            )
            or (
                procedural_review_re.search(text)
                and (has_person or has_discipline)
            )
            or (
                procedural_challenge_re.search(text)
                and (has_person or has_discipline)
            )
            or (
                procedural_reopen_re.search(text)
                and (has_person or has_discipline)
            )
        )

    def appeal_policy_issue(text: str) -> str:
        c = norm(text)
        if not c:
            return ""
        subject = appeal_subject(c)
        if not subject:
            return ""
        # A labelled example or fixture that the same clause marks as
        # non-operative ("... but it is not part of this design") is exempt as
        # a whole. Splitting off the framing label and evaluating only the
        # quoted sample would turn a non-operative illustration into a grant.
        if (
            example_frame_re.search(c)
            and meta_rejection_re.search(c)
            and not APPEAL_CONTEXT_NEGATED.search(c)
            and not APPEAL_ACTIVE_FRAME.search(c)
        ):
            return ""
        if external_moderation_re.search(text) and not alliance_member_re.search(c):
            return ""
        # A colon or dash can separate a framing label from the assertion it
        # introduces. The residual is a policy statement in its own right, so
        # a historical or disclaimer prefix cannot immunise it.
        candidates = [c]
        framed = framing_split_re.split(c, maxsplit=1)
        if len(framed) == 2 and len(framed[0]) <= 150:
            candidates.append(framed[1])
        for candidate in candidates:
            if non_policy_context(candidate):
                continue
            if neutral_holding(candidate):
                # Evaluate the branch that survives neutral framing, not the
                # complete clause. A denial phrase inside a neutral holding
                # must not mask a grant asserted in an except/unless branch.
                target = neutral_residual(candidate)
            else:
                target = candidate
            issue = first_policy_match(APPEAL_VIOLATION_PATTERNS, target)
            if not issue and procedural_policy_signal(target) == "fail":
                issue = "asserts a procedural appeal, review or expulsion-remedy policy"
            if issue:
                return issue
        return ""

    def appeal_review_issue(text: str) -> str:
        c = norm(text)
        if not c or not appeal_subject(c):
            return ""
        if external_moderation_re.search(text) and not alliance_member_re.search(c):
            return ""
        if (
            example_frame_re.search(c)
            and meta_rejection_re.search(c)
            and not APPEAL_CONTEXT_NEGATED.search(c)
            and not APPEAL_ACTIVE_FRAME.search(c)
        ):
            return ""
        candidates = [c]
        framed = framing_split_re.split(c, maxsplit=1)
        if len(framed) == 2 and len(framed[0]) <= 150:
            candidates.append(framed[1])
        for candidate in candidates:
            if non_policy_context(candidate) or neutral_holding(candidate):
                continue
            verdict = procedural_policy_signal(candidate)
            if verdict == "review":
                return "uncertain procedural remedy wording"
            issue = first_policy_match(APPEAL_REVIEW_PATTERNS, candidate)
            if issue:
                return issue
        return ""

    for label, content in membership_documents:
        document = plain(content)
        for sentence in sentences(document):
            sentence_norm = norm(sentence)
            non_operative_quoted_example = bool(
                quoted_example_re.search(sentence)
                and meta_rejection_re.search(sentence_norm)
                and not APPEAL_CONTEXT_NEGATED.search(sentence_norm)
                and not APPEAL_ACTIVE_FRAME.search(sentence_norm)
            )
            failures_before = len(failures)
            for clause in clauses(sentence):
                if non_operative_quoted_example and example_frame_re.search(norm(clause)):
                    continue
                issue = ""
                for segment in policy_segments(clause):
                    issue = appeal_policy_issue(segment)
                    if issue:
                        break
                if issue:
                    source = f"{label} {nearest_id(document, clause)}".strip()
                    failures.append(
                        f"[C25] {source} asserts an unauthorized appeal policy "
                        f"under owner-reserved UD-044 ({issue}): {clause[:180]}"
                    )
                    continue
                # A negation or conditional marker no longer exempts the whole
                # clause. Each policy branch is evaluated on its own; only a
                # branch that is itself a neutral holding statement is exempt.
                review_candidate = ""
                for segment in policy_segments(clause):
                    c = norm(segment)
                    if neutral_holding(c) or non_policy_context(c):
                        continue
                    if procedural_policy_signal(c) == "review":
                        if not review_candidate:
                            review_candidate = "uncertain procedural remedy wording"
                        continue
                    if (
                        appeal_re.search(c)
                        and mandate_re.search(c)
                        and alliance_member_re.search(c)
                        and not external_moderation_re.search(c)
                    ):
                        source = f"{label} {nearest_id(document, clause)}".strip()
                        failures.append(
                            f"[C25] {source} mandates an alliance appeal or dispute procedure "
                            f"under owner-reserved UD-044: {clause[:180]}"
                        )
                        break
                    if expel_re.search(c) and mandate_re.search(c):
                        source = f"{label} {nearest_id(document, clause)}".strip()
                        failures.append(
                            f"[C25] {source} mandates an expulsion rule under owner-reserved "
                            f"UD-044: {clause[:180]}"
                        )
                        break
                    if (
                        rejoin_re.search(c)
                        and rejoin_restriction_re.search(c)
                        and mandate_re.search(c)
                    ):
                        source = f"{label} {nearest_id(document, clause)}".strip()
                        failures.append(
                            f"[C25] {source} mandates a rejoin rule under owner-reserved "
                            f"UD-044: {clause[:180]}"
                        )
                        break
                    if not review_candidate:
                        review_candidate = appeal_review_issue(segment)
                else:
                    if review_candidate:
                        source = f"{label} {nearest_id(document, clause)}".strip()
                        review_findings.append(
                            f"[C25][REVIEW] {source} contains uncertain active appeal/review "
                            f"wording under owner-reserved UD-044 ({review_candidate}); "
                            f"manual review required: {clause[:180]}"
                        )
            # A coordinated sentence can distribute subject and object across
            # an "and": "All expulsion decisions are final and cannot be
            # reviewed." Each clause alone looks incomplete, so evaluate the
            # complete sentence as a bounded fallback. A failure already found
            # in any clause still controls.
            if len(failures) == failures_before:
                sentence_verdict = procedural_policy_signal(sentence_norm)
                if (
                    sentence_verdict == "fail"
                    and not non_policy_context(sentence_norm)
                    and not neutral_holding(sentence_norm)
                    and not (
                        external_moderation_re.search(sentence_norm)
                        and not alliance_member_re.search(sentence_norm)
                    )
                ):
                    source = f"{label} {nearest_id(document, sentence)}".strip()
                    failures.append(
                        f"[C25] {source} asserts a coordinated unauthorized appeal "
                        f"policy under owner-reserved UD-044: {sentence[:180]}"
                    )

    # ------------------------------------------------------------------
    # C26 - Measured reservation of UD-040..UD-049 by subject
    # ------------------------------------------------------------------
    b09_plain = plain(b09).lower()
    ud_anchors = {
        "UD-040": (
            "B-09",
            b09_plain,
            "eligibility, fees and the single-alliance rule are candidate only",
        ),
        "UD-041": (
            "B-09",
            b09_plain,
            "office template, succession/removal and pool policy remain owner-reserved under ud-041",
        ),
        "UD-042": ("B-09", b09_plain, "any native ballot tool is candidate scope"),
        "UD-043": (
            "B-09",
            b09_plain,
            "any rule for resolving competing claims remains owner-reserved under ud-043",
        ),
        "UD-044": (
            "B-09",
            b09_plain,
            "member rights and protections are owner-reserved under ud-044",
        ),
        "UD-045": (
            "B-09",
            b09_plain,
            "remain open owner decisions under ud-045",
        ),
        "UD-046": (
            "B-09",
            b09_plain,
            "ownership, custody, capacity, general withdrawal",
        ),
        "UD-047": ("B-09", b09_plain, "positions are candidate under ud-047"),
        "UD-048": ("B-09", b09_plain, "remain owner-reserved under ud-048"),
        "UD-049": ("B-09", b09_plain, "candidate bulletin tools"),
    }
    for ud_id, (label, content, token) in ud_anchors.items():
        if token not in content:
            failures.append(f"[C26] {label} lost its '{token}' reservation for {ud_id}")

    ud_settled_guards = {
        "UD-040": (
            "founding or multi-membership policy",
            [
                r"\b(?:one|a single|at most one)\s+alliance\b[^.\n]{0,40}\b(?:is|remains?)\s+"
                r"(?:the\s+)?(?:approved|mandatory|enforced|in force|final|binding)\b",
                r"\b(?:founding|found(?:ing)?\s+an\s+alliance)\b[^.\n]{0,50}"
                r"\b(?:costs?|requires?|fees?)\b[^.\n]{0,30}"
                r"\b(?:approved|mandatory|in force|enforced)\b",
                r"\b(?:membership|member)\b[^.\n]{0,40}\b(?:is|are)\s+limited\s+to\s+"
                r"(?:one|a single)\s+alliance\b",
            ],
        ),
        "UD-041": (
            "default office or government model",
            [
                r"\b(?:default|approved)\s+(?:office|government|role)\s+(?:model|template|set)\b"
                r"[^.\n]{0,60}\b(?:is|includes?|contains?|ships?)\b",
            ],
        ),
        "UD-042": (
            "charter or native ballot policy",
            [
                r"\b(?:native|internal)\s+(?:votes?|ballots?)\b[^.\n]{0,50}"
                r"\b(?:are|is|will\s+be)\s+(?:approved|enabled|mandatory|in\s+force|available)\b",
                r"\b(?:charter|constitution)\s+ratification\s+(?:requires|needs|is)\b"
                r"[^.\n]{0,40}\b(?:native|member)\s+(?:vote|ballot)\b",
            ],
        ),
        "UD-045": (
            "permission catalogue or delegation limits",
            [
                r"\b(?:permission|capability)\s+(?:catalogue|set|list)\b[^.\n]{0,50}"
                r"\b(?:is|are)\s+(?:approved|adopted|fixed|in\s+force|mandatory)\b",
                r"\broles\.manage\b[^.\n]{0,40}\b(?:is|remains)\s+"
                r"(?:approved|required|mandatory|enabled)\b",
            ],
        ),
        "UD-046": (
            "treasury ownership, capacity or approval policy",
            [
                r"\b(?:alliance|pool|treasury)\b[^.\n]{0,40}\b(?:ownership|capacity|withdrawal)\b"
                r"[^.\n]{0,40}\b(?:is|are)\s+(?:approved|enforced|in\s+force|mandatory)\b",
            ],
        ),
        "UD-047": (
            "collective diplomacy policy",
            [
                r"\bcollective\s+(?:diplomatic\s+)?(?:positions?|stances?|treat(?:y|ies))\b"
                r"[^.\n]{0,50}\b(?:are|is|become|becomes)\s+"
                r"(?:binding|enforceable|approved|in\s+force)\b",
                r"\balliance\s+(?:may|can|shall)\s+(?:sign|conclude|ratify|negotiate)\b"
                r"[^.\n]{0,30}\btreat(?:y|ies)\b",
            ],
        ),
        "UD-048": (
            "Discord invite visibility or validation policy",
            [
                r"\b(?:discord\s+)?invite\s+(?:link|url)\b[^.\n]{0,50}"
                r"\b(?:is|are|defaults?\s+to)\s+(?:public|visible|alliance[- ]only|hidden|required)\b",
                r"\b(?:discord\s+)?invite\s+(?:link|url)\b[^.\n]{0,50}\b(?:must|shall)\s+be\b",
            ],
        ),
        "UD-049": (
            "announcement or formal-vote release scope",
            [
                r"\b(?:announcements?|formal\s+votes?|native\s+votes?|bulletins?)\b"
                r"[^.\n]{0,60}\b(?:are|is|will\s+be|ships?)\b[^.\n]{0,40}"
                r"\b(?:approved|adopted|included|enabled|available|in\s+the\s+first\s+release)\b",
                r"\b(?:first\s+release|launch\s+scope|initial\s+release)\b[^.\n]{0,60}"
                r"\b(?:includes?|will\s+include|contains?)\b[^.\n]{0,40}"
                r"\b(?:announcements?|formal\s+votes?|bulletins?)\b",
            ],
        ),
    }
    ud_documents = [
        ("B-09", b09),
        ("contracts", contracts),
        ("formula register", formulas),
        ("requirements", trace),
        ("DD register", dd),
        ("DECISIONS", decisions),
        ("B-02", text["b02"]),
        ("B-03", text["b03"]),
        ("B-04", text["b04"]),
        ("B-05", text["b05"]),
        ("B-06", text["b06"]),
        ("B-07", text["b07"]),
        ("B-08", text["b08"]),
        ("08C workflows", text["b08_workflows"]),
    ]
    for label, content in ud_documents:
        for sentence in sentences(plain(content)):
            if len(sentence) > 700 or sentence.rstrip().endswith("?"):
                continue
            if NEGATION.search(sentence) or CONDITIONAL.search(sentence):
                continue
            for ud_id, (description, patterns) in ud_settled_guards.items():
                if not any(re.search(pattern, sentence, re.I) for pattern in patterns):
                    continue
                failures.append(
                    f"[C26] {label} settles {ud_id} {description} without owner approval: "
                    f"{sentence[:180]}"
                )


    # ------------------------------------------------------------------
    # C27 - Owner-authorized automatic per-turn production taxation
    # ------------------------------------------------------------------
    def section_has_all(rule_range: range, tokens: list[str], label: str) -> None:
        text = " ".join(get_rule(b09, f"ALL-{i:03d}") for i in rule_range)
        lowered = text.lower()
        for token in tokens:
            if token.lower() not in lowered:
                failures.append(f"[{label}] Rule set {rule_range.start:03d}..{rule_range.stop - 1:03d} lost '{token}'")

    section_has_all(
        range(179, 188),
        [
            "automatic",
            "per-turn",
            "current-turn production",
            "10,000",
            "basis points",
            "0% through 100%",
            "restricted to 10-percentage-point increments",
            "0% fallback",
            "player-authored constitution",
            "no fixed office",
            "require the member nation's owner to approve each policy version",
            "cumulative gross",
            "independent per-event floors are not used",
            "alliance receiving ledger",
            "idempotency key",
            "snapshot",
            "no ownership interest",
            "non-member",
            "no universal default rate",
            "never applied to the post-tax balance",
            "atomic transaction",
            "ud-046",
            "deducted at most once",
            "more than 100%",
            "multiple membership never authorizes multiple deductions",
            "no alliance is credited",
            "does not resolve `ud-040`",
            "post-tax net",
            "existing stockpiles consumed later are not taxable",
            "input consumed in processing is not taxed again",
            "newly generated output is taxed once",
            "per alliance",
            "one active bracket assignment",
            "holding a bracket in one alliance creates no bracket",
        ],
        "C27",
    )
    all183_body = get_rule(b09, "ALL-183").split(":**", 1)[-1].lower()
    if "no fixed office" not in all183_body:
        failures.append("[C27] ALL-183 operative text lost 'no fixed office'")

    def positive_matches(content: str, pattern: str, skip_negation: bool = True):
        for match in re.finditer(pattern, content):
            left = max(content.rfind(".", 0, match.start()), content.rfind("\n", 0, match.start()))
            rights = [pos for pos in (content.find(".", match.end()), content.find("\n", match.end())) if pos != -1]
            right = min(rights) if rights else len(content)
            clause_text = content[left + 1 : right + 1]
            if not skip_negation or not NEGATION.search(clause_text):
                yield match

    tax_guard = [
        (r"\b(?:the\s+)?(?:default|universal)\s+(?:alliance\s+)?tax\s+rate\s+(?:is|shall be|applies)\s+\d", "invents a default tax rate", False),
        (r"\b(?:silence|inactivity|membership|majority)\b[^.\n]{0,30}\b(?:counts?|is|constitutes?)\s+(?:as\s+)?consent\b", "treats silence or membership as consent", True),
        (r"\btax\b[^.\n]{0,60}\b(?:existing|opening|stored|prior|accumulated)\b[^.\n]{0,20}\b(?:balance|stockpile|production)\b", "taxes existing value rather than current-turn production", True),
        (r"\b(?:tax\s+rates?|rates?)\b[^.\n]{0,40}\b(?:restricted|limited)\s+to\b[^.\n]{0,20}\b10\s*%", "restricts rates to fixed 10% steps", True),
        (r"\btax\b[^.\n]{0,40}\b(?:requires?|needs?)\b[^.\n]{0,20}\b(?:each|every)\b[^.\n]{0,20}\b(?:owner|member)\b[^.\n]{0,20}\bapprov", "requires per-policy owner approval", True),
        (r"\b(?:tax|tax\s+receipt|receipt)\b[^.\n]{0,40}\b(?:rejected|discarded|destroyed|lost)\b[^.\n]{0,30}\bcapacity\b", "rejects a receipt on an invented capacity limit", True),
        (r"\b(?:leader|treasurer|president|officer)\b[^.\n]{0,40}\b(?:automatically|always|by\s+default)\b[^.\n]{0,40}\b(?:tax|rate|bracket)\b", "hard-codes tax authority to a fixed office", True),
        (r"\b(?:any|every)\s+(?:officer|member|leader)\b[^.\n]{0,30}\b(?:may|can)\b[^.\n]{0,20}\b(?:change|edit|set|assign)\b[^.\n]{0,30}\b(?:tax|bracket|rate)\b", "lets an unauthorized actor change tax policy", True),
    ]
    for pattern, description, skip_negation in tax_guard:
        for match in positive_matches(b09_plain, pattern, skip_negation):
            failures.append(f"[C27] B-09 {description}: {match.group(0)[:160]}")
    for req_id in [f"REQ-{i:03d}" for i in range(618, 626)]:
        row = get_row(trace, req_id)
        if not row or status_word(row[3]) != "Approved":
            failures.append(f"[C27] {req_id} must exist and be Approved (owner-authorized taxation)")
    if "AX-27" not in ax or "F-AL-006" not in formulas:
        failures.append("[C27] Taxation lacks its AX-27 contract or F-AL-006 arithmetic")

    # 09B-K final correction: failure codes, ARL naming, membership safeguard,
    # production chain and authorisation semantics.
    alf_lines = {
        code: next(
            (line for line in b09_plain.splitlines() if line.strip().startswith(f"| {code.lower()} |")),
            "",
        )
        for code in ("ALF-21", "ALF-23", "ALF-24")
    }
    if "required active alliance permission" not in alf_lines["ALF-21"]:
        failures.append("[C27] ALF-21 must be an active-permission/authorization failure")
    if "consent" in alf_lines["ALF-21"]:
        failures.append("[C27] ALF-21 still requires national-owner consent")
    if "frozen turn snapshot" not in alf_lines["ALF-23"]:
        failures.append("[C27] ALF-23 must name the frozen turn snapshot/production record")
    if "unreserved" in alf_lines["ALF-23"] or "stockpile or balance is charged" not in alf_lines["ALF-23"]:
        failures.append("[C27] ALF-23 still describes a stockpile/balance failure")
    if "alliance receiving ledger credit fails" not in alf_lines["ALF-24"]:
        failures.append("[C27] ALF-24 must cover the ARL credit failure")
    if "no destination-capacity limit exists" not in alf_lines["ALF-24"]:
        failures.append("[C27] ALF-24 must state that no destination-capacity limit exists")
    req626_row = get_row(trace, "REQ-626")
    req626_text = " ".join(req626_row) if req626_row else ""
    req626_lower = req626_text.lower()
    if "alliance receiving ledger" not in req626_lower or "accounting" not in req626_lower:
        failures.append("[C27] REQ-626 no longer names the ARL receipt/accounting record")
    if "received" not in req626_lower or "available" not in req626_lower:
        failures.append("[C27] REQ-626 no longer records the donation as RECEIVED/AVAILABLE")
    if "alliance treasury" in req626_text.lower():
        failures.append("[C27] REQ-626 still calls the ARL an alliance treasury")
    for token in (
        "Production-chain examples A–G",
        "total alliance tax is 107",
        "550 is available",
        "total ARL credit remains 50, never 100",
    ):
        if token not in formulas:
            failures.append(f"[C27] F-AL-006 lost the production-chain token '{token}'")
    if "ALF-24" not in formulas:
        failures.append("[C27] F-AL-007 lost its ALF-24 rejection set")
    ax27 = ax.get("AX-27", ("", ""))[1]
    for token in ("deducted at most once", "visible recorded 0% fallback", "post-tax net", "ALF-21", "ALF-23"):
        if token not in ax27:
            failures.append(f"[C27] AX-27 lost the 09B-K token '{token}'")
    ecm = text["b04"]
    if "Multiple-membership safeguard (`UD-040` remains Open)" not in ecm:
        failures.append("[C27] ECN-213a lost the provisional UD-040 membership safeguard")
    if "(7) write the per-event paired ledger events" not in ecm:
        failures.append("[C27] ECN-213a lost the seven-step settlement sequence")
    if "Independent per-event floors are not used" not in ecm:
        failures.append("[C27] ECN-213a lost the cumulative-accrual rule")
    if "reconcile at end of turn that the event taxes sum to $D_{a,m_a}$" not in ecm:
        failures.append("[C27] ECN-213a lost the end-of-turn cumulative reconciliation")
    if "A 100% rate leaves zero of that turn's production" not in ecm:
        failures.append("[C27] ECN-213a lost the 100% post-tax-zero rule")

    # ------------------------------------------------------------------
    # C28 - Donations are voluntary, distinct and non-withdrawable
    # ------------------------------------------------------------------
    section_has_all(
        range(188, 196),
        [
            "never mandatory",
            "never automatically withdrawn",
            "authenticated owner",
            "distinct",
            "the donor selects the asset and the amount",
            "confirmation shows the donor nation",
            "the receiving alliance",
            "irrevocable once settled",
            "lacks unreserved value",
            "idempotency key",
            "duplicate",
            "immutable receipt",
            "donation history",
            "general withdrawal",
            "ud-046",
        ],
        "C28",
    )
    donation_guard = [
        (r"\bdonations?\b[^.\n]{0,40}\b(?:is|are)\s+(?:mandatory|compulsory|automatic)\b", "makes a donation mandatory"),
        (r"\b(?:alliance|treasury)\b[^.\n]{0,40}\b(?:automatically|silently)\s+(?:withdraw|debit|deduct)", "automatically withdraws funds"),
        (r"\bcompulsory\b[^.\n]{0,30}\b(?:recorded|labelled|displayed)\s+as\s+(?:a\s+)?donation\b", "relabels compulsory deduction as a donation"),
        (r"\bdonation\b[^.\n]{0,50}\bauthori[sz]es?\b[^.\n]{0,30}\bwithdraw", "treats a donation as withdrawal authority"),
    ]
    for pattern, description in donation_guard:
        for match in positive_matches(b09_plain, pattern):
            failures.append(f"[C28] B-09 {description}: {match.group(0)[:160]}")
    for req_id in [f"REQ-{i:03d}" for i in range(626, 633)]:
        row = get_row(trace, req_id)
        if not row or status_word(row[3]) != "Approved":
            failures.append(f"[C28] {req_id} must exist and be Approved (owner-authorized donations)")
    if "AX-28" not in ax or "F-AL-007" not in formulas:
        failures.append("[C28] Donations lack their AX-28 contract or F-AL-007 arithmetic")

    # ------------------------------------------------------------------
    # C29 - ALL-093 withdrawal keeps the tombstone and independent safeguards
    # ------------------------------------------------------------------
    all093 = get_rule(b09, "ALL-093")
    if not all093:
        failures.append("[C29] ALL-093 tombstone is missing")
    else:
        for token in ("withdrawn", "d-140", "grants no right", "confiscation"):
            if token not in all093.lower():
                failures.append(f"[C29] ALL-093 tombstone lost '{token}'")
    if "protection against arbitrary confiscation" in all093.lower():
        failures.append("[C29] ALL-093 still carries the withdrawn confiscation clause")
    for rule_id in ("ALL-087", "ALL-142", "ALL-145"):
        text = get_rule(b09, rule_id).lower()
        if not text:
            failures.append(f"[C29] Independent protection {rule_id} is missing")
    for token in ("authentication", "audit", "authorization", "server-side", "transaction"):
        if token not in b09.lower():
            failures.append(f"[C29] B-09 lost its independent security/audit anchor '{token}'")

    # ------------------------------------------------------------------
    # C30 - Separate Alliance treaty object, explicit consent and NAP
    # ------------------------------------------------------------------
    section_has_all(
        range(196, 209),
        [
            "alliance_agreement_id",
            "at-t01",
            "at-t05",
            "explicitly consent",
            "silence",
            "diplomatic delegation",
            "server-side",
            "every attack method",
            "rejected before execution",
            "clear reason",
            "audit event",
            "no discretionary exception",
            "no automatic war entry",
            "each alliance's approval",
            "covered-nation scope",
            "activation turn",
            "expiry or open-ended term",
            "termination or breach",
            "join",
            "leave",
            "transfer",
            "dissolution",
            "multiple alliances",
            "non-covered member",
            "must not be refused admission",
            "as a whole",
            "no covered member of b may attack",
            "descriptive only",
        ],
        "C30",
    )
    all199 = get_rule(b09, "ALL-199").lower()
    for token in ("must explicitly consent", "silence", "never counts as consent"):
        if token not in all199:
            failures.append(f"[C30] ALL-199 lost '{token}' (nation consent must be explicit)")
    for pattern, description in [
        (r"\balliance\s+(?:treaty|agreement)\b[^.\n]{0,50}\breuse[sd]?\b[^.\n]{0,30}\bb-08\b", "reuses the B-08 object"),
        (r"\balliance\s+(?:leader|officer|majority)\b[^.\n]{0,40}\b(?:consents?|signs?)\b[^.\n]{0,30}\bfor\s+(?:a|the)\s+nation\b", "lets an alliance actor consent for a nation"),
        (r"\bnap\b[^.\n]{0,40}\b(?:waived|exception|opt-out|opt out)\b", "permits a NAP waiver"),
        (r"\b(?:refus(?:e|ed|es|ing)|den(?:y|ied|ies|ying)|bar(?:s|red)?|block\w*)\b[^.\n]{0,30}\badmission\b[^.\n]{0,60}\b(?:declin\w*|withhold\w*|refus\w*)\b[^.\n]{0,40}\b(?:nap|consent|treaty)\b", "refuses admission for withheld treaty consent"),
        (r"\bjoining\b[^.\n]{0,40}\b(?:is|becomes?|be)\s+(?:automatically\s+)?(?:covered|added)\b", "extends NAP coverage automatically to a joiner"),
        (r"\b(?:player-authored|free[- ]text|custom)\b[^.\n]{0,40}\b(?:terms?|wording|prose|clauses?)\b[^.\n]{0,40}\b(?:parsed|executed|enforced|becomes?|creates?)\b[^.\n]{0,30}\b(?:rule|effect|attack|restriction)\b", "makes custom treaty prose executable"),
    ]:
        for match in positive_matches(b09_plain, pattern):
            failures.append(f"[C30] B-09 {description}: {match.group(0)[:160]}")
    for req_id in [f"REQ-{i:03d}" for i in range(633, 645)]:
        row = get_row(trace, req_id)
        if not row or status_word(row[3]) != "Approved":
            failures.append(f"[C30] {req_id} must exist and be Approved (owner-authorized treaty framework)")
    if "AX-29" not in ax:
        failures.append("[C30] The Alliance treaty framework lacks AX-29")

    # ------------------------------------------------------------------
    # C31 - Same-Alliance attack ban is mandatory and server-side
    # ------------------------------------------------------------------
    section_has_all(
        range(209, 216),
        [
            "share at least one active alliance",
            "must not attack each other",
            "independent of the alliance constitution",
            "every attack method",
            "one canonical server-side",
            "again at execution",
            "fails closed",
            "join",
            "leave",
            "transfer",
            "multiple alliances",
            "prompt 10",
            "no confiscation",
            "mandatory audit event",
            "leaving a shared alliance does not bypass",
        ],
        "C31",
    )
    all212 = get_rule(b09, "ALL-212").lower()
    for token in ("join", "leave", "transfer", "expulsion", "dissolution", "rejoin", "multiple alliances"):
        if not re.search(rf"\b{re.escape(token)}\b", all212):
            failures.append(f"[C31] ALL-212 lost membership-change token '{token}'")
    for pattern, description in [
        (r"\bsame[- ]alliance\b[^.\n]{0,40}\b(?:may|can)\s+(?:opt out|waive|disable)\b", "permits opting out of the same-Alliance ban"),
        (r"\b(?:ui|client)[- ](?:only|side)\b[^.\n]{0,40}\b(?:enforcement|check)\b", "relies on UI/client enforcement"),
        (r"\bsame[- ]alliance\b[^.\n]{0,40}\b(?:is|are)\s+(?:optional|candidate|recommended)\b", "makes the same-Alliance ban optional"),
    ]:
        for match in positive_matches(b09_plain, pattern):
            failures.append(f"[C31] B-09 {description}: {match.group(0)[:160]}")
    for req_id in ("REQ-645", "REQ-646", "REQ-647"):
        row = get_row(trace, req_id)
        if not row or status_word(row[3]) != "Approved":
            failures.append(f"[C31] {req_id} must exist and be Approved (same-Alliance attack ban)")
    if "AX-30" not in ax or "DD-163" not in dd:
        failures.append("[C31] The same-Alliance ban lacks AX-30 or DD-163")

    # ------------------------------------------------------------------
    # C32 - ARL receipt/accounting and purpose-limited operational funding
    # ------------------------------------------------------------------
    for rule_id in range(220, 227):
        if not get_rule(b09, f"ALL-{rule_id:03d}"):
            failures.append(f"[C32] Operational funding rule ALL-{rule_id:03d} is missing")
    section_has_all(
        range(220, 227),
        [
            "purpose-limited",
            "aop-01",
            "aop-02",
            "aop-03",
            "aop-04",
            "registered platform cost sink",
            "authorize_operational_expenditure",
            "no fixed office",
            "alf-27",
            "alf-28",
            "alf-29",
            "aud-al-019",
            "idempotency",
            "received",
            "available",
            "reserved",
            "expended",
            "no general withdrawal",
            "no negative balance",
            "no capacity limit",
            "may not pay a general withdrawal",
        ],
        "C32",
    )
    for token in (
        "received",
        "reserved",
        "expended",
        "avl",
        "rsv",
        "exp",
        "rec",
        "registered platform cost",
        "no ownership",
        "ud-046",
    ):
        if token.lower() not in formulas.lower():
            failures.append(f"[C32] F-AL-008 lost the accounting token '{token}'")
    for req_id in (f"REQ-{i:03d}" for i in range(648, 654)):
        row = get_row(trace, req_id)
        if not row or status_word(row[3]) != "Approved":
            failures.append(f"[C32] {req_id} must exist and be Approved (operational funding)")
    ax27 = ax.get("AX-27", ("", ""))[1].lower()
    ax28 = ax.get("AX-28", ("", ""))[1].lower()
    for token in ("received", "available", "reserved", "expended", "operational"):
        if token not in ax27:
            failures.append(f"[C32] AX-27 lost the ARL accounting token '{token}'")
    for token in ("received", "available", "operational", "no general withdrawal"):
        if token not in ax28:
            failures.append(f"[C32] AX-28 lost the ARL/donation token '{token}'")
    ud046_row = get_row(b09, "UD-046")
    ud046_text = " ".join(ud046_row).lower() if ud046_row else ""
    ud046_status = ud046_row[3].lower() if ud046_row and len(ud046_row) > 3 else ""
    if "open" not in ud046_status:
        failures.append("[C32] UD-046 is no longer recorded Open")
    for token in ("ownership", "custody", "general withdrawal", "capacity"):
        if token not in ud046_text:
            failures.append(f"[C32] UD-046 lost its reserved '{token}' subject")
    ud045_row = get_row(b09, "UD-045")
    ud045_text = " ".join(ud045_row).lower() if ud045_row else ""
    ud045_status = ud045_row[3].lower() if ud045_row and len(ud045_row) > 3 else ""
    if "open" not in ud045_status:
        failures.append("[C32] UD-045 is no longer recorded Open")
    for token in (
        "bracket creation",
        "crowns and resource rate",
        "member bracket assignment",
        "reporting access",
        "still open",
    ):
        if token not in ud045_text:
            failures.append(f"[C32] UD-045 lost its narrow authorization token '{token}'")
    for pattern, description in [
        (r"\boperational\s+(?:funding|expenditure|expense)\b[^.\n]{0,50}\b(?:is|are)\s+(?:a\s+)?general\s+withdrawal\b", "collapses operational funding into a general withdrawal"),
        (r"\b(?:may|can|shall)\s+(?:pay|distribute|transfer)\b[^.\n]{0,40}\b(?:to\s+)?(?:a\s+)?(?:member|nation|officer|player|external\s+recipient)\b", "authorizes a player payment"),
        (r"\boperational\s+(?:funding|expense)\b[^.\n]{0,60}\binvented\s+capacity\b", "reintroduces an invented capacity limit"),
        (r"\b(?:general\s+withdrawal|distribution)\b[^.\n]{0,40}\b(?:is|are)\s+(?:approved|authorized|available)\b", "claims an approved general withdrawal"),
    ]:
        for match in positive_matches(b09_plain, pattern):
            failures.append(f"[C32] B-09 {description}: {match.group(0)[:160]}")

    # ------------------------------------------------------------------
    # C33 - Registered record-only and NAP treaty effects
    # ------------------------------------------------------------------
    all197 = get_rule(b09, "ALL-197").lower()
    all203 = get_rule(b09, "ALL-203").lower()
    for token in (
        "at-e00",
        "at-e01",
        "record-only",
        "valid diplomatic record",
        "executes no mechanic",
        "unknown, unregistered",
        "alf-25",
        "free text is never parsed",
    ):
        if token not in all197:
            failures.append(f"[C33] ALL-197 lost the structured-effect token '{token}'")
    for token in (
        "only `at-t01` selecting `at-e01`",
        "at-t02",
        "at-t03",
        "at-t04",
        "at-t05",
        "execute no mechanic",
    ):
        if token not in all203:
            failures.append(f"[C33] ALL-203 lost the effect-scope token '{token}'")
    for token in ("at-e00", "at-e01", "record-only", "structured", "consent"):
        if token not in contracts.lower():
            failures.append(f"[C33] AX-29 lost the structured-effect token '{token}'")
    for req_id in ("REQ-634", "REQ-640"):
        row = get_row(trace, req_id)
        if not row or status_word(row[3]) != "Approved":
            failures.append(f"[C33] {req_id} must exist and be Approved (treaty effects)")
    if "at-e00" not in formulas.lower() and "at-e01" not in formulas.lower():
        # Effects are not arithmetic; the formula register is not required to
        # duplicate the catalogue. This records the intentional absence.
        pass
    record_only_contradictions = [
        r"\brecord-only\b[^.\n]{0,70}\b(?:rejected|invalid|unsupported|not\s+stored|not\s+a\s+valid\s+treaty)\b",
        r"\beffectless\b[^.\n]{0,70}\b(?:rejected|invalid|unsupported|not\s+stored|not\s+a\s+valid\s+treaty)\b",
        r"\bno\s+record-only\s+(?:treaty|effect)\b",
    ]
    for pattern in record_only_contradictions:
        for match in re.finditer(pattern, b09_plain, re.I):
            segment = match.group(0)
            if re.search(r"\b(?:not|never|no)\b", segment, re.I) and not re.search(
                r"\b(?:rejected|invalid|unsupported|not\s+stored)\b", segment, re.I
            ):
                continue
            failures.append(
                f"[C33] B-09 contradicts the record-only catalogue: {segment[:160]}"
            )
    for pattern, description in [
        (r"\bat-t0[2-5]\b[^.\n]{0,60}\b(?:blocks?|prohibits?|prevents?)\b[^.\n]{0,30}\battack", "makes a non-NAP treaty restrict attacks"),
        (r"\b(?:free[- ]text|custom\s+wording|player-authored\s+terms)\b[^.\n]{0,60}\b(?:parsed|executed|enforced)\b", "makes treaty prose executable"),
    ]:
        for match in positive_matches(b09_plain, pattern):
            failures.append(f"[C33] B-09 {description}: {match.group(0)[:160]}")

    # ------------------------------------------------------------------
    # C34 - National/municipal tax settings, authorized withholding and
    #       the three distinct transfer classes (Prompt 09B-L)
    # ------------------------------------------------------------------
    all006 = get_rule(b09, "ALL-006").lower()
    all007 = get_rule(b09, "ALL-007").lower()
    all008 = get_rule(b09, "ALL-008").lower()
    for token in (
        "national",
        "municipal",
        "tax rate",
        "cannot alter",
        "automatic per-turn production tax",
        "current-turn production",
        "opening balance",
        "existing stockpile",
        "alliance receiving ledger",
        "no ownership interest",
        "ud-046",
    ):
        if token not in all006:
            failures.append(f"[C34] ALL-006 lost the tax-boundary token '{token}'")
    for token in (
        "authorized automatic withholding",
        "current-turn production",
        "not a forced spend",
        "does not permit confiscation",
        "access to national stockpiles",
        "unauthorized withdrawals",
        "unapproved spending or transfers",
        "change to national financial policy",
    ):
        if token not in all007:
            failures.append(f"[C34] ALL-007 lost the non-interference token '{token}'")
    for token in (
        "automatic alliance tax withholding",
        "current-turn production",
        "voluntary donations",
        "every other transfer",
        "voluntary and explicit",
        "purpose-limited operational funding",
        "debits only the arl",
    ):
        if token not in all008:
            failures.append(f"[C34] ALL-008 lost the transfer-class token '{token}'")
    tax_boundary_guards = [
        (
            r"\balliance\b[^.\n]{0,40}\b(?:sets?|changes?|alters?)\b[^.\n]{0,30}\b(?:national|municipal)\b[^.\n]{0,20}\btax\b",
            "lets an alliance set or change national or municipal tax rates",
        ),
        (
            r"\balliance\b[^.\n]{0,50}\btax\b[^.\n]{0,40}\b(?:prohibits?|bans?|forbids?)\b[^.\n]{0,20}\bautomatic\b",
            "prohibits the authorized automatic withholding",
        ),
        (
            r"\bautomatic\b[^.\n]{0,30}\bwithholding\b[^.\n]{0,40}\b(?:is|constitutes?)\s+(?:a\s+)?confiscation\b",
            "misclassifies authorized automatic withholding as confiscation",
        ),
        (
            r"\bautomatic\s+(?:alliance\s+)?tax\b[^.\n]{0,40}\b(?:is|are)\s+(?:a\s+)?(?:donation|voluntary)\b",
            "misclassifies automatic tax as a voluntary donation",
        ),
    ]
    for pattern, description in tax_boundary_guards:
        for match in positive_matches(b09_plain, pattern):
            failures.append(f"[C34] B-09 {description}: {match.group(0)[:160]}")

    return failures


def run_checks_with_review(base_dir: Path | None = None) -> tuple[list[str], list[str]]:
    """Return confirmed failures and uncertain findings that need manual review.

    Review findings are deliberately not failures: they are wording that may
    assert an owner-reserved appeal policy but that the validator cannot
    classify with confidence. A caller must surface them rather than treating
    the run as a silent pass. This is a bounded classifier, not exhaustive
    natural-language detection.
    """
    reviews: list[str] = []
    failures = run_checks(base_dir, reviews)
    return failures, reviews


def main() -> int:
    print("=" * 72)
    print("Nation Supremacy - Prompt 09B-P Alliance Semantic Validator")
    print("=" * 72)
    failures, reviews = run_checks_with_review()
    if failures:
        print(f"[FAIL] {len(failures)} semantic defect(s):")
        for index, failure in enumerate(failures, 1):
            print(f"  {index}. {failure.encode('ascii', 'replace').decode('ascii')}")
    if reviews:
        print(f"[REVIEW] {len(reviews)} uncertain finding(s) require manual review:")
        for index, review in enumerate(reviews, 1):
            print(f"  {index}. {review.encode('ascii', 'replace').decode('ascii')}")
    if failures or reviews:
        print("[NOT PASSED] Confirmed defects fail; review findings must not pass silently.")
        return 1
    print("[PASS] All 34 semantic checks passed with no review findings.")
    print("Status: Phase 09B Alliance specification and documentation accepted at the specification/documentation level; Prompt 09C is complete at the specification/documentation level; Prompt 10A research, the Prompt 10B specification and Prompt 10C workflows and acceptance are complete; Prompt 11A research and design foundations is complete at the research/design-foundations level (2026-11-05); Prompt 11B is complete at the system-specification level (2026-11-05), and its 11B-C2 correction preserves the original 52-gate crosswalk (52/52 PASS) with 61 separate validator checks; independent acceptance of 11B-C2 was recorded by C3 on 2026-11-05; Prompt 11C is complete at the specification/documentation level (2026-11-06, 20 gates at 12 PASS / 8 PARTIAL with 31 separate validator checks), and Prompt 12A is complete at the research and design-foundations level (2026-11-06; reconciled by the 12A-C1 pass on 2026-11-07; 22 gates at 15 PASS / 7 PARTIAL with 45 separate validator checks), and Prompt 12B is complete at the specification/documentation level (2026-11-07), Prompt 12C is complete at the specification/documentation level (2026-11-10) and was owner-accepted on 2026-11-11, Prompt 13A is complete at the research/design-foundations level (2026-11-11) and owner accepted per the 13B instruction, Prompt 13B is complete at the specification/documentation level (2026-11-13), and Prompt 13C remains next and needs separate owner authorization.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
