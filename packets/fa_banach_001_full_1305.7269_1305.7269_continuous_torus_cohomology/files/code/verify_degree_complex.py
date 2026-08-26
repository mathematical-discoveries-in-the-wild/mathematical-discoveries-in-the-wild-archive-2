#!/usr/bin/env python3
"""Exact sign checks for the winding-number shadow of the bar differential.

This is only a sanity check.  The proof packet uses normalized cochains and
the smash-product lifting argument, which is stronger and avoids relying on
this finite-dimensional calculation.
"""

from fractions import Fraction


def degree_differential(n: int) -> list[list[int]]:
    """Matrix Z^n -> Z^(n+1) induced by the inhomogeneous bar differential."""
    matrix = [[0 for _ in range(n)] for _ in range(n + 1)]

    # f(x_2,...,x_{n+1})
    for j in range(n):
        matrix[j + 1][j] += 1

    # sum_i (-1)^i f(...,x_i+x_{i+1},...)
    for i in range(1, n + 1):
        sign = -1 if i % 2 else 1
        for j in range(1, n + 1):
            if j < i:
                matrix[j - 1][j - 1] += sign
            elif j == i:
                matrix[i - 1][j - 1] += sign
                matrix[i][j - 1] += sign
            else:
                matrix[j][j - 1] += sign

    # (-1)^(n+1) f(x_1,...,x_n)
    sign = -1 if (n + 1) % 2 else 1
    for j in range(n):
        matrix[j][j] += sign
    return matrix


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def rank(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def main() -> None:
    matrices = {n: degree_differential(n) for n in range(1, 10)}
    assert matrices[1] == [[0], [0]]
    assert matrices[2] == [[-1, 0], [0, 0], [0, 1]]
    assert matrices[3] == [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]

    for n in range(1, 9):
        composition = multiply(matrices[n + 1], matrices[n])
        assert all(value == 0 for row in composition for value in row)

    # Exactness over Q in degrees 2,...,8.  In degree 3 this reproduces
    # ker D_3={(a,0,c)}=im D_2 integrally from the displayed matrices.
    for n in range(2, 9):
        assert rank(matrices[n - 1]) + rank(matrices[n]) == n

    print("bar-differential signs: PASS")
    print("D2 =", matrices[2])
    print("D3 =", matrices[3])
    print("D_(n+1) D_n = 0 for n=1,...,8: PASS")
    print("winding complex exact over Q in degrees 2,...,8: PASS")


if __name__ == "__main__":
    main()
