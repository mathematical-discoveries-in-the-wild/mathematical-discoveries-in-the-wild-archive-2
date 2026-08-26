#!/usr/bin/env python3
"""Finite exact and numerical checks for the MBI-not-MLIM packet.

The infinite-dimensional argument is proved in main.tex.  This companion
checks the scalar invariant identities, the explicit K_infinity modulus, and
long finite prefixes of the tail trajectory.
"""

from fractions import Fraction
from math import sqrt


def g(t: float) -> float:
    return t * t if t <= 1.0 else (t + 1.0) / 2.0


def xi(t: float) -> float:
    return 6.0 * t if t <= 0.25 else 1.0 + 2.0 * t


def shift_prefix(x: list[float]) -> list[float]:
    return [0.0] + [g(t) for t in x[:-1]]


def main() -> None:
    # The two pieces of xi agree exactly at 1/4.
    d = Fraction(1, 4)
    assert 6 * d == 1 + 2 * d == Fraction(3, 2)

    # For the large-input invariant interval B=1+2d, g(B)+d=B.
    for d in [Fraction(1, 4), Fraction(1, 3), Fraction(1), Fraction(7, 2)]:
        B = 1 + 2 * d
        assert B >= 1
        assert (B + 1) / 2 + d == B

    # For the small-input invariant interval alpha, alpha^2+d=alpha and
    # alpha<=2d.  Iterating the maximal recurrence never leaves it.
    for d in [0.0, 1e-6, 0.01, 0.1, 0.249999, 0.25]:
        alpha = (1.0 - sqrt(1.0 - 4.0 * d)) / 2.0
        assert abs(alpha * alpha + d - alpha) < 2e-12
        assert d <= alpha + 2e-12
        assert alpha <= 2.0 * d + 2e-12
        value = d
        for _ in range(10000):
            value = g(value) + d
            assert value <= alpha + 2e-10
        assert value <= xi(d) + 2e-10

    # The explicit large-input bound is invariant for maximal recurrences.
    for d in [0.250001, 0.3, 1.0, 10.0]:
        B = 1.0 + 2.0 * d
        value = d
        for _ in range(10000):
            value = g(value) + d
            assert value <= B + 2e-10
        assert abs(B - xi(d)) < 1e-12

    # Every finite window of a tail indicator is shifted by one coordinate.
    # Extra ones prevent the artificial right boundary from entering the test.
    width = 200
    for k in range(50):
        xk = [0.0] * k + [1.0] * (width + 2 - k)
        shifted = shift_prefix(xk)
        expected = [0.0] * (k + 1) + [1.0] * (width + 1 - k)
        assert shifted == expected
        assert max(xk) == max(shifted) == 1.0
        assert all(b <= a for a, b in zip(xk, shifted))

    print("all scalar MBI and tail-trajectory checks passed")


if __name__ == "__main__":
    main()
