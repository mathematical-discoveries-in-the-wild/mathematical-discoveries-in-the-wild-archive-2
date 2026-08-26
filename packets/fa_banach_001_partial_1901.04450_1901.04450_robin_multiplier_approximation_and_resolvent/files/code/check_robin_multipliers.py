#!/usr/bin/env python3
"""Symbolic and finite-grid checks for the Robin multiplier identities.

This script is diagnostic only; the packet contains uniform analytic proofs.
"""

from __future__ import annotations

import math

import sympy as sp


def symbolic_checks() -> None:
    alpha, beta, n, t = sp.symbols("alpha beta n t", nonzero=True)
    b = sp.exp(-n * t) * (alpha - beta * n * sp.exp(-t)) / (alpha - beta * n)
    factored = sp.exp(-n * t) * (
        1 + beta * (1 - sp.exp(-t)) * n / (alpha - beta * n)
    )
    assert sp.simplify(b - factored) == 0
    derivative = sp.simplify(sp.diff(b, t).subs(t, 0))
    expected = -n + beta * n / (alpha - beta * n)
    assert sp.simplify(derivative - expected) == 0

    lam, a = sp.symbols("lambda a", nonzero=True)
    lhs = lam / (lam - 1 / a)
    rhs = 1 - lam ** -1 / (lam ** -1 - a)
    assert sp.simplify(lhs - rhs) == 0


def numerical_checks() -> None:
    cs = (-2.0, 0.0, 0.3, 1.2, 2.9, 10.1)
    ts = (1e-7, 1e-5, 1e-3, 5e-3)
    for c in cs:
        ratios = []
        for n in range(1, 501):
            if abs(n - c) < 1e-12:
                raise AssertionError("resonant test parameter")
            for t in ts:
                a = -math.expm1(-n * t)
                q = -math.expm1(-(n + 1) * t) / a
                ratio = (n * q - c) / (n - c)
                ratios.append(abs(ratio))
        lo, hi = min(ratios), max(ratios)
        print(f"c={c:5.1f}: min |ratio|={lo:.6g}, max |ratio|={hi:.6g}")
        assert lo > 1e-3
        assert hi < 100


def main() -> None:
    symbolic_checks()
    numerical_checks()
    print("PASS: factorization, derivative, resolvent, and finite-grid ratios")


if __name__ == "__main__":
    main()
