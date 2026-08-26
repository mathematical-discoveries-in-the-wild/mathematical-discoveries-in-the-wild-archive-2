#!/usr/bin/env python3
"""Numerical checks for the arbitrary Ermakoff-limit construction."""

from __future__ import annotations

import math


def parameters(a: float) -> tuple[float, float, float]:
    c = math.log(a)
    A = max(1.0, c + 1.0)
    E0 = math.exp(A)
    m = (A - c) / (E0 - A)
    assert m > 0
    return c, A, m


def h_value(x: float, a: float) -> float:
    c, A, m = parameters(a)
    E0 = math.exp(A)
    increments: list[float] = []
    while x > E0:
        x = math.log(x)
        increments.append(x - c)
    return m * x + sum(increments)


def log_ratio(t: float, a: float) -> float:
    return math.log(t) + h_value(math.log(t), a) - h_value(t, a)


def verify_one(a: float) -> None:
    c, A, m = parameters(a)
    E0 = math.exp(A)

    # Compatibility of the seed and recurrence at the first junction.
    left = m * E0
    right = m * A + A - c
    assert math.isclose(left, right, rel_tol=2e-14, abs_tol=2e-14)

    # The conjugated equation and the Ermakoff ratio are exact up to rounding.
    for x in (A, A + 0.1, 2 * A + 1, 10 * A + 3):
        lhs = h_value(math.exp(x), a)
        rhs = h_value(x, a) + x - c
        assert math.isclose(lhs, rhs, rel_tol=2e-13, abs_tol=2e-13)
    for t in (E0, 1.1 * E0, 10 * E0, 1.0e5 * E0):
        assert math.isclose(log_ratio(t, a), c, rel_tol=2e-12, abs_tol=2e-12)

    # Monotonicity on a broad logarithmic grid.
    samples = [0.0]
    samples.extend(math.exp(-5 + k * 15 / 800) for k in range(801))
    samples = sorted(set(samples))
    values = [h_value(x, a) for x in samples]
    assert all(v2 > v1 for v1, v2 in zip(values, values[1:]))

    # Probe continuity at the first two finite tower boundaries.
    boundaries = [E0]
    for _ in range(1):
        boundaries.append(math.exp(boundaries[-1]))
    for boundary in boundaries:
        eps = 1.0e-9
        center = h_value(boundary, a)
        below = h_value(boundary * (1 - eps), a)
        above = h_value(boundary * (1 + eps), a)
        assert below < center < above
        assert max(center - below, above - center) < 1.0e-4 * max(1.0, abs(center))

    print(
        f"a={a:g} A={A:.12g} m={m:.12g} "
        f"log_ratio(10E0)={log_ratio(10 * E0, a):.12g}"
    )


def main() -> None:
    for a in (0.2, 0.5, 1.0, 2.0, 10.0):
        verify_one(a)
    print("all checks passed")


if __name__ == "__main__":
    main()
