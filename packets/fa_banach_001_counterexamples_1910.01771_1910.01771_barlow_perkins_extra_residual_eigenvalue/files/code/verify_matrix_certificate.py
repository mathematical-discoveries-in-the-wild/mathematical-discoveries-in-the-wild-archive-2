"""Exact verification of the two-step matrix certificate in the packet."""

from __future__ import annotations

import sympy as sp


def child_matrices(coefficient: sp.Expr) -> list[sp.Matrix]:
    c = coefficient
    return [
        sp.Matrix([[1, 0, 0], [1, 1, c], [1, c, 1]]),
        sp.Matrix([[1, 1, c], [0, 1, 0], [c, 1, 1]]),
        sp.Matrix([[1, c, 1], [c, 1, 1], [0, 0, 1]]),
    ]


def main() -> None:
    root = sp.sqrt(3)
    fine = child_matrices(root - 1)
    coarse = child_matrices(-(1 + root))
    matrices = [sp.simplify(a * b) for b in coarse for a in fine]
    p_form = sp.eye(3) - root * sp.ones(3) / 6

    print("P eigenvalues:", p_form.eigenvals())
    assert p_form.is_positive_definite

    diagonal_representative = sp.simplify(9 * p_form - matrices[0].T * p_form * matrices[0])
    off_diagonal_representative = sp.simplify(
        9 * p_form - matrices[1].T * p_form * matrices[1]
    )
    print("9P-M00^T P M00 =")
    sp.pprint(diagonal_representative)
    print("9P-M01^T P M01 =")
    sp.pprint(off_diagonal_representative)

    assert diagonal_representative.is_positive_semidefinite
    assert off_diagonal_representative.is_positive_definite
    for matrix in matrices:
        defect = sp.simplify(9 * p_form - matrix.T * p_form * matrix)
        assert defect.is_positive_semidefinite

    seed = sp.Matrix([0, 1, 1])
    assert sp.simplify(matrices[0] * seed) == sp.Matrix([0, -3, -3])
    print("All nine inequalities and the consistency identity hold exactly.")


if __name__ == "__main__":
    main()
