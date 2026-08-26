#!/usr/bin/env python3
"""Exact scalar verification of the counterexample to printed Conjecture 3.7."""

import sympy as sp


def main() -> None:
    # Scalar data: n=m=1, A=4, B=1, s=3/2, r=p=t=1.
    A = sp.Integer(4)
    B = sp.Integer(1)
    s = sp.Rational(3, 2)
    r = p = t = sp.Integer(1)

    # For positive scalars x sharp y = sqrt(xy).
    lhs = (sp.sqrt(A**s * B**s)) ** r
    rhs = (
        A ** ((1 - t) * s * r * p / 2)
        * B ** (t * s * r * p)
        * A ** ((1 - t) * s * r * p / 2)
    ) ** (1 / p)

    assert sp.simplify(lhs - 2 * sp.sqrt(2)) == 0
    assert sp.simplify(rhs - 1) == 0
    assert sp.simplify(lhs - rhs) > 0
    print(f"LHS = {lhs}")
    print(f"RHS = {rhs}")
    print(f"LHS - RHS = {sp.simplify(lhs - rhs)} > 0")


if __name__ == "__main__":
    main()
