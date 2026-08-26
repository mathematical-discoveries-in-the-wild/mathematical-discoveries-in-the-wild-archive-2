#!/usr/bin/env python3
"""Finite-dimensional sanity checks for the active-core spectral argument.

The proof packet is infinite-dimensional.  This script only checks its matrix
analogue: larger secant weights dominate a connected core on the normalized
subspace, and I-(eta/epsilon)A is a strict contraction.
"""

from __future__ import annotations

import numpy as np


def normalized_basis(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    """Orthonormal basis after converting the weighted norm to Euclidean."""
    normal = np.concatenate((np.sqrt(p), -np.sqrt(q)))
    _, _, vh = np.linalg.svd(normal.reshape(1, -1), full_matrices=True)
    return vh[1:].T


def energy_matrix(p: np.ndarray, q: np.ndarray, weights: np.ndarray) -> np.ndarray:
    row_mass = weights @ q
    col_mass = weights.T @ p
    cross = np.sqrt(p[:, None] * q[None, :]) * weights
    return np.block(
        [
            [np.diag(row_mass), cross],
            [cross.T, np.diag(col_mass)],
        ]
    )


def connected_core(rows: int, cols: int) -> np.ndarray:
    core = np.zeros((rows, cols), dtype=float)
    core[:, 0] = 1.0
    core[0, :] = 1.0
    return core


def main() -> None:
    rng = np.random.default_rng(250908547)
    configurations = 0
    weight_samples = 0

    for rows in range(2, 8):
        for cols in range(2, 8):
            for _ in range(6):
                p = rng.random(rows)
                p /= p.sum()
                q = rng.random(cols)
                q /= q.sum()
                basis = normalized_basis(p, q)
                core = connected_core(rows, cols)
                core_reduced = basis.T @ energy_matrix(p, q, core) @ basis
                kappa = np.linalg.eigvalsh(core_reduced)[0]
                assert kappa > 1.0e-10

                step_ratio = rng.uniform(0.02, 0.98)
                contraction_bound = max(abs(1 - 2 * step_ratio), abs(1 - step_ratio * kappa))
                assert contraction_bound < 1

                for _ in range(20):
                    weights = np.where(core > 0, 1.0, rng.random((rows, cols)))
                    reduced = basis.T @ energy_matrix(p, q, weights) @ basis
                    eigenvalues = np.linalg.eigvalsh(reduced)
                    assert eigenvalues[0] + 1.0e-10 >= kappa
                    assert eigenvalues[-1] <= 2.0 + 1.0e-10
                    contraction = np.max(np.abs(1 - step_ratio * eigenvalues))
                    assert contraction <= contraction_bound + 1.0e-10
                    assert contraction < 1
                    weight_samples += 1

                configurations += 1

    print(f"configurations={configurations}")
    print(f"weight_samples={weight_samples}")
    print("status=PASS")


if __name__ == "__main__":
    main()

