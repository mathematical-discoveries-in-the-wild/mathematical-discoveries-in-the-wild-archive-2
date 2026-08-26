#!/usr/bin/env python3
"""Exact checks for the bounded-spectral-complexity packet."""

import sympy as sp


def commutator(a, b):
    return a * b - b * a


def main():
    I = sp.I

    # Exact normal-pair obstruction to rank equality under adjointing.
    v = sp.Matrix([1, 2, 3, 4])
    u = sp.eye(4) - 2 * (v * v.T) / (v.dot(v))
    a = sp.diag(0, 1, -5 * I, 2 + I)
    b = sp.simplify(u * sp.diag(0, 1 + I, 2 - I, 3 + 2 * I) * u.T)
    assert sp.simplify(u.T * u) == sp.eye(4)
    assert sp.simplify(commutator(a, a.conjugate().T)) == sp.zeros(4)
    assert sp.simplify(commutator(b, b.conjugate().T)) == sp.zeros(4)
    assert commutator(a, b).rank() == 2
    assert commutator(a.conjugate().T, b).rank() == 4

    # Lagrange interpolation of the adjoint on a three-point spectrum.
    z = sp.symbols("z")
    spectrum = [1 + I, 2 - I, -3 + 2 * I]
    p = sp.interpolate([(lam, sp.conjugate(lam)) for lam in spectrum], z)
    d = sp.diag(*spectrum, spectrum[1], spectrum[0])
    p_of_d = sp.zeros(5)
    poly = sp.Poly(p, z)
    for (degree,), coefficient in poly.terms():
        p_of_d += coefficient * (d ** degree)
    assert sp.simplify(p_of_d - d.conjugate().T) == sp.zeros(5)
    assert sp.degree(p, z) <= 2

    # A deterministic exact instance of the telescoping rank estimate.
    x = sp.diag(0, 1, 2, 4, 7)
    y = sp.Matrix(
        [
            [1, 1, 0, 0, 0],
            [0, 2, 1, 0, 0],
            [0, 0, 3, 1, 0],
            [0, 0, 0, 4, 1],
            [1, 0, 0, 0, 5],
        ]
    )
    qx = 3 * x**3 - 2 * x**2 + 5 * x + 7 * sp.eye(5)
    base_rank = commutator(x, y).rank()
    assert commutator(qx, y).rank() <= (1 + 2 + 3) * base_rank

    # Rank perturbation inequality used in the concentration corollary.
    d1 = sp.diag(0, 0, 0, 0, 5)
    d2 = sp.diag(0, 0, 0, 6, 0)
    x2, y2 = x + d1, y + d2
    lhs = (commutator(x2, y2) - commutator(x, y)).rank()
    rhs = 2 * d1.rank() + 2 * d2.rank()
    assert lhs <= rhs

    print("PASS: interpolation, commutator bounds, and exact normal-pair obstruction")


if __name__ == "__main__":
    main()

