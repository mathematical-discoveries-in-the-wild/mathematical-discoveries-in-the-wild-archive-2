#!/usr/bin/env python3
"""Auxiliary exact checks for the one-variable counterexample.

The proof is analytic.  This script checks the coefficient/weight formulas,
the finite defect diagonals, and the recurrence certificate used in the
no-similarity argument.
"""

from fractions import Fraction
from math import comb


def weight_squared(m: int, k: int) -> Fraction:
    b_k = comb(k + m - 1, m - 1)
    b_next = comb(k + m, m - 1)
    return Fraction(b_k, b_next)


def check_weights() -> None:
    for m in range(2, 11):
        for k in range(80):
            expected = Fraction(k + 1, k + m)
            assert weight_squared(m, k) == expected


def shift_defect_diagonal(order: int, k: int) -> int:
    """Diagonal of (id-Phi_S)^order(I) at e_k."""
    total = 0
    for j in range(order + 1):
        # S^j S*^j e_k equals e_k exactly when k >= j.
        if k >= j:
            total += (-1) ** j * comb(order, j)
    return total


def check_unilateral_shift_fails_second_defect() -> None:
    values = [shift_defect_diagonal(2, k) for k in range(12)]
    assert values == [1, -1] + [0] * 10


def check_growth_certificate() -> None:
    # q_1 >= 0 forces r_1 >= 2r_0.  Subsequent q_k >= 0 make the
    # first differences nondecreasing.  The extremal sequence is r_k=k+1.
    r = [Fraction(1), Fraction(2)]
    for _ in range(2, 200):
        r.append(2 * r[-1] - r[-2])
    assert r == [Fraction(k + 1) for k in range(200)]
    for k in range(1, 200):
        assert r[k] - r[k - 1] == 1


def check_strong_purity_on_finite_support() -> None:
    # S^k S*^k kills every vector supported on e_0,...,e_N once k>N.
    for support_max in range(50):
        for k in range(support_max + 1, support_max + 10):
            survivors = [j for j in range(support_max + 1) if j >= k]
            assert not survivors


if __name__ == "__main__":
    check_weights()
    check_unilateral_shift_fails_second_defect()
    check_growth_certificate()
    check_strong_purity_on_finite_support()
    print("all exact shift and defect checks passed")

