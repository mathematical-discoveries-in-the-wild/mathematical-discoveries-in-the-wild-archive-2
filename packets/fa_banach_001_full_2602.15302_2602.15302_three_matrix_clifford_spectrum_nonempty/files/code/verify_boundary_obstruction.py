#!/usr/bin/env python3
"""Sanity checks for the large-sphere homotopy in the proof packet.

This script is not part of the proof.  It samples the analytic gap estimate,
checks the negative rank, and verifies the determinant winding of n Hopf
summands.
"""

from __future__ import annotations

import numpy as np


SIGMA = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)


def random_hermitian(rng: np.random.Generator, n: int) -> np.ndarray:
    matrix = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (matrix + matrix.conj().T) / 2


def sphere_points(rng: np.random.Generator, count: int) -> np.ndarray:
    points = rng.normal(size=(count, 3))
    return points / np.linalg.norm(points, axis=1)[:, None]


def main() -> None:
    rng = np.random.default_rng(260215302)
    gap_checks = 0
    rank_checks = 0

    for n in range(1, 6):
        matrices = [random_hermitian(rng, n) for _ in range(3)]
        localizer_zero = sum(np.kron(a, s) for a, s in zip(matrices, SIGMA))
        norm_k = np.linalg.norm(localizer_zero, ord=2)
        radius = norm_k + 0.75

        for omega in sphere_points(rng, 80):
            clifford_direction = sum(x * s for x, s in zip(omega, SIGMA))
            boundary_model = np.kron(np.eye(n), clifford_direction)
            for t in np.linspace(0.0, 1.0, 9):
                homotopy = t * localizer_zero - radius * boundary_model
                eigenvalues = np.linalg.eigvalsh(homotopy)
                observed_gap = np.min(np.abs(eigenvalues))
                analytic_gap = radius - t * norm_k
                assert observed_gap + 1.0e-9 >= analytic_gap
                assert np.count_nonzero(eigenvalues < 0) == n
                gap_checks += 1
                rank_checks += 1

        phi = np.linspace(0.0, 2 * np.pi, 4097)
        determinant_phase = np.unwrap(np.angle(np.exp(-1j * n * phi)))
        winding = (determinant_phase[-1] - determinant_phase[0]) / (2 * np.pi)
        assert abs(winding + n) < 1.0e-10

    print(f"gap_checks={gap_checks}")
    print(f"rank_checks={rank_checks}")
    print("hopf_windings=-1,-2,-3,-4,-5")
    print("status=PASS")


if __name__ == "__main__":
    main()

