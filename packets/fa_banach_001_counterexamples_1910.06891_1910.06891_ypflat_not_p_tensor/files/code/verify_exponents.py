#!/usr/bin/env python3
"""Exact algebra and finite Fourier checks for the Y_{p_flat} counterexample."""

from fractions import Fraction
import cmath
import math

import numpy as np


def check_rational(p: Fraction) -> None:
    assert 0 < p < 1
    q = 2 * p / (2 - p)
    r = p / (1 - p)
    theta = 2 * p / (1 - p)

    assert 1 / q == 1 / r + Fraction(1, 2)
    assert q / p == Fraction(2, 1) / (2 - p) > 1
    assert theta * (1 - p) == 2 * p
    assert 1 / p - 1 / r == 1


def check_fourier(n: int) -> None:
    omega = cmath.exp(2j * math.pi / n)
    u = np.array(
        [[omega ** (j * k) / math.sqrt(n) for k in range(n)] for j in range(n)],
        dtype=np.complex128,
    )
    assert np.max(np.abs(u.conj().T @ u - np.eye(n))) < 1e-10
    assert np.max(np.abs(np.abs(u) - n ** -0.5)) < 1e-10
    assert np.max(np.abs(np.linalg.svd(u, compute_uv=False) - 1.0)) < 1e-10


def main() -> None:
    for p in (
        Fraction(1, 10),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(9, 10),
    ):
        check_rational(p)
    for n in (2, 3, 5, 8, 11):
        check_fourier(n)
    print("all exponent identities and finite Fourier checks passed")


if __name__ == "__main__":
    main()
