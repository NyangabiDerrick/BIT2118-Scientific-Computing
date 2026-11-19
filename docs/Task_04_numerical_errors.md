# Task 4 – Floating-Point Arithmetic and Numerical Errors

Programs: [`code/Task_04_numerical_errors.py`](../code/Task_04_numerical_errors.py) · [`extensions/Task_04_ext_banking_sums.py`](../extensions/Task_04_ext_banking_sums.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Inputs | 0.1, 0.2, 0.3; √2 and its approximation 1.414; x = 10⁻⁴, 10⁻⁸, 10⁻¹² |
| Operations | exact `==` vs `np.isclose`; absolute error \|true − approx\|; relative error = absolute / \|true\|; comparison of the unstable form (√(1+x) − 1)/x with the algebraically equal stable form 1/(√(1+x) + 1) |

## C. Changing an input

* **Precision (float64 → float32):** `0.1 + 0.2 == 0.3` is `False` in float64 but `True` in float32, because float32 has only ≈ 7 digits (machine epsilon 1.19 × 10⁻⁷ vs 2.22 × 10⁻¹⁶) so the tiny difference is rounded away.
* **Tolerance of `isclose`:** `atol = 1e-20` → `False`; `1e-12` → `True`; `1e-3` → `True`. A tolerance that is too tight rejects values that are equal for all practical purposes; too loose accepts genuinely different ones.

## D. Meaning of the output

```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

* 0.1 and 0.2 have no exact binary representation, so their sum is 0.30000000000000004 – "equal" must be tested with a tolerance.
* Rounding √2 to 1.414 gives a relative error of about 0.015 %.
* The true limit of (√(1+x) − 1)/x as x → 0 is 0.5. The direct formula subtracts two nearly equal numbers (**catastrophic cancellation**) and is wrong in the 5th digit at x = 10⁻¹² (0.50004445), while the algebraically rearranged form stays exact. *Mathematically equal does not mean numerically equal.*

## E. Different real-world case – accumulating bank deposits

* **Assumptions:** one million deposits of exactly 0.10 are added to a balance; the exact answer is 100,000.00 (computed with `Decimal`).
* **Methods compared:** naive loop in float64, `np.sum` (pairwise summation), `math.fsum` (error-compensated), and a naive float32 loop of 100,000 deposits.
* **Output:**
  ```
  exact (Decimal)        : 100000.00
  naive float64 loop     : 100000.0000013329  error 1.333e-06
  np.sum (pairwise)      : 100000.0000000000  error 2.910e-11
  math.fsum              : 100000.0000000000  error 0.000e+00
  naive float32, 100,000 : 9998.5566  (error 1.443)
  ```
* **Interpretation:** each addition adds a tiny rounding error and they accumulate. The naive double-precision loop drifts by about a millionth of a unit; float32 loses 1.44 currency units after only 100,000 deposits – unacceptable in banking. Use integer cents or `Decimal` for money, and summation algorithms that limit error growth for scientific data.
