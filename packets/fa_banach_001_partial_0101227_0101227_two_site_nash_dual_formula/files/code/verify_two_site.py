#!/usr/bin/env python3
"""Exact checks for the two-site nonlinear variational-formula packet."""

from fractions import Fraction

import mpmath as mp
import sympy as sp


def exact_p4_checks() -> None:
    s, t = sp.symbols("s t", positive=True)
    q4 = sp.sqrt(1 + s**4) / (s**2 + (1 - s) ** 2)
    j1 = (1 + s**3) / (s * sp.sqrt(1 + s**4))
    j2 = 1 / ((1 - s) * sp.sqrt(1 + s**4))

    h = 3 * s**4 - 2 * s**3 + 1
    assert sp.simplify(sp.diff(j1, s) + h / (s**2 * (1 + s**4) ** sp.Rational(3, 2))) == 0
    assert sp.simplify(sp.diff(j2, s) - h / ((1 - s) ** 2 * (1 + s**4) ** sp.Rational(3, 2))) == 0

    stationary = sp.factor(sp.together(sp.diff(q4, s) / q4))
    assert sp.simplify(
        stationary
        - 2 * (1 - 2 * s + s**3 - s**4)
        / ((1 + s**4) * (s**2 + (1 - s) ** 2))
    ) == 0
    assert sp.factor(sp.together(j1 - j2)).as_numer_denom()[0] == s**4 - s**3 + 2 * s - 1

    p_poly = lambda x: x**4 - x**3 + 2 * x - 1
    q_poly = lambda x: x**4 - 2 * x**3 + x**2 - 2 * x + 1

    s_lo, s_hi = Fraction(535, 1000), Fraction(536, 1000)
    t_lo, t_hi = Fraction(1883, 1000), Fraction(1884, 1000)
    assert p_poly(s_lo) < 0 < p_poly(s_hi)
    assert q_poly(t_lo) < 0 < q_poly(t_hi)

    d = lambda x: 2 * x * x - 2 * x + 1
    a4_sq_upper = (1 + s_hi**4) / d(s_lo) ** 2
    u4_sq_lower = 1 + t_lo**2
    assert a4_sq_upper < Fraction(208, 100) ** 2
    assert u4_sq_lower > Fraction(213, 100) ** 2

    print("p=4 derivative factor H(s) =", h)
    print("s_4 bracket = [0.535, 0.536]")
    print("t tail-functional bracket = [1.883, 1.884]")
    print("A_4^2 exact upper =", a4_sq_upper, "=", float(a4_sq_upper))
    print("U_4^2 exact lower =", u4_sq_lower, "=", float(u4_sq_lower))
    print("certified strict gap: A_4 < 2.08 < 2.13 < U_4")


def numerical_general_p_checks() -> None:
    mp.mp.dps = 60
    for p in (mp.mpf("2.1"), mp.mpf(3), mp.mpf(4), mp.mpf(6), mp.mpf(10)):
        f = lambda s: 1 - 2 * s + s ** (p - 1) - s**p
        root = mp.findroot(f, (mp.mpf("0.1"), mp.mpf("0.9")))
        norm_factor = (1 + root**p) ** ((p - 2) / p)
        j1 = (1 + root ** (p - 1)) / (root * norm_factor)
        j2 = 1 / ((1 - root) * norm_factor)
        q = (1 + root**p) ** (2 / p) / (root**2 + (1 - root) ** 2)
        assert abs(j1 - j2) < mp.mpf("1e-50")
        assert abs(j1 - q) < mp.mpf("1e-50")
        print(
            "p=", mp.nstr(p, 5),
            "s_p=", mp.nstr(root, 16),
            "A_p=", mp.nstr(q, 16),
        )


if __name__ == "__main__":
    exact_p4_checks()
    numerical_general_p_checks()
    print("PASS")
