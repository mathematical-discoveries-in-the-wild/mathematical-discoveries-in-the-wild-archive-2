#!/usr/bin/env python3
"""Exact and numerical checks for the parallel-line restriction splitting.

This verifies the explicit right inverse used in the proof.  It does not
verify the functional-analytic stability of property (Omega).
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np


BASES = (Fraction(-1), Fraction(1, 2), Fraction(2))


def lagrange(i: int, y: Fraction) -> Fraction:
    value = Fraction(1)
    for j, base in enumerate(BASES):
        if j != i:
            value *= (y - base) / (BASES[i] - base)
    return value


def g(i: int, t: np.ndarray) -> np.ndarray:
    if i == 0:
        return np.sin(t) + t**2
    if i == 1:
        return np.cos(2 * t) - t
    return 1 + t + t**3


def extension(t: np.ndarray, y: float) -> np.ndarray:
    return sum(float(lagrange(i, Fraction(y))) * g(i, t) for i in range(len(BASES)))


def main() -> None:
    matrix = [[lagrange(i, base) for i in range(len(BASES))] for base in BASES]
    expected = [[Fraction(int(i == j)) for i in range(len(BASES))] for j in range(len(BASES))]
    assert matrix == expected

    grid = np.linspace(-2.0, 2.0, 101)
    for j, base in enumerate(BASES):
        error = np.max(np.abs(extension(grid, float(base)) - g(j, grid)))
        assert error < 1e-12

    # A function in the kernel of simultaneous restriction is any smooth
    # multiple of the transverse vanishing polynomial.
    for base in BASES:
        vanish = np.prod([float(base - other) for other in BASES])
        assert abs(vanish) < 1e-15

    print("exact transverse interpolation matrix: identity")
    print("simultaneous restriction/right-inverse checks passed on 303 samples")


if __name__ == "__main__":
    main()

