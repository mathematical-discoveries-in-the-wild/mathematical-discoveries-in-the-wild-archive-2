#!/usr/bin/env python3
"""Numerically verify the finite matrices used in the proof packet."""

from __future__ import annotations

import numpy as np


def sylvester(order: int) -> np.ndarray:
    h = np.array([[1.0]])
    while h.shape[0] < order:
        h = np.block([[h, h], [h, -h]])
    if h.shape != (order, order):
        raise ValueError("order must be a power of two")
    return h


def mixed_norm(matrix: np.ndarray, p: float) -> float:
    """Mixed norm for the equal-block step kernel represented by matrix."""
    m = matrix.shape[0]
    q = p / (p - 1.0)
    inner = np.mean(np.abs(matrix) ** q, axis=0)
    return float(np.mean(inner ** (p / q)) ** (1.0 / p))


def schatten_step_norm(matrix: np.ndarray, p: float) -> float:
    """S_p norm of the step-kernel operator (whose matrix is A/m)."""
    m = matrix.shape[0]
    singular = np.linalg.svd(matrix / m, compute_uv=False)
    return float(np.sum(singular**p) ** (1.0 / p))


def special_matrix(c: float) -> np.ndarray:
    h = np.array([0.0, 1.0 / c, 1.0, 1.0 + 1.0 / c])
    weights = np.ones((4, 4))
    np.fill_diagonal(weights, 0.0)
    weights[0, 1] = weights[1, 0] = c
    weights[2, 3] = weights[3, 2] = c
    return (h[None, :] - h[:, None]) * weights


def main() -> None:
    limit = np.triu(np.ones((4, 4)), 1)
    limit = limit - limit.T
    expected = np.array(
        [np.sqrt(2.0) + 1.0] * 2 + [np.sqrt(2.0) - 1.0] * 2
    )
    actual = np.sort(np.linalg.svd(limit, compute_uv=False))[::-1]
    print("limit singular-value error", np.max(np.abs(actual - expected)))

    for p in (1.1, 1.25, 1.5, 1.75, 1.9, 1.99):
        ratio_limit = schatten_step_norm(limit, p) / mixed_norm(limit, p)
        ratio_finite = schatten_step_norm(special_matrix(256.0), p) / mixed_norm(
            special_matrix(256.0), p
        )
        print(
            f"p={p:.2f} limit_ratio={ratio_limit:.12f} "
            f"c=256_ratio={ratio_finite:.12f}"
        )

    for order in (2, 4, 8, 16, 32):
        u = sylvester(order) / np.sqrt(order)
        zero = np.zeros_like(u)
        a = np.block([[zero, u], [-u.T, zero]])
        orthogonality_error = np.max(np.abs(a.T @ a - np.eye(2 * order)))
        p = 1.5
        ratio = schatten_step_norm(a, p) / mixed_norm(a, p)
        expected_ratio = order ** (1.0 / p - 0.5)
        print(
            f"Hadamard n={order:2d} orthogonality_error={orthogonality_error:.2e} "
            f"ratio_error={abs(ratio-expected_ratio):.2e}"
        )


if __name__ == "__main__":
    main()

