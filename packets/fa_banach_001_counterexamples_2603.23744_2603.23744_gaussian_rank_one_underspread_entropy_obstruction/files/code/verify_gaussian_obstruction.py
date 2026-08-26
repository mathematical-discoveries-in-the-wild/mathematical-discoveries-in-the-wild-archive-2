#!/usr/bin/env python3
"""Numerical sanity checks for the Gaussian rank-one obstruction.

The proof in main.tex is symbolic.  This script independently integrates the
radial phase-space expression by Simpson's rule and checks the resulting exact
formula, spreading L1 norm, entropy covering formula, and asymptotic separation.
Only the Python standard library is required.
"""

from __future__ import annotations

import math


def simpson(f, left: float, right: float, panels: int = 20_000) -> float:
    if panels % 2:
        raise ValueError("Simpson panel count must be even")
    h = (right - left) / panels
    total = f(left) + f(right)
    total += 4.0 * sum(f(left + k * h) for k in range(1, panels, 2))
    total += 2.0 * sum(f(left + k * h) for k in range(2, panels, 2))
    return total * h / 3.0


def unit_ball_volume(n: int) -> float:
    return math.pi ** (n / 2) / math.gamma(n / 2 + 1)


def exact_log_integral(d: int, c: float, eps: float) -> float:
    level = math.log(c * 2**d / eps)
    return level ** (d + 1) / (2**d * math.factorial(d) * (d + 1))


def numeric_log_integral(d: int, c: float, eps: float) -> float:
    n = 2 * d
    level = math.log(c * 2**d / eps)
    radius = math.sqrt(level / (2 * math.pi))
    sphere_area = n * unit_ball_volume(n)
    radial = simpson(
        lambda r: (level - 2 * math.pi * r * r) * r ** (n - 1),
        0.0,
        radius,
    )
    return sphere_area * radial


def entropy(d: int, c: float, eps: float) -> float:
    del d
    return math.log(math.ceil(c / eps))


def run() -> None:
    checked_integrals = 0
    for d in range(1, 6):
        for c in (0.03, 1.0, 2.0):
            for level in (3.0, 7.0, 15.0):
                eps = c * 2**d * math.exp(-level)
                exact = exact_log_integral(d, c, eps)
                numeric = numeric_log_integral(d, c, eps)
                rel_error = abs(numeric - exact) / exact
                assert rel_error < 2e-10, (d, c, level, rel_error)
                checked_integrals += 1

    # Arbitrarily small spreading norm: ||eta_c||_1 = c 2^d.
    for d in range(1, 9):
        for delta in (1e-2, 1e-6, 1e-12):
            c = delta / (2 ** (d + 1))
            assert c * 2**d < delta

    # The exact covering number is ceil(c/eps); its logarithm is asymptotic to
    # log(c/eps).  The ratio against the phase-space integral must decrease
    # toward zero along an explicit sequence.
    for d in range(1, 6):
        c = 0.7
        ratios = []
        for exponent in (10.0, 20.0, 40.0, 80.0):
            eps = c * math.exp(-exponent)
            h_value = entropy(d, c, eps)
            assert abs(h_value / exponent - 1.0) < 1e-4
            ratios.append(h_value / exact_log_integral(d, c, eps))
        assert all(a > b for a, b in zip(ratios, ratios[1:])), (d, ratios)
        assert ratios[-1] < ratios[0] / 2.0, (d, ratios)

    print(
        "PASS: Gaussian Weyl/log-integral formulas and entropy separation "
        f"verified ({checked_integrals} radial integrations)"
    )


if __name__ == "__main__":
    run()
