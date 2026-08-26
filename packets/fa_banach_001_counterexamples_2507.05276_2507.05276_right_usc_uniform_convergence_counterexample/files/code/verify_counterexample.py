#!/usr/bin/env python3
"""Finite exact-arithmetic checks for the countdown-ultrametric example.

The mathematical proof is symbolic.  This script checks large finite
truncations for transcription/indexing mistakes; it is not used as proof of
the infinite assertions.
"""

from fractions import Fraction


def radius(k: int) -> Fraction:
    if k == 0:
        return Fraction(0)
    return Fraction(k, k + 1)


def distance(j: int, k: int) -> Fraction:
    if j == k:
        return Fraction(0)
    return radius(max(j, k))


def iterate(k: int, n: int) -> int:
    return max(k - n, 0)


def phi_at_radius(k: int) -> Fraction:
    if k == 0:
        return Fraction(0)
    if k == 1:
        return Fraction(1, 4)
    return radius(k - 1)


def main() -> None:
    max_index = 80
    max_iterate = 40

    # Ultrametric inequality on a finite truncation.
    for i in range(max_index + 1):
        for j in range(max_index + 1):
            for k in range(max_index + 1):
                assert distance(i, k) <= max(distance(i, j), distance(j, k))

    # Every positive iterate obeys the same control phi on all realized
    # distances in the truncation.
    for n in range(1, max_iterate + 1):
        for j in range(max_index + 1):
            for k in range(max_index + 1):
                lhs = distance(iterate(j, n), iterate(k, n))
                rhs = phi_at_radius(max(j, k)) if j != k else Fraction(0)
                assert lhs <= rhs

    # Explicit witnesses against uniform convergence: T^n x_{n+4}=x_4,
    # whose distance from the fixed point is 4/5.
    for n in range(max_iterate + 1):
        witness = iterate(n + 4, n)
        assert witness == 4
        assert distance(witness, 0) == Fraction(4, 5)

    print(
        "verified: ultrametric triples through index 80; "
        "all contraction inequalities for iterates 1..40; "
        "non-uniform witnesses for n=0..40"
    )


if __name__ == "__main__":
    main()
