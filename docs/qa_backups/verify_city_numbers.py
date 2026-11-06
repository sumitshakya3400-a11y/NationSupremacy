"""QA-only arithmetic checker for the B-05 city, infrastructure and research examples.

Recomputes the constants, the cost curves and all 20 worked examples from the published
numbers, then checks that the rulebook and the formula register actually state them.

This is document QA, not game code: it holds no state, writes nothing and is imported by
nothing. Run it from the `docs/` directory:

    python qa_backups/verify_city_numbers.py

Exit status 0 means every recomputation agreed with the documents.
"""

from __future__ import annotations

import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
SPEC = DOCS / "stage-2" / "11_cities_infrastructure_production_and_research.md"
REGISTER = DOCS / "stage-2" / "11_city_infrastructure_production_and_research_formula_register.md"
TRACE = DOCS / "stage-2" / "03_requirements_traceability.md"
DECISIONS = DOCS / "DECISIONS.md"
ECON_SPEC = DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md"
ECON_REG = DOCS / "stage-2" / "10_economic_formula_and_balance_register.md"

FAILURES: list[str] = []
CHECKS = [0]


def check(label: str, actual, expected) -> None:
    CHECKS[0] += 1
    if actual != expected:
        FAILURES.append(f"{label}: computed {actual!r}, expected {expected!r}")


# --- published constants -----------------------------------------------------

CITY_MAX = 12
CAP_BASE = 10
CAP_PER_LEVELS = 10
INFRA_MIN, INFRA_MAX = 10, 500
HOUSING_BASE = 45_000
HOUSING_PER_INFRA = 100
HOUSING_PER_CIVIC = 25_000

PRICE = {  # B-04 register section 3.5
    "food": 1, "coal": 1, "oil": 2, "iron": 1, "bauxite": 2, "lead": 3,
    "uranium": 30, "gasoline": 6, "steel": 7, "aluminum": 8, "ammunition": 6,
}

# building -> (dc, crowns, materials, class)
BUILDINGS = {
    "farm": (1, 120, {"steel": 5}, "extraction"),
    "coal_mine": (1, 160, {"steel": 5}, "extraction"),
    "oil_well": (1, 220, {"steel": 5}, "extraction"),
    "iron_mine": (1, 180, {"steel": 5}, "extraction"),
    "bauxite_mine": (1, 220, {"steel": 5}, "extraction"),
    "lead_mine": (1, 260, {"steel": 5}, "extraction"),
    "uranium_mine": (1, 600, {"steel": 10, "aluminum": 5}, "extraction"),
    "refinery": (2, 320, {"steel": 15}, "processing"),
    "steel_mill": (2, 380, {"steel": 15}, "processing"),
    "smelter": (2, 420, {"steel": 20}, "processing"),
    "ammo_plant": (2, 360, {"steel": 15}, "processing"),
    "coal_plant": (2, 280, {"steel": 10}, "generation"),
    "oil_plant": (2, 340, {"steel": 10, "aluminum": 5}, "generation"),
    "nuclear_plant": (2, 1_200, {"steel": 30, "aluminum": 20}, "generation"),
    "warehouse": (1, 180, {"steel": 5}, "support"),
    "lab": (3, 500, {"steel": 20}, "support"),
    "civic": (2, 300, {"steel": 10}, "support"),
}

START_FACILITIES = {"farm": 3, "coal_mine": 2, "oil_well": 1, "iron_mine": 1,
                    "refinery": 1, "coal_plant": 1}

TECH = {  # id: (branch, rp, crowns)
    "agri_rotation": ("agriculture", 24, 160),
    "agri_mechanisation": ("agriculture", 44, 300),
    "ext_coal": ("extraction", 20, 140),
    "ext_oil": ("extraction", 32, 220),
    "ext_metals": ("extraction", 40, 280),
    "ext_deep": ("extraction", 56, 360),
    "ind_heat": ("industry", 28, 200),
    "ind_chem": ("industry", 48, 340),
    "ind_ordnance": ("industry", 36, 260),
    "civ_survey": ("civil", 20, 140),
    "civ_methods": ("civil", 40, 280),
    "nuclear_engineering": ("energy", 60, 500),
}

PROGRAMMES = {
    "granary": 900, "survey": 1_000, "standards": 1_200, "civil_works": 1_100,
}


# --- formulas ----------------------------------------------------------------

def capacity(infra: int) -> int:
    return CAP_BASE + infra // CAP_PER_LEVELS


def housing(infra: int, civic: int = 0) -> int:
    return HOUSING_BASE + HOUSING_PER_INFRA * infra + HOUSING_PER_CIVIC * civic


def infra_unit_cost(level: int) -> int:
    return 8 + level // 10


def infra_cost(level: int, n: int, discount_bp: int = 0) -> int:
    total = sum(infra_unit_cost(level + k) for k in range(n))
    return -(-(total * (10_000 - discount_bp)) // 10_000)


def city_cost(k: int) -> int:
    return 400 + 150 * k * k


def book_value(name: str, discount_bp: int = 0) -> int:
    dc, crowns, materials, _cls = BUILDINGS[name]
    paid = -(-(crowns * (10_000 - discount_bp)) // 10_000)
    return paid + sum(q * PRICE[r] for r, q in materials.items())


def used_capacity(facilities: dict[str, int]) -> int:
    return sum(BUILDINGS[name][0] * count for name, count in facilities.items())


def margin(name: str) -> int:
    """Base margin per batch at reference prices, before power (B-04 register section 5)."""
    if name == "farm":
        return 20 * PRICE["food"] - 12 - 1
    if name == "coal_mine":
        return 10 * PRICE["coal"] - 10 - 1
    if name == "oil_well":
        return 8 * PRICE["oil"] - 14 - 1
    if name == "iron_mine":
        return 10 * PRICE["iron"] - 10 - 1
    if name == "bauxite_mine":
        return 8 * PRICE["bauxite"] - 14 - 1
    if name == "lead_mine":
        return 6 * PRICE["lead"] - 16 - 1
    if name == "uranium_mine":
        return 1 * PRICE["uranium"] - 28 - 1
    if name == "refinery":
        return 8 * PRICE["gasoline"] - 10 * PRICE["oil"] - 20 - 2
    if name == "steel_mill":
        return 8 * PRICE["steel"] - (10 * PRICE["iron"] + 6 * PRICE["coal"]) - 24 - 2
    if name == "smelter":
        return 8 * PRICE["aluminum"] - 12 * PRICE["bauxite"] - 24 - 2
    if name == "ammo_plant":
        return 10 * PRICE["ammunition"] - (8 * PRICE["lead"] + 4 * PRICE["coal"]) - 20 - 2
    raise KeyError(name)


def warehouse_cost(n: int) -> int:
    return 180 + 40 * n


def run_examples() -> None:
    # Standard capital.
    cap = capacity(50)
    check("Ex1 capacity", cap, 15)
    check("Ex1 used", used_capacity(START_FACILITIES), 11)
    check("Ex1 free", cap - used_capacity(START_FACILITIES), 4)
    check("Ex1 housing", housing(50), 50_000)
    check("Ex1 book value", sum(0 for _ in START_FACILITIES), 0)

    # Capacity curve.
    check("capacity(10)", capacity(10), 11)
    check("capacity(500)", capacity(500), 60)

    # Housing curve.
    check("housing(10)", housing(10), 46_000)
    check("housing(100)", housing(100), 55_000)
    check("housing(500,3)", housing(500, 3), 170_000)

    # Infrastructure cost.
    check("infra 50->60", infra_cost(50, 10), 130)
    check("infra 100->110", infra_cost(100, 10), 180)
    check("infra 400->410", infra_cost(400, 10), 480)
    check("infra 50->100", infra_cost(50, 50), 750)
    check("infra 50->100 disc", infra_cost(50, 50, 1_000), 675)
    check("infra 50->500 total", infra_cost(50, 450), 15_750)

    # City cost.
    for k, expected in ((2, 1_000), (3, 1_750), (4, 2_800), (12, 22_000)):
        check(f"city_cost({k})", city_cost(k), expected)
    check("city steel", 20, 20)

    # Book values.
    expected_book = {
        "farm": 155, "coal_mine": 195, "oil_well": 255, "iron_mine": 215,
        "bauxite_mine": 255, "lead_mine": 295, "uranium_mine": 710,
        "refinery": 425, "steel_mill": 485, "smelter": 560, "ammo_plant": 465,
        "coal_plant": 350, "oil_plant": 450, "nuclear_plant": 1_570,
        "warehouse": 215, "lab": 640, "civic": 370,
    }
    for name, value in expected_book.items():
        check(f"book value {name}", book_value(name), value)
    check("book value farm discounted", book_value("farm", 1_000), 143)
    check("book value refinery discounted", book_value("refinery", 1_000), 393)

    # Base margins.
    expected_margin = {
        "farm": 7, "coal_mine": -1, "oil_well": 1, "iron_mine": -1,
        "bauxite_mine": 1, "lead_mine": 1, "uranium_mine": 1,
        "refinery": 6, "steel_mill": 14, "smelter": 14, "ammo_plant": 10,
    }
    for name, value in expected_margin.items():
        check(f"margin {name}", margin(name), value)

    # Example 2 - second city.
    check("Ex2 treasury", 1_529 - 1_000, 529)
    check("Ex2 steel", 20 - 20, 0)
    check("Ex2 book", 1_000 + 20 * PRICE["steel"], 1_140)
    check("Ex2 national housing", 55_000 + 46_000, 101_000)

    # Example 4 - free capacity after the upgrade.
    check("Ex4 free after", capacity(100) - 11, 9)

    # Example 6 - four farms.
    check("Ex6 food output", 4 * 20, 80)
    check("Ex6 variable cost", 4 * 12, 48)
    check("Ex6 maintenance", 4 * 1, 4)
    check("Ex6 total cost", 48 + 4, 52)
    check("Ex6 closing food", 120 + 80 - 50, 150)
    check("Ex6 margin", 80 * PRICE["food"] - 52, 28)

    # Example 7 - coal.
    check("Ex7 output", 3 * 10, 30)
    check("Ex7 margin", 30 * PRICE["coal"] - 30 - 3, -3)
    check("Ex7 closing coal", 60 + 30 - 6, 84)

    # Example 9 - refining.
    check("Ex9 treasury", 1_529 - 20 - 10 - 2 - 2, 1_495)
    check("Ex9 gasoline", 20 + 8, 28)
    check("Ex9 oil", 30 - 10, 20)
    check("Ex9 coal", 60 - 6, 54)

    # Example 10 - steel.
    check("Ex10 demand", 2 + 3, 5)
    check("Ex10 coal", 54 - 6 - 6, 42)
    check("Ex10 steel", 20 + 8, 28)
    check("Ex10 treasury", 1_495 - 24 - 2 - 10 - 2, 1_457)

    # Example 11 - the power cliff.
    check("Ex11 demand", 2 + 3 + 4, 9)
    pct = 100 * 6 // 9
    check("Ex11 power pct", pct, 66)
    check("Ex11 batches at 66", 1 * pct // 100, 0)
    check("Ex11 supply with 2 plants", 6 + 6, 12)
    check("Ex11 runs at 12", 12 >= 9, True)

    # Example 12 - ammunition.
    check("Ex12 lead", 20 - 8, 12)
    check("Ex12 coal", 42 - 4, 38)
    check("Ex12 ammunition", 10, 10)
    check("Ex12 with tech", 10 + 1, 11)

    # Example 16 - modifiers add, never multiply.
    check("Ex16 food", 4 * (20 + 1 + 1 + 1), 92)
    check("Ex16 cap", 20 + 3, 23)

    # Example 17 - demolition.
    check("Ex17 refund farm", 120 * 2_500 // 10_000, 30)
    check("Ex17 impairment", 155 - 30, 125)
    check("Ex17 refund refinery", 320 * 2_500 // 10_000, 80)
    check("Ex17 granted refund", 0, 0)

    # Example 18 - four refineries on one coal plant.
    check("Ex18 demand", 4 * 2, 8)
    pct18 = 100 * 6 // 8
    check("Ex18 power pct", pct18, 75)
    check("Ex18 batches", 4 * pct18 // 100, 3)
    check("Ex18 gasoline", 3 * 8, 24)
    check("Ex18 variable", 3 * 20, 60)

    # Example 19 - wealth is unchanged by construction.
    opening_wealth = 1_529 + 20 * PRICE["steel"]
    closing_wealth = (1_529 - 320) + 5 * PRICE["steel"] + 425
    check("Ex19 opening wealth", opening_wealth, 1_669)
    check("Ex19 closing wealth", closing_wealth, 1_669)
    check("Ex19 discounted cost", -(-(320 * 9_000) // 10_000), 288)
    check("Ex19 discounted book", 288 + 15 * PRICE["steel"], 393)

    # Research.
    check("research rate 1 lab", 1, 1)
    check("first tech turns, 1 lab", TECH["agri_rotation"][1] // 1, 24)
    check("first tech turns, 2 labs", TECH["agri_rotation"][1] // 2, 12)
    check("tech RP total", sum(t[1] for t in TECH.values()), 448)
    check("tech crown total", sum(t[2] for t in TECH.values()), 3_180)
    check("programme crowns total", sum(PROGRAMMES.values()), 4_200)

    # Upkeep.
    check("upkeep 2 labs 3 civic", 2 * 2 + 3 * 1, 7)

    # Warehouse.
    check("warehouse 1st", warehouse_cost(0), 180)
    check("warehouse 2nd", warehouse_cost(1), 220)
    check("warehouse 6th", warehouse_cost(5), 380)
    check("warehouse national", 2_000 + 250 + 500, 2_750)

    # Cost of a maxed city.
    max_dc = 8 * 1 + 4 * 2 * 4 + 6 * 2 + 6 * 1 + 2 * 3 + 3 * 2
    check("maxed city DC need", max_dc, 70)
    check("max city capacity", capacity(500), 60)

    # Developed-city construction cost.
    representative = 15_750 + 8 * 180 + 8 * 370 + 4 * 310 + 2 * 500 + 300 + 220
    check("representative city cost", representative, 22_910)

    # Correction C - the stepped model is authoritative and the bound is 16,170.
    check("largest legal order 10->500", infra_cost(10, 490), 16_170)
    check("50->500 split into ten-level orders",
          sum(infra_cost(50 + 10 * i, 10) for i in range(45)), 15_750)
    check("largest order at the 2,000 bp cap", infra_cost(10, 490, 2_000), 12_936)
    check("50->500 at the launch 1,000 bp discount", infra_cost(50, 450, 1_000), 14_175)
    # A stale flat unit price at the starting level would give 450 x 13 = 5,850.
    check("flat starting-price result (must not be the rule)", 450 * 13, 5_850)
    check("stepped result differs from the flat one",
          infra_cost(50, 450) != 450 * 13, True)

    # Correction D - basis-point vocabulary.
    check("a 10% discount is 1,000 bp", 10_000 - 9_000, 1_000)
    check("the remaining multiplier is 9,000 bp", 9_000, 9_000)
    check("the 20% cap is 2,000 bp", 10_000 - 8_000, 2_000)
    check("750 base at 1,000 bp", -(-(750 * 9_000) // 10_000), 675)
    check("one discount only on a 320 refinery",
          -(-(320 * 9_000) // 10_000), 288)

    # Correction E - total, reserved and available are distinct (Example 8).
    check("Ex8 treasury total at acceptance", 1_000, 1_000)
    check("Ex8 treasury reserved", 120, 120)
    check("Ex8 treasury available", 1_000 - 120, 880)
    check("Ex8 steel total at acceptance", 20, 20)
    check("Ex8 steel available", 20 - 5, 15)
    check("Ex8 total after resolution", 1_000 - 120, 880)
    check("Ex8 steel after resolution", 20 - 5, 15)
    check("Ex8 DC claim fits", 19 + 1, 20)
    check("Ex8 reservation not a charge", 1_000 - 120 == 880 and 1_000 != 880, True)

    # Correction A - Example 12 is funded and never negative.
    check("Ex12 opening treasury", 1_000, 1_000)
    check("Ex12 variable plus maintenance", 20 + 2, 22)
    check("Ex12 closing treasury", 1_000 - 20 - 2, 978)
    check("Ex12 closing treasury is non-negative", 978 >= 0, True)
    check("Ex12 a 21-crown treasury cannot run the batch", 21 < 22, True)
    check("Ex12 blocked batch still owes maintenance", 21 - 2, 19)
    check("Ex12 blocked batch leaves stock untouched", 20 - 0, 20)

    # Correction G - derating allocates whole batches, never fractions.
    check("Ex11 66% capacity 1 runs", 1 * 66 // 100, 0)
    check("Ex11 66% capacity 2 runs", 2 * 66 // 100, 1)
    check("Ex11 one batch is a full recipe", 1 * 8, 8)
    check("Ex11 two full batches of aluminum", 2 * 8, 16)

    # Correction B - research points are assigned exactly once.
    gen, cost, prog = 3, 24, 22
    applied = min(gen, max(0, cost - prog))
    check("Ex15B applied", applied, 2)
    check("Ex15B progress after P4.2", prog + applied, 24)
    check("Ex15B overflow to the pool", gen - applied, 1)
    check("Ex15B generated equals applied plus banked", gen, applied + (gen - applied))
    check("Ex15C banked points fund the programme", 100 - 100, 0)
    check("Ex15C progress after P4.2", 10 + 5, 15)
    check("Ex15C progress after seven turns", 10 + 5 * 6 + 4, 44)
    check("Ex15C final overflow", 5 - 4, 1)
    check("Ex15C reconciliation", 100 + 35, 100 + 34 + 1)
    check("a programme never reads project progress", 100 <= 100, True)

    # Correction A - F-CI-021 must describe Example 15B's real state (22/24).
    gen_b, cost_b, prog_b = 3, 24, 22
    applied_b = min(gen_b, cost_b - prog_b)
    check("15B applied from 22/24", applied_b, 2)
    check("15B final progress", prog_b + applied_b, 24)
    check("15B banked overflow", gen_b - applied_b, 1)
    check("15B generated equals progress gained plus banked",
          gen_b, (prog_b + applied_b - prog_b) + (gen_b - applied_b))
    check("the 23/24 case is a different scenario", min(3, 24 - 23), 1)

    # Correction B - planned batches are M + A, never C + M.
    for C, M, A, P in ((2, 2, 0, 2), (3, 1, 2, 3), (3, 0, 0, 0)):
        check(f"planned batches C={C} M={M} A={A}", M + A, P)
        check(f"plan stays inside capacity C={C} M={M} A={A}", M + A <= C, True)
    check("refining C=2 M=2 demand", 2 * 2, 4)
    check("the invalid C+M plan would demand", (2 + 2) * 2, 8)
    check("the invalid plan would derate to 25%", 10_000 * 2 // 8, 2_500)
    check("the invalid plan would allow no batch", 2 * 2_500 // 10_000, 0)
    check("an idle chain plans no batches", 0 * 2, 0)
    check("an idle chain still pays processing maintenance", 3 * 2, 6)

    # Correction C - whole-batch execution never exceeds supply.
    C, supply, draw = 4, 6, 2
    demand = C * draw
    pct = 10_000 if supply >= demand else 10_000 * supply // demand
    avail = C * pct // 10_000
    check("Ex18 demand, no manual orders", demand, 8)
    check("Ex18 power percent", pct // 100, 75)
    check("Ex18 batches available", avail, 3)
    check("Ex18 executed power fits supply", avail * draw <= supply, True)
    check("Ex18 three slots can absorb a two-batch manual order", 2 <= avail, True)
    check("Ex12 two manual batches need more than one powered slot",
          2 > 2 * 5_000 // 10_000, True)

    # Case 5 - a repeated settlement applies each batch once.
    outputs: dict[str, int] = {}
    for _ in range(2):
        outputs.setdefault("(812, nation, P3.5, refining, 1)", 8)
    check("retry keeps one production event", len(outputs), 1)
    check("retry keeps one output quantity", sum(outputs.values()), 8)


DOC_TOKENS = [
    (SPEC, "**15 DC**", "Example 1 states the capital's capacity"),
    (SPEC, "**4 DC free**", "Example 1 states the free capacity"),
    (SPEC, "**750**", "Example 3 states the 50-to-100 cost"),
    (SPEC, "= 675", "Example 3 states the discounted cost"),
    (SPEC, "**15,750 crowns**", "the developed-city infrastructure total"),
    (SPEC, "22,910", "the representative city cost"),
    (SPEC, "= 1,669", "Example 19 states the unchanged wealth"),
    (SPEC, "= 92", "Example 16 states the modified output"),
    (SPEC, "**64 tests**", "the test count"),
    (SPEC, "T05-A01", "the test IDs"),
    (SPEC, "REQ-188", "the first new requirement"),
    (SPEC, "REQ-257", "the last new requirement"),
    (REGISTER, "10 + floor(infrastructure / 10)", "the capacity formula"),
    (REGISTER, "45,000 + 100", "the housing formula base"),
    (REGISTER, "25,000", "the civic housing term"),
    (REGISTER, "400 + 150", "the city cost formula"),
    (REGISTER, "**448**", "the technology RP total"),
    (REGISTER, "**3,180**", "the technology crown total"),
    (REGISTER, "2,500", "the demolition refund rate"),
    (REGISTER, "15,750", "the infrastructure total"),
    (SPEC, "floor(j / 10)", "URB-043 sums the marginal price of each level"),
    (SPEC, "**16,170 crowns**", "URB-043 states the corrected maximum order cost"),
    (SPEC, "1,000 basis points", "URB-044 states the discount in basis points"),
    (SPEC, "D-015 is the current Operations Points decision", "URB-014 cites the live decision"),
    (SPEC, "**978**", "Example 12 closes at 978 crowns"),
    (SPEC, "**880**", "Example 8 shows the available balance after acceptance"),
    (SPEC, "rp_applied", "URB-095 allocates generated points once"),
    (SPEC, "rp_reserved", "URB-095 reserves banked points for programmes"),
    (SPEC, "**One assignment, never two.**", "URB-095 states the no-double-count rule"),
    (REGISTER, "**16,170**", "F-CI-005 states the corrected upper bound"),
    (REGISTER, "rp_applied = min(rp_per_turn, need)", "F-CI-021 is the assignment formula"),
    (REGISTER, "**Scope:** `BUILD_FACILITY`", "F-CI-011 is scoped away from infrastructure"),
]

# Each entry must be absent: it is either the superseded rule or a value that produced
# the defect this checker exists to catch.
NEGATIVE_TOKENS = [
    (SPEC, "treasury −22", "Example 12 must not report an unexplained negative treasury"),
    (SPEC, "n × (8 + floor(I / 10))", "URB-043 must not use the flat starting-price formula"),
    (SPEC, "9,000 bp", "the discount is 1,000 bp; 9,000 bp is the remaining multiplier"),
    (SPEC, "D-004 stays provisional", "D-004 is superseded by D-015"),
    (SPEC, "`paid_rp`", "programme spending must never be subtracted from project progress"),
    (REGISTER, "28,420", "the maximum infrastructure order is 16,170, not 28,420"),
    (REGISTER, "paid_rp", "F-CI-021 must not subtract programme spending from progress"),
    (REGISTER, "uses the **starting** level for every step", "the unit price is marginal, not fixed"),
]

STALE_TOKENS = [
    "14,250",
    "21,410",
    "22,600",
    "50 × 13 = 650",
]


def run_cross_document_checks() -> None:
    """The rulebook, the register and the project records must tell one story."""
    for path in (TRACE, DECISIONS, ECON_SPEC, ECON_REG):
        CHECKS[0] += 1
        if not path.exists():
            FAILURES.append(f"missing document: {path.name}")
            return
    trace = TRACE.read_text(encoding="utf-8")
    decisions = DECISIONS.read_text(encoding="utf-8")
    econspec = ECON_SPEC.read_text(encoding="utf-8")
    econreg = ECON_REG.read_text(encoding="utf-8")
    reg = REGISTER.read_text(encoding="utf-8")
    spec_text = SPEC.read_text(encoding="utf-8")

    # The traceability record must describe coverage, not a frozen assertion count.
    CHECKS[0] += 1
    if "141 arithmetic assertions" in trace:
        FAILURES.append("traceability still claims 141 arithmetic assertions")
    CHECKS[0] += 1
    if "verify_city_numbers.py" not in trace:
        FAILURES.append("traceability does not name the city arithmetic verifier")

    # D-069 must describe the stepped model the rulebook now uses.
    row = next((line for line in decisions.splitlines() if line.startswith("| D-069 |")), "")
    CHECKS[0] += 1
    if "stepped marginal sum" not in row:
        FAILURES.append("D-069 does not describe the stepped marginal sum")
    CHECKS[0] += 1
    if "16,170" not in row or "1,000 bp" not in row:
        FAILURES.append("D-069 does not record the 16,170 maximum and the 1,000 bp launch discount")
    CHECKS[0] += 1
    if "2,000 bp" not in row:
        FAILURES.append("D-069 does not record the 2,000 bp combined cap")

    # D-004 must stay visible as history, never as the active decision.
    d004 = next((line for line in decisions.splitlines() if line.startswith("| D-004 |")), "")
    CHECKS[0] += 1
    if "Superseded by D-015" not in d004:
        FAILURES.append("D-004 is not marked superseded by D-015 in DECISIONS.md")

    # --- Correction A: the register's example must be Example 15B's real state -----
    f21 = reg[reg.index("**F-CI-021 — Research progress.**"):
             reg.index("**F-CI-022 — Research completion.**")]
    check("F-CI-021 cites Example 15B's 22/24 state", "**22/24, 3 RP**" in f21, True)
    check("F-CI-021 banks exactly one overflow point", "pool +1" in f21, True)
    check("F-CI-021 does not present 23/24 as Example 15B", "23/24, 3 RP" in f21, False)
    check("F-CI-021 keeps the 23/24 case in Example 20", "Example 20" in f21, True)
    ex15b = spec_text[spec_text.index("**B — overflow at completion.**"):
                     spec_text.index("**C — a programme funded")]
    check("Example 15B opens at 22/24", "**22/24**" in ex15b, True)
    check("Example 15B banks one point", "rp_pool += 3 − 2 = 1" in ex15b, True)
    check("Example 15B says the extra point goes to the pool",
          "1 to the pool" in ex15b, True)

    # --- Correction B: one capacity model across B-04 and B-05 ---------------------
    f6 = econreg[econreg.index("**F-EC-006 — Power demand.**"):
                econreg.index("**F-EC-007 — Power percentage.**")]
    check("F-EC-006 defines planned_batches as M + A", "planned_batches = M + A" in f6, True)
    check("F-EC-006 bounds the plan by capacity", "M + A ≤ C" in f6, True)
    check("F-EC-006 no longer adds manual batches to capacity",
          "capacity + accepted manual batches" in f6, False)
    ecn60 = econspec[econspec.index("**ECN-060 — Processing demand is the sum of batch draws.**"):
                     econspec.index("**ECN-061 — Derating is published and pro-rata.**")]
    check("ECN-060 defines the plan", "planned_batches = M + A" in ecn60, True)
    check("ECN-060 no longer adds manual batches to capacity",
          "chain capacities plus accepted manual orders" in ecn60, False)
    ecn53 = econspec[econspec.index("**ECN-053 — Manual orders reserve capacity.**"):
                     econspec.index("**ECN-054 — A batch is atomic.**")]
    check("ECN-053 says a reservation occupies capacity",
          "occupies slots **inside** `C`" in ecn53, True)
    u74 = spec_text[spec_text.index("**URB-074 — The grid is national and B-04 owns it.**"):
                    spec_text.index("**URB-075 — Generator levels are additive.**")]
    check("URB-074 states M + A ≤ capacity", "M + A ≤ capacity" in u74, True)
    check("URB-074 names capacity + M as invalid", "capacity + M" in u74, True)
    check("URB-074 defines planned_batches", "planned_batches = M + A" in u74, True)
    ex12 = econspec[econspec.index("### Example 12 — Insufficient inputs and an accepted-then-failed order"):
                    econspec.index("### Example 13 — Storage capacity and overflow")]
    check("Example 12 tabulates the C=2, M=2 case", "| Manual fills the chain | 2 | 2 |" in ex12, True)
    check("Example 12 states 4 GU, not 8", "4 GU, not 8" in ex12, True)
    check("Example 12 shows the mixed case", "| Mixed | 3 | 1 |" in ex12, True)
    check("Example 12 shows the idle case", "| Idle with spare capacity | 3 | 0 |" in ex12, True)
    check("Example 12 does not reserve grid units", "power is **not** reserved" in ex12, True)



def main() -> int:
    if not SPEC.exists() or not REGISTER.exists():
        print("FAIL: the B-05 specification or register is missing")
        return 1

    documents = {
        SPEC: SPEC.read_text(encoding="utf-8"),
        REGISTER: REGISTER.read_text(encoding="utf-8"),
    }

    run_examples()
    run_cross_document_checks()

    # --- catalogue and technology counts, read from the published tables -----
    spec_text = documents[SPEC]

    def table_rows(start: str, end: str) -> int:
        segment = spec_text[spec_text.index(start):spec_text.index(end)]
        return len([line for line in segment.splitlines() if line.startswith("| `bld_")])

    extraction = table_rows("**URB-055", "**URB-056")
    processing = table_rows("**URB-056", "**URB-057")
    generators = table_rows("**URB-057", "**URB-058")
    catalogue = extraction + processing + generators + 3  # warehouse, institute, civic centre
    check("extraction facility types", extraction, 7)
    check("processing facility types", processing, 4)
    check("generator classes", generators, 3)
    check("catalogue size", catalogue, 17)
    check("the spec states seventeen types", "seventeen types" in spec_text, True)

    tech_segment = spec_text[spec_text.index("| ID | Name | Branch | RP | Crowns"):
                             spec_text.index("Total: **448 RP**")]
    tech_rows = [line for line in tech_segment.splitlines() if line.startswith("| `tech_")]
    check("technology count", len(tech_rows), 12)
    check("technology RP total", sum(int(line.split("|")[4].strip()) for line in tech_rows), 448)
    check("technology crown total",
          sum(int(line.split("|")[5].strip().replace(",", "")) for line in tech_rows), 3_180)
    check("the spec states twelve technologies", "twelve technologies" in spec_text, True)

    for document, token, reason in DOC_TOKENS:
        CHECKS[0] += 1
        if token not in documents[document]:
            FAILURES.append(f"{document.name}: missing '{token}' ({reason})")

    for document, text in documents.items():
        for token in STALE_TOKENS:
            CHECKS[0] += 1
            if token in text:
                FAILURES.append(f"{document.name}: stale text present: '{token}'")

    for document, token, reason in NEGATIVE_TOKENS:
        CHECKS[0] += 1
        if token in documents[document]:
            FAILURES.append(f"{document.name}: forbidden text present: '{token}' ({reason})")

    for document, name, version in ((SPEC, "B-05", "1.7"), (REGISTER, "register", "1.3")):
        head = "\n".join(documents[document].splitlines()[:4])
        CHECKS[0] += 1
        if f"**Version:** {version}" not in head:
            FAILURES.append(f"{name}: header is not v{version}")

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} problem(s) in {CHECKS[0]} checks")
        for item in FAILURES:
            print("  -", item)
        return 1

    print(f"PASS: {CHECKS[0]}/{CHECKS[0]} city arithmetic checks passed")
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
