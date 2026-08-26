#!/usr/bin/env python3
"""Finite audits for the diagonal Podles-sphere counterexample.

The proof in the packet is analytic.  This script only checks the indexing,
normalizations, boundary estimate, and finite Toeplitz matrix pattern.
"""

from __future__ import annotations

import math

import numpy as np


def f_value(q: float, k: int, terms: int = 500) -> float:
    return sum(
        (1.0 - q * q)
        * (q**j)
        * ((-1.0) ** j)
        / math.sqrt(1.0 - q ** (2 * j + 2))
        for j in range(k, k + terms)
    )


def normalized_difference(q: float, fk: float, fkp1: float, k: int) -> float:
    return (
        (fk - fkp1)
        * (q ** (-k))
        * math.sqrt(1.0 - q ** (2 * k + 2))
        / (1.0 - q * q)
    )


def audit(q: float, size: int = 18) -> None:
    values = [f_value(q, k) for k in range(size + 1)]
    weights = [
        normalized_difference(q, values[k], values[k + 1], k)
        for k in range(size)
    ]
    expected = np.array([(-1.0) ** k for k in range(size)])
    np.testing.assert_allclose(weights, expected, atol=1e-10, rtol=1e-10)

    # The derivative in the faithful representation is a backward weighted
    # shift.  Its first subdiagonal is exactly the normalized sequence.
    matrix = np.zeros((size + 1, size + 1))
    for k, weight in enumerate(weights):
        matrix[k, k + 1] = weight
    np.testing.assert_allclose(
        [matrix[k, k + 1] for k in range(size)], expected
    )

    # A truncation has one extra boundary weight.  It stays below the formal
    # geometric bound 1/(1-q), uniformly in the truncation level.
    boundary = []
    for n in range(size):
        b_n = (
            (q ** (-n))
            * math.sqrt(1.0 - q ** (2 * n + 2))
            * values[n]
            / (1.0 - q * q)
        )
        boundary.append(abs(b_n))
    assert max(boundary) <= 1.0 / (1.0 - q) + 1e-12

    # Alternation prevents convergence, hence this weighted shift cannot be
    # an element of the Toeplitz algebra.  This finite check is illustrative;
    # the proof uses the exact formula w_k=(-1)^k.
    assert all(abs(weights[k + 1] - weights[k]) > 1.9 for k in range(size - 1))

    print(
        f"q={q:.2f}: {size} exact normalized weights checked; "
        f"max truncation-boundary weight={max(boundary):.8f} "
        f"<= {1/(1-q):.8f}"
    )


def main() -> None:
    for q in (0.20, 0.50, 0.80, 0.95):
        audit(q)
    print("all finite normalization audits passed")


if __name__ == "__main__":
    main()
