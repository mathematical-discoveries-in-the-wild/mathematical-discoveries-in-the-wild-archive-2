#!/usr/bin/env python3
"""Exact checks for the complex three-point strong-Leibniz counterexample."""

import sympy as sp


def squared_modulus(expr):
    return sp.factor(sp.expand_complex(expr * sp.conjugate(expr)))


def verify_symbolic_family():
    k = sp.symbols("k", positive=True, real=True)
    i = sp.I
    z = (k**2 - 1 - 2 * k * i) / (k**2 + 1)
    f = [sp.Integer(1), z, 2 - z]
    a = [sp.simplify(1 / x) for x in f]
    mean_a = sp.simplify(sum(a) / 3)
    deviations = [sp.simplify(x - mean_a) for x in a]
    D = (k**2 + 1) * (k**2 + 9)

    assert sp.simplify(squared_modulus(z) - 1) == 0
    assert sp.simplify(sum(f) / 3 - 1) == 0
    assert sp.simplify(squared_modulus(f[2]) - (k**2 + 9) / (k**2 + 1)) == 0
    expected_squares = [
        64 / (9 * D),
        4 * (9 * k**2 + 25) / (9 * D),
        4 * (9 * k**2 + 1) / (9 * D),
    ]
    for actual, expected in zip(deviations, expected_squares):
        assert sp.simplify(squared_modulus(actual) - expected) == 0


def verify_explicit_witness():
    i = sp.I
    f = [sp.Integer(1), (24 - 7 * i) / 25, (26 + 7 * i) / 25]
    a = [sp.simplify(1 / x) for x in f]

    def sigma1(values):
        mean = sp.simplify(sum(values) / 3)
        return sp.simplify(
            sum(sp.sqrt(squared_modulus(x - mean)) for x in values) / 3
        )

    sigma_f = sigma1(f)
    sigma_a = sigma1(a)
    assert sp.simplify(sigma_f - 2 * sp.sqrt(2) / 15) == 0
    expected_a = (
        4 * sp.sqrt(29) + sp.sqrt(12818) + sp.sqrt(13514)
    ) / 1305
    assert sp.simplify(sigma_a - expected_a) == 0

    # Fully rational certificates for the strict radical comparison:
    # LHS > 4*5+113+116 = 249, while
    # 174*sqrt(2) < 174*(71/50) = 6177/25 < 249.
    assert 29 > 5**2
    assert 12818 > 113**2
    assert 13514 > 116**2
    assert sp.Rational(71, 50) ** 2 > 2
    assert sp.Rational(6177, 25) < 249
    assert sp.N(sigma_a - sigma_f, 50) > 0


if __name__ == "__main__":
    verify_symbolic_family()
    verify_explicit_witness()
    print("PASS: symbolic family and exact k=7 inverse violation")

