#!/usr/bin/env python3
"""Verify the exact Lagrange coefficient extractor used in the proof packet."""

from fractions import Fraction
from math import comb


def coefficients(k: int) -> list[Fraction]:
    harmonic = sum((Fraction(1, j) for j in range(1, k + 1)), Fraction())
    return [-harmonic] + [
        Fraction(((-1) ** (ell - 1)) * comb(k, ell), ell)
        for ell in range(1, k + 1)
    ]


def verify(k: int) -> None:
    coeffs = coefficients(k)
    for degree in range(k + 1):
        value = sum(
            (coeffs[ell] * (Fraction(ell) ** degree) for ell in range(k + 1)),
            Fraction(),
        )
        expected = Fraction(1 if degree == 1 else 0)
        if value != expected:
            raise AssertionError(
                f"k={k}, degree={degree}: got {value}, expected {expected}"
            )


def main() -> None:
    for k in range(1, 21):
        verify(k)
    print("PASS: exact coefficient extraction verified for 1 <= k <= 20")


if __name__ == "__main__":
    main()

