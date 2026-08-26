#!/usr/bin/env python3
"""Sanity checks for the two-channel spinor instability packet.

The proof is analytic.  This script checks the angular coefficients, the
closed Pöschl--Teller energy, the stated threshold, and one direct radial
quadrature.  It also exhibits points where the mixed direction is unstable
while both constituent one-channel directions remain stable.
"""

from __future__ import annotations

import math

import numpy as np


def poschl_energy(mu: float, delta: float, alpha: float, p: float) -> float:
    """Lowest energy for a fixed angular spinor and optimized scalar radial part."""
    d = 0.5 - alpha
    a = 0.5 * p * d * d
    b = 0.5 * (p - 2.0) * d
    coupling = a * (1.0 + (p - 2.0) * delta)
    return mu - 0.25 * (math.sqrt(4.0 * coupling + b * b) - b) ** 2


def mixed_threshold(alpha: float) -> float:
    d = 0.5 - alpha
    return 2.0 * math.sqrt(1.0 + 2.0 / (d * d))


def mixed_energy(alpha: float, p: float) -> float:
    d = 0.5 - alpha
    return poschl_energy(d * d + 2.0, 1.0, alpha, p)


def radial_quadrature(alpha: float, p: float) -> tuple[float, float]:
    """Compare the explicit ground-state Rayleigh quotient with its formula."""
    d = 0.5 - alpha
    mu = d * d + 2.0
    a = 0.5 * p * d * d
    b = 0.5 * (p - 2.0) * d
    coupling = a * (p - 1.0)
    exponent = (math.sqrt(4.0 * coupling + b * b) - b) / (2.0 * b)

    s = np.linspace(-20.0 / b, 20.0 / b, 200_001)
    bs = b * s
    w = np.cosh(bs) ** (-exponent)
    wp = -exponent * b * np.tanh(bs) * w
    numerator = np.trapz(
        wp * wp + mu * w * w - coupling * w * w / np.cosh(bs) ** 2,
        s,
    )
    denominator = np.trapz(w * w, s)
    return numerator / denominator, mixed_energy(alpha, p)


def main() -> None:
    # Angular cancellation:
    # sqrt(2/3) chi_1^(1/2) + sqrt(1/3) chi_-2^(1/2)
    # has upper coefficient 1 and lower coefficient 0.
    r2 = math.sqrt(2.0 / 3.0)
    r1 = math.sqrt(1.0 / 3.0)
    upper = r2 * r2 + r1 * r1
    lower = r2 * r1 - r1 * r2
    assert abs(upper - 1.0) < 1e-15
    assert abs(lower) < 1e-15

    # The threshold is exactly the unique zero of the mixed energy in (2, 6).
    for alpha in (-0.49, -0.4, -0.25, -0.1, -0.05, -0.001):
        p0 = mixed_threshold(alpha)
        assert 2.0 < p0 < 6.0
        assert abs(mixed_energy(alpha, p0)) < 2e-13
        assert mixed_energy(alpha, p0 - 1e-3) > 0.0
        assert mixed_energy(alpha, p0 + 1e-3) < 0.0

    # These points lie outside both constituent single-channel instabilities.
    cases = ((-0.10, 5.50), (-0.05, 5.80), (-0.18, 5.00), (-0.25, 4.50))
    for alpha, p in cases:
        mixed = mixed_energy(alpha, p)
        plus = poschl_energy((1.5 - alpha) ** 2, 2.0 / 3.0, alpha, p)
        minus = poschl_energy((1.5 + alpha) ** 2, 1.0 / 3.0, alpha, p)
        assert mixed < 0.0 < min(plus, minus)
        print(
            f"alpha={alpha: .2f} p={p:.2f} "
            f"mixed={mixed: .12f} pure_plus={plus: .12f} "
            f"pure_minus={minus: .12f}"
        )

    numerical, closed = radial_quadrature(-0.10, 5.50)
    assert abs(numerical - closed) < 2e-9
    print(f"radial quadrature={numerical:.12f} closed={closed:.12f}")
    print("all two-channel checks passed")


if __name__ == "__main__":
    main()
