#!/usr/bin/env python3
"""Exact verification of the 2x2 self-adjoint symmetrized-AGM witness."""

from __future__ import annotations

import itertools

import sympy as sp


def main() -> None:
    matrices = (
        sp.Matrix([[-1, -2], [-2, 0]]),
        sp.Matrix([[-2, 2], [2, 1]]),
        sp.Matrix([[-1, 1], [1, 2]]),
    )

    without_sum = sp.zeros(2)
    with_sum = sp.zeros(2)
    for indices in itertools.product(range(3), repeat=3):
        product = sp.eye(2)
        for index in indices:
            product = matrices[index] * product
        term = product.T * product
        with_sum += term
        if len(set(indices)) == 3:
            without_sum += term

    without = without_sum / 6
    with_ = with_sum / 27
    expected_without = sp.Matrix([[sp.Rational(521, 6), 27],
                                  [27, sp.Rational(641, 6)]])
    expected_with = sp.Matrix([[sp.Rational(1027, 9), sp.Rational(302, 27)],
                               [sp.Rational(302, 27), sp.Rational(3083, 27)]])
    assert without == expected_without
    assert with_ == expected_with
    assert all(matrix == matrix.T for matrix in matrices)

    norm_without = sp.Rational(581, 6) + sp.sqrt(829)
    norm_with = (3082 + sp.sqrt(91205)) / 27
    assert norm_without in without.eigenvals()
    assert norm_with in with_.eigenvals()

    # Completely rational certificate for the strict comparison:
    # sqrt(829)>1439/50 and sqrt(91205)<303, so the norm gap is
    # larger than 581/6+1439/50-(3082+303)/27=164/675.
    assert sp.Rational(1439, 50) ** 2 < 829
    assert 303**2 > 91205
    rational_gap_bound = (
        sp.Rational(581, 6)
        + sp.Rational(1439, 50)
        - sp.Rational(3082 + 303, 27)
    )
    assert rational_gap_bound == sp.Rational(164, 675) > 0

    print("E_wo =")
    sp.pprint(without)
    print("E_wr =")
    sp.pprint(with_)
    print("||E_wo|| =", norm_without, "=", sp.N(norm_without, 16))
    print("||E_wr|| =", norm_with, "=", sp.N(norm_with, 16))
    print("ratio =", sp.N(norm_without / norm_with, 16))
    print("certified norm gap >", rational_gap_bound)


if __name__ == "__main__":
    main()
