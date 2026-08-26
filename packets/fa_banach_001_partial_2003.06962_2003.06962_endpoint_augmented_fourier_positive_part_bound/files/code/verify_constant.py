#!/usr/bin/env python3
"""Exact checkpoint plus a non-proof numerical scan for the packet constant."""

from __future__ import annotations

import math
from fractions import Fraction


def sinc(y: float) -> float:
    return 1.0 if y == 0.0 else math.sin(y) / y


def multiplier(y: float) -> float:
    return (2.0 / 3.0) * (2.0 + math.cos(y) - 3.0 * sinc(y))


def main() -> None:
    r = Fraction(144, 25)
    z_lower = Fraction(693, 1325)  # from pi > 333/106
    tangent_lower = (
        z_lower
        + z_lower**3 / 3
        + 2 * z_lower**5 / 15
    )
    tangent_target = 3 * r / (r * r - 3)
    difference = tangent_lower - tangent_target
    assert difference > 0

    proved_upper = (96.0 + math.sqrt(2929.0)) / 72.0
    proved_lower = 1.0 / proved_upper

    step = 0.0001
    count = 800_001
    best_value = -math.inf
    best_y = 0.0
    for index in range(count):
        y = index * step
        value = multiplier(y)
        if value > best_value:
            best_value = value
            best_y = y

    print(f"exact rational checkpoint = {difference}")
    print(f"proved sup(K) upper bound = {proved_upper:.15f}")
    print(f"proved positive-part lower bound = {proved_lower:.15f}")
    print(f"grid cases = {count}, interval = [0, {step*(count-1):.1f}]")
    print(f"grid max(K) = {best_value:.15f} at y = {best_y:.4f}")
    assert best_value < proved_upper


if __name__ == "__main__":
    main()
