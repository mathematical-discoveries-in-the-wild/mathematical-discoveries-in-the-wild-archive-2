#!/usr/bin/env python3
"""Exact finite checks for the trace-identity mechanism.

This audits Amitsur--Levitzki on small random integer matrices, the explicit
sharpness witness in M_{r+1}, and the nonvanishing unit-expansion coefficient.
It is not used as proof.
"""

from itertools import permutations
from math import comb
import random
import numpy as np


def parity(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def standard_polynomial(mats):
    n = mats[0].shape[0]
    out = np.zeros((n, n), dtype=object)
    for perm in permutations(range(len(mats))):
        prod = np.eye(n, dtype=object)
        for j in perm:
            prod = prod @ mats[j]
        out += parity(perm) * prod
    return out


def matrix_unit(n, i, j):
    a = np.zeros((n, n), dtype=object)
    a[i, j] = 1
    return a


def chain_witness(r):
    n = r + 1
    mats = []
    for j in range(r):
        mats.append(matrix_unit(n, j, j))
        mats.append(matrix_unit(n, j, j + 1))
    return mats


def binom0(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def unit_coefficient(m, r):
    k = 2 * r + 1
    return k * binom0(m, k) + (k - 1) * binom0(m, k - 1)


def main():
    rng = random.Random(20260817)
    for r in range(1, 5):
        random_mats = [
            np.array([[rng.randint(-2, 2) for _ in range(r)] for _ in range(r)], dtype=object)
            for _ in range(2 * r)
        ]
        assert np.all(standard_polynomial(random_mats) == 0)

        witness = standard_polynomial(chain_witness(r))
        expected = matrix_unit(r + 1, 0, r)
        assert np.array_equal(witness, expected)
        marker = matrix_unit(r + 1, r, 0)
        assert np.trace(witness @ marker) == 1

        assert unit_coefficient(2 * r, r) == 2 * r

    print("PASS: S_{2r}=0 in sampled M_r cases for r=1,...,4")
    print("PASS: explicit M_{r+1} chain witness gives e_{1,r+1}")
    print("PASS: boundary unit coefficient C_{2r,2r+1,1}=2r is nonzero")


if __name__ == "__main__":
    main()
