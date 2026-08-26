#!/usr/bin/env python3
"""Symbolically verify the matrix-potential instability construction.

The symbolic check uses q=a+lambda.  It verifies the identities that make
N=w eta^T nilpotent and make u an eigenfunction of d^2/dx^2+V.  It also
checks the explicit non-dissipative matrix at x=pi/2 for a=lambda=1.
"""

import sympy as sp


def main():
    c, d, q = sp.symbols("c d q", real=True)
    u = sp.Matrix([1, c, d])
    u_second = sp.Matrix([0, -c, -4*d])
    w = q*u-u_second
    determinant = sp.expand((u.cross(w)).dot(u.cross(w)))
    expected = c**2 + (9*c**2+16)*d**2
    assert sp.simplify(determinant-expected) == 0

    eta = (w.dot(w)*u-u.dot(w)*w)/determinant
    assert sp.simplify(eta.dot(u)-1) == 0
    assert sp.simplify(eta.dot(w)) == 0

    nilpotent = sp.simplify(w*eta.T*w*eta.T)
    assert nilpotent == sp.zeros(3)

    a, lam = sp.symbols("a lam", positive=True)
    # q is a+lambda, N*u=w, and V=-aI+N.
    pde_residual = sp.simplify(u_second-a*u+w-lam*u).subs(q, a+lam)
    assert pde_residual == sp.zeros(3, 1)

    # Special point x=pi/2 for a=lambda=1: c=0, d=-1, q=2.
    eta_mid = sp.simplify(eta.subs({c: 0, d: -1, q: 2}))
    w_mid = w.subs({c: 0, d: -1, q: 2})
    v_mid = -sp.eye(3) + w_mid*eta_mid.T
    expected_mid = sp.Matrix([[2, 0, 1], [0, -1, 0], [-9, 0, -4]])
    assert v_mid == expected_mid
    assert v_mid.charpoly().as_expr().factor() == (sp.Symbol("lambda") + 1)**3

    print("cross-product denominator:", determinant)
    print("eta^T u:", sp.simplify(eta.dot(u)))
    print("eta^T w:", sp.simplify(eta.dot(w)))
    print("N^2 is zero:", nilpotent == sp.zeros(3))
    print("PDE residual is zero:", pde_residual == sp.zeros(3, 1))
    print("V(pi/2) for a=lambda=1:")
    sp.pprint(v_mid)
    print("all symbolic checks passed")


if __name__ == "__main__":
    main()
