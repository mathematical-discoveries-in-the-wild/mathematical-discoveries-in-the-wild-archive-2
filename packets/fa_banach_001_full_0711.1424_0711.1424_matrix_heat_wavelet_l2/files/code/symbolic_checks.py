#!/usr/bin/env python3
"""Non-proof sanity checks for the matrix-gamma wavelet packet.

Checks the scalar Rodrigues/Laplace identity numerically and the first
two-by-two Cayley derivative symbolically.  The general proof uses the
matrix-gamma integral and Cayley/Riesz distribution identity, not this code.
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp


def scalar_check() -> None:
    mp.mp.dps = 50
    beta = mp.mpf("6.25")
    n = 3
    s = mp.mpf("1.7")

    def g(x: mp.mpf) -> mp.mpf:
        return mp.e ** (-x) * x ** (beta - 1) / mp.gamma(beta)

    integral = mp.quad(lambda x: mp.e ** (-s * x) * mp.diff(g, x, n), [0, mp.inf])
    target = s**n * (1 + s) ** (-beta)
    print("scalar Laplace absolute error:", mp.nstr(abs(integral - target), 8))

    alpha = mp.mpf("1.5")
    lhs = mp.quad(
        lambda r: r ** (n - alpha / 2 - 1) * (1 + r) ** (-beta),
        [0, 1, mp.inf],
    )
    rhs = mp.beta(n - alpha / 2, beta - n + alpha / 2)
    print("scalar beta absolute error:", mp.nstr(abs(lhs - rhs), 8))


def two_by_two_check() -> None:
    x, y, z, lam = sp.symbols("x y z lam")
    determinant = x * z - y**2
    density = sp.exp(-x - z) * determinant**lam
    cayley = sp.diff(density, x, z) - sp.Rational(1, 4) * sp.diff(density, y, 2)
    ratio = sp.factor(cayley / (sp.exp(-x - z) * determinant ** (lam - 1)))
    expected = determinant - lam * (x + z) + lam * (lam + sp.Rational(1, 2))
    assert sp.simplify(ratio - expected) == 0
    print("m=2 first Cayley derivative: exact symbolic identity passed")


if __name__ == "__main__":
    scalar_check()
    two_by_two_check()

