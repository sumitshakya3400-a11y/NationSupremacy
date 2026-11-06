-- profile_permissions.test.sql — executable permission and RLS tests.
--
-- Run against a disposable database that has migrations 0001-0005 applied:
--   psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/sql/profile_permissions.test.sql
--
-- Every case raises a notice on success and an exception on failure, so psql
-- exits non-zero the moment the database does not behave as documented. The
-- whole run is one transaction and rolls back: no data is left behind.
--
-- This file proves behaviour only when it is actually executed against a
-- database. A static read of the SQL is not evidence.

\set ON_ERROR_STOP on

begin;

-- Seed two players and two nations as the migration owner.
insert into feasibility.nations (id, label, treasury) values
  (900001, 'Permission Nation A', 1000),
  (900002, 'Permission Nation B', 2000)
on conflict (id) do nothing;

insert into feasibility.profiles (owner_sub, display_name, treasury)
select v.sub, v.name, v.treasury
from (values ('user-a', 'Player A', 500::bigint),
             ('user-b', 'Player B', 600::bigint)) as v(sub, name, treasury)
where not exists (select 1 from feasibility.profiles p where p.owner_sub = v.sub);

-- Make the turn slot deterministic for the authorized-server case.
delete from feasibility.turn_applied where slot = 910001;
delete from feasibility.turn_runs where slot = 910001;

-- A SECURITY DEFINER path exists only to prove the guard trigger still bites
-- when a privileged function is the writer.
create or replace function feasibility.test_write_profile_treasury(p_sub text, p_value bigint)
returns void
language sql
security definer
set search_path = feasibility, pg_temp
as $$
  update feasibility.profiles set treasury = p_value where owner_sub = p_sub;
$$;
grant execute on function feasibility.test_write_profile_treasury(text, bigint) to authenticated;

-- ---------------------------------------------------------------------------
set role authenticated;
select set_config('request.jwt.claims', '{"sub":"user-a"}', true);

-- 1. Own display name: ALLOWED.
do $$
declare n integer;
begin
  update feasibility.profiles set display_name = 'Player A renamed' where owner_sub = 'user-a';
  get diagnostics n = row_count;
  if n <> 1 then
    raise exception 'FAIL display_name: % row(s) updated, expected 1', n;
  end if;
  raise notice 'PASS 1/7 user updates own display_name (allowed)';
end $$;

-- 2. Own profiles.treasury: DENIED by column privilege.
do $$
declare denied boolean := false;
begin
  begin
    update feasibility.profiles set treasury = 999999 where owner_sub = 'user-a';
  exception when insufficient_privilege then
    denied := true;
  end;
  if not denied then
    raise exception 'FAIL profiles.treasury was writable by its owner';
  end if;
  raise notice 'PASS 2/7 user cannot update own profiles.treasury (denied)';
end $$;

-- 3. Own nations.treasury: DENIED by table privilege.
do $$
declare denied boolean := false;
begin
  begin
    update feasibility.nations set treasury = 999999 where id = 900001;
  exception when insufficient_privilege then
    denied := true;
  end;
  if not denied then
    raise exception 'FAIL nations.treasury was writable by authenticated';
  end if;
  raise notice 'PASS 3/7 user cannot update own nations.treasury (denied)';
end $$;

-- 4. Another user's profile: RLS matches no row, so 0 rows change.
do $$
declare n integer;
begin
  update feasibility.profiles set display_name = 'hijacked' where owner_sub = 'user-b';
  get diagnostics n = row_count;
  if n <> 0 then
    raise exception 'FAIL cross-user profile update changed % row(s)', n;
  end if;
  raise notice 'PASS 4/7 user cannot update another user''s profile (0 rows)';
end $$;

-- 5. Another nation's treasury: DENIED before RLS is even reached.
do $$
declare denied boolean := false;
begin
  begin
    update feasibility.nations set treasury = 999999 where id = 900002;
  exception when insufficient_privilege then
    denied := true;
  end;
  if not denied then
    raise exception 'FAIL another nation''s treasury was writable';
  end if;
  raise notice 'PASS 5/7 user cannot modify another nation''s treasury (denied)';
end $$;

-- 6. Alternative write path: a SECURITY DEFINER function must still be blocked
--    by the guard trigger, even though it runs as the owner.
do $$
declare denied boolean := false;
begin
  begin
    perform feasibility.test_write_profile_treasury('user-a', 777777);
  exception when insufficient_privilege then
    denied := true;
  end;
  if not denied then
    raise exception 'FAIL the guard trigger did not block a SECURITY DEFINER write';
  end if;
  raise notice 'PASS 6/7 SECURITY DEFINER path cannot change profiles.treasury (denied)';
end $$;

reset role;
select set_config('request.jwt.claims', '', true);

-- 7. Authorized server operation: the turn resolver may still move money, and
--    it moves it on nations (its own subsystem), not through a profile row.
--    The resolver is batch-bounded, so keep calling it while the result is
--    partial and the target treasury has not increased; a failure reports the
--    final resolver result, not just the unlucky first call.
do $$
declare
  before_value bigint;
  after_value bigint;
  result jsonb;
  guard integer := 0;
begin
  select treasury into before_value from feasibility.nations where id = 900001;
  loop
    result := feasibility.resolve_turn(910001, 1);
    guard := guard + 1;
    select treasury into after_value from feasibility.nations where id = 900001;
    exit when after_value > before_value or coalesce(result->>'outcome', '') <> 'partial';
    if guard >= 1000 then
      raise exception 'FAIL the resolver stayed partial after % batches; final result %', guard, result;
    end if;
  end loop;
  if after_value <= before_value then
    raise exception 'FAIL the server resolver did not credit the nation (% -> %); final result %',
      before_value, after_value, result;
  end if;
  raise notice 'PASS 7/7 authorized server operation still credits nations.treasury (% -> %; final result %)',
    before_value, after_value, result;
end $$;

drop function if exists feasibility.test_write_profile_treasury(text, bigint);

rollback;
\echo 'PROFILE PERMISSION TESTS: all seven cases behaved as documented.'
