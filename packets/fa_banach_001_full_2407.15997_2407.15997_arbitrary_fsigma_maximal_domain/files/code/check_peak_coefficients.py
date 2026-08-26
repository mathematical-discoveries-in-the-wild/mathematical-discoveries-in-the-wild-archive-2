#!/usr/bin/env python3
"""Finite sanity checks for the boundary-peak divided-difference formula."""

from __future__ import annotations

import cmath
import math

import numpy as np


def peak_coefficients(n: int, w: complex) -> np.ndarray:
    return np.array(
        [math.comb(n, k) * (w.conjugate() ** k) / (2**n) for k in range(n + 1)],
        dtype=np.complex128,
    )


def quotient_from_tail(a: np.ndarray, gamma: complex) -> np.ndarray:
    n = len(a) - 1
    return np.array(
        [sum(a[k] * gamma ** (k - 1 - j) for k in range(j + 1, n + 1)) for j in range(n)],
        dtype=np.complex128,
    )


def main() -> None:
    worst_formula_error = 0.0
    worst_uniform_coefficient = 0.0
    for n in (4, 8, 16, 32, 64):
        for w_angle in np.linspace(0.0, 2.0 * math.pi, 9, endpoint=False):
            w = cmath.exp(1j * w_angle)
            a = peak_coefficients(n, w)
            for gamma_angle in np.linspace(0.0, 2.0 * math.pi, 31, endpoint=False):
                gamma = cmath.exp(1j * gamma_angle)
                b = quotient_from_tail(a, gamma)
                # numpy.polynomial.polynomial.polydiv uses increasing order.
                numerator = a.copy()
                value = sum(a[k] * gamma**k for k in range(n + 1))
                numerator[0] -= value
                quotient, remainder = np.polynomial.polynomial.polydiv(
                    numerator, np.array([-gamma, 1.0], dtype=np.complex128)
                )
                worst_formula_error = max(
                    worst_formula_error,
                    float(np.max(np.abs(quotient - b))),
                    float(np.max(np.abs(remainder))),
                )
                worst_uniform_coefficient = max(
                    worst_uniform_coefficient, float(np.max(np.abs(b)))
                )

    assert worst_formula_error < 2e-12, worst_formula_error
    assert worst_uniform_coefficient <= 1.0 + 2e-12, worst_uniform_coefficient
    print(f"max formula/remainder error: {worst_formula_error:.3e}")
    print(f"max divided-difference coefficient modulus: {worst_uniform_coefficient:.12f}")
    print("finite sanity checks passed")


if __name__ == "__main__":
    main()

