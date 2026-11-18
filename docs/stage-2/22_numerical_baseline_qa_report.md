# B-14 companion — numerical baseline QA report

**Stage:** Stage 2 · **Parent:** Prompt 14 · **Subphase:** 14A · **Executed:** 2026-11-13
**Status:** Documentation-quality baseline. No gameplay formula has been executed against a scheduler, database, player or simulation. Nothing in this report is a balance result.

---

## 1. What was executed

Every command below was run on 2026-11-13 from `docs/` with Python 3.12 on Windows, against the working tree as found. Results are the actual terminal output, not a recollection or an old log.

| # | Test name | Command | Scope | Actual result | Pass/fail | Limitation | Relationship to 14A |
|---:|---|---|---|---|---|---|---|
| 1 | Economy arithmetic | `python qa_backups/verify_economy_numbers.py` | Recomputes the starting bundle, margins, worked examples and register index from §3 constants | `PASS: 164/164 economy arithmetic checks passed`; `ALL CHECKS PASSED` | PASS | Hand arithmetic, not a simulation | Numerical baseline |
| 2 | City arithmetic | `python qa_backups/verify_city_numbers.py` | City, construction, research and upkeep arithmetic | `PASS: 267/267 city arithmetic checks passed` | PASS | Hand arithmetic | Numerical baseline |
| 3 | Politics arithmetic and guards | `python qa_backups/verify_politics_numbers.py` | Population, approval, stability, elections arithmetic plus continuity guards | `POLITICS NUMBERS: 1 FAILED of 879 checks` — guard requires the literal “Prompt 13C next” in progress-log row 10 | **FAIL (inherited)** | 878 arithmetic and structural checks pass; one stale guard fails; **actual process exit code 1** (measured 2026-11-13) | Baseline + inherited stale guard |
| 4 | Market arithmetic | `python qa_backups/verify_market_numbers.py` | Directed trade, band, fees, conservation | `MARKET VALIDATION: ALL CHECKS PASSED` | PASS | Hand arithmetic | Numerical baseline |
| 5 | Diplomacy arithmetic and structure | `python qa_backups/verify_diplomacy_numbers.py` | 9 groups: structure, filenames, same-turn order, keys, freeze arithmetic, rolling window, posture, authority, cooldowns | `9 groups checked … 0 failed` | PASS | Hand arithmetic | Numerical baseline |
| 6 | Alliance arithmetic | `python qa_backups/verify_alliance_numbers.py` | B-09 formulas and candidate values | `375 passed, 0 failed` | PASS | Candidate values are not approved | Numerical baseline |
| 7 | Warfare workflows and fixtures | `python qa_backups/verify_warfare_workflows.py` | 40 workflows, 60 edge cases, 124 tests, fixture registry, current-status claims, validator integrity | `CHECKS: 49 EXECUTED: 49 FAILED: 0` | PASS | Designed tests, not runtime | Numerical regression |
| 8 | Alliance workflows | `python qa_backups/verify_alliance_workflows.py` | 49 workflows, 65 edge cases, 132 tests | `ALL CHECKS PASSED` | PASS | Designed tests | Numerical regression |
| 9 | Diplomacy workflows | `python qa_backups/verify_diplomacy_workflows.py` | 17 groups: sections, 30×23 workflows, 54 cases, 88 tests, matrices, traceability | `17 groups checked … 0 failed` | PASS | Designed tests | Numerical regression |
| 10 | Market workflows | `python qa_backups/verify_market_workflows.py` | B-07 companion links, progress-log naming, no release claim | `07C VALIDATION: ALL CHECKS PASSED` | PASS | Structural | Numerical regression |
| 11 | B-03 validator | `python qa_backups/09_validate.py` | B-03 rules, registers, handoff, history | `371/371 checks passed` | PASS | Structural | Structural baseline |
| 12 | Alliance validator | `python qa_backups/09A_validate_alliance.py` | B-09 943 checks incl. next-prompt guards | `Checks run: 943`; `FAIL: 2 problem(s)` — handoff does not name Prompt 10 next; AI_CONTEXT next-prompt guard | **FAIL (inherited)** | Two frozen continuity guards; 941 checks pass; **actual process exit code 1** | Inherited stale continuity guard |
| 13 | Alliance semantic validator | `python qa_backups/09B_validate_alliance_semantic.py` | B-09 semantic and register-tally checks | **8 problems**: C17 expects D-001…D-219, DD-001…DD-267, and frozen DD status counts; C18 next-prompt guard | **FAIL (inherited)** | Frozen historical expectations; **actual process exit code 1** | Inherited stale guard |
| 14 | Warfare validator | `python qa_backups/10B_validate_warfare.py` | 1,036 structural, disposition, formula and boundary checks; 73 negative fixtures | `Checks run: 1036`; `PASS`; `73/73 rejected; CF-01 and CF-02 PASS` | PASS | Documentary | Structural/arithmetic |
| 15 | 11A research validator | `python qa_backups/11A_validate_research.py` | 30 research-quality checks | `CHECKS: 30 EXECUTED: 30 FAILED: 1` — frozen `REQ-703` maximum | **FAIL (inherited)** | Stale maximum guard; **actual process exit code 1** | Inherited stale guard |
| 16 | B-11 validator | `python qa_backups/11B_validate_b11.py` | B-11 specification and 52 gates | `PASS`; `CLOSEOUT ELIGIBILITY: all 52 gates PASS` | PASS | Documentary | Structural |
| 17 | B-11 workflows | `python qa_backups/11C_validate_b11_workflows.py` | 11C workflows and acceptance | `RESULT: PASS` | PASS | Documentary | Structural |
| 18 | B-12 research validator | `python qa_backups/12A_validate_foundations.py` | 45 checks | `CHECKS: 45/45 passed; 0 failed` | PASS | Documentary | Structural |
| 19 | B-12 validator | `python qa_backups/12B_validate_b12.py` | 87 checks incl. 59 positive and 153 negative fixtures | `CHECKS: 87/87 passed; 0 failed` | PASS | Documentary | Structural/arithmetic |
| 20 | B-12 workflows | `python qa_backups/12C_validate_fair_play_workflows.py` | 24 checks | `CHECKS: 24/24 passed; 0 failed` | PASS | Documentary | Structural |
| 21 | 13A UI foundations | `python qa_backups/13A_validate_ui_foundations.py` | 34 checks | `34/34 passed` | PASS | Documentary | Unrelated (regression guard) |
| 22 | 13B UI specifications | `python qa_backups/13B_validate_ui_specifications.py` | 28 checks | `28/28 passed` | PASS | Documentary | Unrelated (regression guard) |
| 23 | 13C interaction specs | `python qa_backups/13C_validate_interaction_specs.py` | 27 checks | `27/27 passed` | PASS | Documentary | Unrelated (regression guard) |
| 24 | 13D integration | `python qa_backups/13D_validate_integration.py` | 75 checks | `75/75 passed` | PASS | Documentary | Unrelated (regression guard) |
| 25 | Final project validator | `python qa_backups/validate_final.py` | Project-wide document structure, decisions, requirements, next action | `VALIDATION: ALL CHECKS PASSED` | PASS | Documentary | Final QA |
| 26 | Documentation links | `python qa_backups/validate_links.py` | 131 Markdown files | `Markdown files scanned: 131`; `Links found: 4386`; `local 4004`; `external 382`; `anchors 34`; `Unresolved: 0` (historical: 95 122 / 4,321 / 3,939; C1 123 / 4,328 / 3,946; R1 124 / 4,335 / 3,953; R1-R1 125 / 4,341 / 3,959; CLOSURE 130 / 4,364 / 3,982; §106 130 / 4,367 / 3,985) | PASS | External links skipped | Documentation QA |
| 27 | Decision-register tests | `python qa_backups/test_decision_registers.py` | UD register integrity | `Ran 12 tests … OK` | PASS | Register only | Register QA |
| 28 | Next-action tests | `python qa_backups/test_next_action.py` | Continuity / next-action consistency | `Ran 27 tests … OK` | PASS | Continuity only | Continuity QA |
| 29 | **Prompt 14A validator** | `python qa_backups/14A_validate_numerical_foundation.py` | 55 documentary checks (including per-record 393-record metadata reconciliation and the constrained B-04 semantic contract): registers, counts, inventory completeness, metadata, source resolution, status vocabulary, owner-approved safeguard, B-03 exact values/owners, parameter coverage, B-14 headings, D-019/D-015, conversions, conservation, filename mapping, owner-reserved UDs, gates, archive | `CHECKS: 55  FAILED: 0`; `RESULT: PASS — documentary consistency only.` | PASS | Documentary; no formula execution | **14A primary** |
| 30 | **Prompt 14A self-tests** | `python qa_backups/14A_validate_numerical_foundation.py --self-test` | 138 positive/negative fixtures: prior 128 + constrained semantic-contract cases 129–138 | `SELF-TESTS: 138/138 passed` | PASS | Fixtures test the validator, not the game | **14A regression** |

---

## 2. Existing failures — classified

Four scripts fail on expectations frozen at an earlier prompt. All four failures pre-date Prompt 14A; none is caused by it; none was edited to make it pass.

| # | Script | Failure | Class | Why it is not a 14A defect | Disposition |
|---:|---|---|---|---|---|
| 1 | `verify_politics_numbers.py` (1/879) | Guard requires “Prompt 13C next” in progress-log row 10; the row now correctly says “Prompt 14 next” | 3 — stale documentation validator | The guard was written when 13C was the live sub-prompt; the progress log has legitimately advanced | Left unchanged; recorded as inherited |
| 2 | `11A_validate_research.py` (1/30) | Guard requires the maximum `REQ-` to stay `REQ-703` | 3 — stale documentation validator / 4 — incorrect expected count | Later prompts legitimately allocated `REQ-704`…`REQ-1203` | Left unchanged; recorded |
| 3 | `09A_validate_alliance.py` (2/943) | Handoff must name Prompt 10 next; AI_CONTEXT must set a 10–13 series next prompt | 3 — stale continuity guard | Historical 09A-era expectations | Left unchanged; recorded |
| 4 | `09B_validate_alliance_semantic.py` (8 problems) | D/DD register ranges and tallies frozen at D-219 / DD-267; next-prompt guard | 3 + 4 — stale guards and frozen counts | The registers have legitimately grown to D-237 / DD-285 | Left unchanged; recorded |

**Failure classes from Prompt 14A §12.2:**

| Class | Instances in the 14A baseline |
|---|---|
| 1. Genuine arithmetic errors | **0** |
| 2. Missing formula metadata | **Present but not a validator failure**: recorded in the inventory (B-05 rounding, B-07 timing, B-08 output, B-09 dependencies, B-12 phase) |
| 3. Stale documentation validators | **4 scripts** (above) |
| 4. Incorrect expected counts | **2** folded into the stale guards (`REQ-703`, D-219/DD-267) |
| 5. Cross-reference failures | **1 source defect**: B-07 `F-TM-000e` cites `§4.20` |
| 6. Missing test coverage | **B-12 has no runtime or case-data test**; formula-level timing is unvalidated |
| 7. Runtime implementation limitations | **No runtime exists**; nothing to run |
| 8. Unrelated legacy QA issues | **None asserted generically.** Measured on 2026-11-13: `Verify_politics`, `11A`, `09A` and `09B` each print FAIL and return exit code **1**; the earlier “exit 0” claim was incorrect |

---

## 2a. Validator expectation advances required by D-237 / DD-285

Adding the legitimate decision pair **D-237 / DD-285** made five historical validators fail on frozen register maxima. The expectations were advanced to the new source-evidenced maximum; no check was deleted, relaxed or converted into a warning.

| File | Change | Source evidence |
|---|---|---|
| `validate_final.py` | DD count `284` → `285`; added the spelled count “two hundred and thirty-seven” = 237 | `D-237` row exists; `DD-285` row exists |
| `09_validate.py` | DD contiguity `DD-001..DD-284` → `DD-001..DD-285`; added the 237 spelled count | Same |
| `12A_validate_foundations.py` | continuity `decisions_range` `D-001..D-236` → `D-001..D-237` | Same |
| `13A_validate_ui_foundations.py` | continuity `decisions_range` and DD contiguity → `D-237` / `DD-285` | Same |
| `13B_validate_ui_specifications.py` | D range `237`, DD range `285`, continuity `decisions_range` | Same |

All five pass after the advance. These are expectation updates, not weakened checks: the validators still reject a missing, duplicate or non-contiguous row. The 13A validator also requires a “Prompt 13A” mention within the first 6,000 characters of AI_CONTEXT/PROJECT_PROGRESS; the new 14A head block records that Prompt 13A, 13B and 13C remain owner accepted, which satisfies that check without moving the historical record.

---

## 3. Coverage gaps

| Area | Covered by | Gap |
|---|---|---|
| B-04 arithmetic | `verify_economy_numbers.py` 164 checks | No simulation of interacting turns |
| B-05 arithmetic | `verify_city_numbers.py` 267 checks | No cross-check with B-04 production over time |
| B-06 arithmetic | `verify_politics_numbers.py` 878/879 | Election cycle over many terms not simulated |
| B-07 arithmetic | `verify_market_numbers.py` | No market-clearing or liquidity test; Global Trade release-gated |
| B-08 arithmetic | `verify_diplomacy_numbers.py` | No multi-party timer interaction test |
| B-09 arithmetic | `verify_alliance_numbers.py` 375 checks | No owner decision provides a real rate, bracket or capacity |
| B-10 arithmetic | `10B_validate_warfare.py` 1,036 checks | No battle simulation; seeded outcomes not statistically tested |
| B-11 arithmetic | `11B_validate_b11.py` | Reward impact on the economy not modelled |
| B-12 arithmetic | `12B_validate_b12.py` 87 checks | No case data; six parameters undefined by owner decision |
| Cross-system | 14A dependency map | **No integrated simulation of P3–P7 across all systems** |
| Player behaviour | None | **No playtest exists** |

---

## 4. Specification versus execution

| Category | Status on 2026-11-13 |
|---|---|
| Formula specified | **Yes** — 295 active identifiers resolve to nine registers |
| Arithmetic independently checked | **Yes for many formulas** — the arithmetic scripts recompute examples and identities from source constants |
| Validator passed | **Yes** — 55/55 in the 14A validator and 138/138 14A self-tests; the historical scripts pass except the four inherited stale guards |
| Offline simulation performed | **No** — no simulation engine exists |
| Runtime test executed | **No** — no playable Nation Supremacy runtime exists |
| Actual player playtest performed | **No** — no player has played the game |

A result in one row cannot be promoted into the row below it. In particular:

- A passing arithmetic check is not an approved value.
- A passing documentary validator is not an implemented mechanic.
- The feasibility prototype is infrastructure-feasibility code, not a gameplay simulation.
- No WCAG, security, retention or balance claim follows from this report.

---

## 5. Prompt 14A regression evidence

The 14A validator carries an integrated self-test facility (`--self-test`). It mutates in-memory copies of the real documents and asserts the expected outcome for each required case.

| # | Fixture | Expected | Actual |
|---:|---|---|---|
| 1 | Correct 295-ID baseline | PASS | PASS |
| 2 | Missing active formula | FAIL | FAIL (`14A-05`) |
| 3 | Duplicate active formula | FAIL | FAIL (`14A-05`) |
| 4 | Retired formula counted as active | FAIL | FAIL (`14A-05`) |
| 5 | Unresolved formula source reference | FAIL | FAIL (`14A-07`) |
| 6 | Missing unit metadata | FAIL | FAIL (`14A-06`) |
| 7 | Missing rounding metadata | FAIL | FAIL (`14A-06`) |
| 8 | Missing timing metadata | FAIL | FAIL (`14A-06`) |
| 9 | Missing B-03 carry-in | FAIL | FAIL (`14A-10`) |
| 10 | Altered B-03 provisional value | FAIL | FAIL (`14A-11`) |
| 11 | Incorrect parameter owner | FAIL | FAIL (`14A-11`) |
| 12 | Invalid numerical status | FAIL | FAIL (`14A-08`) |
| 13 | False owner-approved classification | FAIL | FAIL (`14A-09`) |
| 14 | Owner-reserved UD silently resolved | FAIL | FAIL (`14A-25`) |
| 15 | Correct current B-14 `22_` mapping | PASS | PASS (`14A-22`) |
| 16 | Live roadmap row using stale `21_` | FAIL | FAIL (`14A-22`) |
| 17 | Historical superseded `21_` mention labelled | PASS | PASS (`14A-22`) |
| 18 | D-019 ordering preserved | PASS | PASS (`14A-17`) |
| 19 | Obsolete D-015 wording presented as current | FAIL | FAIL (`14A-18`) |
| 20 | Missing validator reference | FAIL | FAIL (`14A-06`) |

### 5.1 Prompt 14A-C1 parameter mutation fixtures

| # | Fixture | Expected | Actual |
|---:|---|---|---|
| 21 | Remove B-10 `F-WR-001` parameter record | FAIL | FAIL (`14A-29`) |
| 22 | Change B-10 `F-WR-003` owner | FAIL | FAIL (`14A-32`) |
| 23 | Promote B-10 `F-WR-003` to owner-approved without evidence | FAIL | FAIL (`14A-32`) |
| 24 | Change B-04 starting treasury 1,500 → 1,501 | FAIL | FAIL (`14A-30`) |
| 25 | Change a parameter unit | FAIL | FAIL (`14A-31`) |
| 26 | Change a parameter rounding rule | FAIL | FAIL (`14A-33`) |
| 27 | Remove a parameter source reference | FAIL | FAIL (`14A-33`) |
| 28 | Duplicate a parameter record | FAIL | FAIL (`14A-29`) |
| 29 | Remove a B-08 parameter record | FAIL | FAIL (`14A-29`) |
| 30 | Remove a B-09 parameter record | FAIL | FAIL (`14A-29`) |
| 31 | Remove a B-11 parameter record | FAIL | FAIL (`14A-29`) |
| 32 | Mark playtesting-dependent `FP-P07` owner-approved | FAIL | FAIL (`14A-32`) |
| 33 | Preserve a correctly documented provisional parameter | PASS | PASS (`14A-32`) |
| 34 | Preserve a properly sourced owner-approved parameter | PASS | PASS (`14A-32`) |
| 35 | Preserve an explicit missing-data marker where the source omits the field | PASS | PASS (`14A-33`) |

The original 20 fixtures remain unchanged. The four mutations reproduced by the independent audit are fixtures 21–24; all four are now rejected. **Test history at the C1 stage (superseded by §5.2 after C1-R1):** previous 28 checks and 20 self-tests; added 7 checks (`14A-29`…`14A-35`) and 15 fixtures; C1 totals **35 checks / 35 self-tests**. After C1-R1 the totals are **41 checks / 48 self-tests**. The new checks protect record presence, source values, units, rounding, timing, authority, status, owner-reserved state, evidence visibility and archive indexing.

### 5.2 Prompt 14A-C1-R1 source-metadata fixtures

| # | Fixture | Expected | Actual |
|---:|---|---|---|
| 36 | B-10 `F-WR-003` unit → `bananas` | REJECT | REJECT (`14A-39`) |
| 37 | B-04 Treasury decision authority changed | REJECT | REJECT (`14A-36`) |
| 38 | B-04 Treasury promoted to `OWNER-APPROVED VALUE` | REJECT | REJECT (`14A-36`) |
| 39 | B-04 Treasury timing changed | REJECT | REJECT (`14A-36`) |
| 40 | B-03 `W_obs` unit → `bananas` | REJECT | REJECT (`14A-38`) |
| 41 | B-03 `W_obs` evidence replaced by “evidence already satisfied” | REJECT | REJECT (`14A-38`) |
| 42 | B-03 `W_obs` evidence class → `Confirmed` | REJECT | REJECT (`14A-38`) |
| 43 | B-02 Turn length status → `PROVISIONAL VALUE` | REJECT | REJECT (`14A-37`) |
| 44 | B-12 `FP-P07` unit → `bananas` | REJECT | REJECT (`14A-39`) |
| 45 | Source unit field removed (unparseable) | REJECT | REJECT (`14A-39`) |
| 46 | B-10 `F-WR-003` timing changed | REJECT | REJECT (`14A-33`) |
| 47 | B-09 `F-AL-002` owner-reserved flag cleared | REJECT | REJECT (`14A-32`) |
| 48 | Preserve the approved B-02 turn-length status | ACCEPT | ACCEPT (`14A-37`) |

The nine audit mutations are fixtures 36–44. Fixtures 46–48 add distinct protections; the remaining C1-R1 matrix cases reuse the existing fixtures 21–35 (record removal, duplication, B-03 value/owner, owner-approved promotion, rounding, owner-reserved UD, and the three positive cases).

**Exact totals:** 55 checks, 0 failed; 138 self-tests, 138 passed.

### 5.3 Parameter source-coverage matrix

Produced by `python qa_backups/14A_validate_numerical_foundation.py --coverage`. `m` = source-matched, `x` = explicit source omission, `d` = derived analysis label (source states no such field), `c` = register-level convention.

| System | Records | Values | Units | Precision + rounding | Timing | Authority | Status | Evidence |
|---|---:|---:|---|---|---|---:|---:|---|
| B-02 | 7 | 7/7 | 7m/0x/0d | 0m/7x/0c | 7m/0x/0c | 7/7 | 7/7 | 0m/7x |
| B-03 | 20 | 20/20 | 20m/0x/0d | 0m/20x/0c | 0m/20x/0c | 20/20 | 20/20 | 20m/0x |
| B-04 | 49 | 49/49 | 42m/7x/0d | 0m/0x/49c | 0m/0x/49c | 49/49 | 49/49 | 0m/49x |
| B-05 | 73 | 73/73 | 60m/13x/0d | 0m/0x/73c | 0m/0x/73c | 73/73 | 73/73 | 0m/73x |
| B-06 | 96 | 96/96 | 73m/23x/0d | 0m/0x/96c | 0m/0x/96c | 96/96 | 96/96 | 0m/96x |
| B-07 | 26 | 26/26 | 26m/0x/0d | 0m/0x/26c | 0m/0x/26c | 26/26 | 26/26 | 0m/26x |
| B-08 | 12 | 12/12 | 11m/1x/0d | 12m/0x/0c | 12m/0x/0c | 12/12 | 12/12 | 0m/12x |
| B-09 | 8 | 8/8 | 8m/0x/0d | 8m/0x/0c | 8m/0x/0c | 8/8 | 8/8 | 0m/8x |
| B-10 | 39 | 39/39 | 18m/21x/0d | 39m/0x/0c | 39m/0x/0c | 39/39 | 39/39 | 0m/39x |
| B-11 | 49 | 49/49 | 40m/9x/0d | 49m/0x/0c | 49m/0x/0c | 49/49 | 49/49 | 0m/49x |
| B-12 | 14 | 14/14 | 1m/0x/13d | 0m/14x/0c | 0m/14x/0c | 14/14 | 14/14 | 14m/0x |
| **Total** | **393** | **393/393** | **306m/74x/13d** | **108m/41x/244c** | **115m/34x/244c** | **393/393** | **393/393** | **34m/359x** |

**Unparseable source fields: 0.** B-12 states no per-parameter rounding or timing, so those are explicit omissions. B-12 also states no unit column; 13 units are derived analysis labels, and `FP-P07` is source-validated against `F-FP-009` (“Operations per turn”). B-03 states no evidence classification; its class column is a derived label frozen against change.

### 5.4 Source-authorized metadata corrections made in C1-R1

Values, owners and statuses were not changed. The following metadata corrections were made so the columns reflect their sources:

1. Formula-row units are now derived from the source fields — B-08/B-09 `Variables` + `Range`, B-10 `Output`, B-11 `Units` + `Output range` — instead of from the status text. Records with no source unit carry `NOT SPECIFIED IN SOURCE`.
2. `FP-P07` unit corrected from `actions` to `operations per turn`, the unit stated by `F-FP-009`.
3. B-03 evidence-class column relabelled as derived (`Evidence class (derived; not in B-03)`) because B-03 §21.2 states no classification.
4. B-12 evidence column relabelled `Review trigger / evidence required` to match the source register's `Review trigger` field.

### 5.5 Final precision/rounding coverage (C1-R1-R1)

| Scope | Rule type | Count | Validation |
|---|---|---:|---|
| B-04 constants | Register-level integer/basis-point convention (`F-EC-000b`) | 49 | Exact convention string; fixture 49 rejects `round to nearest banana` |
| B-05 constants | Register-level integer convention (`F-CI-000c`) | 73 | Exact convention string; fixture 51 rejects a change |
| B-06 constants | Register-level integer convention (`F-PD-000b`) | 96 | Exact convention string; fixture 52 rejects a change |
| B-07 constants | Register-level integer convention (`F-TM-000c`) | 26 | Exact convention string; fixture 53 rejects a change |
| B-08…B-11 formula rows | Individual source `Rounding` field | 108 | Source-matched; 41 explicit omissions |
| B-02, B-03, B-12 records | No per-record precision/rounding field | 41 | Explicit omission/derived marker; not counted as matched |

The four source anchors are present in the registers; if any anchor or the convention text is missing, `14A-42` fails closed (fixture 55).

### 5.6 Final owner-reserved coverage (C1-R1-R1)

| Class | Count | Source basis |
|---|---:|---|
| Applicable records | 386 | Constants 244, formulas 108, B-12 14, B-03 20 |
| Not owner-reserved | 368 | `No`; B-03 may note the legal dependency `UD-017` |
| Owner-reserved | 18 | B-09 8 (UD-040/043/044/046) and B-12 10 (owner/counsel/UD-053/056/059/017/055) |
| No flag field (N/A) | 7 | B-02 timing rows have no owner-reserved column |

Fixture 56 rejects a false Treasury `Yes`; fixtures 57–61 reject removal of a genuine `Yes` and unsupported additions; fixture 62 rejects an empty B-12 owner field as ambiguous. Genuine B-09/B-12 owner-reserved rows and non-owner-reserved Treasury pass.

### 5.7 Archive reconciliation (C1-R1-R1)

| Archive | Status | Bytes | SHA-256 |
|---|---|---:|---|
| Prompt 14A | Unchanged | 45,984 | `5441eef4…` |
| Prompt 14A-C1 | Unchanged | 25,856 | `ffee4c8f…` |
| Prompt 14A-C1-R1 | Provenance paragraph removed; title and supplied instruction retained | 28,525 | `4c282b11d449484850e9a27832286b9ff77e793257a5b7ac4c4bc51cd988b52b` |
| Prompt 14A-C1-R1-R1 | Archived verbatim, no provenance paragraph | 24,815 | `12e03da21a94fdf646b75f06ba92f764b18069d9050ce93d5ec468a21e4e2702` |
| Prompt 14A-C1-R1-R1-C1 | Archived verbatim, no provenance paragraph | 20,967 | `3cd013609ccb826b478414418388a140be75532b9a1326b8fa5be4d902de8a96` |
| Prompt 14A-C1-R1-R1-C1-R1 | Archived verbatim, no provenance paragraph | 19,654 | `5e11f66212c7312f46b98561841949a7a6bffc220a06dcabfca90a8cbed409fe` |
| Prompt 14A-C1-R1-R1-C1-R1-C1 | Archived verbatim, no provenance paragraph | 29,966 | `a377413ecaa9792af7f1f49e03e510ac1e77b53e353ea3cf87305e995ade3fec` |
| Prompt 14A-C1-R1-R1-C1-R1-C1-R1 | Archived verbatim, no provenance paragraph | 18,397 | `41fcf5d32a39a39bc528457786af1c541ce2379f17b4f4f9a5a3084563f65317` |
| Prompt 14A-C1-R1-R1-C1-R1-C1-R1-R1 | Archived verbatim, no provenance paragraph | 24,429 | `365d60e98aae49b01fedbf26f934ef66f5100133f20fb0846729418ddf477774` |

No independent external original exists for byte comparison; the limitation is recorded in [INDEX.md](../prompts/INDEX.md).

### 5.8 B-04 semantic source contracts (final C1)

| Clause | Source version | Protected elements | Contract hash | Mutations rejected |
|---|---|---|---|---|
| `F-EC-000b` | B-04 register v1.4 | Integer quantities; every division states floor/ceil/round_half_up; no binary floating point; integer basis points; 10,000 bp = 100% | `bb1090cc…` | Decimal fractions; floating-point permission; removal of the prohibition or rounding requirement; basis-point and 10,000-bp changes (fixtures 66–71) |
| `F-EC-000f` | B-04 register v1.4 | v1.0 provisional calibration; carried unchanged into v1.1; `F-EC-044`; not observed prices; not balance claims; Prompt 14 changes only by a new register revision | `3025cc44…` | Owner-only revision authority; provisional-classification removal; v1.0/v1.1 change; `F-EC-044` removal; observed-price and balance-claim promotions (fixtures 73–78) |

The controlled contract is stored in the validator independently of the source read. A legitimate amendment requires a D-014 decision, a revised B-04 register, a deliberate controlled-contract update and a regression test; the validator fails closed until that path is followed.

### 5.9 C1 documentation-link reconciliation (historical snapshot)

| Measure | Final actual result |
|---|---:|
| Markdown files scanned | **126** |
| Total links checked | **4,342** |
| Local links | **3,960** |
| External links skipped | **382** |
| Anchors checked | **34** |
| Unresolved links | **0** |

These totals belong to the C1 correction and are preserved as a dated snapshot; later corrections superseded them. The current executed totals are recorded in §5.18.

### 5.10 Final test totals

**55 checks / 138 self-tests = 193 assertions**, all passing. The prior 53 checks and 128 tests remain intact; fixtures 65–78 add the B-04 semantic contracts, 79–94 the amendment-authorization chain, 95–118 the substantive D-014 decision evidence, 119–124 the evidence-content relevance checks, 125–128 the contradiction/negation/scope checks, and 129–138 the constrained semantic-contract exception cases.

### 5.17 Evidence contradiction detection (final)

| Control | Result |
|---|---|
| Stance | Independently classified `supports` / `contradicts` / `not_established`; a declared stance is not trusted alone |
| D-999 prohibition-as-permission | Rejected — cited passage prohibits binary floating point |
| Negation reversal | Rejected — “observed prices / balance claims” against “not observed prices / not balance claims” |
| Numerical scope | Rejected — changed basis-point relationship against the 10,000-bp passage |
| Partial coverage | Rejected — supports-claim term absent from the quote |
| Fractional carry | “No fractional carry stated” is not treated as permission |
| Unauthorized mapping | A manifest-declared allowlist is ignored; the controlled allowlist governs |
| Positive Category A/B/C | Accepted under their D-014 paths |
| Baseline | PASS |

### 5.18 Final semantic-contract closure totals (current)

| Measure | Final actual result |
|---|---:|
| Markdown files scanned | **131** |
| Total links checked | **4,386** |
| Local links | **4,004** |
| External links skipped | **382** |
| Anchors checked | **34** |
| Unresolved links | **0** |

### 5.19 Constrained semantic-contract validation (final)

| Control | Result |
|---|---|
| Mechanism | Deterministic `_semantic_contract_violation` for the two controlled B-04 clauses; no external model at validation runtime |
| F-EC-000b | Integer quantities, explicit division rounding, prohibition of binary floating point, integer basis points and 10,000-bp totality enforced; exceptions, conditions and alternative representations rejected |
| F-EC-000f | Provisional-calibration/revision rule enforced; final-value and affirmative observed-price/balance claims rejected; exceptions rejected |
| Representation vocabulary | IEEE-754 / binary32 / binary64 / binary128 / single-precision / double-precision / alternative, binary and decimal representation all rejected where they would alter the arithmetic rule |
| Exception and scope wording | `exception`, `unless`, `except`, `provided that`, `only when`, `subject to`, `notwithstanding`, `however` combined with controlled arithmetic terms are rejected rather than accepted |
| Fractional carry | “No fractional carry stated” and equivalent permissions rejected |
| Unknown material wording | Fails closed — an unclassified material arithmetic clause is not accepted as compliant |
| Exact D-990 attack | **REJECTED** (`semantic-contract`) |
| D-999 permission/prohibition attack | **REJECTED** (`contradicts` / `semantic-contract`) |
| D-998 fair-play evidence attack | **REJECTED** (unauthorized evidence locus) |
| Positive Category A/B/C fixtures | Accepted under their D-014 paths (fixtures 80, 81, 118) |
| Baseline | PASS — 55/55 checks; 138/138 self-tests |
| Production manifest | Empty |

The final semantic check is deliberately narrow: it validates only the two existing controlled B-04 source clauses against their published arithmetic rules. It is not a general natural-language validator and does not authorize the use of an external AI model during validation.

### 5.15 Evidence-content relevance validation (final)

| Control | Result |
|---|---|
| Authorized evidence loci | F-EC-000b: B-04 F-EC-000b/F-EC-000c, B-14 §8.2, REQ-162; F-EC-000f: B-04 F-EC-000f/F-EC-044, B-14 §5/§7 |
| Structured evidence | `path=`, `section=`, `quote="…"`, `supports="…"`, `Rationale:` |
| Section resolution | Section heading/row must exist; quote must appear in that section |
| Claim relevance | Supports-claim must overlap the quoted evidence |
| D-998 fair-play attack | Rejected because the fair-play document is not an authorized evidence locus for F-EC-000b |
| Unrelated document with similar terms | Rejected (unrecognized locus) |
| Misleading context / wrong section | Rejected (quote not in the cited section) |
| Fabricated excerpt | Rejected (quote absent) |
| Stale/invalid location | Rejected (unrecognized or missing section) |
| Materially changed evidence | Rejected (quote absent) |
| Unsupported/partial claim | Rejected (supports-claim not substantiated) |
| Category A/B/C positive fixtures | Accepted under their D-014 paths |
| Baseline | PASS |

The fair-play document does not mention F-EC-000b or its arithmetic terms, and the evidence allowlist is clause-specific. A path, generic rationale or matching hash is not accepted as relevance. A future evidence source requires a controlled allowlist update with the authorizing decision and regression evidence.

### 5.16 Evidence-relevance closure totals (historical snapshot)

| Measure | Final actual result |
|---|---:|
| Markdown files scanned | **129** |
| Total links checked | **4,360** |
| Local links | **3,978** |
| External links skipped | **382** |
| Anchors checked | **34** |
| Unresolved links | **0** |

### 5.13 Substantive D-014 decision-evidence validation (final closure)

The validator now parses the actual eight-column `DECISIONS.md` table by header name and validates the target row's cells, not just the row text.

| Evidence | Enforcement |
|---|---|
| Exact source and clause identity | Exact B-04 filename and clause ID required |
| Previous rule | `Previous rule:` marker plus normalized/token comparison with the controlled baseline |
| Replacement rule | `Replacement rule:` marker plus comparison with the actual revised clause |
| Alternatives | `Alternatives:` marker with substantive content |
| Rationale and evidence | Non-generic Reason & evidence; repository path must resolve |
| Consequences | Substantive Consequences field |
| Reopening conditions | `Reopening:` marker with substantive content |
| Category and status | Explicit Category A/B/C/D; matching status and manifest fields |
| Owner authorization | Required for Category A/D and owner-reserved amendments |
| Duplicates/malformed rows | Duplicate IDs rejected; target amendment row must have eight cells |

The minimal D-998 pattern (clause, source, “Amends”, Confirmed, generic reason/evidence) is rejected with specific missing-field diagnostics. Complete Category B, owner-authorized Category A and Provisional Category C fixtures pass. The production manifest remains `amendments: []`.

**Legacy register limitation:** 26 historical `DECISIONS.md` rows have fewer than eight cells (D-066…D-080, D-162, D-188…D-211 subset). They are not eligible for amendment validation; a target amendment row with fewer than eight cells fails as missing. This is an inherited register-structure limitation, not a new defect.

### 5.14 R1-R1-C1 closure totals (historical snapshot)

| Measure | Final actual result |
|---|---:|
| Markdown files scanned | **128** |
| Total links checked | **4,355** |
| Local links | **3,973** |
| External links skipped | **382** |
| Anchors checked | **34** |
| Unresolved links | **0** |

### 5.11 D-014 amendment-authorization chain (final closure)

| Control | Result |
|---|---|
| Source → decision → amendment → revised contract → revised hash → regression evidence | Enforced by `14A-45`, `14A-46` and `14A-48` |
| Baseline hashes | `bb1090cc…` and `3025cc44…`, independently maintained in the validator and JSON manifest |
| Valid Category B amendment fixture | Accepted (fixture 80) |
| Valid owner-authorized Category A fixture | Accepted (fixture 81) |
| Changed source without decision | Rejected (fixture 82) |
| Hash/manifest update without decision | Rejected (fixtures 83, 90) |
| Unrelated decision citation | Rejected (fixture 84) |
| Wrong-clause decision | Rejected (fixture 85) |
| Pending/rejected/deferred/superseded decision | Rejected (fixtures 86–89) |
| Wrong previous/new fingerprint | Rejected (fixtures 91–92) |
| Owner-reserved change without owner authority | Rejected (fixture 93) |
| Amendment entry without source change | Rejected (fixture 94) |

The controlled amendment manifest is [14A_b04_source_contract_amendments.json](../qa_backups/14A_b04_source_contract_amendments.json): baseline hashes only, with an empty amendment list. A future amendment requires a real D-014 decision, a revised B-04 register, a deliberate manifest/contract update and a regression test.

### 5.12 R1-R1 closure totals (historical snapshot)

| Measure | Final actual result |
|---|---:|
| Markdown files scanned | **127** |
| Total links checked | **4,348** |
| Local links | **3,966** |
| External links skipped | **382** |
| Anchors checked | **34** |
| Unresolved links | **0** |


---

## 6. Limitations

1. The 14A validator checks documentary consistency, not arithmetic. The arithmetic scripts check arithmetic, not balance.
2. The four inherited failing scripts were re-executed without a pipeline and each returned process exit code **1** (`verify_politics_numbers.py`, `11A_validate_research.py`, `09A_validate_alliance.py`, `09B_validate_alliance_semantic.py`). The earlier statement that they return `0` was incorrect and has been removed. The 14A validator returns `0` on PASS and non-zero on any failed check.
3. Four historical validators carry frozen expectations. Repairing them is a separate bounded maintenance task; doing it inside 14A would mix a validator rewrite into a numerical-foundation phase.
4. The parameter inventory is complete at the granularity of register constant tables and formula-level value sets. It is not a re-derivation of every variable in every expression.
5. The B-14 document and its companions are specification-level artefacts. No implementation, deployment, simulation or playtest follows from them.

---

## 7. Reproduction

```bash
cd docs
python qa_backups/14A_validate_numerical_foundation.py
python qa_backups/14A_validate_numerical_foundation.py --self-test
python qa_backups/verify_economy_numbers.py
python qa_backups/verify_city_numbers.py
python qa_backups/verify_politics_numbers.py
python qa_backups/verify_market_numbers.py
python qa_backups/verify_diplomacy_numbers.py
python qa_backups/verify_alliance_numbers.py
python qa_backups/validate_final.py
python qa_backups/validate_links.py
python qa_backups/test_decision_registers.py
python qa_backups/test_next_action.py
```

The four inherited failures reproduce identically before and after Prompt 14A.

---

## 8. Superseding controlled-contract implementation (2026-11-16)

This section supersedes the current-status claims in §§5.11–5.19 for semantic acceptance. The historical tables remain preserved.

### 8.1 Finding

The independent review of Project X (105) reproduced three complete false acceptances against the 55-check lexical validator:

| Case | Attack | Historical result |
|---|---|---|
| D-991 | Radix-two exponent/significand encoding permission | Accepted 55/55 |
| D-992 | Sign, exponent and mantissa representation permission | Accepted 55/55 |
| D-993 | Residual sub-unit amounts preserved between turns | Accepted 55/55 |

The lexical gate was a blocklist over known surface forms. Sentences outside the list returned “no violation”. B-14 §15.11 SEM-07 therefore did not establish that unknown material wording fails closed.

### 8.2 Implementation

D-238 adopts two typed contracts, `NC-F-EC-000b` and `NC-F-EC-000f` (v1.0.0), in `docs/stage-2/22_numerical_contracts/`: a strict schema, a closed lexicon, deterministic projection templates, a draft evidence catalogue and an index recording the preserved baseline. The contract validator implements:

- strict schema and semantic validation (unknown fields, enumerations, references and metadata fail);
- deterministic rendering and 100 % material coverage;
- typed proposition diffs;
- an evidence gate based only on governed, independently reviewed `SUPPORTS` mappings;
- a separate D-014 authority gate, including Category A/D owner-authorization provenance;
- a fail-closed prose ingest path that cannot accept a semantic change without a typed patch;
- deterministic fingerprints for contracts, projections, source Markdown and evidence documents.

The legacy lexical functions remain as historical diagnostics. They are not an acceptance gate: a clarification that the lexical gate rejects is accepted by the typed contract when the proposition set is unchanged.

### 8.3 Executed results

| Check | Actual result |
|---|---|
| `14A_validate_numerical_foundation.py` | **64/64 checks; 150/150 self-tests** |
| `14A_contract_validator.py` | **9/9 production checks; PASS** |
| `test_14A_contract_validator.py` | **83/83 tests; OK** |
| D-998 / D-999 / D-990 | Rejected for the stated semantic reason; three paraphrases each |
| D-991 / D-992 / D-993 | Rejected; three paraphrases each; D-993 has no reviewed `SUPPORTS` mapping |
| Positive fixtures | Baseline, wording clarification, typed Category B, Category C, owner-authorized Category A (test-only proposition) and B-09 F-AL-006 within-turn accrual accepted under their stated conditions |
| Evidence mappings | 11 active; 0 reviewed; 0 reviewed `SUPPORTS` |
| B-04 source hashes | `bb1090cc…` / `3025cc44…` unchanged |
| Production amendment manifest | `amendments: []` |
| Active formulas / parameter records / B-03 carry-ins / registers | 295 / 393 / 20 / 9 preserved |

### 8.4 Status

Implementation is complete; validation passed at the documentation/tooling level; documentation is reconciled for this pass; **owner acceptance is PENDING and is not claimed**. Prompt 14A remains **OPEN** until owner acceptance. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**.

**Exact next action:** owner review and acceptance or rejection of the Prompt 14A controlled-contract implementation and its executed evidence.

The full implementation report is [14A_SEMANTIC_CONTRACT_IMPLEMENTATION_REPORT.md](../qa_backups/14A_SEMANTIC_CONTRACT_IMPLEMENTATION_REPORT.md).

---

## 9. Prompt 14A-C2 trusted-input and semantic-gate hardening (2026-11-16)

Project X (106) confirmed the typed-contract architecture and reproduced five remaining defects: caller-controlled trusted inputs, incomplete material coverage, evidence not revalidated on the amendment path, substitute decision/owner authority, and an inaccurate Git-status count.

D-239 closes them without changing the contracts or numerical rules:

- `validate_amendment(request)` now accepts only a strict seven-field request; all trusted inputs (baseline contracts, schema, lexicon, evidence registry, source documents, `DECISIONS.md`, `AUTONOMOUS_DECISION_POLICY.md`, owner authorizations and projection templates) are loaded by a fixed `TrustedContext` from canonical repository paths. Overrides and aliases fail `CONTRACT_TRUSTED_INPUT_OVERRIDE`; path traversal and symbolic links fail path-protection errors.
- Evidence is revalidated against actual source bytes, hashes, sections, excerpts, proposition identity, scope, classification and review metadata on every amendment.
- `material_coverage()` performs complete span accounting and detects inserted material before, between, inside and after expected fragments. The exact insertion “B-04 binary floating-point calculations are permitted” is rejected at every tested position.
- The amendment path executes four independent gates: contract integrity, evidence integrity, D-014 authority and complete comparison.
- The fabricated D-940 attack is rejected: request-supplied decision text or owner authorizations fail the request gate; `decision_ref = D-940` fails the authority gate against the real register.

**Executed results:** numerical validator **64/64 checks and 150/150 self-tests**; contract validator **9/9**; original contract suite **83/83**; new trusted-input/semantic-gate suite **46/46**. The 295 formulas, 393 parameter records, 20 B-03 carry-ins, nine registers, both B-04 hashes and the empty production manifest are preserved. All production evidence mappings remain `NOT_REVIEWED`; no human review or owner authorization is claimed.

**Git correction:** the live tree has **17 modified tracked files, 33 untracked files (50 total), 43 `git status --short` display lines and 0 staged changes**. The previous 40 figure was a display-line count, not a file count. The Project X (106) audit's 152/23/175 could not be reproduced from the supplied snapshot in this environment; the read-only snapshot comparison and the live counts are recorded in the [C2 report](../qa_backups/14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md). No Git operation was performed.

**Status:** Prompt 14A remains **OPEN**; owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**.

The C2 report is [14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md](../qa_backups/14A_TRUSTED_INPUT_AND_SEMANTIC_GATE_HARDENING_REPORT.md).

---

## 10. Prompt 14A-C3 final QA reconciliation and documentation closeout (2026-11-17)

The Project X (107) audit confirmed the C2 fixes and identified four remaining closeout issues. All four are resolved without changing the contract model or numerical rules.

### 10.1 Contract-level metadata diff

`diff_contracts()` now reports `metadata_changes` for `contract_version`, `effective_decision` and `lifecycle_status` with previous value, proposed value, change flag and a classification of `UNCHANGED`, `AUTHORIZED`, `PROVISIONAL`, `UNAUTHORIZED` or `INVALID`. The classification is assigned after the contract, evidence and D-014 authority gates from their actual results; it never makes a change valid. The authority gate independently rejects a candidate whose `effective_decision` differs from the request `decision_ref`. The contract, evidence, authority and comparison gates remain separate.

### 10.2 Complete numerical self-test execution

The baseline self-test run took **2m23.817s**. Safe text-hash memoization of immutable reads and parsers reduced the complete run to **1m00.094s** without removing, skipping or weakening any case. The complete suite executed **150/150** tests, all passed, with exit status 0 and deterministic repeated results. No test was silently skipped.

### 10.3 Git status reconciliation

Read-only inspection with `git status --short --untracked-files=all` reports **17 modified tracked paths, 36 untracked individual files, 53 individual paths, 46 default display lines and 0 staged changes** (the untracked count includes the C3 report). The audit's 152/33/185 figures are not reproduced by `git status --short --untracked-files=all`, `git diff --name-status` or the snapshot `.git` index against the live worktree in this environment. The difference is attributed to the audit environment's Git index, line-ending/filter state or a different measurement; no file was staged, reverted or discarded to force agreement. The previous 40/50 figure was a display-line count, not an individual-path count.

### 10.4 File inventory

The C3 report contains a complete file-level inventory with previous and final SHA-256 for every C3-created or C3-modified file. Earlier C2 changes remain attributed to C2; no earlier change is reclassified as C3.

### 10.5 Executed results

| Suite | Result |
|---|---|
| Numerical foundation validator | **64/64 checks** |
| Numerical self-tests | **150/150 executed and passed** |
| Contract production validator | **9/9 checks** |
| Original contract suite | **83/83 tests** |
| C2 security suite | **46/46 tests** |
| C3 metadata-diff suite | **8/8 tests** |
| Decision-register tests | **12/12** |
| Next-action tests | **27/27** |
| Documentation links | **0 unresolved** |

The 295 formulas, 393 parameter records, 20 B-03 carry-ins, nine registers, both B-04 hashes and the empty production manifest are preserved. D-014, D-045/D-064, D-238 and D-239 are unchanged. All production evidence mappings remain `NOT_REVIEWED`; no human review or owner authorization is claimed.

**Status:** Prompt 14A remains **OPEN**; owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**. The consolidated closeout evidence is in [14A_FINAL_QA_CLOSEOUT_REPORT.md](../qa_backups/14A_FINAL_QA_CLOSEOUT_REPORT.md).

---

## 11. Prompt 14A-C4 final Git-status and handoff closeout (2026-11-17)

C4 made no source, formula, parameter, contract or validator change. It reconciles reporting and handoff state before the owner's planned commit.

**Repository-wide Git status.** The exact command `git status --porcelain=v1 --untracked-files=all` was executed read-only on 2026-11-17. Live result: **17 modified tracked paths, 38 untracked individual files, 55 individual paths, 48 default `git status --short` display lines, 0 staged changes.** `git diff --name-status` reports 17 modified, 0 added/deleted/renamed; `git diff --cached --name-status` reports 0.

The 17 modified tracked paths are the total accumulated tracked changes. They are not C3/C4-specific: C3 changed 14 files and created 3; C4 changes documentation only. The 38 untracked individual files include the 33 pre-existing Prompt 14A artifacts, the 3 C3-created files, the C4 prompt archive and the C4 precommit report.

The Project X (108) audit's **152 modified / 36 untracked / 188 total / 0 staged** is preserved as an audit-environment observation. It is not reproduced by the live Git index or by the Project X (108) snapshot `.git` index against the live worktree in this environment. The audit's 36 untracked count matches the pre-C4 live count; C4 later added two files, so the final untracked count is 38. The 152 modified count does not match. The difference is attributed to the audit environment's Git index, line-ending/filter normalization or a different measurement. The live counts are the authoritative repository-wide record; no file was staged, reverted or discarded to force agreement.

**Handoff banner.** `docs/AI_HANDOFF.md` now begins with **CURRENT PROJECT POSITION — 17 NOVEMBER 2026** and states: Prompt 13A–13D owner accepted; Prompt 13 fully owner accepted; Prompt 14A numerical foundation substantially complete; semantic-contract architecture implemented; C2 and C3 implemented; C4 complete at the documentation/reporting level; Prompt 14A awaiting formal owner acceptance; Prompt 14B not authorized. The November 16 semantic-contract banner is preserved as **SUPERSEDED / HISTORICAL**. `AI_CONTEXT.md` agrees.

**Generated cache artifacts.** The two modified Python bytecode cache files are:

- `docs/qa_backups/__pycache__/14A_contract_validator.cpython-312.pyc`
- `docs/qa_backups/__pycache__/14A_validate_numerical_foundation.cpython-312.pyc`

They are generated artifacts, ignored by `.gitignore` (`__pycache__/`, `*.pyc`), not tracked and not substantive source changes. They were not deleted, manipulated or reclassified; the ignore/tracking policy was not changed.

**Validation.** C4 changed documentation only. The documentation-link validator reports **0 unresolved**; `validate_final.py` reports **ALL CHECKS PASSED**; decision-register tests 12/12; next-action tests 27/27; the prompt archive/index validates. The expensive suites (150 numerical self-tests, 83 contract tests, 46 C2 tests, 8 C3 tests, 64/9 validators) were last executed to completion in C3 and were not rerun after documentation-only changes; they remain previously independently verified, not newly executed in C4.

**Preservation.** 295 formulas, 393 parameter records, 20 B-03 carry-ins, nine registers, both B-04 hashes, B-09 F-AL-006, the empty production manifest, D-014, D-045/D-064, D-238 and D-239 remain unchanged. All production evidence mappings remain `NOT_REVIEWED`; no human review or owner authorization is claimed.

**Status:** Prompt 14A remains **OPEN**; independent verification is recorded; formal owner acceptance is **PENDING and not claimed**. Prompt 14B remains **NOT AUTHORIZED / NOT STARTED**. The precommit report is [14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md](../qa_backups/14A_FINAL_PRECOMMIT_RECONCILIATION_REPORT.md).

**End of QA baseline report and C4 precommit reconciliation.**

---

## 7. Prompt 14B execution record (2026-11-17)

**14B-C1 closeout (2026-11-17).** The 35-row matrix tally was corrected to **27/4/4/0** (the earlier 27/6/5 summary mixed matrix rows with contradiction-register entries), and the 49-record D-014 category metadata was added to [the parameter inventory §6.1](22_numerical_parameter_inventory.md). The detailed evidence crosswalk is §8 below. No value, formula identity or numerical status changed.

**Scope.** Prompt 14B — B-04 economy, resources, income and treasury — reconciled the 47 active B-04 formulas and 49 B-04 parameter records, calculated the starting economy, the seven extraction chains, three generators, four recipes, maintenance, treasury, inventory, reference prices and margins, re-ran the 20 examples and added Examples A–H, built the 35-row cross-system matrix, and recorded F14B-01…F14B-20 without retuning a value. 35 dependency-matrix rows: 27 `VERIFIED CONSISTENT`, 4 `VERIFIED WITH DOCUMENTED LIMITATION`, 4 `CONTRADICTION IDENTIFIED`, 0 `NOT YET VERIFIED` (sum 35); separately, the 18-entry contradiction register and the 2 B-06 `OUTSIDE PROMPT 14B AUTHORITY` items are not part of the 35. See [25_prompt_14B_b04_economy_completion_report.md](25_prompt_14B_b04_economy_completion_report.md).

**Actual results.** The 14B validator `14B_verify_b04_economy.py` passes **321/321** checks and **4/4** self-tests. `verify_economy_numbers.py` passes **170/170**. City 267/267, market, diplomacy, alliance, warfare, 09_validate 371/371, 10B 1036 checks with 73/73 negative fixtures, 11B 61/61 with 52/52 gates and 0 unresolved links, 11C PASS, 12A PASS, 12B 87/87, 12C 24/24, 13A 34/34, 13B 28/28, 13C 27/27, 13D 75/75, 14A 64 checks 0 failed, contract 9/9, contract tests 83/83, C2 security 46/46, C3 metadata 8/8, `validate_final.py` ALL CHECKS PASSED, links 0 unresolved, decision registers 12/12, next action 27/27. The four inherited failures remain: politics 878/879, 11A 29/30, 09A 941/943 and 09B 8 frozen-range problems.

**Expectation advances.** The frozen register maxima in `validate_final.py`, `09_validate.py`, `12A_validate_foundations.py`, `13A`, `13B`, `test_next_action.py`, `14A_validate_numerical_foundation.py` and `verify_economy_numbers.py` were advanced to the D-243 / DD-289 / B-04 v1.5 / register v1.5 truth. No check was deleted, relaxed or converted into a warning.

**Controlled contracts.** The protected clauses `F-EC-000b` and `F-EC-000f` are byte-identical; the contracts and projections were not changed. The whole-document source hashes in `index.json` and `evidence_mappings.json` were refreshed after the legitimate B-04/B-14/DECISIONS amendments; all 11 evidence mappings remain `NOT_REVIEWED`, and no human review or owner authorization is claimed.

**Preservation.** 295 active formulas, 393 parameter records, 20 B-04 examples, 20 B-03 carry-ins, 11 resources, four recipes, three generators, 310 starting units, 1,500 crowns, 2,000 warehouse, 300 bp, the two-hour settlement, the four numerical statuses and every owner-reserved decision remain unchanged. No value was retuned; no formula was added, renumbered or retired.

**Status.** Prompt 14A is OWNER ACCEPTED (2026-11-17). Prompt 14B is **COMPLETE at the documentation, numerical-analysis and document-validation level**, not implemented and not balance-accepted. Prompt 14C–14K remain **NOT AUTHORIZED**. No Git staging or commit was performed.

---

## 8. Prompt 14B — Detailed Evidence Crosswalk

**Purpose.** This crosswalk maps each of the 17 required QA areas to its authoritative source, the supporting section/formula/parameter range, the completion-report section, the validator or test that exercised it, the actual result or limitation, and seven **separate** evidence dimensions. It is a navigation and traceability aid, **not** a second economic specification, and it does not collapse the dimensions into one overall PASS.

### 8.1 Evidence-status vocabulary

| Status | Meaning |
|---|---|
| `DOCUMENTED` | The rule, formula, parameter or analysis exists in an authoritative source and was checked structurally. |
| `NUMERICALLY VALIDATED` | The arithmetic, formula or invariant was checked by an actually executed validator or test. |
| `INTEGRATION CHECKED` | The ownership and cross-system contracts were checked against their authoritative sources. |
| `RUNTIME VERIFIED` | The behaviour was implemented and verified in a running application. **Not used in this report.** |
| `RUNTIME NOT VERIFIED` | No implementation, database, scheduler, API or UI exists; no runtime behaviour was observed. |
| `MIGRATION VERIFIED` | The relevant database or data migration was implemented and verified. **Not used in this report.** |
| `MIGRATION NOT VERIFIED` | A migration is in scope but was not implemented or verified. |
| `BALANCE TESTED` | Economic performance and strategic interactions were evaluated with actual balance evidence. **Not used in this report.** |
| `BALANCE NOT ACCEPTED` | The economic values are provisional and no balance acceptance is claimed. |
| `PLAYTESTED` | Actual playtests were conducted and their results recorded. **Not used in this report.** |
| `PLAYTESTING NOT EXECUTED` | No player, simulation or balance trial exists. |
| `NOT APPLICABLE` | The dimension does not apply to this category or scope. |
| `NOT YET VERIFIED` | The dimension applies but has no evidence yet. |

No row claims `RUNTIME VERIFIED`, `MIGRATION VERIFIED`, `BALANCE TESTED` or `PLAYTESTED`. `NOT APPLICABLE` is used in the Migration column because Prompt 14B defines no database or data migration; a later implementation stage must replace it with `MIGRATION NOT VERIFIED` or `MIGRATION VERIFIED` if one is created. **Prompt 14B is a documentation, formula, numerical-analysis and cross-system consistency phase; it creates no runtime economy, no production database migration, no accepted balance and no gameplay test.** `NOT APPLICABLE` is a scope statement: Prompt 14B defines no database schema or migration, so there is no migration to verify; a later implementation stage must change this status if one is created.

### 8.2 Source and result mapping

The **Primary status** column is a short summary only. The authoritative per-dimension record is §8.3.

| # | QA category | Authoritative source | Supporting section / formula / parameter range | Completion-report section | Validator / test | Result or limitation | Primary status |
|---:|---|---|---|---|---|---|---|
| 1 | Tax and income | B-04 rulebook; B-04 register | `ECN-094`, `ECN-146`; `F-EC-001`, `F-EC-003` | 14B §4.1 | `verify_economy_numbers.py` 170/170; `14B_verify_b04_economy.py` 321/321 | Standard 150; 100,000 people 300; 600 bp hunger 282; full starvation 105 | `NUMERICALLY VALIDATED` |
| 2 | Resource inventory and accounting | B-04 rulebook §13; register §4.3 | `ECN-119`–`ECN-130`; `F-EC-021`–`F-EC-023`, `F-EC-028`–`F-EC-030` | 14B §4.7, §6 | `14B_verify_b04_economy.py` conservation checks | `310+106−69=347` (Example G); 11-resource deltas reconcile | `NUMERICALLY VALIDATED` |
| 3 | Starting economy and initial parameters | B-04 §3.1; D-063; parameter inventory §6 | `ECN-121`; register §3.1; the 24 §3.1 records | 14B §3 | `14B_verify_b04_economy.py` constants and Example H checks | 310 units, 600 book, 2,100 wealth, 1,690 free, closing 1,499 | `NUMERICALLY VALIDATED` |
| 4 | Extraction and production chains | B-04; register §3.2 | `ECN-042`/`ECN-046`/`ECN-049`/`ECN-148`; `F-EC-004`/`F-EC-005` | 14B §4.3 | `14B_verify_b04_economy.py` extraction and margin checks | Seven chains; capacity binds at the standard start; base margins +7/−1/+1/−1/+1/+1/+1 | `NUMERICALLY VALIDATED` |
| 5 | Manufacturing and processing recipes | B-04 §10; D-046; register §3.3 | `ECN-066`–`ECN-079`; `F-EC-006`–`F-EC-012` | 14B §4.5 | `14B_verify_b04_economy.py` margin and dominance checks | Four recipes unchanged; loaded margins 0/+5/+2/+4; Example 4 155/23 | `NUMERICALLY VALIDATED` |
| 6 | Food demand and civilian/military boundaries | B-04 §11; B-10 `F-WR-036` | `ECN-080`–`ECN-091`, `ECN-214`; `F-EC-002`, `F-EC-002a`, `F-EC-003` | 14B §4.2, §6 Examples C and F | `14B_verify_b04_economy.py` food checks | 50/100 demand; 0/600/3,000 bp; military ration separate and whole-cancelled; B-10 quantity not changed | `NUMERICALLY VALIDATED` |
| 7 | Power demand, generation and fuel | B-04 §9; register §3.4 | `ECN-056`–`ECN-065`; `F-EC-006`, `F-EC-007`, `F-EC-008`, `F-EC-013` | 14B §4.4 | `14B_verify_b04_economy.py` power and utilisation checks | 6 GU; 2/6 used; 3.00/GU marginal vs 9.00/GU actual; fail-closed fuel | `NUMERICALLY VALIDATED` |
| 8 | Maintenance and operating costs | B-04 `ECN-051`, `ECN-105`, `ECN-147`, `ECN-147a` | `F-EC-014`; register §3.3/§3.4 | 14B §4.6 | `14B_verify_b04_economy.py` maintenance checks; `verify_economy_numbers.py` ECN-147a block | 11-crown standard start; 1 crown pays oil; whole cancellation | `NUMERICALLY VALIDATED` |
| 9 | Treasury, reservations, cash flow and closing balances | B-04 §12; register §4.3 | `ECN-092`–`ECN-118`, `ECN-125`–`ECN-128`; `F-EC-018`, `F-EC-019`, `F-EC-020` | 14B §4.7, Example G | `14B_verify_b04_economy.py` treasury identity | `1,500+135−11−80−10−20−30=1,484`; reservations never reduce total | `NUMERICALLY VALIDATED` |
| 10 | Reference prices, margins and payback | Register §3.5/§5; D-058 | `F-EC-031`, `F-EC-032`, `F-EC-036`, `F-EC-037` | 14B §4.8 | `14B_verify_b04_economy.py` margin and payback checks | Gasoline 6.00, steel 6.375, aluminum 7.75, ammunition 5.60; Example 4 155/23 | `NUMERICALLY VALIDATED` |
| 11 | Conservation and reconciliation | Register §4.3/§4.4 | `F-EC-024`, `F-EC-025`, `F-EC-026`, `F-EC-029`, `F-EC-030`, `F-EC-035` | 14B §4.7, §6 | `14B_verify_b04_economy.py` conservation checks | Resource, treasury, wealth and alliance identities in A/G and the 30-turn model | `NUMERICALLY VALIDATED` |
| 12 | Worked economic examples A–H | 14B report §6; B-04 §20 | Examples 1–20; Examples A–H | 14B §6 | `14B_verify_b04_economy.py`; `verify_economy_numbers.py` | 28 examples reproduce; Example 4 corrected to 155/23 | `NUMERICALLY VALIDATED` |
| 13 | Cross-system dependency matrix | 14B report §5; B-02/B-03/B-05–B-10 sources | X-01…X-35; C-01…C-18 register | 14B §5 | `14B_C1_validate_closeout.py` B-checks | 35 rows, 27/4/4/0; 18-entry register separate; 2 B-06 items outside authority | `INTEGRATION CHECKED` |
| 14 | Parameter ownership and D-014 category metadata | Parameter inventory §6/§6.1 | 49 records; source IDs remain `None`; categories A/B/C/D | 14B §2.3; inventory §6.1 | `14B_C1_validate_closeout.py` A-checks | 49/49 Category C; 0 A/B/D; 0 unresolved; values and statuses unchanged | `DOCUMENTED` |
| 15 | Exploit, dominance and money-creation | Register §5; 14B report §4.9/§4.10 | `F-EC-038`, `F-EC-039`; F14B-01…F14B-20 | 14B §4.9, §4.10 | `14B_verify_b04_economy.py` 30-turn checks | Gross 4,500 vs 4,476 (fails by 24); net passes; idle fails; no exploit loop; balance not accepted | `NUMERICALLY VALIDATED` |
| 16 | Validation scripts and actual execution results | 14B report §8; this report §7 | 35 command rows | 14B §8 | `validate_final.py`; `validate_links.py`; the 14B §8.1 validators | Actual pass/fail counts in §8.1; four inherited failures preserved | `NUMERICALLY VALIDATED` |
| 17 | Limitations and runtime/playtesting | 14B report §9; B-04 `ECN-228`; register `F-EC-046` | §9.1–§9.4 | 14B §9 | None (no runtime or playtest exists) | No implementation, simulation, player or balance acceptance; playtesting required | `DOCUMENTED` |

### 8.3 Evidence-dimension matrix

Every row is assessed separately for all seven dimensions. `NOT APPLICABLE` is used only where the dimension genuinely does not apply to that category or to the Prompt 14B scope.

| # | QA category | Documentation | Numerical validation | Integration consistency | Runtime implementation | Migration | Gameplay balance | Playtesting |
|---:|---|---|---|---|---|---|---|---|
| 1 | Tax and income | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 2 | Resource inventory and accounting | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 3 | Starting economy and initial parameters | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 4 | Extraction and production chains | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 5 | Manufacturing and processing recipes | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 6 | Food demand and civilian/military boundaries | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 7 | Power demand, generation and fuel | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 8 | Maintenance and operating costs | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 9 | Treasury, reservations, cash flow and closing balances | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 10 | Reference prices, margins and payback | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 11 | Conservation and reconciliation | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 12 | Worked economic examples A–H | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 13 | Cross-system dependency matrix | `DOCUMENTED` | `NOT APPLICABLE` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `NOT APPLICABLE` | `NOT APPLICABLE` |
| 14 | Parameter ownership and D-014 category metadata | `DOCUMENTED` | `NOT APPLICABLE` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `NOT APPLICABLE` | `NOT APPLICABLE` |
| 15 | Exploit, dominance and money-creation | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |
| 16 | Validation scripts and actual execution results | `DOCUMENTED` | `NUMERICALLY VALIDATED` | `INTEGRATION CHECKED` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `NOT APPLICABLE` | `NOT APPLICABLE` |
| 17 | Limitations and runtime/playtesting | `DOCUMENTED` | `NOT APPLICABLE` | `NOT APPLICABLE` | `RUNTIME NOT VERIFIED` | `NOT APPLICABLE` | `BALANCE NOT ACCEPTED` | `PLAYTESTING NOT EXECUTED` |

**Supporting evidence for each verified status.** The source/section/validator mapping in §8.2 is the evidence for `DOCUMENTED`, `NUMERICALLY VALIDATED` and `INTEGRATION CHECKED`. `RUNTIME NOT VERIFIED`, `NOT APPLICABLE`, `BALANCE NOT ACCEPTED` and `PLAYTESTING NOT EXECUTED` are supported by the absence of any implementation, schema, balance trial or playtest in the repository and are recorded in 14B report §9.

### 8.4 Scope boundary

Prompt 14B and 14B-C1/R1 do not create a runtime economy, a verified production database migration, accepted economic balance, completed gameplay testing or production readiness. No row claims any of them. A later implementation or playtest stage must add evidence and change the relevant cell rather than reinterpreting this table.

## 9. Crosswalk maintenance rule

The crosswalk is updated only when an authoritative section, formula ID, validator, evidence dimension or status changes. It must never be used to upgrade a documentation or arithmetic result into a runtime, migration, balance or playtesting claim. A future subphase that implements, migrates, balances or playtests a category must add that evidence explicitly rather than reinterpreting an existing row.

**End of Prompt 14B execution record.**
