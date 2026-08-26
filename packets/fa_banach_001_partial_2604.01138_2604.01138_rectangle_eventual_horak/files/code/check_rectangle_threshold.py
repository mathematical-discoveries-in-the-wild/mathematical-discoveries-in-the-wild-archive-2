#!/usr/bin/env python3
"""Numerically audit the geometry and explicit finite-p comparison."""

from __future__ import annotations

import math


SAMPLES = (1.01, 1.10, 1.25, 1.50, 1.75, 1.90, 1.99)


def radius(a: float) -> float:
    return (a + 1.0 - math.sqrt(2.0 * a)) / 2.0


def log_ratio(a: float, p: int) -> float:
    """Log of upper-bound/lower-bound ratio in the theorem."""
    r = radius(a)
    rho = a / (4.0 * r)
    return (
        math.log(p + 1.0)
        + math.log(p + 2.0)
        - math.log(2.0)
        - math.log(p - 1.0)
        + p * math.log(rho)
    )


def first_passing_integer(a: float) -> int:
    low = 1
    high = 2
    while log_ratio(a, high) >= 0.0:
        low = high
        high *= 2
    while high - low > 1:
        middle = (low + high) // 2
        if log_ratio(a, middle) < 0.0:
            high = middle
        else:
            low = middle
    return high


def main() -> None:
    checks = 0
    tolerance = 2e-12

    # Dense grid on 1<a<2: placement, tangency, and exponential gap.
    for index in range(1, 10_000):
        a = 1.0 + index / 10_000.0
        r = radius(a)
        rho = a / (4.0 * r)
        assert a / 4.0 < r < 0.5
        checks += 1
        tangency_error = abs((a - 2.0 * r) ** 2 + (1.0 - 2.0 * r) ** 2 - 4.0 * r**2)
        assert tangency_error <= tolerance
        checks += 1
        assert 0.0 < rho < 1.0
        checks += 1

    print("a       r_a          rho_a        first integer p passing")
    for a in SAMPLES:
        r = radius(a)
        rho = a / (4.0 * r)
        p = first_passing_integer(a)
        assert log_ratio(a, p) < 0.0
        checks += 1
        assert p == 2 or log_ratio(a, p - 1) >= 0.0
        checks += 1
        print(f"{a:4.2f}   {r:0.9f}  {rho:0.9f}   {p}")

    print(f"passed {checks:,} geometry and threshold checks")


if __name__ == "__main__":
    main()
