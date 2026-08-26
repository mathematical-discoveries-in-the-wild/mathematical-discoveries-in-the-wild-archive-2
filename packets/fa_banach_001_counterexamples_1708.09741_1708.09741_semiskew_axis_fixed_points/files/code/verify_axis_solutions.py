#!/usr/bin/env python3
"""Exact symbolic checks for the semi-skew axis fixed points."""

from __future__ import annotations

import sympy as sp


def same_column_space(a: sp.Matrix, b: sp.Matrix) -> bool:
    return a.rank() == b.rank() == a.row_join(b).rank()


def polar_subspace_basis(basis: sp.Matrix) -> sp.Matrix:
    """Columns span L; return columns spanning L^perp, the polar of L."""
    null = basis.T.nullspace()
    if not null:
        return sp.zeros(basis.rows, 0)
    return sp.Matrix.hstack(*null)


def main() -> None:
    alpha1, alpha2 = sp.symbols("alpha1 alpha2", nonzero=True, real=True)
    g = sp.Matrix([[0, alpha2], [-alpha1, 0]])
    h = sp.simplify(g.inv() * g.T)
    expected_h = sp.diag(-alpha2 / alpha1, -alpha1 / alpha2)
    assert h == expected_h

    e1 = sp.Matrix([[1], [0]])
    e2 = sp.Matrix([[0], [1]])
    assert same_column_space(g * e1, e2)
    assert same_column_space(g * e2, e1)
    assert same_column_space(polar_subspace_basis(g * e1), e1)
    assert same_column_space(polar_subspace_basis(g * e2), e2)

    zero = sp.zeros(2, 0)
    plane = sp.eye(2)
    assert not same_column_space(polar_subspace_basis(g * zero), zero)
    assert not same_column_space(polar_subspace_basis(g * plane), plane)

    for a, b in [(1, 2), (3, 1), (-1, -4), (-5, -2)]:
        gn = g.subs({alpha1: a, alpha2: b})
        hn = h.subs({alpha1: a, alpha2: b})
        assert gn.det() != 0
        assert hn[0, 0] * hn[1, 1] == 1
        assert abs(float(hn[0, 0])) != 1.0

    print("all symbolic axis and hyperbolic-invariance checks passed")


if __name__ == "__main__":
    main()
