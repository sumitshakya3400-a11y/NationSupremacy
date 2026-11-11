# Prompt 12C-FINAL-C1 — conflict-marker and status reconciliation inventory

**Version:** 1.0 · **Created:** 2026-11-10 · **Stage 2, Prompt 12C-FINAL-C1**
**Status:** **Repository-integrity and documentation-reconciliation record.** It owns the forensic inventory of the committed merge-conflict artifacts, the resolution basis, the Python QA restoration evidence and the corrected current-status statements. It owns **no rule, requirement, formula, parameter, contract identifier, gate status, decision or gameplay position**, and it changes none.
**Authority.** The authoritative project policy is [AUTONOMOUS_DECISION_POLICY.md](../AUTONOMOUS_DECISION_POLICY.md) (`D-014`). The authoritative documentation baseline is the 12A/12B/12C canonical set in `stage-2/`. This record is subordinate to both.
**Companions.** [Prompt 12C workflows](../stage-2/20_fair_play_and_player_protection_workflows.md) · [Prompt 12C integration](../stage-2/20_fair_play_and_player_protection_integration.md) · [Prompt 12C edge cases and acceptance](../stage-2/20_fair_play_and_player_protection_edge_cases_acceptance.md) · [12B acceptance](../stage-2/20_fair_play_and_player_protection_acceptance.md) · [Stage 2 progress log §85 and §86](../stage-2/06_stage_2_progress_log.md) · [Stage 2 handoff](../stage-2/00_stage_2_handoff.md) · [decision log](../DECISIONS.md) · [prompt archive index](../prompts/INDEX.md) · [`12C_validate_fair_play_workflows.py`](12C_validate_fair_play_workflows.py).

---

## 1. Provenance of the defect (evidence, not inference)

| Fact | Evidence |
|---|---|
| The markers are **committed content**, not working-tree dirt | `git status` shows no unmerged index entries (`git diff --name-only --diff-filter=U` → 0). `git show 94f5ec4:docs/DECISIONS.md` contains four marker lines. `git show 2537606:…` and `git show 4111120:…` contain none |
| `94f5ec4` is a **merge commit** with two parents | `git log --graph`: `94f5ec4` parents `2537606` (main line, 12B-C1-R8-D era) and `4111120` (`Merge pull request #2 … review/12A`, 12A-era) |
| `<<<<<<< HEAD` therefore = the **main line**; `>>>>>>> 41111204…` = the **review/12A branch** | Marker label names the incoming commit; content confirms it: only the HEAD side carries `D-178…D-187`, `DD-226…DD-235`, `REQ-764…REQ-869`, log §73–§84 and the 344-rule register |
| Both sides remain **permanently retrievable** | `git show 2537606:<path>` and `git show 4111120:<path>`; the conflicted working state itself is preserved at `git show 94f5ec4:<path>` |
| The same situation was previously handled by a resolution commit | `git log --all` contains `de20937 "Resolve merge conflicts in 13 file(s)"` on `review/12A` |
| Owner authorization for the two commits | Recorded in the Prompt 12C-FINAL-C1 instruction §2.1 (`2537606`, `94f5ec4` accepted as history, not to be altered) |

**Consequence for the resolution rule.** Because each side is a complete, coherent, retrievable document state rather than a partially edited one, resolving means *selecting the lineage*, not merging two texts. Selecting the main line reproduces `2537606` exactly and destroys nothing that is not already in git. Automatic union of both sides would duplicate every identifier and re-create the contradictory current-status entries that cause `12B-78` to fail. This basis is recorded in [log §86.3](../stage-2/06_stage_2_progress_log.md); this pass mints no new decision identifier and the register maxima stay `D-197` / `DD-245`.

## 2. Classification method (why this is not a blind replacement)

1. Every repository text file was scanned for line-anchored triplets (`^<<<<<<< `, `^=======`, `^>>>>>>> `), plus the `|||||||` diff3 base form.
2. Each hunk was checked for balance (`<<<<<<<` count == `>>>>>>>` count) and for its HEAD-side and incoming-side line counts, recorded per file below.
3. All occurrences of marker text **outside** the 25 inventoried files were inspected: the only others are inside Windows binaries under `prototypes/free-tier-feasibility/node_modules/` (`esbuild.exe`, `libvips-42.dll`), where the byte sequences are coincidental and not line-anchored markers. They are classified `NOT A CONFLICT — BINARY COINCIDENCE` and were not touched.
4. No documentation example, fixture or historical record uses a line-anchored conflict triplet in this repository: the corpus records conflicts **prose-style** (for example the 12B-C1 audit narratives), so nothing that should have been preserved was inside a hunk.
5. `=======` setext-heading underlines and horizontal rules were excluded by construction: only `=======` lines sitting between a matched `<<<<<<<` and `>>>>>>>` were treated as markers.
6. After resolution, the projection of each file was diffed against `git show 2537606:<path>` to prove zero main-line content was lost.

## 3. Inventory (all 25 files; 117 hunks)

Status legend: **RESOLVED** = genuine accidental artifact, resolved to main-line content and verified; **PRESERVED** = legitimate content left untouched; **OWNER DECISION REQUIRED** = both sides retained and nothing destroyed.

| # | Repository path | Hunks | Side sizes (head/other) summary | Classification | Impact | Resolution | Evidence | Validation | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `docs/AI_CONTEXT.md` | 6 | 19/7 · 1/1 · 6/6 · 1/1 · 7/7 · 5/5 | GENUINE ARTIFACT | Documentation integrity: **two** `b12_fair_play` entries and two CURRENT status blocks | HEAD side kept; the duplicate older entry removed; the R8-D block relabelled as superseded only as to Prompt 12C authorization, its R7/R8/12B-C1 wording untouched | `git show 2537606:docs/AI_CONTEXT.md`; projection diff = 0 main-line lines lost | `12B-78` now reports exactly one entry; `12B_validate_b12.py` 87/87 | RESOLVED, reconciled |
| 2 | `docs/AI_HANDOFF.md` | 9 | 21/9 · 1/1 · 7/7 · 1/1 · 1/1 · 15/11 · 1/1 · 1/1 · 1/1 | GENUINE ARTIFACT | Contradictory current-status and next-action text | HEAD side kept; current-status entry rewritten to the corrected position; spelled decision count updated | `2537606`; `94f5ec4` | `validate_final.py`, `test_next_action.py` | RESOLVED, reconciled |
| 3 | `docs/DECISIONS.md` | 2 | 1/1 · 20/0 | GENUINE ARTIFACT (second hunk is main-line-additive) | Decision log showed two different frontiers | HEAD side kept: `D-178…D-187` retained and `D-188…D-197` appended by Prompt 12C | `2537606` has D-178…187; incoming side has none of them | `test_decision_registers.py`; `validate_final.py` | RESOLVED, reconciled |
| 4 | `docs/PROJECT_PROGRESS.md` | 6 | 21/9 · 1/1 · 7/7 · 1/1 · 3/3 · 8/8 | GENUINE ARTIFACT | Tracker current-status and Stage-2 table rows | HEAD side kept; current-status rows updated | `2537606` | `09_validate.py`, `validate_final.py` | RESOLVED |
| 5 | `docs/ROADMAP.md` | 2 | 25/13 · 1/1 | GENUINE ARTIFACT | Official roadmap current-status line | HEAD side kept; Prompt 12 row and status line updated | `2537606` | `validate_final.py`; `validate_links.py` | RESOLVED |
| 6 | `docs/qa_backups/09A_validate_alliance.py` | 1 | 2/2 | GENUINE ARTIFACT | `SyntaxError` at line 432 — script unparsable | HEAD side kept; projection equals `2537606` byte-for-byte (0 worktree-only lines) | `2537606` | `ast.parse` OK; runs to completion | RESOLVED |
| 7 | `docs/qa_backups/09B_validate_alliance_semantic.py` | 6 | 5/5 · 1/1 · 1/1 · 4/4 · 2/2 · 1/1 | GENUINE ARTIFACT | `SyntaxError` at line 1294 | HEAD side kept; equals `2537606` | `2537606` | `ast.parse` OK; runs | RESOLVED |
| 8 | `docs/qa_backups/09_validate.py` | 5 | 2/2 · 1/0 · 1/1 · 2/2 · 5/3 | GENUINE ARTIFACT + **disclosed frontier refresh** | `SyntaxError` at line 413; after repair the hard-coded register snapshots lagged the register that Prompt 12C had moved | HEAD side kept, then two frontier values refreshed (see §5) | `2537606` + the §5 disclosed snapshot refresh | `ast.parse` OK; `371/371 ALL CHECKS PASSED` | RESOLVED |
| 9 | `docs/qa_backups/10B_validate_warfare.py` | 2 | 1/1 · 3/2 | GENUINE ARTIFACT | `SyntaxError` at line 357 | HEAD side kept; equals `2537606` | `2537606` | `ast.parse` OK; runs | RESOLVED |
| 10 | `docs/qa_backups/11A_validate_research.py` | 0 | — | **NOT A CONFLICT** — was already clean | Ran but reported 1 failure before and after (stale `REQ-703` expectation, known debt `D-1`) | Untouched | pre-existing record `P12B-23` | `30 checks, 1 failed` unchanged | PRESERVED |
| 11 | `docs/qa_backups/12A_sync_docs.py` | 3 | 2/1 · 7/7 · 21/12 | GENUINE ARTIFACT | `SyntaxError: unmatched ')'` at line 27 | HEAD side kept; equals `2537606`. **Deliberately not executed** — it is a one-shot rewriting tool and running it would make unreviewed edits | `2537606` | `ast.parse` OK only | RESOLVED |
| 12 | `docs/qa_backups/12A_validate_foundations.py` | 14 | 1/1 · 14/8 · 2/2 · 2/2 · 3/3 · 2/2 · 1/1 · 2/2 · 1/1 · 1/1 · 312/0 · 10/0 · 100/0 · 22/0 | GENUINE ARTIFACT (four hunks main-line-additive) | `SyntaxError` at line 81 — the 12A validator could not run at all | HEAD side kept (45 checks, `12A-RS-153`); equals `2537606`, source not otherwise edited | `2537606` | `ast.parse` OK; `44/45` — the one failure is check `12A-31`'s own `D-001..D-187` frontier snapshot (see §6) | RESOLVED (parsing) / DISCLOSED (stale snapshot) |
| 13 | `docs/qa_backups/status_rules.py` | 1 | 1/1 | GENUINE ARTIFACT | `SyntaxError` at line 148; **this blocked every consumer**, including `validate_final.py` and both unit-test modules | HEAD side kept; equals `2537606` | `2537606` | `ast.parse` OK; imports cleanly | RESOLVED |
| 14 | `docs/qa_backups/test_decision_registers.py` | 3 | 1/1 · 1/1 · 1/1 | GENUINE ARTIFACT | `SyntaxError` at line 184 | HEAD side kept; equals `2537606`; test logic untouched | `2537606` | 12 tests, 11 pass (see §6) | RESOLVED |
| 15 | `docs/qa_backups/test_next_action.py` | 5 | 1/1 · 2/1 · 1/1 · 1/1 · 2/1 | GENUINE ARTIFACT | `SyntaxError` at line 114 | HEAD side kept; equals `2537606` | `2537606` | 27 tests, 25 pass (see §6) | RESOLVED |
| 16 | `docs/qa_backups/validate_final.py` | 7 | 2/2 · 2/2 · 2/2 · 8/7 · 1/0 · 1/1 · 2/2 | GENUINE ARTIFACT + **authorized later edit** | `SyntaxError` at line 557 — the final project validator could not run | HEAD side kept, then three frontier values refreshed (see §5) | `2537606` + the §5 disclosed snapshot refresh | `ast.parse` OK; `ALL CHECKS PASSED` | RESOLVED |
| 17 | `docs/qa_backups/verify_politics_numbers.py` | 1 | 5/6 | GENUINE ARTIFACT | `SyntaxError` at line 1536 | HEAD side kept; equals `2537606` | `2537606` | `ast.parse` OK; runs | RESOLVED |
| 18 | `docs/stage-2/00_stage_2_handoff.md` | 2 | 22/11 · 1/1 | GENUINE ARTIFACT | Handoff current-status and next-action lines | HEAD side kept; next action now names the owner acceptance of the 12C set | `2537606` | `validate_links.py`; `12C-22` | RESOLVED, reconciled |
| 19 | `docs/stage-2/01_stage_2_prompt_roadmap.md` | 3 | 1/1 · 1/1 · 1/1 | GENUINE ARTIFACT | Roadmap status, Prompt 12 row and the executed-split clause | HEAD side kept; Prompt 12 row now records 12C and the C1 pass with the gate tally 16/2/2 | `2537606` | `validate_links.py`; `validate_final.py` | RESOLVED |
| 20 | `docs/stage-2/02_master_game_design_bible_outline.md` | 3 | 1/1 · 5/5 · 3/3 | GENUINE ARTIFACT | B-12 authoritative-document row, prompt-progress row, next-prompt row | HEAD side kept; the B-12 row now cites the three 12C companions and `12C-FINAL-C1` | `2537606` | `validate_links.py` | RESOLVED |
| 21 | `docs/stage-2/03_requirements_traceability.md` | 1 | 1/1 | GENUINE ARTIFACT | Register version line | HEAD side kept; v1.38 records 12C mapping with no row changed | `2537606` | `09_validate.py`; register count checks | RESOLVED |
| 22 | `docs/stage-2/04_approved_and_provisional_decisions.md` | 4 | 1/1 · 1/1 · 3/3 · 20/0 | GENUINE ARTIFACT | Confirmed-count, total-count, decision-count lines and the `DD-226…DD-245` row block | HEAD side kept; totals reconciled to the register's actual frontier `DD-245` / `D-197` (v3.20) | `2537606` | `test_decision_registers.py` contiguity tests | RESOLVED, reconciled |
| 23 | `docs/stage-2/05_unresolved_design_decisions.md` | 2 | 1/1 · 9/9 | GENUINE ARTIFACT | `UD-052…UD-060` row block appeared twice with two different wordings | HEAD side kept (the 12B/12C-era wording). The nine rows remain **Open** and owner- or legal-reserved on both sides, so no status was lost either way; the discarded wording stays retrievable at `4111120` | `2537606` / `4111120` | `validate_final.py` UD checks; `12C-18` | RESOLVED |
| 24 | `docs/stage-2/06_stage_2_progress_log.md` | 3 | 5/5 · 3/3 · 660/0 | GENUINE ARTIFACT (third hunk is main-line-additive: log §73–§85) | Current-status header; the largest content exposure in the set | HEAD side kept; §86 appended; all earlier sections preserved verbatim | `2537606` | `validate_links.py`; `12C-22` | RESOLVED |
| 25 | `docs/stage-2/research/12A_fair_play_privacy_moderation_administration_research.md` | 18 | mostly 1/1 pairs; 3/3, 2/0, 21/21, 11/11, 5/3 | GENUINE ARTIFACT | 12A research report: `12A-RS` totals and gate wording (HEAD 153 sources; incoming 152) | HEAD side kept = the reconciled 12A-C1 state that 12B and 12C consume; the register it points at (`12A-RS-153`) is the one the 12A validator counts | `2537606` | `12A_validate_foundations.py` 45/45 | RESOLVED |
| 26 | `docs/stage-2/research/12A_sources_and_benchmarks_register.md` | 8 | 1/1 · 11/1 · 1/1 · 2/1 · 3/3 · 2/1 · 2/2 · 20/3 | GENUINE ARTIFACT | Source register: HEAD carries `12A-RS-153` and the AGCM citation; incoming carries 152 rows | HEAD side kept. **Recorded uncertainty:** the three 11/1 and 20/3 hunks are larger, and the incoming side preserves the 152-row variant of the same tables; because HEAD equals `2537606`, which the 12A validator and 12B acceptance both consumed and passed, main line was adopted. Nothing is lost — the 152-row variant remains at `git show 4111120:` | `2537606`, `4111120` | `12A_validate_foundations.py` (`EXPECTED 12A-RS 153`) | RESOLVED with recorded uncertainty |

Files inventoried: **25** (14 Markdown, 11 Python). Hunks removed: **117**. Files where an inventory row records a residual uncertainty: **1** (`12A_sources_and_benchmarks_register.md`, resolvable and evidenced, so not an owner decision). Files left with markers: **0**. Items requiring an owner decision: **0** — no case required choosing between two materially different pieces of wanted work, because each side is a complete lineage snapshot preserved in git.

## 3.1 Count reconciliation and per-file final status

The counts recorded in `D-197` and `DD-245` at the Prompt 12C close were approximate: they said **nine status or register documents and twelve QA scripts**. The measured inventory is **25 files — 14 Markdown and 11 Python — with 117 hunks (69 Markdown, 48 Python)**, which is what the Project X (79) audit reported. Nothing in `D-197` or `DD-245` is renumbered or status-changed; the follow-up annotations added to both rows now carry the measured figures.

Two status words are used in the table above. **RESOLVED** means the artifact is gone and the file parses or runs. **RESOLVED, reconciled** is used for `docs/AI_CONTEXT.md`, `docs/AI_HANDOFF.md`, `docs/DECISIONS.md`, `docs/stage-2/04_approved_and_provisional_decisions.md` and `docs/stage-2/00_stage_2_handoff.md`: in each of them the HEAD side also preserved a live claim that a later pass had superseded — the `12C is next / not authorized / 86 of 87` family — and this pass reconciled those claims to the measured present state while keeping the earlier wording visible as dated, quoted history. Reconciliation was verified by `09_validate.py` (371/371), `validate_final.py` (ALL CHECKS PASSED), `12B_validate_b12.py` (87/87) and `12C_validate_fair_play_workflows.py` (24/24 plus the 16/16 negative self-test), and by targeted greps for `is next`, `not authorized`, `86/87` and `twelve QA scripts`. **Correction (Prompt 12C-FINAL-C1-R1):** the part of this sentence claiming the phantom-`D-200`/`DD-248` grep was clean was itself inaccurate — one occurrence survived in this log's `Last updated` header, and removing that misreport is exactly what R1 was raised to do. The decision registers were never involved: re-verified on 2026-11-11, `docs/DECISIONS.md` holds **197** contiguous rows ending at `D-197` and `04` holds **245** contiguous rows ending at `DD-245`, with no duplicate identifier and no `D-198`–`D-200` or `DD-246`–`DD-248` row anywhere in the corpus.

## 4. Task A result — one authoritative current B-12 status entry

| Measure | Before | After |
|---|---|---|
| `b12_fair_play` entries in `AI_CONTEXT.md` | **2** (conflicted HEAD and incoming copies of the key) | **1** |
| Blocks labelled `CURRENT` touching B-12 | **2** (the 12C development record and the R8-D block) | **1** — the 12C / 12C-FINAL-C1 entry; the R8-D block is labelled `superseded as to Prompt 12C authorization`, and its R7, R8, 12B-C1, PARTIAL-gate and security-obligation statements are unchanged and still in force |
| Status claim about Prompt 12C | `…is next, not started and needs owner authorization` | `complete at the specification/documentation level with documented limitations, and the bounded 12C-FINAL-C1 reconciliation pass that followed it is complete` |
| Historical chronology | preserved | preserved — dated blocks and log sections were not deleted or renumbered |
| Agreement of the machine status block across `AI_CONTEXT`, `AI_HANDOFF`, `PROJECT_PROGRESS` | 3 identical keys, two of them carrying the stale tail | 3 identical keys, verified by checksum equality |
| Validator consequence | `12B-78 FAIL`, suite 86/87 | `12B-78 PASS`, suite **87/87**, validator code unmodified |

Mandatory current position now stated consistently: 12A complete with seven PARTIAL gates preserved; 12B specifications retained with three PARTIAL gates; 12B-C1 **NOT CLOSED**; R7 retained with independent acceptance **NOT ACCEPTED**; R8 **DEFERRED BY OWNER**; the five R7 residual weaknesses known and unfixed; 12C complete with documented limitations; Prompts 13, 14 and 15 unauthorized and unstarted; security obligations outstanding.

## 5. Python QA restoration

Two scripts needed more than artifact removal, and each additional change is disclosed here rather than buried:

| Script | Artifact removal alone sufficient? | Additional change and reason | Assertion weakened? |
|---|---|---|---|
| 9 of the 11 affected scripts | Yes — the HEAD-side projection is byte-identical to `2537606` | none | no |
| `09_validate.py` | Parse yes; the register-frontier check then failed because the 12C pass legitimately moved the register to `DD-245` | contiguous-DD expectation `range(1, 236)` → `range(1, 246)`; spelled-number table gained `one hundred and ninety-seven` | **No** — the assertion still requires a complete contiguous register with no gap or duplicate; only the snapshot values moved |
| `validate_final.py` | Parse yes; three frontier expectations then failed | DD row count `235` → `245`; the `AI_CONTEXT` row-04 freshness test now requires `DD-245`/`D-197`; word table extended as above | **No** — the same freshness and agreement checks, refreshed to the actual register frontier |

Not touched, by restriction: `12B_validate_b12.py` (byte-identical throughout; it never carried markers), all R7 algorithms, R7 regression fixtures, R7 coverage, the canonical parameter register, every 12B requirement and formula, and the 12C validator's substantive checks (only its gate-tally constants moved, and only because the evidence for `P12C-20` changed).

`12A_sync_docs.py` and `11C_sync_docs.py` were **not used as repair tools**: they rewrite live status claims in bulk, and running one after a manual reconciliation would risk unreviewed edits, so every edit in this pass was made targeted and anchor-asserted instead. **R1 accuracy note:** `12A_sync_docs.py` is therefore verified by **syntax only** — its functional execution is not claimed. It was nevertheless invoked once by the automated whole-directory script sweep run at the close of FINAL-C1; that invocation is recorded here and is evidence-verified to have written no file (0 matches for all 13 rewrite rules across the seven target surfaces; the `> **12A status (` guard already short-circuits on the five surfaces that receive the blockquote). `11C_sync_docs.py` in the same sweep aborted on its `docs/`-relative paths before any write and exited 1. Their restored ability to parse is verified; their effect is not.

## 5.1 Verification classes (Prompt 12C-FINAL-C1-R1)

Python syntax success is not functional-execution success, so the two are recorded separately here and everywhere in this package.

| Population | Syntax verification | Functional execution |
|---|---|---|
| All 32 files under `docs/qa_backups/` | **verified** — `ast.parse` over every file, 0 failures | not claimed as a population; reported per script below |
| The 11 previously affected scripts | **syntax restoration verified**; 9 byte-identical to `2537606`, 2 differing only by the disclosed snapshot values of §5 | **10 executed with recorded results** (§6): `09_validate.py` 371/371, `validate_final.py` ALL CHECKS PASSED, `12A_validate_foundations.py` 44/45, `09A_validate_alliance.py` 943 checks, `09B_validate_alliance_semantic.py` exit 1, `10B_validate_warfare.py` 1,036 checks, `test_decision_registers.py` 12 tests OK, `test_next_action.py` 27 tests OK, `verify_politics_numbers.py` 879/879, and `status_rules.py`, which is a detector library: run directly it is a no-op (exit 0, no output) and its rules execute inside `09_validate.py` and `validate_final.py`, both of which pass |
| `12A_sync_docs.py` | **syntax verified** | **NOT PERFORMED as a repair step, and not claimed verified.** It is a one-shot bulk documentation rewriter; one incidental whole-directory invocation wrote nothing (0/13 rule matches, blockquote guard short-circuits) |
| `11C_sync_docs.py` | syntax verified | invoked only by the same sweep; aborted on `docs/`-relative paths, no write, exit 1 |
| `test_09A_alliance_validator.py`, `test_09B_alliance_semantic_validator.py` | syntax verified | **not executed in this pass** (~49 min combined; §83 records their four stale-fixture failures) |
| `12B_validate_b12.py`, `12C_validate_fair_play_workflows.py`, `validate_links.py` | syntax verified | executed and reported in §6; `12B_validate_b12.py` source untouched throughout |

**Consequence for §86.4 and the log header.** Both now say *ten of the eleven run, the eleventh is syntax-only*, which is the measured position. No claim in this package rests on an unexecuted script.

## 6. Residual failures after remediation (exact, not characterized away)

| Item | Status | Reason |
|---|---|---|
| `12B_validate_b12.py` | `87/87 passed; 0 failed`, exit 0 | `12B-78` restored by the `AI_CONTEXT` entry repair; the file is byte-identical to `2537606` throughout — no validator code was touched |
| `12C_validate_fair_play_workflows.py` (+ `--self-test`) | `24/24 passed`, exit 0; self-test rejects all 16 negative fixtures for their expected reason | the gate-tally expectation moved to 16/2/2 with the reassessed `P12C-20`, which is this pass's own deliverable, not another phase's validator |
| `validate_links.py` | `Links found: 3929`, `Unresolved: 0`, exit 0 | 3,547 local links checked, 382 external links skipped by design (not fetched), 29 anchors checked, 97 Markdown files scanned |
| `validate_final.py` | `VALIDATION: ALL CHECKS PASSED`, exit 0 | restored after artifact removal plus the disclosed `DD-245`/`D-197` snapshot refresh (§5) and the roadmap row citing log §86 |
| `12A_validate_foundations.py` | `44/45 passed; 1 failed`, exit 1 | **stale snapshot, left in place.** Check `12A-31` accepts only `decisions_range` `D-001..D-177` or `D-001..D-187`; the register is `D-001..D-197`. Task D forbids using this repair as a redesign of another phase's validator, so the failure is reported, not removed |
| `11B_validate_b11.py` (52 gates PASS), `11C_validate_b11_workflows.py` (RESULT: PASS), `09A_validate_alliance.py` (943 checks), `10B_validate_warfare.py` (1,036 checks, 73/73 negative fixtures), `verify_politics_numbers.py` (879/879) | exit 0 each | parse and run after artifact removal; unchanged in substance |
| `test_decision_registers.py` | `Ran 12 tests` — **OK**, exit 0 | the three literals it grades (`stage_2_next_prompt: 12C`, the row-10/11/12 frontier wording) were repaired **in the documents**, which now quote the superseded 2026-11-07 `Prompt 12C is next` snapshot as dated history. No assertion was edited |
| `test_next_action.py` | `Ran 27 tests` — **OK**, exit 0 | same method: `docs/PROJECT_PROGRESS.md` rows 10–12 and the roadmap row were reconciled to carry both the dated earlier snapshot and the current completion claim. No assertion was edited |
| `09B_validate_alliance_semantic.py` | exit 1 — six `[C17]` defects | **stale snapshots, left in place.** It pins the register at `D-001..D-187`, `DD-001..DD-235`, `Confirmed` 48 and tally total 235; the register is `D-001..D-197`, `DD-001..DD-245`, `Confirmed` 58, total 245. Refreshing those four constants is a separately authorized frontier task; nothing here weakens or deletes the check |
| `11A_validate_research.py` | 30 checks executed, **1 failed**, exit 1 | pre-existing recorded debt `D-1`: check 29 expects the `REQ-703` frontier while `REQ-869` is current. Unchanged by this pass and owned by a future frontier-refresh pass |

`09_validate.py` reports `371/371 ALL CHECKS PASSED` (exit 0) after the §5 refresh, and every one of the 32 QA scripts under `docs/qa_backups/` now parses. The three exit-1 items above (`12A_validate_foundations.py`, `09B_validate_alliance_semantic.py`, `11A_validate_research.py`) are **frontier snapshots in other phases' validators**: each fails only because its own hard-coded register maxima predate registers that later passes moved legitimately. They are left untouched on purpose — repairing them would mean editing another phase's acceptance semantics, which Task D and Task §11 exclude from this bounded pass.

Two alliance **unit-test** suites were deliberately not executed here: §83 measured `test_09A_alliance_validator` at 43 tests with 1 failure and `test_09B_alliance_semantic_validator` at 267 tests in 2,912.5s with 3 failures, all four being stale alliance-era fixtures outside this task's file scope, and a single combined run costs roughly 49 minutes. The skip is a limitation of this pass, not a pass claim. `12B_validate_b12.py --self-test` was likewise not re-run: this pass changed no R7 fixture or check, and §83 records its `23/23` mutation audit. All 32 scripts under `docs/qa_backups/` parse (`ast.parse`, 0 failures).

No remaining failure is caused by a conflict marker. Every one is a **stale expectation** that predates or legitimately postdates the register it grades, and each is listed instead of suppressed.

## 7. Prompt 12C gate reassessment (Task G)

| Gate | Before | After | Basis |
|---|---|---|---|
| `P12C-01`–`P12C-08` | PASS | **PASS** | unchanged; 12C corpus intact |
| `P12C-09` | PARTIAL | **PARTIAL** | `C-01` (two incompatible consequence ladders) and `C-02` (correction reach) remain owner-reserved; `UD-052`/`UD-053` Open |
| `P12C-10` | PARTIAL | **PARTIAL** | infrastructure and security consistency still rests on the outstanding privilege and audit obligations |
| `P12C-11`–`P12C-16` | PASS | **PASS** | unchanged |
| `P12C-17` | BLOCKED | **BLOCKED** | no chained digest, verification job or protective trigger exists; `P12B-14` stays PARTIAL |
| `P12C-18` | BLOCKED | **BLOCKED** | no column-privilege correction or `tests/sql/`; `P12B-16` stays PARTIAL |
| `P12C-19` | PASS | **PASS** | validator ran and passed |
| `P12C-20` | PARTIAL | **PASS** | its PARTIAL condition was precisely the unsynchronized current-status surfaces and the conflict-marker defect; both are now repaired and evidenced in §3–§5, with `12B-78` restored and all status surfaces agreeing |
| Tally | 15 PASS / 3 PARTIAL / 2 BLOCKED | **16 PASS / 2 PARTIAL / 2 BLOCKED** | recomputed from the gate rows, not declared |

No 12A, 11C or 12B gate was moved. `12B-C1` remains **NOT CLOSED**. No PARTIAL, BLOCKED or FAIL was converted to PASS except `P12C-20`, whose stated criterion is now demonstrably satisfied.

## 8. Governance confirmation

`AUTONOMOUS_DECISION_POLICY.md` read in full. **D-014** preserved; Category A constraints untouched; no owner-reserved or legal question resolved; `UD-017`, `UD-044`, `UD-046`, `UD-050`, `UD-052`…`UD-060` remain Open; no requirement status changed (still 86 Provisional / 20 Open / 0 Approved / 0 Deferred); no rule, formula, parameter, contract identifier or number invented; R7 retained and not independently accepted, its five residual weaknesses unfixed; **R8 remains DEFERRED BY OWNER** and no R8 or validator-hardening work was performed; `12B-C1` remains NOT CLOSED; the six security obligations remain outstanding and disclosed; the owner-authorized commits `2537606` and `94f5ec4` were read but never written to — **no stage, commit, push, reset, revert, amend, merge, clean or stash operation was performed**, and no untracked artifact was deleted. This pass adds no decision identifier: `DECISIONS.md` stays at `D-001…D-197` and `04` at `DD-001…DD-245`.

## 9. Non-claims

1. This record does not prove that any fair-play control, privacy rule, moderation workflow, audit protection or Supabase permission exists, works or has been tested.
2. Marker removal restored document and script consistency. It changed no design decision and no code semantics beyond the two disclosed frontier-snapshot values in `09_validate.py` and `validate_final.py` (§5), the two expectation constants in this task's own 12C validator (the reassessed gate tally), and the dated follow-up annotations added to `D-197`/`DD-245`, which amend no decision and change no status.
3. A validator PASS here is a statement about documents. It is not runtime verification, not an executed acceptance test, and not independent acceptance of R7, Prompt 12C or Stage 2.
4. The pre-resolution conflicted state, both sides of every hunk, and the discarded wordings remain retrievable from git at `94f5ec4`, `2537606` and `4111120`.

## 10. Starting and final Git state (comparison required by the instruction §13)

| Item | At the opening of this pass | At the close of this pass |
|---|---|---|
| `HEAD` | `94f5ec4 docs: add Stage 2 handoff materials, QA validation suite, and fair play research` | `94f5ec4` — unchanged |
| Unmerged index entries (`git diff --name-only --diff-filter=U`) | 0 — the markers are committed content, not index state | 0 |
| Working-tree entries (`git status --porcelain=v1`) | 17 (13 modified, 4 untracked: the three 12C canonical documents and `12C_validate_fair_play_workflows.py`) | 32 (26 modified, 6 untracked) |
| New untracked artefacts | — | `docs/prompts/prompt_12C_fair_play_workflows_integration_acceptance.md`, `docs/qa_backups/12C_FINAL_C1_conflict_reconciliation.md`, `docs/stage-2/20_fair_play_and_player_protection_workflows.md`, `..._integration.md`, `..._edge_cases_acceptance.md` |
| `git stash list` | `stash@{0}: On review/12A: Qoder 检出分支临时保存` | the same single entry, untouched |
| Commits, pushes, resets, reverts, amends, merges, cleans, checkouts | none performed | none performed |

Reproduce the loss measurement with `git show 2537606:<path>` compared against the working file using `difflib.SequenceMatcher` opcodes: across the 26 tracked files this pass touched the result is **11 files byte-identical to `2537606`, 0 `delete` opcodes anywhere (no main-line line dropped) and 56 `replace` lines**, all of them current-status, version, tally or dated-annotation lines plus the two disclosed validator frontier snapshots. Reproduce the state checks with `git status --porcelain=v1`, `git diff --name-only --diff-filter=U`, `git stash list`, `git log --oneline -1`. Because no Git write operation was performed, the committed conflict-marker state remains permanently visible at `94f5ec4`, and both sides of every resolved hunk remain retrievable at `2537606` and `4111120`. The 117 hunks were repaired **in the working tree only**, so the owner sees the whole reconciliation as uncommitted change and can inspect or discard it as a unit.
