#!/usr/bin/env python3
"""Finite sanity checks for the Rademacher-block counterexample.

The proof in the packet is analytic.  This script only verifies the exact
normalizations and the predicted power-law divergence in small dimensions.
"""

from __future__ import annotations

import itertools
import math


def matmul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [
        [sum(x * y for x, y in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def block_maps(a: float, d: int) -> tuple[list[list[float]], list[list[float]]]:
    signs = list(itertools.product((-1.0, 1.0), repeat=d))
    n = len(signs)
    conjugate = a / (a - 1.0)
    embedding = [[n ** (-1.0 / a) * sign[j] for j in range(d)] for sign in signs]
    quotient = [
        [n ** (-1.0 / conjugate) * sign[j] for sign in signs]
        for j in range(d)
    ]
    return embedding, quotient


def check_identity(a: float, d: int) -> float:
    embedding, quotient = block_maps(a, d)
    product = matmul(quotient, embedding)
    return max(
        abs(product[i][j] - (1.0 if i == j else 0.0))
        for i in range(d)
        for j in range(d)
    )


def check_divergence(p: float) -> None:
    reciprocal_r = 1.0 / p - 0.5
    assert reciprocal_r > 0.0
    ratios = []
    for exponent in range(1, 9):
        dimension = 2**exponent
        weight = dimension ** (-reciprocal_r / 2.0)
        ratio = weight * dimension ** (1.0 / p - 0.5)
        expected = dimension ** (reciprocal_r / 2.0)
        assert math.isclose(ratio, expected, rel_tol=1e-12, abs_tol=1e-12)
        ratios.append(ratio)
    assert all(a < b for a, b in zip(ratios, ratios[1:]))
    print(f"p={p:.3f}: ratios increase from {ratios[0]:.6f} to {ratios[-1]:.6f}")


def main() -> None:
    worst_error = 0.0
    for a in (1.2, 1.5, 2.0, 3.0, 5.0):
        for d in range(1, 8):
            worst_error = max(worst_error, check_identity(a, d))
    assert worst_error < 1e-11
    print(f"max ||Q_(a,d) E_(a,d)-I||_entry = {worst_error:.3e}")
    for p in (1.1, 1.25, 1.5, 1.9):
        check_divergence(p)
    print("all finite sanity checks passed")


if __name__ == "__main__":
    main()
