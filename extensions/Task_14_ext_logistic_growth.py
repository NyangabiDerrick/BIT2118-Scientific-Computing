"""Task 14 extension - logistic growth of mobile-money subscribers.

C. Parameter change: fit linear / quadratic / cubic models and compare RMSE.
E. New case: S-shaped (logistic) adoption curve with curve_fit and forecasting.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

FIG = Path(__file__).resolve().parent.parent / "figures"

# ---- C. Parameter change: model choice on the original server data -------------------------------
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
print("C. Polynomial degree on the server data (RMSE in ms)")
for deg in (1, 2, 3):
    p = np.polyfit(users, resp, deg)
    rmse = np.sqrt(np.mean((resp - np.polyval(p, users)) ** 2))
    print(f"  degree {deg}: RMSE {rmse:6.2f}, prediction at 400 users {np.polyval(p, 400):7.1f} ms")

# ---- E. New case: logistic growth ------------------------------------------------------------------
# Subscribers (millions) in a country over 10 years (synthetic data with noise, seed 1).
rng = np.random.default_rng(1)
years = np.arange(0, 10, dtype=float)


def logistic(t, K, r, t0):
    return K / (1 + np.exp(-r * (t - t0)))


true = logistic(years, 38.0, 0.9, 4.5)
obs = true + rng.normal(0, 0.8, len(years))
popt, pcov = curve_fit(logistic, years, obs, p0=[obs.max() * 1.5, 0.5, 5.0])
K, r, t0 = popt
err = np.sqrt(np.diag(pcov))
rmse = np.sqrt(np.mean((obs - logistic(years, *popt)) ** 2))
print("\nE. New case: logistic adoption of mobile money")
print(f"  carrying capacity K = {K:.1f} +/- {err[0]:.1f} million subscribers")
print(f"  growth rate r = {r:.3f}/yr, midpoint t0 = {t0:.2f} years, RMSE = {rmse:.2f}")
for y in (10, 12, 15):
    print(f"  forecast year {y}: {logistic(y, *popt):.1f} million")
p2 = np.polyfit(years, obs, 2)
print(f"  quadratic would forecast {np.polyval(p2, 15):.1f} million in year 15 (unrealistic: no ceiling)")

x = np.linspace(0, 15, 300)
plt.scatter(years, obs, label="Observed")
plt.plot(x, logistic(x, *popt), label="Logistic fit")
plt.plot(x, np.polyval(p2, x), "--", label="Quadratic fit")
plt.axhline(K, linestyle=":", color="gray")
plt.xlabel("Year")
plt.ylabel("Subscribers (millions)")
plt.ylim(0, K * 1.6)
plt.title("Logistic growth of mobile-money adoption")
plt.legend()
plt.grid(True)
plt.savefig(FIG / "ext_task_14_logistic.png", dpi=150, bbox_inches="tight")
