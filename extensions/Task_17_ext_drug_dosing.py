"""Task 17 extension - drug concentration with repeated doses (Euler method).

C. Parameter change: step size h = 1, 0.5, 0.1 on the cooling problem.
E. New case: dA/dt = -k A with 100 mg doses every 8 hours.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"

# ---- C. Parameter change: step size ------------------------------------------------------------------------
Ta, T0, k = 25.0, 90.0, 0.12
print("C. Euler error at t = 30 min for cooling dT/dt = -k (T - Ta)")
for h in (4.0, 1.0, 0.5, 0.1, 0.01):
    t = np.arange(0, 30 + h / 2, h)
    T = T0
    for _ in range(len(t) - 1):
        T += h * (-k * (T - Ta))
    exact = Ta + (T0 - Ta) * np.exp(-k * 30)
    print(f"  h = {h:>5}: Euler {T:7.3f} C, exact {exact:.3f} C, error {abs(T - exact):.4f} C")
print("  Halving h roughly halves the error (Euler is first order).")
print("  Stability: with h = 20 (> 2/k = 16.7) Euler oscillates and diverges:")
T = T0
for _ in range(3):
    T += 20 * (-k * (T - Ta))
    print(f"    T = {T:.1f}")

# ---- E. New case: dosing ------------------------------------------------------------------------------------------
k_el = 0.2           # elimination rate constant per hour (half-life ~3.5 h)
dose = 100.0         # mg taken at each dose
interval = 8.0       # hours
h = 0.05
t = np.arange(0, 48 + h / 2, h)
A = np.zeros_like(t)
A[0] = dose
dose_steps = {int(round(d / h)) for d in np.arange(interval, 48, interval)}
for i in range(len(t) - 1):
    A[i + 1] = A[i] + h * (-k_el * A[i])
    if (i + 1) in dose_steps:
        A[i + 1] += dose
peak_after_last = A[int(round(40 / h))]
print("\nE. New case: 100 mg every 8 h, elimination k = 0.2 /h, Euler h = 0.05 h")
print(f"  amount in body just after dose at 8 h : {A[int(round(8 / h))]:.1f} mg")
print(f"  amount just after dose at 40 h        : {peak_after_last:.1f} mg")
steady_peak = dose / (1 - np.exp(-k_el * interval))
print(f"  theoretical steady-state peak         : {steady_peak:.1f} mg")
print(f"  trough just before a dose at 40 h     : {A[int(round(40 / h)) - 1]:.1f} mg")
print(f"  half-life = ln2/k = {np.log(2) / k_el:.2f} h")

plt.plot(t, A)
plt.xlabel("Time (hours)")
plt.ylabel("Drug in body (mg)")
plt.title("Repeated dosing, Euler simulation")
plt.grid(True)
plt.savefig(FIG / "ext_task_17_dosing.png", dpi=150, bbox_inches="tight")
