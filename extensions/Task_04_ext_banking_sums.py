"""Task 4 extension - accumulated round-off in banking.

C. Parameter change: float32 instead of float64, and tolerance changes.
E. New case: summing one million 0.10 deposits - naive loop, pairwise and exact.
"""
import math
from decimal import Decimal

import numpy as np

# ---- C. Parameter change -----------------------------------------------------
print("C. Precision / tolerance changes")
print("  float64: 0.1+0.2 ==0.3 ->", np.float64(0.1) + np.float64(0.2) == np.float64(0.3))
print("  float32: 0.1+0.2 ==0.3 ->", np.float32(0.1) + np.float32(0.2) == np.float32(0.3))
print("  eps float64 = %.2e, eps float32 = %.2e" % (np.finfo(np.float64).eps, np.finfo(np.float32).eps))
for tol in (1e-20, 1e-12, 1e-3):
    print(f"  isclose(0.1+0.2, 0.3, atol={tol:g}, rtol=0) ->", np.isclose(0.1 + 0.2, 0.3, rtol=0, atol=tol))

# ---- E. New case: one million deposits of 0.10 --------------------------------
n = 1_000_000
true_total = Decimal("0.10") * n          # exact decimal arithmetic = 100000.00
naive = 0.0
for _ in range(n):
    naive += 0.1
pairwise = float(np.sum(np.full(n, 0.1)))  # NumPy pairwise summation
fsum = math.fsum([0.1] * n)                # error-compensated summation
naive32 = np.float32(0.0)
for _ in range(100_000):                   # fewer terms: float32 drifts fast
    naive32 += np.float32(0.1)

print("\nE. New case: adding one million deposits of 0.10")
print(f"  exact (Decimal)        : {true_total}")
print(f"  naive float64 loop     : {naive:.10f}  error {abs(naive - float(true_total)):.3e}")
print(f"  np.sum (pairwise)      : {pairwise:.10f}  error {abs(pairwise - float(true_total)):.3e}")
print(f"  math.fsum              : {fsum:.10f}  error {abs(fsum - float(true_total)):.3e}")
print(f"  naive float32, 100,000 : {float(naive32):.4f}  (exact 10000.0, error {abs(float(naive32) - 10000.0):.3f})")
print("  Lesson: store money as integer cents or Decimal; never compare floats with ==.")
