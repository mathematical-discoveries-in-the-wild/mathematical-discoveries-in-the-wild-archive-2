#!/usr/bin/env python3
"""Random search for a 2x2 counterexample to the open operator Alzer claim."""

from __future__ import annotations

import numpy as np


def matrix_power(a: np.ndarray, exponent: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(a)
    return (vectors * values**exponent) @ vectors.conj().T


def geometric_mean(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    root = matrix_power(a, 0.5)
    invroot = matrix_power(a, -0.5)
    return root @ matrix_power(invroot @ b @ invroot, 0.5) @ root


def power_mean_step(a: np.ndarray, b: np.ndarray, m: int) -> np.ndarray:
    root = matrix_power(b, 0.5)
    invroot = matrix_power(b, -0.5)
    return root @ matrix_power(invroot @ a @ invroot, 1.0 / m) @ root


def recursive_geometric_mean(matrices: list[np.ndarray]) -> np.ndarray:
    if len(matrices) == 2:
        return geometric_mean(matrices[0], matrices[1])
    return power_mean_step(matrices[0], recursive_geometric_mean(matrices[1:]), len(matrices))


def random_positive_contraction(rng: np.random.Generator, dimension: int) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    rotation, _ = np.linalg.qr(raw)
    values = rng.uniform(0.01, 0.49, size=dimension)
    return rotation @ np.diag(values) @ rotation.conj().T


def defect(matrices: list[np.ndarray]) -> np.ndarray:
    identity = np.eye(matrices[0].shape[0])
    original = sum(matrices) / len(matrices) - recursive_geometric_mean(matrices)
    complements = [identity - matrix for matrix in matrices]
    complement = sum(complements) / len(complements) - recursive_geometric_mean(complements)
    return original - complement


def main() -> None:
    rng = np.random.default_rng(180610806)
    best = None
    dimension = 3
    matrix_count = 3
    for trial in range(200_000):
        matrices = [random_positive_contraction(rng, dimension) for _ in range(matrix_count)]
        d = defect(matrices)
        minimum = float(np.linalg.eigvalsh(d)[0])
        if best is None or minimum < best[0]:
            best = (minimum, trial, matrices, d)
        if minimum < -1e-4:
            break
    assert best is not None
    minimum, trial, matrices, d = best
    print(f"trial={trial} min_eigenvalue={minimum:.16e}")
    for index, matrix in enumerate(matrices, start=1):
        print(f"A{index}=")
        print(matrix)
    print("RHS_minus_LHS=")
    print(d)
    print("eigenvalues=", np.linalg.eigvalsh(d))


if __name__ == "__main__":
    main()
