#!/usr/bin/env python3
"""Finite sanity checks for the leading-exponential argument.

This script does not verify the infinite-dimensional proof.
"""

from __future__ import annotations

import math
import random
from decimal import Decimal, getcontext


def falling_factorial_bound(base: float, p: float, terms: int = 300) -> float:
    total = 0.0
    factorial = 1.0
    for j in range(1, terms + 1):
        factorial *= j
        term = base ** (p * j) / factorial
        total += term
        if not math.isfinite(total):
            raise AssertionError("finite factorial-weighted partial sum overflowed")
    return total


def polynomial_value(
    monomials: list[tuple[tuple[int, ...], float]],
    values: list[Decimal],
) -> Decimal:
    total = Decimal(0)
    for powers, coefficient in monomials:
        term = Decimal(str(coefficient))
        for value, power in zip(values, powers):
            term *= value**power
        total += term
    return total


def check_cases(count: int = 2_000) -> None:
    getcontext().prec = 60
    rng = random.Random(12073818)
    # Logs of distinct primes are Q-linearly independent.
    thetas = [Decimal(2), Decimal(3), Decimal(5)]
    epsilons = [Decimal("0.17"), Decimal("0.11"), Decimal("0.07")]
    checked = 0
    for _ in range(count):
        powers_seen: set[tuple[int, ...]] = set()
        monomials: list[tuple[tuple[int, ...], float]] = []
        while len(monomials) < 5:
            powers = tuple(rng.randint(0, 3) for _ in range(3))
            if powers == (0, 0, 0) or powers in powers_seen:
                continue
            powers_seen.add(powers)
            coefficient = rng.choice([-3, -2, -1, 1, 2, 3])
            monomials.append((powers, coefficient))

        rates = [
            math.prod(theta**power for theta, power in zip(thetas, powers))
            for powers, _ in monomials
        ]
        winner = max(range(len(rates)), key=rates.__getitem__)
        max_rate = rates[winner]
        powers_star, coefficient_star = monomials[winner]
        leading_coefficient = coefficient_star * math.prod(
            eps**power for eps, power in zip(epsilons, powers_star)
        )

        # Bounded perturbations vary with j but stay uniformly bounded.
        ratios: list[Decimal] = []
        for j in (100, 200, 400, 800):
            bounded = [
                Decimal((j % 7) - 3) / Decimal(10),
                Decimal((j % 5) - 2) / Decimal(10),
                Decimal((j % 3) - 1) / Decimal(10),
            ]
            values = [
                h + eps * theta**j
                for h, eps, theta in zip(bounded, epsilons, thetas)
            ]
            value = polynomial_value(monomials, values)
            ratios.append(value / (leading_coefficient * max_rate**j))
        assert abs(ratios[-1] - Decimal(1)) < Decimal("1e-3")
        checked += 1

    assert checked == count


def main() -> None:
    check_cases()
    for p in (0.3, 0.8, 1.0, 1.7, 3.0):
        assert falling_factorial_bound(1.2, p) > 0.0
    print("PASS: 2000 unique-leading-rate perturbation cases")
    print("PASS: representative factorial-weighted p-sums for p<1 and p>=1")


if __name__ == "__main__":
    main()
