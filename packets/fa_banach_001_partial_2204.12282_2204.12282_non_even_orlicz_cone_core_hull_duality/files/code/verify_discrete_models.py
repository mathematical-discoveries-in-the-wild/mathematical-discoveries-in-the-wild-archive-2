#!/usr/bin/env python3
"""Numerical/algebraic checks for the discrete models in the packet.

The script checks:
  1. the two-sided core norm bounds for random finite atomic models
     phi_i(t) = a_i (t_+)^p + b_i (t_-)^p;
  2. the exact scalar infimal-convolution/conjugate identity;
  3. the two sharpness families used in the proof packet.

These checks are not a proof of the functional-analytic theorems.
"""

from __future__ import annotations

import math
import random


def pos(x: float) -> float:
    return max(x, 0.0)


def modular(u: list[float], a: list[float], b: list[float], power: float) -> float:
    n = len(u)
    return sum(
        (a[i] * pos(u[i]) ** power + b[i] * pos(-u[i]) ** power) / n
        for i in range(n)
    )


def core_modular(u: list[float], a: list[float], b: list[float], power: float) -> float:
    n = len(u)
    return sum(max(a[i], b[i]) * abs(u[i]) ** power / n for i in range(n))


def scalar_infconv_coefficient(a: float, b: float, power: float) -> float:
    exponent = -1.0 / (power - 1.0)
    return (a**exponent + b**exponent) ** (-(power - 1.0))


def scalar_conjugate_coefficient(a: float, power: float) -> float:
    q = power / (power - 1.0)
    return (power - 1.0) * power ** (-q) * a ** (-1.0 / (power - 1.0))


def check_random_core_models(rng: random.Random, cases: int = 500) -> float:
    worst_slack = math.inf
    for _ in range(cases):
        n = rng.randint(1, 12)
        power = rng.uniform(1.05, 4.0)
        a = [10 ** rng.uniform(-2.0, 2.0) for _ in range(n)]
        b = [10 ** rng.uniform(-2.0, 2.0) for _ in range(n)]
        u = [rng.uniform(-4.0, 4.0) for _ in range(n)]

        p_forward = modular(u, a, b, power) ** (1.0 / power)
        p_backward = modular([-x for x in u], a, b, power) ** (1.0 / power)
        q = max(p_forward, p_backward)
        p_core = core_modular(u, a, b, power) ** (1.0 / power)

        lower_slack = p_core - q
        upper_slack = 2.0 * q - p_core
        worst_slack = min(worst_slack, lower_slack, upper_slack)
        assert lower_slack >= -1e-11
        assert upper_slack >= -1e-11
    return worst_slack


def check_conjugate_split(rng: random.Random, cases: int = 500) -> float:
    worst_relative_error = 0.0
    for _ in range(cases):
        power = rng.uniform(1.05, 5.0)
        a = 10 ** rng.uniform(-3.0, 3.0)
        b = 10 ** rng.uniform(-3.0, 3.0)
        c = scalar_infconv_coefficient(a, b, power)

        left = scalar_conjugate_coefficient(c, power)
        right = scalar_conjugate_coefficient(a, power) + scalar_conjugate_coefficient(
            b, power
        )
        relative_error = abs(left - right) / max(1.0, abs(left), abs(right))
        worst_relative_error = max(worst_relative_error, relative_error)
        assert relative_error < 2e-12
    return worst_relative_error


def check_sharpness() -> tuple[float, float]:
    epsilon = 1e-8
    # Two equally weighted atoms, phi_e(t)=t_+ + e t_- and u=(1,-1).
    core_ratio = 2.0 / (1.0 + epsilon)
    assert 2.0 - core_ratio < 3e-8

    m = 10**8
    # One atom, phi_M(t)=M(|t|-1)_+.
    hull_ratio = (2.0 * m + 1.0) / (m + 1.0)
    assert 2.0 - hull_ratio < 2e-8
    return core_ratio, hull_ratio


def main() -> None:
    rng = random.Random(220412282)
    core_slack = check_random_core_models(rng)
    conjugate_error = check_conjugate_split(rng)
    core_ratio, hull_ratio = check_sharpness()
    print("random core models: 500 passed")
    print(f"minimum recorded inequality slack: {core_slack:.3e}")
    print("scalar conjugate splits: 500 passed")
    print(f"maximum relative coefficient error: {conjugate_error:.3e}")
    print(f"core sharpness ratio: {core_ratio:.12f}")
    print(f"hull sharpness ratio: {hull_ratio:.12f}")
    print("all checks passed")


if __name__ == "__main__":
    main()
