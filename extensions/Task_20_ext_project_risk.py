"""Task 20 extension - project completion risk by Monte Carlo.

C. Parameter change: number of simulations N and server capacity / spread.
E. New case: probability a three-stage software project finishes within 30 days.
"""
from math import erf, sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"

# ---- C. Parameter change -------------------------------------------------------------------------------------------
exact = 0.5 * (1 - erf((1000 - 850) / (120 * sqrt(2))))   # exact tail of the normal distribution
print(f"C. Overload probability P(demand > 1000), exact normal tail = {exact:.4%}")
for N in (100, 1_000, 100_000, 1_000_000):
    est = (np.random.default_rng(42).normal(850, 120, N) > 1000).mean()
    se = sqrt(max(est * (1 - est), 1e-12) / N)
    print(f"  N = {N:>9,}: estimate {est:7.3%} (std. error ~ {se:.3%}), error {abs(est - exact):.3%}")
for cap, sd in ((1000, 120), (1100, 120), (1000, 80)):
    p = (np.random.default_rng(42).normal(850, sd, 200_000) > cap).mean()
    print(f"  capacity {cap}, std {sd}: overload probability {p:.3%}")

# ---- E. New case: project schedule ----------------------------------------------------------------------------------
# Durations in days (min, most likely, max) - triangular distributions, stages in sequence.
stages = {"Design": (6, 8, 14), "Development": (12, 15, 25), "Testing": (4, 6, 12)}
rng = np.random.default_rng(2024)
N = 200_000
total = sum(rng.triangular(lo, mode, hi, N) for lo, mode, hi in stages.values())
deadline = 30
p_on_time = (total <= deadline).mean()
print("\nE. New case: three-stage software project (days)")
print(f"  expected total {total.mean():.1f} d (sum of most likely = {sum(m for _, m, _ in stages.values())} d), std {total.std():.1f} d")
print(f"  P(finish within {deadline} days) = {p_on_time:.1%}")
print(f"  80th percentile = {np.percentile(total, 80):.1f} d; 95th = {np.percentile(total, 95):.1f} d")
print(f"  a deadline of {np.percentile(total, 90):.0f} days gives ~90% confidence")

plt.hist(total, bins=80, density=True)
plt.axvline(deadline, color="red", linestyle="--", label=f"Deadline {deadline} d")
plt.xlabel("Total project duration (days)")
plt.ylabel("Probability density")
plt.title("Monte Carlo project-duration distribution")
plt.legend()
plt.grid(True)
plt.savefig(FIG / "ext_task_20_project.png", dpi=150, bbox_inches="tight")
