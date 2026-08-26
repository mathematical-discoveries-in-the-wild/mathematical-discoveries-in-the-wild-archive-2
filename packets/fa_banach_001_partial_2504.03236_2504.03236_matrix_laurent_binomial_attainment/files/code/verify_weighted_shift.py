#!/usr/bin/env python3
"""Transcription checks for the Laurent-binomial weighted-shift proof.

The theorem is analytic.  These finite-dimensional checks only verify the
matrix orientation, the annular norm constraints, the decisive compression,
and the lift restriction formula for representative parameters.
"""

from __future__ import annotations

import numpy as np


def weighted_shift(radius_outer: float, radius_inner: float, k: int, ell: int):
    """Return T with T e_{j+1}=w_j e_j and T e_1=w_N e_N."""
    weights = np.array([radius_outer] * k + [radius_inner] * ell, dtype=complex)
    size = k + ell
    operator = np.zeros((size, size), dtype=complex)
    for j in range(size - 1):
        operator[j, j + 1] = weights[j]
    operator[size - 1, 0] = weights[size - 1]
    return operator


def check_case(radius_outer: float, radius_inner: float, k: int, ell: int, n: int):
    rng = np.random.default_rng(1701 + 31 * k + 43 * ell + n)
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    b = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    operator = weighted_shift(radius_outer, radius_inner, k, ell)

    singular_values = np.linalg.svd(operator, compute_uv=False)
    assert np.isclose(singular_values.max(), radius_outer, atol=1e-12)
    assert np.isclose(singular_values.min(), radius_inner, atol=1e-12)
    assert np.isclose(np.linalg.norm(operator, 2), radius_outer, atol=1e-12)
    assert np.isclose(
        np.linalg.norm(np.linalg.inv(operator), 2), 1 / radius_inner, atol=1e-12
    )

    # Several rotations check the exact block used by the proof.  With
    # coordinate blocks ordered by the shift basis, row 0 and column k are the
    # compression from e_{k+1} tensor C^n to e_1 tensor C^n.
    for theta in [0.0, 0.17, 1.13, 2.71, 5.04]:
        alpha = np.exp(1j * theta)
        rotated = alpha * operator
        f_of_t = np.kron(np.linalg.matrix_power(rotated, k), a)
        f_of_t += np.kron(np.linalg.matrix_power(rotated, -ell), b)
        block = f_of_t[0:n, k * n : (k + 1) * n]
        expected = (
            alpha**k * radius_outer**k * a
            + alpha ** (-ell) * radius_inner ** (-ell) * b
        )
        assert np.allclose(block, expected, atol=2e-11)
        assert np.linalg.norm(f_of_t, 2) + 2e-11 >= np.linalg.norm(expected, 2)

    # Restriction of the canonical mixed lift to gamma(z)=(z/R,r/z).
    for rho in np.linspace(radius_inner, radius_outer, 7):
        for theta in [0.11, 1.7, 4.2]:
            z = rho * np.exp(1j * theta)
            z1, z2 = z / radius_outer, radius_inner / z
            lift = radius_outer**k * z1**k * a
            lift += radius_inner ** (-ell) * z2**ell * b
            original = z**k * a + z ** (-ell) * b
            assert np.allclose(lift, original, atol=2e-11)

    # The phase alpha^{-(k+ell)} covers the relative phase circle.  Compare a
    # grid of bidisk phases with the corresponding roots alpha.
    for phi in np.linspace(0.0, 2 * np.pi, 129, endpoint=False):
        omega = np.exp(1j * phi)
        alpha = np.exp(-1j * phi / (k + ell))
        phase_expression = alpha**k * (
            radius_outer**k * a + omega * radius_inner ** (-ell) * b
        )
        direct_expression = (
            alpha**k * radius_outer**k * a
            + alpha ** (-ell) * radius_inner ** (-ell) * b
        )
        assert np.allclose(phase_expression, direct_expression, atol=2e-11)


def main() -> None:
    cases = [
        (1.0, 0.5, 1, 1, 1),
        (2.3, 0.4, 2, 3, 2),
        (0.8, 0.17, 4, 1, 3),
        (5.0, 1.2, 3, 4, 4),
    ]
    for case in cases:
        check_case(*case)
    print(f"weighted-shift transcription checks passed for {len(cases)} cases")


if __name__ == "__main__":
    main()

