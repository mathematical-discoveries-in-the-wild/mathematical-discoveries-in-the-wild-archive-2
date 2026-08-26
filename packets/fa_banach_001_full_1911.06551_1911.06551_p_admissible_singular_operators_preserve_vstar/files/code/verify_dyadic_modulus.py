#!/usr/bin/env python3
"""Stress-test the dyadic transition used in the V* preservation proof.

This numerically checks the exact geometric majorant. It is not a proof.
"""

from __future__ import annotations

import math


def exact_sum(a: float, eta: float, mass: float) -> float:
    """Evaluate sum_k min(eta, mass*2^(-a*k)) by its transition index."""
    if eta == 0.0 or mass == 0.0:
        return 0.0
    transition = math.ceil(math.log(mass / eta) / (a * math.log(2.0)))
    transition = max(0, transition)
    return transition * eta + mass * 2.0 ** (-a * transition) / (
        1.0 - 2.0 ** (-a)
    )


def majorant(a: float, eta: float, mass: float) -> float:
    if eta == 0.0 or mass == 0.0:
        return 0.0
    constant = 1.0 / (a * math.log(2.0)) + 1.0 + 1.0 / (
        1.0 - 2.0 ** (-a)
    )
    return constant * eta * (1.0 + math.log(mass / eta))


def main() -> None:
    checked = 0
    worst_ratio = 0.0
    for n in range(1, 13):
        for p_tenths in range(11, 81):
            p = p_tenths / 10.0
            for fraction in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9):
                lam = fraction * n
                a = (n - lam) / p
                for exponent in range(0, 15):
                    mass = 1.0
                    eta = 10.0 ** (-exponent)
                    lhs = exact_sum(a, eta, mass)
                    rhs = majorant(a, eta, mass)
                    if lhs > rhs * (1.0 + 1.0e-12):
                        raise AssertionError((n, p, lam, eta, lhs, rhs))
                    worst_ratio = max(worst_ratio, lhs / rhs if rhs else 0.0)
                    checked += 1

    # Independently sum far beyond the parameter-dependent transition and
    # compare against the exact infinite-series formula.
    for a in (0.01, 0.1, 0.5, 1.0, 3.0, 10.0):
        for exponent in (0, 1, 3, 10, 30, 100):
            eta = 10.0 ** (-exponent)
            transition = math.ceil(math.log(1.0 / eta) / (a * math.log(2.0)))
            terms = transition + math.ceil(50.0 / a)
            direct = sum(min(eta, 2.0 ** (-a * k)) for k in range(terms))
            exact = exact_sum(a, eta, 1.0)
            if not math.isclose(direct, exact, rel_tol=5.0e-12, abs_tol=1.0e-300):
                raise AssertionError((a, eta, direct, exact))
            checked += 1

    print(f"dyadic checks passed: {checked}")
    print(f"worst exact/majorant ratio: {worst_ratio:.12f}")
    print("vanishing samples eta*(1+log(1/eta)):")
    for exponent in (1, 2, 4, 8, 16, 32, 64):
        eta = 10.0 ** (-exponent)
        print(f"  1e-{exponent:02d}: {eta * (1.0 + math.log(1.0 / eta)):.6e}")


if __name__ == "__main__":
    main()
