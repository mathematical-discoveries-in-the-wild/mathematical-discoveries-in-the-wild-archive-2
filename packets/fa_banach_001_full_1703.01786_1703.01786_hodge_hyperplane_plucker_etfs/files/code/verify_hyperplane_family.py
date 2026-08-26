#!/usr/bin/env python3
"""Numerical stress check for the simplex/hyperplane Plucker construction.

This script is verification support only; the proof is in main.tex.
"""

from itertools import combinations

import numpy as np


def simplex_in_rt(t: int) -> np.ndarray:
    """Return a t by (t+1) matrix whose columns are a regular simplex."""
    d = np.eye(t + 1)[:, :t] - np.eye(t + 1)[:, [t]]
    basis, _ = np.linalg.qr(d)
    centered = np.eye(t + 1) - np.ones((t + 1, t + 1)) / (t + 1)
    ambient = np.sqrt((t + 1) / t) * centered
    return basis.T @ ambient


def plucker_vector_for_hyperplane(u: np.ndarray) -> np.ndarray:
    """Compute maximal minors of an orthonormal row basis of u^perp."""
    _, _, vh = np.linalg.svd(u.reshape(1, -1), full_matrices=True)
    a = vh[1:, :]
    coordinates = [np.linalg.det(a[:, cols]) for cols in combinations(range(len(u)), len(u) - 1)]
    return np.asarray(coordinates)


def check(t: int) -> dict[str, float]:
    u = simplex_in_rt(t)
    n = t + 1
    projections = [np.eye(t) - np.outer(u[:, j], u[:, j]) for j in range(n)]
    plucker = np.column_stack([plucker_vector_for_hyperplane(u[:, j]) for j in range(n)])

    gram_u = u.T @ u
    gram_p = plucker.T @ plucker
    off = ~np.eye(n, dtype=bool)

    return {
        "unit_vectors": float(np.max(np.abs(np.diag(gram_u) - 1))),
        "simplex_angles": float(np.max(np.abs(np.abs(gram_u[off]) - 1 / t))),
        "frame_tightness": float(np.linalg.norm(u @ u.T - (n / t) * np.eye(t))),
        "projection_idempotence": float(max(np.linalg.norm(q @ q - q) for q in projections)),
        "fusion_tightness": float(np.linalg.norm(sum(projections) - n * (t - 1) / t * np.eye(t))),
        "plucker_unit": float(np.max(np.abs(np.diag(gram_p) - 1))),
        "plucker_angles": float(np.max(np.abs(np.abs(gram_p[off]) - 1 / t))),
        "plucker_tightness": float(np.linalg.norm(plucker @ plucker.T - (n / t) * np.eye(t))),
    }


if __name__ == "__main__":
    worst = 0.0
    for dimension in range(3, 13):
        errors = check(dimension)
        local = max(errors.values())
        worst = max(worst, local)
        print(f"t={dimension:2d} max_error={local:.3e} {errors}")
    assert worst < 1e-10
    print(f"PASS: all tests, worst error {worst:.3e}")
