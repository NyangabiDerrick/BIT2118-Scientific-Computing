# Task 2 – NumPy Arrays and Numerical Computation

Programs: [`code/Task_02_numpy_arrays.py`](../code/Task_02_numpy_arrays.py) · [`extensions/Task_02_ext_soil_moisture.py`](../extensions/Task_02_ext_soil_moisture.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Input | `temperatures_c`: 24 hourly readings in °C (17.5 … 29.4) |
| Operations | mean = Σxᵢ / 24, minimum, maximum, and the element-wise conversion **F = 1.8·C + 32** applied to the whole array at once (no loop) |

## C. Changing an input

One reading (12:00) was replaced by a faulty value of 60 °C:

| Statistic | Original | After change |
|---|---|---|
| Mean | 23.12 °C | 24.40 °C |
| Maximum | 29.40 °C | 60.00 °C |
| Median | 22.75 °C | 22.75 °C |

**Explanation:** the mean uses every value, so one bad sensor shifts it by (60 − 29.4)/24 ≈ 1.3 °C, and the maximum is replaced outright. The median depends only on the middle of the sorted data, so it did not move. For IoT data with occasional faulty readings, robust statistics (median) are safer.

## D. Meaning of the output

```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

The day averaged 23.12 °C. It was coldest (17.5 °C) in the early morning (hour index 3) and hottest (29.4 °C) around midday (index 12). The first six Fahrenheit values are the early-morning readings, e.g. 18.5 °C → 1.8 × 18.5 + 32 = 65.3 °F. No graph is produced by this task.

## E. Different real-world case – IoT soil-moisture monitoring

* **Assumptions:** one probe reads volumetric soil moisture (%) every hour; the crop needs at least 30 %; readings are accurate.
* **Input data:** 24 hourly values between 25 % and 41 %.
* **Method:** mean/min/max as before, a boolean mask `moisture < 30` to find dry hours, and `np.clip(30 - moisture, 0, None)` to compute the moisture deficit – all vectorised.
* **Output:**
  ```
  mean / min / max moisture: 33.96 / 25 / 41 %
  hours below 30% (irrigate): [9, 10, 11, 12, 13, 14, 15]
  hours of water stress: 7 of 24
  total moisture deficit: 24 %-hours
  ```
* **Interpretation:** the soil dries during the day (evaporation peaks 12:00–14:00) and recovers at night. The farmer should irrigate between roughly 09:00 and 15:00; a controller could switch the pump on whenever the mask is `True`.
