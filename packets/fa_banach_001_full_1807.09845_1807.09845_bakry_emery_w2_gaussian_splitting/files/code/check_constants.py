#!/usr/bin/env python3
"""Non-proof sanity checks for the Bakry--Emery W2 packet."""

from __future__ import annotations

import math

import numpy as np


def check_constants() -> None:
    assert (1.0 + math.sqrt(2.0) + 1.0 / 6.0) ** 2 < 7.0
    assert (1.0 + math.sqrt(7.0)) ** 2 < 14.0
    assert math.sqrt(168.0) < 13.0
    assert 6.0 * math.sqrt(3.0) < 13.0


def check_matrix_inequalities(trials: int = 2000, seed: int = 180709845) -> None:
    rng = np.random.default_rng(seed)
    worst_b_gap = float("inf")
    worst_trace_gap = float("inf")

    for _ in range(trials):
        n = int(rng.integers(2, 13))
        k = int(rng.integers(1, n + 1))

        q, _ = np.linalg.qr(rng.normal(size=(n, n)))
        eigenvalues = rng.uniform(0.0, 1.0, size=n)
        a = q @ np.diag(eigenvalues) @ q.T
        b = np.eye(n) - a

        b_gap = np.linalg.eigvalsh(np.eye(n) - a @ a - b @ b).min()
        worst_b_gap = min(worst_b_gap, float(b_gap))
        assert b_gap > -1e-10

        e, _ = np.linalg.qr(rng.normal(size=(n, k)))
        singular_values = rng.uniform(0.5, 2.0, size=k)
        rotation, _ = np.linalg.qr(rng.normal(size=(k, k)))
        w = e @ rotation @ np.diag(singular_values)
        p = e @ e.T

        lhs = float(np.trace(b @ b @ p))
        rhs = float(4.0 * np.trace(b @ b @ w @ w.T))
        trace_gap = rhs - lhs
        worst_trace_gap = min(worst_trace_gap, trace_gap)
        assert trace_gap > -1e-9

    print("constant_checks=passed")
    print(f"matrix_trials={trials}")
    print(f"minimum_B2_gap={worst_b_gap:.3e}")
    print(f"minimum_trace_gap={worst_trace_gap:.3e}")


if __name__ == "__main__":
    check_constants()
    check_matrix_inequalities()
