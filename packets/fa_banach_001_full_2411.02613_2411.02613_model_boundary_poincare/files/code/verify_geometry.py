#!/usr/bin/env python3
"""Symbolic sanity checks for the model-boundary horizontal fields."""

import sympy as sp


x, y, t, lam = sp.symbols("x y t lam", positive=True)


def check(k: int) -> None:
    radial = (x**2 + y**2) ** (k - 1)
    a = y * radial
    b = -x * radial

    # For X1=d_x+a d_t and X2=d_y+b d_t, the bracket is vertical.
    bracket_t = sp.expand(sp.diff(b, x) - sp.diff(a, y))
    expected = sp.expand(-2 * k * radial)
    assert sp.simplify(bracket_t - expected) == 0

    terminal = sp.diff(bracket_t, x, 2 * k - 2).subs({x: 0, y: 0})
    assert terminal == -2 * k * sp.factorial(2 * k - 2)

    # Coefficients in the vertical terms have weighted degree 2k-1.
    assert sp.expand(a.subs({x: lam * x, y: lam * y}) - lam ** (2 * k - 1) * a) == 0
    assert sp.expand(b.subs({x: lam * x, y: lam * y}) - lam ** (2 * k - 1) * b) == 0


def main() -> None:
    for k in range(2, 9):
        check(k)
    print("PASS: bracket, terminal commutator, and homogeneity checks for k=2,...,8")


if __name__ == "__main__":
    main()

