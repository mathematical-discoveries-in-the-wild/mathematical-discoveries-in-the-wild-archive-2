#!/usr/bin/env python3
"""Finite-coordinate check of the exact Cesaro separation mechanism."""

from fractions import Fraction


def weights(n: int, length: int) -> list[Fraction]:
    return [Fraction(1, n) if 1 <= k <= n else Fraction(0) for k in range(1, length + 1)]


def main() -> None:
    for n in range(1, 101):
        a_n = weights(n, 2 * n)
        a_2n = weights(2 * n, 2 * n)
        diagonal_test = [Fraction(1) if k <= n else Fraction(-1) for k in range(1, 2 * n + 1)]
        value_n = sum(w * d for w, d in zip(a_n, diagonal_test))
        value_2n = sum(w * d for w, d in zip(a_2n, diagonal_test))
        l1_gap = sum(abs(x - y) for x, y in zip(a_n, a_2n))
        assert value_n == 1
        assert value_2n == 0
        assert l1_gap == 1
    print("verified exact Cesaro gap 1 for N=1,...,100")


if __name__ == "__main__":
    main()
