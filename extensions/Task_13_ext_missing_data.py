"""Task 13 extension - filling missing air-quality sensor readings.

C. Parameter change: change one measurement and use another interpolation kind.
E. New case: PM2.5 sensor dropped three hours; reconstruct them.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, interp1d

FIG = Path(__file__).resolve().parent.parent / "figures"

# ---- C. Parameter change ------------------------------------------------------------------------
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
for temp12 in (25.0, 29.0):
    temp = np.array([18.0, 20.0, 22.5, 24.0, temp12, 25.5, 25.0])
    lin, cub = interp1d(hours, temp)(10.5), CubicSpline(hours, temp)(10.5)
    quad = interp1d(hours, temp, kind="quadratic")(10.5)
    print(f"C. reading at 12:00 = {temp12}: 10:30 linear {float(lin):.2f}, quadratic {float(quad):.2f}, cubic {float(cub):.2f}")

# ---- E. New case ----------------------------------------------------------------------------------
# PM2.5 in micrograms/m3, hourly. The sensor lost power at 13:00, 14:00, 15:00.
t = np.arange(8, 21, dtype=float)
pm = np.array([22, 25, 31, 38, 44, np.nan, np.nan, np.nan, 61, 55, 47, 40, 33], dtype=float)
ok = ~np.isnan(pm)
lin = interp1d(t[ok], pm[ok])
cub = CubicSpline(t[ok], pm[ok])
missing = t[~ok]
print("\nE. New case: reconstruct missing PM2.5 readings (ug/m3)")
print(f"  {'hour':>5} {'linear':>8} {'cubic':>8}")
for h in missing:
    print(f"  {h:>5.0f} {float(lin(h)):>8.1f} {float(cub(h)):>8.1f}")
fine = np.linspace(8, 20, 241)
print("  health note: values above 35 ug/m3 are 'unhealthy for sensitive groups';")
print(f"  hours above 35 ug/m3 over 08:00-20:00 (cubic estimate): {np.sum(cub(fine) > 35) * (fine[1] - fine[0]):.1f} h")
print("  caution: interpolation cannot recover a real pollution peak that fell inside the gap.")

plt.scatter(t[ok], pm[ok], label="Measured")
plt.plot(fine, lin(fine), label="Linear")
plt.plot(fine, cub(fine), label="Cubic spline")
plt.axhline(35, linestyle=":", color="gray")
plt.xlabel("Hour of day")
plt.ylabel("PM2.5 (ug/m3)")
plt.title("Reconstructing missing air-quality data")
plt.legend()
plt.grid(True)
plt.savefig(FIG / "ext_task_13_pm25.png", dpi=150, bbox_inches="tight")
