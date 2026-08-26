#!/usr/bin/env python3
"""Finite exact sanity checks for the narrowing-cone counterexample."""

from fractions import Fraction
from math import fsum


def block(r: Fraction, s: Fraction, n: int) -> tuple[Fraction, Fraction]:
    return r + s, s / n


def coefficients(x: Fraction, y: Fraction, n: int) -> tuple[Fraction, Fraction]:
    return x - n * y, n * y


def dot(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> Fraction:
    return x[0] * y[0] + x[1] * y[1]


for n in range(1, 101):
    p = block(Fraction(1), Fraction(0), n)
    q = block(Fraction(0), Fraction(1), n)
    assert p == (1, 0)
    assert q == (1, Fraction(1, n))
    assert coefficients(*p, n) == (1, 0)
    assert coefficients(*q, n) == (0, 1)
    assert dot(p, p) > 0 and dot(p, q) > 0 and dot(q, q) > 0

    # Exhaust a small rational grid of cone elements and check acuteness.
    for a in range(4):
        for b in range(4):
            u = block(Fraction(a), Fraction(b), n)
            for c in range(4):
                for d in range(4):
                    w = block(Fraction(c), Fraction(d), n)
                    assert dot(u, w) >= 0

    # The nth block of z* is q_n-p_n=(0,1/n), with coefficients (-1,1).
    z = (Fraction(0), Fraction(1, n))
    assert (z[0], z[1]) == (q[0] - p[0], q[1] - p[1])
    assert coefficients(*z, n) == (-1, 1)

# Numerical convergence sanity check for the finite truncations z^(N).
partial_norm_squares = [fsum(1.0 / (n * n) for n in range(1, N + 1)) for N in (4, 16, 64, 256)]
assert all(a < b for a, b in zip(partial_norm_squares, partial_norm_squares[1:]))
tail_bound = fsum(1.0 / (n * n) for n in range(257, 200_001)) + 1.0 / 200_000
assert tail_bound < 1.0 / 256

print("all exact block, acuteness, coefficient, and truncation checks passed")
