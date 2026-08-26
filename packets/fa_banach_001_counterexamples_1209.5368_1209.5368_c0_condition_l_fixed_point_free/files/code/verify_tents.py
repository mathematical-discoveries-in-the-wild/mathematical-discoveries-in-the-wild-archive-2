#!/usr/bin/env python3
"""Numerical sanity checks for the moving-tent counterexample.

This script does not replace any infinite-dimensional proof.  It checks
finite samples of the explicit formulas and the inequalities used in it.
"""

from __future__ import annotations

import math
import random

import numpy as np


def center(n: int) -> int:
    return n**4


def width(n: int) -> float:
    return n ** 3.5


def tent(n: int, coordinates: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, 1.0 - np.abs(coordinates - center(n)) / width(n))


def exact_sampled_step(n: int) -> float:
    lo = max(1, math.floor(min(center(n) - width(n), center(n + 1) - width(n + 1))))
    hi = math.ceil(max(center(n) + width(n), center(n + 1) + width(n + 1)))
    coordinates = np.arange(lo, hi + 1, dtype=np.float64)
    return float(np.max(np.abs(tent(n + 1, coordinates) - tent(n, coordinates))))


def analytic_step_bound(n: int) -> float:
    return (center(n + 1) - center(n)) / width(n + 1) + 1.0 - width(n) / width(n + 1)


def sparse_step(n: int) -> float:
    """Maximize on integer coordinates using the piecewise-linear knots."""
    knots = []
    for m in (n, n + 1):
        knots.extend((center(m) - width(m), center(m), center(m) + width(m)))
    coordinates: set[int] = {1}
    for knot in knots:
        coordinates.update((max(1, math.floor(knot)), max(1, math.ceil(knot))))
    values = np.array(sorted(coordinates), dtype=np.float64)
    return float(np.max(np.abs(tent(n + 1, values) - tent(n, values))))


def finite_orbit(max_n: int, coordinates: np.ndarray) -> list[np.ndarray]:
    return [tent(n, coordinates) for n in range(1, max_n + 1)]


def main() -> None:
    steps = [exact_sampled_step(n) for n in range(2, 23)]
    bounds = [analytic_step_bound(n) for n in range(2, 23)]
    for n, step, bound in zip(range(2, 23), steps, bounds):
        assert 0.0 < step <= bound + 2e-14, (n, step, bound)

    # Cross-check the knot method against exhaustive integer sampling, then
    # use it at scales too large for dense arrays.  Monotonicity is not used.
    for n, step in zip(range(2, 23), steps):
        assert abs(sparse_step(n) - step) < 2e-12
    late_steps = {n: sparse_step(n) for n in (100, 1000, 10_000)}
    assert late_steps[10_000] < 0.05

    rng = random.Random(12095368)
    max_n = 18
    hi = math.ceil(center(max_n) + width(max_n))
    coordinates = np.arange(1, hi + 1, dtype=np.float64)
    orbit = finite_orbit(max_n, coordinates)

    # Every orbit point has itself as its unique nearest point.
    for m, u_m in enumerate(orbit):
        distances = np.array([np.max(np.abs(u_m - u)) for u in orbit])
        assert int(np.argmin(distances)) == m
        assert distances[m] == 0.0

    # Random positive convex combinations have all coordinates in [0,1]
    # and an attained nearest index in every finite truncation.
    for _ in range(20):
        raw = np.array([rng.random() for _ in range(max_n + 1)])
        raw /= raw.sum()  # coefficient 0 multiplies the zero vector
        x = sum(raw[n] * orbit[n - 1] for n in range(1, max_n + 1))
        assert float(np.min(x)) >= -1e-15
        assert float(np.max(x)) <= 1.0 + 1e-15
        distances = np.array([np.max(np.abs(x - u)) for u in orbit])
        n0 = int(np.argmin(distances))
        delta = float(np.max(np.abs(x - orbit[n0 + 1]))) if n0 + 1 < max_n else None
        if delta is not None:
            assert distances[n0] <= delta + 1e-14
            step = float(np.max(np.abs(orbit[n0 + 1] - orbit[n0])))
            assert step <= distances[n0] + delta + 1e-14

    print("moving-tent checks: PASS")
    print(f"sampled d_2={steps[0]:.9f}, d_22={steps[-1]:.9f}")
    print("late sampled steps: " + ", ".join(f"d_{n}={d:.9f}" for n, d in late_steps.items()))
    print(f"analytic bound at n=10000: {analytic_step_bound(10_000):.9f}")


if __name__ == "__main__":
    main()
