"""Numerical/symbolic sanity checks for the 3/2 corner-deletion constant.

The proof in main.tex is exact.  This script only checks the algebraic
sign-flip identity and the elementary 2x2 endpoint witness used in the
sharpness argument.
"""

from itertools import product

import numpy as np


def norm_infty_to_one(matrix: np.ndarray) -> float:
    """Exact for a real 2x2 matrix: the maximum occurs at a cube vertex."""
    return max(
        np.abs(matrix @ np.asarray(x, dtype=float)).sum()
        for x in product((-1.0, 1.0), repeat=2)
    )


def main() -> None:
    rng = np.random.default_rng(171108906)
    p = np.diag([1.0, 0.0, 1.0, 0.0])
    q = np.diag([1.0, 1.0, 0.0, 0.0])
    u = 2.0 * p - np.eye(4)
    v = 2.0 * q - np.eye(4)

    max_error = 0.0
    for _ in range(100):
        t = rng.normal(size=(4, 4))
        direct = t - p @ t @ q
        averaged = (3.0 * t - u @ t - t @ v - u @ t @ v) / 4.0
        max_error = max(max_error, np.max(np.abs(direct - averaged)))

    a = np.asarray([[1.0, -1.0], [-1.0, -1.0]])
    deleted = a.copy()
    deleted[0, 0] = 0.0
    norm_a = norm_infty_to_one(a)
    norm_deleted = norm_infty_to_one(deleted)

    assert max_error < 1e-12
    assert norm_a == 2.0
    assert norm_deleted == 3.0

    print(f"sign_flip_identity_max_error={max_error:.3e}")
    print(f"endpoint_norm_original={norm_a:.1f}")
    print(f"endpoint_norm_deleted={norm_deleted:.1f}")
    print(f"endpoint_ratio={norm_deleted / norm_a:.6f}")


if __name__ == "__main__":
    main()
