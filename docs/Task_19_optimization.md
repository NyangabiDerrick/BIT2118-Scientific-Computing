# Task 19 – Numerical Optimization

Programs: [`code/Task_19_optimization.py`](../code/Task_19_optimization.py) · [`extensions/Task_19_ext_feed_mix.py`](../extensions/Task_19_ext_feed_mix.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Objective | minimise cost = 12x + 18y (x, y = units of server Type A and B) |
| Constraints | capacity 100x + 170y ≥ 1000; x ≥ 0, y ≥ 0 |
| Inputs | starting point (5, 3); method SLSQP (sequential quadratic programming) |
| Operations | `scipy.optimize.minimize` iterates to the lowest-cost point that satisfies the constraints; a brute-force search over whole numbers (0–19) finds the best integer solution |

## C. Changing an input

The cost of a Type A unit was changed (Type B stays at 18):

| Cost of A | Continuous optimum | Cheapest whole servers (cost, A, B) |
|---|---|---|
| 12 (original) | A = 0, B = 5.88, cost 105.88 | (108, 0, 6) |
| 8 | A = 10, B = 0, cost 80.00 | (80, 10, 0) |
| 20 | A = 0, B = 5.88, cost 105.88 | (108, 0, 6) |

**Explanation:** what matters is the cost per unit of capacity: A = 12/100 = 0.120, B = 18/170 = 0.106. B is cheaper per capacity, so all the capacity is bought from B. When A drops to 8/100 = 0.08 it becomes the better buy and the whole solution flips to A. This is typical of linear problems: the optimum sits at a *corner* of the feasible region and jumps when a coefficient crosses a threshold.

## D. Meaning of the output

```
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution (cost, A, B, capacity): (108, 0, 6, 1020)
```

The cheapest way to supply the required 1000 capacity units is to use no Type A and 5.88 units of Type B (cost 105.88); the capacity constraint is exactly met (nothing wasted). Whole servers are usually required, so 6 Type B servers (capacity 1020, cost 108) is the real answer – slightly more expensive than the continuous optimum because of rounding up.

## E. Different real-world case – least-cost poultry feed

* **Assumptions:** 100 kg of feed is made from maize (30 KES/kg, 9 % protein, 3.4 Mcal/kg) and soybean meal (60 KES/kg, 44 % protein, 2.5 Mcal/kg). Requirements: x + y = 100 kg, at least 18 kg protein, at least 300 Mcal energy, x, y ≥ 0.
* **Output:**
  ```
  SLSQP : maize 74.29 kg, soybean 25.71 kg, cost 3,771.43 KES
  linprog check: maize 74.29 kg, soybean 25.71 kg, cost 3,771.43 KES
  protein supplied 18.00 kg (need 18, binding), energy 316.9 Mcal (need 300, slack)
  ```
* **Interpretation:** the cheapest mix is about 74 % maize and 26 % soybean meal. The protein requirement is the *binding* constraint (met exactly) – more soybean would be unnecessary cost – while the energy requirement has slack (317 vs 300 Mcal). `linprog`, a dedicated linear-programming solver, confirms the answer.
