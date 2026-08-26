#!/usr/bin/env python3
"""Finite sanity checks for the explicit Gamma_* construction.

This script is not a proof.  It checks representative rescaling errors and
the angular cover used for finite-order unimodular multipliers.
"""

from __future__ import annotations

import cmath
import math


def gaussian_approx(z: complex, mesh: int) -> complex:
    return complex(round(mesh * z.real), round(mesh * z.imag)) / mesh


def check_tail(mu: complex, c: complex, start: int = 8, stop: int = 40) -> None:
    errors = []
    for n in range(start, stop + 1):
        target = c / (mu**n)
        mesh = max(10, math.ceil(n * abs(mu) ** n))
        gamma = gaussian_approx(target, mesh)
        errors.append(abs((mu**n) * gamma - c))
    assert errors[-1] < 0.15
    assert min(errors[-5:]) < min(errors[:5])


def check_finite_half_plane_cover(order: int, samples: int = 4000) -> None:
    roots = [cmath.exp(2j * math.pi * k / order) for k in range(order)]
    for j in range(samples):
        z = cmath.exp(2j * math.pi * j / samples)
        assert max((z / root).real for root in roots) >= -1e-12


def main() -> None:
    check_tail(1.4 * cmath.exp(0.37j), 1.2 - 0.8j)
    check_tail(0.72 * cmath.exp(-0.41j), -1.1 + 0.9j)
    for order in range(2, 41):
        check_finite_half_plane_cover(order)
    print("Gamma_* sanity checks passed: two nonunit scalings and orders 2..40")


if __name__ == "__main__":
    main()
