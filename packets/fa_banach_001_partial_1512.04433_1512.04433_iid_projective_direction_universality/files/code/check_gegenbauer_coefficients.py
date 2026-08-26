#!/usr/bin/env python3
"""Finite sanity checks for the projective-direction universality packet.

This script is not a proof.  It symbolically checks a bounded table of odd
Funk--Hecke integrals and exhaustively verifies the two-dimensional Rademacher
obstruction for a few rational parameters.
"""

from itertools import product

import sympy as sp


def check_coefficients() -> None:
    t = sp.symbols("t", real=True)
    for dimension in range(3, 9):
        alpha = sp.Rational(dimension - 2, 2)
        weight = (1 - t**2) ** (alpha - sp.Rational(1, 2))
        values = []
        for degree in range(1, 10, 2):
            coefficient = sp.simplify(
                2 * sp.integrate(sp.gegenbauer(degree, alpha, t) * weight, (t, 0, 1))
            )
            if coefficient == 0:
                raise AssertionError((dimension, degree, coefficient))
            values.append(coefficient)
        print(f"n={dimension}: {values}")


def check_rademacher_pair() -> None:
    for parameter in (sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(4, 5)):
        for epsilon_1, epsilon_2 in product((-1, 1), repeat=2):
            first_sign = sp.sign(epsilon_1)
            second_sign = sp.sign(epsilon_1 + parameter * epsilon_2)
            if first_sign != second_sign:
                raise AssertionError((parameter, epsilon_1, epsilon_2))
        print(f"Rademacher obstruction verified for t={parameter}")


if __name__ == "__main__":
    check_coefficients()
    check_rademacher_pair()
    print("all finite sanity checks passed")

