#!/usr/bin/env python3
"""Regression checks for the stretched-exponential Orlicz--Besov theorem."""

from fractions import Fraction
from math import floor


def check_power_exponential_family() -> int:
    checks = 0
    for n in range(2, 21):
        for p_num in range(2 * n + 1, 8 * n + 1):
            p = Fraction(p_num, 2)
            if p <= n:
                continue
            p_prime = p / (p - 1)
            # alpha=1 is always newly allowed.
            assert Fraction(1) < p_prime
            # A midpoint alpha between 1 and p' is also allowed.
            alpha = (Fraction(1) + p_prime) / 2
            assert 1 <= alpha < p_prime
            checks += 1
    return checks


def check_truncated_exponential_family() -> int:
    checks = 0
    for n in range(2, 21):
        # Exact gamma=1 endpoint.
        gamma = Fraction(1)
        m = floor(Fraction(n, 1) / gamma)
        q = gamma * (m + 1)
        assert q > n and gamma < q / (q - 1)
        checks += 1

        # Rational samples strictly below 1+1/n.
        for denominator in range(2, 31):
            gamma = Fraction(1) + Fraction(1, n * denominator)
            assert gamma < Fraction(n + 1, n)
            m = floor(Fraction(n, 1) / gamma)
            q = gamma * (m + 1)
            assert m == n - 1
            assert q > n
            assert gamma < q / (q - 1)
            checks += 1
    return checks


def check_geometric_recurrence() -> int:
    checks = 0
    for n in range(2, 21):
        ratio = 2 ** (-1 / (2 * n))
        geometric_constant = ratio / (1 - ratio)
        for k in range(2, 31):
            rho = 10.0 ** (-k)
            # Sum of C*rho^(1/(2n))*2^(-j/(2n)), with C=1.
            closed_form = rho ** (1 / (2 * n)) * geometric_constant
            partial = sum(
                rho ** (1 / (2 * n)) * 2 ** (-j / (2 * n))
                for j in range(1, 5000)
            )
            assert abs(partial - closed_form) <= 1e-10 * max(1.0, closed_form)
            checks += 1
    return checks


def main() -> None:
    a = check_power_exponential_family()
    b = check_truncated_exponential_family()
    c = check_geometric_recurrence()
    print(f"power-times-exponential parameter checks: {a}")
    print(f"truncated-exponential parameter checks: {b}")
    print(f"geometric recurrence checks: {c}")
    print("all exponent and recurrence checks passed")


if __name__ == "__main__":
    main()

