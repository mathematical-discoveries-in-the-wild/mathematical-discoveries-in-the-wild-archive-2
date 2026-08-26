#!/usr/bin/env python3
"""Numerically audit the dimensionless Rauch comparison constant."""

import math


def mesh(a: float) -> float:
    return 0.25 if a == 0.0 else a / (4.0 * math.sinh(a))


def ratio(q: float, delta: float) -> float:
    return delta if q == 0.0 else delta * math.sinh(q) / q


def main() -> None:
    tested = 0
    worst = 0.0
    for a in [0.0, 0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 12.0]:
        delta = mesh(a)
        for j in range(1001):
            q = a * j / 1000.0
            value = ratio(q, delta)
            assert value <= 0.25 + 1e-12, (a, q, value)
            worst = max(worst, value)
            tested += 1
        if a > 0:
            assert abs(ratio(a, delta) - 0.25) < 1e-12
    print(f"dimensionless angular samples passed: {tested}")
    print(f"worst distance/time ratio: {worst:.12f}")


if __name__ == "__main__":
    main()

