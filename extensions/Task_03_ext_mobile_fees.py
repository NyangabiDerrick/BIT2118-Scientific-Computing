"""Task 3 extension - tiered transaction fees for one million payments.

C. Parameter change: array size N = 100,000 instead of 1,000,000.
E. New case: mobile-money fee calculation, loop vs np.select.
"""
import timeit
import numpy as np

# ---- C. Parameter change: size of the data ----------------------------------
for n in (100_000, 1_000_000):
    rng = np.random.default_rng(42)
    ms = rng.uniform(5, 250, n)
    loop = timeit.timeit(lambda: [(v / 1000.0) ** 2 for v in ms], number=1)
    vec = timeit.timeit(lambda: (ms / 1000.0) ** 2, number=3) / 3
    print(f"C. N={n:>9,}: loop {loop:.4f}s, vectorized {vec:.5f}s, speed-up {loop/vec:.0f}x")

# ---- E. New case: tiered fees ----------------------------------------------
# Assumptions (illustrative tariff, KES): amount <=100 -> 0; <=1,000 -> 11;
# <=10,000 -> 28; above -> 0.5% of the amount, capped at 200.
rng = np.random.default_rng(7)
amount = rng.lognormal(mean=6.0, sigma=1.2, size=1_000_000)  # skewed amounts


def fee_loop(values):
    out = []
    for a in values:
        if a <= 100:
            out.append(0.0)
        elif a <= 1000:
            out.append(11.0)
        elif a <= 10000:
            out.append(28.0)
        else:
            out.append(min(0.005 * a, 200.0))
    return out


def fee_vec(a):
    return np.select(
        [a <= 100, a <= 1000, a <= 10000],
        [0.0, 11.0, 28.0],
        default=np.minimum(0.005 * a, 200.0))


t_loop = timeit.timeit(lambda: fee_loop(amount), number=1)
t_vec = timeit.timeit(lambda: fee_vec(amount), number=3) / 3
fees = fee_vec(amount)
assert np.allclose(fees, fee_loop(amount))  # both methods agree
print("\nE. New case: mobile-money tiered fees on 1,000,000 payments")
print(f"  total value moved : {amount.sum():,.0f} KES")
print(f"  total fees earned : {fees.sum():,.0f} KES ({fees.sum()/amount.sum():.3%} of value)")
print(f"  loop {t_loop:.3f}s vs vectorized {t_vec:.4f}s -> {t_loop/t_vec:.0f}x faster")
