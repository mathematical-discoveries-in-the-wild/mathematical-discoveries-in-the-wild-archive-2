"""Finite-model checks for the arbitrary-index quasitubal theorem."""

from __future__ import annotations

import itertools
import numpy as np


def allocations(num_slices: int, max_rank: int, budget: int):
    for ranks in itertools.product(range(max_rank + 1), repeat=num_slices):
        if sum(ranks) <= budget:
            yield ranks


def check(seed: int = 20260811) -> None:
    rng = np.random.default_rng(seed)
    num_slices, m, p = 7, 4, 3
    slices = [
        rng.normal(size=(m, p)) + 1j * rng.normal(size=(m, p))
        for _ in range(num_slices)
    ]
    singular = [np.linalg.svd(a, compute_uv=False) for a in slices]
    all_values = sorted(
        (float(s) for values in singular for s in values), reverse=True
    )

    for budget in range(0, 9):
        global_error_sq = sum(s * s for s in all_values[budget:])
        allocation_error_sq = min(
            sum(
                float(np.dot(values[rank:], values[rank:]))
                for values, rank in zip(singular, ranks)
            )
            for ranks in allocations(num_slices, min(m, p), budget)
        )
        if not np.isclose(global_error_sq, allocation_error_sq, rtol=1e-11):
            raise AssertionError((budget, global_error_sq, allocation_error_sq))

        op_residual = all_values[budget] if budget < len(all_values) else 0.0
        if budget + 1 < len(all_values) and op_residual < all_values[budget + 1]:
            raise AssertionError("global singular values are not decreasing")

    # A finite-support vector is the exact finite shadow of an ell_2(I) vector.
    # Coordinate multiplication obeys the ideal and multiplier norm identities.
    x = rng.normal(size=30) + 1j * rng.normal(size=30)
    y = rng.normal(size=30) + 1j * rng.normal(size=30)
    a = rng.normal(size=30) + 1j * rng.normal(size=30)
    if np.linalg.norm(x * y) > np.linalg.norm(x) * np.linalg.norm(y) + 1e-12:
        raise AssertionError("ell_2 coordinate product bound failed")
    multiplier_ratio = np.linalg.norm(a * x) / np.linalg.norm(x)
    if multiplier_ratio > np.max(np.abs(a)) + 1e-12:
        raise AssertionError("diagonal multiplier bound failed")

    print("verified global rank-budget allocation for budgets 0..8")
    print("verified coordinate ideal and diagonal multiplier bounds")


if __name__ == "__main__":
    check()

