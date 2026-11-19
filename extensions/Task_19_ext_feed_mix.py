"""Task 19 extension - least-cost poultry feed mix.

C. Parameter change: cost of Type A server 12 -> 8 (and 12 -> 20).
E. New case: blend maize and soybean meal to meet protein and energy needs.
"""
import numpy as np
from scipy.optimize import linprog, minimize

# ---- C. Parameter change: unit cost --------------------------------------------------------------------------
print("C. Cheapest server mix when the cost of Type A changes (B costs 18, capacities 100/170, need >= 1000)")
for ca in (12, 8, 20):
    res = linprog([ca, 18], A_ub=[[-100, -170]], b_ub=[-1000], bounds=[(0, None)] * 2)
    best = min(((ca * a + 18 * b, a, b) for a in range(20) for b in range(20) if 100 * a + 170 * b >= 1000))
    print(f"  cost A = {ca:>2}: continuous A={res.x[0]:.2f}, B={res.x[1]:.2f}, cost {res.fun:.2f}; best whole servers (cost, A, B) = {best}")
print("  Cost per capacity unit decides: A = 12/100 = 0.12, B = 18/170 = 0.106 -> B wins until A gets cheaper.")

# ---- E. New case: feed mix -------------------------------------------------------------------------------------
# Make 100 kg of feed from maize (x) and soybean meal (y).
#   maize:   30 KES/kg, 9% protein, 3.4 Mcal/kg
#   soybean: 60 KES/kg, 44% protein, 2.5 Mcal/kg
# Need: x + y = 100, protein >= 18 kg, energy >= 300 Mcal.
cost = lambda z: 30 * z[0] + 60 * z[1]
cons = [
    {"type": "eq",   "fun": lambda z: z[0] + z[1] - 100},
    {"type": "ineq", "fun": lambda z: 0.09 * z[0] + 0.44 * z[1] - 18},
    {"type": "ineq", "fun": lambda z: 3.4 * z[0] + 2.5 * z[1] - 300},
]
res = minimize(cost, x0=[50, 50], method="SLSQP", bounds=[(0, None)] * 2, constraints=cons)
x, y = res.x
lp = linprog([30, 60], A_eq=[[1, 1]], b_eq=[100],
             A_ub=[[-0.09, -0.44], [-3.4, -2.5]], b_ub=[-18, -300], bounds=[(0, None)] * 2)
print("\nE. New case: 100 kg poultry feed")
print(f"  SLSQP : maize {x:.2f} kg, soybean {y:.2f} kg, cost {res.fun:,.2f} KES")
print(f"  linprog check: maize {lp.x[0]:.2f} kg, soybean {lp.x[1]:.2f} kg, cost {lp.fun:,.2f} KES")
print(f"  protein supplied {0.09 * x + 0.44 * y:.2f} kg (need 18, binding), energy {3.4 * x + 2.5 * y:.1f} Mcal (need 300, slack)")
print("  Active constraint = protein: the optimum uses exactly the minimum protein allowed.")
