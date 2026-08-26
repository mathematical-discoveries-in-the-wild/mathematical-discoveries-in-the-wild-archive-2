#!/usr/bin/env python3
"""Finite checks for the 2N-1-site vv-RKBS group-l2 obstruction."""

from __future__ import annotations

import numpy as np


def construction(n: int):
    if n < 2:
        raise ValueError("n must be at least 2")

    cols: list[np.ndarray] = []
    directions: list[np.ndarray] = []

    e1 = np.zeros(n)
    e1[0] = 1.0
    e2 = np.zeros(n)
    e2[1] = 1.0
    cols.extend([e1, e2, (e1 + e2) / np.sqrt(2.0)])
    directions.extend(
        [
            np.array([1.0, 0.0]),
            np.array([0.0, 1.0]),
            np.array([1.0, 1.0]) / np.sqrt(2.0),
        ]
    )

    for k in range(2, n):
        ek = np.zeros(n)
        ek[k] = 1.0
        cols.extend([e1 + ek, e2 + ek])
        directions.extend([np.array([1.0, 0.0]), np.array([0.0, 1.0])])

    a = np.column_stack(cols)
    s = np.row_stack(directions)
    g = np.zeros((n, 2))
    g[0, 0] = 1.0
    g[1, 1] = 1.0
    return a, s, g


def objective(a: np.ndarray, c: np.ndarray, target: np.ndarray) -> float:
    n = a.shape[0]
    residual = a @ c - target
    return (np.linalg.norm(residual) ** 2) / (2.0 * n) + np.linalg.norm(
        c, axis=1
    ).sum() / n


def check_n(n: int, rng: np.random.Generator) -> None:
    a, s, g = construction(n)
    m = 2 * n - 1
    assert a.shape == (n, m)
    assert s.shape == (m, 2)
    assert np.linalg.matrix_rank(a, tol=1e-10) == n
    assert np.allclose(np.linalg.norm(s, axis=1), 1.0)
    assert np.allclose(g.T @ a, s.T)

    atoms = np.stack([np.outer(a[:, j], s[j]) for j in range(m)])
    atom_matrix = np.column_stack([atom.ravel() for atom in atoms])
    assert np.linalg.matrix_rank(atom_matrix, tol=1e-10) == m

    y0 = a @ s
    target = y0 + g
    residual = y0 - target
    kkt = (a.T @ residual + s) / n
    assert np.linalg.norm(kkt) < 1e-11

    certificate = float(np.sum(g * y0))
    assert abs(certificate - m) < 1e-11
    assert abs(np.linalg.norm(s, axis=1).sum() - m) < 1e-11

    # Complete the N rows of A to a square invertible feature matrix F.
    _, _, vh = np.linalg.svd(a, full_matrices=True)
    complement = vh[n:, :]
    f_matrix = np.row_stack([a, complement])
    assert f_matrix.shape == (m, m)
    assert np.linalg.matrix_rank(f_matrix, tol=1e-10) == m

    # The equality case in the certificate has a unique vector of ray scales.
    scales, residuals, rank, _ = np.linalg.lstsq(atom_matrix, y0.ravel(), rcond=None)
    assert rank == m
    assert residuals.size == 0 or residuals.max() < 1e-20
    assert np.allclose(scales, np.ones(m), atol=1e-10)

    # Random global and prediction-preserving perturbations are extra sanity checks.
    base_value = objective(a, s, target)
    for scale in (1e-4, 1e-2, 1.0, 10.0):
        for _ in range(100):
            c = s + scale * rng.normal(size=s.shape)
            assert objective(a, c, target) >= base_value - 1e-10

    null_basis = complement.T
    for _ in range(100):
        perturbation = null_basis @ rng.normal(size=(m - n, 2))
        assert np.linalg.norm(a @ perturbation) < 1e-10
        assert np.linalg.norm(s + perturbation, axis=1).sum() >= m - 1e-10


def main() -> None:
    rng = np.random.default_rng(250926371)
    for n in range(2, 13):
        check_n(n, rng)
    print("all checks passed for 2 <= N <= 12")


if __name__ == "__main__":
    main()
