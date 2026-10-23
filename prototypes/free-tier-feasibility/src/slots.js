/**
 * Shared-turn slot arithmetic and spike authorisation.
 *
 * Deliberately free of D1 and of the Workers runtime so it can be unit-tested
 * with `node --test` and reused unchanged inside the Worker.
 */

/** One shared turn every two hours, on fixed UTC boundaries (REQ-015). */
export const TURN_SECONDS = 7200;
export const TURN_MS = TURN_SECONDS * 1000;

/** Slot index = number of complete 2-hour periods since the Unix epoch (UTC). */
export function computeSlot(epochMs) {
  if (typeof epochMs !== "number" || !Number.isFinite(epochMs)) {
    throw new TypeError("computeSlot requires a finite epoch in milliseconds");
  }
  return Math.floor(epochMs / TURN_MS);
}

export function slotStartMs(slot) {
  if (!Number.isInteger(slot) || slot < 0) {
    throw new TypeError("slotStartMs requires a non-negative integer slot");
  }
  return slot * TURN_MS;
}

export function slotIso(slot) {
  return new Date(slotStartMs(slot)).toISOString();
}

/** A slot is only resolvable once its boundary has passed. */
export function isSlotClosed(slot, nowMs = Date.now()) {
  return slotStartMs(slot) <= nowMs;
}

export function slotsBetween(startMs, endMs) {
  const first = computeSlot(startMs);
  const last = computeSlot(endMs - 1);
  return Array.from({ length: Math.max(0, last - first + 1) }, (_, i) => first + i);
}

/** Test-only routes are closed unless the deployment explicitly opts in. */
export function spikeAllowed(env) {
  return Boolean(env && env.ALLOW_SPIKE === "1");
}

export function tokenMatches(headers, env) {
  const expected = env && env.SPIKE_TOKEN;
  if (!expected) return false;
  const supplied = headers.get("x-spike-token");
  if (!supplied || supplied.length !== expected.length) return false;
  let diff = 0;
  for (let i = 0; i < supplied.length; i += 1) {
    diff |= supplied.charCodeAt(i) ^ expected.charCodeAt(i);
  }
  return diff === 0;
}

export function authorizeSpike(request, env) {
  if (!spikeAllowed(env)) return false;
  return tokenMatches(request.headers, env);
}

/** The only cron pattern this prototype accepts as the product cadence. */
export const PRODUCT_CRON = "0 */2 * * *";

export function isProductCron(expression) {
  return expression === PRODUCT_CRON;
}

/** Structural check for a five-field cron expression (UTC, as Workers uses). */
export function isValidCron(expression) {
  if (typeof expression !== "string") return false;
  const fields = expression.trim().split(/\s+/);
  return fields.length === 5;
}
