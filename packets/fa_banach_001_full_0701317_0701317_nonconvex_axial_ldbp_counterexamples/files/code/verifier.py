#!/usr/bin/env python3
"""Sanity checks for the parameter inequalities in the 0701317 packet.

This script does not verify the cosine-transform or Radon-transform theorems.
It checks the elementary algebra used to choose epsilon, the sign of the
degree-two representing density at the block axis, and the negative polar
curvature of the explicit star body.
"""

from __future__ import annotations

import math


def check_case(n: int, ell: int, step: int) -> None:
    i = ell + step
    k = n - i
    lower = k * n / (i * (n - ell))
    upper = n / ell
    epsilon = (lower + upper) / 2.0

    assert 1 <= ell <= n / 2
    assert i + ell <= n
    assert step in (1, 2)
    assert k >= ell >= 1
    assert 0.0 < lower < epsilon < upper

    # rho_B^k = a + epsilon*t, 0 <= t <= 1.
    a = 1.0 - epsilon * ell / n
    assert a > 0.0

    # M^(1-i) multiplies the degree-two harmonic by -i/k relative
    # to the constant harmonic.
    density_at_block_axis = 1.0 - epsilon * (i / k) * (1.0 - ell / n)
    assert density_at_block_axis < 0.0

    # At the complementary axis, the polar curvature numerator is
    # a^(2/k-1) * (a - 2*epsilon/k), so only the last factor matters.
    curvature_sign_factor = a - 2.0 * epsilon / k
    assert curvature_sign_factor < 0.0

    # Directly sample the positive radial-power profile.
    for j in range(201):
        omega = (math.pi / 2.0) * j / 200.0
        radial_power = a + epsilon * math.sin(omega) ** 2
        assert radial_power > 0.0


def main() -> None:
    checked = 0
    examples: list[tuple[int, int, int]] = []
    for n in range(3, 101):
        for ell in range(1, n // 2 + 1):
            for step in (1, 2):
                i = ell + step
                if i <= n - 1 and i + ell <= n:
                    check_case(n, ell, step)
                    checked += 1
                    if len(examples) < 6:
                        examples.append((n, ell, i))

    print(f"checked {checked} admissible (n, ell, i) triples with 3 <= n <= 100")
    print("first cases:", examples)
    print("all positivity, density-sign, and curvature-sign checks passed")


if __name__ == "__main__":
    main()
