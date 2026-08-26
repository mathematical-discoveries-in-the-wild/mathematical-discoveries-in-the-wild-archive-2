#!/usr/bin/env python3
"""Exact checks for the invariant-block Q3--Q4 partial result.

This is verification, not the proof: it checks the symbolic edge identities
and concrete quaternionic/octonionic Clifford models.
"""

from __future__ import annotations

import numpy as np
import sympy as sp


def check_edge_identity() -> None:
    D, m = sp.symbols("D m", positive=True)
    Delta = D**2 + (D + 1) * m + 1
    q3 = ((D - 1) / (D + m), (m + 1) / (D + m))
    q4 = (D * (D - 1) / Delta, (m + 1) * (D - 1) / Delta)

    # r=m+1 specialization of the invariant-block necessary inequality.
    line = lambda x, y: sp.factor((D - 1) * (1 + y) - (D + 2 * m + 1) * x)
    assert sp.simplify(line(*q3)) == 0
    assert sp.simplify(line(*q4)) == 0

    r = sp.symbols("r")
    general = lambda x, y: sp.factor(
        D - m + r - 2 + (D + m - r) * y - (D + m + r) * x
    )
    assert sp.simplify(general(*q3)) == 0
    assert sp.simplify(
        general(*q4) - 2 * (m + 1) * (r - m - 1) / Delta
    ) == 0


FANO_TRIPLES = [
    (1, 2, 3),
    (1, 4, 5),
    (1, 7, 6),
    (2, 4, 6),
    (2, 5, 7),
    (3, 4, 7),
    (3, 6, 5),
]


def octonion_basis_product(i: int, j: int) -> tuple[int, int]:
    if i == 0:
        return 1, j
    if j == 0:
        return 1, i
    if i == j:
        return -1, 0
    for a, b, c in FANO_TRIPLES:
        cyclic = {(a, b): c, (b, c): a, (c, a): b}
        if (i, j) in cyclic:
            return 1, cyclic[i, j]
        if (j, i) in cyclic:
            return -1, cyclic[j, i]
    raise AssertionError((i, j))


def left_multiplication_matrices() -> list[np.ndarray]:
    matrices = []
    for i in range(1, 8):
        matrix = np.zeros((8, 8), dtype=int)
        for j in range(8):
            sign, k = octonion_basis_product(i, j)
            matrix[k, j] = sign
        matrices.append(matrix)
    return matrices


def check_clifford_models() -> None:
    matrices = left_multiplication_matrices()
    identity8 = np.eye(8, dtype=int)
    zero8 = np.zeros((8, 8), dtype=int)
    for i, ji in enumerate(matrices):
        assert np.array_equal(ji.T, -ji)
        for j, jj in enumerate(matrices):
            expected = -2 * identity8 if i == j else zero8
            assert np.array_equal(ji @ jj + jj @ ji, expected)

    # The first quaternionic copy span{1,e1,e2,e3} is invariant under e1,e2,e3.
    q_indices = [0, 1, 2, 3]
    q_complement = [4, 5, 6, 7]
    for ji in matrices[:3]:
        assert np.count_nonzero(ji[np.ix_(q_complement, q_indices)]) == 0


if __name__ == "__main__":
    check_edge_identity()
    check_clifford_models()
    print("PASS: Q3/Q4 identities and real Clifford models m=3,7 verified")
