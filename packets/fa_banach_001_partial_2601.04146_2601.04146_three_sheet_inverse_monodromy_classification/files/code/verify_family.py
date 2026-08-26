#!/usr/bin/env python3
"""Numerical/symbolic sanity checks for the explicit F_m family.

This script is not part of the proof.  It checks junction values and first
derivatives, winding numbers at representative points, and the rank of the
root-of-unity Vandermonde matrix for 3 <= m <= 20.
"""

from __future__ import annotations

import cmath
import math


def outer(m: int, theta: float) -> complex:
    return 2 - m + (m - 1) * cmath.exp(-1j * m * theta / (m - 1))


def inner(m: int, theta: float) -> complex:
    return cmath.exp(-1j * m * theta)


def outer_derivative(m: int, theta: float) -> complex:
    return -1j * m * cmath.exp(-1j * m * theta / (m - 1))


def inner_derivative(m: int, theta: float) -> complex:
    return -1j * m * cmath.exp(-1j * m * theta)


def winding(samples: list[complex], point: complex) -> int:
    total = 0.0
    previous = cmath.phase(samples[0] - point)
    for value in samples[1:] + samples[:1]:
        current = cmath.phase(value - point)
        delta = current - previous
        while delta <= -math.pi:
            delta += 2 * math.pi
        while delta > math.pi:
            delta -= 2 * math.pi
        total += delta
        previous = current
    return round(total / (2 * math.pi))


def determinant3(rows: list[list[complex]]) -> complex:
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def check(m: int) -> None:
    join = 2 * math.pi * (m - 1) / m
    tolerance = 1e-10

    assert abs(outer(m, 0.0) - inner(m, 2 * math.pi)) < tolerance
    assert abs(outer(m, join) - inner(m, join)) < tolerance
    assert abs(outer_derivative(m, 0.0) - inner_derivative(m, 2 * math.pi)) < tolerance
    assert abs(outer_derivative(m, join) - inner_derivative(m, join)) < tolerance

    n = 20_000
    samples = []
    for j in range(n):
        theta = 2 * math.pi * j / n
        samples.append(outer(m, theta) if theta <= join else inner(m, theta))
    assert winding(samples, 0j) == -2
    annulus_point = complex(-(m - 2), 0.5 * (m - 2))
    if abs(annulus_point) <= 1:
        annulus_point = complex(-(m - 2), 1.1)
    assert abs(annulus_point - (2 - m)) < m - 1
    assert abs(annulus_point) > 1
    assert winding(samples, annulus_point) == -1

    omega = cmath.exp(2j * math.pi / m)
    roots = [1, omega, omega**2]
    vandermonde = [[1, root, root**2] for root in roots]
    assert abs(determinant3(vandermonde)) > 1e-8


def main() -> None:
    for m in range(3, 21):
        check(m)
    print("verified m=3,...,20: C1 junctions, winding -2/-1, Vandermonde nonzero")


if __name__ == "__main__":
    main()
