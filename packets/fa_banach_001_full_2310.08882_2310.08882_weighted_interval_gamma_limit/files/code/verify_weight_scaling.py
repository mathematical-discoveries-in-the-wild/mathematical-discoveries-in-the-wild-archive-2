#!/usr/bin/env python3
"""Discrete checks for the weighted one-dimensional nonlocal functional."""

from __future__ import annotations

import math
import random


def energy(values, weights, q, kernel_index):
    """Midpoint Riemann sum for rho_i(r)=i 1_{r<=1/i}."""
    n = len(values)
    dx = 1.0 / n
    points = [(j + 0.5) * dx for j in range(n)]
    total = 0.0
    radius = 1.0 / kernel_index
    for y in range(n):
        inner = 0.0
        for x in range(n):
            distance = abs(points[x] - points[y])
            if 0.0 < distance <= radius:
                quotient = abs(values[x] - values[y]) / distance
                inner += quotient**q * kernel_index * weights[x] * dx
        total += weights[y] * inner ** (1.0 / q) * dx
    return total


def check_lower_bound():
    rng = random.Random(231008882)
    n = 180
    m = 0.7
    for q in (1.25, 2.0, 3.5):
        for kernel_index in (9, 17, 31):
            for trial in range(8):
                values = [
                    math.sin((trial + 1) * 2.0 * math.pi * (j + 0.5) / n)
                    + 0.15 * rng.uniform(-1.0, 1.0)
                    for j in range(n)
                ]
                weights = [m + 1.8 * rng.random() for _ in range(n)]
                weighted = energy(values, weights, q, kernel_index)
                euclidean = energy(values, [1.0] * n, q, kernel_index)
                lower = m ** (1.0 + 1.0 / q) * euclidean
                assert weighted + 2e-12 >= lower, (q, kernel_index, trial)


def check_exact_locality():
    n = 400
    points = [(j + 0.5) / n for j in range(n)]
    m = 0.8
    weights = [m if 0.30 < x < 0.70 else 2.4 for x in points]
    values = [0.0 if x <= 0.45 else 1.0 if x >= 0.55 else 10.0 * (x - 0.45) for x in points]
    for q in (1.4, 2.0, 4.0):
        # Radius 1/50 is much smaller than the gap from the transition to
        # the high-weight region, so every nonconstant pair sees weight m.
        weighted = energy(values, weights, q, 50)
        euclidean = energy(values, [1.0] * n, q, 50)
        expected = m ** (1.0 + 1.0 / q) * euclidean
        assert math.isclose(weighted, expected, rel_tol=2e-13, abs_tol=2e-13)


def check_affine_constant():
    n = 900
    points = [(j + 0.5) / n for j in range(n)]
    values = points
    q = 2.3
    target = 2.0 ** (1.0 / q)
    errors = []
    for kernel_index in (12, 24, 48):
        observed = energy(values, [1.0] * n, q, kernel_index)
        errors.append(abs(observed - target))
    assert errors[-1] < errors[0]
    assert errors[-1] < 0.035, (errors, target)


if __name__ == "__main__":
    check_lower_bound()
    check_exact_locality()
    check_affine_constant()
    print("PASS: weight comparison, exact locality, and affine normalization")
