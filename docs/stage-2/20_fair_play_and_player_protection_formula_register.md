# B-12 fair play, privacy, moderation and administration — formula and parameter register

**Version:** 1.0 · **Created:** 2026-11-07 · **Stage 2, Prompt 12B**
**Status:** **Specification complete at the documentation level. Unimplemented, uncalibrated and untested.**
**Authority.** This register is the authoritative statement of every B-12 calculation. The [B-12 rulebook](20_fair_play_and_player_protection.md) defines the rules; where prose and register diverge, this register governs and the rulebook is corrected.
**Companions.** [B-12 rulebook](20_fair_play_and_player_protection.md) · [B-12 requirements](20_fair_play_and_player_protection_requirements.md) · [B-12 acceptance](20_fair_play_and_player_protection_acceptance.md) · [12A research](research/12A_fair_play_privacy_moderation_administration_research.md) · [requirements](03_requirements_traceability.md) · [decisions](../DECISIONS.md).

**Status of values.** No B-12 numeric value is approved. Every parameter is one of: **Structural** (the expression is fixed and contains no unapproved constant), **Structural + provisional parameter** (the expression is fixed; the named constant awaits Prompt 14, the owner or a measured test), **Provisional** (the whole calculation awaits calibration), **Owner decision required**, **Legal review required**, or **Capacity validation required**. A structural formula may contain a provisional constant; the structure is fixed, the constant is not.

---

## 1. Formula inventory

| ID | Name | Domain | Status | Main rule |
|---|---|---|---|---|
| `F-FP-001` | Severity index | Sanction | Structural + provisional weights | MOD-039 |
| `F-FP-002` | Correction amount | Correction | Structural + provisional valuation | MOD-053 |
| `F-FP-003` | Illicit benefit estimate | Correction | Structural + provisional valuation | COR-003 |
| `F-FP-004` | Restitution priority | Correction | Structural | COR-011 |
| `F-FP-005` | Restriction duration | Sanction | Provisional | MOD-012, MOD-037 |
| `F-FP-006` | Appeal filing window | Appeal | Owner decision required | MOD-050 |
| `F-FP-007` | Evidence sufficiency predicate | Evidence | Structural | EVD-010 |
| `F-FP-008` | Report cluster key | Reporting | Structural + provisional window | MOD-003 |
| `F-FP-009` | Rate allowance | Security | Structural + provisional cap and factor | SEC-007 |
| `F-FP-010` | Idempotency retention | Security | Structural | SEC-003 |
| `F-FP-011` | Recidivism multiplier | Sanction | Structural + provisional weights | MOD-039 |
| `F-FP-012` | Audit digest chain | Audit | Structural | EVD-031 |
| `F-FP-013` | Verification interval | Audit | Provisional | EVD-032 |
| `F-FP-014` | Correction conservation identity | Correction | Structural | COR-003 |
| `F-FP-015` | Compensation cap | Correction | Provisional | COR-006, MOD-056 |
| `F-FP-016` | Emergency expiry | Administration | Structural + provisional duration | MOD-026 |

**Counts.** 16 formula IDs, all active. **Structural, no unapproved constant: 5** — `F-FP-004`, `007`, `010`, `012`, `014`. **Structural + provisional parameter: 7** — `001`, `002`, `003`, `008`, `009`, `011`, `016`. **Provisional: 3** — `005`, `013`, `015`. **Owner decision required: 1** — `006`. Total 16. Duplicate identifiers: 0. Undefined variables: 0. **Parameters: 14** (`FP-P01`…`FP-P14`), none calibrated.

---

## 2. Formula records

Every record uses the twenty mandatory fields. A value marked **provisional** is not a launch threshold.

### F-FP-001 — Severity index

1. **Purpose.** Produce an ordinal severity input for tier selection, excluding repetition. Repetition is applied exactly once, by `F-FP-011`.
2. **Inputs.** Base class severity `S_c` (Annex A), proven impact `I_p`, intent factor `K`, mitigation factor `M`.
3. **Units.** Dimensionless ordinal points.
4. **Expression.** `SEV = S_c + I_p + K − M`.
5. **Variables.** `S_c` ∈ {1,2,3,4,5}; `I_p` ∈ {0,1,2,3}; `K` ∈ {0,1,2}; `M` ∈ {0,1,2}. There is no repetition term here.
6. **Constraints.** All inputs are integers from the stated sets. `SEV` floors at 0. An unconfirmed prior never enters this formula.
7. **Boundary behaviour.** `SEV = 0` maps to `T0`; `1–3` to `T1`; `4–6` to `T2`; `7–9` to `T3`; `10–12` to `T4`; `13+` to `T5`, subject to MOD-037 authority.
8. **Rounding.** None; integer arithmetic.
9. **Null behaviour.** A missing proven impact is `I_p = 0` only when Annex A does not require impact; otherwise the calculation returns `INCONCLUSIVE`.
10. **Exceptional conditions.** A `T5` result still requires `E3`, owner-authorized threshold and independent review where available.
11. **Dependencies.** Annex A, MOD-036…MOD-039, `F-FP-011`, `UD-053`.
12. **Worked example.** `S_c = 3`, `I_p = 1`, `K = 1`, `M = 0` → `SEV = 5` → `T2`. With one confirmed prior, `F-FP-011` then applies the single repetition adjustment.
13. **Verification.** Specification review and case-table fixture; no runtime test.
14. **Parameter status.** Weights are provisional; Prompt 14 or the owner may calibrate.
15. **Owner.** Owner (`UD-053`), with Prompt 14 support.
16. **Affected rules.** MOD-039, MOD-060.
17. **Affected requirements.** `REQ-812`, `REQ-813`, `REQ-821`.
18. **Revision.** 1.1, 2026-11-07 (12B-C1: removed the duplicate repetition term; `F-FP-011` is the sole repetition adjustment).
19. **Review trigger.** Calibration evidence, appeal-overturn data or an owner decision.
20. **Approval.** Not approved; structural with provisional weights.

### F-FP-002 — Correction amount

1. **Purpose.** Remove the excess value an invalid effect produced, restoring the counterfactual lawful state. A shortfall against the lawful state is a loss and is handled by compensation (`F-FP-015`), not by this removal formula.
2. **Inputs.** Observed post-effect value `V_obs`, lawful counterfactual `V_law`, illicit benefit `B_i`.
3. **Units.** The owning ledger's value unit.
4. **Expression.** `C = min(max(V_obs − V_law, 0), B_i)`.
5. **Variables.** `V_obs` is the account value actually observed after the invalid effect; `V_law` is computed by the owning subsystem from the last lawful state; `B_i` is `F-FP-003`. The subtraction is **observed minus lawful**: a positive difference is the excess to remove.
6. **Constraints.** `C ≥ 0`; `C` never exceeds `B_i`; no negative balance is created.
7. **Boundary behaviour.** If `V_obs ≤ V_law`, `C = 0` (no excess exists). If the account holds less than `C`, the correction floors at the held value and records the shortfall (`COR-012`).
8. **Rounding.** The owning ledger's minor unit; no fractional unit.
9. **Null behaviour.** A missing lawful counterfactual returns `NO_CALCULATION` and an incident, never zero.
10. **Exceptional conditions.** Valuation disputes are resolved by the owning subsystem's published rule, not by administrator discretion.
11. **Dependencies.** B-04 ledger, `F-FP-003`, `F-FP-014`, COR-001…COR-017.
12. **Worked examples.** No discrepancy: `V_law = 100`, `V_obs = 100`, `B_i = 0` → `C = 0`. Positive discrepancy: `V_law = 100`, `V_obs = 140`, `B_i = 40` → `C = min(max(40, 0), 40) = 40`. Negative discrepancy (a loss, not an excess): `V_law = 100`, `V_obs = 80`, `B_i = 0` → `C = 0`; any restoration is compensation under `F-FP-015`. Cap binding: `V_law = 100`, `V_obs = 200`, `B_i = 40` → `C = 40`. Missing input: `V_law` absent → `NO_CALCULATION`.
13. **Verification.** Ledger simulation fixture; no runtime test.
14. **Parameter status.** Provisional valuation inputs.
15. **Owner.** B-04 for value, B-12 for the correction instruction.
16. **Affected rules.** MOD-051…MOD-055, COR-002…COR-012.
17. **Affected requirements.** `REQ-817`, `REQ-836`, `REQ-845`.
18. **Revision.** 1.1, 2026-11-07 (12B-C1: corrected subtraction direction and boundary statement; the 1.0 expression contradicted its own worked example).
19. **Review trigger.** A ledger-valuation decision or a correction dispute.
20. **Approval.** Not approved.

### F-FP-003 — Illicit benefit estimate

1. **Purpose.** Bound the value obtained through an invalid effect.
2. **Inputs.** The set of linked transactions `T`, each with value delta `d_t` and lawful entitlement `e_t`.
3. **Units.** The owning ledger's value unit.
4. **Expression.** `B_i = Σ max(d_t − e_t, 0)` over `T`.
5. **Variables.** `T` is the recorded flow set; `d_t` is the observed delta; `e_t` is the delta the published rules would have produced.
6. **Constraints.** Only transactions proved linked to the case are included. Transfers between innocent third parties are excluded unless the record proves the flow.
7. **Boundary behaviour.** No linked transactions → `B_i = 0`, no correction.
8. **Rounding.** Minor unit.
9. **Null behaviour.** An unvaluable transaction returns `INCONCLUSIVE` for that leg; no estimate is fabricated.
10. **Exceptional conditions.** A market-priced asset uses the owning market's recorded price at the transaction boundary.
11. **Dependencies.** B-04, B-07, COR-003.
12. **Worked example.** Two linked grants of 20 and 10 with zero entitlement → `B_i = 30`.
13. **Verification.** Flow-set fixture and ledger reconciliation.
14. **Parameter status.** Structural with provisional valuation.
15. **Owner.** B-04 and B-12.
16. **Affected rules.** COR-003, COR-006, COR-011.
17. **Affected requirements.** `REQ-782`, `REQ-817`, `REQ-845`.
18. **Revision.** 1.0.
19. **Review trigger.** New ledger event type or valuation rule.
20. **Approval.** Not approved.

### F-FP-004 — Restitution priority

1. **Purpose.** Order recovery when multiple corrections affect one account.
2. **Inputs.** Correction records with case order `n`, type `y`, and amount `a`.
3. **Units.** Order position.
4. **Expression.** Sort by `(case_closed_turn, n, type_rank)` ascending, where `type_rank` is `REVERSAL=1`, `CORRECTION=2`, `ILLICIT_REMOVAL=3`, `COMPENSATION=4`, `ADMIN_ADJUSTMENT=5`.
5. **Variables.** `case_closed_turn` is the boundary at which the decision became final.
6. **Constraints.** No correction reorders a closed turn; all apply at the next valid boundary.
7. **Boundary behaviour.** Ties use the original transaction ID ascending.
8. **Rounding.** None.
9. **Null behaviour.** A missing case turn returns `HOLD`, not a guessed order.
10. **Exceptional conditions.** A legal hold suspends application until released.
11. **Dependencies.** COR-007, COR-011.
12. **Worked example.** Case A closes at turn 100, case B at 101 → A applies first.
13. **Verification.** Ordered ledger fixture.
14. **Parameter status.** Structural.
15. **Owner.** B-12 and B-04.
16. **Affected rules.** COR-007, COR-011, COR-017.
17. **Affected requirements.** `REQ-836`, `REQ-865`.
18. **Revision.** 1.0.
19. **Review trigger.** A conflicting-correction incident.
20. **Approval.** Not approved.

### F-FP-005 — Restriction duration

1. **Purpose.** Express a temporary restriction in turn boundaries.
2. **Inputs.** Tier `T`, base turns `D_base(T)`, extension count `x`.
3. **Units.** Turn boundaries.
4. **Expression.** `D = D_base(T) × (1 + x)`, capped at the tier maximum `D_max(T)`.
5. **Variables.** `D_base` and `D_max` are provisional owner parameters (`UD-053`).
6. **Constraints.** `D` is an integer ≥ 1. `T1` is a warning with no duration. `T4`/`T5` require owner authority.
7. **Boundary behaviour.** A duration ending between boundaries ends at the next boundary.
8. **Rounding.** Ceiling to the next whole turn.
9. **Null behaviour.** An unapproved tier duration returns `PROVISIONAL_BLOCK`, not a default.
10. **Exceptional conditions.** Emergency measures use `F-FP-016`.
11. **Dependencies.** MOD-036…MOD-041, `UD-053`.
12. **Worked example.** `D_base(T2)=12`, `x=0` → 12 turns.
13. **Verification.** Boundary fixture.
14. **Parameter status.** Provisional.
15. **Owner.** Owner (`UD-053`).
16. **Affected rules.** MOD-012, MOD-037, MOD-040, MOD-041.
17. **Affected requirements.** `REQ-812`, `REQ-821`, `REQ-833`.
18. **Revision.** 1.0.
19. **Review trigger.** Owner decision or appeal-capacity evidence.
20. **Approval.** Not approved.

### F-FP-006 — Appeal filing window

1. **Purpose.** Define the structural filing window.
2. **Inputs.** Notice turn `t_n`, window turns `W`.
3. **Units.** Turn boundaries.
4. **Expression.** `t_close = t_n + W`.
5. **Variables.** `W` is an owner parameter (`UD-059`).
6. **Constraints.** `W ≥ 1`; the window includes the notice turn.
7. **Boundary behaviour.** A filing at `t_close` is in time; later is out of time unless an outage extension applies.
8. **Rounding.** Whole turns.
9. **Null behaviour.** An unapproved `W` returns `PROVISIONAL_BLOCK`.
10. **Exceptional conditions.** A recorded service outage extends `t_close` by the outage's turn count (`FR-10`).
11. **Dependencies.** MOD-042, MOD-050, `UD-059`.
12. **Worked example.** Notice at 200, `W = 24` → close at 224.
13. **Verification.** Boundary fixture.
14. **Parameter status.** Owner decision required.
15. **Owner.** Owner (`UD-059`).
16. **Affected rules.** MOD-042, MOD-050.
17. **Affected requirements.** `REQ-833`, `REQ-834`.
18. **Revision.** 1.0.
19. **Review trigger.** Owner decision.
20. **Approval.** Not approved.

### F-FP-007 — Evidence sufficiency predicate

1. **Purpose.** Decide whether a claim may proceed to a consequence.
2. **Inputs.** Evidence state `E`, independent source count `n_i`, non-behavioural flag `b`, claim type `c`.
3. **Units.** Boolean.
4. **Expression.** `SUFFICIENT(c) = (c = correction ∧ E ≥ E2) ∨ (c = conduct ∧ E = E3 ∧ n_i ≥ 2 ∧ b = 1)`.
5. **Variables.** `E ∈ {E0,E1,E2,E3,EX}`; `n_i` counts independent sources; `b` is 1 when at least one source is non-behavioural.
6. **Constraints.** Two outputs of one detector are not independent. Network evidence is never non-behavioural for identity.
7. **Boundary behaviour.** `E = EX` always returns false.
8. **Rounding.** None.
9. **Null behaviour.** A missing source count returns false.
10. **Exceptional conditions.** A reversible preventive hold may proceed at `E1` without this predicate (`EVD-002`).
11. **Dependencies.** EVD-010, EVD-011, EVD-015.
12. **Worked example.** `E3`, `n_i = 2`, `b = 1`, conduct → true.
13. **Verification.** Matrix fixture.
14. **Parameter status.** Structural.
15. **Owner.** B-12.
16. **Affected rules.** EVD-002, EVD-010, EVD-011.
17. **Affected requirements.** `REQ-766`, `REQ-767`, `REQ-793`, `REQ-826`.
18. **Revision.** 1.0.
19. **Review trigger.** Evidence-law or appeal finding.
20. **Approval.** Not approved.

### F-FP-008 — Report cluster key

1. **Purpose.** Coalesce duplicate reports of the same conduct.
2. **Inputs.** Subject account `s`, violation class `v`, time window `w`, conduct event key `e`.
3. **Units.** Opaque key.
4. **Expression.** `key = H(s ‖ v ‖ w ‖ e)`.
5. **Variables.** `H` is a stable keyed hash; `e` is the earliest linked event reference or `NONE`; `w` is the configurable clustering window `FP-P13`, expressed in turns.
6. **Constraints.** Different classes never coalesce; a reporter's identity is not part of the key.
7. **Boundary behaviour.** A report outside `w` forms a new cluster.
8. **Rounding.** None.
9. **Null behaviour.** A missing subject returns a held report, not a cluster. An unapproved `w` returns `PROVISIONAL_BLOCK`.
10. **Exceptional conditions.** A coordinated-report signal is stored separately and never raises a tier.
11. **Dependencies.** MOD-003, MOD-004, `FP-P13`.
12. **Worked example.** Three reports of `V-06` against one account in one window → one case.
13. **Verification.** Cluster fixture.
14. **Parameter status.** Structural + provisional window (`FP-P13`).
15. **Owner.** B-12.
16. **Affected rules.** MOD-003, MOD-005.
17. **Affected requirements.** `REQ-822`, `REQ-823`.
18. **Revision.** 1.1, 2026-11-07 (12B-C1: registered the configurable window `w` as `FP-P13`).
19. **Review trigger.** Report-tooling change.
20. **Approval.** Not approved.

### F-FP-009 — Rate allowance

1. **Purpose.** State the structural per-account allowance.
2. **Inputs.** Base allowance `A_0`, action class factor `f`, boundary length `L`.
3. **Units.** Operations per turn.
4. **Expression.** `A = ceil(A_0 × f × L)`.
5. **Variables.** `A_0` is the configurable rate base `FP-P07`; `f` is the configurable action-class factor `FP-P14`; `L` is the owning subsystem's declared boundary length, derived from the fixed cadence and not independently configurable.
6. **Constraints.** Never keyed to IP or network. A single account cannot exceed `A`.
7. **Boundary behaviour.** A new boundary resets the counter; carry-over does not exist.
8. **Rounding.** Ceiling.
9. **Null behaviour.** An unapproved `A_0` or `f` returns `PROVISIONAL_BLOCK`.
10. **Exceptional conditions.** Incident containment may lower `A` temporarily; the change is recorded.
11. **Dependencies.** SEC-007, D-168, `FP-P07`, `FP-P14`.
12. **Worked example.** `A_0=100`, `f=1`, `L=1` → 100.
13. **Verification.** Boundary and concurrency fixture.
14. **Parameter status.** Structural + provisional cap and factor (`FP-P07`, `FP-P14`).
15. **Owner.** Prompt 14 / Stage 5.
16. **Affected rules.** SEC-007, FR-13.
17. **Affected requirements.** `REQ-775`, `REQ-776`.
18. **Revision.** 1.1, 2026-11-07 (12B-C1: registered the action-class factor `f` as `FP-P14`).
19. **Review trigger.** Load measurement.
20. **Approval.** Not approved.

### F-FP-010 — Idempotency retention

1. **Purpose.** Ensure the key outlives the longest legitimate retry path.
2. **Inputs.** Maximum retry path `P_r` in turns, safety margin `m`.
3. **Units.** Turn boundaries.
4. **Expression.** `K = P_r + m`.
5. **Variables.** `P_r` is the owning subsystem's declared maximum; `m` is a fixed structural margin of 1 turn.
6. **Constraints.** `K ≥ P_r + 1`; no wall-clock minute value may replace `K`.
7. **Boundary behaviour.** A retry at or before `K` coalesces; after `K` it is a new request and must be rejected by state.
8. **Rounding.** Whole turns.
9. **Null behaviour.** An undeclared `P_r` returns a specification defect.
10. **Exceptional conditions.** A boundary failure extends `K` by the recovery turns.
11. **Dependencies.** SEC-003, SEC-006.
12. **Worked example.** `P_r = 3`, `m = 1` → 4 turns.
13. **Verification.** Replay fixture.
14. **Parameter status.** Structural.
15. **Owner.** B-12 and owning subsystem.
16. **Affected rules.** SEC-003, SEC-006, FR-09.
17. **Affected requirements.** `REQ-770`, `REQ-771`.
18. **Revision.** 1.0.
19. **Review trigger.** A duplicate-settlement incident.
20. **Approval.** Not approved.

### F-FP-011 — Recidivism multiplier

1. **Purpose.** Apply the single bounded escalation for confirmed repetition. This is the only formula that adds a repetition term; `F-FP-001` deliberately contains none, so a prior violation is counted once.
2. **Inputs.** Confirmed prior count `R`, base severity `SEV` from `F-FP-001`.
3. **Units.** Ordinal points.
4. **Expression.** `SEV_R = SEV + min(R, 2) × q`, where `q` is provisional.
5. **Variables.** `R` counts only `E3` findings in the review window; `q` is provisional. `SEV` is the repetition-free output of `F-FP-001`.
6. **Constraints.** `EX` and dismissed cases never count. The result never exceeds the tier maximum. Economic correction is never increased by `R`; correction and sanction remain independent (`COR-010`, `MOD-055`).
7. **Boundary behaviour.** `R > 2` is capped at 2 for escalation.
8. **Rounding.** Integer.
9. **Null behaviour.** Unknown prior history returns `R = 0`.
10. **Exceptional conditions.** A successful appeal removes the prior from the count.
11. **Dependencies.** FP-025, F-FP-001.
12. **Worked example.** `SEV = 5`, `R = 1`, `q = 1` → `SEV_R = 6` → `T2`. Two or more confirmed priors with `q = 1` → `SEV_R = 7` → `T3`.
13. **Verification.** Case fixture.
14. **Parameter status.** Structural + provisional weight.
15. **Owner.** Owner (`UD-053`).
16. **Affected rules.** FP-025, MOD-039.
17. **Affected requirements.** `REQ-812`, `REQ-813`.
18. **Revision.** 1.1, 2026-11-07 (12B-C1: documented as the sole repetition adjustment after removing the duplicate term from `F-FP-001`).
19. **Review trigger.** Calibration or appeal data.
20. **Approval.** Not approved.

### F-FP-012 — Audit digest chain

1. **Purpose.** Make record alteration detectable.
2. **Inputs.** Canonical record bytes `r_i`, previous digest `h_{i−1}`.
3. **Units.** 32-byte digest.
4. **Expression.** `h_i = SHA-256(h_{i−1} ‖ canonical(r_i))`, with `h_0` a published genesis value.
5. **Variables.** `canonical()` is a deterministic field ordering and encoding; no secret is stored in the row.
6. **Constraints.** The digest covers every protected field. A missing field invalidates the chain.
7. **Boundary behaviour.** The first row uses the fixed genesis digest for the chain instance.
8. **Rounding.** None.
9. **Null behaviour.** A missing record returns `CHAIN_BREAK`, not a skipped link.
10. **Exceptional conditions.** A correction appends a new record; it never recomputes an old digest.
11. **Dependencies.** EVD-030…EVD-034, `TR-090`.
12. **Worked example.** Record 1 digest is the SHA-256 of genesis plus canonical record 1.
13. **Verification.** Chain fixture and verification-run design; no runtime verification exists.
14. **Parameter status.** Structural.
15. **Owner.** B-02 spine, B-12 requirement.
16. **Affected rules.** EVD-030…EVD-034, SEC-038.
17. **Affected requirements.** `REQ-828`, `REQ-829`, `REQ-855`.
18. **Revision.** 1.0.
19. **Review trigger.** Spine implementation or algorithm change.
20. **Approval.** Not approved.

### F-FP-013 — Verification interval

1. **Purpose.** Bound the time between audit-chain verifications.
2. **Inputs.** Operational interval `I_v` in turns.
3. **Units.** Turns.
4. **Expression.** `I_v` (provisional constant).
5. **Variables.** `I_v` is provisional and must not exceed the owner-approved maximum.
6. **Constraints.** Verification is an executed job, not a documentation claim.
7. **Boundary behaviour.** A missed interval raises an incident at the next boundary.
8. **Rounding.** Whole turns.
9. **Null behaviour.** An unapproved interval returns `PROVISIONAL_BLOCK`.
10. **Exceptional conditions.** A chain break halts the next publication until reviewed.
11. **Dependencies.** EVD-032, `UD-058`.
12. **Worked example.** `I_v = 12` verifies once per 12 turns.
13. **Verification.** Job-existence check at implementation; none exists today.
14. **Parameter status.** Provisional.
15. **Owner.** Owner and Stage 5.
16. **Affected rules.** EVD-032, SEC-038.
17. **Affected requirements.** `REQ-829`, `REQ-858`.
18. **Revision.** 1.0.
19. **Review trigger.** Operational measurement.
20. **Approval.** Not approved.

### F-FP-014 — Correction conservation identity

1. **Purpose.** Prove that a correction neither creates nor loses value except through an explicitly recorded transaction.
2. **Inputs.** Opening balance `O`; signed sums of ledger deltas by transaction type: lawful originals `L`, corrections `C`, reversals `R`, compensations `P`, illicit removals `X`, administrative adjustments `A`; closing balance `Z`.
3. **Units.** Ledger value, minor unit.
4. **Expression.** `Z = O + L + C + R + P + X + A`.
5. **Variables.** **Sign convention:** every transaction carries a signed delta in the ledger's minor unit; a credit is positive and a debit is negative. Each term is the sum of the signed deltas of its `COR-001` type over the case window. `O` and `Z` are balances, not deltas. A `REVERSAL` references one original transaction and appends the exact opposite of its remaining unreversed effect; a partial reversal is permitted only up to that remainder; a duplicate reversal coalesces under `COR-005` and adds nothing.
6. **Constraints.** `Z ≥ 0`; every term references a recorded transaction; no unreferenced adjustment. A fully reversed correction contributes net zero (`C + R = 0` for that pair). The identity covers all six `COR-001` types; `ADMIN_ADJUSTMENT` is included as `A` and is never hidden inside another term.
7. **Boundary behaviour.** A nonzero residual between the computed and recorded closing balance fails the correction and raises an incident (`COR-017`).
8. **Rounding.** Minor unit.
9. **Null behaviour.** A missing term is zero only where the case has no such transaction; otherwise `INCOMPLETE`. A reversal with no resolvable original returns `NO_ORIGINAL` and is not applied.
10. **Exceptional conditions.** A ledger's own lawful creation/destruction is recorded as a separate owner event, not hidden in `C`.
11. **Dependencies.** COR-001…COR-017, B-04.
12. **Worked examples.** Original positive transaction: `O = 100`, `L = +40` → `Z = 140`. Negative correction removing the excess: `C = −40` → `Z = 100`. Reversal of that negative correction (for example after a successful appeal): `R = +40` → `Z = 140`, the exact opposite effect. Partial correction: `L = +40`, `C = −25` → `Z = 115`. Partial reversal of the partial correction: `R = +10` (≤ the 25 remainder) → `Z = 125`. Duplicate reversal attempt: the second `R = +10` coalesces and adds nothing → `Z = 125`. Missing original: a reversal referencing an absent transaction returns `NO_ORIGINAL`; no delta is appended. Failed correction transaction: the append rolls back (`COR-018`), so `C` contributes nothing and `Z` is unchanged.
13. **Verification.** Ledger reconciliation test design.
14. **Parameter status.** Structural.
15. **Owner.** B-04 and B-12.
16. **Affected rules.** COR-003, COR-017.
17. **Affected requirements.** `REQ-817`, `REQ-836`, `REQ-845`.
18. **Revision.** 1.1, 2026-11-07 (12B-C1: explicit signed-delta convention, added the `ADMIN_ADJUSTMENT` term, and specified reversal, partial-reversal and duplicate behaviour).
19. **Review trigger.** New transaction type.
20. **Approval.** Not approved.

### F-FP-015 — Compensation cap

1. **Purpose.** Bound discretionary compensation.
2. **Inputs.** Proven loss `L_p`, cap `C_max`.
3. **Units.** Ledger value.
4. **Expression.** `P = min(L_p, C_max)`.
5. **Variables.** `L_p` is established by the owning subsystem; `C_max` is an owner parameter.
6. **Constraints.** Compensation never exceeds proven loss and never creates a negative balance.
7. **Boundary behaviour.** `L_p = 0` → no compensation.
8. **Rounding.** Minor unit.
9. **Null behaviour.** An unapproved `C_max` returns `PROVISIONAL_BLOCK`.
10. **Exceptional conditions.** A systemic incident may use a published compensation schedule; it is still capped.
11. **Dependencies.** COR-006, MOD-056, `UD-053`.
12. **Worked example.** `L_p = 50`, `C_max = 100` → 50.
13. **Verification.** Ledger fixture.
14. **Parameter status.** Provisional.
15. **Owner.** Owner.
16. **Affected rules.** COR-006, MOD-056.
17. **Affected requirements.** `REQ-817`, `REQ-836`.
18. **Revision.** 1.0.
19. **Review trigger.** Owner decision or incident.
20. **Approval.** Not approved.

### F-FP-016 — Emergency expiry

1. **Purpose.** Make an emergency measure self-expiring.
2. **Inputs.** Start boundary `t_s`, duration `D_e`.
3. **Units.** Turns.
4. **Expression.** `t_e = t_s + D_e`.
5. **Variables.** `D_e` is a provisional owner parameter (`UD-056`).
6. **Constraints.** `D_e ≥ 1`; no indefinite emergency.
7. **Boundary behaviour.** At `t_e` the measure expires unless a new recorded extension exists.
8. **Rounding.** Whole turns.
9. **Null behaviour.** An unapproved `D_e` returns `PROVISIONAL_BLOCK`, not an indefinite measure.
10. **Exceptional conditions.** Extension requires a new review and remains bounded.
11. **Dependencies.** MOD-026, MOD-028, `UD-056`.
12. **Worked example.** Start 300, `D_e = 6` → expiry 306.
13. **Verification.** Expiry fixture.
14. **Parameter status.** Structural + provisional duration.
15. **Owner.** Owner (`UD-056`).
16. **Affected rules.** MOD-026, MOD-028.
17. **Affected requirements.** `REQ-847`, `REQ-849`, `REQ-850`.
18. **Revision.** 1.0.
19. **Review trigger.** Owner decision.
20. **Approval.** Not approved.

---

## 3. Parameter register

| Parameter | Used by | Current value | Classification | Owner | Review trigger |
|---|---|---|---|---|---|
| `FP-P01` severity weights (`S_c`) | `F-FP-001` | Annex A bands | Provisional | Owner (`UD-053`) | Calibration |
| `FP-P02` impact points | `F-FP-001` | 0–3 | Provisional | Prompt 14 | Case data |
| `FP-P03` recidivism weight `q` | `F-FP-011` | 1 | Provisional | Owner | Appeal data |
| `FP-P04` base restriction turns | `F-FP-005` | undefined | Owner decision required | Owner (`UD-053`) | Owner decision |
| `FP-P05` maximum restriction turns | `F-FP-005` | undefined | Owner decision required | Owner (`UD-053`) | Owner decision |
| `FP-P06` appeal window `W` | `F-FP-006` | undefined | Owner decision required | Owner (`UD-059`) | Owner decision |
| `FP-P07` rate base `A_0` | `F-FP-009` | undefined | Capacity validation | Stage 5/Prompt 14 | Load test |
| `FP-P08` verification interval `I_v` | `F-FP-013` | undefined | Provisional | Owner/Stage 5 | Measurement |
| `FP-P09` compensation cap `C_max` | `F-FP-015` | undefined | Owner decision required | Owner | Owner decision |
| `FP-P10` emergency duration `D_e` | `F-FP-016` | undefined | Owner decision required | Owner (`UD-056`) | Owner decision |
| `FP-P11` final retention periods | `PRV-023` | `D-026` values only | Legal review required | Owner/counsel (`UD-017`, `UD-055`) | Legal review |
| `FP-P12` appeal budget | `MOD-050` | undefined | Owner decision required | Owner (`UD-059`) | Owner decision |
| `FP-P13` report cluster window `w` | `F-FP-008` | undefined | Provisional | B-12 / Prompt 13 tooling | Report-tooling change |
| `FP-P14` action-class rate factor `f` | `F-FP-009` | undefined | Provisional | Stage 5 / Prompt 14 | Load measurement |

### 3.1 Formula-to-parameter mapping

Every independently configurable input has a register entry. Derived values, runtime inputs and fixed structural constants are listed separately and are **not** parameters.

| Formula | Configurable parameters | Derived / runtime inputs | Fixed structural constants |
|---|---|---|---|
| `F-FP-001` | `FP-P01` (`S_c` bands), `FP-P02` (impact points) | case facts | ordinal sets for `K`, `M`; tier bands |
| `F-FP-002` | — | `V_obs`, `V_law`, `B_i` | `min`/`max` form |
| `F-FP-003` | — | transaction set `T`, `d_t`, `e_t` | summation form |
| `F-FP-004` | — | case records | `type_rank` ordering |
| `F-FP-005` | `FP-P04` (`D_base`), `FP-P05` (`D_max`) | tier `T`, extension count `x` | integer turns |
| `F-FP-006` | `FP-P06` (`W`) | notice boundary `t_n` | — |
| `F-FP-007` | — | evidence state `E`, source counts | two-source / one-non-behavioural threshold |
| `F-FP-008` | `FP-P13` (`w`) | `s`, `v`, `e` | keyed hash `H` |
| `F-FP-009` | `FP-P07` (`A_0`), `FP-P14` (`f`) | boundary length `L` (from fixed cadence) | ceiling |
| `F-FP-010` | — | `P_r` (owning subsystem declaration) | margin `m = 1` turn |
| `F-FP-011` | `FP-P03` (`q`) | `R`, `SEV` | cap `min(R, 2)` |
| `F-FP-012` | — | record bytes, previous digest | SHA-256; genesis `h_0` per chain instance |
| `F-FP-013` | `FP-P08` (`I_v`) | — | whole turns |
| `F-FP-014` | — | signed transaction deltas | conservation identity |
| `F-FP-015` | `FP-P09` (`C_max`) | proven loss `L_p` | `min` form |
| `F-FP-016` | `FP-P10` (`D_e`) | start boundary `t_s` | whole turns |

Rule-level parameters outside the formula set: `FP-P11` (retention, `PRV-023`) and `FP-P12` (appeal budget, `MOD-050`). No parameter is approved; `FP-P13` and `FP-P14` were added by 12B-C1 because `w` and `f` are independently configurable and were previously unregistered.

---

## 4. Non-claims

No formula in this register is calibrated, implemented or executed. `F-FP-012` specifies a digest construction but does not prove that a chain exists or is verified. `F-FP-013` specifies an interval but no job runs. `F-FP-014` specifies a conservation identity but no ledger has been tested against it. Structural completeness is not numerical approval and is not runtime evidence.