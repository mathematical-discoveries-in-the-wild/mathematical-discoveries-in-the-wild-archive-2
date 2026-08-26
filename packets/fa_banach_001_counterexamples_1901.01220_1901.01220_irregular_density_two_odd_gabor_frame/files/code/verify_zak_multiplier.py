#!/usr/bin/env python3
"""Numerical regression check for the exact Zak-multiplier proof.

The theorem is proved analytically in main.tex. This script only samples the
closed piecewise formula and checks the modular zero classes.
"""

from __future__ import annotations

import math


def g(t: float) -> float:
    if abs(t) >= 0.5:
        return 0.0
    return t * math.exp(-1.0 / (1.0 - 4.0 * t * t))


def zak_abs_squared(x: float) -> float:
    """|Zg(x,w)|^2; it is independent of w for this one-term formula."""
    r = x % 1.0
    if 0.0 < r < 0.5:
        return g(r) ** 2
    if 0.5 < r < 1.0:
        return g(r - 1.0) ** 2
    return 0.0


def multiplier(x: float) -> float:
    return zak_abs_squared(x) + zak_abs_squared(x - 0.25)


def main() -> None:
    zero_classes = {0.0, 0.5}
    translated_zero_classes = {0.25, 0.75}
    assert zero_classes.isdisjoint(translated_zero_classes)
    for x in zero_classes:
        assert zak_abs_squared(x) == 0.0
        assert zak_abs_squared(x - 0.25) > 0.0
    for x in translated_zero_classes:
        assert zak_abs_squared(x - 0.25) == 0.0
        assert zak_abs_squared(x) > 0.0

    samples = 200_000
    values = [multiplier(j / samples) for j in range(samples)]
    lower = min(values)
    upper = max(values)
    argmin = values.index(lower) / samples
    assert lower > 0.0
    print(f"samples={samples}")
    print(f"sampled_lower={lower:.16g} at x={argmin:.8f}")
    print(f"sampled_upper={upper:.16g}")
    print("zero classes disjoint: yes")
    print("periodic motif count per unit cell: 2")


if __name__ == "__main__":
    main()
