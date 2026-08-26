#!/usr/bin/env python3
"""Sanity checks for the Hadamard-module packet.

This script checks explicit formulas at representative exponents.  It is not
an exhaustive search and is not used as a proof.
"""

from __future__ import annotations

import cmath
import math
import random

import numpy as np


def lp_norm(z: np.ndarray, exponent: float) -> float:
    return float(np.sum(np.abs(z) ** exponent) ** (1.0 / exponent))


def check_exponent(p: float) -> None:
    s = p / (p - 1.0)
    q = 3.0 ** (p - 1.0)
    N = 2.0 ** (1.0 / p - 1.0) * (3.0**p + 1.0) ** (1.0 / p)
    D = (2.0 * (q**s + 1.0)) ** (1.0 / s)
    assert abs((2.0 * N) ** (p - 1.0) - D) < 2e-11

    scalar_margin = (s - 1.0) * (q ** (s - 2.0) + q**2) - (q**s + 1.0)
    axis_ratio_power = ((q + 1.0) ** s + (q - 1.0) ** s) / (
        2.0 * (q**s + 1.0)
    )
    assert scalar_margin > 0.0
    assert axis_ratio_power > 1.0

    g = np.array([q, 1.0, q, -1.0], dtype=complex) / D
    phi_plus = np.array([1.0, 1.0j])
    c0 = np.array(
        [
            [q - 1.0j, 1.0 - 1.0j * q],
            [1.0 - 1.0j * q, q - 1.0j],
            [q + 1.0j, -1.0 - 1.0j * q],
            [-1.0 - 1.0j * q, q + 1.0j],
        ],
        dtype=complex,
    ) / (2.0 * D)
    assert np.max(np.abs(c0 @ phi_plus - g)) < 2e-12

    second_variation = 2.0 * s * scalar_margin / (q**s + 1.0)
    assert second_variation > 0.0

    # Find a small explicit perturbation with positive expansion.
    c = 2.0 ** (1.0 / s) * c0
    phi_minus = np.array([1.0, -1.0j])
    found = None
    for k in range(2, 15):
        t = 10.0 ** (-k)
        xi = phi_plus + 1.0j * t * phi_minus
        excess = lp_norm(c @ xi, s) ** s - lp_norm(xi, s) ** s
        if excess > 1e-14:
            found = (t, excess)
            break
    assert found is not None

    # Random samples verify the sharp source-column upper bound.
    T = 0.5 * np.array(
        [[3, 1], [1, 3], [3, -1], [-1, 3]], dtype=complex
    )
    rng = random.Random(19471 + round(1000 * p))
    sampled_max = 0.0
    for _ in range(25000):
        theta = math.pi * rng.random()
        phase = 2.0 * math.pi * rng.random()
        raw = np.array(
            [math.cos(theta), math.sin(theta) * cmath.exp(1.0j * phase)]
        )
        raw /= lp_norm(raw, p)
        sampled_max = max(sampled_max, lp_norm(T @ raw, p))
    assert sampled_max <= N * (1.0 + 2e-12)

    print(
        f"p={p:.3f} p'={s:.6f} N={N:.9f} "
        f"scalar_margin={scalar_margin:.6e} axis_ratio^s={axis_ratio_power:.9f} "
        f"perturbation={found[0]:.0e} excess={found[1]:.3e} "
        f"sampled_column_norm={sampled_max:.9f}"
    )


def main() -> None:
    for exponent in (1.05, 1.10, 1.25, 1.50, 1.75, 1.90, 1.99):
        check_exponent(exponent)
    print("all explicit identity and sampling checks passed")


if __name__ == "__main__":
    main()
