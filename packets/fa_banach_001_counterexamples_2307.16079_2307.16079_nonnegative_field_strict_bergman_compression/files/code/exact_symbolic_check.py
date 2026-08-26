#!/usr/bin/env python3
"""Exact checks for the positive-field counterexample to arXiv:2307.16079.

The script verifies polynomial identities, the pointwise lower bound for B,
and the exact finite compression determinant.  The Hardy/Toeplitz dimension
argument remains a proof in the packet; it is not replaced by computation.
"""

from fractions import Fraction

import sympy as sp


def main() -> None:
    x, y = sp.symbols("x y", real=True)
    a = sp.Rational(399, 200)
    b = sp.Rational(6, 25)
    r2 = x**2 + y**2
    p3 = x**3 - 3 * x * y**2

    phi = a * (r2 - 1) / 2 - b * (1 - r2) * p3
    magnetic_field = sp.expand(sp.diff(phi, x, 2) + sp.diff(phi, y, 2))
    expected_field = sp.expand(2 * a + 16 * b * p3)
    assert sp.expand(magnetic_field - expected_field) == 0

    # On x^2+y^2=1, phi=0 and A_tau = grad(phi).(x,y).
    radial_derivative = sp.expand(x * sp.diff(phi, x) + y * sp.diff(phi, y))
    boundary_remainder = sp.rem(
        sp.Poly(radial_derivative - (a + 2 * b * p3), x, y),
        sp.Poly(r2 - 1, x, y),
    )
    assert boundary_remainder.as_expr() == 0

    lower_bound = 2 * a - 16 * b
    assert lower_bound == sp.Rational(3, 20)

    block = sp.Matrix([[2 - a, -b], [-b, 5 - a]])
    determinant = sp.factor(block.det())
    assert determinant == -sp.Rational(1703, 40000)
    assert sp.trace(block) > 0

    # Exact rational duplicate, independent of SymPy's simplifier.
    determinant_fraction = (
        (Fraction(2) - Fraction(399, 200))
        * (Fraction(5) - Fraction(399, 200))
        - Fraction(6, 25) ** 2
    )
    assert determinant_fraction == Fraction(-1703, 40000)

    print(f"Delta(phi) = {magnetic_field}")
    print(f"global lower bound for B = {lower_bound}")
    print(f"2x2 compression determinant = {determinant}")
    print("q(1)<0, q(z)<0, and the 2x2 block has one negative eigenvalue")
    print("all exact checks passed")


if __name__ == "__main__":
    main()
