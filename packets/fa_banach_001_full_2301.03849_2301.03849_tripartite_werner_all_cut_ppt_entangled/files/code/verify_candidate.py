#!/usr/bin/env python3
"""Exact and direct-matrix checks for the all-cut Werner-state example."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import sqrt

import numpy as np


RP, RM, R1, R2, R3 = F(3, 4), F(1, 32), F(0), F(0), F(3, 16)
R0 = 1 - RP - RM


def exact_checks() -> None:
    assert R0 == F(7, 32)
    assert R1 * R1 + R2 * R2 + R3 * R3 == F(36, 1024)
    assert R0 * R0 == F(49, 1024)
    assert R3 * R3 < R0 * R0

    linear_1 = 1 + R1 - RP - RM
    linear_2 = 1 - R1 - 5 * RM - RP
    linear_3 = -1 - R1 + RM + 5 * RP
    transverse = R2 * R2 + R3 * R3
    ppt_radius_1 = linear_2 * linear_3 / 3
    ppt_radius_2 = (1 - R1 - RM - RP) * (1 + R1 - RM - RP)
    assert (RM, linear_1, linear_2, linear_3) == (
        F(1, 32), F(7, 32), F(3, 32), F(89, 32)
    )
    assert transverse == F(36, 1024)
    assert ppt_radius_1 == F(89, 1024)
    assert ppt_radius_2 == F(49, 1024)
    assert transverse < min(ppt_radius_1, ppt_radius_2)

    u = (1 + R1 - RM - 2 * RP) / (1 - 3 * RM)
    bisep_left = 3 * (R2 * R2 + R3 * R3) + (1 + 2 * R1 + RM - RP) ** 2
    bisep_right = (2 + R1 - 4 * RM - 2 * RP) ** 2
    assert u == F(-17, 29)
    assert -1 < u < 0
    assert bisep_left == F(189, 1024)
    assert bisep_right == F(144, 1024)
    assert bisep_left - bisep_right == F(45, 1024)
    print("exact state, PPT, and non-biseparability checks passed")


def permutation_matrix(d: int, sigma: tuple[int, int, int]) -> np.ndarray:
    size = d**3
    matrix = np.zeros((size, size), dtype=complex)
    inverse = tuple(sigma.index(j) for j in range(3))
    for indices in product(range(d), repeat=3):
        source = (indices[0] * d + indices[1]) * d + indices[2]
        target_indices = tuple(indices[inverse[j]] for j in range(3))
        target = (target_indices[0] * d + target_indices[1]) * d + target_indices[2]
        matrix[target, source] = 1.0
    return matrix


def partial_transpose(matrix: np.ndarray, d: int, subsystem: int) -> np.ndarray:
    tensor = matrix.reshape((d, d, d, d, d, d))
    axes = list(range(6))
    axes[subsystem], axes[subsystem + 3] = axes[subsystem + 3], axes[subsystem]
    return tensor.transpose(axes).reshape((d**3, d**3))


def matrix_checks(d: int) -> None:
    identity = permutation_matrix(d, (0, 1, 2))
    v12 = permutation_matrix(d, (1, 0, 2))
    v23 = permutation_matrix(d, (0, 2, 1))
    v13 = permutation_matrix(d, (2, 1, 0))
    v123 = permutation_matrix(d, (1, 2, 0))
    v321 = permutation_matrix(d, (2, 0, 1))

    r_plus_op = (identity + v12 + v23 + v13 + v123 + v321) / 6.0
    r_minus_op = (identity - v12 - v23 - v13 + v123 + v321) / 6.0
    r_zero_op = (2.0 * identity - v123 - v321) / 3.0
    r_one_op = (2.0 * v23 - v13 - v12) / 3.0
    r_two_op = (v12 - v13) / sqrt(3.0)
    r_three_op = 1j * (v123 - v321) / sqrt(3.0)

    coefficient_plus = 9.0 / (2.0 * d * (d + 1) * (d + 2))
    coefficient_minus = 3.0 / (16.0 * d * (d - 1) * (d - 2))
    coefficient_zero = 21.0 / (64.0 * d * (d * d - 1))
    coefficient_three = 9.0 / (32.0 * d * (d * d - 1))
    rho = (
        coefficient_plus * r_plus_op
        + coefficient_minus * r_minus_op
        + coefficient_zero * r_zero_op
        + coefficient_three * r_three_op
    )

    operators = (r_plus_op, r_minus_op, r_one_op, r_two_op, r_three_op)
    expected = (0.75, 1.0 / 32.0, 0.0, 0.0, 3.0 / 16.0)
    observed = tuple(float(np.trace(rho @ op).real) for op in operators)
    assert np.allclose(observed, expected, atol=2e-12)
    assert abs(np.trace(rho) - 1.0) < 2e-12
    assert np.linalg.eigvalsh(rho).min() > -2e-12
    assert np.linalg.norm(v123 @ rho @ v123.conj().T - rho) < 2e-12
    pt_minima = [float(np.linalg.eigvalsh(partial_transpose(rho, d, cut)).min()) for cut in range(3)]
    assert min(pt_minima) > -2e-12
    print(f"d={d}: coordinates={observed}, partial-transpose minima={pt_minima}")


def main() -> None:
    exact_checks()
    for dimension in (3, 4, 5):
        matrix_checks(dimension)
    print("all checks passed")


if __name__ == "__main__":
    main()
