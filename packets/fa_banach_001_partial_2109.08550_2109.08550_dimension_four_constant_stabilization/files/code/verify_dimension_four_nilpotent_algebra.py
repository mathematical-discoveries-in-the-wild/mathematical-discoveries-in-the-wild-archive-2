#!/usr/bin/env python3
"""Finite-field stress test for the 4x4 maximal nilpotent lemma.

The proof in the accompanying attempt is over C and is not computer-dependent.
This script independently enumerates every four-dimensional subspace of the
six-dimensional algebra of strictly upper triangular 4x4 matrices over F_3.
It selects the subspaces that are commutative subalgebras and checks that every
product in each selected algebra is zero.
"""

from __future__ import annotations

from itertools import combinations, product


Q = 3
N = 6
K = 4


def add_scaled(row: list[int], other: list[int], scalar: int) -> None:
    for j in range(len(row)):
        row[j] = (row[j] + scalar * other[j]) % Q


def rank_mod_q(rows: list[tuple[int, ...] | list[int]]) -> int:
    matrix = [[entry % Q for entry in row] for row in rows if any(entry % Q for entry in row)]
    rank = 0
    for col in range(N):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][col], -1, Q)
        matrix[rank] = [(inverse * entry) % Q for entry in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank and matrix[i][col]:
                add_scaled(matrix[i], matrix[rank], -matrix[i][col])
        rank += 1
        if rank == len(matrix):
            break
    return rank


def in_span(vector: tuple[int, ...], basis: tuple[tuple[int, ...], ...]) -> bool:
    return rank_mod_q([*basis, vector]) == K


def multiply(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    """Multiply strict-upper matrices encoded by (12,13,14,23,24,34)."""
    a, b, _c, d, _e, _f = x
    _A, _B, _C, D, E, F = y
    return (0, a * D % Q, (a * E + b * F) % Q, 0, d * F % Q, 0)


def rref_subspaces():
    """Yield each K-plane in F_Q^N exactly once via its RREF basis."""
    for pivots in combinations(range(N), K):
        free_columns = [column for column in range(N) if column not in pivots]
        slots = [
            (row, column)
            for column in free_columns
            for row, pivot in enumerate(pivots)
            if pivot < column
        ]
        for values in product(range(Q), repeat=len(slots)):
            basis = [[0] * N for _ in range(K)]
            for row, pivot in enumerate(pivots):
                basis[row][pivot] = 1
            for (row, column), value in zip(slots, values):
                basis[row][column] = value
            yield tuple(tuple(row) for row in basis)


def main() -> None:
    subspace_count = 0
    algebra_count = 0
    non_square_zero = []

    for basis in rref_subspaces():
        subspace_count += 1
        is_commutative_algebra = True
        for x in basis:
            for y in basis:
                xy = multiply(x, y)
                yx = multiply(y, x)
                if xy != yx or not in_span(xy, basis):
                    is_commutative_algebra = False
                    break
            if not is_commutative_algebra:
                break
        if not is_commutative_algebra:
            continue

        algebra_count += 1
        if any(multiply(x, y) != (0,) * N for x in basis for y in basis):
            non_square_zero.append(basis)

    expected_subspaces = 11011  # Gaussian binomial [6 choose 4]_3.
    assert subspace_count == expected_subspaces, (subspace_count, expected_subspaces)
    assert not non_square_zero, non_square_zero[:1]
    print(f"field: F_{Q}")
    print(f"four-dimensional subspaces exhausted: {subspace_count}")
    print(f"commutative subalgebras found: {algebra_count}")
    print("non-square-zero commutative subalgebras found: 0")
    print("ALL FINITE-FIELD NILPOTENT-ALGEBRA CHECKS PASSED")


if __name__ == "__main__":
    main()
