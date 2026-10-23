# Supabase feasibility prototype

**Not game code.** A bounded spike that tests the owner-selected architecture:
Cloudflare for the website, Supabase PostgreSQL for the turn engine. Synthetic
data only — no accounts, no players, no gameplay, no economy.

Read [Report 11 §14](../../docs/stage-1/11_free_tier_feasibility_results.md) for
the recorded results and the limitations that go with them.

## Layout

```
site/index.html                 the public page (single file, no build dependencies)
scripts/build-site.mjs          wraps the page in a Worker script -> dist/worker.js
migrations/0001_schema.sql      isolated `feasibility` schema, tables, RLS policies
migrations/0002_functions.sql   slot arithmetic + batched, idempotent turn resolver
migrations/0003_grants_and_rls.sql  least-privilege grants, RLS locks
results/deployed-supabase.json  what actually happened, as measured
```

## What it demonstrates

| Claim | Mechanism |
|---|---|
| One shared turn per two-hour UTC boundary | `feasibility.current_slot()` = `floor(epoch/7200)`, identical to the browser and the D1 spike |
| A slot cannot be resolved twice | `turn_runs.slot` primary key + `status` check before any work |
| A nation-turn cannot be applied twice | `(slot, nation_id)` primary key on `turn_applied` |
| A batch is all-or-nothing | one SQL statement per batch; a raised error rolls the whole batch back |
| Long worlds can be resumed | `turn_runs.cursor` advances forward-only; `resolve_slot` loops batches |
| Clients cannot move money or complete turns | `revoke execute` on the resolver; `select` only on `nations` |
| Players cannot read each other's rows | RLS policy on `feasibility.profiles` keyed to the JWT `sub` |
| Cron can drive it | `pg_cron` job `0 */2 * * *` calling `resolve_current_turn()` |

## Apply the migrations

Any of these work; the first is what was used, through the connected Supabase
integration (`apply_migration`):

```bash
psql "$DATABASE_URL" -f migrations/0001_schema.sql
psql "$DATABASE_URL" -f migrations/0002_functions.sql
psql "$DATABASE_URL" -f migrations/0003_grants_and_rls.sql
```

Every statement is `if not exists` / `create or replace`, so re-applying is safe.
The schema is `feasibility`; nothing in `public` is touched.

## Exercise the engine

```sql
insert into feasibility.nations (id, label)
select g, 'Synthetic Nation ' || g from generate_series(1, 1000) g
on conflict (id) do nothing;

select feasibility.current_slot(now());          -- the shared slot for "now"
select feasibility.resolve_turn(248992, 250);    -- one batch, commits on return
select feasibility.resolve_slot(248993, 250);    -- whole slot, one transaction
```

`resolve_turn` returns JSON: `outcome` (`partial`, `completed`, `noop`),
`applied_this_batch`, `nations_applied`, `remaining`, `cursor`, `duration_ms`.

The fourth argument of `resolve_turn` is a **test hook** (`p_force_error_at`):
passing a nation id raises an exception after the batch's value change, which is
how the rollback behaviour was measured. It is not used by the cron entry point.

## Schedule it

```sql
select cron.schedule('nation-supremacy-turn', '0 */2 * * *',
                     $$select feasibility.resolve_current_turn(250)$$);
select * from cron.job;
select * from cron.job_run_details order by start_time desc limit 5;
```

`resolve_current_turn` also writes a row to `feasibility.cron_heartbeat`, so a
firing is visible even when the slot is already completed and the resolver
no-ops.

Remove a job with `select cron.unschedule('nation-supremacy-turn');`.

## Build and deploy the page

```bash
node scripts/build-site.mjs     # -> dist/worker.js
```

The page is deployed as Worker `nation-supremacy` on
`https://nation-supremacy.nationsphere.workers.dev`.

The connected Cloudflare integration can upload a Worker script but cannot set
the `Authorization` header the Workers static-assets upload requires, so the page
is served by the Worker itself. Production should use static assets (free and
unmetered) or Pages; neither was used here. See Report 11 §14.2.

## Limits of the evidence

- The overlapping-invocation test was **serialised by the tool**: the second call
  ran after the first completed, so the advisory-lock path has not been exercised
  under true concurrency. The unique constraints are the tested defence.
- `duration_ms` is server-side function time, not network or client time.
- 1,000 nations is an exploratory size. No capacity target is approved.
- No backup or restore drill was performed; the free plan has no provider-managed
  backups (see Report 11 §15).
