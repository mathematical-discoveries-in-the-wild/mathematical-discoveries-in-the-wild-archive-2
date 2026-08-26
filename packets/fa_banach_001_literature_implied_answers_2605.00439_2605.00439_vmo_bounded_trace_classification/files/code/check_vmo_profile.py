#!/usr/bin/env python3
"""Numerical sanity checks for the radial CMO example; not part of the proof."""

from __future__ import annotations

import math


A = math.exp(math.e)


def h(radius: float) -> float:
    return math.log(math.log(A + radius))


def centered_mean_oscillation(radius: float, dimension: int, steps: int = 200_000) -> float:
    # Under normalized measure on B(0,R), y=-log(|x|/R) is exponential
    # with rate n. Midpoint quadrature after truncating an exponentially tiny tail.
    cutoff = 30.0 / dimension
    delta = cutoff / steps
    values = []
    weights = []
    for index in range(steps):
        y = (index + 0.5) * delta
        weight = dimension * math.exp(-dimension * y) * delta
        values.append(h(radius * math.exp(-y)))
        weights.append(weight)
    total_weight = sum(weights)
    mean = sum(v * w for v, w in zip(values, weights)) / total_weight
    return sum(abs(v - mean) * w for v, w in zip(values, weights)) / total_weight


def analytic_comparison_bound(radius: float, dimension: int) -> float:
    level = math.log(A + radius)
    tail = max(0.0, math.log(level / math.e)) * math.exp(-dimension * level / 2.0)
    # Mean oscillation is at most twice the average distance from h(R).
    return 2.0 * (2.0 / (dimension * level) + tail)


def main() -> None:
    for dimension in (1, 2, 5):
        print(f"dimension={dimension}")
        previous = None
        for radius in (1e2, 1e4, 1e8, 1e16):
            oscillation = centered_mean_oscillation(radius, dimension)
            bound = analytic_comparison_bound(radius, dimension)
            assert oscillation <= bound * 1.001
            if previous is not None:
                assert oscillation < previous
            previous = oscillation
            print(f"  R={radius:.0e}  MO={oscillation:.8g}  proof_bound={bound:.8g}")
    print("all centered-profile checks passed")


if __name__ == "__main__":
    main()
