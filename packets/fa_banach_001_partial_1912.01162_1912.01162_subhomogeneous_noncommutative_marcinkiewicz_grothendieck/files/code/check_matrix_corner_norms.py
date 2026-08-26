#!/usr/bin/env python3
"""Finite atomic checks for the matrix-corner norm inequalities."""

from __future__ import annotations

import numpy as np


def marcinkiewicz_norm(values: np.ndarray, exponent: float = 0.6) -> float:
    """Discrete M_psi norm with psi(k)=k**exponent."""
    decreasing = np.sort(np.abs(values).ravel())[::-1]
    partial = np.cumsum(decreasing)
    indices = np.arange(1, decreasing.size + 1, dtype=float)
    return float(np.max(partial / indices**exponent, initial=0.0))


def operator_marcinkiewicz_norm(field: np.ndarray, exponent: float = 0.6) -> float:
    singular_values = np.concatenate([np.linalg.svd(matrix, compute_uv=False) for matrix in field])
    return marcinkiewicz_norm(singular_values, exponent)


def main() -> None:
    rng = np.random.default_rng(191201162)
    for atoms, degree in ((3, 2), (5, 3), (4, 4)):
        field = rng.normal(size=(atoms, degree, degree)) + 1j * rng.normal(
            size=(atoms, degree, degree)
        )
        whole = operator_marcinkiewicz_norm(field)
        corner_norms = [
            marcinkiewicz_norm(field[:, i, j])
            for i in range(degree)
            for j in range(degree)
        ]
        assert max(corner_norms) <= whole + 1e-10
        assert whole <= sum(corner_norms) + 1e-10

        rebuilt = np.zeros_like(field)
        for i in range(degree):
            for j in range(degree):
                rebuilt[:, i, j] = field[:, i, j]
        assert np.allclose(rebuilt, field)
        print(
            f"atoms={atoms}, degree={degree}: "
            f"max_corner={max(corner_norms):.6f} <= whole={whole:.6f} "
            f"<= corner_sum={sum(corner_norms):.6f}"
        )


if __name__ == "__main__":
    main()

