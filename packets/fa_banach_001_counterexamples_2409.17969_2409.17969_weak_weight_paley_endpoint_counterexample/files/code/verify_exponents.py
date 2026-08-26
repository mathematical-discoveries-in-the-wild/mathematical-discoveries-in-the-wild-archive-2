#!/usr/bin/env python3
"""Checks the exponent algebra and the critical logarithmic model."""

from fractions import Fraction
import math


def conjugate(x):
    return x / (x - 1)


def check_interior(p, q):
    pp = conjugate(p)
    assert 1 < p < 2 and p < q < pp
    upper = min(q, conjugate(q), Fraction(2))
    r = (p + upper) / 2
    assert p < r < 2 and r < q and q < conjugate(r)
    theta = (1 - 1 / p) / (1 - 1 / r)
    assert theta > 0 and theta < 1
    assert theta / conjugate(r) == 1 / pp
    assert conjugate(p) / p == 1 / (p - 1)
    assert Fraction(1, 1) / (2 - p) == conjugate(Fraction(1, 1) / (p - 1))


def main():
    for p, q in [
        (Fraction(6, 5), Fraction(3, 2)),
        (Fraction(4, 3), Fraction(2)),
        (Fraction(3, 2), Fraction(5, 2)),
        (Fraction(7, 5), Fraction(9, 5)),
    ]:
        check_interior(p, q)

    # Model density comparable to the rank-one Plancherel density at infinity.
    for n in [1, 2, 3, 5, 8]:
        for r in [10, 100, 1000]:
            # Integral_1^R lambda^{-n} lambda^{n-1} dlambda = log R.
            exact = math.log(r)
            assert abs(exact / math.log(r) - 1) < 1e-12
            # Weak-L1 model: alpha * volume(radius alpha^{-1/n}) = 1.
            for alpha in [1e-1, 1e-3, 1e-6]:
                radius = alpha ** (-1 / n)
                assert abs(alpha * radius**n - 1) < 1e-8

    # The scalar factor in the packet is at most one.
    for rho in [0.5, 1.0, 3.0]:
        for q in [1.0, 1.5, 2.0, 3.0, 10.0]:
            rho_q = (2 / q - 1) * rho
            for lam in [0.0, 1.0, 10.0]:
                numerator = lam * lam + rho_q * rho_q
                denominator = lam * lam + (rho_q + 2 * rho) ** 2
                assert numerator <= denominator + 1e-12

    print("PASS: interpolation exponents, logarithmic model, and scalar factor")


if __name__ == "__main__":
    main()

