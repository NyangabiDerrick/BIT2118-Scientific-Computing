# BIT 2118 – Scientific Computing: Group Work (Tasks 2–20)

Python programs, documentation and extensions for the BIT 2118 group work sheet.
For every task the repository contains:

| Instruction | Where it is answered |
|---|---|
| **A.** the task programme | [`code/`](code) – one script per task (Tasks 2–20) |
| **B.** inputs and mathematical operation | `docs/Task_XX_*.md`, section **B** |
| **C.** change a parameter and explain the effect | `docs/…`, section **C** (and the first half of each script in [`extensions/`](extensions)) |
| **D.** meaning of the output / graph interpretation | `docs/…`, section **D**, figures in [`figures/`](figures) |
| **E.** modified programme for a different real-world case (assumptions, input data, output, interpretation) | `docs/…`, section **E**, script in [`extensions/`](extensions) |

Raw console output of every script is saved in [`outputs/`](outputs).

## Task index

| Task | Topic | Original programme | Extension (new real-world case) | Documentation |
|---|---|---|---|---|
| 1 | Data Science Essentials with Python (self-paced prerequisite) | – | – | see note below |
| 2 | NumPy arrays | [code](code/Task_02_numpy_arrays.py) | [soil-moisture IoT](extensions/Task_02_ext_soil_moisture.py) | [doc](docs/Task_02_numpy_arrays.md) |
| 3 | Vectorization | [code](code/Task_03_vectorization.py) | [mobile-money fees](extensions/Task_03_ext_mobile_fees.py) | [doc](docs/Task_03_vectorization.md) |
| 4 | Floating-point errors | [code](code/Task_04_numerical_errors.py) | [banking sums](extensions/Task_04_ext_banking_sums.py) | [doc](docs/Task_04_numerical_errors.md) |
| 5 | Matrix algebra | [code](code/Task_05_matrix_algebra.py) | [robot arm](extensions/Task_05_ext_robot_arm.py) | [doc](docs/Task_05_matrix_algebra.md) |
| 6 | Linear systems | [code](code/Task_06_linear_systems.py) | [circuit mesh currents](extensions/Task_06_ext_circuit_mesh.py) | [doc](docs/Task_06_linear_systems.md) |
| 7 | Gaussian elimination / LU | [code](code/Task_07_gaussian_lu.py) | [Leontief economy](extensions/Task_07_ext_leontief_lu.py) | [doc](docs/Task_07_gaussian_lu.md) |
| 8 | Iterative methods | [code](code/Task_08_iterative_linear.py) | [heated rod](extensions/Task_08_ext_heated_rod.py) | [doc](docs/Task_08_iterative_linear.md) |
| 9 | Eigenvalues | [code](code/Task_09_eigenvalues.py) | [PageRank](extensions/Task_09_ext_pagerank.py) | [doc](docs/Task_09_eigenvalues.md) |
| 10 | Bisection / fixed point | [code](code/Task_10_bisection_fixed_point.py) | [break-even](extensions/Task_10_ext_break_even.py) | [doc](docs/Task_10_bisection_fixed_point.md) |
| 11 | Newton / secant | [code](code/Task_11_newton_secant.py) | [loan APR](extensions/Task_11_ext_loan_apr.py) | [doc](docs/Task_11_newton_secant.md) |
| 12 | Nonlinear equations | [code](code/Task_12_nonlinear_equations.py) | [chemical equilibrium](extensions/Task_12_ext_chemical_equilibrium.py) | [doc](docs/Task_12_nonlinear_equations.md) |
| 13 | Interpolation | [code](code/Task_13_interpolation.py) | [missing air-quality data](extensions/Task_13_ext_missing_data.py) | [doc](docs/Task_13_interpolation.md) |
| 14 | Curve fitting | [code](code/Task_14_curve_fitting.py) | [logistic growth](extensions/Task_14_ext_logistic_growth.py) | [doc](docs/Task_14_curve_fitting.md) |
| 15 | Numerical differentiation | [code](code/Task_15_numerical_differentiation.py) | [bus acceleration](extensions/Task_15_ext_acceleration.py) | [doc](docs/Task_15_numerical_differentiation.md) |
| 16 | Numerical integration | [code](code/Task_16_numerical_integration.py) | [borehole volume](extensions/Task_16_ext_borehole_volume.py) | [doc](docs/Task_16_numerical_integration.md) |
| 17 | ODEs – Euler | [code](code/Task_17_euler_ode.py) | [drug dosing](extensions/Task_17_ext_drug_dosing.py) | [doc](docs/Task_17_euler_ode.md) |
| 18 | ODEs – SciPy | [code](code/Task_18_scipy_ode.py) | [SIR epidemic](extensions/Task_18_ext_sir_epidemic.py) | [doc](docs/Task_18_scipy_ode.md) |
| 19 | Optimization | [code](code/Task_19_optimization.py) | [poultry feed mix](extensions/Task_19_ext_feed_mix.py) | [doc](docs/Task_19_optimization.md) |
| 20 | Monte Carlo | [code](code/Task_20_monte_carlo.py) | [project-schedule risk](extensions/Task_20_ext_project_risk.py) | [doc](docs/Task_20_monte_carlo.md) |

## Running the programmes

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python code/Task_02_numpy_arrays.py          # any single task
./run_all.sh                                 # everything: refreshes outputs/ and figures/
```

Requirements: Python 3.10+, NumPy ≥ 2.0 (Task 16 uses `np.trapezoid`), SciPy, Matplotlib.
Plots are saved to `figures/` (the scripts use the non-interactive `Agg` backend, so they also run on servers).

## Notes

* **Task 1** (Data Science Essentials with Python) is a self-paced online prerequisite course, not a programming task, so it has no code here.
* Timing results (Tasks 3 and 7) depend on the computer and change a little between runs; everything else is deterministic (fixed random seeds).
* Datasets in the extensions are small illustrative or synthetic data created for this exercise – they are **not** real measurements, and the tariffs, prices and rates are assumptions stated in each document.
* The group discussed the tasks together, but this repository is the individual submission required by the instructions.
