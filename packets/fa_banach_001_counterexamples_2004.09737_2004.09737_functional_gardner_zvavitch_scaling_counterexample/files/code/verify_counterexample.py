#!/usr/bin/env python3
"""Exact verification of the reciprocal-scaling counterexample."""

import sympy as sp


def main() -> None:
    x, y = sp.symbols("x y", real=True)

    # The exponent gap proving h((x+y)/2) >= sqrt(f_M(x) g_M(y)).
    gap = sp.simplify((x**2 + y**2) / 2 - (x + y) ** 2 / 4)
    assert sp.simplify(gap - (x - y) ** 2 / 4) == 0

    # Integral of exp(-x^2) against standard Gaussian measure.
    gaussian_density = sp.exp(-x**2 / 2) / sp.sqrt(2 * sp.pi)
    mass = sp.integrate(sp.exp(-x**2) * gaussian_density, (x, -sp.oo, sp.oo))
    assert sp.simplify(mass - 1 / sp.sqrt(3)) == 0

    # For each proposed constant C, M=2C+1 violates the reduced inequality.
    for constant in (sp.Integer(1), sp.Integer(2), sp.Integer(10), sp.Integer(100)):
        amplitude = 2 * constant + 1
        ratio = sp.simplify((amplitude + 1 / amplitude) / (2 * constant))
        assert ratio > 1
        print(f"C={str(constant):>3}, M={str(amplitude):>3}, RHS/LHS={ratio}")

    print(f"pointwise exponent gap: {gap}")
    print(f"Gaussian base integral: {mass}")
    print("all exact checks: PASS")


if __name__ == "__main__":
    main()
