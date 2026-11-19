"""Task 16 extension - total water pumped by a borehole.

C. Parameter change: number of sample points for a function with a known answer.
E. New case: flow-rate readings (litres/minute) integrated into total litres.
"""
import numpy as np
from scipy.integrate import simpson

# ---- C. Parameter change: sampling density --------------------------------------------------------------
# Integral of sin(x) from 0 to pi is exactly 2.
print("C. Integral of sin(x) on [0, pi] (exact value 2)")
print(f"  {'points':>7} {'trapezoid err':>15} {'Simpson err':>13}")
for n in (5, 9, 17, 33):
    x = np.linspace(0, np.pi, n)
    y = np.sin(x)
    print(f"  {n:>7} {abs(np.trapezoid(y, x) - 2):>15.2e} {abs(simpson(y, x=x) - 2):>13.2e}")

# ---- E. New case: borehole -------------------------------------------------------------------------------------
# Flow in litres/minute measured every 10 minutes over one hour of pumping.
t_min = np.arange(0, 61, 10, dtype=float)
flow = np.array([0.0, 42.0, 55.0, 58.0, 56.0, 50.0, 41.0])
trap = np.trapezoid(flow, t_min)
simp = simpson(flow, x=t_min)
print("\nE. New case: borehole pump, flow every 10 minutes")
print(f"  trapezoid: {trap:,.1f} L; Simpson: {simp:,.1f} L; difference {abs(trap - simp):.1f} L")
print(f"  average flow = {simp / 60:.1f} L/min")
tank = 2500.0
print(f"  a {tank:,.0f} L tank would be {min(simp / tank, 1):.0%} full after one hour")
print(f"  hours of pumping to fill the tank at this rate: {tank / simp:.2f} h")
