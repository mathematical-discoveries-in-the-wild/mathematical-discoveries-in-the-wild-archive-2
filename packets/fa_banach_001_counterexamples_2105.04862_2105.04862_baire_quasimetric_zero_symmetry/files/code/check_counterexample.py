#!/usr/bin/env python3
"""Finite sanity checks for the quasi-metric counterexample.

The universal proof is in ../main.tex. These tests are not a proof.
"""

from __future__ import annotations

import math
import random


def positive_part(value: float) -> float:
    return max(value, 0.0)


def d(x: float, y: float) -> float:
    return positive_part(y - x) + positive_part(math.exp(-y) - math.exp(-x))


def ds_formula(x: float, y: float) -> float:
    return max(abs(x - y), abs(math.exp(-x) - math.exp(-y)))


def check_triple(x: float, y: float, z: float, tolerance: float = 1e-12) -> None:
    left = d(x, y)
    right = d(x, z) + d(z, y)
    rounding_allowance = tolerance * max(1.0, abs(left), abs(right))
    if left > right + rounding_allowance:
        raise AssertionError((x, y, z, left, right))


def main() -> None:
    grid = [-20, -10, -3, -1, -0.1, 0, 0.1, 0.5, 1, 2, 3, 10, 20]

    for x in grid:
        for y in grid:
            if (d(x, y) == 0.0) != (x == y):
                raise AssertionError(("separation", x, y, d(x, y)))
            expected = ds_formula(x, y)
            actual = max(d(x, y), d(y, x))
            if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError(("symmetrization", x, y, actual, expected))
            for z in grid:
                check_triple(x, y, z)

    rng = random.Random(210504862)
    for _ in range(100_000):
        x, y, z = (rng.uniform(-20.0, 20.0) for _ in range(3))
        check_triple(x, y, z, tolerance=1e-9)

    ratios = []
    for n in [0, 1, 2, 5, 10, 20, 40]:
        numerator = d(n + 1.0, n)
        denominator = d(n, n + 1.0)
        ratios.append((n, numerator / denominator))

    print("grid points:", len(grid))
    print("grid triples checked:", len(grid) ** 3)
    print("seeded random triples checked: 100000")
    print("symmetry ratios d(n+1,n)/d(n,n+1):")
    for n, ratio in ratios:
        print(f"  n={n:2d}: {ratio:.16g}")
    print("all checks passed")


if __name__ == "__main__":
    main()
