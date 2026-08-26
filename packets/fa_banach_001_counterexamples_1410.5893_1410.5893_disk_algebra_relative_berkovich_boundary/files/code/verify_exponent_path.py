#!/usr/bin/env python3
"""Sanity checks for the valuation-exponent path used in the packet."""

from math import isclose


def value_at_zero(coefficients, exponent):
    constant = abs(coefficients[0]) if coefficients else 0
    return 0.0 if constant == 0 else constant**exponent


def main():
    exponents = [0.5, 0.9, 0.99, 0.999]
    polynomials = [
        [2],
        [-3, 7, 1],
        [0, 1],
        [5, 0, -4, 2],
    ]
    for coefficients in polynomials:
        target = value_at_zero(coefficients, 1.0)
        values = [value_at_zero(coefficients, nu) for nu in exponents]
        assert isclose(values[-1], target, rel_tol=2e-3, abs_tol=1e-12)
        print(coefficients, values, "->", target)
    for nu in exponents:
        assert 2**nu != 2
    print("all rescaled points fail the C_1 scalar restriction at the constant 2")


if __name__ == "__main__":
    main()
