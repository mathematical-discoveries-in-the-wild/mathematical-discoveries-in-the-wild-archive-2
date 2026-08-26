#!/usr/bin/env python3
"""Regression checks for the multiblock CAVI comparison-matrix theorem."""

from __future__ import annotations

import numpy as np


def gauss_seidel_matrix(a: np.ndarray) -> np.ndarray:
    lower = np.tril(a, k=-1)
    upper = np.triu(a, k=1)
    return np.linalg.solve(np.eye(a.shape[0]) - lower, upper)


def sequential_sweep(a: np.ndarray, old: np.ndarray) -> np.ndarray:
    new = np.zeros_like(old)
    for i in range(len(old)):
        new[i] = a[i, :i] @ new[:i] + a[i, i + 1 :] @ old[i + 1 :]
    return new


def main() -> None:
    rng = np.random.default_rng(260530253)
    matrix_cases = 25_000
    vector_cases = 0
    worst_weight_slack = float("inf")
    worst_recursion_error = 0.0

    for _ in range(matrix_cases):
        m = int(rng.integers(2, 10))
        a = rng.random((m, m))
        np.fill_diagonal(a, 0.0)
        # Small interactions give a broad collection of convergent, generally
        # nonsymmetric Gauss--Seidel comparison matrices.
        a *= float(rng.uniform(0.02, 0.42)) / max(1.0, np.max(a.sum(axis=1)))
        g = gauss_seidel_matrix(a)
        rho = float(np.max(np.abs(np.linalg.eigvals(g))))
        if not rho < 1.0:
            raise AssertionError((m, rho))

        q = (1.0 + rho) / 2.0
        w = np.linalg.solve(np.eye(m) - g / q, np.ones(m))
        slack = q * w - g @ w
        worst_weight_slack = min(worst_weight_slack, float(np.min(slack)))
        if np.min(w) <= 0.0 or np.min(slack) < -2e-12:
            raise AssertionError((rho, q, w, slack))

        for _ in range(4):
            old = rng.random(m)
            direct = sequential_sweep(a, old)
            matrix = g @ old
            err = float(np.max(np.abs(direct - matrix)))
            worst_recursion_error = max(worst_recursion_error, err)
            if err > 2e-12:
                raise AssertionError(err)

            old_norm = float(np.max(old / w))
            new_norm = float(np.max(direct / w))
            if new_norm > q * old_norm + 2e-12:
                raise AssertionError((new_norm, q * old_norm))
            vector_cases += 1

    # The two-block matrix must reduce to the product condition in the source.
    two_block_cases = 20_000
    worst_two_block_error = 0.0
    for _ in range(two_block_cases):
        a12, a21 = rng.lognormal(mean=-0.4, sigma=1.1, size=2)
        a = np.array([[0.0, a12], [a21, 0.0]])
        rho = float(np.max(np.abs(np.linalg.eigvals(gauss_seidel_matrix(a)))))
        err = abs(rho - a12 * a21)
        worst_two_block_error = max(worst_two_block_error, err)
        if err > 2e-12 * max(1.0, a12 * a21):
            raise AssertionError((rho, a12 * a21))

    print(f"matrix cases passed: {matrix_cases}/{matrix_cases}")
    print(f"error-vector cases passed: {vector_cases}/{vector_cases}")
    print(f"two-block reductions passed: {two_block_cases}/{two_block_cases}")
    print(f"minimum Perron-weight slack: {worst_weight_slack:.3e}")
    print(f"maximum recursion residual: {worst_recursion_error:.3e}")
    print(f"maximum two-block spectral-radius residual: {worst_two_block_error:.3e}")


if __name__ == "__main__":
    main()
