#!/usr/bin/env python3
"""Exact checks for the complete-homogeneous PBF formula.

The script verifies finite leading truncations with Fraction arithmetic.  It
is a normalization/regression check; the general result is proved symbolically
in the packet.
"""

from fractions import Fraction
from functools import reduce
from itertools import combinations


def matmul(a, b):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def identity(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def elementary(betas, degree):
    if degree == 0:
        return Fraction(1)
    return sum(
        (reduce(lambda x, y: x * y, terms, Fraction(1))
         for terms in combinations(betas, degree)),
        Fraction(0),
    )


def homogeneous_table(betas, max_degree):
    # h_n(x_1,...,x_m), initialized at m=0.
    h = [Fraction(1)] + [Fraction(0)] * max_degree
    for beta in betas:
        new = [Fraction(1)] + [Fraction(0)] * max_degree
        for n in range(1, max_degree + 1):
            new[n] = h[n] + beta * new[n - 1]
        h = new
    return h


def factors(betas, n):
    hs = [None]
    for m in range(1, len(betas) + 1):
        hs.append(homogeneous_table(betas[:m], n + 1))

    lowers = []
    for m in range(2, len(betas) + 1):
        lower = identity(n)
        for row in range(1, n):
            q_prev = hs[m - 1][row + 1] / hs[m - 1][row]
            q_new_before = hs[m][row] / hs[m][row - 1]
            lower[row][row - 1] = betas[m - 1] * q_prev / q_new_before
            assert lower[row][row - 1] > 0
        lowers.append(lower)

    upper = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    h_final = hs[len(betas)]
    for row in range(n):
        upper[row][row] = h_final[row + 1] / h_final[row]
        assert upper[row][row] > 0
        if row + 1 < n:
            upper[row][row + 1] = Fraction(1)
    return lowers, upper


def toeplitz_target(betas, n):
    r = len(betas) - 1
    target = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for row in range(n):
        if row + 1 < n:
            target[row][row + 1] = Fraction(1)
        for depth in range(r + 1):
            col = row - depth
            if col >= 0:
                target[row][col] = elementary(betas, depth + 1)
    return target


def check(betas, n=12):
    lowers, upper = factors(tuple(betas), n)
    product = identity(n)
    for lower in lowers:
        product = matmul(product, lower)
    product = matmul(product, upper)
    assert product == toeplitz_target(tuple(betas), n)


def main():
    cases = [
        (Fraction(2), Fraction(1)),
        (Fraction(3), Fraction(2), Fraction(1)),
        (Fraction(4), Fraction(3), Fraction(2), Fraction(1)),
        (Fraction(5, 2), Fraction(5, 2), Fraction(3, 2), Fraction(1, 3)),
        (Fraction(6), Fraction(5), Fraction(4), Fraction(3), Fraction(2), Fraction(1)),
    ]
    for betas in cases:
        check(betas)
    print("PASS: exact PBF identities and strict positivity verified")
    print("cases=5, truncation_size=12, maximum_subdiagonals=5")


if __name__ == "__main__":
    main()
