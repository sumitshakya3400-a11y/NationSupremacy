-- 0005_profile_column_privileges.sql — least-privilege profile edits.
--
-- Defect (found by the Prompt 11C audit, confirmed by static inspection on
-- 2026-11-06): 0003 granted `select, insert, update` on the whole
-- `feasibility.profiles` table to `authenticated`. The RLS policy only scopes
-- *which row* a player may touch, so a signed-in player could write any column
-- of their own row — including `treasury`, which is server-authoritative. The
-- earlier feasibility report tested `nations.treasury` (correctly denied) but
-- never `profiles.treasury`, so the hole was not covered by that evidence.
--
-- Correction, in three layers:
--   1. table-wide UPDATE is revoked and only `display_name` is granted;
--   2. INSERT is revoked: no policy authorises it, so no legitimate path loses
--      anything (profile rows are created server-side);
--   3. a trigger refuses any change to the server-authoritative columns even if
--      a future grant, view or SECURITY DEFINER path widens write access.
--
-- Safe to re-apply: every statement is idempotent. No data is modified.

begin;

-- 1. Column-level write privilege -------------------------------------------
revoke update on table feasibility.profiles from authenticated;
revoke insert on table feasibility.profiles from authenticated;

grant update (display_name) on table feasibility.profiles to authenticated;

-- Reading one's own row is still allowed; the RLS policy in 0001 decides which.
-- `anon` never had access and must not gain it here.
revoke all on table feasibility.profiles from public, anon;

-- 2. Defence in depth: refuse server-authoritative column changes -------------
-- The trigger fires for every role, including a SECURITY DEFINER function or a
-- future widened grant. A legitimate financial write belongs to the subsystem
-- that owns the value (nations.treasury is written by the turn resolver); it
-- must not be smuggled through a profile row. The setting is a deliberate,
-- session-scoped opt-in for a documented migration or test, not a runtime path.
create or replace function feasibility.profiles_guard_server_columns()
returns trigger
language plpgsql
security definer
set search_path = feasibility, pg_temp
as $$
begin
  if coalesce(current_setting('feasibility.allow_profile_server_write', true), '') = 'on' then
    return new;
  end if;

  if new.user_id is distinct from old.user_id then
    raise exception 'profiles.user_id is server-authoritative'
      using errcode = '42501';
  end if;
  if new.owner_sub is distinct from old.owner_sub then
    raise exception 'profiles.owner_sub is server-authoritative'
      using errcode = '42501';
  end if;
  if new.treasury is distinct from old.treasury then
    raise exception 'profiles.treasury is server-authoritative and is not client-writable'
      using errcode = '42501';
  end if;

  return new;
end;
$$;

drop trigger if exists profiles_guard_server_columns on feasibility.profiles;
create trigger profiles_guard_server_columns
  before update on feasibility.profiles
  for each row
  execute function feasibility.profiles_guard_server_columns();

-- 3. Make the intent legible to a reader of the catalogue ---------------------
comment on column feasibility.profiles.display_name is
  'Client-editable: the only column an authenticated player may write.';
comment on column feasibility.profiles.treasury is
  'Server-authoritative. Never client-writable; guard trigger 0005 rejects changes.';
comment on column feasibility.profiles.owner_sub is
  'Server-authoritative identity key used by the RLS policy.';

commit;
