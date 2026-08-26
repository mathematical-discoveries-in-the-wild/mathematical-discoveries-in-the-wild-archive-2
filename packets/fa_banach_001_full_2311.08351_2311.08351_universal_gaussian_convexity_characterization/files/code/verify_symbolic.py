#!/usr/bin/env python3
"""Symbolic sanity checks for the universal Gaussian characterization."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    lam = sp.symbols("lam", real=True)
    mean, variance = sp.symbols("mean variance", real=True)

    gaussian_k = mean * lam + variance * lam**2 / 2
    gaussian_phi = sp.simplify(gaussian_k / lam)
    assert gaussian_phi == mean + variance * lam / 2
    assert sp.diff(gaussian_phi, lam, 2) == 0

    # The simplest non-Gaussian obstruction: a symmetric Rademacher law.
    rademacher_phi = sp.log(sp.cosh(lam)) / lam
    series = sp.series(rademacher_phi, lam, 0, 7)
    assert series.removeO().coeff(lam, 3) == -sp.Rational(1, 12)
    second_at_one = sp.N(sp.diff(rademacher_phi, lam, 2).subs(lam, 1), 30)
    second_at_minus_one = sp.N(
        sp.diff(rademacher_phi, lam, 2).subs(lam, -1), 30
    )
    assert second_at_one < 0 < second_at_minus_one

    print("Gaussian normalized log-mgf:", gaussian_phi)
    print("Rademacher expansion:", series)
    print("Rademacher second derivatives at +/-1:", second_at_one, second_at_minus_one)


if __name__ == "__main__":
    main()
