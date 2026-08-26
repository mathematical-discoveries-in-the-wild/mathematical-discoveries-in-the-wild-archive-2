#!/usr/bin/env python3
"""Exponent and finite phase checks for the coherent wave-packet proof."""

from fractions import Fraction
import math


def main() -> None:
    alpha = Fraction(3, 4)
    packet_power = 1 - alpha / 2
    forced_gamma = packet_power / 4
    proposed_gamma = (1 - alpha) / 4

    assert 0 < alpha < 1
    assert packet_power == Fraction(5, 8)
    assert forced_gamma == Fraction(5, 32)
    assert proposed_gamma == Fraction(1, 16)
    assert forced_gamma - proposed_gamma == alpha / 8

    # Representative finite packet: verify Taylor remainder and phase arc.
    n = 10**8
    delta = 0.1
    m = int(delta * n ** float(packet_power))
    max_remainder = 0.0
    for j in range(m):
        rem = abs((n + j) ** float(alpha) - n ** float(alpha)
                  - float(alpha) * n ** (float(alpha) - 1) * j)
        max_remainder = max(max_remainder, rem)

    analytic_bound = (float(alpha) * (1 - float(alpha)) / 2
                      * n ** (float(alpha) - 2) * m**2)
    assert max_remainder <= analytic_bound * (1 + 1e-8)
    assert delta + analytic_bound < math.pi / 3

    print("coherent wave-packet checks passed")
    print(f"alpha={alpha}, packet power={packet_power}")
    print(f"forced gamma={forced_gamma}, proposed gamma={proposed_gamma}")
    print(f"N={n}, M={m}, max remainder={max_remainder:.8g}")
    print(f"analytic remainder bound={analytic_bound:.8g}")


if __name__ == "__main__":
    main()
