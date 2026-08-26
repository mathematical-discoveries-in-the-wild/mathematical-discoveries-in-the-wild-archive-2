#!/usr/bin/env python3
"""Numerical regression checks for the quadratic Koenigs-domain packet.

This script is not part of the proof. It checks the boundary uniformization,
the harmonic-measure normalization, and representative truncated integrals.
"""

from __future__ import annotations

import cmath
import math

from scipy.integrate import quad


def conformal_map(z: complex, c: float) -> complex:
    return cmath.cosh(math.pi * cmath.sqrt(c * z - 0.25))


def check_boundary_identity() -> None:
    for c in (0.4, 1.0, 2.5):
        for y in (-3.0, -0.7, 0.0, 0.4, 2.0):
            z = c * y * y + 1j * y
            lhs = conformal_map(z, c)
            rhs = 1j * math.sinh(math.pi * c * y)
            assert abs(lhs - rhs) < 1e-9 * (1.0 + abs(rhs))


def harmonic_density(y: float, c: float) -> float:
    x = abs(math.pi * c * y)
    decay = math.exp(-x)
    return 2.0 * c * decay / (1.0 + decay * decay)


def check_harmonic_measure_normalization() -> None:
    for c in (0.4, 1.0, 2.5):
        value, error = quad(lambda y: harmonic_density(y, c), -math.inf, math.inf)
        assert abs(value - 1.0) < 1e-10
        assert error < 1e-9


def truncated_frequency_integral(c: float, p: float, b: float, radius: float) -> float:
    integrand = lambda y: math.exp(-p * b * y) * harmonic_density(y, c)
    value, _ = quad(integrand, -radius, radius, limit=300)
    return value


def check_threshold_behavior() -> None:
    c = 1.0
    p = 2.0
    inside = 0.8 * math.pi * c / p
    endpoint = math.pi * c / p
    inside_values = [truncated_frequency_integral(c, p, inside, r) for r in (2, 4, 6)]
    endpoint_values = [truncated_frequency_integral(c, p, endpoint, r) for r in (2, 4, 6)]
    assert inside_values[-1] - inside_values[-2] < inside_values[-2] - inside_values[-3]
    assert endpoint_values[-1] - endpoint_values[-2] > 1.0


if __name__ == "__main__":
    check_boundary_identity()
    check_harmonic_measure_normalization()
    check_threshold_behavior()
    print("PASS: boundary map, harmonic density, and threshold regression checks")
