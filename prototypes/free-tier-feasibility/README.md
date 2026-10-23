# Free-tier feasibility spike

**Not game code.** This is a bounded technical spike that produced the evidence for
Stage 1 gates GATE-16 and GATE-18. It contains no nation, economy, diplomacy or war
gameplay, no accounts and no player data. Everything in it is synthetic.

## What it proves

| Claim | Where it is tested |
|---|---|
| One shared turn per 2-hour UTC boundary (12/day) | `test/slots.test.js`; `slotsBetween` over a 24h window |
| A turn is applied exactly once per nation | `scripts/integration.mjs` (duplicate invocations, re-runs) |
| Resolution resumes forward-only in bounded batches | `scripts/integration.mjs` (`maxBatches=1`, `faultAfter`) |
| A failed invocation never leaves a half-applied nation | per-nation statements are one D1 `batch()` (one transaction) |
| D1 gives measurable rows-read / rows-written per turn | `meta.rows_read`, `meta.rows_written`, `meta.size_after` |
| The schema is idempotent and reproducible | `schema/0001_init.sql`, `/api/spike/init` twice |

## Layout

```
src/slots.js        pure UTC slot arithmetic + spike authorisation
src/engine.js       resolveTurn(): ledger, batch loop, idempotency, reporting
src/index.js        Worker: HTML page, /health, read-only status, guarded spike routes, scheduled handler
schema/0001_init.sql  minimal D1 schema (synthetic only)
test/slots.test.js  unit tests (node:test, no dependencies)
scripts/integration.mjs  local workerd integration harness (23 checks)
scripts/measure.mjs      local capacity measurements at 50 / 250 / 1000 nations
results/            recorded measurements (local JSON + deployed JSON)
```

## Run it locally

```bash
npm install
npm test                      # unit tests
npm run test:integration      # starts wrangler dev, drives 23 checks, stops it
node scripts/measure.mjs      # local capacity table (50/250/1000 nations)
```

Local dev needs no account and no secrets. The harness passes the token on the
command line (`--var SPIKE_TOKEN:...`), so nothing is written to disk.

Manual run:

```bash
npx wrangler dev --port 8787 --test-scheduled --var SPIKE_TOKEN:local-test-token
curl -s localhost:8787/health
curl -s -X POST localhost:8787/api/spike/init -H "x-spike-token: local-test-token"
curl -s -X POST "localhost:8787/api/spike/seed?n=250&reset=1" -H "x-spike-token: local-test-token"
curl -s -X POST "localhost:8787/api/spike/resolve?slot=<slot>&batch=100" -H "x-spike-token: local-test-token"
```

## Deploying it yourself

The spike was deployed to a free Cloudflare account for measurement. Reproducing
that is optional; if you do it, use a throwaway Worker name and a fresh D1 database:

```bash
npx wrangler d1 create px-feasibility-spike     # put the id into wrangler.jsonc
npx wrangler secret put SPIKE_TOKEN             # any long random value
npx wrangler deploy
```

Do **not** deploy it with `ALLOW_SPIKE=1` and no token: the mutating routes would be
open to anyone. The Worker refuses them when `SPIKE_TOKEN` is unset, but the token is
the intended control.

The deployed copy used two schedules during the spike: the product cadence
`0 */2 * * *` and a temporary `*/5 * * * *` to observe cron behaviour without waiting
two hours. `*/5` is **test-only** and must not exist in a real deployment.

## Cleanup

```bash
npx wrangler delete px-feasibility-spike
npx wrangler d1 delete px-feasibility-spike
```

Deleting the Worker also removes its schedules; the D1 database is separate.

## Limits of the evidence

- Local numbers come from workerd + Miniflare's local D1, not from Cloudflare's
  production D1.
- Deployed `duration_ms` is measured inside the Worker and includes D1 round trips;
  it is not CPU time.
- CPU figures are Cloudflare analytics (`workersInvocationsAdaptive`), which is
  sampled and noisy. They are indicative, not exact per-invocation counters.
- 1,000 nations is an exploratory size, not an approved capacity target.
