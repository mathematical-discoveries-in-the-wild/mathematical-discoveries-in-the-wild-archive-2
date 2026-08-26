#!/usr/bin/env python3
"""Exact checks for the confluent weighted-Bergman determinant formula.

This is an audit, not a substitute for the proof in the packet.  For several
exact values of n and lambda it forms the mixed-derivative confluent matrix
for k(z,u)=(1-zu)^(-lambda) and checks its determinant against the closed
formula.
"""

from __future__ import annotations

import sympy as sp


def check_case(n: int, lam: sp.Rational) -> None:
    z, u = sp.symbols("z u")
    kernel = (1 - z * u) ** (-lam)
    matrix = sp.Matrix(
        [
            [
                sp.diff(kernel, z, p, u, q)
                / (sp.factorial(p) * sp.factorial(q))
                for q in range(n)
            ]
            for p in range(n)
        ]
    )
    constant = sp.prod(sp.rf(lam, j) / sp.factorial(j) for j in range(n))
    expected = constant * (1 - z * u) ** (-n * lam - n * (n - 1))
    ratio = sp.factor(matrix.det() / expected)
    if sp.simplify(ratio - 1) != 0:
        raise AssertionError((n, lam, ratio))
    print(f"PASS n={n}, lambda={lam}, constant={constant}")


def main() -> None:
    cases = [
        (2, sp.Rational(1)),
        (2, sp.Rational(2)),
        (2, sp.Rational(5, 2)),
        (3, sp.Rational(1)),
        (3, sp.Rational(2)),
        (3, sp.Rational(5, 2)),
        (4, sp.Rational(1)),
        (4, sp.Rational(2)),
        (4, sp.Rational(5, 2)),
        (5, sp.Rational(1)),
        (5, sp.Rational(2)),
    ]
    for n, lam in cases:
        check_case(n, lam)
    print(f"All {len(cases)} exact confluent-kernel checks passed.")


if __name__ == "__main__":
    main()

