-- 0004_schedule.sql — the single authoritative turn scheduler.
--
-- Supabase Cron (pg_cron) drives the shared world: one invocation per even UTC
-- hour, twelve a day. There is deliberately no second scheduler: the Cloudflare
-- D1 spike also had a cron trigger, but it is historical comparative evidence
-- and is not part of this architecture (Report 11 §14.6, Report 12 §7).
--
-- Re-running is safe: the job is unscheduled by name first, then recreated.

create extension if not exists pg_cron;

select cron.unschedule(jobid) from cron.job where jobname = 'nation-supremacy-turn';

select cron.schedule(
  'nation-supremacy-turn',
  '0 */2 * * *',
  $$select feasibility.resolve_current_turn(250)$$
);

-- Verification, not part of the schedule:
--   select jobname, schedule, active from cron.job;
--   select * from feasibility.cron_heartbeat order by id desc limit 12;
--   select j.jobname, d.status, d.start_time
--     from cron.job_run_details d join cron.job j on j.jobid = d.jobid
--    order by d.start_time desc limit 12;
