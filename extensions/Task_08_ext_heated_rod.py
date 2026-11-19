"""Task 8 extension - steady heat conduction in a metal rod.

C. Parameter change: tolerance 1e-8 -> 1e-3 and 5 -> 10, 20, 40 grid points.
E. New case: steel rod, ends held at 150 C and 30 C.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"


def system(n, left, right):
    A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n)
    b[0], b[-1] = left, right
    return A, b


def jacobi(A, b, tol):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    for it in range(1, 100000):
        x_new = (b - R @ x) / D
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, it
        x = x_new
    return x, it


def gauss_seidel(A, b, tol):
    x = np.zeros_like(b)
    for it in range(1, 100000):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ old[i + 1:]) / A[i, i]
        if np.linalg.norm(x - old, np.inf) < tol:
            return x, it
    return x, it


# ---- C. Parameter change ------------------------------------------------------------
print("C. Iterations needed (ends 100 C / 20 C)")
print(f"  {'n':>3} {'tol':>7} {'Jacobi':>8} {'Gauss-Seidel':>13}")
for n in (5, 10, 20, 40):
    for tol in (1e-8, 1e-3):
        A, b = system(n, 100.0, 20.0)
        _, ij = jacobi(A, b, tol)
        _, ig = gauss_seidel(A, b, tol)
        print(f"  {n:>3} {tol:>7.0e} {ij:>8} {ig:>13}")

# ---- E. New case: steel rod --------------------------------------------------------------
n = 20
A, b = system(n, 150.0, 30.0)
x_gs, it = gauss_seidel(A, b, 1e-8)
x_exact = np.linalg.solve(A, b)
print(f"\nE. New case: steel rod, {n} interior points, ends 150 C and 30 C")
print(f"  Gauss-Seidel converged in {it} iterations; max error vs direct = {np.abs(x_gs - x_exact).max():.2e} C")
print(f"  temperature at midpoint: {x_gs[n // 2]:.2f} C (linear profile -> expected {(150 + 30) / 2 - (150 - 30) / (2 * (n + 1)):.2f} C)")
pos = np.linspace(0, 1, n + 2)
profile = np.concatenate([[150.0], x_gs, [30.0]])
plt.plot(pos, profile, marker="o")
plt.xlabel("Position along rod (fraction of length)")
plt.ylabel("Temperature (C)")
plt.title("Steady-state temperature in a steel rod")
plt.grid(True)
plt.savefig(FIG / "ext_task_08_rod_profile.png", dpi=150, bbox_inches="tight")
