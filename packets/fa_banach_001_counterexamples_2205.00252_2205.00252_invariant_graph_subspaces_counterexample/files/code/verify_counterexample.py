#!/usr/bin/env python3
"""Exact finite-section checks for the invariant-graph counterexample.

The infinite-dimensional proof is algebraic.  These rational-matrix checks
guard against indexing mistakes and verify the advertised cross-weight
failure on several finite sections.
"""

from __future__ import annotations

from sympy import Matrix, Rational, eye, zeros


def backward_shift(q: Rational, dimension: int) -> Matrix:
    """Return B_q e_n = q**(n-1) e_{n-1} on C^dimension."""
    matrix = zeros(dimension)
    for n in range(1, dimension):
        matrix[n - 1, n] = q ** (n - 1)
    return matrix


def residue_basis(dimension: int, modulus: int, residue: int) -> Matrix:
    identity = eye(dimension)
    columns = [identity[:, j] for j in range(residue, dimension, modulus)]
    return Matrix.hstack(*columns)


def graph_basis(
    shift: Matrix, modulus: int, residue: int, slope: Rational = Rational(1)
) -> Matrix:
    domain = residue_basis(shift.rows, modulus, residue)
    return (eye(shift.rows) + slope * shift) * domain


def contains(column_basis: Matrix, vector: Matrix) -> bool:
    return column_basis.row_join(vector).rank() == column_basis.rank()


def intersection_dimension(left: Matrix, right: Matrix) -> int:
    return left.rank() + right.rank() - left.row_join(right).rank()


def check_graph_family() -> None:
    dimension = 30
    q = Rational(1, 2)
    shift = backward_shift(q, dimension)

    for modulus in range(2, 7):
        power = shift**modulus
        for residue in range(1, modulus):
            graph = graph_basis(shift, modulus, residue, Rational(3, 2))
            domain = residue_basis(dimension, modulus, residue)
            previous = residue_basis(dimension, modulus, residue - 1)

            assert graph.rank() == domain.rank()
            assert graph.rank() < dimension
            assert all(contains(graph, power * graph[:, j]) for j in range(graph.cols))
            assert intersection_dimension(graph, domain) == 0
            assert intersection_dimension(graph, previous) == 0

            other_graph = graph_basis(shift, modulus, residue, Rational(5, 3))
            assert graph.row_join(other_graph).rank() > graph.rank()


def check_source_theorem_counterexample() -> None:
    dimension = 18
    q = Rational(1, 2)
    shift = backward_shift(q, dimension)
    graph = graph_basis(shift, modulus=2, residue=1)
    even = residue_basis(dimension, 2, 0)
    odd = residue_basis(dimension, 2, 1)
    e0 = eye(dimension)[:, 0]

    assert all(contains(graph, shift**2 * graph[:, j]) for j in range(graph.cols))
    assert intersection_dimension(graph, even) == 0
    assert intersection_dimension(graph, odd) == 0
    assert not contains(graph, e0)


def check_lattices_differ_with_weight() -> None:
    dimension = 12
    q = Rational(1, 2)
    p = Rational(1, 3)
    shift_q = backward_shift(q, dimension)
    shift_p = backward_shift(p, dimension)
    graph_q = graph_basis(shift_q, modulus=2, residue=1)

    e3 = eye(dimension)[:, 3]
    test_vector = (eye(dimension) + shift_q) * e3
    image_under_other_square = shift_p**2 * test_vector

    assert contains(graph_q, test_vector)
    assert contains(graph_q, shift_q**2 * test_vector)
    assert not contains(graph_q, image_under_other_square)

    # Explicit coefficients: p^3 e_1 + q^2 p e_0 is in G_q only if q^2=p^2.
    assert image_under_other_square[1] == p**3
    assert image_under_other_square[0] == q**2 * p
    assert q**2 * p != p**3


def main() -> None:
    check_graph_family()
    check_source_theorem_counterexample()
    check_lattices_differ_with_weight()
    print("all exact finite-section checks passed")
    print("checked graph invariance for powers 2 through 6")
    print("verified the q=1/2 graph is not invariant for the p=1/3 square")


if __name__ == "__main__":
    main()
