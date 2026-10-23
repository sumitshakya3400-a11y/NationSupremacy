# Supabase feasibility prototype

**Not game code.** A bounded spike that tests the owner-selected architecture:
Cloudflare for the website, Supabase PostgreSQL for the turn engine. Synthetic
data only — no accounts, no players, no gameplay, no economy.

- Public preview: **https://nation-supremacy.pages.dev** (Cloudflare Pages)
- Backend: Supabase project **Nation Supremacy**, ref `lqdzchtfxrbtwsrpkrzo`, region `ap-south-1`
- Recorded results: [Report 12](../../docs/stage-1/12_nation_supremacy_deployment_and_resource_separation.md)
  and [results/nation-supremacy-project.json](results/nation-supremacy-project.json)
- Earlier run against the retired project: [Report 11 §§14–20](../../docs/stage-1/11_free_tier_feasibility_results.md)

## Layout

```
site/index.html                     the public page (single file, no build step)
scripts/build-pages-worker.mjs      wraps the page in a Pages `_worker.js` -> dist/
migrations/0001_schema.sql          isolated `feasibility` schema, tables, RLS policies
migrations/0002_functions.sql       slot arithmetic + batched, idempotent turn resolver
migrations/0003_grants_and_rls.sql  least-privilege grants, RLS locks
migrations/0004_schedule.sql        the single pg_cron schedule (0 */2 * * *)
results/nation-supremacy-project.json   what this run measured
```

## What it demonstrates

| Claim | Mechanism |
|---|---|
| One shared turn per two-hour UTC boundary | `feasibility.current_slot()` = `floor(epoch/7200)` |
| A slot cannot be resolved twice | `turn_runs.slot` primary key + status check before any work |
| A nation-turn cannot be applied twice | `(slot, nation_id)` primary key on `turn_applied` |
| A batch is all-or-nothing | one SQL statement per batch; a raised error rolls the batch back |
| Long worlds can be resumed | `turn_runs.cursor` advances forward-only; `resolve_slot` loops batches |
| Clients cannot move money or complete turns | `revoke execute` on the resolver; `select` only on `nations` |
| Players cannot read each other's rows | RLS policy on `feasibility.profiles` keyed to the JWT `sub` |
| Cron can drive it | `pg_cron` job `0 */2 * * *` calling `resolve_current_turn()` |
| The page is served by Cloudflare | Pages project `nation-supremacy`, production URL above |

## Apply the migrations

Any of these work; the first is what was used, through the connected Supabase
integration (`apply_migration`):

```bash
psql "$DATABASE_URL" -f migrations/0001_schema.sql
psql "$DATABASE_URL" -f migrations/0002_functions.sql
psql "$DATABASE_URL" -f migrations/0003_grants_and_rls.sql
psql "$DATABASE_URL" -f migrations/0004_schedule.sql
```

Every statement is `if not exists` / `create or replace` (the schedule is
unscheduled by name first), so re-applying is safe. The schema is `feasibility`;
nothing in `public` is touched — in the current project `public` is empty.

## Exercise the engine

```sql
insert into feasibility.nations (id, label)
select g, 'Synthetic Nation ' || g from generate_series(1, 1000) g
on conflict (id) do nothing;

select feasibility.current_slot(now());          -- the shared slot for "now"
select feasibility.resolve_turn(248992, 250);    -- one batch, commits on return
select feasibility.resolve_slot(248993, 250);    -- whole slot, one transaction
```

`resolve_turn` returns JSON: `outcome` (`partial`, `completed`, `noop`,
`busy`, `rejected`), `applied_this_batch`, `nations_applied`, `remaining`,
`cursor`, `duration_ms`.

The fourth argument of `resolve_turn` is a **test hook** (`p_force_error_at`):
passing a nation id raises an exception after the batch's value change, which is
how the rollback behaviour is measured. It is not used by the cron entry point.

## Schedule it

`migrations/0004_schedule.sql` does this; manually:

```sql
select cron.schedule('nation-supremacy-turn', '0 */2 * * *',
                     $$select feasibility.resolve_current_turn(250)$$);
select jobname, schedule, active from cron.job;
select * from cron.job_run_details order by start_time desc limit 5;
```

`resolve_current_turn` also writes a row to `feasibility.cron_heartbeat`, so a
firing is visible even when the slot is already completed and the resolver
no-ops. Remove a job with `select cron.unschedule('nation-supremacy-turn');`.

## Build and deploy the page

```bash
node scripts/build-pages-worker.mjs     # -> dist/pages-worker.js (+ .b64)
```

The script fails if the page loses the official name, mentions the internal
codename or the retired brand, or contains anything that looks like a credential.

**Why Advanced Mode.** The Pages *static asset* endpoint (`/pages/assets/upload`)
requires an `Authorization: Bearer <upload JWT>` header that the connected
Cloudflare integration cannot set, so an asset deployment is impossible from this
environment. The deployment endpoint does accept an inline `_worker.js` part,
which Pages runs as an Advanced Mode function, so the page is served from the
project root by that function. Consequences, stated plainly:

- The site is on Pages at the URL above and returns correct status codes and
  security headers, but it is a function response, not a static-asset response.
  Static assets remain the preferred production path (free and unmetered).
- A `_routes.json` with `include: ["/*"]` is required: without it Pages'
  asset router intercepts `/` and returns 500 when the deployment has no
  `index.html`.

Deploying is done by POSTing `manifest` (a JSON field, *not* a file part),
`_worker.js`, and `_routes.json` as `multipart/form-data` to
`/accounts/{account_id}/pages/projects/nation-supremacy/deployments`. The
`_worker.js` source is ASCII-only so it can be carried as base64 and verified by
SHA-256 before sending.

## Limits of the evidence

- The overlapping-invocation test was **serialised by the tool**: the second call
  ran after the first completed, so the advisory-lock path has not been exercised
  under true concurrency. The unique constraints are the tested defence.
- `duration_ms` is server-side function time, not network or client time.
- 1,000 nations is an exploratory size. No capacity target is approved.
- No backup or restore drill was performed; the free plan has no provider-managed
  backups (see Report 11 §15).
- The scheduler evidence in this project is three consecutive one-minute firings
  plus a configured two-hour product job. No two-hour boundary has yet been
  observed in this project.
