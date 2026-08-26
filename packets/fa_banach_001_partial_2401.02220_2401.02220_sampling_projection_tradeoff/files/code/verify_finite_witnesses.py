#!/usr/bin/env python3
"""Finite exact checks for the 2401.02220 sampling-tradeoff packet."""

from fractions import Fraction
from math import floor, sqrt


def hyperplane_projection_row_norms(q: int) -> list[int]:
    # Sampling coordinates 0,...,q-1 uniquely reconstructs H_q. The first q
    # output rows copy one coordinate; the last is minus their sum.
    return [1] * q + [q]


def check_hyperplanes() -> None:
    for q in range(1, 13):
        rows = hyperplane_projection_row_norms(q)
        assert max(rows) == q
        # The omitted coordinate on the all-ones sample vector attains q.
        omitted = -sum([1] * q)
        assert abs(omitted) == q


def check_blocks() -> None:
    for n in range(2, 101):
        for k in range(1, n + 1):
            blocks = k + 1
            q = floor(n / blocks)
            leftovers = n - blocks * q
            compulsory = blocks * q + leftovers
            assert compulsory == n
            # Giving every hard block an additional sample would require
            # k+1 extras, one more than the budget.
            assert compulsory + blocks > n + k
            assert q == floor(Fraction(n, k + 1))


def check_scalar_upper_bound() -> None:
    for n in range(2, 101):
        for k in range(2, n + 1):
            m = n + k
            d = n + 1
            exact_ratio = (sqrt(m) + sqrt(d)) / (sqrt(m) - sqrt(d))
            simple_ratio = 4 * m / (m - d)
            assert exact_ratio <= simple_ratio + 1e-12
            exact_bound = sqrt(n + 2) * exact_ratio
            simple_bound = 4 * (n + k) * sqrt(n + 2) / (k - 1)
            assert exact_bound <= simple_bound + 1e-10


def main() -> None:
    check_hyperplanes()
    check_blocks()
    check_scalar_upper_bound()
    print("all finite sampling-tradeoff checks passed")


if __name__ == "__main__":
    main()
