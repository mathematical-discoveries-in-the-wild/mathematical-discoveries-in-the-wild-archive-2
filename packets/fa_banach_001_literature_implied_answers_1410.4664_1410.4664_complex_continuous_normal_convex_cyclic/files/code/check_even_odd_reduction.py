#!/usr/bin/env python3
"""Exact checks for the even/odd convex-polynomial construction.

This verifies only the algebraic reduction used in the packet.  Density is
supplied by Feldman--McGuire, Theorem 7.1, and is not computational.
"""

from fractions import Fraction
import random


def random_convex_coefficients(rng: random.Random, degree: int) -> list[Fraction]:
    raw = [rng.randint(1, 50) for _ in range(degree + 1)]
    total = sum(raw)
    return [Fraction(value, total) for value in raw]


def evaluate(coefficients: list[Fraction], z: complex) -> complex:
    return sum(float(c) * z**k for k, c in enumerate(coefficients))


def combine(q: list[Fraction], s: list[Fraction]) -> list[Fraction]:
    degree = max(2 * (len(q) - 1), 2 * (len(s) - 1) + 1)
    p = [Fraction(0) for _ in range(degree + 1)]
    for k, coefficient in enumerate(q):
        p[2 * k] += coefficient / 2
    for k, coefficient in enumerate(s):
        p[2 * k + 1] += coefficient / 2
    return p


def main() -> None:
    rng = random.Random(14104664)
    trials = 1000
    for _ in range(trials):
        q = random_convex_coefficients(rng, rng.randint(0, 12))
        s = random_convex_coefficients(rng, rng.randint(0, 12))
        p = combine(q, s)
        assert all(coefficient >= 0 for coefficient in p)
        assert sum(p) == 1

        r = rng.uniform(1.01, 8.0)
        lhs = evaluate(p, 1j * r)
        rhs = 0.5 * evaluate(q, -(r**2)) + 0.5j * r * evaluate(s, -(r**2))
        assert abs(lhs - rhs) <= 1e-7 * max(1.0, abs(lhs), abs(rhs))

    print(f"PASS: {trials} exact coefficient checks and evaluation identities")


if __name__ == "__main__":
    main()
