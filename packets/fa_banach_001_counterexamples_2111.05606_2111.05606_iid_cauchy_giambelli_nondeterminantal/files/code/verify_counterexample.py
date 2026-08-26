#!/usr/bin/env python3
"""Exact sanity checks for the iid-Cauchy Giambelli counterexample.

The proof itself is symbolic and is given in main.tex.  This script checks:
1. the two three-by-three determinant normal forms;
2. the obstructing four-by-four determinant;
3. finite-degree centered Schur expectations through degree 8 by extracting
   the constant Laurent coefficient after the circle parametrization.
"""

from itertools import product

import sympy as sp


def matrix_checks() -> None:
    a = sp.symbols("a", nonzero=True)
    triple_with_base = sp.Matrix([[2, 1, 1], [2, 2, a], [2, 2 / a, 2]])
    expected = 2 * (a**2 - 2 * a + 2) / a
    assert sp.simplify(triple_with_base.det() - expected) == 0

    ii = sp.I
    transitive = sp.Matrix(
        [[2, 1 + ii, 1 + ii], [1 - ii, 2, 1 + ii], [1 - ii, 1 - ii, 2]]
    )
    cyclic = sp.Matrix(
        [[2, 1 + ii, 1 - ii], [1 - ii, 2, 1 + ii], [1 + ii, 1 - ii, 2]]
    )
    assert transitive.det() == 0
    assert cyclic.det() == -8

    obstruction = sp.Matrix(
        [
            [2, 1, 1, 1],
            [2, 2, 1 + ii, 1 + ii],
            [2, 1 - ii, 2, 1 + ii],
            [2, 1 - ii, 1 - ii, 2],
        ]
    )
    assert obstruction.det() == -4


def partitions(n: int, cap: int | None = None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def complete_homogeneous(power_sums: dict[int, sp.Expr], degree: int):
    # Newton recurrence: n h_n = sum_{k=1}^n p_k h_{n-k}.
    h = [sp.Integer(1)]
    for n in range(1, degree + 1):
        h.append(sp.expand(sum(power_sums[k] * h[n - k] for k in range(1, n + 1)) / n))
    return h


def schur_from_power_sums(lam, power_sums):
    if not lam:
        return sp.Integer(1)
    degree = sum(lam)
    h = complete_homogeneous(power_sums, degree)

    def h_at(k):
        if k < 0:
            return sp.Integer(0)
        return h[k]

    length = len(lam)
    return sp.expand(
        sp.Matrix([[h_at(lam[i] - i + j) for j in range(length)] for i in range(length)]).det()
    )


def constant_term_two_circles(expr, z1, z2):
    # The expressions are ordinary polynomials in z1,z2.  Uniform circle
    # averaging keeps exactly the coefficient z1^0 z2^0.
    return sp.expand(expr).coeff(z1, 0).coeff(z2, 0)


def centered_schur_checks(max_degree: int = 8) -> None:
    c, r, z1, z2 = sp.symbols("c r z1 z2")
    t1, t2 = c + r * z1, c + r * z2
    p = {k: sp.expand(t1**k + t2**k - 2 * c**k) for k in range(1, max_degree + 1)}
    checked = 0
    for degree in range(1, max_degree + 1):
        for lam in partitions(degree):
            value = schur_from_power_sums(lam, p)
            assert constant_term_two_circles(value, z1, z2) == 0, lam
            checked += 1
    print(f"checked {checked} nonempty partitions through degree {max_degree}")


if __name__ == "__main__":
    matrix_checks()
    centered_schur_checks()
    print("all exact checks passed")
