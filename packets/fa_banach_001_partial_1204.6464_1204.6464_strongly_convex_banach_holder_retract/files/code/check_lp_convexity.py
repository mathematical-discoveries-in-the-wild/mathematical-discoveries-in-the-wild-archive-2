#!/usr/bin/env python3
"""Regression checks for constants in the Lp Hölder-retraction packet."""

from __future__ import annotations

import math

import numpy as np


def lp_sq(x: np.ndarray, p: float) -> float:
    return float(np.sum(np.abs(x) ** p) ** (2.0 / p))


def main() -> None:
    rng = np.random.default_rng(12046464)
    trials = 0
    worst_slack = math.inf
    threshold_cases = 0

    for p in (1.51, 1.6, 1.75, 1.9, 2.0):
        for dimension in (1, 2, 5, 20, 80):
            for _ in range(4000):
                x = rng.normal(size=dimension)
                y = rng.normal(size=dimension)
                lhs = 0.5 * (lp_sq(x + y, p) + lp_sq(x - y, p))
                rhs = lp_sq(x, p) + (p - 1.0) * lp_sq(y, p)
                scale = max(1.0, abs(lhs), abs(rhs))
                slack = (lhs - rhs) / scale
                if slack < -2e-12:
                    raise AssertionError((p, dimension, lhs, rhs, slack))
                worst_slack = min(worst_slack, slack)
                trials += 1

        c = p - 1.0
        upper = math.sqrt(2.0 * c)
        for fraction in (0.0, 0.25, 0.5, 0.75, 0.999999):
            k = 1.0 + fraction * (upper - 1.0)
            rho = (k * k - c) / c
            if not (-1e-14 <= rho < 1.0 + 1e-12):
                raise AssertionError((p, k, rho))
            threshold_cases += 1

    print(f"BCL midpoint checks passed: {trials}")
    print(f"threshold checks passed: {threshold_cases}")
    print(f"minimum normalized slack: {worst_slack:.3e}")


if __name__ == "__main__":
    main()
