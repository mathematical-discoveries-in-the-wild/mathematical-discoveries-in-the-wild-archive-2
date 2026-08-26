#!/usr/bin/env python3
"""Symbolic identities and numerical stress tests for the proof packet."""

from __future__ import annotations

import sympy as sp


def quantile(n: int, a: float, u: float) -> float:
    r = 1.0 / n
    if a == 1.0:
        return 2.0 * u
    if a == 0.0:
        return (1.0 - (1.0 - u) ** r) / (1.0 - 2.0 ** (-r))
    num = (1.0 + (a - 1.0) * u) ** r - 1.0
    den = ((1.0 + a) / 2.0) ** r - 1.0
    return num / den


def mean_exact(n: int, a: float) -> float:
    r = 1.0 / n
    if a == 1.0:
        return 1.0
    avg = (a ** (r + 1.0) - 1.0) / ((r + 1.0) * (a - 1.0))
    return (avg - 1.0) / (((1.0 + a) / 2.0) ** r - 1.0)


def trap(values: list[float]) -> float:
    return (sum(values) - 0.5 * values[0] - 0.5 * values[-1]) / (
        len(values) - 1
    )


def symbolic_check() -> None:
    y, r = sp.symbols("y r", positive=True)
    elasticity = r * (y - 1) * y ** (r - 1) / (y**r - 1)
    target = (
        r
        * y ** (r - 2)
        * (y**r - r * y - (1 - r))
        / (y**r - 1) ** 2
    )
    assert sp.simplify(sp.diff(elasticity, y) - target) == 0
    print("symbolic elasticity derivative: OK")


def numerical_check() -> None:
    a_values = [
        0.0,
        1e-10,
        1e-6,
        0.01,
        0.2,
        0.8,
        1.0,
        1.2,
        5.0,
        100.0,
        1e8,
    ]
    us = [j / 4000.0 for j in range(4001)]
    thresholds = [j / 100.0 * 4.0 for j in range(401)]
    worst_cross = 0.0
    worst_mean = 0.0
    worst_call = 0.0

    for n in [2, 3, 4, 10, 50]:
        q0 = [quantile(n, 0.0, u) for u in us]
        m0 = mean_exact(n, 0.0)
        for a in a_values:
            qa = [quantile(n, a, u) for u in us]
            for j, u in enumerate(us):
                if u <= 0.5:
                    worst_cross = max(worst_cross, q0[j] - qa[j])
                else:
                    worst_cross = max(worst_cross, qa[j] - q0[j])
            worst_mean = max(worst_mean, mean_exact(n, a) - m0)
            for s in thresholds:
                ca = trap([max(x - s, 0.0) for x in qa])
                c0 = trap([max(x - s, 0.0) for x in q0])
                worst_call = max(worst_call, ca - c0)

    tolerance = 3e-10
    assert worst_cross <= tolerance
    assert worst_mean <= tolerance
    assert worst_call <= tolerance
    print(f"worst quantile-crossing violation: {worst_cross:.3e}")
    print(f"worst mean violation:              {worst_mean:.3e}")
    print(f"worst stop-loss violation:         {worst_call:.3e}")
    print("numerical stress tests: OK")


if __name__ == "__main__":
    symbolic_check()
    numerical_check()
