#!/usr/bin/env python3
"""Exact rational checks for the exponent identities in the packet."""

from fractions import Fraction


def check(a: Fraction, c: Fraction, rp: Fraction, rq: Fraction) -> None:
    u, v = 1 - rp, 1 - rq
    paper = min(a, c) * min(u, v)
    coordinate = min(a * u, c * v)
    aligned = (a - c) * (u - v) >= 0
    assert (paper == coordinate) == aligned


def main() -> None:
    base = [Fraction(i, j) for j in range(1, 9) for i in range(1, 2 * j + 1)]
    ratios = [Fraction(i, j) for j in range(2, 10) for i in range(0, j)]
    checked = 0
    for a in base:
        for c in base:
            for rp in ratios:
                for rq in ratios:
                    check(a, c, rp, rq)
                    checked += 1
    print(f"checked {checked} rational parameter quadruples")


if __name__ == "__main__":
    main()
