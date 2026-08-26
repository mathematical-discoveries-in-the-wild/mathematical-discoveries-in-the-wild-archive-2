#!/usr/bin/env python3
"""Deterministic sanity checks for the oscillatory-shear counterexample."""

from __future__ import annotations

import math


def g(t: float) -> float:
    return 0.0 if t == 0.0 else t * t * math.sin(1.0 / t)


def gprime(t: float) -> float:
    return 2.0 * t * math.sin(1.0 / t) - math.cos(1.0 / t)


def h(x: float, y: float) -> tuple[float, float]:
    return x + g(y), y


def hinv(u: float, v: float) -> tuple[float, float]:
    return u - g(v), v


def main() -> None:
    slopes = (-4.0, -1.0, -0.25, 0.0, 0.25, 1.0, 4.0)
    checked = 0
    for n in range(1, 501):
        t_minus = 1.0 / (2.0 * math.pi * n)
        t_plus = 1.0 / ((2 * n + 1) * math.pi)
        assert abs(gprime(t_minus) + 1.0) < 2e-12
        assert abs(gprime(t_plus) - 1.0) < 2e-12
        for c in slopes:
            observed = max(abs(gprime(t_minus) - c), abs(gprime(t_plus) - c))
            assert observed >= 1.0 + abs(c) - 2e-12
            checked += 1

    inverse_checks = 0
    for i in range(101):
        for j in range(101):
            x, y = i / 100.0, j / 100.0
            xx, yy = hinv(*h(x, y))
            assert abs(xx - x) < 2e-15 and yy == y
            inverse_checks += 1

    print(f"oscillatory slope checks: {checked}")
    print(f"shear/inverse grid checks: {inverse_checks}")
    print("all checks passed")


if __name__ == "__main__":
    main()
