#!/usr/bin/env python3
"""Prompt 14C — B-05 deterministic reference model (documentation tooling, not game code).

Implements the published B-05 rules on top of the published B-04 settlement order and
B-06 housing-growth formula with integer arithmetic only.  It is a hand-equivalent
arithmetic model: one nation, no market counterparty, no politics, no warfare.

Owned rules consumed, never restated:
  B-04: tax (F-EC-001/003), food demand (F-EC-002), extraction (F-EC-004/005),
        power (F-EC-013), processing (F-EC-006..012), maintenance (F-EC-014),
        warehouse (F-EC-023), reference prices (D-058), P3 order (ECN-144).
  B-05: city costs (F-CI-004/005/006), capacity/housing (F-CI-001/002),
        construction (F-CI-011/012), research (F-CI-020/021/022), upkeep (F-CI-025),
        warehouse (F-CI-014), modifiers (F-CI-023), programmes (F-CI-024).
  B-06: growth (F-PD-001/002) and housing cap (DMP-030), service cost (F-PD-020).

Scenario sales are labelled assumptions: `reference` sells chosen goods to an
assumed buyer at the B-04 reference price (an optimistic B-07 assumption), `none`
sells nothing.  No NPC demand exists in B-07 and the model never claims one.
"""

import json
import math
import sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Published constants (B-04 register §3, B-05 register §3)
# ---------------------------------------------------------------------------
RESOURCES = ["food", "coal", "oil", "iron", "bauxite", "lead", "uranium",
             "gasoline", "ammunition", "steel", "aluminum"]
RAW = ["food", "coal", "oil", "iron", "bauxite", "lead", "uranium"]
MANUFACTURED = ["gasoline", "ammunition", "steel", "aluminum"]

EXTRACT = {  # Y, V, M  per batch
    "food": (20, 12, 1), "coal": (10, 10, 1), "oil": (8, 14, 1),
    "iron": (10, 10, 1), "bauxite": (8, 14, 1), "lead": (6, 16, 1),
    "uranium": (1, 28, 1),
}
PROCESS = {  # chain: (inputs dict, Y, V, GU, M)
    "gasoline": ({"oil": 10}, 8, 20, 2, 2),
    "steel": ({"iron": 10, "coal": 6}, 8, 24, 3, 2),
    "aluminum": ({"bauxite": 12}, 8, 24, 4, 2),
    "ammunition": ({"lead": 8, "coal": 4}, 10, 20, 2, 2),
}
GEN = {  # class: (GU, fuel dict, V, M)
    "coal": (6, {"coal": 6}, 10, 2),
    "oil": (6, {"oil": 5}, 14, 2),
    "nuclear": (20, {"uranium": 1, "lead": 1}, 40, 2),
}
PRICE = {"food": 1, "coal": 1, "oil": 2, "iron": 1, "bauxite": 2, "lead": 3,
         "uranium": 30, "gasoline": 6, "ammunition": 6, "steel": 7, "aluminum": 8}

BUILD = {  # bld: (class, DC, crowns, materials dict, resource or chain)
    "bld_farm": ("extraction", 1, 120, {"steel": 5}, "food"),
    "bld_coal_mine": ("extraction", 1, 160, {"steel": 5}, "coal"),
    "bld_oil_well": ("extraction", 1, 220, {"steel": 5}, "oil"),
    "bld_iron_mine": ("extraction", 1, 180, {"steel": 5}, "iron"),
    "bld_bauxite_mine": ("extraction", 1, 220, {"steel": 5}, "bauxite"),
    "bld_lead_mine": ("extraction", 1, 260, {"steel": 5}, "lead"),
    "bld_uranium_mine": ("extraction", 1, 600, {"steel": 10, "aluminum": 5}, "uranium"),
    "bld_refinery": ("processing", 2, 320, {"steel": 15}, "gasoline"),
    "bld_steel_mill": ("processing", 2, 380, {"steel": 15}, "steel"),
    "bld_smelter": ("processing", 2, 420, {"steel": 20}, "aluminum"),
    "bld_ammo_plant": ("processing", 2, 360, {"steel": 15}, "ammunition"),
    "bld_coal_plant": ("generation", 2, 280, {"steel": 10}, "coal"),
    "bld_oil_plant": ("generation", 2, 340, {"steel": 10, "aluminum": 5}, "oil"),
    "bld_nuclear_plant": ("generation", 2, 1200, {"steel": 30, "aluminum": 20}, "nuclear"),
    "bld_warehouse": ("support", 1, 180, {"steel": 5}, "warehouse"),
    "bld_lab": ("support", 3, 500, {"steel": 20}, "lab"),
    "bld_civic": ("support", 2, 300, {"steel": 10}, "civic"),
}
LIMITS = {"extraction_per_resource": 8, "processing_per_chain": 4,
          "generator_levels": 6, "warehouse": 6, "labs": 2, "civics": 3}

TECH = {  # id: (branch, rp, crowns, prereqs, effect dict)
    "tech_agri_rotation": ("Agriculture", 24, 160, [], {"yield": {"food": 1}}),
    "tech_agri_mechanisation": ("Agriculture", 44, 300, ["tech_agri_rotation"], {"yield": {"food": 1}}),
    "tech_ext_coal": ("Extraction", 20, 140, [], {"yield": {"coal": 1}}),
    "tech_ext_oil": ("Extraction", 32, 220, ["tech_ext_coal"], {"yield": {"oil": 1}}),
    "tech_ext_metals": ("Extraction", 40, 280, ["tech_ext_coal"], {"yield": {"iron": 1, "bauxite": 1}}),
    "tech_ext_deep": ("Extraction", 56, 360, ["tech_ext_metals"], {"yield": {"lead": 1, "uranium": 1}}),
    "tech_ind_heat": ("Industry", 28, 200, [], {"yield": {"steel": 1}, "unlock": ["bld_ammo_plant"]}),
    "tech_ind_chem": ("Industry", 48, 340, ["tech_ind_heat"], {"yield": {"gasoline": 1, "aluminum": 1}, "unlock": ["bld_smelter"]}),
    "tech_ind_ordnance": ("Industry", 36, 260, ["tech_ind_heat"], {"yield": {"ammunition": 1}}),
    "tech_civ_survey": ("Civil works", 20, 140, [], {"infra_discount": 1000}),
    "tech_civ_methods": ("Civil works", 40, 280, ["tech_civ_survey"], {"build_discount": 1000}),
    "tech_nuclear_engineering": ("Energy", 60, 500, ["tech_civ_methods", "tech_ind_chem"], {"unlock": ["bld_uranium_mine", "bld_nuclear_plant"]}),
}
BRANCHES = {
    "Agriculture": ["tech_agri_rotation", "tech_agri_mechanisation"],
    "Extraction": ["tech_ext_coal", "tech_ext_oil", "tech_ext_metals", "tech_ext_deep"],
    "Industry": ["tech_ind_heat", "tech_ind_chem", "tech_ind_ordnance"],
    "Civil works": ["tech_civ_survey", "tech_civ_methods"],
    "Energy": ["tech_nuclear_engineering"],
}
PROGRAMMES = {  # id: (branch, rp, crowns, materials, effect)
    "prg_granary": ("Agriculture", 100, 900, {"steel": 100, "aluminum": 50}, {"warehouse": 500, "yield": {"food": 1}}),
    "prg_survey": ("Extraction", 100, 1000, {"steel": 100, "gasoline": 50}, {"extract_v_bonus": 2}),
    "prg_standards": ("Industry", 100, 1200, {"steel": 150, "aluminum": 50}, {"maint_bonus": 1}),
    "prg_civil_works": ("Civil works", 100, 1100, {"steel": 120, "aluminum": 60}, {"dc_per_city": 2}),
}

CITY_BASE_COST = 400
CITY_COST_COEF = 150
CITY_STEEL = 20
INFRA_MIN = 10
INFRA_MAX = 500
BASE_DC = 10
DC_PER_INFRA = 10
HOUSING_BASE = 45000
HOUSING_PER_INFRA = 100
HOUSING_PER_CIVIC = 25000
MAX_CITIES = 12
DEMOLITION_BP = 2500
# B-06 standard-start fiscal setting: 300 bp tax, 20% service share, approval 55.
TAX_BP = 300
SERVICE_SHARE_BP = 2000
APPROVAL = 55
POP_FLOOR = 1000


def city_cost(k):
    return CITY_BASE_COST + CITY_COST_COEF * k * k


def infra_unit_cost(level):
    return 8 + level // DC_PER_INFRA


def infra_cost(level, n, discount_bp=0):
    base = sum(infra_unit_cost(level + i) for i in range(n))
    if discount_bp:
        return -(-base * (10000 - discount_bp) // 10000)
    return base


def capacity(infra, dc_bonus=0):
    return BASE_DC + infra // DC_PER_INFRA + dc_bonus


def housing(infra, funded_civics):
    return HOUSING_BASE + HOUSING_PER_INFRA * infra + HOUSING_PER_CIVIC * funded_civics


def book_value(crown_cost, materials):
    return crown_cost + sum(q * PRICE[m] for m, q in materials.items())


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------
@dataclass
class CityState:
    name: str
    infra: int = 10
    counts: dict = field(default_factory=dict)   # bld -> count
    infra_gross: int = 0                        # capitalised upgrade lots

    def count(self, bld):
        return self.counts.get(bld, 0)

    def dc_used(self):
        return sum(BUILD[b][1] * self.count(b) for b in BUILD)

    def dc_capacity(self, bonus=0):
        return capacity(self.infra, bonus)


@dataclass
class Nation:
    name: str
    treasury: int
    population: int
    inventory: dict
    cities: list
    expansions: int = 0
    granary: bool = False
    techs: set = field(default_factory=set)
    programmes: set = field(default_factory=set)
    active_tech: str = None
    progress: int = 0
    rp_pool: int = 0
    hunger_bp: int = 0
    fixed_other: int = 0          # founding lots + facility book values
    lab_upkeep_paid: bool = True
    civic_upkeep_paid: bool = True
    turn: int = 0
    # cumulative recorders
    tax_total: int = 0
    variable_total: int = 0
    maintenance_total: int = 0
    upkeep_total: int = 0
    service_total: int = 0
    capex_total: int = 0
    research_crowns: int = 0
    programme_crowns: int = 0
    sales_total: int = 0
    produced: dict = field(default_factory=lambda: {r: 0 for r in RESOURCES})
    sold: dict = field(default_factory=lambda: {r: 0 for r in RESOURCES})
    built: dict = field(default_factory=lambda: {b: 0 for b in BUILD})
    founded: int = 0
    infra_levels_bought: int = 0
    lab_idle_turns: int = 0
    civic_unfunded_turns: int = 0
    chain_unmaintained: dict = field(default_factory=lambda: {c: 0 for c in list(EXTRACT) + list(PROCESS) + list(GEN)})
    space_blocked: dict = field(default_factory=lambda: {c: 0 for c in list(EXTRACT) + list(PROCESS)})
    power_short_turns: int = 0
    idle_generator_gu: int = 0
    warehouse_peak: int = 0
    food_short_turns: int = 0

    # derived -----------------------------------------------------------------
    def add_inv(self, res, qty):
        self.inventory[res] += qty

    def stock(self):
        return sum(self.inventory.values())

    def warehouse_capacity(self):
        return 2000 + 250 * self.expansions + (500 if self.granary else 0)

    def free_space(self):
        return self.warehouse_capacity() - self.stock()

    def labs(self):
        return sum(c.count("bld_lab") for c in self.cities)

    def civics(self):
        return sum(c.count("bld_civic") for c in self.cities)

    def facilities(self, bld):
        return sum(c.count(bld) for c in self.cities)

    def dc_bonus(self):
        return 2 * len(self.cities) if "prg_civil_works" in self.programmes else 0

    def yield_bonus(self, res):
        bonus = 0
        for t in self.techs:
            bonus += TECH[t][4].get("yield", {}).get(res, 0)
        if "prg_granary" in self.programmes and res == "food":
            bonus += 1
        cap = 3 if res == "food" else 1
        if res in MANUFACTURED:
            cap = 1
        return min(cap, bonus)

    def extract_v(self, res):
        v = EXTRACT[res][1]
        if "prg_survey" in self.programmes:
            v = max(2, v - 2)
        return v

    def proc_maint(self):
        return 1 if "prg_standards" in self.programmes else 2

    def housing_growth(self):
        return sum(housing(c.infra, c.count("bld_civic") if self.civic_upkeep_paid else 0)
                   for c in self.cities)

    def fixed_assets(self):
        return sum(c.infra_gross for c in self.cities) + self.fixed_other

    def wealth(self):
        return self.treasury + sum(q * PRICE[r] for r, q in self.inventory.items()) + self.fixed_assets()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def standard_start():
    capital = CityState("Capital", infra=50, counts={
        "bld_farm": 3, "bld_coal_mine": 2, "bld_oil_well": 1, "bld_iron_mine": 1,
        "bld_refinery": 1, "bld_coal_plant": 1})
    inv = {"food": 120, "coal": 60, "oil": 30, "iron": 30, "bauxite": 20,
           "lead": 10, "uranium": 0, "gasoline": 20, "ammunition": 0,
           "steel": 20, "aluminum": 0}
    return Nation("Standard", 1500, 50000, inv, [capital])


def charge(n, crowns, materials=None):
    """Charge if affordable; returns True when paid."""
    materials = materials or {}
    if n.treasury < crowns:
        return False
    if any(n.inventory[m] < q for m, q in materials.items()):
        return False
    n.treasury -= crowns
    for m, q in materials.items():
        n.inventory[m] -= q
    return True


def build_order(n, city, bld):
    """Validate and resolve one BUILD_FACILITY at P4.1. Returns (ok, reason)."""
    cls, dc, crowns, mats, _ = BUILD[bld]
    if bld in ("bld_farm", "bld_coal_mine", "bld_oil_well", "bld_iron_mine",
               "bld_bauxite_mine", "bld_lead_mine", "bld_uranium_mine"):
        if city.count(bld) >= LIMITS["extraction_per_resource"]:
            return False, "limit"
    if bld in ("bld_refinery", "bld_steel_mill", "bld_smelter", "bld_ammo_plant"):
        if city.count(bld) >= LIMITS["processing_per_chain"]:
            return False, "limit"
    if bld in ("bld_coal_plant", "bld_oil_plant", "bld_nuclear_plant"):
        levels = sum(city.count(b) for b in ("bld_coal_plant", "bld_oil_plant", "bld_nuclear_plant"))
        if levels >= LIMITS["generator_levels"]:
            return False, "limit"
    if bld == "bld_warehouse" and city.count(bld) >= LIMITS["warehouse"]:
        return False, "limit"
    if bld == "bld_lab" and city.count(bld) >= LIMITS["labs"]:
        return False, "limit"
    if bld == "bld_civic" and city.count(bld) >= LIMITS["civics"]:
        return False, "limit"
    nuclear_unlocks = TECH["tech_nuclear_engineering"][4]["unlock"]
    if bld in nuclear_unlocks and "tech_nuclear_engineering" not in n.techs:
        return False, "prereq"
    if bld == "bld_smelter" and "tech_ind_chem" not in n.techs:
        return False, "prereq"
    if bld == "bld_ammo_plant" and "tech_ind_heat" not in n.techs:
        return False, "prereq"
    if city.dc_used() + dc > city.dc_capacity(n.dc_bonus()):
        return False, "dc"
    if bld == "bld_warehouse":
        crowns = 180 + 40 * n.expansions
    else:
        crowns = crowns
    if "tech_civ_methods" in n.techs and bld != "bld_warehouse":
        crowns = -(-crowns * 9000 // 10000)
    if bld == "bld_warehouse" and "tech_civ_methods" in n.techs:
        crowns = -(-crowns * 9000 // 10000)
    if not charge(n, crowns, mats):
        return False, "afford"
    city.counts[bld] = city.count(bld) + 1
    n.fixed_other += book_value(crowns, mats)
    n.capex_total += crowns
    n.built[bld] += 1
    if bld == "bld_warehouse":
        n.expansions += 1
    return True, "ok"


def upgrade_infra(n, city, levels):
    target = city.infra + levels
    if target > INFRA_MAX or levels < 1:
        return False, "bound"
    discount = 1000 if "tech_civ_survey" in n.techs else 0
    cost = infra_cost(city.infra, levels, discount)
    if not charge(n, cost):
        return False, "afford"
    city.infra += levels
    city.infra_gross += cost
    n.capex_total += cost
    n.infra_levels_bought += levels
    return True, "ok"


def found_city(n):
    k = len(n.cities) + 1
    if k > MAX_CITIES:
        return False, "bound"
    if sum(c.infra for c in n.cities) < 100 * (k - 1):
        return False, "gate"
    cost = city_cost(k)
    if not charge(n, cost, {"steel": CITY_STEEL}):
        return False, "afford"
    c = CityState(f"City {k}", infra=10)
    n.cities.append(c)
    n.fixed_other += book_value(cost, {"steel": CITY_STEEL})
    n.capex_total += cost
    n.founded += 1
    return True, "ok"


def start_research(n, tech, labs_standing=None):
    if tech in n.techs or n.active_tech:
        return False, "busy"
    if any(p not in n.techs for p in TECH[tech][3]):
        return False, "prereq"
    standing = n.labs() if labs_standing is None else labs_standing
    if standing == 0:
        return False, "no_lab"
    if not charge(n, TECH[tech][2]):
        return False, "afford"
    n.research_crowns += TECH[tech][2]
    n.active_tech = tech
    n.progress = 0
    return True, "ok"


def complete_branches(n):
    return [b for b, ts in BRANCHES.items() if all(t in n.techs for t in ts)]


def commission(n, prg):
    branch, rp, crowns, mats, eff = PROGRAMMES[prg]
    if prg in n.programmes:
        return False, "held"
    if branch not in complete_branches(n):
        return False, "branch"
    if n.rp_pool < rp:
        return False, "rp"
    if not charge(n, crowns, mats):
        return False, "afford"
    n.rp_pool -= rp
    n.programmes.add(prg)
    n.programme_crowns += crowns
    if "warehouse" in eff:
        n.granary = True
    return True, "ok"


# ---------------------------------------------------------------------------
# Settlement
# ---------------------------------------------------------------------------
def settle(n, policy):
    """One two-hour boundary.  Policy keys:
       sell: 'reference' | 'none'; sell_goods: list; keep_food: int
       skip_civic_upkeep: bool; skip_lab_upkeep: bool; no_production: bool
       orders: list of (kind, ...) resolved at P4.1
       research: tech id or None (started at P4.1)
       programme: prg id or None
    """
    n.turn += 1
    log = {"turn": n.turn, "treasury_open": n.treasury}

    # P3.1 tax (hunger from previous turn applied once)
    gross_tax = n.population * TAX_BP * 10000 // 1_000_000_000
    tax = gross_tax * (10000 - n.hunger_bp) // 10000
    n.treasury += tax
    n.tax_total += tax
    log["tax"] = tax
    log["hunger_applied"] = n.hunger_bp
    n.hunger_bp = 0

    # P3.2 maintenance — one whole obligation per chain, extraction -> generation -> processing
    def pay_obligation(amount):
        if n.treasury >= amount:
            n.treasury -= amount
            n.maintenance_total += amount
            return True
        return False

    maintained = {}
    for res in RAW:
        cap_batches = n.facilities("bld_" + {"food": "farm", "coal": "coal_mine", "oil": "oil_well", "iron": "iron_mine",
                                              "bauxite": "bauxite_mine", "lead": "lead_mine", "uranium": "uranium_mine"}[res])
        ok = pay_obligation(cap_batches * EXTRACT[res][2])
        maintained[res] = ok
        if not ok and cap_batches:
            n.chain_unmaintained[res] += 1
    for cls in GEN:
        levels = n.facilities("bld_" + ("coal_plant" if cls == "coal" else "oil_plant" if cls == "oil" else "nuclear_plant"))
        ok = pay_obligation(levels * GEN[cls][3])
        maintained[cls] = ok
        if not ok and levels:
            n.chain_unmaintained[cls] += 1
    for chain in PROCESS:
        cap_batches = n.facilities("bld_" + {"gasoline": "refinery", "steel": "steel_mill",
                                             "aluminum": "smelter", "ammunition": "ammo_plant"}[chain])
        ok = pay_obligation(cap_batches * n.proc_maint())
        maintained[chain] = ok
        if not ok and cap_batches:
            n.chain_unmaintained[chain] += 1
    log["maintenance_paid"] = n.maintenance_total

    # P3.3 extraction, food first
    for res in RAW:
        if policy.get("no_production"):
            break
        batches = n.facilities("bld_" + {"food": "farm", "coal": "coal_mine", "oil": "oil_well", "iron": "iron_mine",
                                         "bauxite": "bauxite_mine", "lead": "lead_mine", "uranium": "uranium_mine"}[res])
        if batches == 0 or not maintained.get(res):
            continue
        y_eff = EXTRACT[res][0] + n.yield_bonus(res)
        v = n.extract_v(res)
        money_limit = n.treasury // v if v else batches
        space_limit = n.free_space() // y_eff if y_eff else batches
        run = min(batches, money_limit, space_limit)
        if run < batches and space_limit < batches:
            n.space_blocked[res] += 1
        if run:
            n.treasury -= run * v
            n.variable_total += run * v
            n.add_inv(res, run * y_eff)
            n.produced[res] += run * y_eff

    # P3.4 power — each level fails closed on fuel and variable cost
    supply = 0
    for cls in GEN:
        bld = "bld_" + ("coal_plant" if cls == "coal" else "oil_plant" if cls == "oil" else "nuclear_plant")
        gu, fuel, v, _m = GEN[cls]
        for _ in range(n.facilities(bld)):
            if not maintained.get(cls):
                break
            if n.treasury < v:
                break
            if any(n.inventory[f] < q for f, q in fuel.items()):
                break
            n.treasury -= v
            n.variable_total += v
            for f, q in fuel.items():
                n.inventory[f] -= q
            supply += gu
    demand = sum(n.facilities("bld_" + {"gasoline": "refinery", "steel": "steel_mill",
                                        "aluminum": "smelter", "ammunition": "ammo_plant"}[c]) * PROCESS[c][3]
                 for c in PROCESS if maintained.get(c) and not policy.get("no_production"))
    pct = 10000 if demand == 0 else min(10000, 10000 * supply // demand)
    used_gu = min(supply, demand)
    n.idle_generator_gu += supply - used_gu
    if demand and supply < demand:
        n.power_short_turns += 1
    log["power_pct"] = pct

    # P3.5 processing
    for chain in PROCESS:
        cap_batches = n.facilities("bld_" + {"gasoline": "refinery", "steel": "steel_mill",
                                             "aluminum": "smelter", "ammunition": "ammo_plant"}[chain])
        if cap_batches == 0 or not maintained.get(chain) or policy.get("no_production"):
            continue
        inputs, y, v, _gu, _m = PROCESS[chain]
        y_eff = y + n.yield_bonus(chain)
        avail = cap_batches * pct // 10000
        if avail == 0:
            continue
        input_limit = min(n.inventory[f] // q for f, q in inputs.items())
        money_limit = n.treasury // v if v else avail
        space_limit = n.free_space() // y_eff if y_eff else avail
        run = min(avail, input_limit, money_limit, space_limit)
        if run < avail:
            if input_limit < avail:
                pass
            if space_limit < avail:
                n.space_blocked[chain] += 1
        if run:
            for f, q in inputs.items():
                n.inventory[f] -= q * run
            n.treasury -= v * run
            n.variable_total += v * run
            n.add_inv(chain, y_eff * run)
            n.produced[chain] += y_eff * run

    # P3.6 civilian food
    demand_food = (n.population + 999) // 1000
    consumed = min(n.inventory["food"], demand_food)
    n.inventory["food"] -= consumed
    unmet = demand_food - consumed
    if demand_food:
        n.hunger_bp = min(3000, unmet * 3000 // demand_food)
    if unmet:
        n.food_short_turns += 1
    log["food_demand"] = demand_food
    log["unmet_food"] = unmet

    # P3.7 discretionary upkeep: 7(a) facility upkeep (labs then civic), 7(b) service cost
    labs = n.labs()
    civics = n.civics()
    lab_cost = 2 * labs
    civic_cost = 1 * civics
    n.lab_upkeep_paid = bool(labs == 0) or (not policy.get("skip_lab_upkeep") and n.treasury >= lab_cost)
    if labs and not n.lab_upkeep_paid:
        n.lab_idle_turns += 1
    elif labs:
        n.treasury -= lab_cost
        n.upkeep_total += lab_cost
    n.civic_upkeep_paid = bool(civics == 0) or (not policy.get("skip_civic_upkeep") and n.treasury >= civic_cost)
    if civics and not n.civic_upkeep_paid:
        n.civic_unfunded_turns += 1
    elif civics:
        n.treasury -= civic_cost
        n.upkeep_total += civic_cost
    service = gross_tax * SERVICE_SHARE_BP // 10000
    service_paid = service <= n.treasury
    if service_paid:
        n.treasury -= service
        n.service_total += service
    log["service_paid"] = service if service_paid else 0

    # P3.8 population growth (B-06 F-PD-001/002, approval held at the neutral 55)
    housing_now = n.housing_growth()
    headroom = max(0, housing_now - n.population)
    crowding_bp = 0 if n.population <= housing_now else min(10000, (n.population - housing_now) * 10000 // n.population)
    growth_bp = 50 + (APPROVAL - 55) // 2 + min(15, headroom * 100 // n.population if n.population else 0) \
        - n.hunger_bp // 30 - crowding_bp // 100
    growth_bp = max(-100, min(100, growth_bp))
    natural = n.population + n.population * growth_bp // 10000
    if n.population > housing_now:
        raw = n.population - max(-(-(n.population - housing_now) // 10), max(0, n.population - natural))
    else:
        raw = min(natural, housing_now)
    n.population = max(POP_FLOOR, raw)
    log["population"] = n.population
    log["crowding_bp"] = crowding_bp

    labs_before_p41 = labs
    # P4.1 construction (one action per city; founding one per nation)
    for order in policy.get("orders", []):
        kind = order[0]
        if kind == "found":
            found_city(n)
        elif kind == "infra":
            _, city_name, levels = order
            city = next((c for c in n.cities if c.name == city_name), None)
            if city:
                upgrade_infra(n, city, levels)
        elif kind == "build":
            _, city_name, bld = order
            city = next((c for c in n.cities if c.name == city_name), None)
            if city:
                build_order(n, city, bld)
    if policy.get("research"):
        start_research(n, policy["research"], labs_standing=labs_before_p41)
    if policy.get("programme"):
        commission(n, policy["programme"])

    # P4.2 research progress (labs present before P4.1 are the ones that generate)
    rp = 0 if (not n.lab_upkeep_paid) else labs_before_p41
    if n.active_tech:
        need = max(0, TECH[n.active_tech][1] - n.progress)
        applied = min(rp, need)
        n.progress += applied
        n.rp_pool += rp - applied
        if n.progress >= TECH[n.active_tech][1]:
            n.techs.add(n.active_tech)
            n.active_tech = None
            n.progress = 0
    else:
        n.rp_pool += rp
    log["rp"] = rp

    # P4.3 labelled demand scenario: sell at reference price
    if policy.get("sell") == "reference":
        keep_map = policy.get("keep", {})
        for g in policy.get("sell_goods", MANUFACTURED):
            keep = keep_map.get(g, policy.get("keep_food", 0) if g == "food" else 0)
            qty = max(0, n.inventory[g] - keep)
            if qty > 0:
                n.inventory[g] -= qty
                n.treasury += qty * PRICE[g]
                n.sales_total += qty * PRICE[g]
                n.sold[g] += qty

    n.warehouse_peak = max(n.warehouse_peak, n.stock())
    log["treasury"] = n.treasury
    log["wealth"] = n.wealth()
    log["stock"] = n.stock()
    log["population"] = n.population
    log["techs"] = len(n.techs)
    return log


# ---------------------------------------------------------------------------
# Scenario investment helpers
# ---------------------------------------------------------------------------
def try_build(n, city, bld):
    return build_order(n, city, bld)[0]


def try_infra(n, city, levels):
    return upgrade_infra(n, city, levels)[0]


def affordable(n, crowns, mats=None):
    mats = mats or {}
    return n.treasury >= crowns and all(n.inventory[m] >= q for m, q in mats.items())


def greedy_planner(n):
    """A conservative balanced planner used by expansion scenarios."""
    # one order per city; priority: food, power, steel chain, housing, research, city growth
    orders = []
    for c in n.cities:
        free = c.dc_capacity(n.dc_bonus()) - c.dc_used()
        if free >= 1 and affordable(n, 120, {"steel": 5}) and c.count("bld_farm") < 6 and \
                n.facilities("bld_farm") * (20 + n.yield_bonus("food")) < (n.population // 1000) + 40:
            orders.append(("build", c.name, "bld_farm"))
            continue
        if free >= 2 and affordable(n, 280, {"steel": 10}) and \
                sum(n.facilities(b) for b in ("bld_coal_plant", "bld_oil_plant", "bld_nuclear_plant")) * 6 < \
                2 * n.facilities("bld_refinery") + 3 * n.facilities("bld_steel_mill") + 4 * n.facilities("bld_smelter") + 12:
            orders.append(("build", c.name, "bld_coal_plant"))
            continue
        if free >= 2 and affordable(n, 380, {"steel": 15}) and c.count("bld_steel_mill") < 2 and \
                n.inventory["iron"] + 10 * n.facilities("bld_iron_mine") >= 10:
            orders.append(("build", c.name, "bld_steel_mill"))
            continue
        if free >= 1 and affordable(n, 180, {"steel": 5}) and c.count("bld_iron_mine") < 4 and \
                n.facilities("bld_steel_mill") * 10 > n.facilities("bld_iron_mine") * 10:
            orders.append(("build", c.name, "bld_iron_mine"))
            continue
        if free >= 1 and affordable(n, 160, {"steel": 5}) and c.count("bld_coal_mine") < 4 and \
                (n.facilities("bld_steel_mill") * 6 + 6 * sum(n.facilities(b) for b in ("bld_coal_plant",)) > n.facilities("bld_coal_mine") * 10):
            orders.append(("build", c.name, "bld_coal_mine"))
            continue
        if free >= 3 and affordable(n, 500, {"steel": 20}) and n.labs() < 2:
            orders.append(("build", c.name, "bld_lab"))
            continue
        if free >= 2 and affordable(n, 300, {"steel": 10}) and c.count("bld_civic") < 2 and \
                n.housing_growth() < n.population + 15000:
            orders.append(("build", c.name, "bld_civic"))
            continue
        if free >= 1 and affordable(n, 220, {"steel": 5}) and c.count("bld_oil_well") < 3 and \
                n.facilities("bld_refinery") * 10 > n.facilities("bld_oil_well") * 8:
            orders.append(("build", c.name, "bld_oil_well"))
            continue
    return orders


def expansion_policy(n, infra_first=False):
    """Found cities as soon as the gate and cost allow; otherwise upgrade the capital/cheapest city."""
    orders = greedy_planner(n)
    occupied = {o[1] for o in orders if o[0] != "found"}
    # founding
    k = len(n.cities) + 1
    if k <= MAX_CITIES and sum(c.infra for c in n.cities) >= 100 * (k - 1) and \
            affordable(n, city_cost(k), {"steel": CITY_STEEL}) and n.treasury > city_cost(k) + 300:
        orders.append(("found",))
    # infrastructure: buy 10 levels in a city without an order
    for c in sorted(n.cities, key=lambda x: x.infra):
        if c.name in occupied:
            continue
        target = min(c.infra + 10, INFRA_MAX)
        nlev = target - c.infra
        if nlev <= 0:
            continue
        cost = infra_cost(c.infra, nlev, 1000 if "tech_civ_survey" in n.techs else 0)
        if n.treasury >= cost + (city_cost(len(n.cities) + 1) if len(n.cities) < MAX_CITIES else 0) // 2:
            orders.append(("infra", c.name, nlev))
        break
    return orders


def research_choice(n, order):
    for t in order:
        if t in n.techs or t == n.active_tech:
            continue
        if all(p in n.techs for p in TECH[t][3]):
            return t
    return None


# ---------------------------------------------------------------------------
# Scenario definitions
# ---------------------------------------------------------------------------
def scenario_baseline(turns, sell=False):
    n = standard_start()

    def policy_fn(state, t):
        return {"sell": "reference" if sell else "none",
                "sell_goods": ["food"], "keep_food": 120}
    return n, policy_fn


def scenario_produce_sell_manufactured(turns):
    n = standard_start()

    def policy_fn(state, t):
        return {"sell": "reference", "sell_goods": ["gasoline", "steel", "aluminum", "ammunition"]}
    return n, policy_fn


def scenario_infra_first(turns):
    n = standard_start()

    def policy_fn(state, t):
        orders = []
        c = n.cities[0]
        if c.infra < INFRA_MAX and affordable(n, infra_cost(c.infra, 10, 1000 if "tech_civ_survey" in n.techs else 0)):
            orders.append(("infra", c.name, min(10, INFRA_MAX - c.infra)))
        return {"sell": "none", "orders": orders}
    return n, policy_fn


def city_growth_planner(n):
    """Expand by founding whenever the gate and cost allow; otherwise grow infrastructure.
    Food capacity is checked first so expansion is not measured through a famine."""
    orders = []
    demand = (n.population + 999) // 1000
    food_capacity = n.facilities("bld_farm") * (20 + n.yield_bonus("food"))
    if food_capacity < demand + 15 and n.inventory["steel"] >= 25:
        for c in n.cities:
            if c.dc_capacity(n.dc_bonus()) - c.dc_used() >= 1 and affordable(n, 120, {"steel": 5}):
                orders.append(("build", c.name, "bld_farm"))
                break
        return orders
    k = len(n.cities) + 1
    cost = city_cost(k) if k <= MAX_CITIES else 0
    if k <= MAX_CITIES and sum(c.infra for c in n.cities) >= 100 * (k - 1) and             affordable(n, cost, {"steel": CITY_STEEL}) and n.treasury > cost + 400:
        orders.append(("found",))
        return orders
    c = min(n.cities, key=lambda x: x.infra)
    nlev = min(10, INFRA_MAX - c.infra)
    if nlev > 0:
        price = infra_cost(c.infra, nlev, 1000 if "tech_civ_survey" in n.techs else 0)
        reserve = cost if k <= MAX_CITIES else 0
        if n.treasury >= price + reserve + 200:
            orders.append(("infra", c.name, nlev))
    return orders


def scenario_city_expansion(turns):
    n = standard_start()

    def policy_fn(state, t):
        return {"sell": "none", "orders": city_growth_planner(n)}
    return n, policy_fn


def scenario_steel_focus(turns, sell=True):
    """Build a self-contained 4-batch steel package, then idle."""
    n = standard_start()

    def policy_fn(state, t):
        orders = []
        capital = n.cities[0]
        # one order per turn at the capital
        plan = []
        if capital.infra < 200:
            plan.append(("infra", "Capital", 10))
        elif capital.count("bld_steel_mill") < 1:
            plan.append(("build", "Capital", "bld_steel_mill"))
        elif capital.count("bld_coal_mine") < 4:
            plan.append(("build", "Capital", "bld_coal_mine"))
        elif capital.count("bld_iron_mine") < 4:
            plan.append(("build", "Capital", "bld_iron_mine"))
        elif capital.count("bld_steel_mill") < 4:
            plan.append(("build", "Capital", "bld_steel_mill"))
        elif sum(capital.count(b) for b in ("bld_coal_plant",)) < 2:
            plan.append(("build", "Capital", "bld_coal_plant"))
        elif n.facilities("bld_farm") < 4:
            plan.append(("build", "Capital", "bld_farm"))
        orders.extend(plan)
        complete = capital.count("bld_steel_mill") >= 4 and capital.count("bld_iron_mine") >= 4             and capital.count("bld_coal_mine") >= 4 and capital.count("bld_coal_plant") >= 2
        return {"sell": "reference" if sell else "none",
                "sell_goods": ["steel", "gasoline", "coal"],
                "keep": {"steel": 0 if complete else 100, "gasoline": 20, "coal": 80},
                "orders": orders}
    return n, policy_fn


def scenario_aluminum_focus(turns, sell=True):
    n = standard_start()

    def policy_fn(state, t):
        orders = []
        capital = n.cities[0]
        if capital.infra < 250:
            orders.append(("infra", "Capital", 10))
        elif n.facilities("bld_farm") < 4:
            orders.append(("build", "Capital", "bld_farm"))
        elif capital.count("bld_coal_mine") < 4:
            orders.append(("build", "Capital", "bld_coal_mine"))
        elif capital.count("bld_bauxite_mine") < 6:
            orders.append(("build", "Capital", "bld_bauxite_mine"))
        elif capital.count("bld_coal_plant") < 3:
            orders.append(("build", "Capital", "bld_coal_plant"))
        # A smelter order is rejected until tech_ind_chem is researched; this scenario
        # deliberately measures the un-researched path, so the order fails and is logged.
        return {"sell": "reference" if sell else "none",
                "sell_goods": ["aluminum", "gasoline", "coal"],
                "keep": {"steel": 140, "gasoline": 20, "coal": 80},
                "orders": orders}
    return n, policy_fn


def scenario_research_first(turns, labs=2):
    n = standard_start()

    def policy_fn(state, t):
        orders = []
        capital = n.cities[0]
        if n.labs() < labs:
            if capital.dc_capacity() - capital.dc_used() >= 3:
                orders.append(("build", "Capital", "bld_lab"))
            else:
                orders.append(("infra", "Capital", 10))
        tech = research_choice(n, ["tech_agri_rotation", "tech_ext_metals", "tech_ind_heat",
                                   "tech_civ_survey", "tech_ind_chem", "tech_ind_ordnance",
                                   "tech_civ_methods", "tech_agri_mechanisation",
                                   "tech_ext_coal", "tech_ext_oil", "tech_ext_deep",
                                   "tech_nuclear_engineering"])
        return {"sell": "none", "orders": orders, "research": tech}
    return n, policy_fn


def scenario_research_prepared(turns, labs):
    """Prepared mid-game research state: `labs` institutes spread over cities."""
    cities = []
    remaining = labs
    i = 1
    while remaining > 0:
        here = min(2, remaining)
        cities.append(CityState(f"Research City {i}", infra=100, counts={
            "bld_lab": here, "bld_farm": 3, "bld_coal_mine": 2, "bld_coal_plant": 1}))
        remaining -= here
        i += 1
    inv = {"food": 400, "coal": 150, "oil": 40, "iron": 40, "bauxite": 20,
           "lead": 10, "uranium": 0, "gasoline": 30, "ammunition": 0,
           "steel": 120, "aluminum": 20}
    n = Nation(f"Research x{labs}", 4000, 100000, inv, cities)

    def policy_fn(state, t):
        tech = research_choice(n, ["tech_agri_rotation", "tech_agri_mechanisation",
                                   "tech_ext_coal", "tech_ext_oil", "tech_ext_metals", "tech_ext_deep",
                                   "tech_ind_heat", "tech_ind_chem", "tech_ind_ordnance",
                                   "tech_civ_survey", "tech_civ_methods", "tech_nuclear_engineering"])
        return {"sell": "none", "research": tech}
    return n, policy_fn


def scenario_excess_labs(turns):
    """Prepared mid-game state with 12 labs and the full tree to research."""
    cities = [CityState(f"Lab City {i}", infra=100, counts={"bld_lab": 2,
                                                             "bld_farm": 3, "bld_coal_mine": 2,
                                                             "bld_coal_plant": 1})
              for i in range(1, 7)]
    inv = {"food": 500, "coal": 200, "oil": 60, "iron": 60, "bauxite": 40,
           "lead": 20, "uranium": 0, "gasoline": 40, "ammunition": 0,
           "steel": 200, "aluminum": 50}
    n = Nation("Excess Labs", 5000, 150000, inv, cities, fixed_other=0)

    def policy_fn(state, t):
        tech = research_choice(n, ["tech_agri_rotation", "tech_agri_mechanisation",
                                   "tech_ext_coal", "tech_ext_oil", "tech_ext_metals", "tech_ext_deep",
                                   "tech_ind_heat", "tech_ind_chem", "tech_ind_ordnance",
                                   "tech_civ_survey", "tech_civ_methods", "tech_nuclear_engineering"])
        return {"sell": "none", "research": tech}
    return n, policy_fn


def scenario_excess_facilities(turns):
    """Prepared overbuilt state: 8 farms, 8 coal, 8 iron, 4 refineries, 2 steel mills, 1 generator level."""
    capital = CityState("Overbuilt", infra=500, counts={
        "bld_farm": 8, "bld_coal_mine": 8, "bld_iron_mine": 8,
        "bld_refinery": 4, "bld_steel_mill": 2, "bld_coal_plant": 1})
    inv = {"food": 200, "coal": 100, "oil": 20, "iron": 40, "bauxite": 0,
           "lead": 0, "uranium": 0, "gasoline": 0, "ammunition": 0,
           "steel": 50, "aluminum": 0}
    n = Nation("Overbuilt", 3000, 50000, inv, [capital])

    def policy_fn(state, t):
        return {"sell": "none"}
    return n, policy_fn


def scenario_underused_refining(turns):
    """4 refineries, 1 oil well: input-starved, maintenance paid on capacity."""
    inv = {"food": 300, "coal": 100, "oil": 0, "iron": 30, "bauxite": 20,
           "lead": 10, "uranium": 0, "gasoline": 0, "ammunition": 0,
           "steel": 30, "aluminum": 0}
    capital = CityState("Refinery Stack", infra=100, counts={
        "bld_farm": 3, "bld_coal_mine": 2,
        "bld_refinery": 4, "bld_coal_plant": 1})
    n = Nation("Underused", 2000, 50000, inv, [capital])

    def policy_fn(state, t):
        return {"sell": "reference", "sell_goods": ["gasoline"]}
    return n, policy_fn


def scenario_power_overbuild(turns):
    capital = CityState("Power Stack", infra=150, counts={
        "bld_farm": 3, "bld_coal_mine": 2, "bld_oil_well": 1, "bld_iron_mine": 1,
        "bld_refinery": 1, "bld_coal_plant": 6})
    inv = {"food": 120, "coal": 60, "oil": 30, "iron": 30, "bauxite": 20,
           "lead": 10, "uranium": 0, "gasoline": 20, "ammunition": 0,
           "steel": 20, "aluminum": 0}
    n = Nation("Power Overbuild", 1500, 50000, inv, [capital])

    def policy_fn(state, t):
        return {"sell": "none"}
    return n, policy_fn


def scenario_housing_shortage(turns):
    """Prepared city with 150,000 population, housing from 3 civics; upkeep stops at turn 4."""
    capital = CityState("Crowded", infra=300, counts={"bld_farm": 8, "bld_coal_mine": 2,
                                                      "bld_coal_plant": 1, "bld_civic": 3,
                                                      "bld_lab": 0})
    inv = {"food": 2000, "coal": 200, "oil": 30, "iron": 30, "bauxite": 20,
           "lead": 10, "uranium": 0, "gasoline": 40, "ammunition": 0,
           "steel": 100, "aluminum": 0}
    n = Nation("Crowded", 3000, 150000, inv, [capital])

    def policy_fn(state, t):
        return {"sell": "none", "skip_civic_upkeep": t >= 4}
    return n, policy_fn


def scenario_food_shortage(turns):
    """No farms; existing stock runs out and hunger suppresses tax."""
    capital = CityState("Starving", infra=50, counts={
        "bld_coal_mine": 2, "bld_oil_well": 1, "bld_iron_mine": 1,
        "bld_refinery": 1, "bld_coal_plant": 1})
    inv = {"food": 60, "coal": 60, "oil": 30, "iron": 30, "bauxite": 20,
           "lead": 10, "uranium": 0, "gasoline": 20, "ammunition": 0,
           "steel": 20, "aluminum": 0}
    n = Nation("Starving", 1500, 50000, inv, [capital])

    def policy_fn(state, t):
        return {"sell": "none"}
    return n, policy_fn


def scenario_low_treasury(turns):
    """Prepared over-extended industry: 6 cities, 60 extraction and 30 processing
    batches, population still 50,000.  Tax cannot carry the obligations."""
    cities = []
    for i in range(1, 7):
        counts = {"bld_farm": 3, "bld_coal_mine": 2, "bld_coal_plant": 1, "bld_refinery": 1}
        if i <= 3:
            counts.update({"bld_iron_mine": 8, "bld_lead_mine": 8, "bld_steel_mill": 4,
                           "bld_ammo_plant": 4, "bld_smelter": 2})
        cities.append(CityState(f"Wide City {i}", infra=400 if i <= 3 else 100, counts=counts))
    inv = {"food": 300, "coal": 60, "oil": 20, "iron": 40, "bauxite": 10,
           "lead": 10, "uranium": 0, "gasoline": 0, "ammunition": 0,
           "steel": 40, "aluminum": 0}
    n = Nation("Overextended", 1000, 50000, inv, cities)

    def policy_fn(state, t):
        return {"sell": "none"}
    return n, policy_fn


def scenario_no_demand(turns):
    """4-batch steel package with no buyer: inventory accumulates, cash drains."""
    return scenario_steel_focus(turns, sell=False)


def scenario_balanced(turns):
    n = standard_start()

    def policy_fn(state, t):
        orders = greedy_planner(n)
        tech = research_choice(n, ["tech_agri_rotation", "tech_ind_heat", "tech_civ_survey",
                                   "tech_ext_metals", "tech_agri_mechanisation",
                                   "tech_civ_methods", "tech_ind_chem", "tech_ind_ordnance",
                                   "tech_ext_coal", "tech_ext_oil", "tech_ext_deep",
                                   "tech_nuclear_engineering"])
        return {"sell": "reference", "sell_goods": ["food", "steel", "gasoline"],
                "keep": {"food": max(200, n.population // 1000 * 3), "steel": 80, "gasoline": 20},
                "orders": orders, "research": tech}
    return n, policy_fn


def scenario_two_nations(turns, strategy):
    """Steel vs aluminum on identical prepared states (tech_ind_chem granted to both)."""
    capital = CityState("Industrial", infra=250, counts={"bld_farm": 4, "bld_coal_mine": 4})
    inv = {"food": 400, "coal": 200, "oil": 30, "iron": 100, "bauxite": 100,
           "lead": 10, "uranium": 0, "gasoline": 20, "ammunition": 0,
           "steel": 200, "aluminum": 50}
    n = Nation(strategy, 6000, 50000, inv, [capital])
    n.techs.add("tech_ind_heat")
    n.techs.add("tech_ind_chem")

    def policy_fn(state, t):
        orders = []
        c = n.cities[0]
        if strategy == "steel":
            if c.count("bld_iron_mine") < 4:
                orders.append(("build", c.name, "bld_iron_mine"))
            elif c.count("bld_steel_mill") < 4:
                orders.append(("build", c.name, "bld_steel_mill"))
            elif c.count("bld_coal_plant") < 2:
                orders.append(("build", c.name, "bld_coal_plant"))
        else:
            if c.count("bld_bauxite_mine") < 6:
                orders.append(("build", c.name, "bld_bauxite_mine"))
            elif c.count("bld_smelter") < 4:
                orders.append(("build", c.name, "bld_smelter"))
            elif c.count("bld_coal_plant") < 3:
                orders.append(("build", c.name, "bld_coal_plant"))
        target = strategy if strategy == "steel" else "aluminum"
        complete = (c.count("bld_steel_mill") >= 4 if strategy == "steel" else c.count("bld_smelter") >= 4)
        return {"sell": "reference",
                "sell_goods": [target, "food", "coal", "gasoline", "ammunition"],
                "keep": {"steel": 0 if complete else 140, "food": 300, "coal": 60,
                         "gasoline": 20, "aluminum": 0},
                "orders": orders}
    return n, policy_fn


def scenario_menu(kind):
    """Comparable snapshot: the capital is already at 100 (the founding gate met) and the
    nation holds 1,500 crowns; the 100 opening levels are a zero-cost opening lot."""
    n = standard_start()
    n.cities[0].infra = 100
    n.treasury = 1500

    def policy_fn(state, t):
        orders = []
        gold = n.cities[0]
        if t == 1:
            if kind == "city":
                orders.append(("found",))
            elif kind == "lab":
                orders.append(("build", gold.name, "bld_lab"))
            elif kind == "farms":
                orders.append(("build", gold.name, "bld_farm"))
            elif kind == "infra":
                orders.append(("infra", gold.name, 50))
        elif kind == "farms" and t <= 4 and n.inventory["steel"] >= 5:
            orders.append(("build", gold.name, "bld_farm"))
        research = "tech_agri_rotation" if kind == "lab" else None
        return {"sell": "reference", "sell_goods": ["food", "coal", "gasoline"],
                "keep": {"food": 400, "coal": 100, "gasoline": 20},
                "orders": orders, "research": research}
    return n, policy_fn


SCENARIOS = {
    "S01 baseline (no sales)": lambda t: scenario_baseline(t, sell=False),
    "S02 baseline + food sales": lambda t: scenario_baseline(t, sell=True),
    "S03 baseline + manufactured sales": scenario_produce_sell_manufactured,
    "S04 infrastructure-first": scenario_infra_first,
    "S05 rapid city expansion": scenario_city_expansion,
    "S06 steel focus (reference sales)": lambda t: scenario_steel_focus(t, sell=True),
    "S07 steel focus (no demand)": lambda t: scenario_steel_focus(t, sell=False),
    "S08 aluminum-first attempt (tech-gated)": lambda t: scenario_aluminum_focus(t, sell=True),
    "S09 research-first (2 labs)": lambda t: scenario_research_first(t, labs=2),
    "S10 research-first (4 labs, prepared)": lambda t: scenario_research_prepared(t, labs=4),
    "S11 excessive institutes (12 labs)": scenario_excess_labs,
    "S12 excessive facilities (overbuilt)": scenario_excess_facilities,
    "S13 underused refining capacity": scenario_underused_refining,
    "S14 power overinvestment": scenario_power_overbuild,
    "S15 housing shortage (civic unfunded)": scenario_housing_shortage,
    "S16 food shortage": scenario_food_shortage,
    "S17 insufficient treasury": scenario_low_treasury,
    "S18 balanced mixed development": scenario_balanced,
    "S19 steel vs aluminum — steel": lambda t: scenario_two_nations(t, "steel"),
    "S20 steel vs aluminum — aluminum": lambda t: scenario_two_nations(t, "aluminum"),
    "S21 menu — second city": lambda t: scenario_menu("city"),
    "S22 menu — research institute": lambda t: scenario_menu("lab"),
    "S23 menu — four farms": lambda t: scenario_menu("farms"),
    "S24 menu — infrastructure 100-150": lambda t: scenario_menu("infra"),
}

HORIZONS = (10, 30, 60, 120)


def run(name, turns):
    n, policy_fn = SCENARIOS[name](turns)
    series = []
    for t in range(1, turns + 1):
        series.append(settle(n, policy_fn(n, t)))
    return n, series


def summary(n, series, horizon):
    snap = next((s for s in series if s["turn"] == horizon), None)
    return {
        "scenario": n.name,
        "horizon": horizon,
        "treasury": snap["treasury"] if snap else None,
        "inventory_units": snap["stock"] if snap else None,
        "inventory_book": sum(q * PRICE[r] for r, q in n.inventory.items()) if horizon == n.turn else None,
        "fixed_assets": n.fixed_assets(),
        "wealth": snap["wealth"] if snap else None,
        "population": snap["population"] if snap else None,
        "techs": snap["techs"] if snap else None,
        "tax_total": n.tax_total,
        "sales_total": n.sales_total,
        "variable_total": n.variable_total,
        "maintenance_total": n.maintenance_total,
        "upkeep_total": n.upkeep_total,
        "service_total": n.service_total,
        "capex_total": n.capex_total,
        "research_crowns": n.research_crowns,
        "cities": len(n.cities),
        "founded": n.founded,
        "infra_bought": n.infra_levels_bought,
        "food_short_turns": n.food_short_turns,
        "power_short_turns": n.power_short_turns,
        "lab_idle_turns": n.lab_idle_turns,
        "civic_unfunded_turns": n.civic_unfunded_turns,
        "warehouse_peak": n.warehouse_peak,
        "produced": dict(n.produced),
        "sold": dict(n.sold),
        "built": {k: v for k, v in n.built.items() if v},
    }


def run_all():
    out = {}
    for name in SCENARIOS:
        # run to the longest horizon once; snapshot at each horizon
        n, series = run(name, max(HORIZONS))
        rows = {}
        for h in HORIZONS:
            if h <= n.turn:
                snap = next(s for s in series if s["turn"] == h)
                # reconstruct per-horizon cumulative totals by replaying to h
                n_h, series_h = run(name, h)
                rows[h] = summary(n_h, series_h, h)
        out[name] = rows
    return out


def invariants(n):
    """Identity checks that must hold for every scenario."""
    problems = []
    if n.treasury < 0:
        problems.append("negative treasury")
    if n.stock() > n.warehouse_capacity():
        problems.append("warehouse overflow")
    for c in n.cities:
        if c.dc_used() > c.dc_capacity(n.dc_bonus()):
            problems.append(f"capacity overdraw {c.name}")
        if c.infra < INFRA_MIN or c.infra > INFRA_MAX:
            problems.append(f"infrastructure bound {c.name}")
    if n.population < POP_FLOOR:
        problems.append("population floor")
    return problems


def main(argv):
    horizons = [int(x) for x in argv[1:]] if len(argv) > 1 else list(HORIZONS)
    results = {}
    for name in SCENARIOS:
        n, series = run(name, max(horizons))
        problems = invariants(n)
        rows = {}
        for h in horizons:
            n_h, series_h = run(name, h)
            rows[h] = summary(n_h, series_h, h)
            rows[h]["invariants"] = invariants(n_h)
        results[name] = rows
        line = f"{name:42s}"
        for h in horizons:
            r = rows[h]
            line += f" | T{h}: treasury={r['treasury']:>8} stock={r['inventory_units']:>6} wealth={r['wealth']:>9} techs={r['techs']}"
        print(line)
        if problems:
            print("   INVARIANT PROBLEMS:", problems)
    with open("14C_simulation_results.json", "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print("\nWrote 14C_simulation_results.json")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
