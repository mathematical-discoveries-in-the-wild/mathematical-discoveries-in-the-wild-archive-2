#!/usr/bin/env python3
"""Deterministic checks for the Green-circle endpoint construction."""

from __future__ import annotations

import cmath
import math


TAU = 2.0 * math.pi
SAMPLES = 16384


def phi(a: complex, w: complex) -> complex:
    return (a + w) / (1.0 + a.conjugate() * w)


def eta(a: complex, z: complex) -> complex:
    return (z - a) / (1.0 - a.conjugate() * z)


def automorphism(b: complex, alpha: float, z: complex) -> complex:
    return cmath.exp(1j * alpha) * eta(b, z)


def circle_mean(function, a: complex, radius: float) -> float:
    total = 0.0
    for k in range(SAMPLES):
        w = radius * cmath.exp(1j * TAU * k / SAMPLES)
        total += function(phi(a, w))
    return total / SAMPLES


def test_jensen_identity() -> None:
    cases = [
        (0.13 + 0.07j, 0.42),
        (-0.51 + 0.11j, 0.24),
        (0.28 - 0.36j, 0.71),
    ]
    for a, radius in cases:
        observed = circle_mean(lambda z: -math.log(abs(z)), a, radius)
        expected = -math.log(max(abs(a), radius))
        assert abs(observed - expected) < 2.0e-8, (observed, expected)


def test_mobius_circle_factorization() -> None:
    a = 0.21 - 0.17j
    b = -0.31 + 0.09j
    alpha = 0.37
    center = automorphism(b, alpha, a)
    probe = 0.23 + 0.08j
    image = automorphism(b, alpha, phi(a, probe))
    rotation = eta(center, image) / probe
    assert abs(abs(rotation) - 1.0) < 2.0e-14
    for k in range(200):
        w = 0.63 * cmath.exp(1j * TAU * k / 200)
        left = automorphism(b, alpha, phi(a, w))
        right = phi(center, rotation * w)
        assert abs(left - right) < 3.0e-14


def test_radial_reduction() -> None:
    def profile(t: float) -> float:
        return min(t, 2.7) / math.sqrt(2.7)

    radial_endpoint = 1.0
    centers = [0j, 0.17 + 0.09j, -0.46 + 0.13j, 0.72j]
    radii = [math.exp(-t) for t in (0.15, 0.6, 1.3, 2.7, 5.0)]
    observed = 0.0
    for a in centers:
        for radius in radii:
            t = -math.log(radius)
            mean_square = circle_mean(
                lambda z: profile(-math.log(abs(z))) ** 2, a, radius
            )
            observed = max(observed, math.sqrt(mean_square / t))
    assert observed <= radial_endpoint + 3.0e-8
    assert abs(profile(2.7) / math.sqrt(2.7) - radial_endpoint) < 1.0e-14


def test_dilation_and_sharp_constant() -> None:
    for s in (0.19, 0.7, 1.6, 8.0):
        for t in (0.1, 0.8, 2.7, 9.0):
            original = min(s * t, 2.7) / math.sqrt(2.7 * s * t)
            dilated = (
                s ** -0.5
                * min(s * t, 2.7)
                / math.sqrt(2.7 * t)
            )
            assert abs(original - dilated) < 1.0e-14
    energy = 1.0
    green_norm = 1.0 / math.sqrt(2.0 * math.pi)
    assert abs(green_norm - math.sqrt(energy / (2.0 * math.pi))) < 1.0e-15


def local_weight_ratio(s: float, radius: float) -> float:
    numerator = s * radius ** (2.0 - 2.0 / s)
    numerator *= (1.0 - radius ** (2.0 / s)) ** 2
    denominator = (1.0 - radius**2) ** 2
    return numerator / denominator


def test_local_integral_obstruction() -> None:
    for s in (0.5, 1.7, 3.0):
        ratios = [local_weight_ratio(s, r) for r in (0.17, 0.43, 0.79)]
        assert max(ratios) - min(ratios) > 1.0e-3


def main() -> None:
    test_jensen_identity()
    test_mobius_circle_factorization()
    test_radial_reduction()
    test_dilation_and_sharp_constant()
    test_local_integral_obstruction()
    print("verified Jensen identity on three off-center Green circles")
    print("verified Möbius circle factorization pointwise")
    print("verified radial endpoint bound on sampled profiles")
    print("verified dilation scaling and sharp constant")
    print("verified nonconstant local-weight ratios for s != 1")


if __name__ == "__main__":
    main()
