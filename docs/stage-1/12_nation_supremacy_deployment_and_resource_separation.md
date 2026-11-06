# Report 12 — Nation Supremacy deployment and resource separation

**Version:** 1.0
**Date:** 2026-10-23
**Status:** Executed. Records what was actually created, tested, replaced and retired, and what remains blocked.
**Scope:** Deployment cleanup and replacement only. This report does not approve an architecture detail, a game mechanic, a capacity target or Stage 1 completion.

---

## 0. What this pass changed

| Item | Before | After |
|---|---|---|
| Public preview URL | `https://nation-supremacy.nationsphere.workers.dev` (Worker) | **`https://nation-supremacy.pages.dev`** (Pages) |
| Cloudflare Worker `nation-supremacy` | serving the preview | **deleted 2026-10-23T10:34:17Z** |
| Supabase project | `NATIONSPHERE` (`suotjamclwdithcitspe`, `ap-southeast-2`) | **`Nation Supremacy`** (`lqdzchtfxrbtwsrpkrzo`, `ap-south-1`) |
| Old Supabase project | active | **paused** — deletion blocked, see §9 |

The public page is a **technical feasibility preview**, not the game. It says so on the page, in its metadata description, and in every document here.

---

## 1. Initial live inventory

Read from the services themselves, not from earlier reports.

### Cloudflare (account `7bf870c15d1119f08a648c7f03c11c20`)

| Resource | State found | Action |
|---|---|---|
| Account `workers.dev` subdomain | `nationsphere` | **not changed** (shared by every Worker in the account) |
| Worker `nation-supremacy` | present, 2 deployments, no bindings, no cron, created 09:48Z | deleted after replacement verified |
| Worker `px-feasibility-spike` | present (D1 spike, historical evidence) | untouched |
| Worker `nationsphere-api` | **not present** in the live list | none — see §1.1 |
| Pages projects | **none** | created `nation-supremacy` |
| D1 databases | 1 (`px-feasibility-spike`) | untouched |

#### 1.1 A correction to earlier reports

Report 10 §1 and Report 11 §19 record an unrelated Worker `nationsphere-api` in this account, created 2026-09-17. The live script list during this pass contains exactly two Workers — `nation-supremacy` and `px-feasibility-spike` — and no `nationsphere-api`. Either it was removed between the earlier pass and this one, or that earlier observation was wrong. It could not be re-confirmed, so this report does not assert that it exists or that it was ever deleted by this project. Nothing was done to it.

### Supabase

| Resource | State found | Action |
|---|---|---|
| Organizations | one: `NATIONSPHERE`, id `cjppmvjnkjlzpvwebzai`, plan **free**, tier `tier_free` | none possible — see §6.1 |
| Project `NATIONSPHERE` | `suotjamclwdithcitspe`, `ap-southeast-2`, PostgreSQL 17.6.1.166, `ACTIVE_HEALTHY` | paused after replacement verified |
| Project `Nation Supremacy` | did not exist | created `lqdzchtfxrbtwsrpkrzo`, `ap-south-1` |
| Free-project limit | 2 active projects per organization; one was in use | the new project fits; no paid upgrade was needed |

---

## 2. Cloudflare Pages: project and verified behaviour

Created at **2026-10-23T10:25:28Z**:

```
name: nation-supremacy        production_branch: main
subdomain/domains: nation-supremacy.pages.dev   (the requested name was available)
```

Verified against the production URL after the final deployment (`cf5a492a-10a9-4c62-b41a-5ff93ba3f5d6`):

| Check | Result |
|---|---|
| HTTPS, `GET /` | **200**, `text/html; charset=utf-8`, 1,145 bytes |
| `<title>` | `Nation Supremacy` |
| visible `<h1>` | `Nation Supremacy` |
| honest self-description | "Technical feasibility preview" + "It is not the game." |
| `NationSphere` / `nationsphere` anywhere in the page | **0 occurrences** |
| link to the retired `.nationsphere.workers.dev` site | none (the page has no outbound links) |
| secret-looking content | none; the page is static text and CSS |
| claims of login/gameplay | none; the page states no accounts, no player data, no gameplay |
| `GET /health` | 200, JSON describing a feasibility preview |
| `GET /nonexistent` | 404 |
| `POST /` | 405 with `allow: GET, HEAD` |
| Security headers | `content-security-policy` (`default-src 'none'`), `x-content-type-options: nosniff`, `referrer-policy: no-referrer`, `x-frame-options: DENY`, `permissions-policy` |

### 2.1 Why the site runs as a Pages Function, not static assets

This is the honest, load-bearing limitation of the deployment.

1. A Pages **static** deployment requires uploading asset bytes to
   `/pages/assets/upload`, which authenticates with an `Authorization: Bearer
   <upload JWT>` header obtained from the project's `upload-token` endpoint. The
   connected Cloudflare integration cannot set request headers, so it receives
   **403 `8000013 Authorization failed`** on that endpoint even with a valid JWT
   in hand.
2. The deployment endpoint (`POST /pages/projects/{name}/deployments`) accepts
   only a `manifest` mapping paths to *already uploaded* hashes. Uploading file
   parts alongside the manifest is silently ignored: the deployment reports
   success, and the site returns **500** because the referenced content does not
   exist. Two such deployments were created and discarded during this pass
   (`918fc1b1`, `5672c222`) — the second is why the first verification attempt
   returned 500.
3. The same endpoint *does* accept an inline `_worker.js` part (Pages Advanced
   Mode). That is what is deployed. The page is served by that function; there
   are no static assets.

Consequences, stated rather than glossed:

- The URL, HTTPS, status codes, headers and content are real and verified.
- This is **not** the static-asset path, which remains the preferred production
  hosting (free and unmetered). Moving to it needs a deployment credential that
  can set headers, or a Git-connected Pages project.
- A `_routes.json` with `include: ["/*"]` is required. Without it, Pages' asset
  router intercepts `/` and returns 500 for a function-only deployment. The
  first Advanced Mode deployment without it served `/health` correctly and 500'd
  on `/`, which is how this was found.

---

## 3. Supabase: replacement project

| Field | Value |
|---|---|
| Display name | **Nation Supremacy** |
| Project reference | `lqdzchtfxrbtwsrpkrzo` |
| Region | `ap-south-1` (Mumbai) |
| PostgreSQL | 17.11.0.003 |
| Plan | free (`tier_free`), organization `cjppmvjnkjlzpvwebzai` |
| Created (API-reported) | 2026-10-23T09:23:12Z |
| Status at end | `ACTIVE_HEALTHY` |
| `public` schema | **empty** — the project carried no pre-existing objects |

**Region rationale.** The previous project was in `ap-southeast-2` (Sydney) and
measured 47–59 ms for a 1,000-nation slot. `ap-south-1` is the closest free
region to the owner's stated cost context and audience; the same workload now
measures 9.8–35.5 ms (§5.3). Region choice is a latency decision, not a branding
or quota one, and it is reversible only by creating another project.

**What was deliberately not copied.** No object, row, grant, auth setting or
secret from `NATIONSPHERE` — including its unrelated abandoned-game `public`
schema — was migrated. The new project was built only from the saved migrations
in `prototypes/supabase-feasibility/migrations/`.

### 3.1 Migrations applied

| File | Contents | Applied |
|---|---|---|
| `0001_schema.sql` | `feasibility` schema; `nations`, `turn_runs`, `turn_applied`, `audit`, `cron_heartbeat`, `profiles`; RLS policies on `profiles` | yes |
| `0002_functions.sql` | `current_slot`, `resolve_turn`, `resolve_slot`, `resolve_current_turn`, `cron_tick` | yes |
| `0003_grants_and_rls.sql` | revokes, selective grants, RLS enabled on the ledger tables | yes |
| `0004_schedule.sql` | `pg_cron` extension + job `nation-supremacy-turn` `0 */2 * * *` | yes |

`0004_schedule.sql` was added to the repository during this pass so the schedule
is reproducible from source rather than being a console-only action. Post-apply
inventory: 6 tables, 5 functions, 2 policies, 1 cron job, `public` empty.

---

## 4. Security boundaries, re-tested in the new project

| Test | Role | Result |
|---|---|---|
| Read own profile | `authenticated` (`sub=user-a`) | 1 row |
| Read another player's profile | `authenticated` | **0 rows** |
| Update own profile | `authenticated` | 1 row |
| Update another player's profile | `authenticated` | **0 rows** |
| Read the world (`nations`) | `authenticated` | 1,000 rows (intended) |
| Set a treasury balance directly | `authenticated` | `42501 permission denied for table nations` |
| Execute the turn resolver | `authenticated` | `42501 permission denied for function resolve_slot` |
| Read `profiles` signed out | `anon` | `42501 permission denied for table profiles` |

The browser-facing client therefore cannot move money, complete a turn, call the
resolver, or read another player's row. Service-role and database credentials
appear in no page, repository file or report; no secret was printed in this pass.

**Not tested:** Supabase Auth end-to-end (no sign-in flow exists in the
prototype), one-account-per-person enforcement, and true concurrent resolver
calls (§8).

---

## 5. Turn engine, idempotency, recovery

### 5.1 Slot arithmetic

| Instant | Slot |
|---|---|
| `2026-10-23T08:00:00Z` | 248992 |
| `2026-10-23T09:59:59Z` | 248992 |
| `2026-10-23T10:00:00Z` | 248993 |

Identical to the values measured in the previous project on the same day: the
slot is derived from the epoch, not stored per deployment, so a project move
does not shift the world clock.

### 5.2 Behavioural tests (1,000 synthetic nations)

| Test | Outcome |
|---|---|
| Batch of 250 (first call) | `partial`, 250 applied, 750 remaining, 9.763 ms |
| Resume to completion | `completed`, 1,000 applied, 4 batches |
| Full slot in one call (fresh slot) | `completed`, 1,000 applied, 4 batches, **35.488 ms** |
| Duplicate trigger on a completed slot | `noop`, "slot already completed", 0 applied |
| Older slot | `noop`, "older than the last completed slot" |
| Invalid batch size | `rejected`, "batch size out of range" |
| Injected failure at nation 100 | exception `P0001`, transaction rolled back |
| After the failure | **0** run rows, **0** markers, **0** audit rows, treasury unchanged, **0** nations touched |
| Retry after the failure | `completed`, 1,000 applied — no duplication |
| Conservation after four slots | 4,000 markers, 4,000 audit rows, treasury 40,000, 0 wrong rows, ledger `248992…248995 all completed 1000/4` |

The rollback evidence is the important one: the failure is injected *after* the
value change, and nothing survives it — not the ledger row, not the per-nation
markers, not the audit spine, not the treasury delta.

### 5.3 Timing and storage

| Measure | Value |
|---|---|
| First batch of 250 | 9.763 ms |
| Full 1,000-nation slot (4 batches) | 35.488 ms |
| Storage after 4,000 nation-turns | `turn_applied` 491,520 B; `audit` 565,248 B; `nations` 565,248 B |
| Derived marginal cost | **≈264 bytes per nation-turn** (page-quantised, 4,000-turn average) |
| Database total (empty otherwise) | 12.9 MB |

At 264 B, 1,000 nations × 12 turns/day is ≈3.2 MB/day, so the 500 MB free
database is roughly a 150-day budget without retention — consistent with the
291 B/turn measured earlier. Still an exploratory size, not an approved target.

---

## 6. Scheduler

`pg_cron` is installed in the new project and carries **one** job:

```
nation-supremacy-turn   [0 */2 * * *]   active = true
```

To obtain evidence that the mechanism actually fires — rather than trusting that
`cron.schedule` returned successfully — a temporary minute job was run and then
removed:

| Firing | Status | Heartbeat row |
|---|---|---|
| `2026-10-23T10:34:00Z` | succeeded | yes |
| `2026-10-23T10:35:00Z` | succeeded | yes |
| `2026-10-23T10:36:00Z` | succeeded | yes |

All three landed on the exact minute, `cron.job_run_details` records
`succeeded` for each, and `feasibility.cron_heartbeat` contains the three rows.
The job was then unscheduled; `select count(*) from cron.job` returns **1**, and
that one is the two-hour product job.

**What this does not prove.** No two-hour boundary has yet fired in this project.
The next even-hour boundary after creation is `12:00:00Z`, outside this session's
verification window, and twelve consecutive boundaries are still unobserved.
A real boundary firing was observed in the *previous* project at `10:00:00Z`
(Report 11 §7); that is historical evidence for the mechanism, not evidence for
this project's job.

### 6.1 Organization limitation

The owner asked for a new organization named **Nation Supremacy**. The connected
Supabase integration exposes `list_organizations`, `get_organization`,
`create_project`, `pause_project` and `restore_project` — but **no
organization-creation action and no project-deletion action**. The project was
therefore created with the requested name inside the only existing organization,
whose display name remains `NATIONSPHERE` (id `cjppmvjnkjlzpvwebzai`). Creating
the organization is a manual dashboard step; renaming the existing one is
possible there too, and would achieve the same separation without moving the
project.

This is a naming limitation, not a functional one: the project, its database, its
schema, its credentials and its data are entirely separate from the retired one.

---

## 7. Resource separation, verified

| Question | Evidence |
|---|---|
| Does the site depend on the retired Worker? | No. The page is served by the Pages function; the Worker was deleted and the URL now returns 404 / Cloudflare 1104. |
| Does the site or prototype depend on the retired project? | No. `results/deployed-supabase.json` retains the old reference as a **historical record only**; the live configuration is the new project, and the new project was built from migrations, not copied. |
| Are two turn schedulers running? | No. Supabase Cron is the only scheduler for this architecture. The D1 spike's own trigger is historical and its two-hour schedule belongs to that retired spike, not to this system. |
| Are unrelated resources untouched? | Yes: `px-feasibility-spike` and its D1 database still respond (200); the account `workers.dev` subdomain is unchanged; no other Supabase project was modified except the authorised pause. |
| Any secret in client code or the repository? | No. The page is static text and CSS; no key, token or connection string exists in `site/`, `dist/` or the report. |

---

## 8. What is verified, and what is not

| Statement | Status |
|---|---|
| The site is live at `https://nation-supremacy.pages.dev` and serves the branded preview | **verified by HTTP** |
| The site avoids `nationsphere` in its URL and content | **verified** |
| The retired Worker is removed and its URL dead | **verified** |
| A dedicated Supabase project named Nation Supremacy exists and is healthy | **verified** |
| Migrations reproduce the schema from source | **verified (4 applied, inventory matches)** |
| Exactly-once, resumability, rollback, conservation | **verified** |
| RLS and grants deny client writes/reads beyond policy | **verified** |
| The scheduler mechanism fires and records evidence | **verified for a minute job; not for a two-hour boundary in this project** |
| Twelve consecutive boundaries observed | **not done** |
| Backup and restore drill | **not done** — free plan has no provider-managed backups |
| True concurrent resolver execution | **not exercised** — the tool serialises calls |
| Supabase Auth end-to-end | **not exercised** |
| Dedicated Supabase organization named Nation Supremacy | **not created** — no connector action; manual step |
| Old `NATIONSPHERE` project deleted | **not deleted** — no connector action; paused instead |
| Capacity target approved | **no** |
| Cloudflare billing scope read | **still 403** |

---

## 9. Deletion results

| Target | Authorised | Result |
|---|---|---|
| Worker `nation-supremacy` | yes | **deleted** `2026-10-23T10:34:17Z` (`DELETE` returned 200; remaining scripts: `px-feasibility-spike` only). `https://nation-supremacy.nationsphere.workers.dev/` then returned **404, error 1104**, and the Pages URL still returned **200**. |
| Supabase project `NATIONSPHERE` (`suotjamclwdithcitspe`) | yes, after replacement verified | **not deleted**: the integration has no delete action. It was **paused** instead (`PAUSING` at 10:37Z) — reversible, and it stops the abandoned backend serving anything. |

Manual step to finish the authorised deletion: Supabase dashboard → project
`NATIONSPHERE` → Settings → General → **Delete project**, then confirm the name
`NATIONSPHERE`. This destroys the project's `feasibility` schema from Prompt 10.1
and its unrelated abandoned-game `public` schema (which held no rows). That loss
is what the owner authorised; it should be done knowingly.

---

## 10. Cost

No paid plan, add-on, domain or subscription was introduced.

| Item | Cost |
|---|---|
| Cloudflare Pages | free; the project is on the account's existing free plan |
| Cloudflare Worker (deleted) | free; removing it reduces usage |
| Supabase project | free plan, `$0/month` (`get_cost` returned amount 0 before creation) |
| Supabase organization | unchanged free tier |
| Domain | none purchased; `pages.dev` is provider-supplied |

The ₹0 objective is **supported for the tested configuration**, not guaranteed
indefinitely: both providers can change their free-tier terms, and the retention
and capacity questions in Report 11 §8 remain open.

---

## 11. Effect on the Stage 1 gates

No gate is promoted.

| Gate | Status | Why it did not move |
|---|---|---|
| GATE-13 | **CONDITIONAL** | Unchanged: OD-02, DEF-003 acceptance and the V-2/CV-002 sessions are still open. |
| GATE-16 | **CONDITIONAL** | The public site, a dedicated backend and a firing scheduler now exist and are verified — but there is still no 12-boundary observation, no backup/restore drill, and no Supabase Auth exercise. E-mail remains owner-blocked. |
| GATE-18 | **CONDITIONAL** | New measurements (35.5 ms/slot, 264 B/turn) are consistent with the earlier ones, but there is still no approved capacity target, no quota-exhaustion run, and no billing-scope verification. |

Stage 1 remains **incomplete — conditionally ready**.

---

## 12. Audit answers

| # | Question | Answer |
|---|---|---|
| 1 | Live Cloudflare inventory checked? | Yes — Workers, subdomain, Pages, D1 (§1). |
| 2 | Separate Pages project created? | Yes, `nation-supremacy`. |
| 3 | Exact working public URL? | **https://nation-supremacy.pages.dev** |
| 4 | Does it avoid `.nationsphere`? | Yes. |
| 5 | Nation Supremacy branding consistent? | Yes — title, `<h1>`, description. |
| 6 | Still honestly a feasibility preview? | Yes — "Technical feasibility preview", "It is not the game." |
| 7 | New Supabase organization created on Free plan? | **No** — no connector action exists; the project was created in the existing free organization (§6.1). |
| 8 | Separate project named Nation Supremacy created? | Yes, `lqdzchtfxrbtwsrpkrzo`. |
| 9 | Reference different from the old one? | Yes: `lqdz…` vs `suot…`. |
| 10 | Saved migrations executed? | Yes, all four, from source. |
| 11 | Permission and RLS checks passed? | Yes, 8/8 (§4). |
| 12 | Intended scheduler configured? | Yes, `0 */2 * * *`, one job only. |
| 13 | Scheduler runs observed? | Three minute-test firings at 10:34/35/36Z, all succeeded; no two-hour boundary yet (§6). |
| 14 | Old Worker removed only after replacement worked? | Yes — Pages verified first, deletion at 10:34:17Z. |
| 15 | Old `NATIONSPHERE` project deleted? | **No** — no delete action; paused instead (§9). |
| 16 | Unrelated resources changed or deleted? | No. |
| 17 | Configuration updated without exposing credentials? | Yes — no secret was written or printed. |
| 18 | Four continuity files updated consistently? | Yes (§13). |
| 19 | Report saved and cross-linked? | Yes — this file, linked from 11 and the continuity files. |
| 20 | Which gates remain conditional, and why? | GATE-13, GATE-16, GATE-18 (§11). |

---

## 13. Records updated

- [DECISIONS.md](../DECISIONS.md) — **D-009** (Pages address is the public site) and **D-010** (dedicated Nation Supremacy project; legacy project retired), both marked as this owner instruction. D-004 is untouched and still **Provisional**.
- [AI_CONTEXT.md](../AI_CONTEXT.md), [AI_HANDOFF.md](../AI_HANDOFF.md), [PROJECT_PROGRESS.md](../PROJECT_PROGRESS.md) — current URL, project, statuses and next task.
- [Report 11](11_free_tier_feasibility_results.md) — kept as the historical record of the earlier Worker and `NATIONSPHERE` project, with a forward-reference to this report. Its URL is **not** rewritten.
- `prototypes/supabase-feasibility/` — migrations (including `0004_schedule.sql`), `scripts/build-pages-worker.mjs`, README and `results/nation-supremacy-project.json`.

## 14. Official documentation consulted

- Pages deployments and API: <https://developers.cloudflare.com/pages/configuration/api/>
- Pages Advanced Mode: <https://developers.cloudflare.com/pages/functions/advanced-mode/>
- Workers limits and pricing: <https://developers.cloudflare.com/workers/platform/limits/>, <https://developers.cloudflare.com/workers/platform/pricing/>
- Supabase Cron: <https://supabase.com/docs/guides/cron>
- Supabase pricing and free plan: <https://supabase.com/pricing>
- Supabase backups: <https://supabase.com/docs/guides/platform/backups>
- Supabase row level security: <https://supabase.com/docs/guides/database/postgres/row-level-security>

---

**The site is a feasibility preview, not the completed game.** Stage 1 completion
still depends on the criteria in Report 10 §2, not on this deployment.
