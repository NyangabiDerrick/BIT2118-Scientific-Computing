# Task 12 – Polynomial and Nonlinear Equation Solving

Programs: [`code/Task_12_nonlinear_equations.py`](../code/Task_12_nonlinear_equations.py) · [`extensions/Task_12_ext_chemical_equilibrium.py`](../extensions/Task_12_ext_chemical_equilibrium.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Equations | circle x² + y² = 4 and parabola y = x² − 1, written as residuals F(x, y) = [x² + y² − 4, y − (x² − 1)] = 0 |
| Inputs | initial guesses (1, 1) and (−1, 1) |
| Operations | `scipy.optimize.root` iteratively adjusts (x, y) (Newton-type/hybrid method) until both residuals are ≈ 0 |

## C. Changing an input

Circle radius 2 → 1 → 0.5 (solved from 33 different starting guesses each):

| Radius | Intersections found |
|---|---|
| 2.0 | 2: (±1.517, 1.303) |
| 1.0 | 3: (±1, 0) and (0, −1) |
| 0.5 | none |

**Explanation:** substituting x² = y + 1 gives y² + y + 1 = r². The number of intersections depends on r: for r < √3/2 ≈ 0.866 the quadratic in y has no valid root (circle too small to touch the parabola), for r = 1 it has two roots (y = 0 and y = −1), and for r = 2 only one root has x² ≥ 0. Non-linear systems may have several solutions or none, and the solver finds the one *near its starting guess* – so several guesses are needed.

## D. Meaning of the output

```
Initial guess: [1.0, 1.0]    Intersection: [1.51748991 1.30277564]   Converged: True
Initial guess: [-1.0, 1.0]   Intersection: [-1.51748991 1.30277564]  Converged: True
Residuals ≈ −2.5e-13
```

The two guesses lead to the two mirror-image intersection points (±1.5175, 1.3028). Check: 1.5175² + 1.3028² = 2.303 + 1.697 = 4.000 ✓ and 1.5175² − 1 = 1.303 ✓. Residuals of about 10⁻¹³ mean both equations are satisfied to numerical precision; `Converged: True` confirms the solver succeeded.

## E. Different real-world case – chemical equilibrium (polynomial equation)

* **Assumptions:** reaction A + B ⇌ C at constant temperature, equilibrium constant K = [C]/([A][B]) = 5 L/mol; initial concentrations [A] = 1.0, [B] = 0.8, [C] = 0 mol/L. Let x = [C] at equilibrium.
* **Method:** K(1 − x)(0.8 − x) = x → 5x² − 10x + 4 = 0, solved with `np.roots`; the physical root must satisfy 0 ≤ x ≤ 0.8.
* **Output:**
  ```
  polynomial roots: [1.44721 0.55279] -> only 0.55279 is physical (cannot exceed 0.8)
  [C] = 0.5528 mol/L, [A] = 0.4472, [B] = 0.2472, check K = 5.000000
  with K =  1.0: [C] = 0.3230 mol/L  (40.4% of B converted)
  with K = 20.0: [C] = 0.6892 mol/L  (86.1% of B converted)
  ```
* **Interpretation:** the second root, 1.447 mol/L, is mathematically valid but impossible (it would use more B than exists). At equilibrium 69 % of B has reacted. A larger K favours the product: 86 % conversion at K = 20 vs 40 % at K = 1.
