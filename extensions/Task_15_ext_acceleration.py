"""Task 15 extension - acceleration and harsh braking of a bus from speed data.

C. Parameter change: step size h for forward vs central differences.
E. New case: telematics - acceleration from velocity samples with np.gradient.
"""
import numpy as np

# ---- C. Parameter change: step size -------------------------------------------------------------------
x0, exact = 1.0, np.cos(1.0)     # derivative of sin at x = 1
print("C. Error of d/dx sin(x) at x=1 for different step sizes h")
print(f"  {'h':>8} {'forward err':>13} {'central err':>13}")
for h in (1.0, 0.1, 0.01, 1e-4, 1e-8, 1e-12):
    fwd = (np.sin(x0 + h) - np.sin(x0)) / h
    cen = (np.sin(x0 + h) - np.sin(x0 - h)) / (2 * h)
    print(f"  {h:>8.0e} {abs(fwd - exact):>13.3e} {abs(cen - exact):>13.3e}")
print("  Error falls with h (truncation) until round-off takes over for tiny h.")

# ---- E. New case: bus telematics -------------------------------------------------------------------------
t = np.arange(0, 21, 2.0)                                              # seconds
v = np.array([0, 3.0, 7.5, 11.0, 13.5, 14.0, 13.8, 9.0, 4.0, 1.0, 0.0])  # speed in m/s
a = np.gradient(v, t)          # central differences inside, one-sided at the ends
print("\nE. New case: bus acceleration from 2-second speed samples")
for ti, vi, ai in zip(t, v, a):
    print(f"  t={ti:>4.0f}s  v={vi:>5.1f} m/s  a={ai:+6.2f} m/s^2")
harsh = t[a < -1.5]
print(f"  harsh braking (a < -1.5 m/s^2) at t = {harsh.tolist()} s")
print(f"  peak deceleration {a.min():.2f} m/s^2, peak acceleration {a.max():.2f} m/s^2")
print("  note: 2 s sampling smooths short spikes; sample faster to catch sudden braking.")
