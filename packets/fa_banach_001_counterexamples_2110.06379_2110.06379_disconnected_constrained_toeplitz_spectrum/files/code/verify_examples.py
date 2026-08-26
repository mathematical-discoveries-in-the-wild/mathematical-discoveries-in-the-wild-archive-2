#!/usr/bin/env python3
"""Exact arithmetic checks for the constrained Toeplitz examples."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z = sp.symbols("z")
    phi = z / (1 - z / 2) ** 2

    # Neil example: gamma=-1/2 and its only preimage is -2.
    neil_gamma = -sp.Rational(1, 2)
    neil_numerator = sp.factor(sp.together(phi - neil_gamma).as_numer_denom()[0])
    assert neil_numerator == (z + 2) ** 2
    assert sp.solve(sp.Eq(phi, neil_gamma), z) == [-2]

    # Two-point example: r=1/10, q=r^2.  Sum the even and odd
    # autocorrelation contributions to <phi f,f>/||f||^2.
    q = sp.Rational(1, 100)
    x = q / 4
    even_contribution = 4 * x / (1 - x) ** 2
    odd_contribution = -(1 + q) * (1 + x) / (2 * (1 - x) ** 2)
    two_point_gamma = sp.factor(even_contribution + odd_contribution)
    expected_gamma = -sp.Rational(79402, 159201)
    assert two_point_gamma == expected_gamma

    s = -two_point_gamma
    assert s > sp.Rational(4, 9)
    assert s < sp.Rational(1, 2)

    roots = sp.solve(sp.Eq(phi, two_point_gamma), z)
    assert len(roots) == 2
    root_values = [float(sp.N(root, 18)) for root in roots]
    assert all(abs(value) > 1.0 for value in root_values)

    # Check the constraint parameter and the norm formula for
    # f=(1-z)/(1-r^2 z^2).
    r = sp.Rational(1, 10)
    t = sp.factor((1 + r) / (1 - r))
    f_norm_squared = sp.factor(2 / (1 - r**4))
    assert t == sp.Rational(11, 9)
    assert f_norm_squared == sp.Rational(20000, 9999)

    print("Neil preimage:", sp.solve(sp.Eq(phi, neil_gamma), z))
    print("two-point gamma:", two_point_gamma)
    print("two-point preimages:", roots)
    print("two-point preimages (decimal):", root_values)
    print("verified exact t=11/9 and ||f||^2=20000/9999")


if __name__ == "__main__":
    main()
