# Autonomous decision policy — Nation Supremacy

**Version:** 1.0 · **Created:** 2026-10-23 · **Status:** **Confirmed** project policy (D-014)
**Applies to:** every human or AI session working on this repository.
**Read with:** [AI_CONTEXT.md](AI_CONTEXT.md) · [AI_HANDOFF.md](AI_HANDOFF.md) · [DECISIONS.md](DECISIONS.md)

---

## 1. Purpose

This project is developed by AI sessions that cannot rely on the owner being present for every design choice. The policy exists so that ordinary decisions are **made, documented and carried forward** instead of stalling the roadmap.

It does not remove owner authority over the project's fixed constraints, spending, legal commitments or destructive external actions. It removes the habit of asking the owner to choose routine game features.

**The one-line rule:** *research it, decide it, write it down, continue — unless the decision is a fixed constraint, a cost, a legal commitment or an irreversible external action.*

---

## 2. Decision categories

| Category | What it covers | Who decides | How it is recorded |
|---|---|---|---|
| **A — Fixed constraints** | Browser delivery; original identity; mapless symbolic world; 2-hour UTC cadence; one account per person; Cloudflare Pages + Supabase; free-first ₹0 target; no paid dependency; the Stage 1/2/3 sequencing | **Owner only.** An AI may not override, relax or reinterpret one | [DECISIONS.md](DECISIONS.md) already records them; a change needs an explicit owner instruction and a new D-entry |
| **B — Ordinary design and implementation decisions** | Game mechanics, formulas, UX, progression, default settings, register structure, documentation conventions, test design, internal implementation choices within the fixed architecture | **The working AI decides** | A new `D-` entry in [DECISIONS.md](DECISIONS.md) with rationale, evidence and consequences; affected registers updated |
| **C — Provisional decisions** | A decision is genuinely blocked by missing evidence, an unmeasured platform limit, a required simulation, or a balance question that only playtesting can settle | The AI chooses a **safe working default** and records the exact evidence that would confirm or replace it | Status **Provisional** in DECISIONS.md / DD / UD, with the owner prompt or test named |
| **D — External, costly or irreversible actions** | Spending money; paid plans; contracts; legal representations; credentials the AI does not hold; deletion of external data; destructive production actions; publishing/deploying on the owner's behalf without authorization | **Owner only** | Record the blocked action, what is needed, and continue all independent work |

**Category C is not a synonym for "ask the owner".** It means "decided provisionally, with a named test". **Category D is not a synonym for "unclear design".** It means an action the AI genuinely cannot take.

---

## 3. The procedure

1. **State the question** in one sentence. If it is not a question, stop.
2. **Name the realistic alternatives** (two or three, not a menu of ten).
3. **Research when the answer depends on external facts** — provider limits, security guidance, browser behaviour, genre evidence. Prefer official provider documentation. Multiple sources for disputed or consequential points.
4. **Check the fixed constraints first** (Category A). A proposal that violates one is not a candidate.
5. **Evaluate against the project's order of priorities** (§4).
6. **Choose.** Prefer the simplest coherent option that can be built and operated by an AI-assisted workflow.
7. **Record** the decision, the alternatives rejected, the evidence, the trade-offs, the confidence, and the condition that would reopen it.
8. **Propagate** it to the owning document and the registers (requirements, DD/UD, outline if scope changes).
9. **Continue** the assigned prompt. Do not end the turn to ask for approval of a Category B choice.

### Research record (compact)

For decisions where external facts mattered, record:

- Question.
- Alternatives considered.
- Selected option.
- Reason.
- Sources / evidence (URLs or report sections).
- Trade-offs.
- Confidence: high / medium / low.
- What would justify revisiting.

Do not write a research essay for a naming or layout choice. Do not claim research that was not performed. If web access is unavailable, say so and proceed on repository evidence, lowering confidence.

---

## 4. Priority order for choosing

1. The owner's explicit requirements and the fixed constraints.
2. Security, privacy, data integrity, fair play and resistance to exploitation.
3. Coherent, enjoyable long-term gameplay.
4. Simplicity and maintainability for an AI-assisted build.
5. Free-first compatibility with Cloudflare Pages + Supabase.
6. Performance, reliability, scale, accessibility, debuggability.
7. Transparent rules, predictable outcomes, explainable feedback.
8. Reversibility when evidence is weak or the cost of reversal is high.
9. No unnecessary complexity, dependencies or features.
10. Record residual risk honestly rather than hiding uncertainty.

A feature is not chosen because it is popular or because another game has it. The rationale must say why it suits **Nation Supremacy**.

---

## 5. What "approved" means

- A **Category B** decision may be recorded as **Confirmed** in [DECISIONS.md](DECISIONS.md) by the working AI, with the rationale and evidence. It is then binding on later prompts until superseded.
- A **Category C** decision is recorded as **Provisional** with its missing evidence. It does not block unrelated work; it blocks only the rule that depends on it.
- **Approval of a rule is not implementation.** "Confirmed" never means built, tested, deployed or balanced. The status vocabulary in the requirements register keeps *specified*, *implemented*, *validated* and *released* separate.
- Historical decisions are **superseded, never rewritten**. Keep the old row and point to its successor. A dated snapshot (a report, a progress-log section, an earlier handoff) stays historical and must be **labelled as a snapshot**, never edited into a false current claim and never read as a live instruction.
- A **future prompt is not complete** because its topic, design or policy has been discussed or decided elsewhere. Mark it complete only when its own deliverables exist and its checks have run.

### What must never happen

- Declaring a rule approved without recording it in DECISIONS.md.
- Using "the design says" to bypass a fixed constraint.
- Promoting a proposed value to proven without testing.
- Asking the owner to choose an ordinary mechanic, UX pattern, formula shape or document convention.
- Creating a second register for a decision that already has an ID.
- Silently changing the 2-hour cadence, the mapless world, the account policy or the architecture.

---

## 6. When stopping **is** correct

Stop and ask only when:

- the action needs money, a paid plan, a contract or legal acceptance;
- the action needs credentials/permissions the session does not have;
- the action is destructive to external data or production;
- two fixed constraints genuinely conflict and no reversible resolution exists;
- the owner's explicit instruction is ambiguous about which of two materially different products is wanted.

Even then: finish every independent part of the task first, state exactly what is blocked, and leave the project consistent.

---

## 7. Prompt-start and prompt-end duties

**At the start of any prompt:** read the continuity files, the roadmap and the owning design document; check the decision log for entries that already answer the question; verify the repository rather than trusting the prompt's summary.

**At the end of any prompt:** update the owning document, the registers, the progress log and the handoff; record every Category B/C decision; run the validators; state actual results. The handoff must name the **next action** and only that action; a later session resumes from it rather than from a remembered conversation. Every remaining Open/Provisional/Deferred/Blocked item must keep its precise question, reason and next test or owner.

---

## 8. Change control for this policy

This policy is itself a project decision (D-014). Changing it requires a new D-entry that names this file and explains the change. A session may not quietly loosen it to avoid documenting a decision.
