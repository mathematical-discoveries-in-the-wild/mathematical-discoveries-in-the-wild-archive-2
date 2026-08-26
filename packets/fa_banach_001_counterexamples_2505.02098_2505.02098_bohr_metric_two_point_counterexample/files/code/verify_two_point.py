#!/usr/bin/env python3
"""Numerical sanity checks for the two-point Bohr-metric counterexample."""

from fractions import Fraction
import cmath

import mpmath as mp


def first_primes(count: int) -> list[int]:
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def rho(a: complex, b: complex) -> float:
    return abs((a - b) / (1 - a.conjugate() * b))


def blaschke(z: complex) -> complex:
    return (0.5 - z) / (1 - 0.5 * z)


def main() -> None:
    mp.mp.dps = 80
    r = Fraction(3, 10)
    classical_det = (1 - r * r) / 8 - Fraction(1, 9)
    assert classical_det == Fraction(19, 7200)

    zeta_ratio = mp.zeta(3) ** 2 / (mp.zeta(2) * mp.zeta(4))
    assert zeta_ratio < mp.mpf(8) / 9 < 1 - mp.mpf(9) / 100

    primes = first_primes(25)
    distances = [mp.mpf(p) / (p * p + p + 1) for p in primes]
    assert distances[0] == mp.mpf(2) / 7
    assert all(a > b for a, b in zip(distances, distances[1:]))
    assert mp.mpf(3) / 10 > distances[0]

    assert abs(blaschke(0.5)) < 1e-15
    assert abs(blaschke(0.25) - 2 / 7) < 1e-15
    for k in range(200):
        z = 0.999999 * cmath.exp(2j * mp.pi * k / 200)
        assert abs(blaschke(z)) < 1.000001

    print(f"classical determinant at r=3/10: {classical_det}")
    print(f"zeta ratio: {mp.nstr(zeta_ratio, 30)}")
    print(f"largest prime-coordinate distance: {mp.nstr(distances[0], 30)}")
    print("explicit B values: B(1/2)=0, B(1/4)=2/7")
    print("all checks passed")


if __name__ == "__main__":
    main()
