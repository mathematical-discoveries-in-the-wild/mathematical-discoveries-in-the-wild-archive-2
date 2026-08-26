#!/usr/bin/env python3
"""Independent checks for the binomial BMO-rearrangement constants.

The proof in the packet is analytic.  This script checks exact formulas,
small finite optimization problems, and the displayed dimension table.
"""

from fractions import Fraction
from itertools import product
from math import comb, sqrt

import numpy as np
from scipy.optimize import linprog


def beta_formula(m: int) -> Fraction:
    return Fraction(m * comb(m - 1, (m - 1) // 2), 2**m)


def beta_direct(m: int) -> Fraction:
    return sum(
        Fraction(comb(m, k), 2**m) * abs(Fraction(k) - Fraction(m, 2))
        for k in range(m + 1)
    )


def exact_lipschitz_mad(m: int) -> float:
    """Maximize MAD on the m-cube by enumerating absolute-value signs.

    Translation is fixed by f(0)=0.  For each sign pattern s,
    E|f-Ef| is the maximum of E[(s-Es)f].
    """
    vertices = np.array(list(product([0, 1], repeat=m)), dtype=int)
    count = len(vertices)
    edges = [
        (i, j)
        for i in range(count)
        for j in range(i + 1, count)
        if np.sum(vertices[i] != vertices[j]) == 1
    ]
    rows = []
    rhs = []
    for i, j in edges:
        row = np.zeros(count)
        row[i], row[j] = 1.0, -1.0
        rows.extend([row, -row])
        rhs.extend([1.0, 1.0])

    best = 0.0
    # Global sign reversal is redundant, so anchor s[0]=1.
    for tail in product([-1.0, 1.0], repeat=count - 1):
        signs = np.array((1.0,) + tail)
        objective = (signs - signs.mean()) / count
        result = linprog(
            -objective,
            A_ub=np.array(rows),
            b_ub=np.array(rhs),
            bounds=[(0.0, 0.0)] + [(None, None)] * (count - 1),
            method="highs",
        )
        assert result.success
        best = max(best, -result.fun)
    return best


def hybrid_constant(n: int) -> tuple[Fraction, int]:
    candidates = []
    for m in range(1, n):
        concentration = 1 + 4 * beta_formula(m)
        container = Fraction(2 ** (n - m))
        candidates.append((min(concentration, container), m))
    return max(candidates)


def main() -> None:
    for m in range(1, 201):
        assert beta_formula(m) == beta_direct(m)
        if m > 1:
            assert beta_formula(m) >= beta_formula(m - 1)

    for m in range(1, 4):
        optimum = exact_lipschitz_mad(m)
        expected = float(beta_formula(m))
        assert abs(optimum - expected) < 1e-9, (m, optimum, expected)

    expected_table = [
        4.0,
        6.0,
        6.0,
        8.0,
        8.0,
        8.0,
        9.5,
        9.5,
        10.75,
        10.75,
        11.84375,
    ]
    actual_table = [2 * float(hybrid_constant(n)[0]) for n in range(2, 13)]
    assert actual_table == expected_table, actual_table

    # The unhybridized binomial comparison is never worse than the source
    # concentration constant, and is strictly better once m >= 2.
    for m in range(1, 201):
        new = 1 + 4 * float(beta_formula(m))
        old = 1 + 2 * sqrt(m)
        assert new <= old + 1e-12
        if m >= 2:
            assert new < old

    print("PASS: beta formula/monotonicity checked through m=200")
    print("PASS: exact Lipschitz-cube LP optima agree for m=1,2,3")
    print("PASS: hybrid constants for n=2,...,12 match the packet")
    print("PASS: binomial comparison improves the source term for m>=2")


if __name__ == "__main__":
    main()
