# Task 5 – Matrix Algebra and Matrix Operations

Programs: [`code/Task_05_matrix_algebra.py`](../code/Task_05_matrix_algebra.py) · [`extensions/Task_05_ext_robot_arm.py`](../extensions/Task_05_ext_robot_arm.py)

## B. Inputs and mathematical operations

| Item | Value |
|---|---|
| Inputs | unit-square corners (4 × 2 array); rotation angle 45°; scale factors 2.0 (x) and 1.5 (y) |
| Operations | rotation matrix R = [[cos θ, −sin θ],[sin θ, cos θ]]; scaling matrix S = diag(2, 1.5); combined T = R·S (matrix product `@`); every point transformed by `points @ T.T`; determinant det(T) |

Note that S is applied first, then R: T = R·S acting on a column vector.

## C. Changing an input

Rotation 45° → 90° and scale (2, 1.5) → (3, 1):

| Parameters | Corner (1, 1) maps to | det(T) |
|---|---|---|
| 45°, (2, 1.5) | (0.354, 2.475) | 3.000 |
| 90°, (3, 1) | (−1, 3) | 3.000 |

**Explanation:** the angle changes *where* the shape ends up (orientation), the scales change *how big* it is. The determinant equals the product of the scale factors (2 × 1.5 = 3 × 1 = 3) because a rotation has determinant 1, so both settings enlarge area 3 times even though the pictures differ.

## D. Meaning of the output

```
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.  0.]
  [ 1.41421356  1.41421356]
  [ 0.35355339  2.47487373]
  [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

The origin stays fixed (linear map). The corner (1, 0) is stretched to length 2 and rotated to 45°, giving (1.414, 1.414). The square becomes a rotated parallelogram. The determinant ≈ 3 means the area is multiplied by 3 (a unit square becomes area 3); it is non-zero, so the transformation is invertible (the original shape can be recovered). The tiny difference from exactly 3 is round-off error (Task 4).

## E. Different real-world case – robot-arm forward kinematics

* **Assumptions:** a planar arm with two links, L₁ = 1.0 m and L₂ = 0.7 m; joint angles in degrees; no joint limits.
* **Method:** each joint is a 3 × 3 homogeneous matrix T(θ, L) (rotate then translate along the link). The end-effector position is T(θ₁, L₁) · T(θ₂, L₂) · [0, 0, 1]ᵀ – the same matrix-multiplication idea as in graphics.
* **Output:**
  ```
  joint angles ( 30,  45) deg -> end effector at x=1.047 m, y=1.176 m
  joint angles ( 30, -20) deg -> end effector at x=1.555 m, y=0.622 m
  joint angles ( 90,   0) deg -> end effector at x=0.000 m, y=1.700 m
  maximum reach (arm straight) = 1.70 m
  ```
* **Interpretation:** with both joints at 90° and 0° the arm points straight up at its full reach of 1.70 m. Bending the second joint shortens the reach (1.575 m for 30°/45°). A robot controller multiplies such matrices thousands of times per second to know where the gripper is.
