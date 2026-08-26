#!/usr/bin/env python3
"""Exact certificates for the non-multiple dilation proof.

All inequality checks use Fraction arithmetic.  Decimal output is explanatory;
the assertions themselves are exact rational comparisons.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import sqrt


def atan_bounds(x: F, last_index: int) -> tuple[F, F]:
    """Alternating-series lower/upper bounds through the given index."""
    partial = F(0)
    lowers: list[F] = []
    uppers: list[F] = []
    for n in range(last_index + 1):
        partial += (1 if n % 2 == 0 else -1) * x ** (2 * n + 1) / (2 * n + 1)
        (uppers if n % 2 == 0 else lowers).append(partial)
    return max(lowers), min(uppers)


def main() -> None:
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    a_lower, a_upper = atan_bounds(F(1, 5), 5)
    b_lower, b_upper = atan_bounds(F(1, 239), 5)
    pi_lower = 16 * a_lower - 4 * b_upper
    pi_upper = 16 * a_upper - 4 * b_lower
    assert pi_lower > F(314159, 100000)
    assert pi_upper < F(314160, 100000)

    # Alternating Taylor bounds, using monotonicity of sine on [0,pi/2].
    sin_intervals: list[tuple[F, F]] = []
    for multiplier, advertised_lower, advertised_upper in (
        (1, F(20791, 100000), F(20792, 100000)),
        (2, F(40673, 100000), F(40674, 100000)),
    ):
        x_lower = multiplier * F(314159, 100000) / 15
        x_upper = multiplier * F(314160, 100000) / 15
        lower = (
            x_lower
            - x_lower**3 / 6
            + x_lower**5 / 120
            - x_lower**7 / 5040
        )
        upper = x_upper - x_upper**3 / 6 + x_upper**5 / 120
        assert lower > advertised_lower
        assert upper < advertised_upper
        sin_intervals.append((advertised_lower, advertised_upper))

    root3_half_lower = F(86602, 100000)
    root3_half_upper = F(86603, 100000)
    assert root3_half_lower**2 < F(3, 4) < root3_half_upper**2

    # x=|a1| and y=a2.  These rational upper bounds follow from the
    # advertised intervals and pi>3.14159.
    x_upper = F(41898, 100000)
    y_lower = F(40512, 100000)
    y_upper = F(40514, 100000)
    direct_x_upper = (
        2 * (root3_half_upper - sin_intervals[0][0]) / F(314159, 100000)
    )
    direct_y_lower = (
        (root3_half_lower + sin_intervals[1][0]) / F(314160, 100000)
    )
    direct_y_upper = (
        (root3_half_upper + sin_intervals[1][1]) / F(314159, 100000)
    )
    assert direct_x_upper < x_upper
    assert direct_y_lower > y_lower
    assert direct_y_upper < y_upper

    # The antisymmetric eigenvalue has modulus 1/5+y < 0.60515.
    assert F(1, 5) + y_upper < F(60515, 100000)

    # For the symmetric eigenvalues, |a0+y/2|<0.00257 and
    # sqrt(y^2+8x^2)/2 < 0.62620, checked without irrational arithmetic.
    center_bound = F(257, 100000)
    half_root_bound = F(62620, 100000)
    assert abs(-F(1, 5) + y_lower / 2) <= center_bound
    assert abs(-F(1, 5) + y_upper / 2) <= center_bound
    assert y_upper**2 + 8 * x_upper**2 < (2 * half_root_bound) ** 2
    norm_upper = center_bound + half_root_bound
    assert norm_upper == F(62877, 100000)
    assert norm_upper * F(314160, 100000) < 2  # norm_upper < 2/pi

    # Arbitrary-size residue decomposition for k=floor(M/2).
    for matrix_level in range(4, 1001):
        dilation = matrix_level // 2
        block_levels = [
            (matrix_level - residue) // dilation
            for residue in range(dilation)
            if residue <= matrix_level
        ]
        assert block_levels[0] == 2
        assert max(block_levels) == 2
        assert 2 * dilation <= matrix_level

    print("certified 3.14159 < pi < 3.14160 by Machin series")
    print("certified sine and sqrt(3)/2 rational intervals")
    print("certified ||A_(psi,2)|| <", float(norm_upper))
    print("certified", float(norm_upper), "< 2/pi")
    print("checked residue block levels for every 4 <= N <= 1000")
    print("illustrative sharp numerical norm: 0.6287467313582313")
    print("PASS")


if __name__ == "__main__":
    main()
