"""Deterministic sanity checks for the scalar-center construction.

These checks are not a proof.  They sample the inequalities used in the
analytic proof packet and fail loudly on any violation beyond roundoff.
"""

from __future__ import annotations

import math
import random


def h_value(u: float, p: float, c: float, delta: float) -> float:
    return ((1.0 - c) * delta**p + c * abs(u) ** p) ** (1.0 / p)


def check_instance(p: float, c: float, delta: float, y: float) -> float:
    left = max(-1.0, y - delta)
    right = min(1.0, y + delta)
    if left > right:
        return 0.0
    h_left = h_value(left, p, c, delta)
    h_right = h_value(right, p, c, delta)
    lower = right - h_right
    upper = left + h_left
    if lower > upper + 2.0e-12:
        raise AssertionError((p, c, delta, y, lower, upper))
    center = (lower + upper) / 2.0
    largest_violation = 0.0
    for step in range(101):
        u = left + (right - left) * step / 100.0
        lhs = abs(u - center) ** p
        rhs = (1.0 - c) * delta**p + c * abs(u) ** p
        largest_violation = max(largest_violation, lhs - rhs)
    if largest_violation > 3.0e-12:
        raise AssertionError((p, c, delta, y, largest_violation))
    return largest_violation


def main() -> None:
    count = 0
    maximum_violation = 0.0
    for p in (1.0, 1.25, 1.5, 2.0, 3.0, 6.0, 12.0):
        for c_step in range(11):
            c = c_step / 10.0
            for delta_step in range(1, 10):
                delta = delta_step / 10.0
                for y_step in range(-20, 21):
                    y = 1.4 * y_step / 20.0
                    maximum_violation = max(
                        maximum_violation, check_instance(p, c, delta, y)
                    )
                    count += 1

    rng = random.Random(251023213)
    for _ in range(20_000):
        p = math.exp(rng.uniform(math.log(1.0), math.log(20.0)))
        c = rng.random()
        delta = 0.001 + 0.998 * rng.random()
        y = rng.uniform(-1.0 - delta, 1.0 + delta)
        maximum_violation = max(
            maximum_violation, check_instance(p, c, delta, y)
        )
        count += 1

    print(
        {
            "status": "passed",
            "instances": count,
            "u_samples_per_instance": 101,
            "maximum_positive_violation": maximum_violation,
        }
    )


if __name__ == "__main__":
    main()
