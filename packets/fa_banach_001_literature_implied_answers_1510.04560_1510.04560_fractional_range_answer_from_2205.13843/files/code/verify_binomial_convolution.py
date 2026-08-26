#!/usr/bin/env python3
"""Exact finite-coefficient check for the packet's binomial Cauchy product."""

from fractions import Fraction


def rising(a: Fraction, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(n):
        out *= a + j
    return out


def falling(a: Fraction, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(n):
        out *= a - j
    return out


def factorial(n: int) -> int:
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def check(alpha: Fraction, degree: int = 40) -> None:
    c = [rising(alpha, n) / factorial(n) for n in range(degree + 1)]
    d = [(-1) ** n * falling(alpha, n) / factorial(n) for n in range(degree + 1)]
    conv = [sum((d[m] * c[k - m] for m in range(k + 1)), Fraction(0))
            for k in range(degree + 1)]
    expected = [Fraction(1)] + [Fraction(0)] * degree
    assert conv == expected
    print(f"alpha={alpha}: coefficients 0..{degree} PASS")


if __name__ == "__main__":
    for value in (Fraction(1, 7), Fraction(1, 3), Fraction(2, 5), Fraction(49, 100)):
        check(value)
    print("all exact convolution checks PASS")
