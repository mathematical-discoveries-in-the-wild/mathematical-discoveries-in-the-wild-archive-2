#!/usr/bin/env python3
"""Deterministic sanity checks for the concave-gauge construction.

This is not a proof.  It checks representative finite data for the slope,
concavity, subadditivity, and dyadic inequalities used in the proof packet.
"""

from __future__ import annotations

import bisect
import random


SCALE_COUNT = 41
RANDOM_CASES = 50_000
TOL = 2e-12


def build_scales() -> list[float]:
    factors = (0.21, 0.08, 0.17, 0.12, 0.23, 0.05)
    scales = [1.0]
    for n in range(SCALE_COUNT - 1):
        scales.append(scales[-1] * factors[n % len(factors)])
    assert all(scales[n + 1] < scales[n] / 4 for n in range(len(scales) - 1))
    return scales


def gauge(x: float, scales: list[float]) -> float:
    if x <= 0.0:
        return 0.0
    if x >= scales[0]:
        return 1.0
    if x < scales[-1]:
        # This branch is never used in the sampled grid.  It gives the linear
        # continuation to the origin for the finite numerical approximation.
        return (2.0 ** (-(len(scales) - 1))) * x / scales[-1]

    increasing_scales = list(reversed(scales))
    position = bisect.bisect_right(increasing_scales, x)
    n = len(scales) - position - 1
    left_x, right_x = scales[n + 1], scales[n]
    left_y, right_y = 2.0 ** (-(n + 1)), 2.0 ** (-n)
    return left_y + (right_y - left_y) * (x - left_x) / (right_x - left_x)


def main() -> None:
    scales = build_scales()
    slopes = [
        2.0 ** (-(n + 1)) / (scales[n] - scales[n + 1])
        for n in range(len(scales) - 1)
    ]
    for n in range(len(slopes) - 1):
        assert slopes[n + 1] > slopes[n]

    rng = random.Random(200100223)
    concavity_cases = 0
    subadditivity_cases = 0
    lower_sample_bound = scales[-1] * 2.0

    for _ in range(RANDOM_CASES):
        x = rng.uniform(lower_sample_bound, 1.4)
        y = rng.uniform(lower_sample_bound, 1.4)
        lam = rng.random()
        lhs = gauge(lam * x + (1.0 - lam) * y, scales)
        rhs = lam * gauge(x, scales) + (1.0 - lam) * gauge(y, scales)
        assert lhs + TOL >= rhs
        concavity_cases += 1

        lhs = gauge(x + y, scales)
        rhs = gauge(x, scales) + gauge(y, scales)
        assert lhs <= rhs + TOL
        subadditivity_cases += 1

    dyadic_cases = 0
    for n in range(31):
        epsilon_low = 2.0 ** (-n)
        epsilon_high = 2.0 ** (1 - n)
        assert epsilon_high / 4.0 == 2.0 ** (-n - 1)
        assert gauge(scales[n], scales) == epsilon_low
        assert gauge(scales[n + 1], scales) == 2.0 ** (-n - 1)
        dyadic_cases += 1

    print(f"scales={len(scales)}")
    print(f"adjacent_slope_checks={len(slopes) - 1}")
    print(f"concavity_cases={concavity_cases}")
    print(f"subadditivity_cases={subadditivity_cases}")
    print(f"dyadic_scale_checks={dyadic_cases}")
    print("result=PASS")


if __name__ == "__main__":
    main()
