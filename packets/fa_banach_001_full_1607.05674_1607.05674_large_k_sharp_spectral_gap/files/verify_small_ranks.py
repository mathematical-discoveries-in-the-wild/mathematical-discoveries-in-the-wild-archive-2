"""Exact small-rank sanity check for the sharp spectral-gap formula.

This is not part of the proof.  It enumerates partitions with bounded first
row, evaluates skew Schur functions at 1^ell by Jacobi--Trudi, and divides by
Weyl's dimension formula.
"""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    answer = Fraction(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            answer = -answer
        value = a[i][i]
        answer *= value
        for j in range(i + 1, len(a)):
            a[i][j] /= value
        for j in range(i + 1, len(a)):
            value = a[j][i]
            if value:
                for q in range(i + 1, len(a)):
                    a[j][q] -= value * a[i][q]
    assert answer.denominator == 1
    return answer.numerator


def complete_homogeneous(ell, degree):
    if degree < 0:
        return 0
    if degree == 0:
        return 1
    return comb(ell + degree - 1, degree)


def skew_schur_at_ones(partition, subpartition, ell):
    n = len(partition)
    return determinant(
        [
            [
                complete_homogeneous(
                    ell, partition[i] - subpartition[j] - i + j
                )
                for j in range(n)
            ]
            for i in range(n)
        ]
    )


def weyl_dimension(partition):
    n = len(partition)
    answer = Fraction(1)
    for i in range(n):
        for j in range(i + 1, n):
            answer *= Fraction(partition[i] - partition[j] + j - i, j - i)
    assert answer.denominator == 1
    return answer.numerator


def check(max_n=9, max_part=5):
    for n in range(2, max_n + 1):
        for k in range((n + 1) // 2, n):
            ell = n - k
            best = Fraction(0)
            witnesses = []
            for increasing in combinations_with_replacement(range(max_part + 1), n - 1):
                partition = tuple(reversed(increasing)) + (0,)
                for d in range(partition[k - 1] + 1):
                    if partition == (0,) * n and d == 0:
                        continue
                    if partition == (1,) + (0,) * (n - 1) and d == 0:
                        continue
                    if partition == (1,) * (n - 1) + (0,) and d == 1:
                        continue
                    subpartition = (d,) * k + (0,) * ell
                    numerator = skew_schur_at_ones(partition, subpartition, ell)
                    if not numerator:
                        continue
                    value = Fraction(numerator, weyl_dimension(partition))
                    if value > best:
                        best = value
                        witnesses = [(partition, d)]
                    elif value == best:
                        witnesses.append((partition, d))
            expected = Fraction(ell * (ell + 1), n * (n + 1))
            assert best == expected, (n, k, best, expected, witnesses)
            print(f"n={n:2d} k={k:2d} max={best} witnesses={witnesses[:3]}")


if __name__ == "__main__":
    check()
