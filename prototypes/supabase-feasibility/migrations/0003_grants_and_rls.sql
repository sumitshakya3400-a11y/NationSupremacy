-- 0003_grants_and_rls.sql — least privilege.
--
-- The browser-facing role must be able to read the world and edit only its own
-- profile. It must not be able to move a treasury, mark a turn complete, write
-- an audit row, or call the resolver.

revoke all on all tables in schema feasibility from anon, authenticated;
revoke all on all sequences in schema feasibility from anon, authenticated;

-- Read-only world view for signed-in players.
grant select on feasibility.nations to authenticated;

-- Own-row profile access; RLS policies in 0001 decide *which* rows.
grant select, insert, update on feasibility.profiles to authenticated;
revoke delete on feasibility.profiles from authenticated;

-- The turn engine is server-side only. `public` holds the default EXECUTE grant
-- for new functions, so revoking from it is the load-bearing line here.
revoke execute on all functions in schema feasibility from public, anon, authenticated;
grant execute on function feasibility.current_slot(timestamptz) to anon, authenticated;

-- Belt and braces: even if a grant is added later, these tables stay readable
-- only to the service role.
alter table feasibility.turn_runs      enable row level security;
alter table feasibility.turn_applied   enable row level security;
alter table feasibility.audit          enable row level security;
alter table feasibility.cron_heartbeat enable row level security;
