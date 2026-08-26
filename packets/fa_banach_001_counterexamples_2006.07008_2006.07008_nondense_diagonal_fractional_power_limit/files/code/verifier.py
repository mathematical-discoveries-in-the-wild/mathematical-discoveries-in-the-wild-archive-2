#!/usr/bin/env python3
"""Numerical sanity check for the exact diagonal counterexample.

This script is not part of the proof.  It compares midpoint quadrature of the
coordinate integral with its closed form for alpha = 1 + 0.7 i.
"""

from __future__ import annotations

import cmath


ALPHA = 1.0 + 0.7j


def positive_power(value: float, exponent: complex) -> complex:
    return cmath.exp(exponent * cmath.log(value))


def closed_form(cutoff: float, coordinate: int) -> complex:
    return positive_power(cutoff / (cutoff + coordinate), ALPHA)


def midpoint_integral(cutoff: float, coordinate: int, panels: int = 200_000) -> complex:
    width = cutoff / panels
    total = 0.0j
    for index in range(panels):
        lam = (index + 0.5) * width
        total += (
            ALPHA
            * positive_power(lam, ALPHA - 1.0)
            * coordinate
            * positive_power(lam + coordinate, -ALPHA - 1.0)
        )
    return width * total


def main() -> None:
    worst = 0.0
    for cutoff in (1.0, 10.0, 100.0):
        for coordinate in (1, 3, 20):
            exact = closed_form(cutoff, coordinate)
            numeric = midpoint_integral(cutoff, coordinate)
            error = abs(exact - numeric)
            worst = max(worst, error)
            print(
                f"N={cutoff:5.1f} k={coordinate:2d} "
                f"quadrature_error={error:.3e}"
            )

    for cutoff in (1.0, 10.0, 100.0):
        finite_tail = max(
            abs(1.0 - closed_form(cutoff, coordinate))
            for coordinate in range(1, 100_001)
        )
        print(f"N={cutoff:5.1f} finite_tail_distance={finite_tail:.12f}")
    print(f"worst_quadrature_error={worst:.3e}")


if __name__ == "__main__":
    main()

