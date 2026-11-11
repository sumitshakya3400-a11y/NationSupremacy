"""Arithmetic and continuity verifier for Stage 2 Prompt 06A (B-06).

Recomputes every number in B-06 section 22 from the constants in
`12_population_and_domestic_politics_formula_register.md`, and checks the
document-level invariants that make those numbers meaningful.

This is a DOCUMENT check. It does not run the game, a database, a scheduler
or a simulation, and it does not prove that any rule is implemented.
"""

import os
import re
import sys

# Diagnostic text contains `−`, `≥` and `×`; a Windows cp1252 console cannot
# encode them and would raise while printing a self-test result. Reconfigure
# stdout only (assertions and exit codes are unchanged).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CHECKS = 0
FAILS = []


def check(label, got, want):
    global CHECKS
    CHECKS += 1
    if got != want:
        FAILS.append("%s: got %r, want %r" % (label, got, want))


def check_true(label, cond, detail=""):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILS.append("%s: %s" % (label, detail or "false"))


# ---------------------------------------------------------------- constants
WEIGHTS = {"labour": 30, "rural": 15, "industry": 20, "commerce": 15,
           "scholars": 10, "security": 10}

GOV = {
    "democracy": dict(aw=32, shift=-100, cap=11000, svc=0, rp=0),
    "constitutional_monarchy": dict(aw=22, shift=200, cap=10900, svc=0, rp=0),
    "absolute_monarchy": dict(aw=14, shift=400, cap=10800, svc=0, rp=0),
    "dictatorship": dict(aw=16, shift=0, cap=10600, svc=-1000, rp=0),
    "military_junta": dict(aw=10, shift=250, cap=10600, svc=500, rp=-1),
    "technocracy": dict(aw=24, shift=-150, cap=10900, svc=0, rp=1),
}

VECTORS = {
    "democracy": (30, 15, 20, 15, 10, 10),
    "constitutional_monarchy": (10, 20, 15, 15, 20, 20),
    "absolute_monarchy": (20, 20, 10, 5, 5, 40),
    "dictatorship": (5, 10, 20, 10, 0, 55),
    "military_junta": (0, 0, 0, 0, 0, 100),
    "technocracy": (5, 0, 15, 5, 65, 10),
}

ORDER = {
    "OPEN": dict(stab=-200, labour=6, rural=-4, industry=2, commerce=8, scholars=10, security=-15),
    "BALANCED": dict(stab=0, labour=0, rural=0, industry=0, commerce=0, scholars=0, security=0),
    "FIRM": dict(stab=300, labour=-6, rural=4, industry=-2, commerce=-8, scholars=-10, security=15),
}

FISCAL = {"LOW": (200, 0), "STANDARD": (300, 2000), "HIGH": (400, 5000)}


def supports(service=2000, tax=300, housing=10000, hunger=0, stability=10000,
             food_share=3750, processing=1250, warehouse=8450, institutes=0,
             order="BALANCED"):
    o = ORDER[order]
    s = {}
    s["labour"] = 48 + service // 400 + (300 - tax) // 40 + (housing // 500 - 18) \
        - hunger // 100 + o["labour"]
    s["rural"] = 48 + food_share // 250 + service // 1000 + (300 - tax) // 20 \
        - hunger // 150 + (stability - 10000) // 500 + o["rural"]
    s["industry"] = 48 + processing // 250 + (300 - tax) // 15 \
        + (warehouse // 1000 - 5) + (stability - 10000) // 400 + o["industry"]
    s["commerce"] = 48 + (warehouse // 1000 - 5) + (300 - tax) // 12 \
        + (stability - 10000) // 400 + o["commerce"]
    s["scholars"] = 48 + min(12, 3 * institutes) + service // 400 \
        + (300 - tax) // 50 + o["scholars"]
    s["security"] = 48 + service // 2000 - hunger // 200 \
        + (stability - 10000) // 400 + o["security"]
    return {k: max(0, min(100, v)) for k, v in s.items()}


def approval_target(s):
    total = sum(s[k] * WEIGHTS[k] for k in WEIGHTS)
    return max(0, min(100, total // 100))


def move_approval(current, target):
    return max(0, min(100, current + max(-5, min(5, target - current))))


def stability_target(approval, gov, order="BALANCED", hunger=0, crowding=0):
    g = GOV[gov]
    raw = 10000 + (approval - 55) * g["aw"] + g["shift"] + ORDER[order]["stab"] \
        - hunger // 2 - crowding // 10
    return max(5000, min(g["cap"], raw))


def move_stability(current, target):
    return current + max(-250, min(250, target - current))


def legitimacy(gov, s):
    v = VECTORS[gov]
    keys = ["labour", "rural", "industry", "commerce", "scholars", "security"]
    return max(0, min(100, sum(v[i] * s[keys[i]] for i in range(6)) // 100))


def growth_bp(approval, population, housing, hunger=0, crowding=0):
    headroom = max(0, housing - population)
    raw = 50 + (approval - 55) // 2 + min(15, headroom * 100 // population) \
        - hunger // 30 - crowding // 100
    return max(-100, min(100, raw))


def apply_growth(population, housing, gbp, crowding=0):
    natural = population + population * gbp // 10000
    if population > housing:
        excess = population - housing
        decline = max(-(-excess // 10), max(0, population - natural))
        return max(1000, population - decline)
    return max(1000, min(natural, housing))


def crowding_bp(population, housing):
    if population <= housing:
        return 0
    return min(10000, (population - housing) * 10000 // population)


def service_cost(tax_income, share, mod):
    base = tax_income * share // 10000
    return -(-(base * (10000 + mod)) // 10000)


def rp_per_turn(institutes, gov):
    if institutes == 0:
        return 0
    return max(0, institutes + GOV[gov]["rp"])


def tax_income(population, rate, stability=10000):
    return population * rate * stability // 1_000_000_000


# ------------------------------------------------------------ table checks
check("weights sum", sum(WEIGHTS.values()), 100)
for g, v in VECTORS.items():
    check("vector %s sums to 100" % g, sum(v), 100)
for g in GOV:
    check_true("cap %s within 10000..11000" % g, 10000 <= GOV[g]["cap"] <= 11000)

# --------------------------------------------------- Example 1: new nation
s1 = supports()
check("E1 labour", s1["labour"], 55)
check("E1 rural", s1["rural"], 65)
check("E1 industry", s1["industry"], 56)
check("E1 commerce", s1["commerce"], 51)
check("E1 scholars", s1["scholars"], 53)
check("E1 security", s1["security"], 49)
check("E1 weighted", sum(s1[k] * WEIGHTS[k] for k in WEIGHTS), 5530)
check("E1 approval", approval_target(s1), 55)
check("E1 stability target", stability_target(55, "constitutional_monarchy"), 10200)
check("E1 stability step", move_stability(10000, 10200), 10200)
check("E1 legitimacy", legitimacy("constitutional_monarchy", s1), 54)
check("E1 growth", growth_bp(55, 50000, 50000), 50)
check("E1 population", apply_growth(50000, 50000, 50), 50000)
check("E1 food demand", -(-50000 // 1000), 50)
check("E1 food supply", 3 * 20, 60)

# --------------------------------------------- Example 2: housing headroom
g1 = growth_bp(55, 50000, 55000)
check("E2 growth turn 1", g1, 60)
p1 = apply_growth(50000, 55000, g1)
check("E2 population turn 1", p1, 50300)
g2 = growth_bp(55, p1, 55000)
check("E2 growth turn 2", g2, 59)
p2 = apply_growth(p1, 55000, g2)
check("E2 population turn 2", p2, 50596)

# ----------------------------------------------- Example 3: housing cap
g3 = growth_bp(55, 50000, 50200)
check("E3 growth", g3, 50)
check("E3 natural", 50000 + 50000 * g3 // 10000, 50250)
check("E3 capped", apply_growth(50000, 50200, g3), 50200)

# ------------------------------------------------- Example 4: food shortage
for hunger, gbp, pop in ((750, 35, 50175), (1500, 10, 50050), (3000, -40, 49800)):
    check("E4 growth at hunger %d" % hunger, growth_bp(55, 50000, 55000, hunger), gbp)
    check("E4 population at hunger %d" % hunger,
          apply_growth(50000, 55000, gbp), pop)

# ------------------------------------------- Example 5: STANDARD to HIGH
hi = supports(service=5000, tax=400)
check("E5 labour", hi["labour"], 59)
check("E5 rural", hi["rural"], 63)
check("E5 industry", hi["industry"], 49)
check("E5 commerce", hi["commerce"], 42)
check("E5 scholars", hi["scholars"], 58)
check("E5 security", hi["security"], 50)
check("E5 weighted", sum(hi[k] * WEIGHTS[k] for k in WEIGHTS), 5405)
check("E5 approval target", approval_target(hi), 54)
check("E5 tax STANDARD", tax_income(50000, 300), 150)
check("E5 tax HIGH", tax_income(50000, 400), 200)
check("E5 service STANDARD", service_cost(150, 2000, 0), 30)
check("E5 service HIGH", service_cost(200, 5000, 0), 100)
check("E5 net STANDARD", 150 - 30, 120)
check("E5 net HIGH", 200 - 100, 100)

# The LOW setting is the other signed-rounding endpoint; it is also the
# DMP-099 / DMP-168 approval figure.
lo = supports(service=0, tax=200)
check("E5 LOW labour", lo["labour"], 52)
check("E5 LOW rural", lo["rural"], 68)
check("E5 LOW industry", lo["industry"], 62)
check("E5 LOW commerce", lo["commerce"], 59)
check("E5 LOW scholars", lo["scholars"], 50)
check("E5 LOW security", lo["security"], 48)
check("E5 LOW weighted", sum(lo[k] * WEIGHTS[k] for k in WEIGHTS), 5685)
check("E5 LOW approval", approval_target(lo), 56)
check("E5 HIGH approval", approval_target(hi), 54)

# ------------------------------------------------- tax-term regressions
# The old expression was -((tax - 300) // step). Python floors negative
# values, so it gave +3/+7/+9 at LOW and -2/-6/-8 at HIGH. The authoritative
# form is (300 - tax) // step, which gives the published endpoints.
for tax, lab, rur, ind, com, sch in (
        (200, 2, 5, 6, 8, 2),
        (300, 0, 0, 0, 0, 0),
        (400, -3, -5, -7, -9, -2)):
    check("TAX labour term %d" % tax, (300 - tax) // 40, lab)
    check("TAX rural term %d" % tax, (300 - tax) // 20, rur)
    check("TAX industry term %d" % tax, (300 - tax) // 15, ind)
    check("TAX commerce term %d" % tax, (300 - tax) // 12, com)
    check("TAX scholars term %d" % tax, (300 - tax) // 50, sch)

# Explicit off-by-one regressions: each would fail if the old floor form
# were restored while the documented ranges stayed unchanged.
check("REGRESSION labour low-tax +2 not +3", supports(service=0, tax=200)["labour"], 52)
check("REGRESSION labour high-tax -3 not -2", supports(service=5000, tax=400)["labour"], 59)
check("REGRESSION industry low-tax +6 not +7", supports(service=0, tax=200)["industry"], 62)
check("REGRESSION industry high-tax -7 not -6", supports(service=5000, tax=400)["industry"], 49)
check("REGRESSION commerce low-tax +8 not +9", supports(service=0, tax=200)["commerce"], 59)
check("REGRESSION commerce high-tax -9 not -8", supports(service=5000, tax=400)["commerce"], 42)

# Threshold-adjacent values and monotonicity over the whole tax line. Only
# 200/300/400 are legal settings, but the formula must not jump the wrong way.
for tax, lab, ind, com in ((199, 2, 6, 8), (201, 2, 6, 8),
                           (299, 0, 0, 0), (301, -1, -1, -1),
                           (399, -3, -7, -9), (401, -3, -7, -9)):
    check("TAX edge labour %d" % tax, (300 - tax) // 40, lab)
    check("TAX edge industry %d" % tax, (300 - tax) // 15, ind)
    check("TAX edge commerce %d" % tax, (300 - tax) // 12, com)

check_true("TAX labour range -3..+2",
           all(-3 <= (300 - t) // 40 <= 2 for t in range(200, 401)))
check_true("TAX industry range -7..+6",
           all(-7 <= (300 - t) // 15 <= 6 for t in range(200, 401)))
check_true("TAX commerce range -9..+8",
           all(-9 <= (300 - t) // 12 <= 8 for t in range(200, 401)))
check_true("TAX terms monotone",
           all((300 - t) // 40 >= (300 - (t + 1)) // 40 and
               (300 - t) // 15 >= (300 - (t + 1)) // 15 and
               (300 - t) // 12 >= (300 - (t + 1)) // 12 for t in range(0, 1000)))

# ------------------------------------------------------- population floor
# F-PD-002 must clamp every path, not only crowding. This is the review case:
# 1,000 people, approval 0, housing 45,000, hunger 3,000 -> raw 993 -> 1,000.
g_floor = growth_bp(0, 1000, 45000, hunger=3000)
check("FLOOR growth -63", g_floor, -63)
check("FLOOR natural 993", 1000 + 1000 * g_floor // 10000, 993)
check("FLOOR applied", apply_growth(1000, 45000, g_floor), 1000)
check("FLOOR raw below minimum", apply_growth(1000, 45000, g_floor) >= 1000, True)
check("FLOOR ordinary negative growth", apply_growth(2000, 45000, -63), 1987)
check("FLOOR positive growth", apply_growth(50000, 55000, 60), 50300)
check("FLOOR housing cap", apply_growth(50000, 50200, 50), 50200)
check("FLOOR crowding path", apply_growth(1010, 1000, -100), 1000)
check("FLOOR crowding above minimum", apply_growth(2000, 1000, 50), 1900)
check("FLOOR pure function", apply_growth(1000, 45000, g_floor),
      apply_growth(1000, 45000, g_floor))
# Repeated settlement: the next pass starts from the value the previous pass
# produced and lands on the floor again; no people-debt is banked, so a nation
# cannot be pushed below 1,000 by re-running the same settlement.
check("FLOOR repeated settlement stays at the floor",
      apply_growth(apply_growth(1000, 45000, g_floor), 45000, g_floor), 1000)
check("FLOOR repeated settlement from the raw value",
      apply_growth(993, 45000, g_floor), 1000)


# -------------------------------------- Example 6: approval after a famine
s_famine = supports(hunger=1500)
check("E6 famine weighted", sum(s_famine[k] * WEIGHTS[k] for k in WEIGHTS), 4860)
check("E6 famine target", approval_target(s_famine), 48)
check("E6 recovery step 1", move_approval(48, 55), 53)
check("E6 recovery step 2", move_approval(53, 55), 55)

# ------------------------------------- Example 7: approval when famine hits
s7 = supports(hunger=3000)
check("E7 labour", s7["labour"], 25)
check("E7 rural", s7["rural"], 45)
check("E7 security", s7["security"], 34)
check("E7 weighted", sum(s7[k] * WEIGHTS[k] for k in WEIGHTS), 4180)
check("E7 target", approval_target(s7), 41)
check("E7 step 1", move_approval(55, 41), 50)
check("E7 step 2", move_approval(50, 41), 45)
check("E7 step 3", move_approval(45, 41), 41)

# ------------------------------------------ Example 8: developed nation
s8 = supports(housing=10000, food_share=3333, processing=2083,
              warehouse=3000, institutes=3, stability=10400)
check("E8 labour", s8["labour"], 55)
check("E8 rural", s8["rural"], 63)
check("E8 industry", s8["industry"], 55)
check("E8 commerce", s8["commerce"], 47)
check("E8 scholars", s8["scholars"], 62)
check("E8 security", s8["security"], 50)
check("E8 weighted", sum(s8[k] * WEIGHTS[k] for k in WEIGHTS), 5520)
check("E8 approval", approval_target(s8), 55)
check("E8 tax", tax_income(140000, 300, 10400), 436)
check("E8 service", service_cost(436, 2000, 0), 87)
check("E8 net", 436 - 87, 349)
check("E8 food share", 8 * 10000 // 24, 3333)
check("E8 processing share", 5 * 10000 // 24, 2083)
check("E8 warehouse", 1200 * 10000 // 4000, 3000)

# ------------------------------------------ Example 9: aggregate weight
check("E9 sum", sum(s1[k] * WEIGHTS[k] for k in WEIGHTS), 5530)
check("E9 target", approval_target(s1), 55)
check_true("E9 within support range",
           min(s1.values()) <= approval_target(s1) <= max(s1.values()))

# --------------------------------- Example 10: democracy versus junta
dem = dict(rate=300, mod=0)
jun = dict(rate=300, mod=500)

dem_s60 = stability_target(60, "democracy")
jun_s60 = stability_target(60, "military_junta", order="FIRM")
check("E10 democracy stability", dem_s60, 10060)
check("E10 junta stability", jun_s60, 10600)
check("E10 democracy tax", tax_income(50000, 300, dem_s60), 150)
check("E10 junta tax", tax_income(50000, 300, jun_s60), 159)
check("E10 democracy service", service_cost(150, 2000, dem["mod"]), 30)
check("E10 junta service", service_cost(159, 2000, jun["mod"]), 33)
check("E10 democracy net", 150 - 30, 120)
check("E10 junta net", 159 - 33, 126)
check("E10 democracy at 90", stability_target(90, "democracy"), 11000)
check("E10 democracy tax at 90", tax_income(50000, 300, 11000), 165)
check("E10 democracy net at 90", 165 - service_cost(165, 2000, 0), 132)
check("E10 crossover stability", stability_target(75, "democracy"), 10540)
check("E10 crossover tax", tax_income(50000, 300, 10540), 158)
check("E10 crossover net", 158 - service_cost(158, 2000, 0), 127)
check_true("E10 junta capped at 90", stability_target(90, "military_junta", order="FIRM") == 10600)

# -------------------------- Example 11: government and research modifier
check("E11 technocracy 1", rp_per_turn(1, "technocracy"), 2)
check("E11 monarchy 1", rp_per_turn(1, "constitutional_monarchy"), 1)
check("E11 junta 1", rp_per_turn(1, "military_junta"), 0)
check("E11 technocracy 3", rp_per_turn(3, "technocracy"), 4)
check("E11 monarchy 3", rp_per_turn(3, "constitutional_monarchy"), 3)
check("E11 junta 3", rp_per_turn(3, "military_junta"), 2)
check("E11 technocracy 0", rp_per_turn(0, "technocracy"), 0)
check("E11 junta 0", rp_per_turn(0, "military_junta"), 0)

# ------------------------------- Example 12: delayed policy with treasury
t = 1529
t += 150 - 30
check("E12 treasury after T", t, 1649)
t += tax_income(50000, 400) - service_cost(tax_income(50000, 400), 5000, 0)
check("E12 treasury after T+1", t, 1749)
check("E12 cooldown", 0 + 12, 12)

# ------------------------------------ Example 13: technocracy selection
tech = supports(order="BALANCED")
check("E13 legitimacy", legitimacy("technocracy", tech), 53)
check("E13 stability target", stability_target(55, "technocracy"), 9850)

# ---------------------------------------- Example 14: order change timing
check("E14 OPEN stability term", ORDER["OPEN"]["stab"], -200)
for key, val in (("labour", 6), ("rural", -4), ("industry", 2),
                 ("commerce", 8), ("scholars", 10), ("security", -15)):
    check("E14 OPEN %s" % key, ORDER["OPEN"][key], val)

# ------------------------------------------- Example 15: reroll resets
new_state = dict(population=50000, approval=approval_target(s1), stability=10000)
check("E15 population", new_state["population"], 50000)
check("E15 approval", new_state["approval"], 55)
check("E15 stability", new_state["stability"], 10000)
check("E15 legitimacy", legitimacy("constitutional_monarchy", s1), 54)

# ------------------------------- Example 16: long-run comparison at 70
expected = {"democracy": 124, "constitutional_monarchy": 126,
            "absolute_monarchy": 128, "dictatorship": 126,
            "military_junta": 126, "technocracy": 123}
nets = {}
for g in GOV:
    order = "FIRM" if g == "military_junta" else "BALANCED"
    st = stability_target(70, g, order=order)
    gross = tax_income(50000, 300, st)
    net = gross - service_cost(gross, 2000, GOV[g]["svc"])
    nets[g] = net
    check("E16 net %s" % g, net, expected[g])
check("E16 120-turn absolute", nets["absolute_monarchy"] * 120, 15360)
check("E16 120-turn technocracy", nets["technocracy"] * 120, 14760)
check("E16 spread", (nets["absolute_monarchy"] - nets["technocracy"]) * 120, 600)
check_true("E16 spread under 10%",
           (nets["absolute_monarchy"] - nets["technocracy"]) * 100
           < nets["absolute_monarchy"] * 10)
check("E16 research technocracy", rp_per_turn(3, "technocracy") * 120, 480)
check("E16 research monarchy", rp_per_turn(3, "constitutional_monarchy") * 120, 360)
check("E16 research junta", rp_per_turn(3, "military_junta") * 120, 240)

# ------------------------------------------- Example 17: unfunded service
s17 = supports(service=0)
check("E17 labour", s17["labour"], 50)
check("E17 rural", s17["rural"], 63)
check("E17 industry", s17["industry"], 56)
check("E17 commerce", s17["commerce"], 51)
check("E17 scholars", s17["scholars"], 48)
check("E17 security", s17["security"], 48)
check("E17 weighted", sum(s17[k] * WEIGHTS[k] for k in WEIGHTS), 5290)
check("E17 target", approval_target(s17), 52)

# ---------------------------------------------- Example 18: crowding
pop, hous = 60000, 50000
cb = crowding_bp(pop, hous)
check("E18 crowding", cb, 1666)
gbp = growth_bp(55, pop, hous, crowding=cb)
check("E18 growth", gbp, 34)
check("E18 natural", pop + pop * gbp // 10000, 60204)
check("E18 new population", apply_growth(pop, hous, gbp, crowding=cb), 59000)
check("E18 second excess", 59000 - hous, 9000)
check("E18 second crowding", crowding_bp(59000, hous), 1525)
check("E18 second decline", -(-9000 // 10), 900)
check("E18 stability penalty", cb // 10, 166)
# the excess decays by ~10% a turn; less than 1,000 remains after 22 turns
excess = 10000
for _ in range(22):
    excess -= -(-excess // 10)
check_true("E18 excess under 1,000 after 22 turns", excess < 1000, str(excess))

# ------------------------------------- term ranges stated in the register
# Every register "Range" cell must be the true range of its term at the
# documented input bounds, otherwise the published bound is a false claim.
# There is ONE implementation of the tax term here — the authoritative signed
# `(300 - tax) // step` of F-PD-004/005/006/007/008, which `supports()` also
# uses. The superseded `-((tax - 300) // step)` helpers that used to sit here
# expected +3/+7/+9 and -2/-6/-8; they contradicted the register and are gone.
def tax_term(tax, step):
    return (300 - tax) // step


check("range labour tax max", tax_term(200, 40), 2)
check("range labour tax min", tax_term(400, 40), -3)
check("range industry tax max", tax_term(200, 15), 6)
check("range industry tax min", tax_term(400, 15), -7)
check("range commerce tax max", tax_term(200, 12), 8)
check("range commerce tax min", tax_term(400, 12), -9)
# Rural (F-PD-005, step 20) and Scholars (F-PD-008, step 50) use the same
# signed term. Their cells' ±5 and ±2 must be the true bounds.
check("range rural tax max", tax_term(200, 20), 5)
check("range rural tax min", tax_term(400, 20), -5)
check("range scholars tax max", tax_term(200, 50), 2)
check("range scholars tax min", tax_term(400, 50), -2)
check_true("range rural tax bounded",
           all(-5 <= tax_term(t, 20) <= 5 for t in range(200, 401)))
check_true("range scholars tax bounded",
           all(-2 <= tax_term(t, 50) <= 2 for t in range(200, 401)))
# The two notations are NOT interchangeable between settings: at tax 250 the
# older `- floor((tax - 300)/20)` gives +3 and the signed term +2. This is why
# B-06 publishes the register's form for all five terms.
check("old vs signed rural at 250", -((250 - 300) // 20), 3)
check("signed rural at 250", tax_term(250, 20), 2)
check("range rural stability min", (5000 - 10000) // 500, -10)
check("range rural stability max", (11000 - 10000) // 500, 2)
check("range industry stability min", (5000 - 10000) // 400, -13)
check("range industry stability max", (11000 - 10000) // 400, 2)
check("range commerce stability min", (5000 - 10000) // 400, -13)
check("range security stability min", (5000 - 10000) // 400, -13)
check("range food share max", 10000 // 250, 40)
check("range processing share max", 10000 // 250, 40)
check("range rural service max", 5000 // 1000, 5)
check("range housing min", 0 // 500 - 18, -18)
check("range housing max", 10000 // 500 - 18, 2)
check("range warehouse min", 0 // 1000 - 5, -5)
check("range warehouse max", 10000 // 1000 - 5, 5)
check("range service cost max", service_cost(200, 5000, 500), 105)
check("range service cost share", service_cost(200, 5000, 500) * 10000 <= 200 * 5250 + 10000, True)

# ------------------------------------------------------- document checks
here = os.path.dirname(os.path.abspath(__file__))
doc = os.path.join(here, "..", "stage-2", "12_population_and_domestic_politics.md")
reg = os.path.join(here, "..", "stage-2",
                   "12_population_and_domestic_politics_formula_register.md")
dec = os.path.join(here, "..", "DECISIONS.md")
req = os.path.join(here, "..", "stage-2", "03_requirements_traceability.md")
prog = os.path.join(here, "..", "PROJECT_PROGRESS.md")
log = os.path.join(here, "..", "stage-2", "06_stage_2_progress_log.md")
summary = os.path.join(here, "..", "stage-2", "04_approved_and_provisional_decisions.md")
handoff = os.path.join(here, "..", "AI_HANDOFF.md")
context = os.path.join(here, "..", "AI_CONTEXT.md")

body = open(doc, encoding="utf-8").read()
regtext = open(reg, encoding="utf-8").read()
dectext = open(dec, encoding="utf-8").read()
reqtext = open(req, encoding="utf-8").read()
progtext = open(prog, encoding="utf-8").read()
logtext = open(log, encoding="utf-8").read()
sumtext = open(summary, encoding="utf-8").read()
handofftext = open(handoff, encoding="utf-8").read()
contexttext = open(context, encoding="utf-8").read()


def dmp_section(marker):
    """The text of one DMP entry, from its bold heading to the next entry.

    Used to check a formula *where it is published* instead of trusting the
    checker's own arithmetic: a stale expression in B-06 is a real defect even
    when this file computes the right answer.
    """
    start = body.index(marker)
    nxt = body.find("**DMP-", start + len(marker))
    return body[start:nxt if nxt != -1 else len(body)]

check("B-06 example count", len(re.findall(r"^### Example \d+", body, re.M)), 49)
for i in (4, 5, 6, 7, 8, 9):
    check("F-PD-00%d in register" % i, ("**F-PD-00%d" % i) in regtext, True)
for i in range(1, 26):
    check("F-PD-%03d in register" % i, ("**F-PD-%03d" % i) in regtext, True)
check_true("D-084 recorded", "| D-084 |" in dectext)
check_true("D-091 recorded", "| D-091 |" in dectext)
check_true("REQ-325 recorded", "| REQ-325 |" in reqtext)
check_true("B-06 marks 06A incomplete", "06B" in body and "pending" in body)
check_true("weights documented as fixed", "fixed" in body.lower())
# Prose tokens: the corrected numbers must appear in the specification itself,
# not only in this checker.
check_true("E8 weighted sum in prose", "= 5,520" in body)
check_true("E10 junta net in prose", "**126**" in body)
check_true("E10 crossover in prose", "approval 75" in body)
check_true("E18 crowding in prose", "1,666" in body)
check_true("E1 stability in prose", "10,200" in body)
check_true("register revision block present", "## 14. Revision history" in regtext)
# The corrected prose and range cells must not silently drift back.
check_true("E10 no stale junta target", "10,550" not in body)
check_true("E10 junta target in prose", "10,600 → cap **10,600**" in body)
check_true("E16 technocracy cost in prose", "gives up **600 crowns**" in body)
check_true("E16 junta cost in prose", "gives up **240 crowns**" in body)
check_true("DMP-166 spread denominator", "8.1% of the best" in body)
check_true("DMP-094 stability value", "4.5 crowns per turn" in body)
check_true("DMP-097 HIGH net", "`HIGH` nets **100**" in body)
check_true("range labour cell", "terms 0…+12 / **−3…+2 at 200/300/400** / −18…+2 / −30 / ±6" in regtext)
check_true("range rural cell", "0…+40 / 0…+5 / −5…+5 / −20 / −10…+2 / ±4" in regtext)
check_true("range industry cell", "0…+40 / **−7…+6 at 200/300/400** / −5…+5 / −13…+2 / ±2" in regtext)
check_true("range commerce cell", "−5…+5 / **−9…+8 at 200/300/400** / −13…+2 / ±8" in regtext)
check_true("range security cell", "0…+2 / −15 / −13…+2 / ±15" in regtext)
# Source synchronisation (2026-10-25): the formula blocks in B-06 must carry the
# register's signed tax term. This is the check that failed to exist when
# DMP-066/068/069 still showed `− floor((tax_bp − 300) / divisor)` while
# F-PD-004/006/007 were already corrected — every arithmetic test passed and the
# prose was still wrong. A stale block in either document now fails.
for marker, group, step in (("**DMP-066 — Labour.**", "labour", 40),
                            ("**DMP-067 — Rural producers.**", "rural", 20),
                            ("**DMP-068 — Industry.**", "industry", 15),
                            ("**DMP-069 — Commerce.**", "commerce", 12),
                            ("**DMP-070 — Scholars.**", "scholars", 50)):
    sec = dmp_section(marker)
    check_true("%s signed tax term in B-06" % group,
               ("+ (300 − tax_bp) // %d" % step) in sec)
    check_true("%s superseded floor term absent from B-06" % group,
               ("− floor((tax_bp − 300) / %d)" % step) not in sec)
    check_true("%s signed tax term in register" % group,
               ("(300 − tax_bp) // %d" % step) in regtext)
    check_true("%s superseded floor term absent from register" % group,
               ("− floor((tax_bp − 300) / %d)" % step) not in regtext)
for step in (40, 20, 15, 12, 50):
    check_true("no superseded tax term /%d anywhere in B-06" % step,
               ("− floor((tax_bp − 300) / %d)" % step) not in body)
# Final micro-correction: the floor and the signed tax term must remain
# visible in the documents, not only in this checker.
# The prose rule must carry the clamp too: a corrected register with an
# unclamped DMP-030a would still teach a developer the old behaviour.
sec30 = dmp_section("**DMP-030a — The 1,000 floor binds every path.**")
check_true("DMP-030a states the clamp", "max(1,000, raw)" in sec30)
check_true("DMP-030a states the 993 case",
           "natural = 1,000 + floor(1,000 × −63/10,000) = 993" in sec30)
check_true("DMP-030a closes at 1,000", "the result is **1,000**, not 993" in sec30)
check_true("F-PD-002 floor expression", "new_population = max(1,000, raw)" in regtext)
check_true("F-PD-002 floor example", "natural = 1,000 + floor(1,000 × −63/10,000) = 993" in regtext)
check_true("F-PD-002 floor result", "max(1,000, 993)" in regtext)
check_true("DMP-071a labour", "| Labour | 40 | **+2** | 0 | **−3** | **−3…+2** |" in body)
check_true("DMP-071a industry", "| Industry | 15 | **+6** | 0 | **−7** | **−7…+6** |" in body)
check_true("DMP-071a commerce", "| Commerce | 12 | **+8** | 0 | **−9** | **−9…+8** |" in body)
check_true("DMP-099 LOW approval", "56 (`LOW`), 55 (`STANDARD`) and 54 (`HIGH`)" in body)
check_true("DMP-168 LOW target", "| `LOW` | 100 | 0 | **100** | 56 |" in body)
check_true("E5 labour support", "| Labour support | 55 | 59 | +4 |" in body)
check_true("register signed tax row", "| `300 − tax_bp` |" in regtext)
check_true("D-091 fiscal approvals", "**56 / 55 / 54**" in dectext)
check_true("constant rural service", "| `service_share_bp` | rural | 1,000 | +5 |" in regtext)
check_true("constant food share", "| `food_share_bp` | rural | 250 | 0…+40 |" in regtext)
check_true("constant processing share", "| `processing_share_bp` | industry | 250 | 0…+40 |" in regtext)
check_true("constant tax caps", "−3…+2 / ±5 / −7…+6 / −9…+8 / ±2" in regtext)
check_true("constant stability caps", "−10…+2 / −13…+2 / −13…+2 / −13…+2" in regtext)

# ================================================================ Prompt 06B
# Elections, campaigns, retention, crisis and recovery. Same discipline: every
# number below is recomputed from the register's constants, and the prose that
# publishes it is checked separately further down.

W6 = {"labour": 30, "rural": 15, "industry": 20, "commerce": 15,
      "scholars": 10, "security": 10}
EW6 = {"labour": 2443, "rural": 1765, "industry": 1991, "commerce": 1357,
       "scholars": 1358, "security": 1086}
IV6 = {"constitutional_monarchy": {"labour": 10, "rural": 20, "industry": 15,
                                     "commerce": 15, "scholars": 20, "security": 20},
       "military_junta": {"labour": 0, "rural": 0, "industry": 0, "commerce": 0,
                          "scholars": 0, "security": 100}}
THRESH6 = {"constitutional_monarchy": 45, "absolute_monarchy": 40,
           "dictatorship": 35, "military_junta": 40, "technocracy": 42}
START6 = {"labour": 55, "rural": 65, "industry": 56, "commerce": 51,
          "scholars": 53, "security": 49}


def approval6(s):
    return sum(W6[k] * s[k] for k in W6) // 100


def legitimacy6(s, gov):
    return sum(IV6[gov][k] * s[k] for k in W6) // 100


def vote6(s, camp=None, inc=200):
    camp = camp or {}
    sc = {k: max(0, min(100, s[k] + camp.get(k, 0))) for k in W6}
    total = sum(EW6[k] * sc[k] for k in W6)
    return total // 100 + inc, sc, total


def confidence6(s, gov="constitutional_monarchy", camp=None):
    camp = camp or {}
    sc = {k: max(0, min(100, s[k] + camp.get(k, 0))) for k in W6}
    return sum(IV6[gov][k] * sc[k] for k in W6)


def challengers6(ap, leg):
    return (max(3600, min(6400, 4400 + (60 - ap) * 40)),
            max(3600, min(6400, 4300 + (55 - leg) * 30)))


def winner6(v, pf, ib):
    """F-PD-034: highest score, incumbent first, then candidate index."""
    scores = [(v, 0), (pf, 1), (ib, 2)]
    best = max(x[0] for x in scores)
    tied = sorted(i for sc, i in scores if sc == best)
    return tied[0]


def status6(state):
    return {"NORMAL": 0, "ELECTORAL": 0, "SUCCESSION": 0,
            "TRANSITION": 800, "CRISIS": 1500, "RECOVERY": 400}[state]


def crisis_run(pop, rate, stab, treasury, opex, turns, penalty):
    target = max(5000, min(11000, 10000 - penalty))
    rows = []
    for t in range(1, turns + 1):
        inc = pop * rate * stab // 1_000_000_000
        treasury += inc - opex
        stab += max(-250, min(250, target - stab))
        rows.append((inc, treasury, stab))
    return rows


# ---- schedule, window and campaign arithmetic
check("E19 term hours", 240 * 2, 480)
check("E19 term days", 480 // 24, 20)
check("E20 first contest", 137 + 240, 377)
check("E20 second contest", 377 + 240, 617)
check("E20 postponed anchor", 377 + 240, 617)
check("E21 campaign open", 1000 - 24, 976)
check("E21 registration close", 1000 - 12, 988)
check("E21 final notice", 1000 - 2, 998)
check("E22 turnout sum", sum(EW6.values()), 10000)
check("E23 rally 50k", 2 * -(-50000 // 1000), 100)
check("E23 rally 500k", 2 * -(-500000 // 1000), 1000)
check("E24 advert 50k x2", 2 * (3 * -(-50000 // 1000)), 300)
check("E24 full campaign 50k", 2 * 50 + 2 * 3 * 50, 400)
check("E24 full campaign 500k", 2 * 500 + 2 * 3 * 500, 4000)
check("E25 rally cap", min(6, 2 + 3), 5)
check("E25 advert cap", min(6, 2 + 2 + 2), 6)
# ---- vote arithmetic
V_START = vote6(START6)
check("E26 total", V_START[2], 554981)
check("E26 vote", V_START[0], 5749)
check("E26 approval", approval6(START6), 55)
check("E26 challengers", challengers6(55, 55), (4600, 4300))
check("E26 margin", V_START[0] - 4600, 1149)
LOW6 = {"labour": 40, "rural": 50, "industry": 41, "commerce": 36,
        "scholars": 38, "security": 34}
V_LOW = vote6(LOW6)
check("E27 total", V_LOW[2], 404981)
check("E27 vote", V_LOW[0], 4249)
check("E27 approval", approval6(LOW6), 40)
check("E27 challengers", challengers6(40, 40), (5200, 4750))
check("E27 deficit", 5200 - V_LOW[0], 951)
NARROW6 = {"labour": 55, "rural": 40, "industry": 47, "commerce": 45,
           "scholars": 40, "security": 50}
V_N = vote6(NARROW6)
check("E28 total", V_N[2], 468227)
check("E28 vote", V_N[0], 4882)
check("E28 approval", approval6(NARROW6), 47)
check("E28 challengers", challengers6(47, 47), (4920, 4540))
check("E28 margin", 4920 - V_N[0], 38)
PLAT6 = {"rural": 2, "scholars": 2, "security": 2}
V_P = vote6(NARROW6, PLAT6)
check("E29 total", V_P[2], 476645)
check("E29 vote", V_P[0], 4966)
check("E29 gain", V_P[0] - V_N[0], 84)
check("E29 win", V_P[0] - 4920, 46)
check("E29 alt allocation", (2 * 2443 + 2 * 1991 + 2 * 1357) // 100, 115)
check("E30 tie returns incumbent", winner6(5000, 5000, 4700), 0)
check("E30 incumbent on score", winner6(5100, 4800, 4800), 0)
check("E30 challenger index", winner6(4700, 4800, 4800), 1)
# ---- confidence
check("E31 confidence", confidence6(START6), 5495)
check("E31 carries by", 5495 - 4500, 995)
CONF_FAIL6 = {"labour": 44, "rural": 40, "industry": 44, "commerce": 40,
              "scholars": 42, "security": 44}
check("E32 confidence", confidence6(CONF_FAIL6), 4220)
check("E32 fails by", 4500 - 4220, 280)
check("E33 early motion confidence", confidence6({"labour": 44, "rural": 40, "industry": 44,
                                                 "commerce": 40, "scholars": 42,
                                                 "security": 44}), 4220)
check("E33 pressure window", 12, 12)
check("E34 transition hours", 12 * 2, 24)
# ---- transition and crisis economics
T12 = crisis_run(50000, 300, 10000, 1500, 121, 12, 800)
check("E35 tax total", sum(r[0] for r in T12), 1680)
check("E35 treasury", T12[-1][1], 1728)
check("E35 normal tax", 12 * 150, 1800)
check("E35 cost", 1800 - 1680, 120)
check("E36 junta margin at 44", 44 - 40, 4)
check("E36 junta pressure at 39", 39 < 40, True)
check("E37 pressure window", 12, 12)
check("E38 dictatorship threshold", THRESH6["dictatorship"], 35)
C18 = crisis_run(50000, 300, 10000, 1500, 121, 18, 1500)
check("E39 tax total", sum(r[0] for r in C18), 2366)
check("E39 treasury", C18[-1][1], 1688)
check("E39 tax cost", 18 * 150 - 2366, 334)
C500 = crisis_run(500000, 300, 10000, 20000, 1210, 18, 1500)
check("E40 tax total", sum(r[0] for r in C500), 23736)
check("E40 treasury", C500[-1][1], 21956)
check("E40 tax cost", 18 * 1500 - 23736, 3264)
check("E41 output-multiplier treasury", 1500 - 36 * 121, -2856)
check("E41 insolvent turn", -(-1500 // 121), 13)
# Batch-cap counterfactual (DMP-246, E41/E42, corrected 2026-10-28): the
# register's default arithmetic is one floor per division (register §2), so
# the 25% variable cost is floor(110 × 25 / 100) = 27 and the per-turn cost is
# 11 + 27 = 38. The superseded model used a rounded 27.5 → 39 and mixed 38
# with 39 in the same table.
BATCH_COST = 11 + 110 * 25 // 100
check("E41 batch-cap cost", BATCH_COST, 38)
check("E41 batch-cap treasury", 1500 - 36 * BATCH_COST, 132)
check("E41 zero-tax loss", 36 * 150, 5400)
check("E42 output-multiplier 48", 1500 - 48 * 121, -4308)
check("E42 batch-cap 48", 1500 - 48 * BATCH_COST, -324)
check("E42 first unpaid obligation", -(-1500 // BATCH_COST), 40)
check("E42 pays 39 turns then fails", 39 * BATCH_COST <= 1500 < 40 * BATCH_COST, True)
check("E42 zero-tax loss 48", 48 * 150, 7200)
check("E43 food at 25%", 60 * 25 // 100, 15)
check("E43 stock after 3", 120 + 3 * (15 - 50), 15)
check("E43 stock after 4", 120 + 4 * (15 - 50), -20)
check("E44 food unchanged", 60 - 50, 10)
check("E45 early exit", 46 >= 40 + 5, True)
check("E45 no early exit at 44", 44 >= 45, False)
check("E47 first contest", 100 + 240, 340)
check("E47 campaign open", 340 - 24, 316)
check("E49 scheduled campaign", 240 - 24, 216)
check("E49 early motion turn", 150 + 12, 162)
check("E49 early before campaign", 162 < 216, True)
check("E48 reroll contest", 100 + 240, 340)

# ---- Part II document checks
for dmp in (134, 138, 146, 150, 157, 166, 176, 186, 196, 201, 207, 214, 231):
    check_true("DMP-%d published" % dmp, ("**DMP-%d —" % dmp) in body)
check_true("DMP-274 closes Part II", "**DMP-274 —" in body)
for fpd in range(26, 45):
    check_true("F-PD-%03d in register" % fpd, ("**F-PD-%03d —" % fpd) in regtext)
check_true("register turnout table", "| Scholars | 10 | 15 | **1,358** |" in regtext)
check_true("register crisis penalty row", "| Stability penalty — crisis | **1,500** | bp |" in regtext)
check_true("register election term row", "| Election term | **240** | turns |" in regtext)
check_true("register threshold table", "| `gov_military_junta` | 40 | `CRISIS` |" in regtext)
check_true("E26 table in prose", "| **Total** | | **10,000** | **554,981** |" in body)
check_true("E26 vote in prose", "5,749" in body)
check_true("E27 vote in prose", "4,249" in body)
check_true("E28 vote in prose", "4,882" in body)
check_true("E29 vote in prose", "**4,966**" in body)
check_true("E31 confidence in prose", "5,495" in body)
check_true("E32 confidence in prose", "4,220" in body)
check_true("E39 tax in prose", "2,366" in body)
check_true("E39 treasury in prose", "1,688" in body)
check_true("E40 tax in prose", "23,736" in body)
check_true("E40 treasury in prose", "21,956" in body)
check_true("E41 insolvency in prose", "−2,856" in body)
check_true("E42 batch-cap in prose", "−324" in body)
check_true("batch-cap cost in prose", "38/turn" in body or "38/turn" in reqtext)
check_true("superseded 39/turn is gone", "39/turn" not in body)
check_true("superseded −372 is gone", "−372" not in body)
check_true("E43 food in prose", "floor(60 × 0.25) = 15" in body)
check_true("E45 early exit in prose", "40 + 5 = 45" in body)
check_true("term conversion in prose", "240 × 2 = 480 hours = 20 days" in body)
check_true("crisis duration in prose", "**18 turns (36 hours)**" in body)
check_true("transition duration in prose", "**12 turns (24 hours)**" in body)
check_true("no production multiplier", "**Production continues unchanged.**" in body)
check_true("no tax multiplier", "**Tax continues unchanged**" in body)
check_true("rejection is explicit", "The proposal is **rejected**" in body)
check_true("government never changes in 06B", "does not change `government_id`" in body)
check_true("campaign money is a ledger entry", "`CAMPAIGN_RALLY`" in body)
check_true("P4.4 defined", "P4.4" in body)
check_true("turnout is not approval", "not the population weights" in body)

# -------------------------------- 2026-10-28 schedule model and document guards
# The election-state contradiction, the schedule anchor, the once-only window,
# the long-dormancy catch-up and the rejected-crisis arithmetic were corrected
# on 2026-10-28. The model below recomputes the schedule; the guards check that
# the *documents* still state the corrected rules. `--self-test` additionally
# proves that each guard fails when its defect is reintroduced into an in-memory
# copy of the real text; no file is modified by that mode.


BLOCKING_STATES = ("TRANSITION", "CRISIS", "RECOVERY")


def eligible_at(turn, available_from=0, blocked=()):
    """Eligibility as a predicate, so an interruption is expressible.

    `blocked` is a sequence of half-open [start, end) ranges: the nation is in
    `TRANSITION`, `CRISIS` or `RECOVERY` (or dormant/protected) on those turns.
    """
    if turn < available_from:
        return False
    return not any(start <= turn < end for start, end in blocked)


def simulate_contest(scheduled, available_from=0, blocked=(), horizon=4000):
    """DMP-181/181b as executable code: one window per contest.

    The opening is searched **once**, at the first eligible turn at or after
    `scheduled - 24`. Its deadline is 24 turns later. The contest then resolves
    at the first eligible turn at or after `max(scheduled, deadline)`.

    A blocking state that begins after the opening therefore delays resolution
    only: it never moves the opening, never restarts the 24 turns, and never
    resolves the contest before its anchor. A nation that was ineligible at
    `scheduled - 24` is the other case: no window has opened yet, so one opens
    at its first eligible turn and runs a full 24 turns.
    """
    opening = None
    for turn in range(scheduled - 24, scheduled + horizon):
        if eligible_at(turn, available_from, blocked):
            opening = turn
            break
    if opening is None:
        raise AssertionError("no eligible turn for a contest due at %d" % scheduled)
    deadline = opening + 24
    for turn in range(max(scheduled, deadline), scheduled + horizon):
        if eligible_at(turn, available_from, blocked):
            return opening, turn
    raise AssertionError("no resolution turn for a contest due at %d" % scheduled)


def campaign_record(scheduled, available_from=0, blocked=(), horizon=4000):
    """DMP-178/F-PD-028: every campaign date, from its own opening.

    `campaign_open_turn` is the single anchor for the four offsets. For an
    on-time campaign it is `scheduled - 24` and the offsets coincide with
    `T-24`, `T-12`, `T-2`; for a delayed opening they do not, and using the
    scheduled turn would put registration or notice in the past.
    """
    opening, resolved = simulate_contest(scheduled, available_from, blocked, horizon)
    return {
        "scheduled": scheduled,
        "open": opening,
        "registration": opening + 12,
        "notice": opening + 22,
        "deadline": opening + 24,
        "resolved": resolved,
    }


def campaign_actionable(turn, record, eligible):
    """DMP-183: a campaign action needs an open, restored window."""
    return record["open"] <= turn < record["deadline"] and eligible


def restored_state(turn, deadline, eligible):
    """DMP-181b/DMP-236: what the last cleared blocker restores."""
    return "ELECTORAL" if turn < deadline and eligible else "NORMAL"


def superseded_resolution(scheduled, eligible_from):
    """The defect this correction removes, kept so the test can prove it wrong.

    It treats *every* delay as a new window: if the campaign had already opened
    and was then interrupted, this returns `interruption + 24` instead of the
    first eligible turn at or after the anchor. Case C below is the proof.
    """
    return max(scheduled - 24, eligible_from) + 24


def next_anchor(scheduled, resolved):
    """DMP-181a: `scheduled + 240 x k`, the first anchor whose window still
    opens strictly after the resolution."""
    k = 1
    while scheduled + 240 * k < resolved + 25:
        k += 1
    return scheduled + 240 * k, k


# label, anchor, first available turn, blocked ranges, open, resolution, k, next
SCHEDULE_CASES = [
    # Cases A-E are the five lifecycle cases of the correction brief.
    ("Case A on time", 1000, 900, (), 976, 1000, 1, 1240),
    ("Case B block clears before the anchor", 1000, 900, ((980, 990),), 976, 1000, 1, 1240),
    ("Case C block clears after the anchor", 1000, 900, ((980, 1010),), 976, 1010, 1, 1240),
    ("Case D ineligible at the scheduled opening", 1000, 980, (), 980, 1004, 1, 1240),
    ("Case E block clears at 1020", 1000, 900, ((980, 1020),), 976, 1020, 1, 1240),
    # Postponement before the window has opened: a full window still runs.
    ("Case F blocked before the window until 360", 377, 0, ((0, 360),), 360, 384, 1, 617),
    ("Case G blocked past the anchor to 387", 377, 0, ((0, 387),), 387, 411, 1, 617),
    ("delayed opening at the anchor, then interrupted", 377, 0, ((0, 377), (384, 401)), 377, 401, 1, 617),
    ("Case H two interruptions inside one window", 1000, 900, ((980, 985), (988, 995)), 976, 1000, 1, 1240),
    # Dormancy and long absence.
    ("short dormancy before the window changes nothing", 377, 300, (), 353, 377, 1, 617),
    ("eligible only from the anchor", 377, 377, (), 377, 401, 1, 617),
    ("returned after one missed cycle", 377, 700, (), 700, 724, 2, 857),
    ("returned 250 turns after the anchor", 377, 627, (), 627, 651, 2, 857),
    ("returned 300 turns after the anchor", 377, 677, (), 677, 701, 2, 857),
    ("returned 400 turns after the anchor", 377, 777, (), 777, 801, 2, 857),
    ("returned after three whole cycles", 377, 1097, (), 1097, 1121, 4, 1337),
    ("returned after several cycles at scale", 377, 2700, (), 2700, 2724, 10, 2777),
]

for label, scheduled, available, blocked, exp_open, exp_res, exp_k, exp_next in SCHEDULE_CASES:
    got_open, got_res = simulate_contest(scheduled, available, blocked)
    check("schedule %s: window open" % label, got_open, exp_open)
    check("schedule %s: resolution" % label, got_res, exp_res)
    got_next, got_k = next_anchor(scheduled, got_res)
    check("schedule %s: next anchor" % label, got_next, exp_next)
    check("schedule %s: catch-up multiplier" % label, got_k, exp_k)
    # The window is always 24 turns (deadline = opening + 24). Resolution may be
    # later when a blocking state interrupted the window; asserting
    # `resolution - opening == 24` would encode the very defect being fixed.
    check("schedule %s: resolution is at or after the 24-turn deadline" % label,
          exp_res >= exp_open + 24, True)
    check("schedule %s: next window opens after the resolution" % label,
          exp_next - 24 > exp_res, True)
    check("schedule %s: resolution never before the anchor" % label, exp_res >= scheduled, True)
    check("schedule %s: resolution is not inside a blocked range" % label,
          not any(a <= exp_res < b for a, b in blocked), True)
    # One evaluation, one next contest: re-running the same closed contest must
    # return the same anchor and multiplier, never a duplicate election.
    check("schedule %s: one next anchor under re-evaluation" % label,
          next_anchor(scheduled, exp_res), (exp_next, exp_k))

# DMP-178/F-PD-028: the deadline convention, ordinary and delayed. Every date is
# derived from the campaign's own opening; a delayed campaign cannot be made to
# obey `T-12`/`T-2`, because those turns are already behind it.
# label, scheduled, available, blocked, open, registration, notice, deadline, resolved
DEADLINE_CASES = [
    ("ordinary campaign", 1000, 900, (), 976, 988, 998, 1000, 1000),
    ("delayed until T-20", 1000, 980, (), 980, 992, 1002, 1004, 1004),
    ("delayed until T-10", 1000, 990, (), 990, 1002, 1012, 1014, 1014),
    ("delayed until after T", 1000, 1010, (), 1010, 1022, 1032, 1034, 1034),
    ("delayed, then interrupted", 1000, 980, ((990, 995),), 980, 992, 1002, 1004, 1004),
    ("delayed, blocked past its deadline", 1000, 980, ((990, 1010),), 980, 992, 1002, 1004, 1010),
    ("ordinary, interrupted twice", 1000, 900, ((980, 985), (988, 995)), 976, 988, 998, 1000, 1000),
]

for label, scheduled, available, blocked, exp_open, exp_reg, exp_notice, exp_deadline, exp_res in DEADLINE_CASES:
    rec = campaign_record(scheduled, available, blocked)
    check("deadline %s: opening" % label, rec["open"], exp_open)
    check("deadline %s: registration closes" % label, rec["registration"], exp_reg)
    check("deadline %s: final notice" % label, rec["notice"], exp_notice)
    check("deadline %s: deadline" % label, rec["deadline"], exp_deadline)
    check("deadline %s: resolution" % label, rec["resolved"], exp_res)
    check("deadline %s: 12 turns from open to registration" % label,
          rec["registration"] - rec["open"], 12)
    check("deadline %s: 22 turns from open to notice" % label,
          rec["notice"] - rec["open"], 22)
    check("deadline %s: 24 turns from open to deadline" % label,
          rec["deadline"] - rec["open"], 24)
    check("deadline %s: no registration or notice in the past at opening" % label,
          rec["registration"] > rec["open"] and rec["notice"] > rec["open"], True)
    check("deadline %s: resolution never before the anchor" % label, rec["resolved"] >= scheduled, True)
    check("deadline %s: resolution at or after the deadline" % label, rec["resolved"] >= rec["deadline"], True)
    check("deadline %s: next anchor comes from the scheduled turn" % label,
          next_anchor(scheduled, rec["resolved"]), (scheduled + 240, 1))
    check("deadline %s: re-evaluation is stable" % label,
          campaign_record(scheduled, available, blocked), rec)

# DMP-188/DMP-190: the ballot and the platform lock use the campaign's own
# registration close. On an on-time campaign that is `T-12`; on a delayed one it
# is `campaign_open_turn + 12`, and using `T-12` would lock the ballot before the
# campaign had even opened.
def ballot_turn(rec):
    """DMP-188/DMP-190: ballot and platform lock share one deadline."""
    return rec["registration"]


def submission_legal(turn, rec, eligible=True):
    """DMP-183/F-PD-028/F-PD-029: open window, before `resolution_turn`."""
    return campaign_actionable(turn, rec, eligible)


ordinary = campaign_record(1000, 900)
delayed = campaign_record(1000, 980)
late = campaign_record(1000, 1010)
check("ballot: an ordinary campaign fixes the ballot at 988", ballot_turn(ordinary), 988)
check("ballot: a delayed campaign fixes the ballot at 992", ballot_turn(delayed), 992)
check("ballot: the delayed ballot is not the stale T-12 turn", ballot_turn(delayed) == 988, False)
check("ballot: the platform lock equals the ballot", ballot_turn(delayed), delayed["open"] + 12)
check("ballot: the delayed ballot is after the opening", ballot_turn(delayed) > delayed["open"], True)
check("ballot: a campaign opened after T registers after T", ballot_turn(late) > 1000, True)
check("ballot: no delayed campaign registers before it opens",
      all(ballot_turn(campaign_record(1000, a)) > a for a in (980, 990, 1010)), True)
# The superseded rule closed every campaign at `T`. The delayed campaign is still
# legal at its anchor, and closes at its own resolution turn.
check("submission: a delayed campaign is legal at its anchor T", submission_legal(1000, delayed), True)
check("submission: the superseded `< T` rule would have closed it", 1000 < 1000, False)
check("submission: it is legal on the last open turn", submission_legal(1003, delayed), True)
check("submission: it closes at the resolution turn", submission_legal(1004, delayed), False)
check("submission: no action while a blocker is active", submission_legal(1000, delayed, False), False)
check("submission: an ordinary campaign is legal at T-1", submission_legal(999, ordinary), True)
check("submission: an ordinary campaign closes at T", submission_legal(1000, ordinary), False)
check("submission: a campaign opened after T is legal at 1011", submission_legal(1011, late), True)
check("submission: it closes at 1034", submission_legal(1034, late), False)

# DMP-181b/DMP-236: what a cleared blocker restores. Before the deadline the
# nation returns to `ELECTORAL` for the remaining turns; at or after it, to
# `NORMAL` and a postponed resolution. Consecutive blockers restore nothing.
ordinary = campaign_record(1000, 900)
check("restoration: remaining window is ELECTORAL",
      restored_state(990, ordinary["deadline"], True), "ELECTORAL")
check("restoration: at the deadline it is NORMAL",
      restored_state(1000, ordinary["deadline"], True), "NORMAL")
check("restoration: after the deadline it is NORMAL",
      restored_state(1010, ordinary["deadline"], True), "NORMAL")
check("restoration: an active blocker restores nothing",
      restored_state(990, ordinary["deadline"], False), "NORMAL")
check("restoration: campaign actions resume at 990", campaign_actionable(990, ordinary, True), True)
check("restoration: no action during the block", campaign_actionable(985, ordinary, False), False)
check("restoration: no action at the deadline", campaign_actionable(1000, ordinary, True), False)
check("restoration: no action after the deadline", campaign_actionable(1010, ordinary, True), False)
consecutive = ((980, 1012),)
check("consecutive blockers: no ELECTORAL turn in the gap",
      any(restored_state(t, ordinary["deadline"], eligible_at(t, 0, consecutive)) == "ELECTORAL"
          for t in range(980, 1012)), False)
check("consecutive blockers: no campaign action in the gap",
      any(campaign_actionable(t, ordinary, eligible_at(t, 0, consecutive)) for t in range(980, 1012)), False)
two_blocks = ((980, 985), (988, 995))
check("two interruptions: action resumes between them",
      campaign_actionable(986, ordinary, eligible_at(986, 0, two_blocks)), True)
check("two interruptions: action stops again in the second",
      campaign_actionable(990, ordinary, eligible_at(990, 0, two_blocks)), False)
check("two interruptions: action resumes after the second",
      campaign_actionable(996, ordinary, eligible_at(996, 0, two_blocks)), True)
check("two interruptions: action ends at the deadline",
      campaign_actionable(1000, ordinary, eligible_at(1000, 0, two_blocks)), False)

# ---------------------------------- Correction C: atomic batches (B-04)
# Standard start (B-04 Examples 1-2): maintenance 11, variable 110 when every
# batch runs, 121/turn. A batch is whole and affordable-or-not (ECN-042/048/054),
# so a percentage of a cost is never a batch charge.
BATCH_VAR = {"food": 12, "coal": 10, "oil": 14, "iron": 10, "generator": 10, "refining": 20}
START_MAINT = {"food": 3, "coal": 2, "oil": 1, "iron": 1, "refining": 2, "generator": 2}
START_PLANNED = {"food": 3, "coal": 2, "oil": 1, "iron": 1}
check("atomic: maintenance is 11", sum(START_MAINT.values()), 11)
check("atomic: variable cost is 110",
      sum(n * BATCH_VAR[c] for c, n in START_PLANNED.items())
      + BATCH_VAR["generator"] + BATCH_VAR["refining"], 110)
check("atomic: ordinary turn is 121", sum(START_MAINT.values()) + 110, 121)


def run_batches(crowns, planned):
    """ECN-048/054: whole batches only, in the P3.3 order food -> coal -> oil -> iron."""
    left = crowns
    run = {}
    for chain in ("food", "coal", "oil", "iron"):
        batches = 0
        while batches < planned.get(chain, 0) and left >= BATCH_VAR[chain]:
            left -= BATCH_VAR[chain]
            batches += 1
        run[chain] = batches
    return left, run


left, run = run_batches(37, START_PLANNED)
check("atomic: 37 crowns run all three food batches", run["food"], 3)
check("atomic: 37 crowns run no coal batch", run["coal"], 0)
check("atomic: 37 crowns leave 1", left, 1)
check("atomic: the three food batches cost 36", 3 * BATCH_VAR["food"], 36)
left, run = run_batches(35, START_PLANNED)
check("atomic: 35 crowns run two food batches", run["food"], 2)
check("atomic: 35 crowns then run one coal batch", run["coal"], 1)
check("atomic: 35 crowns leave 1", left, 1)
left, run = run_batches(11, START_PLANNED)
check("atomic: 11 crowns cannot pay a 12-crown food batch", run["food"], 0)
check("atomic: the remainder is paid in ECN-105 order, so coal still runs", run["coal"], 1)
check("atomic: an unpaid batch leaves the remainder untouched", left, 1)
check("atomic: no chain is over-run", all(run[c] <= START_PLANNED[c] for c in run), True)
check("atomic: turn 13 pays maintenance and food", 11 + 3 * 12, 47)
check("atomic: turn 13 leaves 1", 48 - 47, 1)
check("atomic: 36 turns of B-atomic maintenance", 36 * 11, 396)
check("atomic: 36-turn B-atomic balance", 1_500 - 36 * 11, 1_104)
check("atomic: 48-turn B-atomic balance", 1_500 - 48 * 11, 972)
check("atomic: 36-turn A projection", 1_500 - 36 * 121, -2_856)
check("atomic: 48-turn A projection", 1_500 - 48 * 121, -4_308)
check("atomic: 36-turn B-proportional projection", 1_500 - 36 * 38, 132)
check("atomic: 48-turn B-proportional projection", 1_500 - 48 * 38, -324)
check("atomic: the proportional rate is not a batch cost", 38 in BATCH_VAR.values(), False)

# ------------- Correction C (fourth pass): maintenance allocation (ECN-147)
# Maintenance is one whole obligation per chain (`capacity_batches x rate`).
# ECN-147/147a pays it whole, in the settlement order extraction -> generation ->
# processing, and cancels the unpaid remainder; ECN-105 continues past an
# unaffordable obligation (Example 15 does exactly that for a batch), so a
# cheaper later chain can still be paid.
MAINT_ORDER = ("food", "coal", "oil", "iron", "generator", "refining")


def pay_maintenance(crowns, items, order=MAINT_ORDER):
    """ECN-147a as executable code: whole-chain obligations in the published order."""
    left, paid, cancelled, unmaintained = crowns, {}, {}, []
    for chain in order:
        due = items.get(chain, 0)
        if due == 0:
            continue
        if left >= due:
            paid[chain] = due
            left -= due
        else:
            cancelled[chain] = due
            unmaintained.append(chain)
    return left, paid, cancelled, unmaintained


left, paid, cancelled, unmaintained = pay_maintenance(1, START_MAINT)
check("maintenance: 1 crown pays the oil chain", paid, {"oil": 1})
check("maintenance: 1 crown leaves 0, not 1", left, 0)
check("maintenance: the other five chains are unmaintained", unmaintained,
      ["food", "coal", "iron", "generator", "refining"])
check("maintenance: 10 of the 11 crowns are cancelled", sum(cancelled.values()), 10)
check("maintenance: no obligation is paid partially",
      all(v == START_MAINT[k] for k, v in paid.items()), True)
left, paid, cancelled, unmaintained = pay_maintenance(11, START_MAINT)
check("maintenance: 11 crowns pay every chain", sum(paid.values()), 11)
check("maintenance: 11 crowns leave 0", left, 0)
check("maintenance: nothing is unmaintained when it is paid", unmaintained, [])
left, paid, cancelled, unmaintained = pay_maintenance(0, START_MAINT)
check("maintenance: 0 crowns pays nothing", paid, {})
check("maintenance: 0 crowns unmaintains all six chains", len(unmaintained), 6)
left, paid, cancelled, unmaintained = pay_maintenance(3, START_MAINT)
check("maintenance: 3 crowns pay food and nothing else", paid, {"food": 3})
check("maintenance: 3 crowns leave 0", left, 0)
check("maintenance: the published order is extraction, generation, processing",
      MAINT_ORDER, ("food", "coal", "oil", "iron", "generator", "refining"))

# ------------- Correction A (fifth pass): the result decides the state
# DMP-204/DMP-235: a winner returns to `NORMAL` at T+1; a loser enters
# `TRANSITION` at T+1 for 12 turns. A postponed contest applies the same rule:
# postponement moves the date, not the consequence.
def post_election(outcome, resolved_turn):
    """DMP-204/DMP-235: the outcome, never the mere fact of a contest."""
    if outcome == "incumbent_wins":
        return {"state": "NORMAL", "entered": resolved_turn + 1, "until": 0, "restricted": 0}
    return {"state": "TRANSITION", "entered": resolved_turn + 1,
            "until": resolved_turn + 13, "restricted": 12}


won = post_election("incumbent_wins", 1000)
lost = post_election("incumbent_loses", 1000)
check("result: a winner returns to NORMAL", won["state"], "NORMAL")
check("result: a winner has no transition window", won["until"], 0)
check("result: a loser enters TRANSITION", lost["state"], "TRANSITION")
check("result: the transition starts at T+1", lost["entered"], 1001)
check("result: the transition ends at 1013 (12 restricted turns)", lost["until"], 1013)
check("result: it restricts exactly 12 turns", lost["restricted"], 12)
check("result: until = entered + 12", lost["until"] - lost["entered"], 12)
late_loss = post_election("incumbent_loses", 1010)
check("result: a postponed loss enters TRANSITION too", late_loss["state"], "TRANSITION")
check("result: it starts the turn after the late resolution", late_loss["entered"], 1011)
check("result: postponement does not shorten it", late_loss["restricted"], 12)
check("result: a postponed win still returns to NORMAL",
      post_election("incumbent_wins", 1010)["state"], "NORMAL")
check("result: re-evaluation is stable", post_election("incumbent_loses", 1000), lost)
check("result: a win never starts a transition",
      post_election("incumbent_wins", 1000)["state"] == "TRANSITION", False)


# DMP-206/227/229: the outcome must change what the player may do, not only the
# banner. Only TRANSITION and CRISIS suspend new executive orders; RECOVERY
# restores them and SUCCESSION is informational (DMP-224).
def executive_authority(state):
    return "BLOCKED" if state in {"TRANSITION", "CRISIS"} else "AVAILABLE"


check("authority: a returned incumbent keeps full authority",
      executive_authority(won["state"]), "AVAILABLE")
check("authority: a defeated incumbent loses new orders in TRANSITION",
      executive_authority(lost["state"]), "BLOCKED")
check("authority: a postponed loss blocks exactly the same way",
      executive_authority(late_loss["state"]), "BLOCKED")
check("authority: RECOVERY restores full authority (DMP-229)",
      executive_authority("RECOVERY"), "AVAILABLE")
check("authority: SUCCESSION is informational and blocks nothing (DMP-224)",
      executive_authority("SUCCESSION"), "AVAILABLE")
check("authority: CRISIS suspends new orders (DMP-225)",
      executive_authority("CRISIS"), "BLOCKED")

# ------------------- Correction B (fourth pass): the food stock (ECN-081/082)
# Production is added before consumption; the stock is consumed, never negative;
# unmet demand is the remainder and drives the next turn's hunger penalty.
def food_series(stock, produced, demand, turns):
    rows = []
    for turn in range(1, turns + 1):
        available = stock + produced
        consumed = min(available, demand)
        unmet = max(0, demand - available)
        stock = available - consumed
        rows.append((turn, available, consumed, unmet, stock))
    return rows


def first_shortage(rows):
    return next((r[0] for r in rows if r[3] > 0), None)


MODEL_A = food_series(120, 15, 50, 14)
check("food A: turn 1 closes at 85", MODEL_A[0][4], 85)
check("food A: turn 2 closes at 50", MODEL_A[1][4], 50)
check("food A: turn 3 closes at 15", MODEL_A[2][4], 15)
check("food A: turn 4 closes at 0", MODEL_A[3][4], 0)
check("food A: first shortage is turn 4", first_shortage(MODEL_A), 4)
check("food A: turn 4 is short by 20", MODEL_A[3][3], 20)
check("food A: turn 5 is short by 35", MODEL_A[4][3], 35)
check("food A: turn 13 is short by 35", MODEL_A[12][3], 35)
check("food A: no stock is ever negative", min(r[4] for r in MODEL_A), 0)
check("food A: the 1,200 bp penalty is the turn-4 shortfall",
      min(3000, 3000 * MODEL_A[3][3] // 50), 1200)
check("food A: a full shortage caps the penalty at 3,000",
      min(3000, 3000 * 50 // 50), 3000)
MODEL_A14 = food_series(0, 0, 50, 1)
check("food A: an unmaintained food chain leaves 50 unmet", MODEL_A14[0][3], 50)
MODEL_B_ATOMIC = food_series(120, 0, 50, 3)
check("food B-atomic: first shortage is turn 3", first_shortage(MODEL_B_ATOMIC), 3)
check("food B-atomic: turn 3 is short by 30", MODEL_B_ATOMIC[2][3], 30)
MODEL_B_PROP = food_series(120, 15, 50, 4)
check("food B-proportional: first shortage is turn 4", first_shortage(MODEL_B_PROP), 4)
check("food B-proportional: turn 3 closes at 15", MODEL_B_PROP[2][4], 15)
check("the superseded turn-15 shortage is impossible", first_shortage(MODEL_A) != 15, True)

# Case H (the regression the previous suite missed): an already-open campaign is
# not restarted after an interruption. The correct model resolves at 1010; the
# superseded helper resolves at 1034. Both numbers are asserted so a future edit
# that reverts the helper fails here instead of silently agreeing with itself.
check("Case C: interrupted window resolves at the anchor's first eligible turn",
      simulate_contest(1000, 900, ((980, 1010),))[1], 1010)
check("Case C: the superseded helper would have said 1034",
      superseded_resolution(1000, 1010), 1034)
check_true("Case C: the two models disagree",
           simulate_contest(1000, 900, ((980, 1010),))[1] != superseded_resolution(1000, 1010))

# Repeated evaluation of the same closed state must not move the anchor.
check("schedule catch-up is deterministic",
      next_anchor(377, 700), next_anchor(377, 700))
check("schedule repeat evaluation is identical",
      simulate_contest(1000, 900, ((980, 1010),)),
      simulate_contest(1000, 900, ((980, 1010),)))

# DMP-181/236 and DMP-224: `NORMAL`, `ELECTORAL` and `SUCCESSION` resolve a due
# contest; `TRANSITION`, `CRISIS` and `RECOVERY` postpone it. Each row uses the
# same interrupted window (open 976) and the same clearing turn (1010), so the
# state is the only variable. Expected behaviour is read from the state table,
# not assumed: a non-blocking state cannot postpone, a blocking state cannot
# resolve while it is active.
STATE_CASES = (
    ("NORMAL", (), 1000),
    ("ELECTORAL", (), 1000),
    ("SUCCESSION", (), 1000),
    ("TRANSITION", ((980, 1010),), 1010),
    ("CRISIS", ((980, 1010),), 1010),
    ("RECOVERY", ((980, 1010),), 1010),
)
for state, blocked, exp_res in STATE_CASES:
    check("state %s: blocking classification" % state,
          state in BLOCKING_STATES, bool(blocked))
    opening, resolved = simulate_contest(1000, 900, blocked)
    check("state %s: the window opens once at 976" % state, opening, 976)
    check("state %s: resolution" % state, resolved, exp_res)


def election_state_problems(text, reg, req):
    """Correction A: a due contest resolves in NORMAL *or* ELECTORAL; entering
    ELECTORAL is preparation and is never a postponement condition."""
    problems = []
    for stale in ("`leadership_state` is `NORMAL`", "the state is `NORMAL`",
                  "first `NORMAL` turn", "first active `NORMAL` turn",
                  "postponed to the first `NORMAL`"):
        if stale in text or stale in reg or stale in req:
            problems.append("stale NORMAL-only condition %r" % stale)
    for needed in ("resolving states", "DMP-181b", "never a condition the contest must clear"):
        if needed not in text:
            problems.append("missing rule text %r" % needed)
    if "are both resolving states" not in reg and "NORMAL` **or** `ELECTORAL" not in reg:
        problems.append("F-PD-039 does not publish both resolving states")
    return problems


def anchor_problems(text, reg, req):
    """Correction B: the next contest is anchored on the scheduled turn."""
    problems = []
    for stale in ("resolved_contest_turn + 240", "resolved_turn + 240"):
        if stale in text or stale in reg:
            problems.append("resolution-turn anchor %r" % stale)
    for needed in ("scheduled_contest_turn + 240 × k", "DMP-181a"):
        if needed not in text or needed not in reg:
            problems.append("missing anchor rule %r" % needed)
    if "`next_contest_turn` advances by exactly 240" in text:
        problems.append("the superseded +240 invariant is back")
    return problems


def dormancy_problems(text, reg, req):
    """Correction C: one window, opened as early as the rules allow, never in
    the past, and a caught-up anchor that always leaves a full window."""
    problems = []
    for needed in ("DMP-181a", "DMP-181b", "campaign_open_turn", "never in the past"):
        if needed not in text:
            problems.append("missing dormancy rule %r in B-06" % needed)
    if "campaign_open_turn" not in reg:
        problems.append("F-PD-027/028 do not publish the window opening turn")
    if "window_skipped" in text or "window_skipped" in reg:
        problems.append("the superseded no-window model is back")
    return problems


def arithmetic_problems(text, reg, req):
    """Correction D: the rejected batch-cap model uses one floor per division."""
    problems = []
    if "−324" not in text:
        problems.append("the corrected 48-turn treasury −324 is not published")
    if "38/turn" not in text:
        problems.append("the corrected batch-cap cost 38/turn is not published")
    if "11 + 27 = 38" not in text:
        problems.append("the floor derivation `11 + 27 = 38` is not published")
    # Correction C: the batch-cap reading must be expressed in whole batches,
    # and the proportional 38/turn must stay labelled an illustration.
    for needed in ("ECN-054", "B-atomic", "1,104", "972", "3 × 12 = 36",
                   "floor(3 × 25 / 100) = 0"):
        if needed not in text:
            problems.append("atomic-batch account does not publish %r" % needed)
    if "also the **actual** ending balance" in text:
        problems.append("the proportional illustration is still called an actual balance")
    for stale in ("39/turn", "−372", "1,500 − 36×39", "1,500 − 48×39"):
        if stale in text:
            problems.append("superseded arithmetic %r" % stale)
    return problems


def register_status_problems(text, reg, req):
    """Correction E: the register's metadata must match its real coverage."""
    problems = []
    for stale in ("not in this document; Prompt 06B must append them",
                  "Prompt 06B political systems still pending",
                  "Prompt 06B must append"):
        if stale in text or stale in reg:
            problems.append("stale status text %r" % stale)
    if "F-PD-001…F-PD-044" not in reg:
        problems.append("the register does not state its covered range")
    if "not implemented" not in reg and "No formula has been implemented" not in reg:
        problems.append("the register does not distinguish design from implementation")
    return problems


def campaign_lifecycle_problems(text, reg, req):
    """Correction A: the window opens once; only a delayed opening starts it.

    The superseded helper treated every delay as a new 24-turn window, so an
    interruption at turn 1000 that cleared at 1010 resolved at 1034. Agreement
    between a wrong test and a wrong helper is the defect: the document now has
    to publish the once-only rule *and* name 1034 as the wrong answer.
    """
    problems = []
    for needed in ("(computed once)", "window_deadline",
                   "max(scheduled_contest_turn, window_deadline)"):
        if needed not in text:
            problems.append("B-06 does not publish %r" % needed)
    for needed in ("window_deadline", "max(scheduled_contest_turn, window_deadline)"):
        if needed not in reg:
            problems.append("F-PD-028 does not publish %r" % needed)
    if "not 1034" not in text:
        problems.append("B-06 does not name the superseded 1034 result")
    for stale in ("resolution_turn    = campaign_open_turn + 24, or the first eligible turn after it",
                  "campaign_open(scheduled, eligible_from) + 24"):
        if stale in text:
            problems.append("restarted-window form %r" % stale)
    return problems


def accounting_semantics_problems(text, reg, req):
    """Correction B: a negative projection is never called a treasury.

    B-04 forbids a negative balance (ECN-102) and cancels an unaffordable
    obligation instead of deferring it (ECN-105/106). A multi-turn subtraction
    that ignores those rules is a cash-flow projection, and the document must
    say so where it prints the number.
    """
    problems = []
    if "unconstrained cumulative cash-flow result" not in text:
        problems.append("B-06 does not define the unconstrained cash-flow term")
    for needed in ("ECN-102", "ECN-105"):
        if needed not in text:
            problems.append("B-06 does not cite %s" % needed)
    for stale in ("treasury `1,500 − 48×38 = −324`",
                  "treasury `1,500 − 36×121 = 1,500 − 4,356 = −2,856`",
                  "treasury `1,500 − 36×121 = −2,856`",
                  "treasury `1,500 − 48×121 = −4,308`",
                  "`1,500 − 48×121 = −4,308`, insolvent"):
        if stale in text:
            problems.append("negative projection labelled a treasury: %r" % stale)
    return problems


def succession_problems(text, reg, req):
    """Correction D: `SUCCESSION` resolves a scheduled contest and blocks none.

    The state is a warning, not a postponement (DMP-224); the exceptional
    challenge keeps its own separate 12-turn counter (DMP-218), so allowing the
    ballot during a warning must not make an early motion easier.
    """
    problems = []
    if "`NORMAL`, `ELECTORAL` and `SUCCESSION`" not in text:
        problems.append("DMP-236 does not list SUCCESSION as a resolving state")
    if "does not block a scheduled contest" not in text:
        problems.append("the state table does not say SUCCESSION blocks no contest")
    if "`SUCCESSION` is not a blocking state" not in text:
        problems.append("DMP-181 no longer says SUCCESSION is not blocking")
    if "`SUCCESSION` does not block a contest" not in reg:
        problems.append("F-PD-039 does not keep SUCCESSION non-blocking")
    if "12 pressure turns" not in text:
        problems.append("the exceptional challenge lost its own precondition")
    return problems


def campaign_state_problems(text, reg, req):
    """Corrections A/B: state restoration and the campaign's own deadline anchor.

    A campaign that still has time left when a blocker clears must return to
    `ELECTORAL`, not `NORMAL`; and every deadline offset belongs to
    `campaign_open_turn`, never unconditionally to `T`.
    """
    problems = []
    if "returns to **`ELECTORAL`**" not in text:
        problems.append("B-06 does not define the restoration to ELECTORAL")
    if "Consecutive blockers leave no gap" not in text:
        problems.append("B-06 does not define the no-gap blocker case")
    if "`campaign_open_turn + 12`" not in text:
        problems.append("B-06 does not anchor registration on the opening")
    if "| Registration closes | `T − 12`" in text:
        problems.append("the stale T-12 registration row is back")
    for needed in ("992", "1004"):
        if needed not in text:
            problems.append("the delayed-opening example lacks %r" % needed)
    if "restores to `ELECTORAL`" not in reg:
        problems.append("F-PD-039 does not publish the restoration")
    if "campaign_open_turn + 12" not in reg:
        problems.append("F-PD-028 does not anchor registration on the opening")
    return problems


def progress_status_problems(log_text, progress_text):
    """Correction C: the summary and the 06A/06B/07 rows must agree.

    The defect was a header saying 06B was complete while the table still said
    "next — not started", and a validator that accepted both. The check reads
    the structured status cell, not one exact sentence.
    """
    problems = []
    rows = {}
    for line in log_text.splitlines():
        if not (line.startswith("| 06A |") or line.startswith("| 06B |")
                or line.startswith("| 07 |") or line.startswith("| 08 |")
                or line.startswith("| 09 |") or line.startswith("| 10 |")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4:
            rows[cells[0]] = cells[3]
    if "**Complete**" not in rows.get("06A", ""):
        problems.append("progress-log row 06A is not Complete: %r" % rows.get("06A"))
    if "**Complete**" not in rows.get("06B", ""):
        problems.append("progress-log row 06B is not Complete: %r" % rows.get("06B"))
    if "**Complete**" not in rows.get("07", ""):
        problems.append("progress-log row 07 is not Complete: %r" % rows.get("07"))
    if ("**08A complete**" not in rows.get("08", "")
            or "**08B complete**" not in rows.get("08", "")
            or "**08C complete**" not in rows.get("08", "")):
        problems.append("progress-log row 08 does not record 08A, 08B and 08C complete: %r" % rows.get("08"))
    # 2026-11-03: Phase 09B is accepted at the specification/documentation level;
    # 09C is complete at the same level, 10A research and the 10B specification
    # are complete and Prompt 10C is next.
    if ("**ACCEPTED" not in rows.get("09", "")
            or "Prompt 09C: complete at the specification/documentation level" not in rows.get("09", "")
            or "Prompt 10A: complete" not in rows.get("09", "")
            or "Prompt 10B: complete at the specification/documentation level" not in rows.get("09", "")):
        problems.append("progress-log row 09 does not record Phase 09B accepted, 09C complete, 10A complete and 10B complete: %r" % rows.get("09"))
    # 2026-11-04 (Prompt 10C): 10C closed, so row 10 must also record it.
    # 2026-11-07 (Prompt 12B): 12B closed, so the live sub-prompt named by row 10 is 12C.
    if ("10B specification complete" not in rows.get("10", "")
            or "Prompt 10C complete" not in rows.get("10", "")
            or "Prompt 12C next" not in rows.get("10", "")):
        problems.append("progress-log row 10 does not record 10B complete, 10C complete and Prompt 12C next: %r" % rows.get("10"))
    header = log_text[:log_text.index("## 1.")] if "## 1." in log_text else log_text[:1500]
    if "**Prompt 06B complete**" not in header:
        problems.append("the progress-log header does not record 06B as complete")
    if "**Phase 09B Alliance specification and documentation: ACCEPTED.**" not in header:
        problems.append("the progress-log header does not carry the current Phase 09B acceptance status")
    for pattern, label in ((r"\| 06 \|[^\n]*\| \*\*Complete\*\*", "06 Complete"),
                           (r"\| 07 \|[^\n]*\| \*\*Complete\*\*", "07 Complete"),
                           (r"\| 08 \|[^\n]*\| \*\*08A complete\*\*", "08A complete"),
                           (r"\*\*08B complete\*\*", "08B complete"),
                           (r"\*\*08C complete\*\*", "08C complete"),
                           (r"\| 09 \|[^\n]*\*\*ACCEPTED[^\n]*\*\*", "Phase 09B accepted")):
        if not re.search(pattern, progress_text):
            problems.append("PROJECT_PROGRESS does not record %s" % label)
    return problems


def exceptional_challenge_problems(text, reg, req):
    """Correction A, case E: the early motion keeps its own precondition — a
    constitutional monarchy only — and never borrows the scheduled window."""
    problems = []
    if "no campaign window" not in text:
        problems.append("the early motion no longer states that it has no campaign window")
    if "12 consecutive turns" not in text:
        problems.append("the early motion's 12-turn precondition is missing")
    if "never open a campaign window and never enter `ELECTORAL`" not in text:
        problems.append("exceptional challenges are not separated from scheduled contests")
    if "early motion" in text and "a constitutional monarchy" not in text.lower():
        problems.append("the early motion lost its government restriction")
    return problems


def id_problems(text, reg, req):
    """Rule identifiers are unique and every reference resolves."""
    problems = []
    # A definition is "**DMP-181 —", "**DMP-181a —" or "**F-PD-000a —": the
    # suffix is part of the identifier, so `DMP-030` and `DMP-030a` are two
    # different rules and neither is a duplicate of the other.
    defs = re.findall(r"\*\*(DMP-\d{3}[a-z]?) —", text)
    dupes = sorted({i for i in defs if defs.count(i) > 1})
    if dupes:
        problems.append("duplicate DMP ids %s" % dupes)
    refs = set(re.findall(r"\bDMP-\d{3}\b", text))
    unresolved = sorted(refs - {d[:7] for d in defs})
    if unresolved:
        problems.append("unresolved DMP references %s" % unresolved)
    fpd = re.findall(r"\*\*(F-PD-\d{3}[a-z]?) —", reg)
    fdupes = sorted({i for i in fpd if fpd.count(i) > 1})
    if fdupes:
        problems.append("duplicate F-PD ids %s" % fdupes)
    absent = [i for i in range(1, 45) if "**F-PD-%03d" % i not in reg]
    if absent:
        problems.append("missing F-PD ids %s" % absent)
    return problems


def correction4_problems(text, reg, req):
    """Fourth pass: delayed ballots, the food stock and the maintenance allocation.

    A delayed campaign fixes its ballot at its own `registration_close_turn`; the
    food stock is computed from turn 1 (first shortage turn 4, not 15); and the
    last crown is allocated by maintenance obligation (ECN-105/147), which pays
    the oil chain and leaves the other five `UNMAINTAINED`.
    """
    problems = []
    for stale in ("the ballot is fixed at `T − 12`",
                  "cannot be revised after `T − 12`",
                  "every facility idles as `UNMAINTAINED`",
                  "Food falls to 85 after turn 13 and 35 after turn 14"):
        if stale in text:
            problems.append("superseded text %r" % stale)
    # "not turn 15" is the correction's own wording; only an assertion counts.
    if re.search(r"(?<!not )\bturn 15\b", text):
        problems.append("the superseded turn-15 shortage is back")
    if "first shortage is" not in text:
        problems.append("the corrected first-shortage turn is not stated")
    for needed in ("registration_close_turn", "oil (1) is paid",
                   "every other chain is `UNMAINTAINED`", "ECN-147a"):
        if needed not in text:
            problems.append("missing corrected text %r" % needed)
    if "the banner shows the state **the result produced**" not in text:
        problems.append("DMP-184 does not make the post-election state depend on the result")
    if "the state banner returns to `NORMAL`" in text:
        problems.append("DMP-184 still returns winner and loser alike to NORMAL")
    if "extraction \u2192 generation \u2192 processing" not in text:
        problems.append("B-06 does not publish the maintenance allocation order")
    if "`turn_id < T`" in reg:
        problems.append("the register still closes every campaign at T")
    if "`turn_id < resolution_turn`" not in reg:
        problems.append("F-PD-028/F-PD-029 do not publish the resolution-turn limit")
    return problems


def _row(text, ident):
    """The one markdown row for an ID, or None.

    A guard that scans the whole file can pass on a summary mention while the
    operative entry is wrong, so the decision-log guards read the single row.
    """
    rows = [ln for ln in text.splitlines() if ln.startswith("| %s |" % ident)]
    return rows[0] if len(rows) == 1 else None


def publication_timing_problems(text, dectext, sumtext):
    """D-093 publishes the challengers at the campaign's own opening.

    The defect was a universal `T-24` publication. A campaign opened at 980 for
    a contest due at 1000 would then publish at a turn already in the past, and
    DMP-186 says "at campaign open". The on-time case stays legal only when it
    is explicitly conditional.
    """
    problems = []
    row = _row(dectext, "D-093")
    if row is None:
        return ["D-093 is not a single decision-log row"]
    for stale in ("published at `T-24`", "published at `T − 24`"):
        if stale in row:
            problems.append("D-093 still publishes the challengers at %r" % stale)
    if "published at `campaign_open_turn`" not in row:
        problems.append("D-093 does not anchor publication on campaign_open_turn")
    if "`T-24` only when" not in row:
        problems.append("D-093 does not limit T-24 to the on-time campaign")
    d093 = _row(sumtext, "D-093")
    if d093 is None or "campaign_open_turn" not in d093:
        problems.append("the decision summary does not publish D-093 at campaign open")
    dmp186 = dmp_section("**DMP-186 —")
    if "At campaign open" not in dmp186:
        problems.append("DMP-186 no longer publishes the challengers at campaign open")
    return problems


def catch_up_crossref_problems(text, reg, dectext, sumtext):
    """D-092 must defer the catch-up to D-107, not imply one `+240` step.

    The defect read `scheduled_contest_turn + 240` afterwards, which is silent
    about the `k > 1` skip D-107 requires after long dormancy. The formula
    itself must stay in D-107; D-092 and its summaries may only point at it.
    """
    problems = []
    row = _row(dectext, "D-092")
    if row is None:
        return ["D-092 is not a single decision-log row"]
    for stale in ("`scheduled_contest_turn + 240` afterwards",
                  "`next_contest_turn` advances by exactly 240"):
        if stale in row:
            problems.append("D-092 states a single-step advance as the rule: %r" % stale)
    if "D-107" not in row:
        problems.append("D-092 does not cross-reference D-107")
    if "240 × k" not in row:
        problems.append("D-092 does not publish the catch-up multiplier")
    d092 = _row(sumtext, "D-092")
    if d092 is None or "D-107" not in d092:
        problems.append("the decision summary does not connect D-092 to D-107")
    for ident in ("DD-112", "DD-120"):
        entry = _row(sumtext, ident)
        if entry is None or "D-107" not in entry:
            problems.append("%s does not record the catch-up qualification" % ident)
    d107 = _row(dectext, "D-107")
    if d107 is None or "`scheduled_contest_turn + 240 × k`" not in d107:
        problems.append("D-107 no longer publishes its own catch-up formula")
    elif "next ≥ resolved_turn + 25" not in d107:
        problems.append("D-107's 25-turn guarantee is missing")
    for label, doc in (("B-06", text), ("register", reg)):
        if "scheduled_contest_turn + 240 × k" not in doc:
            problems.append("%s lost the catch-up formula" % label)
    return problems


def handoff_timing_problems(handoff_text, context_text):
    """The handoff must not equate the actual opening with the on-time milestone.

    The defect was `campaign_open_turn` = `T-24` as a flat identity. That is
    false whenever a blocking state delays the opening: DMP-181 defines the
    opening as the first eligible turn >= `scheduled_contest_turn - 24`,
    computed once, so `T-24` is only the on-time coincidence. `T-24` stays legal
    as the ordinary case, so the guard requires that qualification instead of
    banning the token.
    """
    problems = []
    para = next((ln for ln in handoff_text.splitlines()
                 if "campaign_open_turn" in ln and "Part II" in ln), "")
    if not para:
        return ["the handoff has no opening summary that names campaign_open_turn"]
    for stale in ("`campaign_open_turn` = `T-24`",
                  "`campaign_open_turn` is `T-24`",
                  "campaign_open_turn = T-24"):
        if stale in para:
            problems.append("the handoff equates the actual opening with %r" % stale)
    for needed in ("first eligible turn",
                   "computed once",
                   "`T-24` only when the contest opens on time",
                   "campaign_open_turn + 12",
                   "max(scheduled_contest_turn, window_deadline)",
                   "never receives a second window"):
        if needed not in para:
            problems.append("the handoff does not state %r" % needed)
    ctx = next((ln for ln in context_text.splitlines()
                if "240-turn per-nation election cycle" in ln), "")
    if not ctx:
        problems.append("AI_CONTEXT no longer describes the election cycle")
    else:
        if "phases at `T-24`" in ctx:
            problems.append("AI_CONTEXT publishes fixed T-24/T-12/T-2 phases")
        if "campaign_open_turn" not in ctx:
            problems.append("AI_CONTEXT does not anchor the phases on campaign_open_turn")
        if "on-time" not in ctx:
            problems.append("AI_CONTEXT does not qualify the ordinary dates")
    return problems


def truncation_problems(text, reg, req):
    """Integrity: a normative paragraph must not end mid-word.

    The defect was DMP-184 ending in "the sta" and running straight into the next
    section. The check is narrow on purpose: a definition line whose last
    character is a letter or digit is truncated unless the next non-empty line
    opens a display block, where a sentence legitimately continues afterwards
    (DMP-038 and DMP-055 do exactly that).
    """
    problems = []
    docs = [("B-06", text), ("register", reg)]
    for label, name in (("B-04", "10_economy_resources_treasury_and_finances.md"),
                        ("B-04 register", "10_economic_formula_and_balance_register.md")):
        path = os.path.join(here, "..", "stage-2", name)
        if os.path.exists(path):
            docs.append((label, open(path, encoding="utf-8").read()))
    for label, doc in docs:
        lines = doc.splitlines()
        for i, line in enumerate(lines):
            m = re.match(r"^\*\*((?:DMP|F-PD)-\d{3}[a-z]?) — ", line)
            if not m:
                continue
            para = line.rstrip()
            if not para or not para[-1].isalnum():
                continue
            nxt = next((l.strip() for l in lines[i + 1:] if l.strip()), "")
            if nxt.startswith("```"):
                continue
            problems.append("%s %s ends mid-sentence: %r" % (label, m.group(1), para[-50:]))
    return problems


GUARDS = (
    ("election-state rule", election_state_problems),
    ("schedule anchor", anchor_problems),
    ("dormancy catch-up", dormancy_problems),
    ("rejected-crisis arithmetic", arithmetic_problems),
    ("register status", register_status_problems),
    ("rule identifiers", id_problems),
    ("exceptional challenges", exceptional_challenge_problems),
    ("campaign lifecycle", campaign_lifecycle_problems),
    ("accounting terminology", accounting_semantics_problems),
    ("succession elections", succession_problems),
    ("campaign state and deadlines", campaign_state_problems),
    ("delayed ballots and accounting", correction4_problems),
    ("truncated rules", truncation_problems),
)
for guard_label, guard in GUARDS:
    guard_problems = guard(body, regtext, reqtext)
    check_true("guard: %s" % guard_label, not guard_problems, "; ".join(guard_problems))

# The progress records are a fourth and fifth source, so their guard and its
# self-test run outside the (text, register, requirements) tuple.
progress_problems = progress_status_problems(logtext, progtext)
check_true("guard: progress status", not progress_problems, "; ".join(progress_problems))

# The decision log is the fifth source: two corrections lived there while the
# rulebook already agreed, so the guards read the operative row, not a summary.
publication_problems = publication_timing_problems(body, dectext, sumtext)
check_true("guard: challenger publication timing", not publication_problems,
           "; ".join(publication_problems))
crossref_problems = catch_up_crossref_problems(body, regtext, dectext, sumtext)
check_true("guard: D-092/D-107 catch-up cross-reference", not crossref_problems,
           "; ".join(crossref_problems))
# The handoff is the sixth source: a summary can contradict the rulebook even
# when every register row is correct, and a future model reads it first.
handoff_problems = handoff_timing_problems(handofftext, contexttext)
check_true("guard: handoff election timing", not handoff_problems,
           "; ".join(handoff_problems))

# Each guard must fail when its defect is reintroduced. Mutations are applied to
# in-memory copies only, so running the self-test never modifies a project file.
SELF_TESTS = (
    ("election-state rule", election_state_problems,
     lambda b, r, q: (b + "\nA postponed contest waits until `leadership_state` is `NORMAL`.\n", r, q)),
    ("schedule anchor", anchor_problems,
     lambda b, r, q: (b + "\nnext_contest_turn = resolved_contest_turn + 240\n", r, q)),
    ("dormancy catch-up", dormancy_problems,
     lambda b, r, q: (b.replace("DMP-181a", "DMP-XXX"), r, q)),
    ("rejected-crisis arithmetic", arithmetic_problems,
     lambda b, r, q: (b + "\nThe batch-cap reading rounds 27.5 up, so the cost is 39/turn.\n", r, q)),
    ("register status", register_status_problems,
     lambda b, r, q: (b, r + "\nElection formulas are not in this document; Prompt 06B must append them.\n", q)),
    ("rule identifiers", id_problems,
     lambda b, r, q: (b + "\n**DMP-181 — A second rule with the same ID.**\n", r, q)),
    ("exceptional challenges", exceptional_challenge_problems,
     lambda b, r, q: (b.replace("no campaign window", "a 24-turn campaign window"), r, q)),
    ("campaign lifecycle", campaign_lifecycle_problems,
     lambda b, r, q: (b.replace("(computed once)", "(recomputed on every change)"), r, q)),
    ("accounting terminology", accounting_semantics_problems,
     lambda b, r, q: (b + "\nThe treasury `1,500 − 48×38 = −324` after 48 turns.\n", r, q)),
    ("succession elections", succession_problems,
     lambda b, r, q: (b.replace("`NORMAL`, `ELECTORAL` and `SUCCESSION`",
                                "`NORMAL` and `ELECTORAL`"), r, q)),
    ("campaign state and deadlines", campaign_state_problems,
     lambda b, r, q: (b.replace("`campaign_open_turn + 12`", "`T − 12`"), r, q)),
    ("delayed ballots and accounting", correction4_problems,
     lambda b, r, q: (b + "\nFood falls to 85 after turn 13 and 35 after turn 14, so the first shortage is turn 15.\n",
                      r.replace("`turn_id < resolution_turn`", "`turn_id < T`"), q)),
    ("truncated rules", truncation_problems,
     lambda b, r, q: (b + "\n**DMP-998 — Truncated law.** *Provisional.* At the next turn: the sta\n\n## 99. Next\n", r, q)),
)


def stale_d093(text):
    """Reintroduces the original D-093 defect: a universal T-24 publication."""
    mutated = text.replace(
        "Both are **published at `campaign_open_turn`**",
        "Both are **published at `T-24`**", 1)
    return mutated, mutated != text


def missing_catchup(text):
    """Reintroduces the original D-092 defect: one `+240` step, no D-107."""
    row = _row(text, "D-092")
    if row is None:
        return text, False
    stale = row.replace(
        "every later contest advances from the **scheduled** contest turn, never from the resolution turn, and the complete catch-up calculation — the ordinary one-interval step and the `scheduled_contest_turn + 240 × k` skip after long dormancy — is **D-107**.",
        "`scheduled_contest_turn + 240` afterwards.", 1)
    stale = stale.replace(
        " **Revised 2026-10-28 (seventh pass):** the original `scheduled_contest_turn + 240` progression is the ordinary `k = 1` step only; the catch-up rule, its `k > 1` skip and the 25-turn guarantee live in **D-107**, so an overdue contest never advances the anchor by a single interval.",
        "", 1)
    mutated = text.replace(row, stale, 1)
    return mutated, mutated != text


def stale_handoff(text):
    """Reintroduces the original handoff defect: opening equated with `T-24`."""
    stale = text.replace(
        "computes the opening as the **first eligible turn** at or after `scheduled_contest_turn − 24`, **computed once**; it is `T-24` only when the contest opens on time",
        "opens at `campaign_open_turn` = `T-24`", 1)
    return stale, stale != text


def stale_context(text):
    """Reintroduces the same ambiguity in the master context summary."""
    stale = text.replace(
        "the 240-turn per-nation election cycle opens on `campaign_open_turn` (D-107), so the `T-24`/`T-12`/`T-2` phases are quoted as on-time values only",
        "the 240-turn per-nation election cycle runs with phases at `T-24`/`T-12`/`T-2`", 1)
    return stale, stale != text


def stale_progress(log_text):
    """Reintroduces the exact defect Correction C removed: a table row that
    still says 06B is not started while the header says it is complete."""
    stale = log_text.replace(
        "| 06B | Elections, campaigns, retention, crises and unrest | extends B-06 and its register |",
        "| 06B | Elections, campaigns, retention, crises and unrest | extends B-06 and its register | **Next — not started** |",
        1)
    return stale, stale != log_text


# ---------------------------------------------------------------- report
if "--self-test" in sys.argv:
    undetected = []
    for label, guard, mutate in SELF_TESTS:
        found = guard(*mutate(body, regtext, reqtext))
        if found:
            print("SELF-TEST PASS  %s -> %s" % (label, found[0][:90]))
        else:
            undetected.append(label)
            print("SELF-TEST FAIL  %s did not detect its defect" % label)
    total = len(SELF_TESTS) + 1
    mutated_log, changed = stale_progress(logtext)
    found = progress_status_problems(mutated_log, progtext)
    if changed and found:
        print("SELF-TEST PASS  progress status -> %s" % found[0][:90])
    else:
        undetected.append("progress status")
        print("SELF-TEST FAIL  progress status did not detect its defect"
              if changed else "SELF-TEST FAIL  progress mutation did not apply")
    for label, mutate, guard in (
            ("challenger publication timing", stale_d093,
             lambda d: publication_timing_problems(body, d, sumtext)),
            ("D-092/D-107 catch-up cross-reference", missing_catchup,
             lambda d: catch_up_crossref_problems(body, regtext, d, sumtext))):
        mutated, changed = mutate(dectext)
        found = guard(mutated)
        if changed and found:
            print("SELF-TEST PASS  %s -> %s" % (label, found[0][:90]))
        else:
            undetected.append(label)
            print("SELF-TEST FAIL  %s did not detect its defect" % label
                  if changed else "SELF-TEST FAIL  %s mutation did not apply" % label)
    for label, mutate, guard in (
            ("handoff election timing", stale_handoff,
             lambda h: handoff_timing_problems(h, contexttext)),
            ("context election phases", stale_context,
             lambda c: handoff_timing_problems(handofftext, c))):
        mutated, changed = mutate(handofftext if label == "handoff election timing" else contexttext)
        found = guard(mutated)
        if changed and found:
            print("SELF-TEST PASS  %s -> %s" % (label, found[0][:90]))
        else:
            undetected.append(label)
            print("SELF-TEST FAIL  %s did not detect its defect" % label
                  if changed else "SELF-TEST FAIL  %s mutation did not apply" % label)
    total += 4  # challenger publication, catch-up, handoff timing, context phases
    if undetected or FAILS:
        print("SELF-TEST: %d of %d guards failed to detect their defect"
              % (len(undetected), total))
        raise SystemExit(2)
    print("SELF-TEST: %d/%d guards detect their defect; %d/%d document checks passed"
          % (total, total, CHECKS, CHECKS))
    raise SystemExit(0)

if FAILS:
    print("POLITICS NUMBERS: %d FAILED of %d checks" % (len(FAILS), CHECKS))
    for f in FAILS:
        print("  FAIL " + f)
    raise SystemExit(1)
print("POLITICS NUMBERS: %d/%d checks passed" % (CHECKS, CHECKS))
