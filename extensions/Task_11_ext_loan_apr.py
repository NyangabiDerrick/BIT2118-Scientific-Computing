"""Task 11 extension - true cost (APR) of a loan using Newton and secant.

C. Parameter change: different cash flows and starting guesses for the IRR.
E. New case: loan with an upfront fee; find the real monthly interest rate.
"""
from scipy.optimize import root_scalar


# ---- C. Parameter change ----------------------------------------------------------------------
def make(cash_flows):
    npv = lambda r: sum(cf / (1 + r) ** t for t, cf in enumerate(cash_flows))
    dnpv = lambda r: sum(-t * cf / (1 + r) ** (t + 1) for t, cf in enumerate(cash_flows))
    return npv, dnpv


for flows in ([-10000, 3000, 3500, 4000, 2500], [-10000, 4000, 4000, 4000, 4000]):
    npv, dnpv = make(flows)
    nr = root_scalar(npv, fprime=dnpv, x0=0.10, method="newton", xtol=1e-12)
    print(f"C. flows {flows}: IRR = {nr.root:.4%} in {nr.iterations} Newton iterations")
npv, dnpv = make([-10000, 3000, 3500, 4000, 2500])
for x0 in (0.01, 0.10, 0.50):
    r = root_scalar(npv, fprime=dnpv, x0=x0, method="newton", xtol=1e-12)
    print(f"   start {x0:.2f}: {r.root:.4%} after {r.iterations} iterations")

# ---- E. New case: loan APR ------------------------------------------------------------------------
# A lender advertises KES 100,000, repayable as 12 x KES 9,000, but takes a KES 5,000
# processing fee upfront, so the borrower only receives 95,000.
received, payment, months = 95_000.0, 9_000.0, 12


def f(r):                      # present value of repayments minus money actually received
    return sum(payment / (1 + r) ** t for t in range(1, months + 1)) - received


def df(r):
    return sum(-t * payment / (1 + r) ** (t + 1) for t in range(1, months + 1))


nwt = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-12)
sec = root_scalar(f, x0=0.01, x1=0.05, method="secant", xtol=1e-12)
monthly = nwt.root
print("\nE. New case: loan with processing fee")
print(f"  Newton monthly rate: {monthly:.5%} ({nwt.iterations} iterations)")
print(f"  Secant monthly rate: {sec.root:.5%} ({sec.iterations} iterations)")
print(f"  nominal annual rate (x12): {12 * monthly:.2%}; effective annual rate: {(1 + monthly) ** 12 - 1:.2%}")
print(f"  total repaid {payment * months:,.0f} for {received:,.0f} received -> extra cost {payment * months - received:,.0f}")
