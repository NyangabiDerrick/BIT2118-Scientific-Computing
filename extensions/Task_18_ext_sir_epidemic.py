"""Task 18 extension - SIR epidemic model with solve_ivp.

C. Parameter change: RC time constant (R = 1000 -> 2000 ohms).
E. New case: epidemic in a population of 10,000, with and without interventions.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

FIG = Path(__file__).resolve().parent.parent / "figures"

# ---- C. Parameter change: RC circuit ----------------------------------------------------------------------------
Vs, C = 5.0, 0.001
print("C. RC charging, voltage at t = 1 s and time to reach 63.2% (one time constant)")
for R in (500.0, 1000.0, 2000.0):
    sol = solve_ivp(lambda t, V: [(Vs - V[0]) / (R * C)], (0, 10), [0.0], t_eval=np.linspace(0, 10, 2001), rtol=1e-9, atol=1e-11)
    t63 = sol.t[np.argmax(sol.y[0] >= 0.632 * Vs)]
    print(f"  R = {R:>6.0f} ohm, tau = {R*C:.1f} s: V(1 s) = {np.interp(1.0, sol.t, sol.y[0]):.3f} V, t(63%) ~ {t63:.2f} s")

# ---- E. New case: SIR ------------------------------------------------------------------------------------------------------
N = 10_000


def sir(t, y, beta, gamma):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]


gamma = 0.1                      # recovery rate: infectious ~10 days
t_eval = np.linspace(0, 160, 641)
print("\nE. New case: SIR epidemic, N = 10,000, 10 initially infected, gamma = 0.1/day")
plt.figure()
for beta, label in ((0.3, "no intervention (R0=3.0)"), (0.18, "distancing (R0=1.8)"), (0.09, "strong control (R0=0.9)")):
    sol = solve_ivp(sir, (0, 160), [N - 10, 10, 0], args=(beta, gamma), t_eval=t_eval, rtol=1e-8, atol=1e-10)
    S, I, Rr = sol.y
    peak = I.max()
    print(f"  {label:<26}: peak infected {peak:7.0f} on day {sol.t[I.argmax()]:5.1f}; total ever infected {N - S[-1]:7.0f}")
    plt.plot(sol.t, I, label=label)
plt.xlabel("Day")
plt.ylabel("Currently infected")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True)
plt.savefig(FIG / "ext_task_18_sir.png", dpi=150, bbox_inches="tight")
print("  Rule of thumb: R0 = beta/gamma > 1 -> epidemic grows; < 1 -> dies out.")
