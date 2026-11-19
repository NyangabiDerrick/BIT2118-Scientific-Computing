"""Task 10 extension - business break-even points by bisection.

C. Parameter change: heat-balance bracket and ambient constant changed.
E. New case: where revenue equals cost for a small manufacturer.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar

FIG = Path(__file__).resolve().parent.parent / "figures"


def bisect(f, a, b, tol=1e-6):
    """Own bisection implementation; returns root and number of halvings."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    n = 0
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        fm = f(m)
        n += 1
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2, n


# ---- C. Parameter change on the heat-balance model --------------------------------------
for amb in (25.0, 30.0):
    f = lambda T, amb=amb: T - amb - 10 * np.exp(-T / 20)
    r, n = bisect(f, 20, 45, 1e-8)
    print(f"C. ambient {amb:.0f} C -> equilibrium {r:.6f} C after {n} halvings")
for tol in (1e-2, 1e-6, 1e-10):
    r, n = bisect(lambda T: T - 25 - 10 * np.exp(-T / 20), 20, 40, tol)
    print(f"   tolerance {tol:.0e} -> {n} halvings, root {r:.8f}")

# ---- E. New case: break-even ---------------------------------------------------------------
# Price falls with volume: p = 100 - 0.02 q.  Cost = 2000 + 20 q + 0.005 q^2.
def profit(q):
    return q * (100 - 0.02 * q) - (2000 + 20 * q + 0.005 * q ** 2)


low, n1 = bisect(profit, 1, 200)
high, n2 = bisect(profit, 2000, 5000)
check = root_scalar(profit, bracket=[1, 200], method="bisect").root
print("\nE. New case: break-even quantities")
print(f"  lower break-even q = {low:.2f} units ({n1} halvings; SciPy {check:.2f})")
print(f"  upper break-even q = {high:.2f} units ({n2} halvings)")
q_best = 80 / (2 * 0.025)
print(f"  profit is positive between them; maximum at q = {q_best:.0f}, profit = {profit(q_best):,.0f} KES")

q = np.linspace(0, 3500, 400)
plt.plot(q, profit(q))
plt.axhline(0, linewidth=0.8)
for r in (low, high):
    plt.axvline(r, linestyle="--")
plt.xlabel("Units produced and sold (q)")
plt.ylabel("Profit (KES)")
plt.title("Break-even points")
plt.grid(True)
plt.savefig(FIG / "ext_task_10_break_even.png", dpi=150, bbox_inches="tight")
