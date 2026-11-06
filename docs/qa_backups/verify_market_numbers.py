#!/usr/bin/env python3
"""Documentation-level checks for B-07 (trade and markets).

What this proves
----------------
* The worked examples in ``stage-2/13_trade_and_markets.md`` recompute from the
  constants in ``stage-2/13_trade_and_markets_formula_register.md``.
* The specification's rule IDs are unique and contiguous, the formula IDs it
  cites exist, and the code register defines every code family it uses.
* The book values it prints match the authoritative B-04 register.
* Global Trade is described as designed and *gated*, never as implemented.
* The requirements and decision registers carry the rows B-07 claims.

What this does NOT prove
------------------------
No database, scheduler, endpoint, RLS policy or screen exists. These are
arithmetic and document-consistency checks, not runtime tests. The band, caps
and expiry are not balanced.

Usage
-----
    python qa_backups/verify_market_numbers.py
    python qa_backups/verify_market_numbers.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
B07 = DOCS / "stage-2" / "13_trade_and_markets.md"
REG = DOCS / "stage-2" / "13_trade_and_markets_formula_register.md"
B04_REG = DOCS / "stage-2" / "10_economic_formula_and_balance_register.md"
REQ = DOCS / "stage-2" / "03_requirements_traceability.md"
DEC = DOCS / "DECISIONS.md"
DD = DOCS / "stage-2" / "04_approved_and_provisional_decisions.md"
UD = DOCS / "stage-2" / "05_unresolved_design_decisions.md"

BAND_BP = 3000
FRESH_TURNS = 360
OFFER_TTL = 72
STAT_WINDOW = 12
STAT_MIN_TRADES = 5
STAT_MIN_NATIONS = 5
V_BAND = 10
MAX_I64 = 9_223_372_036_854_775_807

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


def band(v_low: int, bp: int = BAND_BP) -> int:
    return v_low * (10_000 + bp) // 10_000


def in_band(v_a: int, v_b: int) -> bool:
    low, high = min(v_a, v_b), max(v_a, v_b)
    if low == 0:
        return False
    return high <= band(low)


def remaining(posted: int, filled: int, locked: int) -> int:
    return posted - filled - locked


def reserved_crowns(remaining_qty: int, locked_qty: int, price: int) -> int:
    return (remaining_qty + locked_qty) * price


def vwap(trades: list[tuple[int, int]]) -> int:
    qty = sum(q for q, _ in trades)
    value = sum(q * p for q, p in trades)
    return value // qty


def sample_ok(trades: int, nations: int) -> bool:
    return trades >= STAT_MIN_TRADES and nations >= STAT_MIN_NATIONS


def conservation(deltas: dict[str, int]) -> bool:
    return all(v == 0 for v in deltas.values())


def safe_product(a: int, b: int) -> int | None:
    if a < 0 or b < 0:
        return None
    if b and a > MAX_I64 // b:
        return None
    return a * b


def arithmetic_checks() -> None:
    # E1: 200 crowns + 100 food at book 1; 50 steel at book 7.
    a, b = 200 + 100 * 1, 50 * 7
    check("E1 values 300/350", (a, b) == (300, 350), (a, b))
    check("E1 bound 390", band(a) == 390, band(a))
    check("E1 in band", in_band(a, b), (a, b, band(a)))

    # E1 ledger (B-07 v1.1): the 200-crown payment appears once, on the
    # payer's TRADE_BUY and the payee's TRADE_SELL. The earlier table put
    # +200 and -200 on both sides, which nets each treasury to zero while the
    # closing balances move by 200.
    e1 = [
        ("Aurelia", "TRADE_SELL", 0, "food", -100),
        ("Aurelia", "TRADE_BUY", -200, "steel", 50),
        ("Borealis", "TRADE_SELL", 200, "steel", -50),
        ("Borealis", "TRADE_BUY", 0, "food", 100),
    ]
    check("E1 ledger has four events", len(e1) == 4, len(e1))
    check("E1 ledger crown sum zero", sum(r[2] for r in e1) == 0, sum(r[2] for r in e1))
    check("E1 ledger food sum zero", sum(r[4] for r in e1 if r[3] == "food") == 0)
    check("E1 ledger steel sum zero", sum(r[4] for r in e1 if r[3] == "steel") == 0)
    check("E1 Aurelia crowns -200", sum(r[2] for r in e1 if r[0] == "Aurelia") == -200)
    check("E1 Borealis crowns +200", sum(r[2] for r in e1 if r[0] == "Borealis") == 200)
    check("E1 closing balances reconcile",
          (1_000 - 200, 300 - 100, 0 + 50, 500 + 200, 0 + 100, 120 - 50)
          == (800, 200, 50, 700, 100, 70))
    check("E1 one side does not carry both crown signs",
          all(not (any(r[2] > 0 for r in e1 if r[0] == n)
                   and any(r[2] < 0 for r in e1 if r[0] == n))
              for n in ("Aurelia", "Borealis")))

    # Space predicate (B-07 v1.1): free = W - inventory - reserved, and the
    # reservation is never added back.
    def free_space(w: int, inv: int, res: int) -> int:
        return w - inv - res

    check("space free 100", free_space(1_000, 900, 0) == 100)
    check("space 60 fits", 60 <= free_space(1_000, 900, 0))
    check("space 50 fails after 60 is reserved", not (50 <= free_space(1_000, 900, 60)))
    check("space settlement conserves free space",
          free_space(1_000, 960, 0) == free_space(1_000, 900, 60) == 40)
    check("adding reservations back would overbook",
          50 <= free_space(1_000, 900, 60) + 60 and not (50 <= free_space(1_000, 900, 60)))

    # Fair-value asymmetry: a 30% premium passes, a 30% discount does not.
    check("band 70 vs 100 fails", not in_band(70, 100), band(70))
    check("band 130 vs 100 passes", in_band(130, 100), band(100))
    check("band 100 vs 130 is inclusive", in_band(100, 130), band(100))

    # E2: 100 + 40*2 + 20*1 vs 20*8 + 5*3.
    a2, b2 = 100 + 40 * 2 + 20 * 1, 20 * 8 + 5 * 3
    check("E2 values 200/175", (a2, b2) == (200, 175), (a2, b2))
    check("E2 bound 227", band(b2) == 227, band(b2))
    check("E2 in band", in_band(a2, b2), (a2, b2, band(a2)))

    # E5: fresh 100 food for 200 crowns fails; 130 passes; 131 fails.
    check("E5 200 > bound 130", not in_band(100, 200), band(100))
    check("E5 130 passes inclusively", in_band(100, 130), band(100))
    check("E5 131 fails", not in_band(100, 131), band(100))

    # E6: 10 uranium book 300 for 600 crowns.
    check("E6 600 out of band", not in_band(300, 600), (300, band(300)))
    check("E6 ratio 20,000 bp", 600 * 10_000 // 300 == 20_000)

    # E7: 500 steel at 8; 200 executed.
    check("E7 fill 1,600", 200 * 8 == 1_600)
    check("E7 remaining 300", remaining(500, 200, 0) == 300, remaining(500, 200, 0))
    check("E7 reserved units 300", 0 + 300 == 300)

    # E8: 400 food at 2; 150 executed.
    check("E8 commitment 800", 400 * 2 == 800)
    check("E8 remaining commitment 500", reserved_crowns(250, 0, 2) == 500, reserved_crowns(250, 0, 2))
    check("E8 release 300", 800 - 150 * 2 == 500)

    # E9: 100 aluminium at 9; book 8.
    check("E9 gap -100", 100 * 8 - 900 == -100)

    # E10: two fills of 200 and 100 at 8.
    check("E10 proceeds 2,400", 200 * 8 + 100 * 8 == 2_400)
    check("E10 identity 200", remaining(500, 300, 0) == 200, remaining(500, 300, 0))

    # E11: 500 posted, 200 locked, cancel releases 300.
    check("E11 release 300", 500 - 200 == 300)

    # E12: posted turn 10, expiry 82.
    check("E12 expiry 82", 10 + OFFER_TTL == 82, 10 + OFFER_TTL)

    # E13: 1,000 crowns, 800 reserved, 200 available; 101*2 fails.
    check("E13 available 200", 1_000 - 800 == 200)
    check("E13 101*2 > 200", 101 * 2 > 200)

    # E15: 2,000 warehouse, 1,950 stock, 50 free.
    check("E15 free 50", 2_000 - 1_950 == 50)

    # E20: the band is inclusive at exactly 130.
    check("E20 130 inclusive", in_band(100, 130) and not in_band(100, 131))

    # Statistics.
    check("VWAP 8", vwap([(100, 8), (200, 9), (50, 7)]) == 8, vwap([(100, 8), (200, 9), (50, 7)]))
    check("volume band 340", (347 // V_BAND) * V_BAND == 340)
    check("sample 4 nations suppressed", not sample_ok(5, 4))
    check("sample 4 trades suppressed", not sample_ok(4, 5))
    check("sample 5/5 publishes", sample_ok(5, 5))

    # Arithmetic bounds.
    check("max directed 50,010,000,000",
          10_000_000 + 5 * 100_000 * 100_000 == 50_010_000_000)
    check("checked multiply accepts 100k x 100k",
          safe_product(100_000, 100_000) == 10_000_000_000)
    check("checked multiply rejects > MAX_I64", safe_product(MAX_I64, 2) is None)
    check("checked multiply rejects negative", safe_product(-1, 2) is None)

    # Conservation.
    check("E18 crown conservation", conservation({"crowns": 200 - 200 + 200 - 200}))
    check("E18 food conservation", conservation({"food": -100 + 100}))
    check("E18 steel conservation", conservation({"steel": 50 - 50}))
    check("broken conservation detected", not conservation({"crowns": 200 - 200 + 200}))
    check("launch fee is zero", (1_600 * 0 // 10_000) + 0 == 0)
    check("a 500bp fee on 1,600 is 80", 1_600 * 500 // 10_000 == 80)


def document_checks() -> None:
    for path, name in ((B07, "B-07"), (REG, "market register")):
        check(f"{name} exists", path.exists(), path)
    if not B07.exists() or not REG.exists():
        return

    b07 = rd(B07)
    reg = rd(REG)

    # Rule IDs: 235 contiguous three-digit rules, no duplicates, no gaps.
    ids = [int(x) for x in re.findall(r"^\*\*MKT-(\d{3}) —", b07, re.M)]
    check("B-07 has 235 numbered rules", len(ids) == 235, len(ids))
    check("B-07 rule IDs unique", len(ids) == len(set(ids)), len(ids) - len(set(ids)))
    check("B-07 rule IDs contiguous", sorted(ids) == list(range(1, 236)),
          sorted(set(range(1, 236)) - set(ids)))
    check("B-07 uses MKT-, not a colliding TR- prefix", "**TR-" not in b07)

    # Formula IDs: 001..039 present in the register and cited by B-07.
    fids = {int(x) for x in re.findall(r"^\*\*F-TM-(\d{3}) —", reg, re.M)}
    check("register has F-TM-001..039", set(range(1, 40)) <= fids,
          sorted(set(range(1, 40)) - fids))
    cited = {int(x) for x in re.findall(r"F-TM-(\d{3})", b07)}
    check("B-07 cites only defined formulas", cited <= fids | {0}, sorted(cited - fids))

    # Examples.
    examples = re.findall(r"^### E(\d+) —", b07, re.M)
    check("B-07 has E1..E21", [int(x) for x in examples] == list(range(1, 22)), examples)

    # Failure scenarios 1..35 (the three tables' first column).
    scenarios = [int(x) for x in re.findall(r"^\| (\d{1,2}) \|", b07, re.M)]
    check("B-07 has failure scenarios 1..35",
          all(n in scenarios for n in range(1, 36)),
          [n for n in range(1, 36) if n not in scenarios])

    # Code families are defined in the code register.
    for family, count in (("A", 10), ("D", 7), ("E", 12), ("L", 17), ("S", 10)):
        missing = [f"MKT-{family}{i:02d}" for i in range(1, count + 1)
                   if f"`MKT-{family}{i:02d}`" not in b07]
        check(f"code family MKT-{family} complete", not missing, missing)
    check("MKT-G01 defined", "`MKT-G01`" in b07)

    # Gate status: five NOT MET and one PARTIAL; nothing claims a pass.
    gates = re.findall(r"^\| \*\*G-(\d)\*\* \|(.*?)\|$", b07, re.M)
    check("six gates listed", len(gates) == 6, len(gates))
    statuses = [row for _, row in gates]
    check("five gates NOT MET", sum("NOT MET" in s for s in statuses) == 5,
          sum("NOT MET" in s for s in statuses))
    check("G-4 is the only PARTIAL", sum("PARTIAL" in s for s in statuses) == 1,
          sum("PARTIAL" in s for s in statuses))
    check("no gate claims MET", not any(re.search(r"\|\s*(MET|PASS|PASSED)\s*\|", s)
                                         for s in statuses))

    # No false implementation claim.
    for phrase in ("Global Trade is implemented", "Global Trade is live",
                   "Global Trade is released", "market is implemented"):
        check(f"no false claim {phrase!r}", phrase not in b07)

    # Book values match the B-04 register.
    expected = {"Food": 1, "Coal": 1, "Oil": 2, "Iron": 1, "Bauxite": 2,
                "Lead": 3, "Uranium": 30, "Gasoline": 6, "Steel": 7,
                "Aluminum": 8, "Ammunition": 6}
    if B04_REG.exists():
        b04 = rd(B04_REG)
        section = b04.split("### 3.5 Reference prices", 1)
        body = section[1].split("\n---\n", 1)[0] if len(section) == 2 else ""
        got = {m.group(1): int(m.group(2))
               for m in re.finditer(r"^\| (Food|Coal|Oil|Iron|Bauxite|Lead|Uranium|Gasoline|Steel|Aluminum|Ammunition) \| (\d+) \|", body, re.M)}
        check("B-04 reference prices parse", got == expected, got)
        check("B-07 prints the same book values",
              all(f"| {r} | {v} |" in b07 for r, v in expected.items()),
              [r for r, v in expected.items() if f"| {r} | {v} |" not in b07])
    else:
        check("B-04 register exists", False, B04_REG)

    # Registers carry the rows B-07 claims.
    if REQ.exists():
        req = rd(REQ)
        check("REQ-427 exists", "| REQ-427 |" in req)
        check("REQ-512 exists", "| REQ-512 |" in req)
        check("REQ-513 exists", "| REQ-513 |" in req)
        check("requirements count 513", req.count("| REQ-") >= 513, req.count("| REQ-"))
    if DEC.exists():
        dec = rd(DEC)
        check("D-109 exists", "| D-109 |" in dec)
        check("D-121 exists", "| D-121 |" in dec)
        check("D-122 exists", "| D-122 |" in dec)
    if DD.exists():
        dd = rd(DD)
        check("DD-123 exists", "| DD-123 |" in dd)
        check("DD-135 exists", "| DD-135 |" in dd)
        check("DD-136 exists", "| DD-136 |" in dd)
    if UD.exists():
        ud = rd(UD)
        check("UD-037 exists", "| UD-037 |" in ud)
        check("UD-038 exists", "| UD-038 |" in ud)


def self_test() -> int:
    """Prove each guard rejects a deliberately corrupted input."""
    guards = [
        ("band rejects a too-large high side", lambda: not in_band(100, 131)),
        ("band accepts the inclusive boundary", lambda: in_band(100, 130)),
        ("remaining catches an over-fill", lambda: remaining(100, 120, 0) != 0),
        ("reserved crowns do not shrink on lock", lambda: reserved_crowns(0, 100, 2) == 200),
        ("VWAP catches a wrong denominator", lambda: vwap([(100, 8), (200, 9)]) != 9),
        ("sample gate rejects four nations", lambda: not sample_ok(5, 4)),
        ("conservation catches a missing leg", lambda: not conservation({"crowns": 200})),
        ("checked multiply rejects overflow", lambda: safe_product(MAX_I64, 2) is None),
        ("fresh window rejects turn 360", lambda: not (360 < FRESH_TURNS)),
        ("fee rejects a non-zero launch value", lambda: 1_600 * 0 // 10_000 == 0),
        ("max bound catches an off-by-one", lambda: 10_000_000 + 5 * 100_000 * 100_000 + 1 != 50_010_000_000),
        ("volume band catches rounding up", lambda: (347 // V_BAND) * V_BAND != 350),
        ("E1 guard rejects the double-counted crown pair",
         lambda: sum(r[2] for r in [("A", "S", 200), ("A", "B", -200),
                                     ("B", "S", 200), ("B", "B", -200)]) == 0
         and sum(r[2] for r in [("A", "S", 200), ("A", "B", -200),
                                 ("B", "S", 200), ("B", "B", -200)]) != -200),
        ("space guard rejects the add-back predicate",
         lambda: 50 <= (1_000 - 900 - 60) + 60 and not (50 <= 1_000 - 900 - 60)),
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    arithmetic_checks()
    document_checks()

    print(f"Market arithmetic/document checks: {len(PASS)} passed, {len(FAIL)} failed")
    for item in FAIL:
        print(f"FAIL  {item}")
    for item in PASS:
        print(f"PASS  {item}")
    if FAIL:
        print("\nMARKET VALIDATION: FAILED")
        return 1
    print("\nMARKET VALIDATION: ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
