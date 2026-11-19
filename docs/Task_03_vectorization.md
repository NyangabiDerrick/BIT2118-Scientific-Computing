# Task 3 – Mathematical Functions and Vectorization

Programs: [`code/Task_03_vectorization.py`](../code/Task_03_vectorization.py) · [`extensions/Task_03_ext_mobile_fees.py`](../extensions/Task_03_ext_mobile_fees.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Input | `latency_ms`: 1,000,000 random latencies uniform on [5, 250] ms (seed 42) |
| Operations | s = ms / 1000, then s² for every element; done twice – once with a Python `for` loop, once with a single NumPy expression – and timed with `timeit` |

## C. Changing an input

The array size N was changed from 1,000,000 to 100,000:

| N | Loop | Vectorized | Speed-up |
|---|---|---|---|
| 100,000 | 0.0295 s | 0.0033 s | ≈ 9× |
| 1,000,000 | 0.2844 s | 0.0048 s | ≈ 59× |

**Explanation:** work grows linearly with N for both methods, but the loop pays Python's per-iteration overhead on every element while NumPy runs one compiled loop. Timings vary from run to run and from machine to machine (the original program measured ≈ 83× on this computer), but vectorized code is always far faster at this scale.

## D. Meaning of the output

```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.5051 s
Vectorized time: 0.0061 s
Approximate speed-up: 82.9x
```

The first numbers are latency² in s² (e.g. 194.6 ms = 0.1946 s → 0.0379 s²). Both methods give the same result, but the vectorized one finished in about 6 ms instead of half a second. For a monitoring system that must process millions of samples per minute, this is the difference between keeping up and falling behind. No graph is produced.

## E. Different real-world case – tiered mobile-money fees

* **Assumptions:** illustrative tariff (KES): amount ≤ 100 → 0; ≤ 1,000 → 11; ≤ 10,000 → 28; above that → 0.5 % of the amount, capped at 200. Payment amounts are log-normally distributed (many small, few large).
* **Input data:** 1,000,000 simulated payments (seed 7).
* **Method:** `np.select` evaluates the whole tariff on the array at once; checked against a loop with `np.allclose`.
* **Output:**
  ```
  total value moved : 827,830,795 KES
  total fees earned : 13,649,048 KES (1.649% of value)
  loop 0.213s vs vectorized 0.0251s -> 9x faster
  ```
* **Interpretation:** about 1.65 % of the money moved is collected as fees. Because `np.select` computes every branch for every element, the speed-up (≈ 9×) is smaller than in the pure arithmetic case, but the code is much shorter and both methods agree exactly.
