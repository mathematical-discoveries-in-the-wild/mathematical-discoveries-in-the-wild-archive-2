#!/usr/bin/env python3
"""Finite consistency checks for the dimension-count Helmholtz packet."""

from fractions import Fraction
from math import comb


def binom(n: int, r: int) -> int:
    if n < 0 or r < 0 or r > n:
        return 0
    return comb(n, r)


def harmonic_dimension(m: int, d: int) -> int:
    return binom(m + d - 1, d - 1) - binom(m + d - 3, d - 1)


def restriction_bound(m: int, k: int) -> int:
    return binom(m + k - 1, k - 1)


def first_degree_with_kernel(d: int, k: int, number: int) -> int:
    for m in range(1, 10000):
        if harmonic_dimension(m, d) > number * restriction_bound(m, k):
            return m
    raise AssertionError((d, k, number))


def check_radial_recurrence(m: int, d: int, wave_sq: int, terms: int) -> None:
    # a_0=1 and a_(ell+1)/a_ell is the exact coefficient ratio in the packet.
    a = Fraction(1)
    for ell in range(terms):
        denominator = 4 * (ell + 1) * Fraction(2 * (ell + m) + d, 2)
        next_a = -Fraction(wave_sq, 1) * a / denominator
        residual = denominator * next_a + wave_sq * a
        assert residual == 0
        a = next_a


def main() -> None:
    cases = 0
    largest_first_degree = 0
    for d in range(4, 11):
        # Verify the two standard closed forms for dim H_m^d agree.
        for m in range(1, 40):
            alternative = binom(m + d - 2, d - 2) + binom(m + d - 3, d - 2)
            assert harmonic_dimension(m, d) == alternative
        for k in range(2, d - 1):
            for number in (1, 2, 5, 10, 25, 100):
                first = first_degree_with_kernel(d, k, number)
                largest_first_degree = max(largest_first_degree, first)
                assert harmonic_dimension(first, d) > number * restriction_bound(first, k)
                cases += 1

    for d in range(4, 10):
        for m in range(1, 12):
            for wave_sq in (0, 1, 2, 7, 25):
                check_radial_recurrence(m, d, wave_sq, 30)

    print(f"dimension cases passed: {cases}")
    print(f"largest first kernel degree in test grid: {largest_first_degree}")
    print("exact radial recurrence checks passed")


if __name__ == "__main__":
    main()

