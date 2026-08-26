#!/usr/bin/env python3
"""Arithmetic checks for the sparse adjacency witness (not part of the proof)."""

from __future__ import annotations

import math


def tree_rayleigh(q: int, radius: int) -> float:
    numerator = 2.0 * radius * (q + 1) / math.sqrt(q)
    denominator = 1.0 + radius * (q + 1) / q
    return numerator / denominator


def main() -> None:
    checks = 0
    for q in (2, 3, 7, 19):
        target = 2.0 * math.sqrt(q)
        previous = 0.0
        for radius in (1, 2, 5, 20, 100, 1000):
            value = tree_rayleigh(q, radius)
            assert previous < value < target
            previous = value
            checks += 1
        assert target - previous < 0.01

        for factors in (1, 2, 4):
            product_value = factors * tree_rayleigh(q, 1000)
            product_target = 2.0 * factors * math.sqrt(q)
            assert 0.0 < product_target - product_value < 0.04
            checks += 1

    q, n, q_prime, n_prime = 3, 2, 5, 4
    rho = 2.0 * n * math.sqrt(q)
    rho_prime = 2.0 * n_prime * math.sqrt(q_prime)
    t = 0.5 * (1.0 / rho + 1.0 / rho_prime)
    assert 1.0 - t * rho >= 0.0
    assert 1.0 - t * rho_prime < 0.0
    checks += 1

    star_size = math.floor(t ** -2) + 2
    star_minimum_eigenvalue = 1.0 - abs(t) * math.sqrt(star_size)
    assert star_minimum_eigenvalue < 0.0
    checks += 1

    print(f"arithmetic_checks={checks}")
    print(f"sample_separating_t={t:.12f}")
    print(f"infinite_star_size={star_size}")
    print(f"infinite_star_min_eigenvalue={star_minimum_eigenvalue:.12f}")
    print("status=PASS")


if __name__ == "__main__":
    main()
