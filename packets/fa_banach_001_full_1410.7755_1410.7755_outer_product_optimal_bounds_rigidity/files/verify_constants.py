#!/usr/bin/env python3
"""Exact arithmetic audit for the constants in the rigidity proof."""

from fractions import Fraction


def main() -> None:
    cases = 0
    for n in range(2, 80):
        for m in range(n + 1, 81):
            alpha = Fraction(m * (n - 1), n * (m - 1))
            beta = Fraction(m, n)
            c = Fraction(m - n, n * (m - 1))
            assert 1 - c == alpha
            assert 1 + (m - 1) * c == beta
            assert (beta - alpha) / m == c
            assert (1 - alpha) / (beta - alpha) == Fraction(1, m)
            assert beta - alpha == m * c
            assert m + m * (m - 1) * c == Fraction(m * m, n)
            cases += 1
    print(f"verified {cases} exact parameter pairs")


if __name__ == "__main__":
    main()

