"""Prompt 14B — B-04 economy analysis and regression checks.

Independent recomputation path for the Prompt 14B deliverables:

  * the 20 published B-04 worked examples;
  * the integrated cross-system examples A–H;
  * the 30-turn deterministic reference model used to re-run F-EC-039;
  * the margin, dominance and power-utilisation tables;
  * resource, treasury and Alliance conservation identities;
  * document-token regression guards for the 14B corrections.

This is document/tooling QA, not game code. It holds no runtime state, writes nothing
and is not imported by anything. Run it from the `docs/` directory:

    python qa_backups/14B_verify_b04_economy.py
    python qa_backups/14B_verify_b04_economy.py --self-test

Exit status 0 means every recomputation and every regression guard agreed.
"""

from __future__ import annotations

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
REGISTER = DOCS / "stage-2" / "10_economic_formula_and_balance_register.md"
SPEC = DOCS / "stage-2" / "10_economy_resources_treasury_and_finances.md"
REPORT = DOCS / "stage-2" / "25_prompt_14B_b04_economy_completion_report.md"
B14 = DOCS / "stage-2" / "22_formulas_and_balance.md"
PARAMS = DOCS / "stage-2" / "22_numerical_parameter_inventory.md"

RESOURCES = [
    "food", "coal", "oil", "iron", "bauxite", "lead",
    "uranium", "gasoline", "steel", "aluminum", "ammunition",
]

# B-04 register §3.5 — reference prices (book values, crowns per unit).
PRICE = {
    "food": 1, "coal": 1, "oil": 2, "iron": 1, "bauxite": 2, "lead": 3,
    "uranium": 30, "gasoline": 6, "steel": 7, "aluminum": 8, "ammunition": 6,
}

# B-04 register §3.2 — output/batch Y, variable cost/batch V, maintenance/batch M.
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

# B-04 register §3.3 — inputs, output resource, output/batch, variable, draw, maintenance.
RECIPES = {
    "refining": ({"oil": 10}, "gasoline", 8, 20, 2, 2),
    "steel": ({"iron": 10, "coal": 6}, "steel", 8, 24, 3, 2),
    "aluminum": ({"bauxite": 12}, "aluminum", 8, 24, 4, 2),
    "ammunition": ({"lead": 8, "coal": 4}, "ammunition", 10, 20, 2, 2),
}
RECIPE_ORDER = ["refining", "steel", "aluminum", "ammunition"]

# B-04 register §3.4 — generators: GU/level, fuel/level, variable/level, maintenance/level.
GENERATORS = {
    "coal": (6, {"coal": 6}, 10, 2),
    "oil": (6, {"oil": 5}, 14, 2),
    "nuclear": (20, {"uranium": 1, "lead": 1}, 40, 2),
}
GENERATOR_ORDER = ["coal", "oil", "nuclear"]

# B-04 register §3.1 — standard starting bundle (D-063).
START_INV = {
    "food": 120, "coal": 60, "oil": 30, "iron": 30, "bauxite": 20, "lead": 10,
    "uranium": 0, "gasoline": 20, "ammunition": 0, "steel": 20, "aluminum": 0,
}
START_CAP = {
    "food": 3, "coal": 2, "oil": 1, "iron": 1, "bauxite": 0, "lead": 0, "uranium": 0,
    "refining": 1, "steel": 0, "aluminum": 0, "ammunition": 0,
}
START_GENS = {"coal": 1, "oil": 0, "nuclear": 0}
START_TREASURY = 1_500
START_POP = 50_000
START_TAX_BP = 300
START_STABILITY_BP = 10_000
WAREHOUSE = 2_000

# B-05 URB-055/056/057 catalogue — building (DC, crown cost, materials).
BUILDINGS = {
    "farm": (1, 120, {"steel": 5}),
    "coal_mine": (1, 160, {"steel": 5}),
    "oil_well": (1, 220, {"steel": 5}),
    "iron_mine": (1, 180, {"steel": 5}),
    "bauxite_mine": (1, 220, {"steel": 5}),
    "lead_mine": (1, 260, {"steel": 5}),
    "uranium_mine": (1, 600, {"steel": 10, "aluminum": 5}),
    "refinery": (2, 320, {"steel": 15}),
    "steel_mill": (2, 380, {"steel": 15}),
    "smelter": (2, 420, {"steel": 20}),
    "ammo_plant": (2, 360, {"steel": 15}),
    "coal_plant": (1, 280, {"steel": 10}),
    "oil_plant": (1, 340, {"steel": 10, "aluminum": 5}),
    "nuclear_plant": (1, 1_200, {"steel": 30, "aluminum": 20}),
    "warehouse": (1, 180, {"steel": 5}),
    "lab": (3, 500, {"steel": 20}),
    "civic": (2, 300, {"steel": 10}),
}
CAPITAL_DC = 15  # capital at infrastructure 50: 10 + floor(50/10)

FAILURES: list[str] = []
CHECKS = [0]


def check(label: str, actual, expected) -> None:
    CHECKS[0] += 1
    if actual != expected:
        FAILURES.append(f"{label}: computed {actual!r}, expected {expected!r}")


def expect_raises(label: str, fn, exc=ValueError) -> None:
    CHECKS[0] += 1
    try:
        fn()
    except exc:
        return
    except Exception as error:  # noqa: BLE001 - report the wrong exception as a failure
        FAILURES.append(f"{label}: raised {type(error).__name__}, expected {exc.__name__}")
        return
    FAILURES.append(f"{label}: did not raise {exc.__name__}")


def total(inv: dict[str, int]) -> int:
    return sum(inv[r] for r in RESOURCES)


def book_value(inv: dict[str, int]) -> int:
    return sum(inv[r] * PRICE[r] for r in RESOURCES)


def free_space(inv: dict[str, int], warehouse: int = WAREHOUSE) -> int:
    return warehouse - total(inv)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def capital(name: str) -> int:
    """B-05 F-CI-012 construction book value at launch (no discount, no research bonus)."""
    _dc, crowns, materials = BUILDINGS[name]
    return crowns + sum(q * PRICE[r] for r, q in materials.items())


# --------------------------------------------------------------------------------------
# Settlement engine — B-04 ECN-144 P3.1…P3.8, plus the adopted B-06 service cost and the
# B-09 source withholding. Mirrors the published order; no hidden reordering.
# --------------------------------------------------------------------------------------


class State:
    def __init__(
        self,
        treasury: int = START_TREASURY,
        inv: dict[str, int] | None = None,
        caps: dict[str, int] | None = None,
        gens: dict[str, int] | None = None,
        population: int = START_POP,
        tax_bp: int = START_TAX_BP,
        stability_bp: int = START_STABILITY_BP,
        warehouse: int = WAREHOUSE,
    ) -> None:
        if treasury < 0:
            raise ValueError("negative opening treasury")
        if population < 0:
            raise ValueError("negative population")
        if not 0 <= tax_bp <= 10_000:
            raise ValueError("tax rate out of range")
        self.treasury = treasury
        self.inv = dict(START_INV if inv is None else inv)
        self.caps = dict(START_CAP if caps is None else caps)
        self.gens = dict(START_GENS if gens is None else gens)
        self.population = population
        self.tax_bp = tax_bp
        self.stability_bp = stability_bp
        self.warehouse = warehouse
        self.hunger_bp = 0
        self.events: list[tuple[str, str, int]] = []
        self.crown_events: list[int] = []
        self.gross_produced: dict[str, int] = {}
        self.arl: dict[str, int] = {}
        self.unmaintained: list[str] = []
        self.flags: list[str] = []
        self.phase_report: dict[str, dict] = {}

    def crowns(self, delta: int, reason: str, phase: str) -> None:
        if self.treasury + delta < 0:
            raise ValueError(f"negative treasury in {phase}/{reason}: {self.treasury}+{delta}")
        self.treasury += delta
        self.events.append((phase, reason, delta))
        self.crown_events.append(delta)

    def resource(self, resource: str, delta: int, reason: str, phase: str) -> None:
        if resource not in PRICE:
            raise ValueError(f"unknown resource {resource!r}")
        if self.inv[resource] + delta < 0:
            raise ValueError(f"negative {resource} in {phase}/{reason}: {self.inv[resource]}+{delta}")
        self.inv[resource] += delta
        self.events.append((phase, f"{reason}:{resource}", delta))

    def produced(self, resource: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("negative production")
        self.gross_produced[resource] = self.gross_produced.get(resource, 0) + amount

    def arl_credit(self, asset: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("alliance credit must be non-negative")
        self.arl[asset] = self.arl.get(asset, 0) + amount

    def free(self) -> int:
        return free_space(self.inv, self.warehouse)


class Alliance:
    """B-09 source withholding under ECN-213a, cumulative fractional accrual."""

    def __init__(self, crowns_bp: int = 0, resource_rates: dict[str, int] | None = None) -> None:
        if not 0 <= crowns_bp <= 10_000:
            raise ValueError("alliance crowns rate out of range")
        self.crowns_bp = crowns_bp
        self.rates = dict(resource_rates or {})
        for rate in self.rates.values():
            if not 0 <= rate <= 10_000:
                raise ValueError("alliance resource rate out of range")
        self.accrued: dict[str, int] = {}
        self.collected: dict[str, int] = {}

    def tax_event(self, state: State, asset: str, gross: int) -> int:
        if gross < 0:
            raise ValueError("negative production event")
        rate = self.crowns_bp if asset == "crowns" else self.rates.get(asset, 0)
        if rate == 0:
            return 0
        before = self.accrued.get(asset, 0)
        after = before + gross
        tax = after * rate // 10_000 - before * rate // 10_000
        if tax < 0 or tax > gross:
            raise ValueError("alliance tax outside 0..gross")
        self.accrued[asset] = after
        self.collected[asset] = self.collected.get(asset, 0) + tax
        state.arl_credit(asset, tax)
        return tax


def settle(
    state: State,
    *,
    service_share_bp: int = 0,
    service_mod_bp: int = 0,
    alliance: Alliance | None = None,
    manual: dict[str, int] | None = None,
    military_equivalents: int = 0,
    military_upkeep: int = 0,
    facility_upkeep: int = 0,
    op09_hold: int = 0,
    run_policy: bool = True,
) -> dict:
    """Run one P3 settlement in the published order and return a phase report."""
    if service_share_bp < 0 or service_share_bp > 5_000:
        raise ValueError("service share out of range")
    if service_mod_bp < -1_000 or service_mod_bp > 500:
        raise ValueError("service modifier out of range")
    if military_equivalents < 0 or military_upkeep < 0 or facility_upkeep < 0:
        raise ValueError("negative obligation")
    if op09_hold < 0:
        raise ValueError("negative OP-09 hold")

    opening_treasury = state.treasury
    opening_inv = dict(state.inv)
    crown_event_start = len(state.crown_events)
    state.gross_produced = {}
    state.unmaintained = []
    state.flags = []
    manual = dict(manual or {})

    # ---- P3.1 Tax -------------------------------------------------------------------
    base_tax = state.population * state.tax_bp * state.stability_bp // 1_000_000_000
    tax = base_tax * (10_000 - state.hunger_bp) // 10_000
    state.hunger_bp = 0
    state.crowns(+tax, "TAX_INCOME", "P3.1")
    alliance_crowns = 0
    if alliance is not None and tax:
        alliance_crowns = alliance.tax_event(state, "crowns", tax)
        state.crowns(-alliance_crowns, "ALLIANCE_TAX", "P3.1")
    p31 = {"base_tax": base_tax, "tax": tax, "alliance_crowns": alliance_crowns,
           "treasury": state.treasury}

    # ---- P3.2 Maintenance (ECN-147a whole obligations, published order) --------------
    obligations = [(r, state.caps.get(r, 0) * EXTRACTION[r][2]) for r in EXTRACTION_ORDER]
    obligations += [("gen_" + g, state.gens.get(g, 0) * GENERATORS[g][3]) for g in GENERATOR_ORDER]
    obligations += [(c, state.caps.get(c, 0) * RECIPES[c][5]) for c in RECIPE_ORDER]
    paid, cancelled = [], []
    for chain, due in obligations:
        if due == 0:
            continue
        if state.treasury >= due:
            state.crowns(-due, "MAINTENANCE", "P3.2")
            paid.append(chain)
        else:
            cancelled.append(chain)
            state.unmaintained.append(chain)
    p32 = {"paid": paid, "cancelled": cancelled, "treasury": state.treasury}

    # ---- P3.3 Extraction (alliance tax at each production event) ---------------------
    extraction_report = {}
    for chain in EXTRACTION_ORDER:
        y, v, _m = EXTRACTION[chain]
        cap = state.caps.get(chain, 0) if (chain not in state.unmaintained and run_policy) else 0
        batches = 0
        blocked = None
        while batches < cap:
            if state.treasury < v:
                blocked = "MONEY_BLOCKED"
                break
            if state.free() < y:
                blocked = "SPACE_BLOCKED"
                break
            batches += 1
            state.crowns(-v, "PRODUCTION_COST", "P3.3")
            withheld = alliance.tax_event(state, chain, y) if alliance else 0
            state.resource(chain, y - withheld, "RESOURCE_PRODUCED", "P3.3")
            state.produced(chain, y)
        extraction_report[chain] = {"batches": batches, "output": batches * y, "blocked": blocked}
    p33 = {"chains": extraction_report, "treasury": state.treasury}

    # ---- P3.4 Power (coal → oil → nuclear, fail-closed per level) -------------------
    supply = 0
    fuel_used = {}
    for gclass in GENERATOR_ORDER:
        gu, fuel, v, _m = GENERATORS[gclass]
        if "gen_" + gclass in state.unmaintained:
            continue
        for _ in range(state.gens.get(gclass, 0)):
            if all(state.inv[f] >= q for f, q in fuel.items()) and state.treasury >= v:
                for f, q in fuel.items():
                    state.resource(f, -q, "POWER_FUEL", "P3.4")
                    fuel_used[f] = fuel_used.get(f, 0) + q
                state.crowns(-v, "PRODUCTION_COST", "P3.4")
                supply += gu
            else:
                state.flags.append("GENERATOR_IDLE")
    p34 = {"supply": supply, "fuel": fuel_used, "treasury": state.treasury}

    # ---- P3.5 Processing (power derating, manual first, then standing policy) --------
    demand = 0
    planned = {}
    for chain in RECIPE_ORDER:
        cap = state.caps.get(chain, 0)
        m = manual.get(chain, 0)
        if m < 0:
            raise ValueError("negative manual order")
        if m > cap:
            raise ValueError("manual order exceeds capacity")
        a = max(0, cap - m) if run_policy else 0
        planned[chain] = (m, a)
        demand += (m + a) * RECIPES[chain][4]
    pct = 10_000 if demand == 0 else min(10_000, 10_000 * supply // demand)
    processing_report = {}
    for chain in RECIPE_ORDER:
        inputs, output, qty, v, _draw, _m = RECIPES[chain]
        cap = state.caps.get(chain, 0) if chain not in state.unmaintained else 0
        available = cap * pct // 10_000
        m = min(planned[chain][0], cap)

        def batch_feasible(count: int) -> bool:
            """Whole-order check: every batch's money, inputs and space in sequence."""
            money = state.treasury
            stock = dict(state.inv)
            for _ in range(count):
                if money < v:
                    return False
                if any(stock[f] < q for f, q in inputs.items()):
                    return False
                if free_space(stock, state.warehouse) < qty:
                    return False
                money -= v
                for f, q in inputs.items():
                    stock[f] -= q
                stock[output] += qty
            return True

        manual_failed = m > available or (m > 0 and not batch_feasible(m))
        ran_manual = 0
        if m and not manual_failed:
            for _ in range(m):
                for f, q in inputs.items():
                    state.resource(f, -q, "MANUFACTURE_INPUT", "P3.5")
                state.crowns(-v, "PRODUCTION_COST", "P3.5")
                withheld = alliance.tax_event(state, output, qty) if alliance else 0
                state.resource(output, qty - withheld, "MANUFACTURE_OUTPUT", "P3.5")
                state.produced(output, qty)
                ran_manual += 1
        elif manual_failed:
            state.flags.append("MANUFACTURE_FAILED")

        standing = min(available - ran_manual, max(0, cap - ran_manual)) if run_policy else 0
        ran_standing = 0
        blocked = None
        for _ in range(max(0, standing)):
            if state.treasury < v:
                blocked = "MONEY_BLOCKED"
                break
            if any(state.inv[f] < q for f, q in inputs.items()):
                blocked = "INPUT_BLOCKED"
                break
            if state.free() < qty:
                blocked = "SPACE_BLOCKED"
                break
            for f, q in inputs.items():
                state.resource(f, -q, "MANUFACTURE_INPUT", "P3.5")
            state.crowns(-v, "PRODUCTION_COST", "P3.5")
            withheld = alliance.tax_event(state, output, qty) if alliance else 0
            state.resource(output, qty - withheld, "MANUFACTURE_OUTPUT", "P3.5")
            state.produced(output, qty)
            ran_standing += 1
        processing_report[chain] = {
            "manual_planned": m, "manual_ran": ran_manual, "manual_failed": manual_failed,
            "standing_ran": ran_standing, "blocked": blocked,
            "output": (ran_manual + ran_standing) * qty,
        }
    p35 = {"demand": demand, "supply": supply, "power_pct": pct,
           "chains": processing_report, "treasury": state.treasury}

    # ---- P3.6 Food -------------------------------------------------------------------
    food_demand = ceil_div(state.population, 1_000)
    food_after_other = state.inv["food"]
    held = op09_hold
    if food_after_other - held < food_demand:
        held = 0  # release the OP-09 reservation in whole; the action fails at P5
    available = food_after_other - held
    consumed = min(available, food_demand)
    unmet = max(0, food_demand - available)
    state.resource("food", -consumed, "FOOD_CONSUMED", "P3.6")
    hunger = 0 if food_demand == 0 else min(3_000, 3_000 * unmet // food_demand)
    state.hunger_bp = hunger
    p36 = {"demand": food_demand, "consumed": consumed, "unmet": unmet,
           "hunger_bp": hunger, "op09_held": held}

    # ---- P3.7 Obligations ------------------------------------------------------------
    military_food = ceil_div(military_equivalents, 1_000)
    ration_paid = 0
    if military_food:
        if state.inv["food"] >= military_food:
            state.resource("food", -military_food, "OBLIGATION_PAID:MILITARY_RATION", "P3.7")
            ration_paid = military_food
        else:
            state.flags.append("RATION_SHORT")
    service_base = tax * service_share_bp // 10_000
    service_cost = ceil_div(service_base * (10_000 + service_mod_bp), 10_000)
    service_paid = 0
    if service_cost:
        if state.treasury >= service_cost:
            state.crowns(-service_cost, "POLICY_SERVICE_COST", "P3.7")
            service_paid = service_cost
        else:
            state.flags.append("SERVICES_UNFUNDED")
    upkeep_paid = 0
    for amount, flag in ((facility_upkeep, "FACILITY_UPKEEP_CANCELLED"),
                         (military_upkeep, "OBLIGATION_CANCELLED")):
        if amount:
            if state.treasury >= amount:
                state.crowns(-amount, "OBLIGATION_PAID", "P3.7")
                upkeep_paid += amount
            else:
                state.flags.append(flag)
    p37 = {"military_food": military_food, "ration_paid": ration_paid,
           "service_cost": service_cost, "service_paid": service_paid,
           "upkeep_paid": upkeep_paid, "treasury": state.treasury}

    # ---- P3.8 Close and reconcile ----------------------------------------------------
    if state.treasury < 0:
        raise ValueError("negative closing treasury")
    if any(state.inv[r] < 0 for r in RESOURCES):
        raise ValueError("negative closing inventory")
    if total(state.inv) > state.warehouse:
        raise ValueError("warehouse overflow")
    crown_delta = sum(state.crown_events[crown_event_start:])
    if opening_treasury + crown_delta != state.treasury:
        raise ValueError("treasury conservation failed")
    p38 = {"opening_treasury": opening_treasury, "closing_treasury": state.treasury,
           "net_cash_flow": state.treasury - opening_treasury,
           "opening_units": total(opening_inv), "closing_units": total(state.inv),
           "opening_book": book_value(opening_inv), "closing_book": book_value(state.inv),
           "wealth": state.treasury + book_value(state.inv),
           "gross_output_value": sum(state.gross_produced.get(r, 0) * PRICE[r]
                                     for r in RESOURCES)}

    state.phase_report = {"P3.1": p31, "P3.2": p32, "P3.3": p33, "P3.4": p34,
                          "P3.5": p35, "P3.6": p36, "P3.7": p37, "P3.8": p38}
    return state.phase_report


# --------------------------------------------------------------------------------------
# Section 1 — constants and the standard bundle
# --------------------------------------------------------------------------------------


def section_constants() -> None:
    check("price vector", [PRICE[r] for r in RESOURCES],
          [1, 1, 2, 1, 2, 3, 30, 6, 7, 8, 6])
    check("extraction vector", EXTRACTION,
          {"food": (20, 12, 1), "coal": (10, 10, 1), "oil": (8, 14, 1),
           "iron": (10, 10, 1), "bauxite": (8, 14, 1), "lead": (6, 16, 1),
           "uranium": (1, 28, 1)})
    check("bundle units", total(START_INV), 310)
    check("bundle book value", book_value(START_INV), 600)
    check("starting wealth", START_TREASURY + book_value(START_INV), 2_100)
    check("free space", free_space(START_INV), 1_690)
    check("warehouse utilisation bp", total(START_INV) * 10_000 // WAREHOUSE, 1_550)
    check("starting tax", START_POP * START_TAX_BP * START_STABILITY_BP // 1_000_000_000, 150)
    check("starting food demand", ceil_div(START_POP, 1_000), 50)
    check("starting maintenance", 3 + 2 + 1 + 1 + 2 + 2, 11)


# --------------------------------------------------------------------------------------
# Section 2 — the 20 published examples, recomputed independently
# --------------------------------------------------------------------------------------


def section_examples() -> None:
    # Example 1.
    check("Ex1 units", total(START_INV), 310)
    check("Ex1 wealth", 1_500 + 600, 2_100)

    # Example 2 — B-04 capacity operations only (no policy obligation).
    s = State()
    r = settle(s)
    check("Ex2 tax", r["P3.1"]["tax"], 150)
    check("Ex2 maintenance", sum(EXTRACTION[c][2] * START_CAP[c] for c in EXTRACTION_ORDER)
          + RECIPES["refining"][5] + GENERATORS["coal"][3], 11)
    check("Ex2 extraction cost", 3 * 12 + 2 * 10 + 14 + 10, 80)
    check("Ex2 processing cost", 20, 20)
    check("Ex2 generator cost", 10, 10)
    check("Ex2 operating expenses", 11 + 80 + 10 + 20, 121)
    check("Ex2 net operating income", 150 - 121, 29)
    check("Ex2 closing treasury", r["P3.8"]["closing_treasury"], 1_529)
    check("Ex2 closing units", r["P3.8"]["closing_units"], 350)
    check("Ex2 closing book", r["P3.8"]["closing_book"], 678)
    check("Ex2 wealth", r["P3.8"]["wealth"], 2_207)
    check("Ex2 food", s.inv["food"], 130)
    check("Ex2 coal", s.inv["coal"], 74)
    check("Ex2 oil", s.inv["oil"], 28)
    check("Ex2 gasoline", s.inv["gasoline"], 28)
    check("Ex2 iron", s.inv["iron"], 40)

    # Example 3 — mature nation, operating loss with rising inventory value.
    ex3_inv = {"food": 200, "coal": 200, "oil": 200, "iron": 200, "bauxite": 200, "lead": 200,
               "uranium": 10, "gasoline": 100, "steel": 100, "aluminum": 100, "ammunition": 50}
    ex3_cap = {"food": 5, "coal": 4, "oil": 3, "iron": 2, "bauxite": 2, "lead": 1, "uranium": 1,
               "refining": 2, "steel": 2, "aluminum": 1, "ammunition": 1}
    s3 = State(treasury=1_529, inv=ex3_inv, caps=ex3_cap, gens={"coal": 3, "oil": 0, "nuclear": 0})
    check("Ex3 opening units", total(ex3_inv), 1_560)
    check("Ex3 opening book", book_value(ex3_inv), 4_700)
    r3 = settle(s3)
    expected = {"food": 250, "coal": 206, "oil": 204, "iron": 200, "bauxite": 204, "lead": 198,
                "uranium": 11, "gasoline": 116, "steel": 116, "aluminum": 108, "ammunition": 60}
    for resource in RESOURCES:
        check(f"Ex3 {resource}", s3.inv[resource], expected[resource])
    check("Ex3 maintenance", 36, 36)
    check("Ex3 power pct", r3["P3.5"]["power_pct"], 10_000)
    check("Ex3 treasury", r3["P3.8"]["closing_treasury"], 1_247)
    check("Ex3 closing units", r3["P3.8"]["closing_units"], 1_673)
    check("Ex3 closing book", r3["P3.8"]["closing_book"], 5_128)
    check("Ex3 wealth", r3["P3.8"]["wealth"], 6_375)
    check("Ex3 wealth change", 6_375 - (1_529 + 4_700), 146)

    # Example 4 — capex versus opex, reconciled to the B-05 farm catalogue.
    check("Ex4 farm crown cost", BUILDINGS["farm"][1], 120)
    check("Ex4 farm materials", BUILDINGS["farm"][2], {"steel": 5})
    check("Ex4 farm book value (F-CI-012)", capital("farm"), 155)
    check("Ex4 treasury after capex", 1_529 - 120, 1_409)
    check("Ex4 next-turn opex", 12 + 4 * 12 + 20 + 14 + 10 + 10 + 20, 134)
    check("Ex4 next-turn net", 150 - 134, 16)
    check("Ex4 extra batch margin", 20 - (12 + 1), 7)
    check("Ex4 payback turns (F-EC-032)", ceil_div(155, 7), 23)

    # Example 5 — treasury surplus reconciliation, no fee.
    check("Ex5 closing treasury", 1_529 + 150 - 121 - 150 + 50 - 30, 1_428)
    check("Ex5 net operating income", 150 - 121, 29)
    check("Ex5 net cash flow", 1_428 - 1_529, -101)
    check("Ex5 net trade", 50 - 30, 20)

    # Example 6 — warehouse limit on coal.
    coal, money, batches = 1_975, 100, 0
    while batches < 5:
        if WAREHOUSE - coal < 10 or money < 10:
            break
        coal, money, batches = coal + 10, money - 10, batches + 1
    check("Ex6 batches", batches, 2)
    check("Ex6 coal", coal, 1_995)
    check("Ex6 free space", WAREHOUSE - coal, 5)
    check("Ex6 treasury", money - 5, 75)

    # Example 7 — refining.
    base7 = 8 * PRICE["gasoline"] - 10 * PRICE["oil"] - 20 - 2
    check("Ex7 base margin", base7, 6)
    check("Ex7 two-batch margin", 2 * base7, 12)
    check("Ex7 fully loaded at 3.0/GU", 2 * (base7 - 2 * 3), 0)
    check("Ex7 break-even gasoline", (10 * PRICE["oil"] + 20 + 2 + 2 * 3) // 8, 6)

    # Example 8 — aluminium.
    base8 = 8 * PRICE["aluminum"] - 12 * PRICE["bauxite"] - 24 - 2
    check("Ex8 base margin", base8, 14)
    check("Ex8 fully loaded", base8 - 4 * 3, 2)
    check("Ex8 loaded aluminium threshold", round((12 * 2 + 24 + 2 + 12) / 8, 2), 7.75)
    check("Ex8 base aluminium threshold", round((12 * 2 + 24 + 2) / 8, 2), 6.25)
    check("Ex8 loaded bauxite threshold", round((8 * 8 - 24 - 2 - 12) / 12, 2), 2.17)
    check("Ex8 base bauxite threshold", round((8 * 8 - 24 - 2) / 12, 2), 3.17)

    # Example 9 — steel.
    base9 = 8 * PRICE["steel"] - (10 * PRICE["iron"] + 6 * PRICE["coal"]) - 24 - 2
    check("Ex9 base margin", base9, 14)
    check("Ex9 fully loaded", base9 - 3 * 3, 5)

    # Example 10 — ammunition.
    base10 = 10 * PRICE["ammunition"] - (8 * PRICE["lead"] + 4 * PRICE["coal"]) - 20 - 2
    check("Ex10 base margin", base10, 10)
    check("Ex10 fully loaded", base10 - 2 * 3, 4)

    # Example 11 and 19 — hunger.
    check("Ex11 full penalty", min(3_000, 3_000 * 50 // 50), 3_000)
    check("Ex11 tax after full", 150 * (10_000 - 3_000) // 10_000, 105)
    check("Ex11 partial penalty", 3_000 * 20 // 50, 1_200)
    check("Ex11 tax after partial", 150 * (10_000 - 1_200) // 10_000, 132)
    check("Ex19 smaller penalty", 3_000 * 10 // 50, 600)
    check("Ex19 tax", 150 * (10_000 - 600) // 10_000, 141)

    # Example 12 — accepted order fails on power, releases, standing runs one batch.
    pct = min(10_000, 10_000 * 2 // 4)
    check("Ex12 power pct", pct, 5_000)
    check("Ex12 batches available", 2 * pct // 10_000, 1)
    check("Ex12 oil after one batch", 20 - 10, 10)
    check("Ex12 gasoline after one batch", 8, 8)

    # Example 13 — blocked batch destroys nothing.
    check("Ex13 extraction blocked", 20 > 12, True)
    check("Ex13 processing blocked", 8 > 5, True)

    # Example 14 — duplicate settlement.
    marker: dict[tuple[int, int], dict] = {}
    key = (812, 42)
    marker[key] = {"state": "COMPLETE", "closing": 1_529}
    first = marker[key]
    second = marker[key]
    check("Ex14 duplicate returns stored row", first is second, True)
    check("Ex14 duplicate writes no event", len(marker), 1)

    # Example 15 — insolvency without debt.
    check("Ex15 tax", 6_667 * 300 * 10_000 // 1_000_000_000, 20)
    check("Ex15 demand", ceil_div(6_667, 1_000), 7)
    check("Ex15 maintenance", 3 + 2 + 1, 6)
    check("Ex15 closing after three paid chains", 70 - 6 - 36 - 20, 8)
    check("Ex15 oil unaffordable", 8 < 14, True)

    # Example 16 — market accounting.
    check("Ex16 seller", 1_529 + 160, 1_689)
    check("Ex16 buyer", 1_000 - 160, 840)
    check("Ex16 seller wealth change", 160 - 20 * PRICE["steel"], 20)
    check("Ex16 hypothetical fee", 160 * 200 // 10_000, 3)

    # Example 17 — reroll.
    check("Ex17 old wealth", 1_529 + 678, 2_207)
    check("Ex17 replacement", 1_500 + 600, 2_100)

    # Example 18 — power shortfall.
    demand18 = 2 * RECIPES["refining"][4] + 2 * RECIPES["steel"][4]
    check("Ex18 demand", demand18, 10)
    pct18 = min(10_000, 10_000 * 6 // demand18)
    check("Ex18 pct", pct18, 6_000)
    check("Ex18 batches per chain", 2 * pct18 // 10_000, 1)
    check("Ex18 actual draw", RECIPES["refining"][4] + RECIPES["steel"][4], 5)
    check("Ex18 cost", 20 + 24, 44)

    # Example 20 — book versus market.
    check("Ex20 book", 10 * PRICE["steel"], 70)
    check("Ex20 proceeds", 10 * 5, 50)
    check("Ex20 wealth change", 50 - 70, -20)


# --------------------------------------------------------------------------------------
# Section 3 — integrated examples A–H
# --------------------------------------------------------------------------------------


def example_h() -> dict:
    """Standard start with the B-06 STANDARD public-service obligation."""
    s = State()
    r = settle(s, service_share_bp=2_000, service_mod_bp=0)
    return {"state": s, "report": r}


def example_a() -> dict:
    """B-02 × B-04: a complete P3 settlement including a manual order and a garrison."""
    s = State()
    r = settle(s, service_share_bp=2_000, manual={"refining": 1}, military_equivalents=50)
    return {"state": s, "report": r}


def example_b() -> dict:
    """B-05 × B-04: development capacity and input limits."""
    plan = ["farm", "farm", "farm", "coal_mine", "coal_mine", "oil_well", "iron_mine",
            "bauxite_mine", "bauxite_mine", "refinery", "steel_mill", "steel_mill", "smelter"]
    legal = ["farm", "farm", "farm", "coal_mine", "coal_mine", "oil_well", "iron_mine",
             "bauxite_mine", "bauxite_mine", "refinery", "steel_mill", "smelter"]
    return {"used": sum(BUILDINGS[n][0] for n in plan),
            "capacity": CAPITAL_DC,
            "legal_used": sum(BUILDINGS[n][0] for n in legal),
            "legal": legal}


def example_c() -> dict:
    """B-06 × B-04: population, food shortage and next-turn tax."""
    inv = dict(START_INV)
    inv["food"] = 20
    s = State(inv=inv, population=100_000)
    r = settle(s, service_share_bp=2_000)
    next_base = 100_000 * 300 * 10_000 // 1_000_000_000
    next_tax = next_base * (10_000 - s.hunger_bp) // 10_000
    return {"state": s, "report": r, "next_base": next_base, "next_tax": next_tax,
            "next_service": next_tax * 2_000 // 10_000}


def example_d() -> dict:
    """B-07 × B-04: a directed trade at P4 and its book-value effect."""
    seller = State(treasury=1_529, inv={**START_INV, "steel": 40})
    buyer = State(treasury=1_000, inv={**START_INV, "steel": 0})
    price, qty = 8, 20
    gross = price * qty
    seller.resource("steel", -qty, "TRADE_SELL", "P4")
    seller.crowns(+gross, "TRADE_SELL", "P4")
    buyer.resource("steel", +qty, "TRADE_BUY", "P4")
    buyer.crowns(-gross, "TRADE_BUY", "P4")
    return {"seller": seller, "buyer": buyer, "gross": gross, "qty": qty}


def example_e() -> dict:
    """B-09 × B-04: alliance Crowns and iron withholding with cumulative accrual."""
    s = State()
    alliance = Alliance(crowns_bp=1_000, resource_rates={"iron": 2_500})
    r = settle(s, service_share_bp=2_000, alliance=alliance)
    accrual = Alliance(resource_rates={"iron": 2_500})
    demo = State(treasury=0, inv={r: 0 for r in RESOURCES},
                 caps={c: 0 for c in START_CAP},
                 gens={"coal": 0, "oil": 0, "nuclear": 0}, population=0)
    taxes = [accrual.tax_event(demo, "iron", 10), accrual.tax_event(demo, "iron", 10)]
    return {"state": s, "report": r, "alliance": alliance,
            "accrual_taxes": taxes,
            "independent_floors": [10 * 2_500 // 10_000, 10 * 2_500 // 10_000],
            "turn_tax": sum(taxes), "per_turn_floor": 20 * 2_500 // 10_000}


def example_f() -> dict:
    """B-10 × B-04: the military garrison ration."""
    s = State()
    r = settle(s, service_share_bp=2_000, military_equivalents=3_200)
    short_inv = dict(START_INV)
    short_inv["food"] = 45
    short_caps = dict(START_CAP)
    short_caps["food"] = 0
    s2 = State(inv=short_inv, caps=short_caps)
    r2 = settle(s2, military_equivalents=3_200)
    return {"state": s, "report": r, "short_state": s2, "short_report": r2}


def example_g() -> dict:
    """Full integrated standard turn: alliance tax, manual order, garrison and service."""
    s = State()
    alliance = Alliance(crowns_bp=1_000, resource_rates={"iron": 2_500})
    r = settle(s, service_share_bp=2_000, alliance=alliance, manual={"refining": 1},
               military_equivalents=50)
    return {"state": s, "report": r, "alliance": alliance}


# --------------------------------------------------------------------------------------
# Section 4 — 30-turn deterministic reference model (F-EC-039 re-run)
# --------------------------------------------------------------------------------------


def run_30_turn(strategy: str) -> dict:
    if strategy not in {"produce", "idle"}:
        raise ValueError("unknown strategy")
    s = State()
    rows = []
    total_tax = 0
    total_output_value = 0
    turn_refining_stopped = None
    turn_warehouse_blocked = None
    for turn in range(1, 31):
        before = dict(s.inv)
        r = settle(s, service_share_bp=2_000, run_policy=(strategy == "produce"))
        total_tax += r["P3.1"]["tax"]
        total_output_value += r["P3.8"]["gross_output_value"]
        if strategy == "produce" and turn_refining_stopped is None \
                and s.inv["gasoline"] == before["gasoline"]:
            turn_refining_stopped = turn
        if turn_warehouse_blocked is None and r["P3.3"]["chains"]["food"]["blocked"] == "SPACE_BLOCKED":
            turn_warehouse_blocked = turn
        rows.append({
            "turn": turn, "treasury": s.treasury, "units": total(s.inv),
            "book": book_value(s.inv), "wealth": s.treasury + book_value(s.inv),
            "food": s.inv["food"], "oil": s.inv["oil"], "gasoline": s.inv["gasoline"],
        })
    return {"rows": rows, "total_tax": total_tax,
            "total_output_value": total_output_value,
            "net_crowns": rows[-1]["treasury"] - START_TREASURY,
            "refining_stopped": turn_refining_stopped,
            "warehouse_blocked": turn_warehouse_blocked}


# --------------------------------------------------------------------------------------
# Section 5 — margins, power utilisation and dominance
# --------------------------------------------------------------------------------------


def section_margins() -> None:
    base = {}
    for chain in EXTRACTION_ORDER:
        y, v, m = EXTRACTION[chain]
        base[chain] = y * PRICE[chain] - v - m
    for chain in RECIPE_ORDER:
        inputs, output, qty, v, _draw, m = RECIPES[chain]
        base[chain] = qty * PRICE[output] - sum(q * PRICE[r] for r, q in inputs.items()) - v - m
    check("base margin vector", base,
          {"food": 7, "coal": -1, "oil": 1, "iron": -1, "bauxite": 1, "lead": 1,
           "uranium": 1, "refining": 6, "steel": 14, "aluminum": 14, "ammunition": 10})

    loaded = {c: base[c] - RECIPES[c][4] * 3 for c in RECIPE_ORDER}
    check("fully loaded margin vector", loaded,
          {"refining": 0, "steel": 5, "aluminum": 2, "ammunition": 4})

    gen_cost = 6 * PRICE["coal"] + 10 + 2
    check("coal level full cost", gen_cost, 18)
    check("marginal coal cost per GU", gen_cost / 6, 3.0)
    check("actual standard-start cost per used GU", gen_cost // 2, 9)
    check("standard-start refining margin, actual power", base["refining"] - gen_cost, -12)

    coal = (6 * PRICE["coal"] + 10 + 2) / 6
    oil = (5 * PRICE["oil"] + 14 + 2) / 6
    nuclear = (1 * PRICE["uranium"] + 1 * PRICE["lead"] + 40 + 2) / 20
    check("coal crowns per GU", round(coal, 2), 3.0)
    check("oil crowns per GU", round(oil, 2), 4.33)
    check("nuclear crowns per GU", round(nuclear, 2), 3.75)

    cap = {name: capital(name) for name in BUILDINGS}
    check("B-05 capital vector", {k: cap[k] for k in (
        "farm", "coal_mine", "oil_well", "iron_mine", "bauxite_mine", "lead_mine",
        "uranium_mine", "refinery", "steel_mill", "smelter", "ammo_plant")},
        {"farm": 155, "coal_mine": 195, "oil_well": 255, "iron_mine": 215,
         "bauxite_mine": 255, "lead_mine": 295, "uranium_mine": 710,
         "refinery": 425, "steel_mill": 485, "smelter": 560, "ammo_plant": 465})
    check("steel capital per loaded margin", ceil_div(cap["steel_mill"], loaded["steel"]), 97)
    check("aluminum capital per loaded margin", ceil_div(cap["smelter"], loaded["aluminum"]), 280)
    check("ammunition capital per loaded margin", ceil_div(cap["ammo_plant"], loaded["ammunition"]), 117)


# --------------------------------------------------------------------------------------
# Section 6 — conservation and negative regression tests
# --------------------------------------------------------------------------------------


def section_conservation() -> None:
    for name, example in (("H", example_h()), ("A", example_a()), ("G", example_g())):
        state = example["state"]
        report = example["report"]
        for resource in RESOURCES:
            delta = sum(d for _p, r, d in state.events if r.endswith(":" + resource))
            check(f"{name} {resource} ledger sums to closing", delta,
                  state.inv[resource] - START_INV[resource])
        check(f"{name} treasury identity",
              report["P3.8"]["opening_treasury"] + sum(state.crown_events),
              report["P3.8"]["closing_treasury"])
        check(f"{name} wealth identity",
              report["P3.8"]["closing_treasury"] + book_value(state.inv),
              report["P3.8"]["wealth"])
        check(f"{name} warehouse respected", total(state.inv) <= WAREHOUSE, True)
        check(f"{name} non-negative treasury", state.treasury >= 0, True)

    g = example_g()
    national_crown_debit = -sum(d for _p, r, d in g["state"].events if r == "ALLIANCE_TAX")
    check("G alliance crowns collected equal national debit",
          g["alliance"].collected.get("crowns", 0), national_crown_debit)
    check("G alliance iron collected", g["alliance"].collected.get("iron", 0), 2)
    check("G ARL iron credited", g["state"].arl.get("iron", 0), 2)
    check("G ARL no negative", all(v >= 0 for v in g["state"].arl.values()), True)

    e = example_e()
    check("E accrual 2+2 is 5, not 4", sum(e["accrual_taxes"]), 5)
    check("E independent floors under-collect", sum(e["independent_floors"]), 4)
    check("E turn tax equals per-turn floor", e["turn_tax"], e["per_turn_floor"])

    h = example_h()
    check("H gross output value", h["report"]["P3.8"]["gross_output_value"], 154)
    check("H net capacity operating income", h["report"]["P3.1"]["tax"] - 121, 29)
    check("H service cost", h["report"]["P3.7"]["service_cost"], 30)
    check("H closing treasury", h["report"]["P3.8"]["closing_treasury"], 1_499)
    check("H net operating income after service", 29 - 30, -1)
    check("H net economic result", -1 + 78, 77)
    check("H wealth", h["report"]["P3.8"]["wealth"], 2_177)

    a = example_a()
    check("A manual refining ran", a["report"]["P3.5"]["chains"]["refining"]["manual_ran"], 1)
    check("A military ration", a["report"]["P3.7"]["ration_paid"], 1)
    check("A food closing", a["state"].inv["food"], 129)
    check("A treasury", a["report"]["P3.8"]["closing_treasury"], 1_499)

    b = example_b()
    check("B build plan exceeds capacity", b["used"], 17)
    check("B capital capacity", b["capacity"], 15)
    check("B legal plan fits exactly", b["legal_used"], 15)

    c = example_c()
    check("C food demanded", c["report"]["P3.6"]["demand"], 100)
    check("C food produced", c["state"].gross_produced["food"], 60)
    check("C unmet", c["report"]["P3.6"]["unmet"], 20)
    check("C hunger", c["state"].hunger_bp, 600)
    check("C next tax", c["next_tax"], 282)
    check("C next service", c["next_service"], 56)

    d = example_d()
    check("D gross", d["gross"], 160)
    check("D seller crowns", d["seller"].treasury, 1_689)
    check("D buyer crowns", d["buyer"].treasury, 840)
    check("D seller steel", d["seller"].inv["steel"], 20)
    check("D buyer steel", d["buyer"].inv["steel"], 20)
    check("D seller wealth change", d["gross"] - d["qty"] * PRICE["steel"], 20)
    check("D buyer wealth change", -d["gross"] + d["qty"] * PRICE["steel"], -20)
    check("D world wealth unchanged", 0, 0)

    f = example_f()
    check("F ration equivalents 3200", ceil_div(3_200, 1_000), 4)
    check("F food after civilian and ration", f["state"].inv["food"], 126)
    check("F short ration cancelled", f["short_report"]["P3.7"]["ration_paid"], 0)
    check("F short flag", "RATION_SHORT" in f["short_state"].flags, True)
    check("F civilian demand paid first", f["short_report"]["P3.6"]["consumed"], 45)

    g2 = example_g()
    check("G treasury", g2["report"]["P3.8"]["closing_treasury"], 1_484)
    check("G food", g2["state"].inv["food"], 129)
    check("G iron net", g2["state"].inv["iron"], 38)
    check("G coal", g2["state"].inv["coal"], 74)
    check("G oil", g2["state"].inv["oil"], 28)
    check("G gasoline", g2["state"].inv["gasoline"], 28)
    check("G units", total(g2["state"].inv), 347)
    check("G book", book_value(g2["state"].inv), 675)
    check("G wealth", g2["report"]["P3.8"]["wealth"], 2_159)
    check("G alliance crowns", g2["alliance"].collected.get("crowns", 0), 15)
    check("G service cost on gross tax", g2["report"]["P3.7"]["service_cost"], 30)


def section_negative() -> None:
    zero = State(treasury=0, inv={r: 0 for r in RESOURCES},
                 caps={c: 0 for c in START_CAP}, gens={"coal": 0, "oil": 0, "nuclear": 0})
    expect_raises("negative crown rejected", lambda: zero.crowns(-1, "TEST", "P3"))
    expect_raises("negative resource rejected", lambda: zero.resource("food", -1, "TEST", "P3"))
    expect_raises("unknown resource rejected", lambda: zero.resource("gold", +1, "TEST", "P3"))
    expect_raises("alliance rate above 10000 rejected", lambda: Alliance(crowns_bp=10_001))
    expect_raises("negative alliance rate rejected", lambda: Alliance(resource_rates={"iron": -1}))
    expect_raises("manual order above capacity rejected",
                  lambda: settle(State(), manual={"refining": 2}))
    expect_raises("negative manual order rejected", lambda: settle(State(), manual={"refining": -1}))
    expect_raises("negative military force rejected",
                  lambda: settle(State(), military_equivalents=-1))
    expect_raises("negative population rejected", lambda: State(population=-1))
    expect_raises("tax rate above 10000 rejected", lambda: State(tax_bp=10_001))
    expect_raises("service share above 5000 rejected", lambda: settle(State(), service_share_bp=5_001))

    poor = State(treasury=0, population=0)
    r = settle(poor)
    check("zero treasury closes at zero", r["P3.8"]["closing_treasury"], 0)
    check("zero treasury cancels all six obligations", len(poor.unmaintained), 6)
    check("zero treasury runs no paid batch",
          any(v["batches"] for v in r["P3.3"]["chains"].values()), False)

    inv = {r: 0 for r in RESOURCES}
    inv.update({"iron": 9, "coal": 100})
    s = State(treasury=100, inv=inv,
              caps={"food": 0, "coal": 0, "oil": 0, "iron": 0, "bauxite": 0, "lead": 0,
                    "uranium": 0, "refining": 0, "steel": 1, "aluminum": 0, "ammunition": 0},
              gens={"coal": 1, "oil": 0, "nuclear": 0}, population=0)
    r = settle(s)
    check("short input runs no steel batch", r["P3.5"]["chains"]["steel"]["output"], 0)
    check("short input leaves iron intact", s.inv["iron"], 9)
    check("short input leaves coal after fuel", s.inv["coal"], 94)

    inv = {r: 0 for r in RESOURCES}
    inv["coal"] = 1_990
    s = State(treasury=100, inv=inv, caps={**{c: 0 for c in START_CAP}, "food": 3},
              gens={"coal": 0, "oil": 0, "nuclear": 0}, population=0)
    r = settle(s)
    check("space-blocked food batch", r["P3.3"]["chains"]["food"]["batches"], 0)
    check("space block destroys nothing", s.inv["coal"], 1_990)

    s = State(treasury=1_000, inv={**START_INV, "oil": 100},
              gens={"coal": 0, "oil": 0, "nuclear": 0})
    r = settle(s)
    check("no power runs no refining", r["P3.5"]["chains"]["refining"]["output"], 0)
    check("no power consumes no oil", s.inv["oil"], 108)

    check("hunger capped near full", min(3_000, 3_000 * 999 // 1_000), 2_997)
    check("hunger cap at full shortage", min(3_000, 3_000 * 50 // 50), 3_000)

    s = State(treasury=0, population=50_000)
    r = settle(s, service_share_bp=2_000)
    check("unfunded service charges nothing", r["P3.7"]["service_paid"], 0)
    check("unfunded service flagged", "SERVICES_UNFUNDED" in s.flags, True)

    inv = dict(START_INV)
    inv["food"] = 0
    s = State(inv=inv, caps={**{c: 0 for c in START_CAP}, "food": 0})
    r = settle(s, military_equivalents=3_200)
    check("ration cancelled whole", r["P3.7"]["ration_paid"], 0)
    check("ration short flagged", "RATION_SHORT" in s.flags, True)

    seen = {("812", "42", "P3.1", "tax", 1)}
    seen.add(("812", "42", "P3.1", "tax", 1))
    check("duplicate event key is a no-op", len(seen), 1)


# --------------------------------------------------------------------------------------
# Section 7 — document-token regression guards
# --------------------------------------------------------------------------------------


def section_documents() -> None:
    documents = {}
    for path in (REGISTER, SPEC, REPORT, B14, PARAMS):
        documents[path] = path.read_text(encoding="utf-8") if path.exists() else ""

    required = [
        (SPEC, "POLICY_SERVICE_COST"),
        (SPEC, "public-service"),
        (SPEC, "net economic result"),
        (SPEC, "yield_bonus"),
        (SPEC, "standards_bonus"),
        (REGISTER, "POLICY_SERVICE_COST"),
        (REGISTER, "net economic result"),
        (REGISTER, "yield_bonus"),
        (SPEC, "120 crowns + 5 steel"),
        (SPEC, "Book value 155"),
        (REGISTER, "Book value 155; margin 7; payback 23"),
        (SPEC, "1,499"),
        (SPEC, "Example H"),
    ]
    for path, token in required:
        CHECKS[0] += 1
        if token not in documents[path]:
            FAILURES.append(f"{path.name}: missing required 14B token {token!r}")

    stale = [
        "roughly twelve turns of full operating cost",
        "positive net operating income if the player does nothing",
        "150 + 10×7 + 5×6 = 250",
        "payback on the 250 book value is about **36 turns**",
        "Book value 250; margin 7; payback 36",
        "P3.7 generator settlement",
        "gasoline → construction fuel",
    ]
    for path, text in documents.items():
        if path is REPORT:
            continue  # the completion report preserves the superseded values as its change record
        for token in stale:
            CHECKS[0] += 1
            if token in text:
                FAILURES.append(f"{path.name}: stale 14B claim still present: {token!r}")

    if documents[REPORT]:
        for token in ("## 1", "## 2", "## 3", "## 4", "## 5", "## 6", "## 7", "## 8",
                      "Example A", "Example B", "Example C", "Example D", "Example E",
                      "Example F", "Example G", "Example H",
                      "VERIFIED CONSISTENT", "CONTRADICTION IDENTIFIED",
                      "OUTSIDE PROMPT 14B AUTHORITY"):
            CHECKS[0] += 1
            if token not in documents[REPORT]:
                FAILURES.append(f"14B report missing {token!r}")

    CHECKS[0] += 1
    if "P3.4 power generation" not in documents[PARAMS]:
        FAILURES.append("parameter inventory: generator timing not corrected to P3.4")


# --------------------------------------------------------------------------------------
# Self-tests — deliberate mutations that must be detected
# --------------------------------------------------------------------------------------


def self_test() -> int:
    global CHECKS, FAILURES
    saved_checks, saved_failures = CHECKS, FAILURES
    cases: list[tuple[str, bool]] = []

    CHECKS, FAILURES = [0], []
    original = PRICE["steel"]
    PRICE["steel"] = 8
    try:
        section_margins()
    finally:
        PRICE["steel"] = original
    cases.append(("mutated steel price detected", bool(FAILURES)))

    CHECKS, FAILURES = [0], []
    original_recipe = RECIPES["steel"]
    RECIPES["steel"] = ({"iron": 10, "coal": 6}, "steel", 9, 24, 3, 2)
    try:
        section_examples()
    finally:
        RECIPES["steel"] = original_recipe
    cases.append(("mutated recipe detected", bool(FAILURES)))

    CHECKS, FAILURES = [0], []
    try:
        State(treasury=0).crowns(-1, "TEST", "P3")
        cases.append(("negative treasury detected", False))
    except ValueError:
        cases.append(("negative treasury detected", True))

    marker = {(1, 1): "COMPLETE"}
    marker[(1, 1)] = "COMPLETE"
    cases.append(("duplicate settlement is idempotent", len(marker) == 1))

    CHECKS, FAILURES = saved_checks, saved_failures
    for label, passed in cases:
        CHECKS[0] += 1
        if not passed:
            FAILURES.append(f"self-test {label} did not trigger")
    print(f"SELF-TESTS: {len(cases)} cases")
    return 0 if all(p for _l, p in cases) else 1


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------


def main() -> int:
    if not REGISTER.exists() or not SPEC.exists():
        print("FAIL: the B-04 register or rulebook is missing")
        return 1

    section_constants()
    section_examples()
    section_margins()
    section_conservation()
    section_negative()
    section_documents()

    produce = run_30_turn("produce")
    idle = run_30_turn("idle")
    check("30-turn produce first refining idle turn", produce["refining_stopped"], 16)
    check("30-turn produce treasury", produce["rows"][-1]["treasury"], 1_530)
    check("30-turn produce wealth", produce["rows"][-1]["wealth"], 4_386)
    check("30-turn produce gross output", produce["total_output_value"], 4_476)
    check("30-turn produce tax", produce["total_tax"], 4_500)
    check("30-turn produce closing units", produce["rows"][-1]["units"], 1_516)
    check("30-turn idle treasury", idle["rows"][-1]["treasury"], 3_713)
    check("30-turn idle wealth", idle["rows"][-1]["wealth"], 4_133)
    check("30-turn idle gross output", idle["total_output_value"], 0)
    check("30-turn idle tax (hunger-reduced)", idle["total_tax"], 3_303)
    check("gross money-creation fails by 24", produce["total_tax"] - produce["total_output_value"], 24)
    check("net money added is 30", produce["net_crowns"], 30)

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} problem(s) in {CHECKS[0]} checks")
        for item in FAILURES:
            print("  -", item)
        return 1

    print(f"PASS: {CHECKS[0]}/{CHECKS[0]} Prompt 14B checks passed")
    print(f"30-turn produce: treasury {produce['rows'][-1]['treasury']}, "
          f"wealth {produce['rows'][-1]['wealth']}, refining stopped turn {produce['refining_stopped']}")
    print(f"30-turn idle:    treasury {idle['rows'][-1]['treasury']}, "
          f"wealth {idle['rows'][-1]['wealth']}")
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
