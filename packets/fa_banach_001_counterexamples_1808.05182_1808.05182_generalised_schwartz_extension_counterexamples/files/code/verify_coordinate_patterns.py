#!/usr/bin/env python3
"""Finite consistency checks for the two c_00 counterexamples."""

from cmath import exp, pi
from math import gcd


def distinct_roots_of_unity(count: int) -> list[complex]:
    roots: list[complex] = []
    # Primitive q-th roots, ordered by q, enumerate all roots without repeats.
    for q in range(1, 1000):
        for p in range(1, q + 1):
            if gcd(p, q) == 1:
                roots.append(exp(2j * pi * p / q))
                if len(roots) == count:
                    return roots
    raise RuntimeError("enumeration bound too small")


def polynomial_value(z: complex, roots: list[complex], n: int) -> complex:
    value = 1.0 + 0.0j
    for root in roots[:n]:
        value *= z - root
    return value


def verify_uniform_pattern(size: int = 128) -> None:
    for coordinate in range(1, size + 1):
        values = [1 if coordinate <= n else 0 for n in range(1, size + 1)]
        assert all(value == 1 for value in values[coordinate - 1 :])


def verify_disc_pattern(size: int = 64) -> None:
    roots = distinct_roots_of_unity(size)
    # At zeta_j, every coordinate n >= j is exactly zero because the same
    # floating-point object occurs as a factor zeta_j-zeta_j.
    for j, zeta in enumerate(roots, start=1):
        for n in range(j, size + 1):
            assert polynomial_value(zeta, roots, n) == 0

    # At the center, every finite product has modulus one and is nonzero.
    for n in range(1, size + 1):
        center = polynomial_value(0.0 + 0.0j, roots, n)
        assert abs(center) > 0.999999999999


if __name__ == "__main__":
    verify_uniform_pattern()
    verify_disc_pattern()
    print("uniform pattern: 128 coordinates passed")
    print("disc pattern: 64 boundary points and center coordinates passed")
