"""Task 12 extension - polynomial solving for chemical equilibrium.

C. Parameter change: circle radius 2 -> 1 and more initial guesses.
E. New case: A + B <-> C, equilibrium concentration from a quadratic.
"""
import numpy as np
from scipy.optimize import root

# ---- C. Parameter change ------------------------------------------------------------------------
for radius in (2.0, 1.0, 0.5):
    eq = lambda z, r=radius: [z[0] ** 2 + z[1] ** 2 - r ** 2, z[1] - (z[0] ** 2 - 1)]
    found = set()
    for gx in np.linspace(-2.5, 2.5, 11):
        for gy in (-1.5, 0.0, 1.5):
            s = root(eq, [gx, gy])
            if s.success and np.linalg.norm(eq(s.x)) < 1e-9:
                found.add((round(float(s.x[0]), 6) + 0.0, round(float(s.x[1]), 6) + 0.0))
    pts = ", ".join(f"({px:.3f}, {py:.3f})" for px, py in sorted(found))
    print(f"C. radius {radius}: {len(found)} intersection(s): {pts or 'none'}")

# ---- E. New case: equilibrium ------------------------------------------------------------------------
# A + B <-> C with K = [C] / ([A][B]).  Start: [A]=1.0, [B]=0.8 mol/L, [C]=0, K = 5 L/mol.
a0, b0, K = 1.0, 0.8, 5.0
# K (a0-x)(b0-x) = x  ->  K x^2 - (K(a0+b0)+1) x + K a0 b0 = 0
coeffs = [K, -(K * (a0 + b0) + 1), K * a0 * b0]
roots = np.roots(coeffs)
physical = [r.real for r in roots if abs(r.imag) < 1e-12 and 0 <= r.real <= min(a0, b0)]
x = physical[0]
print("\nE. New case: chemical equilibrium A + B <-> C (K = 5)")
print("  polynomial roots:", np.round(roots, 5), "-> only", round(x, 5), "is physical (cannot exceed 0.8)")
print(f"  [C] = {x:.4f} mol/L, [A] = {a0 - x:.4f}, [B] = {b0 - x:.4f}")
print(f"  check K = {x / ((a0 - x) * (b0 - x)):.6f}")
for K2 in (1.0, 20.0):
    r2 = np.roots([K2, -(K2 * (a0 + b0) + 1), K2 * a0 * b0])
    x2 = [r.real for r in r2 if 0 <= r.real <= 0.8][0]
    print(f"  with K = {K2:>4}: [C] = {x2:.4f} mol/L  ({x2 / b0:.1%} of B converted)")
