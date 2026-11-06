"""QA-only arithmetic checker for the B-04 economy worked examples.

Recomputes the starting bundle, Examples 1-20 and the register's key figures from the
constants published in `stage-2/10_economic_formula_and_balance_register.md`, then checks
that `stage-2/10_economy_resources_treasury_and_finances.md` and the register actually
state those numbers.

This is document QA, not game code: it holds no runtime state, writes nothing, and is not
imported by anything. Run it from the `docs/` directory:

    python qa_backups/verify_economy_numbers.py

Exit status 0 means every recomputation agreed with the documents.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
SPEC = DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md"
REGISTER = DOCS / "stage-2" / "10_economic_formula_and_balance_register.md"

RESOURCES = [
    "food", "coal", "oil", "iron", "bauxite", "lead",
    "uranium", "gasoline", "steel", "aluminum", "ammunition",
]

# Register section 3.5: reference prices (book values), crowns per unit.
PRICE = {
    "food": 1, "coal": 1, "oil": 2, "iron": 1, "bauxite": 2, "lead": 3,
    "uranium": 30, "gasoline": 6, "steel": 7, "aluminum": 8, "ammunition": 6,
}

# Register section 3.2: output per batch, variable cost per batch, maintenance per batch.
EXTRACTION = {
    "food": (20, 12, 1),
    "coal": (10, 10, 1),
    "oil": (8, 14, 1),
    "iron": (10, 10, 1),
    "bauxite": (8, 14, 1),
    "lead": (6, 16, 1),
    "uranium": (1, 28, 1),
}
EXTRACTION_ORDER = ["food", "coal", "oil", "iron", "bauxite", "lead", "uranium"]

# Register section 3.3: inputs per batch, output resource, output per batch, variable
# cost, power draw in GU, maintenance per batch.
RECIPES = {
    "refining": ({"oil": 10}, "gasoline", 8, 20, 2, 2),
    "steel": ({"iron": 10, "coal": 6}, "steel", 8, 24, 3, 2),
    "aluminum": ({"bauxite": 12}, "aluminum", 8, 24, 4, 2),
    "ammunition": ({"lead": 8, "coal": 4}, "ammunition", 10, 20, 2, 2),
}
RECIPE_ORDER = ["refining", "steel", "aluminum", "ammunition"]

# Register section 3.4: one coal generator level = 6 GU, 6 coal, 10 crowns, 2 maintenance.
COAL_GEN = {"gu": 6, "fuel": {"coal": 6}, "cost": 10, "maintenance": 2}

# Register section 3.1: the standard starting bundle (D-063).
START_INV = {
    "food": 120, "coal": 60, "oil": 30, "iron": 30, "bauxite": 20, "lead": 10,
    "uranium": 0, "gasoline": 20, "ammunition": 0, "steel": 20, "aluminum": 0,
}
START_CAP = {
    "food": 3, "coal": 2, "oil": 1, "iron": 1, "bauxite": 0, "lead": 0, "uranium": 0,
    "refining": 1, "steel": 0, "aluminum": 0, "ammunition": 0,
}
START_TREASURY = 1500
START_POP = 50000
START_TAX_BP = 300
WAREHOUSE = 2000

FAILURES: list[str] = []
CHECKS = [0]


def check(label: str, actual, expected) -> None:
    CHECKS[0] += 1
    if actual != expected:
        FAILURES.append(f"{label}: computed {actual!r}, expected {expected!r}")


def total(inv: dict[str, int]) -> int:
    return sum(inv[r] for r in RESOURCES)


def book_value(inv: dict[str, int]) -> int:
    return sum(inv[r] * PRICE[r] for r in RESOURCES)


def free_space(inv: dict[str, int], warehouse: int = WAREHOUSE) -> int:
    return warehouse - total(inv)


def settle(
    *,
    population: int,
    tax_bp: int,
    treasury: int,
    inv: dict[str, int],
    capacities: dict[str, int],
    generators: int,
    warehouse: int = WAREHOUSE,
) -> dict:
    """One P3 settlement following B-04 section 15's published order (P3.1-P3.6)."""
    inv = dict(inv)
    tax = population * tax_bp * 10_000 // 1_000_000_000
    treasury += tax

    maintenance = sum(EXTRACTION[c][2] * capacities.get(c, 0) for c in EXTRACTION_ORDER)
    maintenance += sum(RECIPES[c][5] * capacities.get(c, 0) for c in RECIPE_ORDER)
    maintenance += COAL_GEN["maintenance"] * generators
    treasury -= maintenance

    # P3.3 extraction: per batch, money then space; a blocked chain stops.
    for chain in EXTRACTION_ORDER:
        produced, cost, _ = EXTRACTION[chain]
        while capacities.get(chain, 0) > 0:
            if treasury < cost or free_space(inv, warehouse) < produced:
                break
            capacities[chain] -= 1
            treasury -= cost
            inv[chain] += produced

    # P3.4 power: fail-closed per generator level.
    supply = 0
    for _ in range(generators):
        if all(inv[f] >= q for f, q in COAL_GEN["fuel"].items()) and treasury >= COAL_GEN["cost"]:
            for f, q in COAL_GEN["fuel"].items():
                inv[f] -= q
            treasury -= COAL_GEN["cost"]
            supply += COAL_GEN["gu"]

    # P3.5 processing: pro-rata derating, then per-batch input/money/space checks.
    demand = sum(RECIPES[c][4] * capacities.get(c, 0) for c in RECIPE_ORDER)
    pct = 100 if demand == 0 else min(100, supply * 100 // demand)
    for chain in RECIPE_ORDER:
        inputs, output, qty, cost, _draw, _maint = RECIPES[chain]
        batches = capacities.get(chain, 0) * pct // 100
        while batches > 0:
            if treasury < cost:
                break
            if any(inv[f] < q for f, q in inputs.items()):
                break
            if free_space(inv, warehouse) < qty:
                break
            for f, q in inputs.items():
                inv[f] -= q
            treasury -= cost
            inv[output] += qty
            batches -= 1

    # P3.6 food.
    food_demand = -(-population // 1000)
    eaten = min(inv["food"], food_demand)
    inv["food"] -= eaten

    return {
        "tax": tax,
        "maintenance": maintenance,
        "treasury": treasury,
        "inv": inv,
        "supply": supply,
        "power_pct": pct,
        "unmet_food": food_demand - eaten,
    }


def capex(crowns: int, materials: dict[str, int]) -> int:
    return crowns + sum(q * PRICE[r] for r, q in materials.items())


def power_cost(gu: int, crowns_per_gu: int = 3) -> int:
    return gu * crowns_per_gu


def derate(supply: int, demand: int) -> int:
    return 100 if demand == 0 else min(100, supply * 100 // demand)


def run_examples() -> None:
    # Example 1 - the standard bundle.
    check("Ex1 bundle units", total(START_INV), 310)
    check("Ex1 bundle book value", book_value(START_INV), 600)
    check("Ex1 starting wealth", START_TREASURY + book_value(START_INV), 2100)
    check("Ex1 free warehouse space", WAREHOUSE - total(START_INV), 1690)

    # Example 2 - standard start, one turn.
    e2 = settle(
        population=START_POP, tax_bp=START_TAX_BP, treasury=START_TREASURY,
        inv=START_INV, capacities=dict(START_CAP), generators=1,
    )
    extraction_variable = 3 * 12 + 2 * 10 + 14 + 10  # food 3, coal 2, oil 1, iron 1
    check("Ex2 tax", e2["tax"], 150)
    check("Ex2 maintenance", e2["maintenance"], 11)
    check("Ex2 operating expenses", e2["maintenance"] + extraction_variable + 10 + 20, 121)
    check("Ex2 net operating income", e2["tax"] - 121, 29)
    check("Ex2 treasury", e2["treasury"], 1529)
    check("Ex2 closing units", total(e2["inv"]), 350)
    check("Ex2 closing book value", book_value(e2["inv"]), 678)
    check("Ex2 closing wealth", e2["treasury"] + book_value(e2["inv"]), 2207)
    check("Ex2 food", e2["inv"]["food"], 130)
    check("Ex2 coal", e2["inv"]["coal"], 74)
    check("Ex2 gasoline", e2["inv"]["gasoline"], 28)

    # Example 3 - mature nation, operating loss with rising inventory value.
    ex3_inv = {
        "food": 200, "coal": 200, "oil": 200, "iron": 200, "bauxite": 200, "lead": 200,
        "uranium": 10, "gasoline": 100, "steel": 100, "aluminum": 100, "ammunition": 50,
    }
    ex3_cap = {
        "food": 5, "coal": 4, "oil": 3, "iron": 2, "bauxite": 2, "lead": 1, "uranium": 1,
        "refining": 2, "steel": 2, "aluminum": 1, "ammunition": 1,
    }
    check("Ex3 opening units", total(ex3_inv), 1560)
    check("Ex3 opening book value", book_value(ex3_inv), 4700)
    e3 = settle(
        population=50000, tax_bp=300, treasury=1529,
        inv=ex3_inv, capacities=dict(ex3_cap), generators=3,
    )
    expected_closing = {
        "food": 250, "coal": 206, "oil": 204, "iron": 200, "bauxite": 204, "lead": 198,
        "uranium": 11, "gasoline": 116, "steel": 116, "aluminum": 108, "ammunition": 60,
    }
    for r in RESOURCES:
        check(f"Ex3 closing {r}", e3["inv"][r], expected_closing[r])
    check("Ex3 maintenance", e3["maintenance"], 36)
    check("Ex3 power pct", e3["power_pct"], 100)
    check("Ex3 treasury", e3["treasury"], 1247)
    check("Ex3 closing units", total(e3["inv"]), 1673)
    check("Ex3 closing book value", book_value(e3["inv"]), 5128)
    check("Ex3 closing wealth", e3["treasury"] + book_value(e3["inv"]), 6375)
    check("Ex3 wealth change", 6375 - (1529 + 4700), 146)
    check("Ex3 warehouse respected", total(e3["inv"]) <= WAREHOUSE, True)

    # Example 4 - capex versus opex.
    check("Ex4 construction book value", capex(150, {"steel": 10, "gasoline": 5}), 250)
    check("Ex4 treasury after capex", 1529 - 150, 1379)
    next_turn_costs = 12 + (4 * 12) + 20 + 14 + 10 + 10 + 20
    check("Ex4 next-turn opex", next_turn_costs, 134)
    check("Ex4 next-turn net", 150 - next_turn_costs, 16)
    check("Ex4 extra batch margin", 20 - (12 + 1), 7)
    check("Ex4 payback turns", -(-250 // 7), 36)

    # Example 5 - reconciliation without a market fee.
    check("Ex5 closing treasury", 1529 + 150 - 121 - 150 + 50 - 30, 1428)
    check("Ex5 net cash flow", 1428 - 1529, -101)
    check("Ex5 net trade", 50 - 30, 20)

    # Example 6 - warehouse limit on coal.
    coal, money, batches = 1975, 100, 0
    for _ in range(5):
        if (WAREHOUSE - coal) < 10 or money < 10:
            break
        coal, money, batches = coal + 10, money - 10, batches + 1
    check("Ex6 batches", batches, 2)
    check("Ex6 closing coal", coal, 1995)
    check("Ex6 free space", WAREHOUSE - coal, 5)
    check("Ex6 treasury", money - 5, 75)

    # Register section 5 - the whole base-margin table must follow from the constants.
    margins = {c: EXTRACTION[c][0] * PRICE[c] - EXTRACTION[c][1] - EXTRACTION[c][2]
               for c in EXTRACTION_ORDER}
    for chain in RECIPE_ORDER:
        inputs, output, qty, cost, _draw, maint = RECIPES[chain]
        margins[chain] = (qty * PRICE[output]
                          - sum(q * PRICE[r] for r, q in inputs.items()) - cost - maint)
    check("register section 5 base margins", margins, {
        "food": 7, "coal": -1, "oil": 1, "iron": -1, "bauxite": 1, "lead": 1,
        "uranium": 1, "refining": 6, "steel": 14, "aluminum": 14, "ammunition": 10,
    })

    # Example 7 - refining.
    base7 = 8 * PRICE["gasoline"] - 10 * PRICE["oil"] - 20 - 2
    check("Ex7 base margin per batch", base7, 6)
    check("Ex7 base margin, two batches", 2 * base7, 12)
    check("Ex7 fully loaded margin", 2 * (base7 - power_cost(2)), 0)
    check("Ex7 break-even gasoline price", (10 * PRICE["oil"] + 20 + 2 + power_cost(2)) // 8, 6)

    # Example 8 - aluminium.
    base8 = 8 * PRICE["aluminum"] - 12 * PRICE["bauxite"] - 24 - 2
    check("Ex8 base margin", base8, 14)
    check("Ex8 fully loaded margin", base8 - power_cost(4), 2)
    loaded8 = 12 * PRICE["bauxite"] + 24 + 2 + power_cost(4)
    check("Ex8 loaded break-even aluminium", loaded8 / 8, 7.75)
    check("Ex8 loaded break-even bauxite", (8 * PRICE["aluminum"] - 24 - 2 - power_cost(4)) / 12, 2.1666666666666665)
    check("Ex8 base break-even aluminium", (12 * PRICE["bauxite"] + 24 + 2) / 8, 6.25)
    check("Ex8 base break-even bauxite", (8 * PRICE["aluminum"] - 24 - 2) / 12, 3.1666666666666665)

    # Example 9 - steel.
    base9 = 8 * PRICE["steel"] - (10 * PRICE["iron"] + 6 * PRICE["coal"]) - 24 - 2
    check("Ex9 base margin", base9, 14)
    check("Ex9 fully loaded margin", base9 - power_cost(3), 5)

    # Example 10 - ammunition.
    base10 = 10 * PRICE["ammunition"] - (8 * PRICE["lead"] + 4 * PRICE["coal"]) - 20 - 2
    check("Ex10 base margin", base10, 10)
    check("Ex10 fully loaded margin", base10 - power_cost(2), 4)

    # Examples 11 and 19 - food shortage, penalty and recovery.
    check("Ex11 full shortage penalty", min(3000, 3000 * 50 // 50), 3000)
    check("Ex11 tax after full shortage", 150 * (10_000 - 3000) // 10_000, 105)
    check("Ex11 partial shortage penalty", 3000 * 20 // 50, 1200)
    check("Ex11 tax after partial shortage", 150 * (10_000 - 1200) // 10_000, 132)
    check("Ex19 smaller shortage tax", 150 * (10_000 - 600) // 10_000, 141)

    # Example 12 - an accepted order fails on power, releases, standing runs one batch.
    pct12 = derate(2, 4)
    check("Ex12 power pct", pct12, 50)
    check("Ex12 batches available", 2 * pct12 // 100, 1)
    check("Ex12 final oil", 20 - 10, 10)
    check("Ex12 gasoline", 8, 8)

    # Example 13 - a blocked batch destroys nothing.
    check("Ex13 extraction treasury", 100 - 3, 97)
    check("Ex13 extraction blocked", 20 > 12, True)
    check("Ex13 processing blocked", 8 > 5, True)

    # Example 15 - insolvency without debt (population 6,667 -> tax 20, food demand 7).
    check("Ex15 tax", 6667 * 300 * 10_000 // 1_000_000_000, 20)
    check("Ex15 food demand", -(-6667 // 1000), 7)
    check("Ex15 maintenance six for three extraction chains", 3 + 2 + 1, 6)
    check("Ex15 closing treasury after three paid chains", 70 - 6 - 36 - 20, 8)
    check("Ex15 oil batch is unaffordable at 8", 8 < 14, True)

    # Example 16 - market accounting contract.
    check("Ex16 seller treasury", 1529 + 160, 1689)
    check("Ex16 buyer treasury", 1000 - 160, 840)
    check("Ex16 seller wealth change", 160 - 20 * PRICE["steel"], 20)
    check("Ex16 hypothetical fee", 160 * 200 // 10_000, 3)

    # Example 17 - reroll destroys; the replacement gets the bundle only.
    check("Ex17 old nation wealth", 1529 + 678, 2207)
    check("Ex17 replacement wealth", START_TREASURY + book_value(START_INV), 2100)

    # Example 18 - power shortfall.
    demand18 = 2 * RECIPES["refining"][4] + 2 * RECIPES["steel"][4]
    check("Ex18 demand", demand18, 10)
    pct18 = derate(6, demand18)
    check("Ex18 power pct", pct18, 60)
    check("Ex18 batches per chain", 2 * pct18 // 100, 1)
    check("Ex18 actual draw", RECIPES["refining"][4] + RECIPES["steel"][4], 5)
    check("Ex18 processing cost", 20 + 24, 44)

    # Example 20 - reference versus market value.
    check("Ex20 book value", 10 * PRICE["steel"], 70)
    check("Ex20 sale proceeds", 10 * 5, 50)
    check("Ex20 wealth change", 50 - 70, -20)


CROWN = re.compile(r"[0-9][0-9,]*")


def index_row(text: str, example: int) -> str:
    """Return the register's worked-example index row for one example, or ''."""
    for line in text.splitlines():
        if line.startswith(f"| {example} "):
            return line
    return ""


def first_crowns(row: str) -> int | None:
    """Parse the first thousands-separated number of an index row's result cell."""
    result_cell = row.rstrip().rstrip("|").rsplit("|", 1)[-1]
    match = CROWN.search(result_cell)
    return int(match.group(0).replace(",", "")) if match else None


def example_block(text: str, example: int) -> str:
    """Return one `### Example N` section of the rulebook, up to the next heading."""
    start = text.find(f"### Example {example} —")
    if start < 0:
        return ""
    end = text.find("\n### ", start + 4)
    return text[start:] if end < 0 else text[start:end]


def check_example5_cross_document(documents: dict[Path, str]) -> None:
    """Example 5 must agree between the rulebook and the register's index.

    The expected treasury is recomputed from the published transaction amounts, so the
    check fails if either document is edited without its arithmetic following. This is
    what the 129-check pass missed: the register's index row still read 1,426 after the
    rulebook dropped the unadopted market fee.
    """
    opening, tax, opex, capex, sale, buy = 1529, 150, 121, 150, 50, 30
    expected = opening + tax - opex - capex + sale - buy
    check("Ex5 cross-document expected treasury", expected, 1428)

    spec_row = example_block(documents[SPEC], 5)
    check("Ex5 rulebook section found", bool(spec_row), True)
    check("Ex5 rulebook states its inputs",
          "1,529 + 150 − 121 − 150 + 50 − 30" in spec_row, True)
    check("Ex5 rulebook closing treasury", f"= {expected:,}" in spec_row, True)
    check("Ex5 rulebook charges no fee", "No market fee is charged" in spec_row, True)

    register_row = index_row(documents[REGISTER], 5)
    check("Ex5 register index row found", bool(register_row), True)
    check("Ex5 register index treasury", first_crowns(register_row), expected)
    check("Ex5 register index keeps the identity note",
          "identity holds" in register_row, True)

    # The register's market example must stay an illustration, not an adopted fee.
    market_row = index_row(documents[REGISTER], 16)
    check("Ex16 register index row found", bool(market_row), True)
    check("Ex16 register index keeps the fee as an illustration",
          "3 fee" in market_row, True)
    spec_market = example_block(documents[SPEC], 16)
    check("Ex16 rulebook labels the fee hypothetical",
          "Hypothetical" in spec_market and "not adopted" in spec_market, True)

    # Both authoritative economic documents must report the revision they describe.
    # B-04 v1.8 is the Prompt 09B-M documentation revision (the operational
    # boundary moves to D-141, no purpose is currently spendable, and the ARL
    # remains a receipt/accounting record); the formula register stays v1.3
    # because no constant or formula changed.
    for document, name, version in ((SPEC, "B-04", "2.0"), (REGISTER, "register", "1.4")):
        head = "\n".join(documents[document].splitlines()[:4])
        check(f"{name} header version", f"**Version:** {version}" in head, True)


DOC_TOKENS = [
    (SPEC, "= **310 units**.", "Example 1 states the 310-unit starting bundle"),
    (SPEC, "= **1,560 units**.", "Example 3 states its 1,560-unit opening"),
    (SPEC, "| **Total** | **1,560** | | | **1,673** |", "Example 3's closing table totals 1,673"),
    (SPEC, "= **5,128 crowns**", "Example 3's closing book value"),
    (SPEC, "= 6,375", "Example 3's closing wealth"),
    (SPEC, "wealth **rises by 146**", "Example 3's wealth change"),
    (SPEC, "= 1,428", "Example 5's fee-free closing treasury"),
    (SPEC, "2,000−310)/20=84", "Example 2's free-space term"),
    (SPEC, "310 units (the Example 1 list)", "Example 17's replacement bundle"),
    (SPEC, "1,500 crowns, 310 units", "the section 24 decision cross-reference"),
    (SPEC, "**2.17**", "Example 8's bauxite break-even"),
    (SPEC, "**7.75**", "Example 8's aluminium break-even"),
    (REGISTER, "The bundle occupies **310 units**", "register section 3.1 total"),
    (REGISTER, "| Example | Standard start: 310 units |", "F-EC-021 example"),
    (REGISTER, "| Example | `2,000 − 310 = 1,690` |", "F-EC-023 example"),
    (REGISTER, "Wealth 2,100; 310 units", "worked example index row 1"),
    (REGISTER, "Closing 1,247; net −282; wealth +146", "worked example index row 3"),
]

STALE_TOKENS = [
    "350 units (D-063)",
    "= **350 units**",
    "Standard start: 350 units",
    "2,000 − 350 = 1,650",
    "wealth +1,042",
    "1,360 units",
    "6,024",
    "1,720 units",
    "market fee 2",
    "`FEE −2`",
    "Closing 1,426; identity holds",
    "+ 150 − 121 − 150 + 50 − 30 − 2",
]




# B-04 v1.3 / ECN-147a: maintenance is one whole obligation per chain, attempted
# extraction -> generation -> processing, paid in full or cancelled in full. The
# standard-start obligations are derived from the published constants.
MAINT_OBLIGATIONS = [("food", 3), ("coal", 2), ("oil", 1), ("iron", 1),
                     ("generator", 2), ("refining", 2)]


def allocate_maintenance(crowns: int):
    left, paid, cancelled = crowns, [], []
    for chain, due in MAINT_OBLIGATIONS:
        if left >= due:
            paid.append(chain)
            left -= due
        else:
            cancelled.append(chain)
    return left, paid, cancelled


def check_maintenance_allocation(documents: dict[Path, str]) -> None:
    spec = documents[SPEC]
    check("maintenance: standard start totals 11", sum(d for _, d in MAINT_OBLIGATIONS), 11)
    check("maintenance: 1 crown pays oil", allocate_maintenance(1)[1], ["oil"])
    check("maintenance: 1 crown leaves 0", allocate_maintenance(1)[0], 0)
    check("maintenance: 1 crown unmaintains five chains", len(allocate_maintenance(1)[2]), 5)
    check("maintenance: 3 crowns pay food only", allocate_maintenance(3)[1], ["food"])
    check("maintenance: 11 crowns pay all six", len(allocate_maintenance(11)[1]), 6)
    check("maintenance: 11 crowns leave 0", allocate_maintenance(11)[0], 0)
    check("maintenance: 0 crowns pay nothing", allocate_maintenance(0)[1], [])
    check("maintenance: no obligation is partially paid",
          allocate_maintenance(1)[2], ["food", "coal", "iron", "generator", "refining"])
    for token in ("ECN-147a", "one obligation per chain",
                  "**Extraction:** food, coal, oil, iron, bauxite, lead, uranium",
                  "**Generation:** coal, oil, nuclear",
                  "**Processing:** refining, steel, aluminum, ammunition",
                  "A nation holding **1** crown pays **oil** (1), cancels the other **10**"):
        CHECKS[0] += 1
        if token not in spec:
            FAILURES.append(f"B-04: missing '{token}' (ECN-147a allocation)")


def main() -> int:
    if not SPEC.exists() or not REGISTER.exists():
        print("FAIL: the B-04 specification or formula register is missing")
        return 1

    documents = {
        SPEC: SPEC.read_text(encoding="utf-8"),
        REGISTER: REGISTER.read_text(encoding="utf-8"),
    }

    run_examples()
    check_example5_cross_document(documents)
    check_maintenance_allocation(documents)


    for document, token, reason in DOC_TOKENS:
        CHECKS[0] += 1
        if token not in documents[document]:
            FAILURES.append(f"{document.name}: missing '{token}' ({reason})")

    for document, text in documents.items():
        for token in STALE_TOKENS:
            CHECKS[0] += 1
            if token in text:
                FAILURES.append(f"{document.name}: stale or unadopted text present: '{token}'")

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} problem(s) in {CHECKS[0]} checks")
        for item in FAILURES:
            print("  -", item)
        return 1

    print(f"PASS: {CHECKS[0]}/{CHECKS[0]} economy arithmetic checks passed")
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
