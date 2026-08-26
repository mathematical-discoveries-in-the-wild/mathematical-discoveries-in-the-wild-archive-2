#!/usr/bin/env python3
"""Finite-atomic checks for the doubly interval-valued inequalities."""

from __future__ import annotations

import math
import random


def gauge(values: list[float], weights: list[float], exponent: float) -> float:
    total = sum(w * x**exponent for w, x in zip(weights, values))
    return total ** (1.0 / exponent)


def close_le(left: float, right: float, tol: float = 1e-10) -> bool:
    return left <= right + tol * max(1.0, abs(left), abs(right))


def main() -> None:
    rng = random.Random(250716332)
    trials = 2000

    for _ in range(trials):
        size = rng.randint(1, 8)
        lower_weights = [rng.uniform(0.05, 2.0) for _ in range(size)]
        upper_weights = [
            a + rng.uniform(0.0, 3.0) for a in lower_weights
        ]
        f_lower = [rng.uniform(0.05, 3.0) for _ in range(size)]
        f_upper = [x + rng.uniform(0.0, 3.0) for x in f_lower]
        g_lower = [rng.uniform(0.05, 3.0) for _ in range(size)]
        g_upper = [x + rng.uniform(0.0, 3.0) for x in g_lower]

        # Positive-exponent Hölder in both endpoint channels.
        p = rng.uniform(1.05, 5.0)
        q = p / (p - 1.0)
        for f, g, w in (
            (f_lower, g_lower, lower_weights),
            (f_upper, g_upper, upper_weights),
        ):
            lhs = sum(wi * fi * gi for wi, fi, gi in zip(w, f, g))
            rhs = gauge(f, w, p) * gauge(g, w, q)
            assert close_le(lhs, rhs)

        # Minkowski and reverse Minkowski in both channels.
        for exponent in (rng.uniform(1.05, 4.0), rng.uniform(0.1, 0.95)):
            for f, g, w in (
                (f_lower, g_lower, lower_weights),
                (f_upper, g_upper, upper_weights),
            ):
                lhs = gauge([x + y for x, y in zip(f, g)], w, exponent)
                rhs = gauge(f, w, exponent) + gauge(g, w, exponent)
                if exponent > 1.0:
                    assert close_le(lhs, rhs)
                else:
                    assert close_le(rhs, lhs)

        # Endpointwise diagonal-hull reverse Hölder.
        p = rng.uniform(0.1, 0.95)
        q = p / (p - 1.0)
        lhs_lower = sum(
            w * f * g
            for w, f, g in zip(lower_weights, f_lower, g_lower)
        )
        lhs_upper = sum(
            w * f * g
            for w, f, g in zip(upper_weights, f_upper, g_upper)
        )
        rhs_lower_channel = gauge(f_lower, lower_weights, p) * gauge(
            g_lower, lower_weights, q
        )
        rhs_upper_channel = gauge(f_upper, upper_weights, p) * gauge(
            g_upper, upper_weights, q
        )
        hull_lower = min(rhs_lower_channel, rhs_upper_channel)
        hull_upper = max(rhs_lower_channel, rhs_upper_channel)
        assert close_le(hull_lower, lhs_lower)
        assert close_le(hull_upper, lhs_upper)

    # Exact natural-gauge obstruction on a single positive atom.
    p = 0.5
    q = -1.0
    a, b = 1.0, 4.0
    lhs = (a, b)
    rhs = (a ** (1 / p) * b ** (1 / q), b ** (1 / p) * a ** (1 / q))
    assert lhs == (1.0, 4.0)
    assert rhs == (0.25, 16.0)
    assert not close_le(rhs[1], lhs[1])

    # The optimal bounded-width factor C^(1/q) restores equality upstairs.
    c = b / a
    factor = c ** (1 / q)
    assert math.isclose(factor * rhs[1], lhs[1])

    print(f"passed {trials} randomized doubly interval-valued trials")
    print("natural reverse Holder obstruction:", lhs, "does not dominate", rhs)
    print("sharp width factor:", factor)


if __name__ == "__main__":
    main()
