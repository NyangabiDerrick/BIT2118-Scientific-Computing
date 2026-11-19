# Task 16 – Numerical Integration

Programs: [`code/Task_16_numerical_integration.py`](../code/Task_16_numerical_integration.py) · [`extensions/Task_16_ext_borehole_volume.py`](../extensions/Task_16_ext_borehole_volume.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Inputs | smart-meter times [0, 2, 4, …, 12] h and power [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9] kW |
| Operations | energy E = ∫ P(t) dt. **Trapezoidal rule:** Σ ½(Pᵢ + Pᵢ₊₁)Δt. **Simpson's rule:** fits parabolas through groups of three points (weights 1-4-2-4-…-1 × Δt/3). Units: kW × h = kWh. |

(`np.trapezoid` needs NumPy ≥ 2.0; on older versions use `np.trapz`.)

## C. Changing an input

The number of sample points was changed on a function with a known integral, ∫₀^π sin x dx = 2:

| Points | Trapezoid error | Simpson error |
|---|---|---|
| 5 | 1.0 × 10⁻¹ | 4.6 × 10⁻³ |
| 9 | 2.6 × 10⁻² | 2.7 × 10⁻⁴ |
| 17 | 6.4 × 10⁻³ | 1.7 × 10⁻⁵ |
| 33 | 1.6 × 10⁻³ | 1.0 × 10⁻⁶ |

**Explanation:** doubling the number of intervals divides the trapezoid error by ≈ 4 (error ∝ h²) but the Simpson error by ≈ 16 (∝ h⁴). For smooth data Simpson's rule is much more accurate for the same number of measurements.

## D. Meaning of the output

```
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule:   15.800 kWh
Difference between estimates:  0.100 kWh
```

Over the 12 hours covered by the readings the appliance/household used about **15.7–15.8 kWh** (the area under the power-time curve). The two estimates differ by only 0.1 kWh (0.6 %), which gives a rough idea of the numerical error. Note that the data cover 0–12 h only; a full-day figure would need readings up to 24 h. No graph is produced.

## E. Different real-world case – water pumped by a borehole

* **Assumptions:** flow rate (L/min) is measured every 10 minutes during one hour of pumping; the flow varies smoothly between readings; the tank holds 2,500 L.
* **Input data:** t = 0…60 min, flow = [0, 42, 55, 58, 56, 50, 41] L/min.
* **Output:**
  ```
  trapezoid: 2,815.0 L; Simpson: 2,876.7 L; difference 61.7 L
  average flow = 47.9 L/min
  hours of pumping to fill the tank at this rate: 0.87 h
  ```
* **Interpretation:** about 2,800–2,900 L are pumped in the hour, so the 2,500 L tank fills in ≈ 52 minutes. The 62 L difference between rules is mainly because the flow rises sharply at the start (0 → 42 L/min), where the straight-line trapezoid approximation is poorest; finer sampling early in the cycle would reduce the uncertainty.
