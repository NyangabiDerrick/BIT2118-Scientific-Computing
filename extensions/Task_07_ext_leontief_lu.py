"""Task 7 extension - Leontief input-output economic model with LU reuse.

C. Parameter change: 3x3 -> 400x400 system with 2,000 right-hand sides (timing).
E. New case: 3-sector economy; production needed for several demand scenarios.
"""
import timeit

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# ---- C. Parameter change: problem size -------------------------------------------
rng = np.random.default_rng(0)
n, k = 300, 500
A = rng.random((n, n)) + n * np.eye(n)
B = rng.random((n, k))
t_repeat = timeit.timeit(lambda: [np.linalg.solve(A, B[:, j]) for j in range(k)], number=1)


def reuse():
    lu, piv = lu_factor(A)
    return [lu_solve((lu, piv), B[:, j]) for j in range(k)]


t_lu = timeit.timeit(reuse, number=1)
print(f"C. n={n}, {k} right-hand sides: solve each time {t_repeat:.3f}s, LU once {t_lu:.3f}s "
      f"-> {t_repeat/t_lu:.1f}x faster")

# ---- E. New case: Leontief model ----------------------------------------------------
# Sectors: Agriculture, Manufacturing, Services. a_ij = input from sector i
# needed to make 1 unit of sector j output. Production x solves (I - a) x = d.
a = np.array([[0.20, 0.15, 0.05],
              [0.25, 0.30, 0.20],
              [0.10, 0.20, 0.15]])
M = np.eye(3) - a
lu, piv = lu_factor(M)
scenarios = {
    "baseline demand":      [100.0, 150.0, 200.0],
    "export boom (mfg)":    [100.0, 250.0, 200.0],
    "services recession":   [100.0, 150.0, 120.0],
}
print("\nE. New case: 3-sector Leontief economy (million KES)")
for name, d in scenarios.items():
    x = lu_solve((lu, piv), np.array(d))
    print(f"  {name:<20} demand {d} -> total output {np.round(x, 2)}  (sum {x.sum():.1f})")
print("  Same LU factors reused for every scenario; no new elimination needed.")
