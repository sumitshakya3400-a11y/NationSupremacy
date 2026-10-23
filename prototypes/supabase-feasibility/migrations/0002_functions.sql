-- 0002_functions.sql — shared two-hour UTC turn resolution.
--
-- Three functions:
--   feasibility.current_slot(ts)         -> the 2-hour UTC slot number for a timestamp
--   feasibility.resolve_turn(slot, n)    -> applies ONE batch of up to n nations, commits on return
--   feasibility.resolve_slot(slot, n)    -> loops batches inside one transaction (cron entry point)
--
-- Exactly-once rests on three mechanisms, not on application logic:
--   1. `turn_runs.slot` is the primary key, so a slot cannot be claimed twice.
--   2. `(slot, nation_id)` is the primary key of `turn_applied`, so a nation-turn
--      cannot be applied twice, even by concurrent batches.
--   3. The batch takes a transaction-scoped advisory lock, so two invocations
--      cannot interleave batches for the same world.

create or replace function feasibility.current_slot(p_at timestamptz default now())
returns bigint
language sql
immutable
as $$
  -- 7200-second bins from the Unix epoch; epoch 0 is a 00:00 UTC boundary, so
  -- every bin boundary is an even UTC hour.
  select floor(extract(epoch from p_at) / 7200)::bigint;
$$;

create or replace function feasibility.resolve_turn(
  p_slot   bigint,
  p_batch  integer default 250,
  p_run_id text    default null,
  p_force_error_at bigint default null   -- test hook: raise when this nation is seen
)
returns jsonb
language plpgsql
security definer
set search_path = feasibility, pg_temp
as $$
declare
  v_run_id        text := coalesce(p_run_id, 'run-' || p_slot::text);
  v_last_completed bigint;
  v_run           feasibility.turn_runs%rowtype;
  v_cursor        bigint;
  v_new_cursor    bigint;
  v_seen          integer;
  v_applied        integer;
  v_remaining     bigint;
  v_started       timestamptz := clock_timestamp();
begin
  if p_slot is null or p_slot < 0 then
    return jsonb_build_object('outcome', 'rejected', 'reason', 'invalid slot');
  end if;
  if p_batch is null or p_batch < 1 or p_batch > 10000 then
    return jsonb_build_object('outcome', 'rejected', 'reason', 'batch size out of range');
  end if;

  -- Serialise resolvers for the duration of this transaction.
  if not pg_try_advisory_xact_lock(hashtext('feasibility.resolve_turn')) then
    return jsonb_build_object('outcome', 'busy', 'reason', 'another resolver holds the lock');
  end if;

  select max(slot) into v_last_completed
    from feasibility.turn_runs where status = 'completed';

  if v_last_completed is not null and p_slot < v_last_completed then
    return jsonb_build_object(
      'outcome', 'noop', 'reason', 'older than the last completed slot',
      'last_completed', v_last_completed, 'slot', p_slot);
  end if;

  insert into feasibility.turn_runs (slot, status)
    values (p_slot, 'running')
    on conflict (slot) do nothing;

  select * into v_run from feasibility.turn_runs where slot = p_slot for update;

  if v_run.status = 'completed' then
    return jsonb_build_object(
      'outcome', 'noop', 'reason', 'slot already completed', 'slot', p_slot,
      'nations_applied', v_run.nations_applied, 'batches', v_run.batches);
  end if;

  v_cursor := v_run.cursor;

  with candidates as (
    select n.id
      from feasibility.nations n
     where n.id > v_cursor
     order by n.id
     limit p_batch
     for update
  ), bounds as (
    select max(id) as max_id, count(*)::integer as seen from candidates
  ), ins as (
    insert into feasibility.turn_applied (slot, nation_id, delta)
    select p_slot, c.id, 10
      from candidates c
    on conflict (slot, nation_id) do nothing
    returning nation_id, delta
  ), upd as (
    update feasibility.nations n
       set treasury = n.treasury + i.delta,
           last_slot = p_slot,
           updated_at = now()
      from ins i
     where n.id = i.nation_id
    returning n.id
  ), aud as (
    insert into feasibility.audit (slot, nation_id, delta, run_id)
    select p_slot, i.nation_id, i.delta, v_run_id from ins i
    returning 1
  )
  select b.max_id, b.seen, (select count(*)::integer from ins)
    into v_new_cursor, v_seen, v_applied
    from bounds b;

  -- The test hook lives *after* the value change on purpose: if it raises, all
  -- of the batch rolls back, which is the failure mode this test is measuring.
  if p_force_error_at is not null and v_new_cursor is not null and v_new_cursor >= p_force_error_at then
    raise exception 'injected failure at nation %', p_force_error_at
      using errcode = 'P0001';
  end if;

  if v_seen = 0 then
    update feasibility.turn_runs
       set status = 'completed',
           completed_at = now()
     where slot = p_slot
       and status = 'running'
    returning * into v_run;

    return jsonb_build_object(
      'outcome', 'completed', 'slot', p_slot,
      'nations_applied', v_run.nations_applied, 'batches', v_run.batches,
      'applied_this_batch', 0,
      'duration_ms', round(extract(epoch from clock_timestamp() - v_started) * 1000, 3));
  end if;

  select count(*) into v_remaining from feasibility.nations where id > v_new_cursor;

  update feasibility.turn_runs
     set cursor = v_new_cursor,
         nations_applied = nations_applied + v_applied,
         batches = batches + 1
   where slot = p_slot
  returning * into v_run;

  if v_remaining = 0 then
    update feasibility.turn_runs
       set status = 'completed', completed_at = now()
     where slot = p_slot
    returning * into v_run;
  end if;

  return jsonb_build_object(
    'outcome', case when v_run.status = 'completed' then 'completed' else 'partial' end,
    'slot', p_slot,
    'applied_this_batch', v_applied,
    'nations_applied', v_run.nations_applied,
    'batches', v_run.batches,
    'remaining', v_remaining,
    'cursor', v_new_cursor,
    'duration_ms', round(extract(epoch from clock_timestamp() - v_started) * 1000, 3));
end;
$$;

create or replace function feasibility.resolve_slot(
  p_slot        bigint,
  p_batch       integer default 250,
  p_max_batches integer default 200
)
returns jsonb
language plpgsql
security definer
set search_path = feasibility, pg_temp
as $$
declare
  v_started timestamptz := clock_timestamp();
  v_result  jsonb;
  v_batches integer := 0;
begin
  loop
    v_result := feasibility.resolve_turn(p_slot, p_batch, 'cron-' || p_slot::text);
    v_batches := v_batches + 1;

    exit when v_result ->> 'outcome' in ('completed', 'noop', 'busy', 'rejected');
    exit when v_batches >= p_max_batches;
  end loop;

  return v_result || jsonb_build_object(
    'batches_run', v_batches,
    'duration_ms', round(extract(epoch from clock_timestamp() - v_started) * 1000, 3));
end;
$$;

-- Cron entry point: resolve whatever slot the current instant belongs to.
create or replace function feasibility.resolve_current_turn(p_batch integer default 250)
returns jsonb
language plpgsql
security definer
set search_path = feasibility, pg_temp
as $$
declare
  v_slot bigint := feasibility.current_slot(now());
  v_out  jsonb;
begin
  v_out := feasibility.resolve_slot(v_slot, p_batch);

  insert into feasibility.cron_heartbeat (job, slot)
    values ('resolve_current_turn', v_slot);

  return v_out || jsonb_build_object('slot', v_slot);
end;
$$;

create or replace function feasibility.cron_tick(p_job text default 'heartbeat')
returns void
language sql
security definer
set search_path = feasibility, pg_temp
as $$
  insert into feasibility.cron_heartbeat (job, slot)
    values (p_job, feasibility.current_slot(now()));
$$;
