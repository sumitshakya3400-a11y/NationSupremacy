import test from "node:test";
import assert from "node:assert/strict";

import {
  PRODUCT_CRON,
  TURN_MS,
  authorizeSpike,
  computeSlot,
  isProductCron,
  isSlotClosed,
  isValidCron,
  slotIso,
  slotStartMs,
  slotsBetween,
} from "../src/slots.js";

const H = 3600 * 1000;
const DAY = 24 * H;

test("a slot starts exactly on an even UTC hour", () => {
  const t = Date.UTC(2026, 9, 23, 8, 0, 0);
  assert.equal(slotStartMs(computeSlot(t)), t);
});

test("a millisecond before the boundary belongs to the previous slot", () => {
  const boundary = Date.UTC(2026, 9, 23, 8, 0, 0);
  assert.equal(computeSlot(boundary - 1), computeSlot(boundary) - 1);
  assert.equal(slotStartMs(computeSlot(boundary - 1)), boundary - TURN_MS);
});

test("a 24-hour UTC day contains exactly 12 distinct slots", () => {
  const start = Date.UTC(2026, 9, 23, 0, 0, 0);
  assert.equal(slotsBetween(start, start + DAY).length, 12);
  assert.equal(new Set(slotsBetween(start, start + DAY)).size, 12);
});

test("every slot in a day is two hours after the previous one", () => {
  const start = Date.UTC(2026, 9, 23, 0, 0, 0);
  const slots = slotsBetween(start, start + DAY);
  for (let i = 1; i < slots.length; i += 1) {
    assert.equal(slotStartMs(slots[i]) - slotStartMs(slots[i - 1]), 2 * H);
  }
});

test("slot ISO strings are UTC and boundary-aligned", () => {
  const slot = computeSlot(Date.UTC(2026, 9, 23, 14, 0, 0));
  assert.equal(slotIso(slot), "2026-10-23T14:00:00.000Z");
});

test("slot arithmetic rejects nonsense instead of silently defaulting", () => {
  assert.throws(() => computeSlot(undefined), TypeError);
  assert.throws(() => computeSlot(NaN), TypeError);
  assert.throws(() => computeSlot("123"), TypeError);
  assert.throws(() => slotStartMs(1.5), TypeError);
  assert.throws(() => slotStartMs(-1), TypeError);
});

test("a slot is only resolvable after its boundary", () => {
  const boundary = Date.UTC(2026, 9, 23, 10, 0, 0);
  const slot = computeSlot(boundary);
  assert.equal(isSlotClosed(slot, boundary), true);
  assert.equal(isSlotClosed(slot, boundary - 1), false);
});

test("the product cadence is the 12-per-day expression and nothing else", () => {
  assert.equal(PRODUCT_CRON, "0 */2 * * *");
  assert.equal(isProductCron("0 */2 * * *"), true);
  assert.equal(isProductCron("0 * * * *"), false);
  assert.equal(isValidCron("0 */2 * * *"), true);
  assert.equal(isValidCron("0 */2 * *"), false);
  assert.equal(isValidCron(""), false);
});

function req(token) {
  return new Request("https://spike.test/api/spike/init", {
    method: "POST",
    headers: token === undefined ? {} : { "x-spike-token": token },
  });
}

test("spike routes are closed unless the deployment opts in", () => {
  assert.equal(authorizeSpike(req("abc"), { ALLOW_SPIKE: "0", SPIKE_TOKEN: "abc" }), false);
  assert.equal(authorizeSpike(req("abc"), { SPIKE_TOKEN: "abc" }), false);
});

test("spike routes require the exact token", () => {
  const env = { ALLOW_SPIKE: "1", SPIKE_TOKEN: "s3cret" };
  assert.equal(authorizeSpike(req(undefined), env), false);
  assert.equal(authorizeSpike(req(""), env), false);
  assert.equal(authorizeSpike(req("s3cret!"), env), false);
  assert.equal(authorizeSpike(req("S3CRET"), env), false);
  assert.equal(authorizeSpike(req("s3cret"), env), true);
});

test("a deployment without a token never authorises", () => {
  assert.equal(authorizeSpike(req("anything"), { ALLOW_SPIKE: "1" }), false);
});
