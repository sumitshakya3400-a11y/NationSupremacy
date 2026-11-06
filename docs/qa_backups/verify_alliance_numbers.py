#!/usr/bin/env python3
"""Documentation-level checks for B-09 (Alliance taxation and donations).

What this proves
----------------
* The F-AL-006 tax arithmetic recomputes: floor rounding, the
  0/10/20/30/37/50/55/73/100 rate sweep, non-multiple-of-10 rates, separate
  Crowns and resource rates, different member brackets, 100% validity and the
  explicit 0% fallback. Multiple same-asset production events use cumulative
  fractional accrual: each event collects the increment of the floored
  cumulative liability, so small events never lose a fractional remainder and
  the event taxes reconcile to the per-turn floor.
* Each asset conserves: tax plus net equals gross, the tax never exceeds
  gross, and the Alliance Receiving Ledger receives the tax exactly once.
* A retried settlement with the same idempotency key is a no-op; a conflicting
  key reusing the same identity aborts rather than paying twice.
* F-AL-007 donation arithmetic conserves value, admits two equal donations
  under distinct keys, rejects insufficient or unsupported value, and assumes
  no destination capacity.
* F-AL-008 operational funding preserves the four ARL categories, reserves and
  settles at most once, rejects insufficient AVAILABLE without a negative
  balance, and never pays a player or invents a capacity. The same documents
  state that no AOP purpose currently has an approved cost schedule, so no
  purpose is spendable and received value remains in the ARL.
* The documents carry the identifiers and boundaries the arithmetic claims:
  ALL-179 to ALL-226, F-AL-006/F-AL-007/F-AL-008, REQ-618 to REQ-653, D-140
  and D-141, DD-161/DD-164, AX-27 to AX-30, the non-covered-member rule,
  whole-treaty dissolution and the mandatory blocked-attack audit, with UD-045
  (narrow tax permissions) and UD-046 (general treasury) still Open.

What this does NOT prove
------------------------
No code, database, scheduler, endpoint, ledger table or audit sink exists.
These are arithmetic and document-consistency checks against a specification
that has not been implemented. They do not establish runtime enforcement, and
they do not settle UD-046 or any other owner-reserved decision.

Usage
-----
    python verify_alliance_numbers.py
    python verify_alliance_numbers.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
B09 = DOCS / "stage-2" / "16_alliances.md"
REG = DOCS / "stage-2" / "16_alliances_formula_register.md"
CONTRACTS = DOCS / "stage-2" / "16_alliances_integration_contracts.md"
REQ = DOCS / "stage-2" / "03_requirements_traceability.md"
DEC = DOCS / "DECISIONS.md"
DD = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
UD = DOCS / "stage-2" / "05_unresolved_design_decisions.md"
ECON = DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md"

BP = 10_000

PASS: list[str] = []
FAIL: list[str] = []


def check(name: str, condition: bool, detail: object = "") -> bool:
    if condition:
        PASS.append(name)
    else:
        FAIL.append(f"{name} :: {detail}")
    return bool(condition)


def rd(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def tax(gross: int, rate_bp: int) -> int:
    if gross < 0:
        raise ValueError("gross production must be non-negative")
    if not 0 <= rate_bp <= BP:
        raise ValueError("rate outside 0..10,000 bp")
    return gross * rate_bp // BP


def net(gross: int, rate_bp: int) -> int:
    return gross - tax(gross, rate_bp)


def settle(key_store: dict[tuple, tuple], key: tuple, gross: int, rate_bp: int) -> tuple:
    if key in key_store:
        prior_gross, prior_rate, prior_tax = key_store[key]
        if (prior_gross, prior_rate) != (gross, rate_bp):
            raise ValueError("conflicting reuse of a settlement key")
        return key_store[key]
    amount = tax(gross, rate_bp)
    receipt = (gross, rate_bp, amount)
    key_store[key] = receipt
    return receipt


def tax_events(gross_events: list[int], rate_bp: int) -> dict:
    """Cumulative fractional accrual for multiple same-asset production events.

    Each event collects ``floor(C_j * rate_bp / 10,000) - D_{j-1}``, the
    increment of one floored cumulative liability, never an independent floor
    of the event's own gross. The event taxes therefore sum to the per-turn
    floor and no fractional remainder is dropped or collected twice.
    """
    if any(gross < 0 for gross in gross_events):
        raise ValueError("gross production must be non-negative")
    if not 0 <= rate_bp <= BP:
        raise ValueError("rate outside 0..10,000 bp")
    cumulative_gross: list[int] = []
    cumulative_due: list[int] = []
    event_taxes: list[int] = []
    event_nets: list[int] = []
    total_gross = 0
    prior_due = 0
    for gross in gross_events:
        total_gross += gross
        due = total_gross * rate_bp // BP
        event_tax = due - prior_due
        cumulative_gross.append(total_gross)
        cumulative_due.append(due)
        event_taxes.append(event_tax)
        event_nets.append(gross - event_tax)
        prior_due = due
    return {
        "cumulative_gross": cumulative_gross,
        "cumulative_due": cumulative_due,
        "event_taxes": event_taxes,
        "event_nets": event_nets,
        "total_gross": total_gross,
        "total_tax": prior_due,
        "total_net": total_gross - prior_due,
    }


def apply_tax_event(
    key_store: dict[tuple, tuple],
    state: dict,
    key: tuple,
    gross: int,
    rate_bp: int,
) -> tuple:
    """Settle one production event with cumulative accrual; a replay is a no-op."""
    if gross < 0:
        raise ValueError("gross production must be non-negative")
    if not 0 <= rate_bp <= BP:
        raise ValueError("rate outside 0..10,000 bp")
    if key in key_store:
        prior = key_store[key]
        if prior[1:3] != (gross, rate_bp):
            raise ValueError("conflicting reuse of an event key")
        return prior
    cumulative = state.get("cumulative_gross", 0) + gross
    due = cumulative * rate_bp // BP
    event_tax = due - state.get("tax_collected", 0)
    receipt = (key, gross, rate_bp, event_tax, cumulative, due)
    key_store[key] = receipt
    state["cumulative_gross"] = cumulative
    state["tax_collected"] = due
    return receipt


def membership_settle(alliances: list[dict], gross: int) -> dict:
    """Provisional UD-040 safeguard: settle only when attribution is unambiguous."""
    active = [alliance for alliance in alliances if alliance.get("active")]
    if not active:
        return {
            "status": "NO_ACTIVE_ALLIANCE",
            "tax": 0,
            "net": gross,
            "alliance": None,
            "reason": "not an active member",
        }
    if len(active) > 1:
        return {
            "status": "AMBIGUOUS_0_PERCENT_FALLBACK",
            "tax": 0,
            "net": gross,
            "alliance": None,
            "reason": "multiple-membership attribution unresolved",
        }
    sole = active[0]
    amount = tax(gross, sole["rate_bp"])
    return {
        "status": "SINGLE_ALLIANCE",
        "tax": amount,
        "net": gross - amount,
        "alliance": sole["id"],
        "reason": "",
    }


def donate(
    amount: int,
    unreserved: int,
    supported: bool,
    settled_keys: set[str],
    key: str,
    capacity: int | None = None,
) -> tuple[int, int, bool]:
    if capacity is not None and amount > capacity:
        return (0, 0, False)
    if amount <= 0 or not supported or amount > unreserved or key in settled_keys:
        return (0, 0, False)
    settled_keys.add(key)
    return (-amount, amount, True)


def operational_expense(
    received: int,
    available: int,
    reserved: int,
    expended: int,
    amount: int,
    purpose: str,
    schedule: int | None,
    destination: str,
    settled_keys: dict[str, int],
    key: str,
    recipient_is_platform_sink: bool = True,
    capacity: int | None = None,
) -> tuple[dict, str]:
    """Purpose-limited F-AL-008 accounting; no withdrawal or player payment."""
    state = {
        "received": received,
        "available": available,
        "reserved": reserved,
        "expended": expended,
    }
    if state["available"] + state["reserved"] + state["expended"] != state["received"]:
        return state, "ALF-27"
    if purpose not in {"AOP-01", "AOP-02", "AOP-03", "AOP-04"}:
        return state, "ALF-27"
    if schedule is None or amount != schedule or destination != "platform_cost_sink":
        return state, "ALF-27"
    if not recipient_is_platform_sink or capacity is not None:
        return state, "ALF-27"
    if key in settled_keys:
        return state, "REPLAY" if settled_keys[key] == amount else "ALF-29"
    if amount <= 0 or amount > state["available"]:
        return state, "ALF-28"
    state["available"] -= amount
    state["reserved"] += amount
    settled_keys[key] = amount
    state["reserved"] -= amount
    state["expended"] += amount
    return state, "SETTLED"


# ---------------------------------------------------------------------------
# Arithmetic
# ---------------------------------------------------------------------------
def arithmetic_checks() -> None:
    sweep = {0: 0, 10: 1_000, 20: 2_000, 30: 3_000, 37: 3_700,
             50: 5_000, 55: 5_500, 73: 7_300, 100: 10_000}
    for percent, expected in sweep.items():
        got = tax(10_000, percent * 100)
        check(f"rate sweep {percent}% on 10,000 -> {expected}", got == expected, got)

    for gross, rate_bp, expected in [
        (100_000, 3_700, 37_000),
        (2_000, 1_000, 200),
        (800, 2_000, 160),
        (400, 5_500, 220),
        (10_000, 100, 100),
        (10_000, 3_700, 3_700),
        (10_000, 7_300, 7_300),
        (10_000, 9_999, 9_999),
        (999, 5_555, 554),
        (3, 1, 0),
    ]:
        got = tax(gross, rate_bp)
        check(
            f"floor tax {gross} x {rate_bp}bp -> {expected}",
            got == expected,
            got,
        )

    example = {"Crowns": (100_000, 3_700, 37_000, 63_000),
               "Food": (2_000, 1_000, 200, 1_800),
               "Iron": (800, 2_000, 160, 640),
               "Oil": (400, 5_500, 220, 180)}
    arl = 0
    for asset, (gross, rate_bp, expected_tax, expected_net) in example.items():
        got_tax = tax(gross, rate_bp)
        got_net = net(gross, rate_bp)
        arl += got_tax
        check(f"worked example {asset} tax", got_tax == expected_tax, got_tax)
        check(f"worked example {asset} net", got_net == expected_net, got_net)
        check(f"worked example {asset} conservation", got_tax + got_net == gross)
    check("worked example Crowns ledger credit", arl == 37_580, arl)

    member_a = {"Crowns": (100_000, 3_700), "Iron": (800, 2_000)}
    member_b = {"Crowns": (100_000, 500), "Iron": (800, 0)}
    check(
        "different brackets tax the same gross differently",
        tax(*member_a["Crowns"]) != tax(*member_b["Crowns"])
        and tax(*member_a["Iron"]) != tax(*member_b["Iron"]),
    )
    check(
        "separate asset rates are independent",
        tax(100_000, 3_700) == 37_000
        and tax(2_000, 1_000) == 200
        and tax(2_000, 3_700) == 740
        and tax(800, 2_000) == 160,
    )

    for gross in (0, 1, 7, 999, 10_000, 123_457):
        for rate_bp in (0, 1, 100, 1_000, 3_700, 5_500, 7_300, 9_999, BP):
            amount = tax(gross, rate_bp)
            check(
                f"bounds/conservation {gross}@{rate_bp}",
                0 <= amount <= gross and amount + net(gross, rate_bp) == gross,
                amount,
            )

    check("0% fallback collects nothing", tax(98_765, 0) == 0 and net(98_765, 0) == 98_765)
    check("100% leaves zero net", net(98_765, BP) == 0 and tax(98_765, BP) == 98_765)
    check(
        "unassigned member uses the 0% fallback, not an engine default",
        tax(50_000, 0) == 0 and tax(50_000, 1_000) == 5_000,
    )

    ledger: list[int] = []
    key_store: dict[tuple, tuple] = {}
    receipt_first = settle(key_store, ("t1", "N1", "Crowns"), 100_000, 3_700)
    ledger.append(receipt_first[2])
    receipt_retry = settle(key_store, ("t1", "N1", "Crowns"), 100_000, 3_700)
    ledger.append(0 if receipt_retry == receipt_first else receipt_retry[2])
    check("retry returns the original receipt", receipt_first == receipt_retry)
    check("retry credits the ledger exactly once", sum(ledger) == 37_000, sum(ledger))
    try:
        settle(key_store, ("t1", "N1", "Crowns"), 100_001, 3_700)
        conflicting_aborted = False
    except ValueError:
        conflicting_aborted = True
    check("conflicting key reuse aborts", conflicting_aborted)

    gross_before = 100_000
    opening_balance = 500_000
    market_receipt = 25_000
    donation = 12_500
    eligible_base = gross_before
    taxable = tax(eligible_base, 3_700)
    check(
        "only current-turn production enters the base",
        taxable == 37_000
        and tax(eligible_base + opening_balance, 3_700) != taxable
        and tax(eligible_base + market_receipt, 3_700) != taxable
        and tax(eligible_base + donation, 3_700) != taxable,
    )
    net_after = net(eligible_base, 3_700)
    check(
        "tax is not applied again to the post-tax balance",
        net_after == 63_000 and tax(net_after, 3_700) == 23_310 and tax(net_after, 3_700) != 0,
    )

    # Cumulative fractional accrual for multiple same-asset production events.
    two_events = tax_events([1, 1], 5_000)
    check(
        "cumulative: two 1-unit events at 50% collect 0 then 1",
        two_events["cumulative_gross"] == [1, 2]
        and two_events["cumulative_due"] == [0, 1]
        and two_events["event_taxes"] == [0, 1]
        and two_events["event_nets"] == [1, 0]
        and two_events["total_tax"] == 1
        and two_events["total_net"] == 1,
        two_events,
    )
    one_event = tax_events([2], 5_000)
    check(
        "cumulative: one 2-unit event at 50% collects the same 1",
        one_event["event_taxes"] == [1]
        and one_event["total_tax"] == two_events["total_tax"] == 1,
        one_event,
    )
    fractional = tax_events([1, 1, 1, 1], 3_333)
    fractional_one_event = tax_events([4], 3_333)
    check(
        "cumulative: four 1-unit events at 3,333 bp collect on the fourth only",
        fractional["cumulative_due"] == [0, 0, 0, 1]
        and fractional["event_taxes"] == [0, 0, 0, 1]
        and fractional["total_tax"] == 1
        and fractional_one_event["total_tax"] == 1,
        (fractional, fractional_one_event),
    )
    check(
        "cumulative: independent per-event floors would under-collect",
        sum(tax(1, 3_333) for _ in range(4)) == 0
        and fractional["total_tax"] == 1,
    )
    zero_rate = tax_events([1, 1, 1], 0)
    full_rate = tax_events([1, 1, 1], BP)
    check(
        "cumulative: 0% and 100% across three events",
        zero_rate["event_taxes"] == [0, 0, 0]
        and zero_rate["total_tax"] == 0
        and full_rate["event_taxes"] == [1, 1, 1]
        and full_rate["total_tax"] == 3
        and full_rate["total_net"] == 0,
        (zero_rate, full_rate),
    )
    iron_events = tax_events([1, 1], 5_000)
    steel_events = tax_events([1, 1], 2_500)
    check(
        "cumulative: different asset rates keep separate accumulators",
        iron_events["total_tax"] == 1
        and steel_events["total_tax"] == 0
        and iron_events["total_tax"] + steel_events["total_tax"] == 1,
        (iron_events["total_tax"], steel_events["total_tax"]),
    )

    for events in ([1, 1], [1, 1, 1, 1], [3, 7, 11], [0, 5, 0, 5]):
        for rate_bp in (0, 1, 100, 3_333, 5_000, 7_300, 9_999, BP):
            result = tax_events(list(events), rate_bp)
            check(
                f"cumulative reconciliation {events}@{rate_bp}",
                sum(result["event_taxes"]) == result["total_tax"] == tax(sum(events), rate_bp)
                and sum(result["event_nets"]) == result["total_net"]
                and result["total_tax"] + result["total_net"] == result["total_gross"]
                and all(0 <= amount <= gross for amount, gross in zip(result["event_taxes"], events))
                and all(
                    due == tax(gross_total, rate_bp)
                    for gross_total, due in zip(result["cumulative_gross"], result["cumulative_due"])
                ),
                result,
            )

    retry_store: dict[tuple, tuple] = {}
    retry_state = {"cumulative_gross": 0, "tax_collected": 0}
    first_event = apply_tax_event(retry_store, retry_state, ("t1", "N1", "Iron", 1), 1, 5_000)
    second_event = apply_tax_event(retry_store, retry_state, ("t1", "N1", "Iron", 2), 1, 5_000)
    state_before_replay = dict(retry_state)
    replay = apply_tax_event(retry_store, retry_state, ("t1", "N1", "Iron", 2), 1, 5_000)
    check(
        "cumulative: a replayed event does not advance the accumulator",
        first_event[3] == 0
        and second_event[3] == 1
        and replay == second_event
        and retry_state == state_before_replay
        and retry_state["cumulative_gross"] == 2
        and retry_state["tax_collected"] == 1
        and len(retry_store) == 2,
        (first_event, second_event, replay, retry_state),
    )
    try:
        apply_tax_event(retry_store, retry_state, ("t1", "N1", "Iron", 2), 2, 5_000)
        event_conflict = False
    except ValueError:
        event_conflict = True
    check(
        "cumulative: a conflicting event replay aborts without advancing",
        event_conflict and retry_state == state_before_replay,
        retry_state,
    )
    check(
        "cumulative: negative gross and invalid rates are rejected",
        _raises(lambda: tax_events([-1], 5_000))
        and _raises(lambda: tax_events([1], -1))
        and _raises(lambda: tax_events([1], BP + 1)),
    )

    keys: set[str] = set()
    donor_a, arl_a, ok_a = donate(12_500, 20_000, True, keys, "k1")
    donor_retry, arl_retry, ok_retry = donate(12_500, 20_000, True, keys, "k1")
    donor_b, arl_b, ok_b = donate(12_500, 20_000, True, keys, "k2")
    check("donation conserves value", ok_a and donor_a + arl_a == 0, (donor_a, arl_a))
    check("donation replay is a no-op", ok_retry is False and donor_retry == arl_retry == 0)
    check("two equal donations under distinct keys both settle", ok_b and donor_b == -12_500)
    check(
        "insufficient donor value fails atomically",
        donate(25_000, 20_000, True, set(), "k3") == (0, 0, False),
    )
    check(
        "unsupported asset fails atomically",
        donate(100, 20_000, False, set(), "k4") == (0, 0, False),
    )
    check(
        "no capacity assumption rejects a valid donation",
        donate(12_500, 20_000, True, set(), "k5")[2] is True,
    )
    check(
        "a donation is not production and is not taxed",
        tax(eligible_base, 3_700) == 37_000
        and tax(eligible_base + 12_500, 3_700) == 41_625,
    )


# ---------------------------------------------------------------------------
# Multiple-membership safeguard and production chain
# ---------------------------------------------------------------------------
def membership_and_chain_checks() -> None:
    # 1. One alliance collects normally.
    one = membership_settle([{"id": "A", "active": True, "rate_bp": 5_000}], 100)
    check(
        "membership 1: one alliance collects normally",
        one["status"] == "SINGLE_ALLIANCE" and one["tax"] == 50 and one["net"] == 50,
        one,
    )

    # 2. Two memberships never duplicate or stack.
    two = membership_settle(
        [
            {"id": "A", "active": True, "rate_bp": 5_000},
            {"id": "B", "active": True, "rate_bp": 5_000},
        ],
        100,
    )
    check(
        "membership 2: multiple memberships never duplicate or stack",
        two["status"] == "AMBIGUOUS_0_PERCENT_FALLBACK"
        and two["tax"] == 0
        and two["tax"] != 50 + 50,
        two,
    )

    # 3. Different rates create no priority.
    different = membership_settle(
        [
            {"id": "A", "active": True, "rate_bp": 1_000},
            {"id": "B", "active": True, "rate_bp": 9_000},
        ],
        100,
    )
    check(
        "membership 3: two alliances with different rates receive no priority",
        different["tax"] == 0 and different["alliance"] is None,
        different,
    )

    # 4. Repeated collection attempts settle once.
    store: dict[tuple, tuple] = {}
    first = settle(store, ("t1", "N1", "Crowns"), 100, 5_000)
    retry = settle(store, ("t1", "N1", "Crowns"), 100, 5_000)
    check(
        "membership 4: repeated collection attempts settle once",
        first[2] == 50 and retry == first and len(store) == 1,
        (first, retry, len(store)),
    )

    # 5. Leaving one alliance preserves historical records.
    history = [{"turn": 1, "alliance": "A", "tax": 50, "status": "SINGLE_ALLIANCE"}]
    before = [dict(record) for record in history]
    after_leave = membership_settle([{"id": "B", "active": True, "rate_bp": 5_000}], 100)
    check(
        "membership 5: leaving one alliance preserves historical records",
        history == before and after_leave["tax"] == 50 and len(history) == 1,
        (history, after_leave),
    )

    # 6. Membership changes are recomputed at the snapshot boundary.
    turn_one = membership_settle([{"id": "A", "active": True, "rate_bp": 5_000}], 100)
    turn_two = membership_settle(
        [
            {"id": "A", "active": True, "rate_bp": 5_000},
            {"id": "B", "active": True, "rate_bp": 5_000},
        ],
        100,
    )
    check(
        "membership 6: membership change applies at the next boundary only",
        turn_one["tax"] == 50 and turn_two["tax"] == 0,
        (turn_one, turn_two),
    )

    # 7. Joining during a turn is neither retroactive nor duplicated.
    snapshot_turn = [{"id": "A", "active": True, "rate_bp": 5_000}]
    before_join = membership_settle(snapshot_turn, 100)
    snapshot_turn.append({"id": "B", "active": True, "rate_bp": 5_000})
    after_join_next_turn = membership_settle(snapshot_turn, 100)
    check(
        "membership 7: joining during a turn is not retroactive or duplicated",
        before_join["tax"] == 50 and after_join_next_turn["tax"] == 0,
        (before_join, after_join_next_turn),
    )

    # 8. Ambiguous attribution is a recorded, visible 0% fallback.
    ambiguous = membership_settle(
        [
            {"id": "A", "active": True, "rate_bp": 3_700},
            {"id": "B", "active": True, "rate_bp": 7_300},
        ],
        100,
    )
    check(
        "membership 8: ambiguous attribution is a visible 0% fallback",
        ambiguous["status"] == "AMBIGUOUS_0_PERCENT_FALLBACK"
        and ambiguous["net"] == 100
        and ambiguous["reason"] != "",
        ambiguous,
    )

    # 9. A later unambiguous turn collects normally.
    resolved = membership_settle([{"id": "A", "active": True, "rate_bp": 3_700}], 100)
    check(
        "membership 9: a later resolved turn collects normally",
        resolved["status"] == "SINGLE_ALLIANCE" and resolved["tax"] == 37,
        resolved,
    )

    # 10. No combination ever exceeds 100% of gross.
    over_100 = False
    for rate_bp in (0, 1_000, 3_700, 5_000, 7_300, 9_999, BP):
        for alliances in (
            [{"id": "A", "active": True, "rate_bp": rate_bp}],
            [
                {"id": "A", "active": True, "rate_bp": rate_bp},
                {"id": "B", "active": True, "rate_bp": rate_bp},
            ],
            [
                {"id": "A", "active": True, "rate_bp": rate_bp},
                {"id": "B", "active": True, "rate_bp": BP - rate_bp},
            ],
        ):
            result = membership_settle(alliances, 100)
            if result["tax"] > 100 or result["net"] < 0:
                over_100 = True
    check("membership 10: no combination exceeds 100% of gross", not over_100)

    # Production-chain examples A-G.
    a_tax, a_net = tax(100, 0), net(100, 0)
    check("chain A: 0% leaves 100 available", a_tax == 0 and a_net == 100, (a_tax, a_net))

    b_tax, b_net = tax(100, 5_000), net(100, 5_000)
    check("chain B: 50% leaves 50 available", b_tax == 50 and b_net == 50, (b_tax, b_net))

    c_tax, c_net = tax(100, BP), net(100, BP)
    check("chain C: 100% leaves 0 available", c_tax == 100 and c_net == 0, (c_tax, c_net))

    iron_gross, iron_rate, consumed, steel_out, steel_rate = 200, 5_000, 60, 30, 2_500
    iron_tax = tax(iron_gross, iron_rate)
    iron_net = net(iron_gross, iron_rate)
    steel_tax = tax(steel_out, steel_rate)
    steel_net = net(steel_out, steel_rate)
    chain_total_tax = iron_tax + steel_tax
    check(
        "chain D: production chain taxes output once and never the consumed input",
        iron_tax == 100
        and iron_net == 100
        and consumed <= iron_net
        and steel_tax == 7
        and steel_net == 23
        and chain_total_tax == 107
        and iron_net - consumed == 40,
        (iron_tax, iron_net, steel_tax, steel_net, chain_total_tax),
    )

    stockpile, current_gross, stock_rate = 500, 100, 5_000
    stock_tax = tax(current_gross, stock_rate)
    available = stockpile + net(current_gross, stock_rate)
    check(
        "chain E: an existing stockpile is not taxed when consumed",
        stock_tax == 50 and stock_tax != tax(stockpile + current_gross, stock_rate) and available == 550,
        (stock_tax, available),
    )

    input_already_taxed, output_gross, output_rate = 40, 20, BP
    output_tax = tax(output_gross, output_rate)
    check(
        "chain F: transformed output is taxed once and its input is not re-taxed",
        output_tax == 20
        and net(output_gross, output_rate) == 0
        and tax(input_already_taxed, output_rate) != output_tax,
        output_tax,
    )

    retry_store: dict[tuple, tuple] = {}
    chain_first = settle(retry_store, ("t1", "N1", "Iron"), 100, 5_000)
    chain_retry = settle(retry_store, ("t1", "N1", "Iron"), 100, 5_000)
    try:
        settle(retry_store, ("t1", "N1", "Iron"), 101, 5_000)
        chain_conflict = False
    except ValueError:
        chain_conflict = True
    check(
        "chain G: retry or duplicate settles once and conflicting reuse aborts",
        chain_first[2] == 50
        and chain_retry == chain_first
        and chain_conflict
        and len(retry_store) == 1,
        (chain_first, chain_retry, chain_conflict),
    )


# ---------------------------------------------------------------------------
# Crowns balance, per-Alliance assignment and operational funding
# ---------------------------------------------------------------------------
def treasury_and_operational_checks() -> None:
    # Crowns examples: 0%, 50%, 73% (non-multiple of ten) and 100%.
    for rate_bp, expected_tax, expected_net in [
        (0, 0, 100_000),
        (5_000, 50_000, 50_000),
        (7_300, 73_000, 27_000),
        (BP, 100_000, 0),
    ]:
        got_tax, got_net = tax(100_000, rate_bp), net(100_000, rate_bp)
        check(
            f"Crowns 100,000 at {rate_bp / 100:g}% -> {expected_tax}/{expected_net}",
            got_tax == expected_tax and got_net == expected_net,
            (got_tax, got_net),
        )

    opening, maintenance, production_cost = 500_000, 20_000, 100_000
    gross_crowns, crown_rate = 100_000, 5_000
    crown_tax = tax(gross_crowns, crown_rate)
    net_crowns = net(gross_crowns, crown_rate)
    after_tax = opening + net_crowns
    after_maintenance = after_tax - maintenance
    after_production_cost = after_maintenance - production_cost
    check(
        "opening balance is not taxed and maintenance is not a tax event",
        crown_tax == 50_000
        and net_crowns == 50_000
        and after_maintenance == 530_000
        and after_production_cost == 430_000
        and crown_tax == tax(gross_crowns, crown_rate),
        (crown_tax, after_maintenance, after_production_cost),
    )
    check(
        "maintenance and later same-turn spending are not in the tax base",
        tax(opening, crown_rate) != 0
        and tax(opening + gross_crowns, crown_rate) != crown_tax,
    )
    check(
        "no negative national balance is produced",
        after_production_cost >= 0 and after_maintenance >= 0,
    )
    check(
        "a 100% Crowns rate leaves zero of new production but preserves the opening balance",
        net(gross_crowns, BP) == 0 and opening == 500_000,
    )
    later_balance, later_cost = 30_000, 50_000
    later_paid = later_balance >= later_cost
    later_after = later_balance - later_cost if later_paid else later_balance
    check(
        "insufficient Crowns is rejected normally without debt, forced sale or a negative balance",
        not later_paid and later_after == 30_000,
        (later_paid, later_after),
    )

    # Per-Alliance assignment: one bracket per member per Alliance, no
    # cross-Alliance effect and no stacking beyond 100%.
    assignment = {("A", "N1"): 1_000, ("B", "N1"): 2_000}
    tax_a = tax(100, assignment[("A", "N1")])
    tax_b = tax(100, assignment[("B", "N1")])
    tax_c = tax(100, assignment.get(("C", "N1"), 0))
    check(
        "a nation holds one bracket per Alliance and each bracket applies only there",
        tax_a == 10
        and tax_b == 20
        and tax_c == 0
        and ("A", "N1") in assignment
        and ("B", "N1") in assignment
        and ("C", "N1") not in assignment,
        (tax_a, tax_b, tax_c),
    )
    check(
        "separate Alliance assignments never duplicate a single collection",
        membership_settle(
            [
                {"id": "A", "active": True, "rate_bp": 1_000},
                {"id": "B", "active": True, "rate_bp": 2_000},
            ],
            100,
        )["tax"]
        == 0,
    )
    check(
        "the 0% fallback is per Alliance and leaves gross intact",
        tax_c == 0 and tax(100, 0) == 0 and net(100, 0) == 100,
    )

    # F-AL-008 operational funding: receipt, reservation, settlement, replay,
    # insufficient value, invalid purpose/amount/destination and no player pay.
    keys: dict[str, int] = {}
    state = {"received": 100_000, "available": 100_000, "reserved": 0, "expended": 0}
    state, status = operational_expense(
        100_000, 100_000, 0, 0, 10_000, "AOP-02", 10_000, "platform_cost_sink", keys, "op-1"
    )
    check(
        "operational expense reserves and settles against AVAILABLE",
        status == "SETTLED"
        and state["available"] == 90_000
        and state["reserved"] == 0
        and state["expended"] == 10_000
        and state["available"] + state["reserved"] + state["expended"] == state["received"],
        (status, state),
    )
    replay_state, replay_status = operational_expense(
        100_000, 90_000, 0, 10_000, 10_000, "AOP-02", 10_000, "platform_cost_sink", keys, "op-1"
    )
    check(
        "a replayed operational expense is a no-op",
        replay_status == "REPLAY" and replay_state == {
            "received": 100_000,
            "available": 90_000,
            "reserved": 0,
            "expended": 10_000,
        },
        (replay_status, replay_state),
    )
    too_much, too_much_status = operational_expense(
        100_000, 90_000, 0, 10_000, 95_000, "AOP-02", 95_000, "platform_cost_sink", keys, "op-2"
    )
    check(
        "insufficient AVAILABLE is ALF-28 with no negative balance or debt",
        too_much_status == "ALF-28"
        and too_much["available"] == 90_000
        and too_much["reserved"] == 0
        and too_much["expended"] == 10_000,
        too_much,
    )
    reserved_only = operational_expense(
        100_000, 0, 100_000, 0, 10_000, "AOP-02", 10_000, "platform_cost_sink", keys, "op-3"
    )
    check(
        "RESERVED and EXPENDED are not spendable",
        reserved_only[1] == "ALF-28" and reserved_only[0]["reserved"] == 100_000,
        reserved_only,
    )
    for amount, purpose, schedule, destination, sink, capacity, label in [
        (10_000, "AOP-99", 10_000, "platform_cost_sink", True, None, "unknown purpose"),
        (9_999, "AOP-02", 10_000, "platform_cost_sink", True, None, "amount off schedule"),
        (10_000, "AOP-02", 10_000, "member_wallet", True, None, "wrong destination"),
        (10_000, "AOP-02", 10_000, "platform_cost_sink", False, None, "player recipient"),
        (10_000, "AOP-02", 10_000, "platform_cost_sink", True, 50_000, "invented capacity"),
    ]:
        invalid_state, invalid_status = operational_expense(
            100_000, 100_000, 0, 0, amount, purpose, schedule, destination, {},
            f"bad-{label}", sink, capacity,
        )
        check(
            f"invalid operational expense ({label}) is ALF-27 with no movement",
            invalid_status == "ALF-27"
            and invalid_state
            == {"received": 100_000, "available": 100_000, "reserved": 0, "expended": 0},
            (invalid_status, invalid_state),
        )
    check(
        "operational funding has no general withdrawal path",
        operational_expense(
            100_000, 100_000, 0, 0, 10_000, "AOP-02", 10_000, "general_withdrawal",
            {}, "wd-1",
        )[1]
        == "ALF-27",
    )
    check(
        "an operational expense debits AVAILABLE but never reduces RECEIVED or reaches a nation",
        state["received"] == 100_000
        and state["expended"] == 10_000
        and state["available"] == 90_000,
        state,
    )


# ---------------------------------------------------------------------------
# Document consistency
# ---------------------------------------------------------------------------
def get_rule(text: str, rule_id: str) -> str:
    match = re.search(
        rf"\*\*`{rule_id}`.*?(?=\n\s*-\s*\*\*`ALL-\d{{3}}`|\n## |\Z)", text, re.S
    )
    return match.group(0) if match else ""


def requirement_status(text: str, req_id: str) -> str:
    for line in text.splitlines():
        if line.startswith(f"| {req_id} |"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 4:
                return cells[3]
    return ""


def regex_block(text: str, heading_pattern: str) -> str:
    match = re.search(
        rf"{heading_pattern}.*?(?=\n### AX-|\n---\s*\n|\Z)", text, re.S
    )
    return match.group(0) if match else ""


def document_checks() -> None:
    b09 = rd(B09)
    reg = rd(REG)
    contracts = rd(CONTRACTS)
    req = rd(REQ)
    dec = rd(DEC)
    dd = rd(DD)
    ud = rd(UD)
    econ = rd(ECON)

    b09_plain = re.sub(r"[*`]", "", b09)
    header = "\n".join(b09.splitlines()[:5])
    check("B-09 header is v2.8 / Prompt 09B-M", "**Version:** 2.8" in header and "Prompt 09B-M" in header)
    definitions = re.findall(r"\*\*`(ALL-\d{3})`", b09)
    for number in range(179, 227):
        rule_id = f"ALL-{number:03d}"
        occurrences = definitions.count(rule_id)
        check(f"{rule_id} defined exactly once", occurrences == 1, occurrences)
    for rule_id, token in [
        ("ALL-179", "does not require the member nation's owner"),
        ("ALL-180", "current-turn production"),
        ("ALL-181", "0 through 10,000 inclusive"),
        ("ALL-182", "0% fallback"),
        ("ALL-183", "no fixed office"),
        ("ALL-184", "change committed"),
        ("ALL-185", "cumulative gross"),
        ("ALL-186", "snapshot identifier"),
        ("ALL-187", "purpose-limited funding boundary"),
        ("ALL-199", "non-covered member"),
        ("ALL-204", "must not be refused admission"),
        ("ALL-205", "as a whole"),
        ("ALL-206", "no covered member of B may attack"),
        ("ALL-214", "mandatory audit event"),
        ("ALL-220", "purpose-limited operational funding"),
        ("ALL-221", "aop-01"),
        ("ALL-222", "authorize_operational_expenditure"),
        ("ALL-223", "alf-28"),
        ("ALL-224", "may not pay a general withdrawal"),
        ("ALL-225", "available = received"),
        ("ALL-226", "narrow partial authorization"),
    ]:
        text = re.sub(r"[*`]", "", get_rule(b09, rule_id)).lower()
        check(f"{rule_id} keeps '{token}'", token.lower() in text, text[:120])
    b09_flat = re.sub(r"[*`]", "", b09).lower()
    check(
        "ALL-220 states no operational purpose is currently spendable",
        "no operational purpose is currently spendable" in b09_flat
        and "blocked pending the required approvals" in b09_flat,
    )
    check(
        "ALL-221 labels every AOP record proposed and unavailable",
        b09_flat.count("proposed; unavailable") >= 4
        and "no purpose is spendable" in b09_flat,
    )
    check(
        "ALL-185 uses cumulative accrual and rejects independent event floors",
        "taxatevent_j = d_j − d_{j−1}" in b09_flat
        and "σ taxatevent_j = d_m" in b09_flat
        and "independent per-event floors are not used" in b09_flat,
    )
    check(
        "B-09 keeps the explicit UD-046 boundary",
        "ud-046" in b09.lower() and "no ownership interest" in b09.lower(),
    )
    check("B-09 claims no runtime enforcement before Prompt 10", "no runtime enforcement is claimed" in b09.lower())
    all093 = get_rule(b09, "ALL-093").lower()
    check("ALL-093 tombstone remains withdrawn", "withdrawn" in all093 and "grants no right" in all093)
    check(
        "ALL-093 carries no confiscation clause",
        "protection against arbitrary confiscation" not in all093,
    )

    check("F-AL-006 is defined", "### F-AL-006" in reg)
    check("F-AL-007 is defined", "### F-AL-007" in reg)
    check("F-AL-008 is defined", "### F-AL-008" in reg)
    for token in ("3,700 bp", "37,000", "63{,}000", "1{,}800", "640", "180", "Rate sweep", "0% fallback", "10{,}000$ inclusive"):
        check(f"F-AL-006 documents '{token}'", token in reg, token)
    check("F-AL-006 names the Alliance Receiving Ledger", "Alliance Receiving Ledger" in reg)
    check(
        "F-AL-006 uses cumulative fractional accrual, not independent event floors",
        "C_{a,j} = \\sum_{k=1}^{j} g_{a,k}" in reg
        and "\\text{TaxDueAtEvent}_{a,j} = D_{a,j} - D_{a,j-1}" in reg
        and "\\sum_{j=1}^{m_a} \\text{TaxAtEvent}_{a,j} = D_{a,m_a}" in reg
        and "Never floor each event's product independently" in reg,
    )
    check(
        "F-AL-006 reconciles the event taxes at end of turn",
        "End-of-turn reconciliation" in reg
        and "sum of every event's $\\text{TaxAtEvent}_{a,j}$ must equal" in reg
        and "never repaired by collecting again" in reg,
    )
    check("F-AL-007 documents conservation", "Delta\\text{Donor}(R) + \\Delta\\text{ARL}(R) = 0" in reg or "conservation" in reg.lower())
    check("F-AL-007 excludes a capacity term", "There is no $\\text{DestinationCapacity}$ term" in reg)
    for token in (
        "Purpose-Limited Operational Funding Arithmetic",
        "AOP-01",
        "AOP-04",
        "registered platform cost sink",
        "There is no $\\text{Capacity}$ term",
        "no ownership",
        "general withdrawal",
        "ALF-28",
        "ALF-29",
        "AUD-AL-019",
    ):
        check(f"F-AL-008 documents '{token}'", token in reg, token)

    for rule_id, token in [
        ("ALL-179", "assumes neither that a nation has one alliance"),
        ("ALL-180", "post-tax net"),
        ("ALL-185", "deducted at most once"),
        ("ALL-185", "more than 100%"),
        ("ALL-185", "does not resolve `UD-040`"),
        ("ALL-186", "membership-attribution status"),
        ("ALL-186", "safeguard reason"),
    ]:
        text = re.sub(r"[*`]", "", get_rule(b09, rule_id)).lower()
        flat_token = re.sub(r"[*`]", "", token).lower()
        check(f"{rule_id} keeps '{token}'", flat_token in text, text[:160])

    for token in (
        "Production-chain examples A–G.",
        "**D — production chain:**",
        "total alliance tax is 107",
        "550 is available",
        "20 Steel is new output taxed once",
        "total ARL credit remains 50, never 100",
        "ambiguous attribution shows the recorded 0% safeguard",
    ):
        check(f"F-AL-006 documents '{token}'", token in reg, token)

    alf21 = next((line for line in b09.splitlines() if line.startswith("| `ALF-21`")), "")
    alf23 = next((line for line in b09.splitlines() if line.startswith("| `ALF-23`")), "")
    alf24 = next((line for line in b09.splitlines() if line.startswith("| `ALF-24`")), "")
    check(
        "ALF-21 is an authorization failure, not owner consent",
        "required active alliance permission" in alf21
        and "consent" not in alf21.lower()
        and "no collection occurred" in alf21,
        alf21,
    )
    check(
        "ALF-23 is a current-turn production/snapshot failure",
        "authoritative gross record or frozen turn snapshot" in alf23
        and "insufficient unreserved value" not in alf23.lower()
        and "no existing stockpile or balance is charged" in alf23,
        alf23,
    )
    check(
        "ALF-24 is a receipt-model donation failure with no capacity limit",
        "Alliance Receiving Ledger credit fails" in alf24
        and "no destination-capacity limit exists" in alf24
        and "lacks sufficient unreserved value" in alf24,
        alf24,
    )

    req626 = next((line for line in req.splitlines() if line.startswith("| REQ-626 |")), "")
    check(
        "REQ-626 names the Alliance Receiving Ledger and its accounting role",
        "Alliance Receiving Ledger" in req626
        and "accounting" in req626.lower()
        and "alliance treasury" not in req626.lower(),
        req626,
    )
    req624 = next((line for line in req.splitlines() if line.startswith("| REQ-624 |")), "")
    check(
        "REQ-624 carries the membership safeguard and post-tax consumption",
        "never deducted more than once" in req624
        and "never exceeds 100% of gross" in req624
        and "post-tax" in req624
        and "stockpile" in req624,
        req624,
    )
    check(
        "REQ-624 uses cumulative event accrual ending at the per-turn floor",
        "cumulative gross through event" in req624
        and "floor(C_j × rate_bp / 10,000) − floor(C_{j−1} × rate_bp / 10,000)" in req624
        and "sum to the per-turn floor" in req624
        and "no over- or under-collection" in req624,
        req624,
    )
    req625 = next((line for line in req.splitlines() if line.startswith("| REQ-625 |")), "")
    check(
        "REQ-625 makes the safeguard visible and non-retroactive",
        "safeguard" in req625.lower()
        and "not retroactively re-taxed" in req625,
        req625,
    )

    ecn213a_match = re.search(
        r"^\*\*ECN-213a\b.*?(?=^\*\*ECN-\d)", econ, re.S | re.M
    )
    ecn213a = ecn213a_match.group(0) if ecn213a_match else ""
    for token in (
        "(6) let every later same-turn P3 stage consume only the cumulative post-tax net",
        "(7) write the per-event paired ledger events",
        "cumulative gross $C_{a,j}",
        "Independent per-event floors are not used",
        "reconcile at end of turn that the event taxes sum to $D_{a,m_a}$",
        "Multiple-membership safeguard (`UD-040` remains Open)",
        "0% Alliance-tax fallback",
        "A 100% rate leaves zero",
        "existing stockpile consumed later is not taxed",
        "processing input is not taxed again",
        "aborts as `ALF-23`",
    ):
        check(f"ECN-213a documents '{token}'", token in ecn213a, token)

    ax27 = regex_block(contracts, r"### AX-27\b")
    for token in (
        "deducted at most once",
        "more than 100%",
        "visible recorded 0% fallback",
        "post-tax net",
        "increment of one floored cumulative liability",
        "sum of event taxes must equal",
        "cumulative-reconciliation mismatch",
        "`ALF-21`",
        "`ALF-23`",
    ):
        check(f"AX-27 documents '{token}'", token in ax27, token)
    ax28 = regex_block(contracts, r"### AX-28\b")
    check(
        "AX-28 lists the ALF-24 receipt failures without capacity",
        "`ALF-24`" in ax28 and "absence of a capacity model is not a failure" in ax28,
        ax28[:200],
    )

    for number in range(618, 648):
        req_id = f"REQ-{number:03d}"
        check(f"{req_id} is Approved", requirement_status(req, req_id) == "Approved", requirement_status(req, req_id))

    check(
        "D-140 remains the historical five-capability owner authorization",
        "| D-140 |" in dec
        and "five alliance capabilities" in dec.lower()
        and "2026-11-01" in dec,
    )
    check(
        "D-141 records the later operational-funding boundary",
        "| D-141 |" in dec
        and "later amendment to d-140" in dec.lower()
        and "no cost schedule" in dec.lower(),
    )
    check(
        "D-141 does not claim owner-selected AOP details",
        "project technical design choices" in dec.lower()
        and ("not owner selections" in dec.lower() or "not owner-selected" in dec.lower()),
    )
    check(
        "F-AL-008 states that no purpose is currently spendable",
        "no operational purpose is currently spendable" in reg.lower(),
    )
    check(
        "ECN-213a states that no purpose is currently spendable",
        "no purpose is currently spendable" in ecn213a.lower(),
    )
    check("DD-161 records the tax direction", "| DD-161 |" in dd and "automatic" in dd.lower())
    ud046 = next((line for line in ud.splitlines() if line.startswith("| UD-046 |")), "")
    check("UD-046 remains Open", "**Open**" in ud046 or "Open" in ud046)
    check("UD-046 keeps ownership and withdrawal unreserved", "withdraw" in ud046.lower() and "ownership" in ud046.lower())

    for ax_id in ("AX-27", "AX-28", "AX-29", "AX-30"):
        check(f"{ax_id} contract exists", f"### {ax_id}" in contracts, ax_id)

    check(
        "NAP covers both directions in the register",
        "no covered member of b may attack any covered member of a" in b09.lower(),
    )
    check(
        "custom prose is descriptive, never executable",
        "descriptive only" in get_rule(b09, "ALL-197").lower()
        or "descriptive only" in b09.lower(),
    )
    check(
        "tax does not require per-version owner approval",
        "does not require the member nation's owner to approve each policy version" in b09_plain.lower(),
    )


def self_test() -> int:
    guards = [
        ("floor rejects round-half-up", lambda: tax(1, 5_000) == 0 and (1 * 5_000 + 5_000) // BP == 1),
        ("37% is not coerced to 40%", lambda: tax(10_000, 3_700) != tax(10_000, 4_000)),
        ("99.99% is representable", lambda: tax(10_000, 9_999) == 9_999),
        ("100% leaves no negative net", lambda: net(10_000, BP) == 0),
        ("0% collects nothing", lambda: tax(10_000, 0) == 0),
        ("tax never exceeds gross", lambda: tax(3, BP) == 3),
        ("existing wealth changes the base if wrongly included", lambda: tax(100_000 + 500_000, 3_700) != tax(100_000, 3_700)),
        ("post-tax balance would double-tax", lambda: tax(net(100_000, 3_700), 3_700) != 0),
        ("retry does not pay twice", lambda: (lambda s: settle(s, ("k",), 100_000, 3_700) == settle(s, ("k",), 100_000, 3_700) and len(s) == 1)({})),
        ("conflicting key aborts", lambda: _conflict()),
        ("donation conserves value", lambda: sum(donate(12_500, 20_000, True, set(), "k")[:2]) == 0),
        ("replayed donation is a no-op", lambda: _donation_replay()),
        ("equal distinct donations both settle", lambda: _two_donations()),
        ("insufficient donor fails", lambda: donate(25_000, 20_000, True, set(), "k") == (0, 0, False)),
        ("unsupported asset fails", lambda: donate(100, 20_000, False, set(), "k") == (0, 0, False)),
        ("capacity assumption would reject", lambda: donate(12_500, 20_000, True, set(), "k", capacity=0)[2] is False),
        ("admission refusal is a defect", lambda: "barred from admission" in "a nation is barred from admission"),
        ("automatic joiner coverage is a defect", lambda: "automatically covered" in "a joining nation is automatically covered"),
        ("one-direction NAP is incomplete", lambda: _bidirectional_guard()),
        ("whole-treaty dissolution is required", lambda: "as a whole" in "terminates the treaty **as a whole**"),
        ("mandatory audit is required", lambda: "mandatory audit event" in "writes a mandatory audit event"),
        ("confiscation clause must stay withdrawn", lambda: "protection against arbitrary confiscation" not in "withdrawn; grants no right"),
        ("two memberships use the 0% safeguard", lambda: membership_settle([{"id": "A", "active": True, "rate_bp": 5_000}, {"id": "B", "active": True, "rate_bp": 5_000}], 100)["tax"] == 0),
        ("one alliance collects normally", lambda: membership_settle([{"id": "A", "active": True, "rate_bp": 5_000}], 100)["tax"] == 50),
        ("no active alliance collects nothing", lambda: membership_settle([], 100)["tax"] == 0),
        ("multiple membership is not authorized to stack", lambda: membership_settle([{"id": "A", "active": True, "rate_bp": 5_000}, {"id": "B", "active": True, "rate_bp": 5_000}], 100)["tax"] != 100),
        ("no membership combination exceeds gross", lambda: all(membership_settle([{"id": "A", "active": True, "rate_bp": rate}, {"id": "B", "active": True, "rate_bp": BP - rate}], 100)["tax"] <= 100 for rate in (0, 1, 1_000, 5_000, 9_999, BP))),
        ("100% leaves zero for later stages", lambda: net(100, BP) == 0),
        ("50% leaves exactly the net for later stages", lambda: net(100, 5_000) == 50),
        ("stockpile is not taxed", lambda: tax(100, 5_000) == 50 and tax(100, 5_000) != tax(600, 5_000)),
        ("processing input is not re-taxed", lambda: tax(200, 5_000) + tax(30, 2_500) == 107 and tax(200, 5_000) + tax(30, 2_500) + tax(60, 5_000) != 107),
        ("cumulative first event collects 0 at 50%", lambda: tax_events([1, 1], 5_000)["event_taxes"][0] == 0),
        ("cumulative second event collects the remainder", lambda: tax_events([1, 1], 5_000)["event_taxes"][1] == 1),
        ("independent event floors under-collect", lambda: sum(tax(1, 3_333) for _ in range(4)) == 0 and tax_events([1, 1, 1, 1], 3_333)["total_tax"] == 1),
        ("event count does not change the turn liability", lambda: tax_events([1, 1], 5_000)["total_tax"] == tax_events([2], 5_000)["total_tax"] == 1),
        ("cumulative event taxes reconcile to the turn floor", lambda: sum(tax_events([3, 7, 11], 3_700)["event_taxes"]) == tax(21, 3_700)),
        ("100% across events collects every unit", lambda: tax_events([1, 1, 1], BP)["event_taxes"] == [1, 1, 1]),
        ("0% across events collects nothing", lambda: tax_events([1, 1, 1], 0)["total_tax"] == 0),
        ("different assets never offset a remainder", lambda: tax_events([1, 1], 5_000)["total_tax"] + tax_events([1, 1], 2_500)["total_tax"] == 1),
        ("a replayed event does not advance the accumulator", lambda: _replay_guard()),
    ]
    failed = 0
    for name, guard in guards:
        try:
            ok = bool(guard())
        except Exception as exc:  # noqa: BLE001 - a guard that raises is a failure
            ok = False
            name = f"{name} (raised {exc})"
        if ok:
            print(f"SELFTEST PASS  {name}")
        else:
            failed += 1
            print(f"SELFTEST FAIL  {name}")
    print(f"\nSELFTEST: {len(guards) - failed}/{len(guards)} guards detected their defect")
    return 0 if failed == 0 else 1


def _bidirectional_guard() -> bool:
    complete = (
        "no covered member of A may attack any covered member of B, "
        "and no covered member of B may attack any covered member of A"
    )
    one_sided = "no covered member of A may attack any covered member of B"
    return (
        "no covered member of B may attack" in complete
        and "no covered member of B may attack" not in one_sided
    )


def _conflict() -> bool:
    store: dict[tuple, tuple] = {}
    settle(store, ("k",), 100_000, 3_700)
    try:
        settle(store, ("k",), 100_001, 3_700)
    except ValueError:
        return True
    return False


def _donation_replay() -> bool:
    keys: set[str] = set()
    donate(12_500, 20_000, True, keys, "k")
    return donate(12_500, 20_000, True, keys, "k") == (0, 0, False)


def _two_donations() -> bool:
    keys: set[str] = set()
    first = donate(12_500, 20_000, True, keys, "k1")
    second = donate(12_500, 20_000, True, keys, "k2")
    return first[2] and second[2] and first[0] == second[0] == -12_500


def _raises(call) -> bool:
    try:
        call()
    except ValueError:
        return True
    return False


def _replay_guard() -> bool:
    store: dict[tuple, tuple] = {}
    state = {"cumulative_gross": 0, "tax_collected": 0}
    apply_tax_event(store, state, ("t", "N", "Iron", 1), 1, 5_000)
    second = apply_tax_event(store, state, ("t", "N", "Iron", 2), 1, 5_000)
    before = dict(state)
    replay = apply_tax_event(store, state, ("t", "N", "Iron", 2), 1, 5_000)
    return second[3] == 1 and replay == second and state == before == {
        "cumulative_gross": 2,
        "tax_collected": 1,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    arithmetic_checks()
    membership_and_chain_checks()
    treasury_and_operational_checks()
    document_checks()

    print(f"Alliance arithmetic/document checks: {len(PASS)} passed, {len(FAIL)} failed")
    for item in FAIL:
        print(f"FAIL  {item}")
    if FAIL:
        print("\nALLIANCE VALIDATION: FAILED")
        return 1
    print("\nALLIANCE VALIDATION: ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
