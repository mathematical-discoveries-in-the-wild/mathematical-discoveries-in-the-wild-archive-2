#!/usr/bin/env python3
"""Exact checks for the first-plane rotation factorization."""

import sympy as sp


def main() -> None:
    c, s = sp.symbols("c s", nonzero=True, real=True)
    A = sp.Matrix([[c, -s], [s, c]])
    U = sp.Matrix([[1, s / c], [0, 1]])
    L = sp.Matrix([[1 / c, 0], [s, c]])
    defect = sp.simplify(U * A - L)
    defect = defect.subs(s**2, 1 - c**2).applyfunc(sp.simplify)
    assert defect == sp.zeros(2)
    assert sp.simplify(A.det().subs(s**2, 1 - c**2)) == 1
    assert U.det() == 1
    assert L.det() == 1

    endpoint = sp.Matrix([[0, -1], [1, 0]])
    e1 = sp.Matrix([1, 0])
    e2 = sp.Matrix([0, 1])
    assert endpoint * e2 == -e1

    # If U is unit upper triangular, U e1=e1, so (U A)e2=-e1.
    a = sp.symbols("a")
    arbitrary_unit_upper = sp.Matrix([[1, a], [0, 1]])
    assert arbitrary_unit_upper * endpoint * e2 == -e1
    print("PASS: U(theta) A(theta) = L(theta) under c^2+s^2=1")
    print("PASS: all three 2x2 blocks have determinant one")
    print("PASS: endpoint sends e2 to -e1 for every unit-upper multiplier")


if __name__ == "__main__":
    main()

