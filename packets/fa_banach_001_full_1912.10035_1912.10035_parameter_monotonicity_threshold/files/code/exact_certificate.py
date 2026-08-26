#!/usr/bin/env python3
"""Exact certificates for the threshold bracket in the solution packet.

Only Python's integer and Fraction arithmetic is used.  The lower endpoint
certificate writes the fifth section in Bernstein form on each of 128 equal
subintervals.  Positivity of all Bernstein coefficients proves positivity of
the section throughout the full interval.
"""

from fractions import Fraction
from math import comb


def section_coefficients(a: Fraction, degree: int) -> list[Fraction]:
    coefficients = [Fraction(1)]
    denominator = Fraction(1)
    for k in range(1, degree + 1):
        denominator *= a**k + 1
        coefficients.append(Fraction((-1) ** k, 1) / denominator)
    return coefficients


def evaluate(coefficients: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def bernstein_coefficients_on_interval(
    coefficients: list[Fraction], left: Fraction, right: Fraction
) -> list[Fraction]:
    """Degree-n Bernstein coefficients after x=left+(right-left)t."""
    n = len(coefficients) - 1
    width = right - left
    power = []
    for j in range(n + 1):
        power.append(
            sum(
                coefficients[k]
                * comb(k, j)
                * left ** (k - j)
                * width**j
                for k in range(j, n + 1)
            )
        )
    return [
        sum(
            power[j] * Fraction(comb(i, j), comb(n, j))
            for j in range(i + 1)
        )
        for i in range(n + 1)
    ]


def lower_endpoint_certificate() -> None:
    a = Fraction(19821, 5000)  # 3.9642
    left, right = a + 1, a * a + 1
    coefficients = section_coefficients(a, 5)
    subdivision_count = 128
    all_bernstein = []
    for interval in range(subdivision_count):
        lo = left + (right - left) * Fraction(interval, subdivision_count)
        hi = left + (right - left) * Fraction(interval + 1, subdivision_count)
        all_bernstein.extend(
            bernstein_coefficients_on_interval(coefficients, lo, hi)
        )
    minimum = min(all_bernstein)
    assert len(all_bernstein) == 768
    assert minimum > 0
    print("lower a =", a, "=", float(a))
    print("Bernstein coefficients checked =", len(all_bernstein))
    print("minimum Bernstein coefficient =", minimum)
    print("minimum Bernstein coefficient (decimal) =", float(minimum))


def upper_endpoint_certificate() -> None:
    a = Fraction(39643, 10000)  # 3.9643
    x = Fraction(2, 3) * (a * a + 1)
    coefficients = section_coefficients(a, 6)
    value = evaluate(coefficients, x)
    assert a + 1 < x < a * a + 1
    assert value < 0
    print("upper a =", a, "=", float(a))
    print("test x = 2(a^2+1)/3 =", x)
    print("S_6(x) =", value)
    print("S_6(x) (decimal) =", float(value))


def derivative_pair_algebra_certificate() -> None:
    # The exceptional k=2 pair reduces to P(a)>0.  Expanding P(u+7/2)
    # gives the following coefficients, in increasing powers of u.  Compute
    # the translation here rather than trusting a pasted list.
    polynomial = [1, -1, 1, -6, 2, -4, -2, 1]  # coefficients of P(a)
    base = Fraction(7, 2)
    coefficients = [
        sum(
            Fraction(polynomial[k]) * comb(k, j) * base ** (k - j)
            for k in range(j, len(polynomial))
        )
        for j in range(len(polynomial))
    ]
    expected = [
        Fraction(90771, 128), Fraction(236319, 64),
        Fraction(156727, 32), Fraction(49107, 16),
        Fraction(8521, 8), Fraction(845, 4),
        Fraction(45, 2), Fraction(1),
    ]
    assert coefficients == expected
    assert all(coefficient > 0 for coefficient in coefficients)
    print("P(u+7/2) coefficients (constant first) =", coefficients)


if __name__ == "__main__":
    derivative_pair_algebra_certificate()
    lower_endpoint_certificate()
    upper_endpoint_certificate()
