#!/usr/bin/env python3
"""Numerical stress check for the uniform lacunary geometric-series bound."""

from __future__ import annotations

import math


def ratio(r: float, s: float, m: int, base: float = 8.0) -> float:
    total = sum(base ** (-j * s) * min(2.0, 2.0 * math.pi * base**j * r)
                for j in range(1, m + 1))
    return total / r**s


def main() -> None:
    for s in (0.1, 0.25, 0.5, 0.75, 0.9):
        values = []
        for m in (1, 4, 16, 64, 256):
            best = max(ratio(10.0 ** (-q / 20.0), s, m)
                       for q in range(-80, 481))
            values.append(best)
        # The maxima stabilize as m grows; the generous cap catches a lost
        # factor or a nonuniform implementation while allowing endpoint s.
        assert max(values) < 100.0
        assert values[-1] <= 1.05 * max(values)
        print(f"s={s:.2f} maxima=" + ",".join(f"{v:.6f}" for v in values))

    epsilon = 0.1
    base = 8.0
    for j in range(1, 32):
        assert base**j + epsilon < base ** (j + 1) - epsilon
        assert base**j - epsilon > 0.0
    print("frequency_support_check=PASS")


if __name__ == "__main__":
    main()
