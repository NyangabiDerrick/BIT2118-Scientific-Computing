# Task 6 – Solution of Systems of Linear Equations

Programs: [`code/Task_06_linear_systems.py`](../code/Task_06_linear_systems.py) · [`extensions/Task_06_ext_circuit_mesh.py`](../extensions/Task_06_ext_circuit_mesh.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Inputs | A = [[4, 2],[8, 12]] (CPU and memory per server type), b = [20, 72] (total CPU, total GB) |
| Operations | solve **A x = b** with `np.linalg.solve` (LU with pivoting); verify with `A @ x`; residual r = b − A x and its norm |

Equations: 4x + 2y = 20 (CPU) and 8x + 12y = 72 (memory).

## C. Changing an input

| Totals b | Type A | Type B | Comment |
|---|---|---|---|
| [20, 72] | 3 | 4 | original |
| [26, 80] | 4.75 | 3.5 | not whole numbers → the observed totals are inconsistent with whole servers |
| [20, 40] | 5 | 0 | only Type A servers are running |

**Explanation:** det(A) = 4·12 − 2·8 = 32 ≠ 0, so every b has exactly one solution. The solution changes smoothly with b, but the *meaning* depends on the real-world constraint that counts must be non-negative integers.

## D. Meaning of the output

```
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

There are 3 Type A and 4 Type B servers: CPU 3·4 + 4·2 = 20 and memory 3·8 + 4·12 = 72, exactly the observed totals. A residual of zero (or ~10⁻¹⁵ in general) proves that the computed x really satisfies the equations.

## E. Different real-world case – electrical mesh currents

* **Assumptions:** three meshes with resistors; shared resistors couple the meshes; mesh 1 has a 12 V source, mesh 3 an opposing 8 V source; ideal sources and resistors.
* **Input data:** resistance matrix R = [[6, −2, 0],[−2, 11, −3],[0, −3, 8]] Ω, voltage vector V = [12, 0, −8] V (Kirchhoff's voltage law R·I = V).
* **Output:**
  ```
  mesh currents I1, I2, I3 (A): [ 2.0362  0.1086 -0.9593]
  residual norm: 4.4e-16
  current through the 2-ohm shared resistor (I1-I2): 1.9276 A
  power in 2-ohm resistor: 7.4313 W
  condition number of R: 2.76
  ```
* **Interpretation:** mesh 3 current is negative, meaning it flows opposite to the assumed (clockwise) direction – the 8 V source is pushing against the circuit. The small condition number (2.76) means the system is well-conditioned: small errors in resistor values cause only small errors in the currents.
