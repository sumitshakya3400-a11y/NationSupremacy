-- 0001_schema.sql — isolated feasibility schema.
--
-- Everything lives in schema `feasibility`. Nothing in `public` is touched:
-- the connected project already carries an unrelated `public` schema, and this
-- spike must not read, alter or depend on it.
--
-- All data is synthetic. Re-running this file is safe (IF NOT EXISTS everywhere).

create schema if not exists feasibility;

revoke all on schema feasibility from public;
grant usage on schema feasibility to anon, authenticated;

-- The world. One row per synthetic nation.
create table if not exists feasibility.nations (
  id          bigint primary key,
  label       text        not null,
  treasury    bigint      not null default 0,
  last_slot   bigint      not null default 0,
  updated_at  timestamptz not null default now()
);

-- One row per shared turn slot: the ledger that makes a slot exactly-once.
create table if not exists feasibility.turn_runs (
  slot             bigint primary key,
  status           text not null check (status in ('running', 'completed', 'failed')),
  cursor           bigint      not null default 0,
  nations_applied  integer     not null default 0,
  batches          integer     not null default 0,
  started_at       timestamptz not null default now(),
  completed_at     timestamptz,
  last_error       text
);

-- Per-nation idempotency marker. The primary key, not application logic, is
-- what prevents a nation-turn from being applied twice.
create table if not exists feasibility.turn_applied (
  slot        bigint not null,
  nation_id   bigint not null references feasibility.nations (id) on delete cascade,
  delta       bigint not null,
  applied_at  timestamptz not null default now(),
  primary key (slot, nation_id)
);

-- Audit spine row per applied nation-turn, written in the same statement as the
-- value change so the two cannot disagree.
create table if not exists feasibility.audit (
  id          bigint generated always as identity primary key,
  slot        bigint not null,
  nation_id   bigint not null,
  delta       bigint not null,
  run_id      text   not null,
  created_at  timestamptz not null default now()
);

create index if not exists audit_slot_idx on feasibility.audit (slot);
create index if not exists turn_applied_slot_idx on feasibility.turn_applied (slot);

-- Scheduler heartbeat: proof that pg_cron actually invoked something, with the
-- timestamp the database saw.
create table if not exists feasibility.cron_heartbeat (
  id          bigint generated always as identity primary key,
  job         text        not null,
  fired_at    timestamptz not null default now(),
  slot        bigint
);

-- Ownership-scoped table used only to exercise Row Level Security.
create table if not exists feasibility.profiles (
  user_id       uuid primary key default gen_random_uuid(),
  owner_sub     text not null,
  display_name  text not null,
  treasury      bigint not null default 0
);

alter table feasibility.profiles enable row level security;

drop policy if exists profiles_select_own on feasibility.profiles;
create policy profiles_select_own on feasibility.profiles
  for select to authenticated
  using (owner_sub = coalesce(current_setting('request.jwt.claims', true)::jsonb ->> 'sub', ''));

drop policy if exists profiles_update_own on feasibility.profiles;
create policy profiles_update_own on feasibility.profiles
  for update to authenticated
  using (owner_sub = coalesce(current_setting('request.jwt.claims', true)::jsonb ->> 'sub', ''))
  with check (owner_sub = coalesce(current_setting('request.jwt.claims', true)::jsonb ->> 'sub', ''));
