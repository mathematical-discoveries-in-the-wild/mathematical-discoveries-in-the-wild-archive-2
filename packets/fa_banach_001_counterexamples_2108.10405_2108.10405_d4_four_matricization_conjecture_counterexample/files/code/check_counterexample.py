#!/usr/bin/env python3
"""Exact verifier for the rational counterexample to Conjecture 1.

All calculations are over the integers.  Dividing the displayed matrices by
8023 produces the actual symmetric matricizations of the normalized spectrum.
"""

WEIGHTS = (1000, 1000, 1000, 1000, 703, 703, 703, 660, 660, 594)
DENOMINATOR = 8023


def det_int(matrix):
    """Integer determinant by fraction-free Bareiss elimination."""
    a = [list(row) for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        previous = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def leading_principal_minors(matrix):
    return tuple(det_int([row[:k] for row in matrix[:k]])
                 for k in range(1, len(matrix) + 1))


def symmetric_matricization(order):
    """Place weights in upper-triangular order and add the transpose."""
    positions = ((0, 0), (0, 1), (0, 2), (0, 3), (1, 1),
                 (1, 2), (1, 3), (2, 2), (2, 3), (3, 3))
    matrix = [[0] * 4 for _ in range(4)]
    for (i, j), index in zip(positions, order):
        value = WEIGHTS[index - 1]
        matrix[i][j] = 2 * value if i == j else value
        matrix[j][i] = matrix[i][j]
    return matrix


def source_four_matrices():
    l = (None,) + WEIGHTS
    return (
        [[2*l[10], l[3], l[2], l[1]],
         [l[3], 2*l[4], l[5], l[6]],
         [l[2], l[5], 2*l[7], l[8]],
         [l[1], l[6], l[8], 2*l[9]]],
        [[2*l[10], l[3], l[2], l[1]],
         [l[3], 2*l[4], l[5], l[7]],
         [l[2], l[5], 2*l[6], l[8]],
         [l[1], l[7], l[8], 2*l[9]]],
        [[2*l[10], l[6], l[2], l[1]],
         [l[6], 2*l[5], l[4], l[3]],
         [l[2], l[4], 2*l[7], l[8]],
         [l[1], l[3], l[8], 2*l[9]]],
        [[2*l[10], l[7], l[2], l[1]],
         [l[7], 2*l[5], l[4], l[3]],
         [l[2], l[4], 2*l[6], l[8]],
         [l[1], l[3], l[8], 2*l[9]]],
    )


def main():
    assert sum(WEIGHTS) == DENOMINATOR
    assert all(WEIGHTS[i] >= WEIGHTS[i + 1]
               for i in range(len(WEIGHTS) - 1))
    assert WEIGHTS[-1] > 0

    tests = source_four_matrices()
    assert tests[0] == tests[1]
    assert tests[2] == tests[3]
    a, b = tests[0], tests[2]
    a_minors = leading_principal_minors(a)
    b_minors = leading_principal_minors(b)
    assert a_minors == (1188, 1376000, 753535708, 293705189448)
    assert b_minors == (1188, 1176119, 465623314, 137338080)
    assert min(a_minors + b_minors) > 0

    # This is ordering 4 in the source authors' list of 26 relevant orders.
    c_order = (10, 9, 3, 1, 7, 4, 2, 5, 6, 8)
    c = symmetric_matricization(c_order)
    assert c == [[1188, 660, 1000, 1000],
                 [660, 1406, 1000, 1000],
                 [1000, 1000, 1406, 703],
                 [1000, 1000, 703, 1320]]
    assert det_int(c) == -337300392

    print("weights:", WEIGHTS)
    print("normalizing denominator:", DENOMINATOR)
    print("M6=M13 leading principal minors:", a_minors)
    print("M11=M12 leading principal minors:", b_minors)
    print("ordering-4 determinant:", det_int(c))
    print("all exact checks passed")


if __name__ == "__main__":
    main()
