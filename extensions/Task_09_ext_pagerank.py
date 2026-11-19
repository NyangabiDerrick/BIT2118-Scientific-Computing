"""Task 9 extension - PageRank of a five-page website.

C. Parameter change: add one link to the original 4-node network.
E. New case: ranking web pages by the dominant eigenvector of the Google matrix.
"""
import numpy as np


def centrality(adj):
    w, v = np.linalg.eig(adj)
    i = np.argmax(w.real)
    vec = np.abs(v[:, i].real)
    return w[i].real, vec / vec.sum()


# ---- C. Parameter change ---------------------------------------------------------------
A = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]], dtype=float)
A2 = A.copy()
A2[0, 3] = A2[3, 0] = 1.0  # add link A-D
for label, M in (("original", A), ("with extra link A-D", A2)):
    lam, c = centrality(M)
    print(f"C. {label:<20} dominant eigenvalue {lam:.4f}; importance A,B,C,D = {np.round(c, 4)}")

# ---- E. New case: PageRank --------------------------------------------------------------
pages = ["Home", "Blog", "Shop", "About", "Contact"]
# links[i][j] = 1 if page i links to page j
links = np.array([
    [0, 1, 1, 1, 1],   # Home  -> all
    [1, 0, 1, 0, 0],   # Blog  -> Home, Shop
    [1, 0, 0, 0, 1],   # Shop  -> Home, Contact
    [1, 0, 0, 0, 0],   # About -> Home
    [1, 0, 1, 0, 0],   # Contact -> Home, Shop
], dtype=float)
P = links / links.sum(axis=1, keepdims=True)     # row-stochastic transition matrix
d, n = 0.85, len(pages)                          # damping factor
G = d * P + (1 - d) / n                          # Google matrix
w, v = np.linalg.eig(G.T)                        # left eigenvector of G, eigenvalue 1
i = np.argmin(np.abs(w - 1))
rank = np.abs(v[:, i].real)
rank /= rank.sum()

# Cross-check with the power method (repeatedly multiply)
r = np.full(n, 1 / n)
for _ in range(100):
    r = G.T @ r
print("\nE. New case: PageRank of a 5-page website (damping 0.85)")
print(f"  eigenvalue closest to 1: {w[i].real:.6f}")
for name, s in sorted(zip(pages, rank), key=lambda t: -t[1]):
    print(f"  {name:<8} {s:.4f}")
print("  power-method difference from eig result:", f"{np.abs(r - rank).max():.2e}")
