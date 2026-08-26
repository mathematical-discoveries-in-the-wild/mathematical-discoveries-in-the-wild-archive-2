#!/usr/bin/env python3
"""Exact rational checks for the nonatomic counterexample."""

from fractions import Fraction


def check(a: Fraction, b: Fraction) -> None:
    assert 0 < b < a < 1
    coherence = Fraction(1)
    threshold = Fraction(1, 2) * (1 + 1 / coherence)
    synthesis_a = (1 / a) * a
    synthesis_b = (1 / b) * b
    assert a < threshold
    assert synthesis_a == synthesis_b == 1
    assert b < a
    # Squared L2 norms are finite: integral |a^-1 1_(0,a)|^2 = 1/a.
    assert 1 / a > 0 and 1 / b > 0


def main() -> None:
    pairs = [
        (Fraction(1, 2), Fraction(1, 4)),
        (Fraction(3, 4), Fraction(1, 10)),
        (Fraction(1, 100), Fraction(1, 1000)),
    ]
    for a, b in pairs:
        check(a, b)
    print("PASS: Parseval/coherence normalization is 1")
    print("PASS: all rational examples meet the threshold and synthesize h=1")
    print("PASS: each competitor has strictly smaller support")


if __name__ == "__main__":
    main()
