#!/usr/bin/env python3
"""Finite sanity checks for the arithmetic-block proof; not a proof."""

from __future__ import annotations

import cmath
import random


def product(weights: list[complex], j: int, n: int) -> complex:
    """W_{j,n} with zero-based storage and mathematical j >= 1."""
    out = 1.0 + 0.0j
    for nu in range(1, n + 1):
        out *= weights[j + nu]
    return out


def main() -> None:
    rng = random.Random(241219115)
    length = 180
    weights = []
    for _ in range(3):
        weights.append(
            [1.0 + 0.0j]
            + [
                (1.15 + 0.4 * rng.random())
                * cmath.exp(1j * rng.uniform(-0.25, 0.25))
                for _ in range(length + 5)
            ]
        )

    checks = 0
    for s in range(3):
        for t in range(3):
            for j in range(1, 6):
                for n in (7, 19, 31):
                    for d in (8, 13, 27):
                        m = n + d
                        lhs = product(weights[s], j + d, n) / product(
                            weights[t], j, m
                        )
                        rhs = (
                            product(weights[s], j, m)
                            / product(weights[t], j, m)
                            / product(weights[s], j, d)
                        )
                        assert abs(lhs - rhs) < 1e-10 * max(1.0, abs(rhs))
                        checks += 1

    # A union of increasingly long M-spaced blocks has local densities
    # tending to 1/M along the block intervals.
    spacing = 11
    densities = []
    for q in (10, 30, 100, 300):
        block = {10000 * q + r * spacing for r in range(q + 1)}
        interval_length = q * spacing + 1
        densities.append(len(block) / interval_length)
    assert all(densities[i + 1] <= densities[i] for i in range(len(densities) - 1))
    assert abs(densities[-1] - 1 / spacing) < 5e-4

    print(f"verified {checks} cocycle/cross-tail identities")
    print("block densities:", ", ".join(f"{x:.6f}" for x in densities))
    print("finite sanity checks passed (not a proof)")


if __name__ == "__main__":
    main()
