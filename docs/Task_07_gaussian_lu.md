# Task 7 – Gaussian Elimination and LU Decomposition

Programs: [`code/Task_07_gaussian_lu.py`](../code/Task_07_gaussian_lu.py) · [`extensions/Task_07_ext_leontief_lu.py`](../extensions/Task_07_ext_leontief_lu.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Inputs | tridiagonal 3 × 3 matrix A = [[4,−1,0],[−1,4,−1],[0,−1,3]] and three measurement vectors b₁ = [15,10,10], b₂ = [16,11,9], b₃ = [14,12,11] |
| Operations | `lu_factor(A)` computes PA = LU **once** (Gaussian elimination with partial pivoting); `lu_solve` then does only forward and back substitution for each b; residual b − A x checks the answer |

## C. Changing an input

Problem size and number of measurement vectors were changed from 3 × 3 with 3 vectors to **300 × 300 with 500 vectors**:

| Strategy | Time |
|---|---|
| `np.linalg.solve` for each b (re-eliminates every time) | 3.33 s |
| `lu_factor` once, `lu_solve` 500 times | 0.33 s (≈ 10× faster) |

**Explanation:** factorisation costs about (2/3)n³ operations, while each triangular solve costs only about 2n². Reusing the factors turns 500 expensive solves into 1 expensive factorisation plus 500 cheap solves. (Exact timings vary by machine.)

## D. Meaning of the output

```
Measurement set 1   Solution: [5. 5. 5.]                      Residual norm: 0.0
Measurement set 2   Solution: [5.31707317 5.26829268 4.75609756]  Residual norm: 1.8e-15
Measurement set 3   Solution: [4.90243902 5.6097561  5.53658537]  Residual norm: 0.0
Direct solution for first set: [5. 5. 5.]
```

Each row is the unknown vector x for one measurement vector. For set 1, x = [5, 5, 5] satisfies 4·5 − 5 = 15, −5 + 20 − 5 = 10, −5 + 15 = 10. The LU answer equals the direct solver's answer, and the residuals are zero to machine precision (≈ 10⁻¹⁵), so the factorisation is accurate.

## E. Different real-world case – Leontief input–output economy

* **Assumptions:** a three-sector economy (Agriculture, Manufacturing, Services). Entry aᵢⱼ is the amount of sector i's output needed to produce one unit of sector j's output. Total output x must satisfy x = a·x + d, i.e. **(I − a)x = d**, where d is final demand (million KES).
* **Input data:** a = [[0.20,0.15,0.05],[0.25,0.30,0.20],[0.10,0.20,0.15]]; demand scenarios: baseline [100,150,200], export boom [100,250,200], services recession [100,150,120].
* **Output:**
  ```
  baseline demand      -> total output [221.09 394.42 354.11]  (sum 969.6)
  export boom (mfg)    -> total output [255.19 561.86 397.52]  (sum 1214.6)
  services recession   -> total output [208.19 360.19 250.42]  (sum 818.8)
  ```
* **Interpretation:** total production must exceed final demand because sectors consume each other's output (agriculture must make 221 to satisfy a demand of only 100). A boom in manufacturing demand of +100 raises manufacturing output by 167 and also raises the other sectors. The matrix (I − a) is factored once and reused for each scenario, which is the main benefit of LU in economic planning.
