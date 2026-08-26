#!/usr/bin/env python3
"""Independent finite checks for the three-Rademacher concavity packet.

The proof in main.tex is symbolic.  This script only checks the formulas and
searches for a numerical contradiction over a fixed reproducible sample.
"""

import itertools
import numpy as np


def laplacian(coefficients, p):
    r = np.asarray(coefficients, dtype=float)
    signs = np.asarray(list(itertools.product((-1.0, 1.0), repeat=len(r))))
    sums = signs @ r
    correlations = (signs.T * np.abs(sums) ** (p - 2.0)) @ signs / len(signs)
    weights = np.outer(r, r) * correlations
    np.fill_diagonal(weights, 0.0)
    matrix = -weights.copy()
    np.fill_diagonal(matrix, weights.sum(axis=1))
    return matrix, weights


def closed_form_weights(r, u, v, p):
    q = p - 2.0
    U = (r + u + v) ** q
    V = (r + u - v) ** q
    W = (r - u + v) ** q
    X = abs(r - u - v) ** q
    P = U + V - W - X
    Q = U - V + W - X
    R = U - V - W + X
    return np.array([r * u * P, r * v * Q, u * v * R]) / 4.0


def main():
    rng = np.random.default_rng(210805785)
    worst_eigenvalue = 0.0
    worst_formula_error = 0.0
    tested = 0
    for p in (2.01, 2.05, 2.1, 2.25, 2.5, 2.75, 2.9, 2.99):
        for _ in range(25_000):
            r, u, v = sorted(np.exp(rng.uniform(-6.0, 6.0, 3)), reverse=True)
            matrix, weights = laplacian((r, u, v), p)
            eigenvalues = np.linalg.eigvalsh(matrix)
            scale = max(1.0, np.linalg.norm(matrix, ord=2))
            worst_eigenvalue = min(worst_eigenvalue, eigenvalues[0] / scale)
            direct = np.array([weights[0, 1], weights[0, 2], weights[1, 2]])
            formula = closed_form_weights(r, u, v, p)
            error = np.max(np.abs(direct - formula)) / max(1.0, np.max(np.abs(direct)))
            worst_formula_error = max(worst_formula_error, error)
            if eigenvalues[0] < -1e-9 * scale:
                raise AssertionError((p, (r, u, v), eigenvalues, weights))
            tested += 1
    print(f"tested={tested}")
    print(f"worst_scaled_min_eigenvalue={worst_eigenvalue:.3e}")
    print(f"worst_relative_formula_error={worst_formula_error:.3e}")
    print("result=no contradiction")


if __name__ == "__main__":
    main()
