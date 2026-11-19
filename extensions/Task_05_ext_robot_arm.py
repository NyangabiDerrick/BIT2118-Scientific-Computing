"""Task 5 extension - robotics: forward kinematics of a 2-link planar arm.

C. Parameter change: rotation 45 -> 90 degrees and a different scale in the original program.
E. New case: homogeneous 3x3 matrices give the end-effector position of a robot arm.
"""
import numpy as np


def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])


# ---- C. Parameter change on the original square ------------------------------
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
for ang, sx, sy in ((45, 2.0, 1.5), (90, 3.0, 1.0)):
    M = rot(ang) @ np.diag([sx, sy])
    print(f"C. angle={ang} deg, scale=({sx},{sy}) -> det={np.linalg.det(M):.3f} (area factor)")
    print("   corner (1,1) ->", np.round(M @ square[2], 4))


# ---- E. New case: robot arm -----------------------------------------------------
def T(deg, length):
    """Rotate by `deg`, then translate `length` along the new x-axis (3x3 homogeneous)."""
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a), length * np.cos(a)],
                     [np.sin(a),  np.cos(a), length * np.sin(a)],
                     [0, 0, 1]])


L1, L2 = 1.0, 0.7        # link lengths in metres
print("\nE. New case: 2-link robot arm (L1=1.0 m, L2=0.7 m)")
for th1, th2 in ((30, 45), (30, -20), (90, 0)):
    end = T(th1, L1) @ T(th2, L2) @ np.array([0, 0, 1.0])
    print(f"  joint angles ({th1:>3}, {th2:>3}) deg -> end effector at x={end[0]:.3f} m, y={end[1]:.3f} m")
reach = L1 + L2
print(f"  maximum reach (arm straight) = {reach:.2f} m; "
      f"distance for (30,45): {np.hypot(*(T(30, L1) @ T(45, L2) @ [0, 0, 1])[:2]):.3f} m")
