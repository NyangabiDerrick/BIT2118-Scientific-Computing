# Task 11 – Root Finding: Newton-Raphson and Secant Methods

Programs: [`code/Task_11_newton_secant.py`](../code/Task_11_newton_secant.py) · [`extensions/Task_11_ext_loan_apr.py`](../extensions/Task_11_ext_loan_apr.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Inputs | cash flows [−10000, 3000, 3500, 4000, 2500] (year 0 investment, years 1–4 inflows); Newton start r₀ = 0.10; secant starts 0.05 and 0.20; tolerance 10⁻¹² |
| Function | NPV(r) = Σ CFₜ / (1 + r)ᵗ ; derivative NPV′(r) = Σ −t·CFₜ / (1 + r)ᵗ⁺¹ |
| Operations | **Newton:** rₙ₊₁ = rₙ − NPV(rₙ)/NPV′(rₙ). **Secant:** same with the slope estimated from the last two points. The root of NPV is the **internal rate of return (IRR)**. |

## C. Changing an input

* **Cash flows** changed to [−10000, 4000, 4000, 4000, 4000]: IRR rises from 11.54 % to **21.86 %** (larger inflows → higher return).
* **Starting guess** (Newton, original flows): 0.01 → 5 iterations; 0.10 → 4; 0.50 → 8. All reach 11.5425 %, but a poor guess costs more iterations (and for some functions could fail to converge).

## D. Meaning of the output

```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method:  11.542461%
NPV at Newton solution:   0.000000
Newton iterations: 4, Secant iterations: 7
```

The investment earns **11.54 % per year**: discounting the inflows at that rate makes their present value exactly equal the 10,000 invested (NPV = 0). If the investor's cost of capital is below 11.54 % the project adds value; above it, it destroys value. Newton needed only 4 iterations (quadratic convergence, but needs the derivative); the secant method needed 7 without a derivative.

## E. Different real-world case – true cost (APR) of a loan with a fee

* **Assumptions:** a lender advertises KES 100,000, repayable as 12 monthly payments of KES 9,000, but deducts a KES 5,000 processing fee up front, so the borrower receives only KES 95,000. Find the monthly rate r such that Σ 9000/(1 + r)ᵗ = 95,000.
* **Output:**
  ```
  Newton monthly rate: 2.03051% (3 iterations)
  Secant monthly rate: 2.03051% (6 iterations)
  nominal annual rate (x12): 24.37%; effective annual rate: 27.28%
  total repaid 108,000 for 95,000 received -> extra cost 13,000
  ```
* **Interpretation:** the loan costs about 2.03 % per month, an effective **27.3 % per year** – higher than the nominal 24.4 % because of monthly compounding, and much higher than the headline price (8,000 interest on 100,000) suggests, because fees reduce the money actually received. Comparing loans by their IRR/APR makes them comparable.
