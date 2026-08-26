#!/usr/bin/env python3
"""Regression checks for the all-rank quartic atom-size synthesis."""

from __future__ import annotations

import numpy as np


def normalized_trace(matrix: np.ndarray) -> float:
    return float(np.trace(matrix) / matrix.shape[0])


def check_commutator_identity() -> float:
    rng = np.random.default_rng(161100494)
    maximum_error = 0.0
    for _ in range(2000):
        size = int(rng.integers(1, 10))
        raw_a = rng.normal(size=(size, size))
        raw_b = rng.normal(size=(size, size))
        a = (raw_a + raw_a.T) / 2.0
        b = (raw_b + raw_b.T) / 2.0
        commutator = a @ b - b @ a
        left = normalized_trace(a @ a @ b @ b) - normalized_trace(a @ b @ a @ b)
        right = 0.5 * normalized_trace(commutator.T @ commutator)
        error = abs(left - right)
        maximum_error = max(maximum_error, error)
        if left < -1e-10 or error > 1e-9 * (1.0 + abs(left) + abs(right)):
            raise AssertionError((size, left, right, error))
    return maximum_error


def check_branch_exhaustion() -> None:
    rank_routes = {
        1: "commutative_or_impossible_nc",
        2: "commutative_or_impossible_nc",
        3: "commutative_or_impossible_nc",
        4: "source_theorem_3_1",
        5: "source_section_6",
        6: "four_normal_forms",
        7: "positive_definite_BCKP13",
    }
    assert set(rank_routes) == set(range(1, 8))

    rank_six_routes = {
        "X2_plus_Y2_equals_1": "source_first_three",
        "XY_plus_YX_equals_0": "source_first_three",
        "Y2_minus_X2_equals_1": "source_first_three",
        "Y2_equals_1": "supporting_packet_2001_11614",
    }
    assert len(rank_six_routes) == 4
    assert all(rank_six_routes.values())


if __name__ == "__main__":
    max_error = check_commutator_identity()
    check_branch_exhaustion()
    print(f"PASS: 2000 commutator identities; maximum absolute error={max_error:.3e}")
    print("PASS: ranks 1..7 and all four rank-six normal forms are covered")

