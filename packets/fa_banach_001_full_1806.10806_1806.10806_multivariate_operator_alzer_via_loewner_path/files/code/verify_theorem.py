#!/usr/bin/env python3
"""Numerical sanity checks for the multivariate operator Alzer proof.

This checks consequences of the proof; it is not itself a proof.
"""

from __future__ import annotations

import numpy as np


def matrix_power(a: np.ndarray, exponent: float) -> np.ndarray:
    values, vectors = np.linalg.eigh((a + a.conj().T) / 2)
    return (vectors * values**exponent) @ vectors.conj().T


def weighted_geometric(a: np.ndarray, b: np.ndarray, alpha: float) -> np.ndarray:
    root = matrix_power(a, 0.5)
    invroot = matrix_power(a, -0.5)
    return root @ matrix_power(invroot @ b @ invroot, alpha) @ root


def recursive_geometric(matrices: list[np.ndarray]) -> np.ndarray:
    if len(matrices) == 1:
        return matrices[0]
    tail = recursive_geometric(matrices[1:])
    return weighted_geometric(matrices[0], tail, (len(matrices) - 1) / len(matrices))


def random_positive_half(
    rng: np.random.Generator, dimension: int, complex_entries: bool
) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension))
    if complex_entries:
        raw = raw + 1j * rng.normal(size=(dimension, dimension))
    unitary, _ = np.linalg.qr(raw)
    values = rng.uniform(0.01, 0.49, size=dimension)
    return unitary @ np.diag(values) @ unitary.conj().T


def alzer_defect(matrices: list[np.ndarray]) -> np.ndarray:
    identity = np.eye(matrices[0].shape[0])
    arithmetic = sum(matrices) / len(matrices)
    complements = [identity - a for a in matrices]
    return (
        arithmetic
        - recursive_geometric(matrices)
        - (identity - arithmetic - recursive_geometric(complements))
    )


def midpoint_derivative_error(matrices: list[np.ndarray]) -> float:
    identity = np.eye(matrices[0].shape[0])
    directions = [identity - 2 * a for a in matrices]
    step = 1e-5

    def path(t: float) -> np.ndarray:
        return recursive_geometric([a + t * q for a, q in zip(matrices, directions)])

    numerical = (path(0.5 + step) - path(0.5 - step)) / (2 * step)
    exact = sum(directions) / len(directions)
    return float(np.linalg.norm(numerical - exact, ord=2))


def main() -> None:
    lambdas = np.geomspace(1e-8, 1e8, 10000)
    # Algebraically equivalent form avoids cancellation for large lambda.
    kernel_gaps = 1 / (4 * (1 + lambdas) * (lambdas + 0.5) ** 2)
    assert np.min(kernel_gaps) > 0
    print(f"minimum scalar kernel gap: {np.min(kernel_gaps):.3e}")

    rng = np.random.default_rng(180610806)
    for dimension, count, complex_entries, trials in [
        (2, 3, False, 5000),
        (2, 4, True, 5000),
        (3, 3, True, 5000),
    ]:
        minimum = float("inf")
        maximum_derivative_error = 0.0
        for _ in range(trials):
            matrices = [
                random_positive_half(rng, dimension, complex_entries)
                for _ in range(count)
            ]
            minimum = min(minimum, float(np.linalg.eigvalsh(alzer_defect(matrices))[0]))
            maximum_derivative_error = max(
                maximum_derivative_error, midpoint_derivative_error(matrices)
            )
        assert minimum > -1e-8
        assert maximum_derivative_error < 1e-7
        print(
            f"dim={dimension} n={count} complex={complex_entries} trials={trials} "
            f"min_defect={minimum:.3e} max_midpoint_derivative_error="
            f"{maximum_derivative_error:.3e}"
        )


if __name__ == "__main__":
    main()
