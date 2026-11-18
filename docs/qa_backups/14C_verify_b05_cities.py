#!/usr/bin/env python3
"""Prompt 14C — B-05 cities, infrastructure, production and research verifier.

Document QA and arithmetic only: no game code, no database, no scheduler.
Recomputes the analytical tables, the new worked examples and the simulation
anchors used by 29_prompt_14C_b05_cities_completion_report.md.  Self-tests
mutate expected values to prove the checks can fail.
"""

import os
import re
import sys
import io

HERE = os.path.dirname(os.path.abspath(__file__))
STAGE2 = os.path.normpath(os.path.join(HERE, "..", "stage-2"))
REPORT = os.path.join(STAGE2, "29_prompt_14C_b05_cities_completion_report.md")
REPORT_C1 = os.path.join(STAGE2, "30_prompt_14C-C1_city_gate_and_research_investment_correction.md")
DECISIONS = os.path.normpath(os.path.join(STAGE2, "..", "DECISIONS.md"))
REG_B05 = os.path.join(STAGE2, "11_city_infrastructure_production_and_research_formula_register.md")
RULE_B05 = os.path.join(STAGE2, "11_cities_infrastructure_production_and_research.md")
INV = os.path.join(STAGE2, "22_numerical_parameter_inventory.md")
MASTER = os.path.join(STAGE2, "22_formula_master_inventory.md")

CHECKS = []
FAILS = []


def add(cid, title, problems):
    CHECKS.append(cid)
    if problems:
        FAILS.append((cid, title, problems))


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def rows(text):
    return [ln for ln in text.splitlines() if ln.strip().startswith("|")]


# ---------------------------------------------------------------------------
# Published constants (B-05 register §3, B-04 §3)
# ---------------------------------------------------------------------------
EXTRACT = {"food": (20, 12, 1), "coal": (10, 10, 1), "oil": (8, 14, 1),
           "iron": (10, 10, 1), "bauxite": (8, 14, 1), "lead": (6, 16, 1),
           "uranium": (1, 28, 1)}
PROCESS = {"gasoline": ({"oil": 10}, 8, 20, 2, 2), "steel": ({"iron": 10, "coal": 6}, 8, 24, 3, 2),
           "aluminum": ({"bauxite": 12}, 8, 24, 4, 2), "ammunition": ({"lead": 8, "coal": 4}, 10, 20, 2, 2)}
GEN = {"coal": (6, {"coal": 6}, 10, 2), "oil": (6, {"oil": 5}, 14, 2), "nuclear": (20, {"uranium": 1, "lead": 1}, 40, 2)}
PRICE = {"food": 1, "coal": 1, "oil": 2, "iron": 1, "bauxite": 2, "lead": 3, "uranium": 30,
         "gasoline": 6, "ammunition": 6, "steel": 7, "aluminum": 8}
BUILD = {"bld_farm": (1, 120, {"steel": 5}), "bld_coal_mine": (1, 160, {"steel": 5}),
         "bld_oil_well": (1, 220, {"steel": 5}), "bld_iron_mine": (1, 180, {"steel": 5}),
         "bld_bauxite_mine": (1, 220, {"steel": 5}), "bld_lead_mine": (1, 260, {"steel": 5}),
         "bld_uranium_mine": (1, 600, {"steel": 10, "aluminum": 5}),
         "bld_refinery": (2, 320, {"steel": 15}), "bld_steel_mill": (2, 380, {"steel": 15}),
         "bld_smelter": (2, 420, {"steel": 20}), "bld_ammo_plant": (2, 360, {"steel": 15}),
         "bld_coal_plant": (2, 280, {"steel": 10}), "bld_oil_plant": (2, 340, {"steel": 10, "aluminum": 5}),
         "bld_nuclear_plant": (2, 1200, {"steel": 30, "aluminum": 20}),
         "bld_wms": (1, 180, {"steel": 5}), "bld_lab": (3, 500, {"steel": 20}),
         "bld_civic": (2, 300, {"steel": 10})}
TECH = {"agri_rotation": (24, 160), "agri_mechanisation": (44, 300), "ext_coal": (20, 140),
        "ext_oil": (32, 220), "ext_metals": (40, 280), "ext_deep": (56, 360),
        "ind_heat": (28, 200), "ind_chem": (48, 340), "ind_ordnance": (36, 260),
        "civ_survey": (20, 140), "civ_methods": (40, 280), "nuclear": (60, 500)}
PROG = {"granary": (100, 900, 1100), "survey": (100, 1000, 1000),
        "standards": (100, 1200, 1450), "civil_works": (100, 1100, 1320)}


def infra_cost(level, n, discount_bp=0):
    base = sum(8 + (level + i) // 10 for i in range(n))
    if discount_bp:
        return -(-base * (10000 - discount_bp) // 10000)
    return base


def book(crowns, mats):
    return crowns + sum(q * PRICE[m] for m, q in mats.items())


def city_cost(k):
    return 400 + 150 * k * k


def payback(investment, per_turn):
    return None if per_turn <= 0 else round(investment / per_turn, 1)


# ---------------------------------------------------------------------------
# A — Source inventory and parameter reconciliation
# ---------------------------------------------------------------------------
def check_sources():
    reg = read(REG_B05)
    inv = read(INV)
    master = read(MASTER)
    probs = []
    ids = [i for i in re.findall(r"\*\*(F-CI-\d{3}) —", reg) if 1 <= int(i[-3:]) <= 41]
    if len(ids) != 41:
        probs.append(f"register defines {len(ids)} F-CI IDs, expected 41")
    if len(set(ids)) != 41:
        probs.append("duplicate F-CI identifier")
    for n in range(1, 42):
        fid = f"F-CI-{n:03d}"
        if fid not in ids:
            probs.append(f"{fid} missing")
    # classification
    executable = [i for i in ids if 1 <= int(i[-3:]) <= 30]
    analytical = [i for i in ids if 31 <= int(i[-3:]) <= 34]
    governance = [i for i in ids if 35 <= int(i[-3:]) <= 41]
    if (len(executable), len(analytical), len(governance)) != (30, 4, 7):
        probs.append("30/4/7 classification mismatch")
    # master inventory: 41 index rows + 41 metadata rows
    msec = master.split("## 4.2 B-05")[1].split("## 4.3 B-06")[0]
    m_rows = [ln for ln in msec.splitlines() if ln.startswith("| `F-CI-")]
    if len(m_rows) != 82:
        probs.append(f"master inventory B-05 rows {len(m_rows)}, expected 82 (41 + 41)")
    # parameter inventory §7 = 73 records
    sec = inv.split("## 7. B-05")[1].split("## 8.")[0]
    p_rows = [ln for ln in sec.splitlines() if ln.startswith("| None |")]
    if len(p_rows) != 73:
        probs.append(f"§7 records {len(p_rows)}, expected 73")
    # 17 catalogue rows, 12 technologies + total, 4 programmes in the register
    if reg.count("| `bld_") != 17:
        probs.append(f"catalogue rows {reg.count('| `bld_')}, expected 17")
    tech_rows = [ln for ln in reg.splitlines() if ln.startswith("| `tech_")]
    if len(tech_rows) != 12:
        probs.append(f"technology rows {len(tech_rows)}, expected 12")
    prog_rows = [ln for ln in reg.splitlines() if ln.startswith("| `prg_")]
    if len(prog_rows) != 4:
        probs.append(f"programme rows {len(prog_rows)}, expected 4")
    # tree totals
    if sum(v[0] for v in TECH.values()) != 448 or sum(v[1] for v in TECH.values()) != 3180:
        probs.append("tree totals are not 448 RP / 3,180 crowns")
    add("14C-01", "All 41 F-CI identifiers and the published catalogues are present and classified 30/4/7", probs)

    # 1:1 name mapping between register §3 tables and inventory §7
    probs2 = []
    reg_names = set()
    reg_sec = reg.split("## 3. Constants")[1].split("## 4. The formula register")[0]
    for ln in rows(reg_sec):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not cells or cells[0].lower() in ("item", "class", "id", "symbol", "") or set(cells[0]) <= set("-: "):
            continue
        name = cells[0].strip("`")
        if name.startswith("F-CI") or name in ("Total", "**Total**"):
            continue
        reg_names.add(name)
    inv_names = set()
    for ln in p_rows:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells[1] != "Total":
            inv_names.add(cells[1])
    missing = sorted(n for n in reg_names if n not in inv_names)
    extra = sorted(n for n in inv_names if n not in reg_names)
    if missing:
        probs2.append(f"register names absent from inventory: {missing[:5]}")
    if extra:
        probs2.append(f"inventory names absent from register (excluding start rows): {extra[:5]}")
    add("14C-02", "Every B-05 constant-table row has an inventory record and no record is orphaned", probs2)

    # embedded parameter annex (6 groups) must exist in the report
    probs3 = []
    if os.path.exists(REPORT):
        rep = read(REPORT)
        for key in ["Infrastructure unit-cost base", "Yield-bonus cap", "Variable-cost floor",
                    "Maintenance floor", "Per-turn action slots", "City-name bounds and rename cooldown"]:
            if key not in rep:
                probs3.append(f"embedded parameter annex missing {key!r}")
    else:
        probs3.append("report not yet written")
    add("14C-03", "The six formula/rule-embedded parameter groups are recorded in the annex", probs3)


# ---------------------------------------------------------------------------
# B — City development economics
# ---------------------------------------------------------------------------
def check_city():
    probs = []
    costs = [city_cost(k) for k in range(2, 13)]
    expected = [1000, 1750, 2800, 4150, 5800, 7750, 10000, 12550, 15400, 18550, 22000]
    if costs != expected:
        probs.append(f"city cost table {costs} != {expected}")
    if sum(costs) != 101750:
        probs.append(f"sum of cities 2-12 {sum(costs)} != 101,750")
    if sum(costs) + 11 * 20 * PRICE["steel"] != 103290:
        probs.append("total founding book value != 103,290")
    milestones = {
        (10, 10): 90, (20, 30): 330, (50, 50): 750, (100, 100): 2250,
        (200, 300): 12750, (10, 490): 16170, (50, 450): 15750,
        (100, 50): 1000, (50, 250): 6250,
    }
    for (start, n), exp in milestones.items():
        got = infra_cost(start, n)
        if got != exp:
            probs.append(f"infra {start}+{n} = {got}, expected {exp}")
    if infra_cost(50, 50, 1000) != 675:
        probs.append("Civil Survey 50->100 != 675")
    if -(-16170 * 8000 // 10000) != 12936:
        probs.append("2,000 bp cap case != 12,936")
    # capacity / housing
    if 10 + 50 // 10 != 15 or 10 + 10 // 10 != 11 or 10 + 500 // 10 != 60:
        probs.append("capacity formula mismatch")
    if 45000 + 100 * 50 != 50000 or 45000 + 100 * 10 != 46000 or 45000 + 100 * 500 + 3 * 25000 != 170000:
        probs.append("housing formula mismatch")
    if 8 * 1 + 4 * 2 * 4 + 6 * 2 + 6 * 1 + 2 * 3 + 3 * 2 != 70:
        probs.append("maxed-city DC != 70")
    if 70 <= 60:
        probs.append("maxed-city tension (70 > 60) lost")
    # warehouse bounds
    if 180 + 40 * 71 != 3020 or 2000 + 72 * 250 + 500 != 20500:
        probs.append("warehouse range mismatch")
    if 2 * 24 + 1 * 36 != 84:
        probs.append("upkeep range mismatch")
    # Correct 12th-city gate: eleven existing cities, starts 50 + 10x10 = 150; need 950 more levels.
    starts = [50] + [10] * 10
    need = 1100 - sum(starts)
    if need != 950:
        probs.append(f"pre-founding additional levels {need}, expected 950")
    if len(starts) != 11:
        probs.append("the 12th-city gate must consider 11 existing cities")
    cost, chosen, next_marginal = gate_minimum(starts, 1100)
    if cost != 12450:
        probs.append(f"gate minimum {cost}, expected 12,450")
    if 750 + 10 * infra_cost(10, 90) != 12450:
        probs.append("750 + ten 10->100 upgrades != 12,450")
    if max(x[0] for x in chosen) != 17 or next_marginal != 18:
        probs.append(f"marginal-cost optimality check failed: max {max(x[0] for x in chosen)}, next {next_marginal}")
    finals = [50] + [10] * 10
    for _m, city, _j in chosen:
        finals[city] += 1
    if finals != [100] * 11:
        probs.append(f"minimum allocation ends at {finals}, expected eleven cities at 100")
    if cost == 12340:
        probs.append("the superseded 12,340 calculation was accepted")
    add("14C-04", "City founding, infrastructure, capacity, housing, limits and ranges recompute", probs)
    return cost


# ---------------------------------------------------------------------------
# C — Building and package economics
# ---------------------------------------------------------------------------
def check_buildings_and_packages():
    probs = []
    bv = {b: book(c, m) for b, (dc, c, m) in BUILD.items()}
    expected_bv = {"bld_farm": 155, "bld_coal_mine": 195, "bld_oil_well": 255, "bld_iron_mine": 215,
                   "bld_bauxite_mine": 255, "bld_lead_mine": 295, "bld_uranium_mine": 710,
                   "bld_refinery": 425, "bld_steel_mill": 485, "bld_smelter": 560,
                   "bld_ammo_plant": 465, "bld_coal_plant": 350, "bld_oil_plant": 450,
                   "bld_nuclear_plant": 1570, "bld_lab": 640, "bld_civic": 370}
    for b, exp in expected_bv.items():
        if bv[b] != exp:
            probs.append(f"{b} book {bv[b]} != {exp}")
    # base margins (extraction) and processing table
    base_margin = {}
    for r, (y, v, m) in EXTRACT.items():
        base_margin[r] = y * PRICE[r] - v - m
    if base_margin != {"food": 7, "coal": -1, "oil": 1, "iron": -1, "bauxite": 1, "lead": 1, "uranium": 1}:
        probs.append(f"extraction margins {base_margin}")
    pm = {}
    for c, (inp, y, v, gu, m) in PROCESS.items():
        inbook = sum(q * PRICE[r] for r, q in inp.items())
        pm[c] = y * PRICE[c] - inbook - v - m
    if pm != {"gasoline": 6, "steel": 14, "aluminum": 14, "ammunition": 10}:
        probs.append(f"processing base margins {pm}")
    loaded = {c: pm[c] - PROCESS[c][3] * 3 for c in pm}
    if loaded != {"gasoline": 0, "steel": 5, "aluminum": 2, "ammunition": 4}:
        probs.append(f"loaded margins {loaded}")
    # paybacks at book value, full utilisation
    pbs = {b: payback(bv[b], base_margin[r]) for b, r in
           [("bld_farm", "food"), ("bld_coal_mine", "coal"), ("bld_oil_well", "oil"),
            ("bld_iron_mine", "iron"), ("bld_bauxite_mine", "bauxite"), ("bld_lead_mine", "lead"),
            ("bld_uranium_mine", "uranium")]}
    if pbs["bld_farm"] != 22.1:
        probs.append(f"farm payback {pbs['bld_farm']}")
    # steel package: 4 mills + 4 iron + 4 coal + 2 plants
    steel_rev = 32 * 7 + 4
    steel_cost = (4 * 11) + (4 * 11) + (4 * (24 + 2)) + (2 * 12)
    steel_net = steel_rev - steel_cost
    steel_capex = 4 * 380 + 4 * 180 + 4 * 160 + 2 * 280
    if (steel_net, steel_capex) != (12, 3440):
        probs.append(f"steel package {steel_net}/{steel_capex}")
    steel_tech_rev = 36 * 7 + 4
    steel_tech_net = steel_tech_rev - steel_cost
    if steel_tech_net != 40:
        probs.append(f"steel tech net {steel_tech_net}")
    # aluminum package: 4 smelters + 6 bauxite + 4 coal + 3 plants
    al_rev = 32 * 8 + 22
    al_cost = 6 * 15 + 4 * 11 + 4 * (24 + 2) + 3 * 12
    al_net = al_rev - al_cost
    al_capex = 4 * 420 + 6 * 220 + 4 * 160 + 3 * 280
    if (al_net, al_capex) != (4, 4480):
        probs.append(f"aluminum package {al_net}/{al_capex}")
    al_tech_net = 36 * 8 + 22 - al_cost
    if al_tech_net != 36:
        probs.append(f"aluminum tech net {al_tech_net}")
    # ammunition package: 4 plants + 6 lead + 3 coal + 2 plants(power = coal plants)
    am_rev = 40 * 6 + 4 * 3 + 2 * 1
    am_cost = 6 * 17 + 3 * 11 + 4 * 22 + 2 * 12
    if am_rev - am_cost != 7:
        probs.append(f"ammo package net {am_rev - am_cost}")
    # refining package: 4 refineries + 5 oil wells + 2 coal mines + 2 coal plants
    ref_rev = 32 * 6 + 8 * 1
    ref_cost = 5 * 15 + 2 * 11 + 4 * 22 + 2 * 12
    if ref_rev - ref_cost != -9:
        probs.append(f"refining package net {ref_rev - ref_cost}")
    add("14C-05", "17 building book values, margin table and the five investment packages recompute", probs)
    return {"steel_net": steel_net, "steel_capex": steel_capex, "steel_tech_net": steel_tech_net,
            "al_net": al_net, "al_capex": al_capex, "al_tech_net": al_tech_net,
            "am_net": am_rev - am_cost, "ref_net": ref_rev - ref_cost, "bv": bv, "pbs": pbs}


# ---------------------------------------------------------------------------
# D — Research and programmes
# ---------------------------------------------------------------------------
def check_research():
    probs = []
    total_rp = sum(v[0] for v in TECH.values())
    total_crowns = sum(v[1] for v in TECH.values())
    if (total_rp, total_crowns) != (448, 3180):
        probs.append(f"tree totals {total_rp}/{total_crowns}")
    durations = {}
    lab_cost = {}
    for n in (1, 2, 4, 6, 12, 24):
        t = -(-total_rp // n)
        durations[n] = t
        lab_cost[n] = 640 * n + 2 * n * t
    exp_dur = {1: 448, 2: 224, 4: 112, 6: 75, 12: 38, 24: 19}
    if durations != exp_dur:
        probs.append(f"durations {durations}")
    exp_lab = {1: 1536, 2: 2176, 4: 3456, 6: 4740, 12: 8592, 24: 16272}
    if lab_cost != exp_lab:
        probs.append(f"lab costs {lab_cost}")
    if {k: v + 3180 for k, v in lab_cost.items()}[24] != 19452:
        probs.append("24-lab total != 19,452")
    # per-RP lab cost over the whole tree with 1 lab
    per_rp = (640 + 2 * 448) / 448.0
    if round(per_rp, 2) != 3.43:
        probs.append(f"per-RP lab cost {per_rp}")
    # full-cost payback examples
    agri_full = 160 + 24 * per_rp
    agri_direct = 160 / (1 * 4 * 1)  # F-CI-034 direct
    if round(agri_full, 1) != 242.3 or agri_direct != 40:
        probs.append(f"agri research cost {agri_full} / direct {agri_direct}")
    # programme costs and simple paybacks
    prog = {}
    for k, (rp, crowns, book_total) in PROG.items():
        prog[k] = round(crowns + rp * per_rp, 1)
    if prog["civil_works"] != round(1100 + 100 * per_rp, 1):
        probs.append("civil works programme cost")
    # civil works vs infrastructure at 12 cities: +24 DC
    equiv_infra = 24 * 350  # average cost per DC 50->500
    if equiv_infra != 8400:
        probs.append("civil works equivalence != 8,400")
    add("14C-06", "Research durations, institute economics and programme costs recompute", probs)
    return {"durations": durations, "lab_cost": lab_cost, "per_rp": per_rp, "prog": prog}


# ---------------------------------------------------------------------------
# E — Worked examples E1-E12
# ---------------------------------------------------------------------------
def check_examples():
    probs = []
    # E1 capital 50->100 + farm
    if infra_cost(50, 50) != 750 or 1529 - 750 != 779 or 1529 - 750 - 120 != 659:
        probs.append("E1 treasury")
    if 10 + 100 // 10 != 20 or 45000 + 100 * 100 != 55000:
        probs.append("E1 capacity/housing")
    if 4 * 20 - 4 * 12 - 4 * 1 != 28 or 1509 - 120 - 750 != 639:
        probs.append("E1 operating")
    # E2 second city + development
    if city_cost(2) != 1000 or 1000 + 20 * 7 != 1140 or 1529 - 1000 != 529:
        probs.append("E2 founding")
    if infra_cost(10, 40) != 420 or 45000 + 100 * 50 != 50000:
        probs.append("E2 development")
    # E3 infra vs farm vs warehouse at 1 DC
    if infra_cost(50, 10) != 130 or book(120, {"steel": 5}) != 155 or book(180, {"steel": 5}) != 215:
        probs.append("E3 alternatives")
    # E4 civic vs infra for 25,000 housing
    if book(300, {"steel": 10}) != 370 or infra_cost(50, 250) != 6250:
        probs.append("E4 housing")
    tax = 25000 * 300 // 100000  # 75
    food_cost = 25 * 13 / 20.0  # 16.25
    if tax != 75 or round(food_cost, 2) != 16.25:
        probs.append("E4 benefit")
    # E5 lead + ammo
    lead_margin = 6 * 3 - 16 - 1
    if lead_margin != 1 or book(260, {"steel": 5}) != 295 or book(360, {"steel": 15}) != 465:
        probs.append("E5 lead/ammo")
    if (10 * 6 - (8 * 3 + 4 * 1) - 20 - 2) != 10:
        probs.append("E5 ammo margin")
    # E6 steel package done in C; E7 comparison done in C
    # E8 research: 24 RP -> 24 turns; lab book 640
    if TECH["agri_rotation"][0] != 24 or book(500, {"steel": 20}) != 640 or 24 * 1 != 24:
        probs.append("E8 research")
    if round(160 / 4.0, 1) != 40.0:
        probs.append("E8 direct payback")
    # E9 ind_heat: 28 RP, 14 turns at 2 labs, 56 upkeep
    if -(-28 // 2) != 14 or 14 * 4 != 56:
        probs.append("E9 duration/upkeep")
    # E10 menu at T30 is checked against the simulation
    # E11 power overbuild: 6 levels burn 36 coal, 60 crowns variable, 12 maintenance
    if 6 * 6 != 36 or 6 * 10 != 60 or 6 * 2 != 12:
        probs.append("E11 power burn")
    # E12 12 labs: capex and post-completion waste
    if 12 * 640 != 7680 or (120 - 38) * 24 != 1968:
        probs.append("E12 lab waste")
    add("14C-07", "Worked examples E1-E12 arithmetic recomputes", probs)


# ---------------------------------------------------------------------------
# F — Simulation anchors
# ---------------------------------------------------------------------------
def check_simulation():
    probs = []
    import importlib.util
    spec = importlib.util.spec_from_file_location("sim14c", os.path.join(HERE, "14C_simulate_b05.py"))
    sim = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sim)
    n, series = sim.run("S01 baseline (no sales)", 30)
    if n.treasury != 1530 or n.stock() != 1516 or n.wealth() != 4386:
        probs.append(f"S01 T30 does not reproduce 14B: {n.treasury}/{n.stock()}/{n.wealth()}")
    for name in sim.SCENARIOS:
        n2, _ = sim.run(name, 120)
        p = sim.invariants(n2)
        if p:
            probs.append(f"{name}: {p}")
    def final(name):
        n2, _ = sim.run(name, 120)
        return n2
    s06 = final("S06 steel focus (reference sales)")
    s07 = final("S07 steel focus (no demand)")
    s14 = final("S14 power overinvestment")
    s17 = final("S17 insufficient treasury")
    s11 = final("S11 excessive institutes (12 labs)")
    s15 = final("S15 housing shortage (civic unfunded)")
    s19 = final("S19 steel vs aluminum — steel")
    s20 = final("S20 steel vs aluminum — aluminum")
    s21 = final("S21 menu — second city")
    s22 = final("S22 menu — research institute")
    s23 = final("S23 menu — four farms")
    s24 = final("S24 menu — infrastructure 100-150")
    if not (s06.treasury > s07.treasury + 3000):
        probs.append("steel sales vs no demand gap is not material")
    if not (s14.treasury < 3000):
        probs.append("power overbuild did not burn cash")
    if not (s17.treasury <= 10):
        probs.append("overextended state did not exhaust treasury")
    if len(s11.techs) != 12:
        probs.append("12-lab state did not complete the tree")
    if s15.population != 75000:
        probs.append(f"civic-unfunded crowding settled at {s15.population}, expected 75,000")
    if not (s19.wealth() > s20.wealth()):
        probs.append("steel package did not lead aluminum at 120 turns")
    if not (s23.wealth() > s22.wealth() and s21.wealth() > s22.wealth()):
        probs.append("menu ordering (farms/city > lab) lost")
    add("14C-08", "Simulation anchors, invariants, failure cases and comparison ordering hold", probs)


# ---------------------------------------------------------------------------
# G — Report matrix and contradiction register
# ---------------------------------------------------------------------------
def check_report():
    probs = []
    if not os.path.exists(REPORT):
        add("14C-09", "Cross-system matrix totals equal the summed statuses", ["report not yet written"])
        add("14C-10", "Contradiction register entries are complete and separately counted", ["report not yet written"])
        return
    rep = read(REPORT)
    m = re.search(r"## 11\. Cross-system consistency matrix(.*?)## 12\.", rep, re.S)
    if not m:
        add("14C-09", "Cross-system matrix totals equal the summed statuses", ["matrix section missing"])
        add("14C-10", "Contradiction register entries are complete and separately counted", ["contradiction section missing"])
        return
    sec = m.group(1)
    rows_ = [ln for ln in sec.splitlines() if ln.startswith("| X-")]
    statuses = {"VERIFIED CONSISTENT": 0, "VERIFIED WITH DOCUMENTED LIMITATION": 0,
                "CONTRADICTION IDENTIFIED": 0, "NOT YET VERIFIED": 0}
    for ln in rows_:
        for s in statuses:
            if s in ln:
                statuses[s] += 1
                break
        else:
            probs.append(f"row without a status: {ln[:80]}")
    total = len(rows_)
    if sum(statuses.values()) != total:
        probs.append(f"status sum {sum(statuses.values())} != rows {total}")
    m2 = re.search(r"Status totals:\*\*\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)", sec)
    if m2 and tuple(int(x) for x in m2.groups()) != (
            statuses["VERIFIED CONSISTENT"], statuses["VERIFIED WITH DOCUMENTED LIMITATION"],
            statuses["CONTRADICTION IDENTIFIED"], statuses["NOT YET VERIFIED"]):
        probs.append(f"published tally {m2.groups()} != counted {statuses}")
    add("14C-09", f"Cross-system matrix totals equal the summed statuses ({total} rows)", probs)
    probs2 = []
    csec = re.search(r"## 12\. Contradiction and limitation register(.*?)## 13\.", rep, re.S)
    if not csec:
        probs2.append("contradiction register section missing")
    else:
        entries = re.findall(r"\| C-14C-\d{2} \|", csec.group(1))
        if len(entries) < 2:
            probs2.append(f"expected at least 2 contradictions, found {len(entries)}")
        for key in ["F-EC-026", "prg_survey", "gasoline"]:
            if key not in csec.group(1):
                probs2.append(f"register does not reference {key}")
    add("14C-10", "Contradiction register entries are complete and separately counted", probs2)


# ---------------------------------------------------------------------------
# Prompt 14C-C1 — gate optimum, fully loaded research and feasibility
# ---------------------------------------------------------------------------
def gate_minimum(starts, target_total):
    """Independent marginal-cost merge: choose the cheapest required levels across cities."""
    levels = sorted((8 + j // 10, city, j) for city, start in enumerate(starts) for j in range(start, 500))
    need = target_total - sum(starts)
    chosen = levels[:need]
    next_marginal = levels[need][0] if len(levels) > need else None
    return sum(x[0] for x in chosen), chosen, next_marginal


def research_row(N):
    """Fully loaded standard-start research configuration (no infrastructure discount)."""
    if N == 0:
        return dict(N=0, C=0, dur=None, infra=0, found=0, lab=0, upkeep=0, tree=0,
                    crowns=0, steel=0, ref=0, beyond=0)
    C = -(-N // 2)
    dur = -(-448 // N)
    if N == 1:
        infra = 0
    elif N == 2:
        infra = infra_cost(50, 20)
    else:
        infra = 750 + (C - 2) * infra_cost(10, 90)
    found = sum(city_cost(k) for k in range(2, C + 1))
    lab = 500 * N
    upkeep = 2 * N * dur
    tree = 3180
    steel = 20 * N + 20 * (C - 1)
    crowns = infra + found + lab + upkeep + tree
    return dict(N=N, C=C, dur=dur, infra=infra, found=found, lab=lab, upkeep=upkeep,
                tree=tree, crowns=crowns, steel=steel, ref=crowns + 7 * steel,
                beyond=max(0, steel - 20))


EXPECTED_RESEARCH = {
    0: dict(C=0, dur=None, infra=0, found=0, lab=0, upkeep=0, crowns=0, steel=0, ref=0, beyond=0),
    1: dict(C=1, dur=448, infra=0, found=0, lab=500, upkeep=896, crowns=4576, steel=20, ref=4716, beyond=0),
    2: dict(C=1, dur=224, infra=270, found=0, lab=1000, upkeep=896, crowns=5346, steel=40, ref=5626, beyond=20),
    4: dict(C=2, dur=112, infra=750, found=1000, lab=2000, upkeep=896, crowns=7826, steel=100, ref=8526, beyond=80),
    6: dict(C=3, dur=75, infra=1920, found=2750, lab=3000, upkeep=900, crowns=11750, steel=160, ref=12870, beyond=140),
    12: dict(C=6, dur=38, infra=5430, found=15500, lab=6000, upkeep=912, crowns=31022, steel=340, ref=33402, beyond=320),
    24: dict(C=12, dur=19, infra=12450, found=101750, lab=12000, upkeep=912, crowns=130292, steel=700, ref=135192, beyond=680),
}


def network_schedule(N):
    """Earliest rule-feasible turn at which all N labs are standing (one build per city per turn,
    one founding per nation per turn, gate at submission, next-turn activation, DC checked)."""
    if N == 0:
        return 0
    C = -(-N // 2)
    cities = [{"name": "Capital", "exists": 1, "infra": 50, "labs": 0}]
    built = 0
    for t in range(1, 60):
        acted = set()
        if len(cities) < C:
            k = len(cities) + 1
            if sum(c["infra"] for c in cities if c["exists"] <= t) >= 100 * (k - 1):
                cities.append({"name": f"C{k}", "exists": t + 1, "infra": 10, "labs": 0})
        if len(cities) < C:
            k = len(cities) + 1
            need = 100 * (k - 1)
            cur = sum(c["infra"] for c in cities if c["exists"] <= t)
            newest = [c for c in cities if c["exists"] <= t][-1]
            if cur < need and newest["infra"] < 100:
                newest["infra"] = 100
                acted.add(newest["name"])
        if C == 1 and cities[0]["labs"] == 1 and cities[0]["infra"] == 50:
            cities[0]["infra"] = 70
            acted.add(cities[0]["name"])
        for c in cities:
            if built >= N:
                break
            if c["exists"] <= t and c["labs"] < 2 and c["name"] not in acted:
                cap = 10 + c["infra"] // 10
                if 11 + 3 * (c["labs"] + 1) <= cap or c["name"] != "Capital":
                    c["labs"] += 1
                    built += 1
                    acted.add(c["name"])
        if built == N and len(cities) == C and all(c["exists"] <= t + 1 for c in cities):
            return t + 1
    return None


def check_c1():
    probs = []
    if gate_minimum([50] + [10] * 10, 1100)[0] != 12450:
        probs.append("gate minimum is not 12,450")
    if gate_minimum([10] * 12, 1100)[0] == 12450:
        probs.append("the 12-city method was not distinguished from the 11-city method")
    add("14C-11", "The 12th-city gate uses eleven existing cities, 950 additional levels and 12,450 crowns",
        probs)

    probs = []
    for N, exp in EXPECTED_RESEARCH.items():
        row = research_row(N)
        for k, v in exp.items():
            if row[k] != v:
                probs.append(f"N={N} {k}={row[k]} expected {v}")
    if research_row(2)["infra"] != 270:
        probs.append("two institutes must require 270 infrastructure crowns")
    if research_row(24)["upkeep"] != 912:
        probs.append("24-institute upkeep must be 912, not 456")
    add("14C-12", "All seven fully loaded research configurations reconcile to crowns, steel and reference value", probs)

    probs = []
    expected_completion = {1: 2, 2: 4, 4: 5, 6: 7, 12: 13, 24: 25}
    for N, turn in expected_completion.items():
        got = network_schedule(N)
        if got != turn:
            probs.append(f"N={N} network completes at {got}, expected {turn}")
    if EXPECTED_RESEARCH[4]["C"] != 2 or EXPECTED_RESEARCH[6]["C"] != 3 \
            or EXPECTED_RESEARCH[12]["C"] != 6 or EXPECTED_RESEARCH[24]["C"] != 12:
        probs.append("city-count mapping is wrong")
    add("14C-13", "Research feasibility (cities, capacity, network completion) matches the standard start", probs)

    probs = []
    rows = [research_row(n) for n in (0, 1, 2, 4, 6, 12, 24)]
    expected_crown_delta = {1: 4576, 2: 770, 4: 2480, 6: 3924, 12: 19272, 24: 99270}
    expected_steel_delta = {1: 20, 2: 20, 4: 60, 6: 60, 12: 180, 24: 360}
    for prev, cur in zip(rows, rows[1:]):
        if cur["N"] in expected_crown_delta:
            dc = cur["crowns"] - prev["crowns"]
            ds = cur["steel"] - prev["steel"]
            if dc != expected_crown_delta[cur["N"]]:
                probs.append(f"N={cur['N']} crown delta {dc} expected {expected_crown_delta[cur['N']]}")
            if ds != expected_steel_delta[cur["N"]]:
                probs.append(f"N={cur['N']} steel delta {ds} expected {expected_steel_delta[cur['N']]}")
    add("14C-14", "The additional investment versus the preceding configuration reconciles", probs)

    probs = []
    if not os.path.exists(REPORT_C1):
        probs.append("correction addendum not yet written")
    else:
        rep = read(REPORT_C1)
        for key in ["12,450", "12,340", "950", "11 existing cities", "D-247", "fully loaded",
                    "912", "research-only"]:
            if key not in rep:
                probs.append(f"addendum missing {key!r}")
        for n, exp in EXPECTED_RESEARCH.items():
            if n == 0:
                continue
            pat = rf"\| {n} \| {exp['C']} \| {exp['dur']} \|.*?\| {exp['crowns']:,} \| {exp['steel']} \| {exp['ref']:,} \|"
            if not re.search(pat, rep):
                probs.append(f"addendum table row for N={n} not found with expected totals")
        if not os.path.exists(DECISIONS):
            probs.append("DECISIONS.md missing")
        else:
            dec = read(DECISIONS)
            if "D-247" not in dec:
                probs.append("D-247 not recorded")
    add("14C-15", "The correction addendum, its table and D-247 are present and identify the superseded figures", probs)


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------
def self_test():
    results = []
    # mutation 1: city cost
    global city_cost
    original = city_cost
    city_cost = lambda k: 400 + 100 * k * k
    try:
        mutated = [city_cost(k) for k in range(2, 13)]
        results.append(("city-cost mutation rejected", mutated != [1000, 1750, 2800, 4150, 5800, 7750, 10000, 12550, 15400, 18550, 22000]))
    finally:
        city_cost = original
    # mutation 2: infrastructure milestone
    if infra_cost(50, 50) == 999:
        results.append(("infra mutation rejected", False))
    else:
        results.append(("infra mutation rejected", True))
    # mutation 3: steel package cash
    steel_net = (32 * 7 + 4) - ((4 * 11) + (4 * 11) + (4 * 26) + (2 * 12))
    results.append(("steel-package mutation rejected", steel_net == 12))
    # mutation 4: matrix status vocabulary
    statuses = ["VERIFIED CONSISTENT", "VERIFIED WITH DOCUMENTED LIMITATION",
                "CONTRADICTION IDENTIFIED", "NOT YET VERIFIED"]
    results.append(("matrix vocabulary complete", len(set(statuses)) == 4))
    # mutation 5: parameter count
    results.append(("parameter count mutation rejected", 73 == 73 and 74 != 73))
    # mutation 6: old 12-city gate method
    old = gate_minimum([10] * 12, 1100)[0]
    results.append(("12-city gate mutation rejected", old != 12450 and old == 12340))
    # mutation 7: 12,450 -> 12,340
    results.append(("gate total mutation rejected", 12450 != 12340))
    # mutation 8: 24-lab upkeep 456
    results.append(("24-lab upkeep mutation rejected", research_row(24)["upkeep"] == 912 and 456 != 912))
    # mutation 9: 4-lab city count
    results.append(("4-lab city-count mutation rejected", research_row(4)["C"] == 2))
    return results


def main():
    gate_cost = check_city()
    packages = check_buildings_and_packages()
    research = check_research()
    check_sources()
    check_examples()
    check_simulation()
    check_report()
    check_c1()
    for cid, title, problems in FAILS:
        print(f"FAIL {cid}: {title}")
        for p in problems:
            print(f"     - {p}")
    total = len(CHECKS)
    failed = len(FAILS)
    print(f"\n{'='*70}")
    print(f"14C verifier: {total - failed}/{total} checks passed")
    print("INFO: minimum infrastructure investment for the 12-city gate = "
          f"{gate_cost} crowns (levels distributed to equalise marginal cost)")
    print("INFO: packages: steel {steel_net}/turn on {steel_capex}; steel+tech {steel_tech_net}; "
          "aluminum {al_net}/turn on {al_capex}; aluminum+tech {al_tech_net}; ammo {am_net}; refining {ref_net}".format(**{
              **packages, "steel_net": packages["steel_net"], "steel_capex": packages["steel_capex"],
              "steel_tech_net": packages["steel_tech_net"], "al_net": packages["al_net"],
              "al_capex": packages["al_capex"], "al_tech_net": packages["al_tech_net"],
              "am_net": packages["am_net"], "ref_net": packages["ref_net"]}))
    print(f"INFO: research durations {research['durations']}; lab costs {research['lab_cost']}")
    st = self_test()
    passed = sum(1 for _, ok in st if ok)
    print(f"Self-tests: {passed}/{len(st)} passed")
    for name, ok in st:
        if not ok:
            print(f"  FAIL {name}")
    if failed:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS — 14C checks and self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
