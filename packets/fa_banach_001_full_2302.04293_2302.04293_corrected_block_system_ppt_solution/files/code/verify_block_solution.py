"""Deterministic checks for the corrected block-system theorem."""

from __future__ import annotations

import numpy as np


def nullspace(matrix: np.ndarray, tolerance: float = 1e-10) -> np.ndarray:
    _, singular, vh = np.linalg.svd(matrix)
    rank = int(np.sum(singular > tolerance))
    return vh[rank:].conj().T


def check() -> None:
    rng = np.random.default_rng(230204293)

    # Minimal counterexample to the source proposition.
    zero = np.zeros((2, 2))
    assert np.allclose(zero @ np.array([0.0, 7.0]), np.zeros(2))
    assert not np.allclose(zero @ np.array([0.0, 7.0]), np.array([0.0, 1.0]))

    for _ in range(200):
        n1, n2 = 3, 4
        a11 = rng.normal(size=(n1, n1))
        a12 = rng.normal(size=(n1, n2))
        a21 = rng.normal(size=(n2, n1))
        # Force singularity and a nontrivial kernel.
        left = rng.normal(size=(n2, 2))
        right = rng.normal(size=(2, n2))
        a22 = left @ right
        pinv = np.linalg.pinv(a22)
        projection = a22 @ pinv
        kernel = nullspace(a22)

        x1 = rng.normal(size=n1)
        seed = rng.normal(size=n2)
        y2 = a21 @ x1 + a22 @ seed
        b = y2 - a21 @ x1
        assert np.linalg.norm((np.eye(n2) - projection) @ b) < 2e-9

        z = kernel @ rng.normal(size=kernel.shape[1])
        x2 = pinv @ b + z
        y1 = a11 @ x1 + a12 @ pinv @ b + a12 @ z
        full = np.block([[a11, a12], [a21, a22]])
        assert np.linalg.norm(full @ np.concatenate([x1, x2])
                              - np.concatenate([y1, y2])) < 2e-8

        # Add a nonzero component perpendicular to ran(A22).
        perp = (np.eye(n2) - projection) @ rng.normal(size=n2)
        if np.linalg.norm(perp) > 1e-7:
            bad_y2 = y2 + perp
            bad_b = bad_y2 - a21 @ x1
            assert np.linalg.norm((np.eye(n2) - projection) @ bad_b) > 1e-7
            least_x2 = pinv @ bad_b
            least_y1 = a11 @ x1 + a12 @ least_x2
            actual = full @ np.concatenate([x1, least_x2])
            projected_lower = a21 @ x1 + projection @ bad_b
            assert np.linalg.norm(actual
                                  - np.concatenate([least_y1, projected_lower])) < 2e-8
            assert np.linalg.norm(actual[n1:] - bad_y2) > 1e-7

    print("verified the zero-matrix counterexample")
    print("verified 200 compatible singular block systems")
    print("verified incompatible-data and projected-system identities")


if __name__ == "__main__":
    check()

