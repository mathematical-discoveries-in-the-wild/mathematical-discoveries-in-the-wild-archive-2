#!/usr/bin/env python3
"""Exact finite checks for the O(3) local one-norm packet."""

from itertools import permutations, product


PERMS = tuple(permutations(range(3)))


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def permute(a, rows, cols):
    return tuple(tuple(a[rows[i]][cols[j]] for j in range(3)) for i in range(3))


def normalize(a):
    # Row signs make the first column positive, then column signs make the
    # first row positive.
    row_fixed = tuple(
        tuple(a[i][j] * a[i][0] for j in range(3)) for i in range(3)
    )
    return tuple(
        tuple(row_fixed[i][j] * row_fixed[0][j] for j in range(3))
        for i in range(3)
    )


def canonical(a):
    return min(
        sum(normalize(permute(a, rows, cols)), ())
        for rows in PERMS
        for cols in PERMS
    )


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def main():
    nonsingular = []
    for entries in product((-1, 1), repeat=9):
        matrix = tuple(tuple(entries[3 * i + j] for j in range(3)) for i in range(3))
        if det3(matrix):
            nonsingular.append(matrix)

    orbits = {canonical(matrix) for matrix in nonsingular}
    assert len(nonsingular) == 192
    assert len(orbits) == 1

    sign_matrix = (
        (1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
    )
    polar_numerator = (
        (1, 2, 2),
        (2, -2, 1),
        (2, 1, -2),
    )
    assert matmul(polar_numerator, transpose(polar_numerator)) == (
        (9, 0, 0),
        (0, 9, 0),
        (0, 0, 9),
    )
    assert tuple(
        tuple(1 if value > 0 else -1 for value in row)
        for row in polar_numerator
    ) == sign_matrix
    positive_numerator = matmul(sign_matrix, transpose(polar_numerator))
    assert positive_numerator == (
        (5, 1, 1),
        (1, 5, -1),
        (1, -1, 5),
    )
    # The characteristic polynomial is (lambda-3)(lambda-6)^2.
    assert det3(positive_numerator) == 108
    assert sum(positive_numerator[i][i] for i in range(3)) == 15
    assert sum(
        positive_numerator[i][i] * positive_numerator[j][j]
        - positive_numerator[i][j] * positive_numerator[j][i]
        for i, j in ((0, 1), (0, 2), (1, 2))
    ) == 72
    assert positive_numerator[0][0] == 5
    assert (
        positive_numerator[0][0] * positive_numerator[1][1]
        - positive_numerator[0][1] * positive_numerator[1][0]
    ) == 24
    assert sum(abs(value) for row in polar_numerator for value in row) == 15

    print("nonsingular_sign_matrices=192")
    print("signed_permutation_orbits=1")
    print("canonical_polar_factor_verified=true")
    print("one_norm=5")


if __name__ == "__main__":
    main()
