"""Task 6 extension - electrical circuit mesh currents (Kirchhoff's voltage law).

C. Parameter change: change the totals b of the server problem.
E. New case: three-loop resistor network, solve for mesh currents.
"""
import numpy as np

# ---- C. Parameter change on the server problem -------------------------------
A = np.array([[4.0, 2.0], [8.0, 12.0]])
for b in ([20.0, 72.0], [26.0, 80.0], [20.0, 40.0]):
    x = np.linalg.solve(A, np.array(b))
    print(f"C. totals {b} -> Type A = {x[0]:.2f}, Type B = {x[1]:.2f}"
          + ("   (negative -> impossible scenario)" if (x < 0).any() else ""))
print("   det(A) =", round(np.linalg.det(A), 3), "(non-zero, so a unique solution exists)")

# ---- E. New case: circuit -------------------------------------------------------
# Three meshes sharing resistors. Unknowns: mesh currents I1, I2, I3 (amperes).
#  Mesh 1: 12V source, 4 ohm own, 2 ohm shared with mesh 2
#  Mesh 2: 6 ohm own, 2 ohm shared with 1, 3 ohm shared with 3
#  Mesh 3: 5 ohm own, 3 ohm shared with 2, 8V source opposing
R = np.array([
    [4 + 2, -2,     0],
    [-2,    2 + 6 + 3, -3],
    [0,     -3,     3 + 5],
], dtype=float)
V = np.array([12.0, 0.0, -8.0])
I = np.linalg.solve(R, V)
print("\nE. New case: 3-mesh resistor circuit")
print("  mesh currents I1, I2, I3 (A):", np.round(I, 4))
print("  residual norm:", np.linalg.norm(V - R @ I))
print("  current through the 2-ohm shared resistor (I1-I2): %.4f A" % (I[0] - I[1]))
print("  power in 2-ohm resistor: %.4f W" % (2 * (I[0] - I[1]) ** 2))
print("  condition number of R:", round(np.linalg.cond(R), 2), "(small -> well-conditioned)")
