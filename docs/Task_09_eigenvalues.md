# Task 9 – Eigenvalues and Eigenvectors

Programs: [`code/Task_09_eigenvalues.py`](../code/Task_09_eigenvalues.py) · [`extensions/Task_09_ext_pagerank.py`](../extensions/Task_09_ext_pagerank.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Input | symmetric 4 × 4 adjacency matrix for nodes A, B, C, D (1 = link): A–B, A–C, B–C, B–D, C–D |
| Operations | `np.linalg.eig(A)` solves A v = λ v; take the largest real eigenvalue (dominant), the absolute value of its eigenvector, normalise so the entries sum to 1 (importance share); verify ‖A v − λ v‖ ≈ 0 |

## C. Changing an input

A link A–D was added (making every node connected to every other node):

| Network | Dominant eigenvalue | Importance A, B, C, D |
|---|---|---|
| original | 2.5616 | 0.2192, 0.2808, 0.2808, 0.2192 |
| with extra link A–D | 3.0000 | 0.25, 0.25, 0.25, 0.25 |

**Explanation:** more connections raise the dominant eigenvalue (the "growth rate" of influence). With the extra link the network is completely symmetric, so no node is more important than another.

## D. Meaning of the output

```
Dominant eigenvalue: 2.5615528128088276
A: 0.2192   B: 0.2808   C: 0.2808   D: 0.2192
Verification error: 2.6e-15
```

The dominant eigenvalue 2.5616 = (1 + √17)/2 is the factor by which influence is amplified when it is passed along links. Nodes B and C (3 connections each) are more central (28.1 % each) than A and D (2 connections, 21.9 %). The verification error ~10⁻¹⁵ confirms A v = λ v. Eigenvector centrality counts not only *how many* neighbours a node has but also *how important* those neighbours are.

## E. Different real-world case – PageRank for a 5-page website

* **Assumptions:** pages Home, Blog, Shop, About, Contact; a visitor follows one outgoing link at random with probability 0.85 and jumps to a random page with probability 0.15 (damping 0.85). The rank vector is the eigenvector of the Google matrix G for eigenvalue 1.
* **Input data:** Home links to all pages; Blog → Home, Shop; Shop → Home, Contact; About → Home; Contact → Home, Shop.
* **Output:**
  ```
  eigenvalue closest to 1: 1.000000
  Home 0.3505   Shop 0.2359   Contact 0.2047   Blog 0.1045   About 0.1045
  power-method difference from eig result: 7.2e-16
  ```
* **Interpretation:** Home is the most important page (35 %) because every page links to it. Shop ranks second because three pages point to it. Blog and About receive links only from Home, so they rank lowest. The power method (repeated multiplication) reaches the same answer – this is how PageRank is computed for huge webs where `eig` would be too expensive.
