#!/usr/bin/env python3
"""Exact arithmetic audit of the constants in the nested-hole proof."""

from fractions import Fraction


def main() -> None:
    q = Fraction(1, 8)

    # The uniform-hole construction: start within R/4 of the center, move
    # R/2 in an almost norming direction, and retain a ball of radius R/8.
    containment = Fraction(1, 4) + Fraction(1, 2) + q
    separator_gain = Fraction(3, 4) * Fraction(1, 2) - q
    assert containment == Fraction(7, 8) < 1
    assert separator_gain == Fraction(1, 4)
    assert separator_gain == 2 * q

    checks = 3
    for integer_radius in range(1, 51):
        radius_zero = Fraction(integer_radius)
        for k in range(1, 201):
            radius_k = radius_zero * q**k
            radius_next = radius_zero * q ** (k + 1)
            level_gap = radius_zero * q ** (2 * k)

            # A kth hole has distance margin R_{k-1}/4 = 2 R_k.
            assert radius_zero * q ** (k - 1) / 4 == 2 * radius_k

            # The final difference quotient is bounded by q^(k-1).
            assert level_gap / radius_next == q ** (k - 1)
            assert level_gap / radius_next <= 1
            checks += 3

    print(f"passed {checks:,} exact constant and rate checks")


if __name__ == "__main__":
    main()
