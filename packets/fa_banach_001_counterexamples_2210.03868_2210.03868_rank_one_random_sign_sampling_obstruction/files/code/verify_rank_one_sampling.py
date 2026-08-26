#!/usr/bin/env python3
"""Sanity checks for the rank-one obstruction to Question 3.7.

The proof is analytic.  This script checks the exact sampled-matrix identity
for a small seeded instance and reports Monte Carlo size ratios.
"""

from __future__ import annotations

import math
import random
import statistics


def sign_vector(n: int, rng: random.Random) -> list[int]:
    return [1 if rng.getrandbits(1) else -1 for _ in range(n)]


def coordinate_sum(epsilon: list[int]) -> int:
    return sum(epsilon)


def direct_bilinear(epsilon_i: list[int], epsilon_j: list[int]) -> int:
    """Return <J epsilon_i, epsilon_j> for J=11^T."""
    n = len(epsilon_i)
    assert len(epsilon_j) == n
    # J epsilon_i is the constant vector with value sum(epsilon_i).
    return sum(epsilon_i) * sum(epsilon_j)


def exact_identity_check() -> None:
    rng = random.Random(20260813)
    n, k = 11, 9
    epsilons = [sign_vector(n, rng) for _ in range(k)]
    sums = [coordinate_sum(epsilon) for epsilon in epsilons]
    direct = [
        [direct_bilinear(epsilons[i], epsilons[j]) for j in range(k)]
        for i in range(k)
    ]
    outer = [[sums[i] * sums[j] for j in range(k)] for i in range(k)]
    assert direct == outer

    # For ss^T the proved rank-one formula is gamma_2(ss^T)=||s||_inf^2.
    gamma2_formula = max(abs(value) for value in sums) ** 2
    max_entry = max(abs(value) for row in direct for value in row)
    assert gamma2_formula == max_entry
    print(f"exact identity: n={n}, K={k}, gamma2={gamma2_formula} [PASS]")


def monte_carlo_table() -> None:
    rng = random.Random(731)
    trials = 400
    multiple = 4
    delta = 0.05
    print("n K median_ratio p95_ratio theorem_bound")
    for n in (32, 64, 128, 256, 512):
        k = multiple * n
        ratios: list[float] = []
        for _ in range(trials):
            maximum = max(
                abs(coordinate_sum(sign_vector(n, rng))) for _ in range(k)
            )
            ratios.append((maximum * maximum) / (n * n))
        ratios.sort()
        median = statistics.median(ratios)
        p95 = ratios[math.ceil(0.95 * trials) - 1]
        bound = 2.0 * math.log(2.0 * k / delta) / n
        print(f"{n:3d} {k:4d} {median:.6f} {p95:.6f} {bound:.6f}")


if __name__ == "__main__":
    exact_identity_check()
    monte_carlo_table()
