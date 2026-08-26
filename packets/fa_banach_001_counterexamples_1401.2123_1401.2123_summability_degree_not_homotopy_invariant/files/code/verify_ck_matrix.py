#!/usr/bin/env python3
"""Exact checks for the Cuntz--Krieger matrix in the proof packet."""

from itertools import combinations
from math import gcd


Q = (
    (0, 1, 1),
    (1, 1, 0),
    (1, 0, 1),
)


def det2(a, b, c, d):
    return a * d - b * c


def det3(m):
    return (
        m[0][0] * det2(m[1][1], m[1][2], m[2][1], m[2][2])
        - m[0][1] * det2(m[1][0], m[1][2], m[2][0], m[2][2])
        + m[0][2] * det2(m[1][0], m[1][1], m[2][0], m[2][1])
    )


def matvec(m, x):
    return tuple(sum(m[i][j] * x[j] for j in range(3)) for i in range(3))


def main():
    # Directed reachability.
    reach = [[bool(Q[i][j]) for j in range(3)] for i in range(3)]
    for i in range(3):
        reach[i][i] = True
    for k in range(3):
        for i in range(3):
            for j in range(3):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    assert all(all(row) for row in reach)
    assert any(sum(row) > 1 for row in Q)

    m = tuple(
        tuple((1 if i == j else 0) - Q[j][i] for j in range(3))
        for i in range(3)
    )
    assert m == ((1, -1, -1), (-1, 0, 0), (-1, 0, 0))
    assert det3(m) == 0

    entries_gcd = 0
    for row in m:
        for value in row:
            entries_gcd = gcd(entries_gcd, abs(value))
    assert entries_gcd == 1

    minors = []
    for rows in combinations(range(3), 2):
        for cols in combinations(range(3), 2):
            minors.append(
                det2(
                    m[rows[0]][cols[0]],
                    m[rows[0]][cols[1]],
                    m[rows[1]][cols[0]],
                    m[rows[1]][cols[1]],
                )
            )
    minors_gcd = 0
    for value in minors:
        minors_gcd = gcd(minors_gcd, abs(value))
    assert minors_gcd == 1
    assert any(value != 0 for value in minors)

    kernel_generator = (0, 1, -1)
    assert matvec(m, kernel_generator) == (0, 0, 0)

    print("Q is irreducible and non-permutation")
    print("I-Q^T =", m)
    print("determinant = 0, rank = 2")
    print("Smith invariants = (1, 1, 0)")
    print("kernel generator =", kernel_generator)
    print("therefore K_0(O_Q) = Z and K_1(O_Q) = Z")


if __name__ == "__main__":
    main()
