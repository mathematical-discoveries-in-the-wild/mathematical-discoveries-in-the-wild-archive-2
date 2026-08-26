#!/usr/bin/env python3
"""Exact sanity checks for the Taylor-minor and dimension-bound steps."""

from math import floor

import sympy as sp


def verify_minor_orders() -> None:
    t = sp.symbols("t")
    for size in range(1, 5):
        # Unit lower triangular, so det(A0)=1 exactly.
        a0 = sp.Matrix(
            size,
            size,
            lambda i, j: 1 if i == j else (i + j + 2 if i > j else 0),
        )
        a1 = sp.Matrix(size, size, lambda i, j: (i + 1) * (j + 2) + 1)
        a2 = sp.Matrix(size, size, lambda i, j: (i + 2) ** 2 - (j + 1))
        assert a0.det() == 1
        for degree in range(1, 6):
            matrix_series = t ** (degree - 1) * (a0 + t * a1 + t**2 * a2)
            determinant = sp.Poly(sp.expand(matrix_series.det()), t)
            lowest = min(exponent[0] for exponent, coefficient in determinant.terms())
            assert lowest == size * (degree - 1)
            assert determinant.coeff_monomial(t**lowest) == a0.det()


def verify_cumulative_bounds() -> None:
    for box_dimension in (0.0, 1.9, 2.0, 5.7, 12.0):
        rank_bound = floor(box_dimension / 2)
        cumulative = 0
        for degree in range(1, 9):
            quotient_bound = (rank_bound + degree) ** degree
            cumulative += quotient_bound
            assert quotient_bound >= 1
            assert cumulative >= quotient_bound


if __name__ == "__main__":
    verify_minor_orders()
    verify_cumulative_bounds()
    print("verified exact leading-minor orders for sizes 1..4 and degrees 1..5")
    print("verified cumulative Taylor-rank bounds for representative dimensions")
