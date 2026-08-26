#!/usr/bin/env python3
"""Finite sanity checks for the alternating Hölder obstruction.

The proof in main.tex is exact and uses an infinite convergent sequence.  This
script checks the metric/Hölder estimates on deep finite initial segments of
the explicit model X={0} union {3^{-n}} and checks the scalar feedback
inequality used in the non-openness upgrade.
"""

from __future__ import annotations

import math


def holder_ratio(x: float, y: float, fx: float, fy: float, alpha: float) -> float:
    if x == y:
        return 0.0
    return abs(fx - fy) / abs(x - y) ** alpha


def verify_model(alpha: float, depth: int = 80) -> float:
    points = [0.0] + [3.0 ** (-n) for n in range(1, depth + 1)]
    values_f = [0.0] + [x**alpha if n % 2 == 0 else 0.0
                              for n, x in enumerate(points[1:], start=1)]
    values_g = [0.0] + [0.0 if n % 2 == 0 else x**alpha
                              for n, x in enumerate(points[1:], start=1)]

    maximum = 0.0
    for i in range(len(points)):
        assert abs(values_f[i] * values_g[i]) < 1e-300
        for j in range(i + 1, len(points)):
            maximum = max(
                maximum,
                holder_ratio(points[i], points[j], values_f[i], values_f[j], alpha),
                holder_ratio(points[i], points[j], values_g[i], values_g[j], alpha),
            )

    theoretical_bound = (3.0 / 2.0) ** alpha
    assert maximum <= theoretical_bound * (1.0 + 1e-12)

    # Along the active parity, the base-point Hölder quotient is exactly one.
    for n, x in enumerate(points[1:], start=1):
        active = values_f[n] if n % 2 == 0 else values_g[n]
        assert math.isclose(active / x**alpha, 1.0, rel_tol=1e-14)
    return maximum


def run() -> None:
    maxima = []
    for alpha in (0.1, 0.25, 0.5, 0.75, 1.0):
        maxima.append((alpha, verify_model(alpha)))

    # The two limiting inequalities imply
    # |a_0| <= q|b_0| and |b_0| <= q|a_0| with q=eps/(1-eps).
    for epsilon in (0.05, 0.2, 0.49):
        feedback = (epsilon / (1.0 - epsilon)) ** 2
        assert feedback < 1.0

    summary = ", ".join(f"alpha={a:g}:max={m:.8f}" for a, m in maxima)
    print(f"PASS: alternating Hölder obstruction verified ({summary})")


if __name__ == "__main__":
    run()

