"""Task 2 extension - IoT soil-moisture sensors on a farm.

C. Parameter change: inject a faulty spike into the original temperature data.
E. New case: 24 hourly soil-moisture readings (%) -> irrigation decisions.
"""
import numpy as np

# ---- C. Parameter change on the original weather data -----------------------
temps = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
spiky = temps.copy()
spiky[12] = 60.0  # one faulty sensor reading at 12:00
print("C. Parameter change (one faulty reading, hour 12: 29.4 -> 60.0)")
print(f"  mean   : {temps.mean():.2f} -> {spiky.mean():.2f} C")
print(f"  max    : {temps.max():.2f} -> {spiky.max():.2f} C")
print(f"  median : {np.median(temps):.2f} -> {np.median(spiky):.2f} C  (robust to the spike)")

# ---- E. New case: soil moisture ---------------------------------------------
# Assumptions: one probe per hour, volumetric moisture in %, crop needs >= 30 %.
moisture = np.array([
    41, 40, 39, 38, 37, 36, 35, 33, 31, 29, 27, 26,
    25, 25, 26, 28, 30, 33, 36, 38, 40, 41, 41, 40], dtype=float)
threshold = 30.0
dry = moisture < threshold
hours = np.arange(24)
print("\nE. New case: soil-moisture irrigation monitor")
print(f"  mean / min / max moisture: {moisture.mean():.2f} / {moisture.min():.0f} / {moisture.max():.0f} %")
print(f"  hours below {threshold:.0f}% (irrigate): {hours[dry].tolist()}")
print(f"  hours of water stress: {dry.sum()} of 24")
deficit = np.clip(threshold - moisture, 0, None)   # vectorized, no loop
print(f"  total moisture deficit: {deficit.sum():.0f} %-hours")
