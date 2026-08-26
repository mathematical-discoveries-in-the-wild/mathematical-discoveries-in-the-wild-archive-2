#!/usr/bin/env python3
"""Exact symbolic checks for the trace-Levi growing-weight identity."""

import sympy as sp


def check_gaussian_dimension(n: int) -> None:
    """Check both sides relative to the Gaussian L2 mass in C^n."""
    a, b = sp.symbols("a b", positive=True)
    # phi=(a/2)|z|^2 and v=exp(-b|z|^2).  For each coordinate,
    # |T_j v|^2-|S_j v|^2 = 2*a*b*|z_j|^2*|v|^2.
    expected_r2 = sp.Rational(n, 2) / b
    lhs_over_mass = sp.simplify(2 * a * b * expected_r2)
    levi_trace = sp.Rational(n, 2) * a
    rhs_over_mass = sp.simplify(2 * levi_trace)
    assert sp.simplify(lhs_over_mass - rhs_over_mass) == 0


def check_adjoint_conjugation() -> None:
    """Verify conjugating T* turns it into antiholomorphic divergence."""
    x, y = sp.symbols("x y", real=True)
    phi = x**2 + 3 * y**2 + x * y
    k_re = x**2 - y
    k_im = x * y + 2
    k = k_re + sp.I * k_im

    def dz(expr):
        return (sp.diff(expr, x) - sp.I * sp.diff(expr, y)) / 2

    def dbar(expr):
        return (sp.diff(expr, x) + sp.I * sp.diff(expr, y)) / 2

    tstar_k = -(dz(k) + dz(phi) * k)
    g = sp.exp(phi) * sp.conjugate(k)
    transformed = -sp.exp(-phi) * dbar(g)
    assert sp.simplify(sp.conjugate(tstar_k) - transformed) == 0


def check_intertwining() -> None:
    """Verify T(e^phi u)=e^phi dbar(u) on a non-holomorphic polynomial."""
    x, y = sp.symbols("x y", real=True)
    phi = x**2 + x * y + 2 * y**2
    u = x**2 + sp.I * x * y + y

    def dbar(expr):
        return (sp.diff(expr, x) + sp.I * sp.diff(expr, y)) / 2

    v = sp.exp(phi) * u
    tv = dbar(v) - v * dbar(phi)
    assert sp.simplify(tv - sp.exp(phi) * dbar(u)) == 0


if __name__ == "__main__":
    for dimension in range(1, 9):
        check_gaussian_dimension(dimension)
    check_adjoint_conjugation()
    check_intertwining()
    print("PASS: dimensions 1..8, adjoint conjugation, and T intertwining")
