#!/usr/bin/env python3
"""Finite-dimensional checks for the 1508.04702 Problem 2 counterexample."""

from __future__ import annotations

import numpy as np


def trace_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def doi(table: np.ndarray) -> np.ndarray:
    """Ordered 2-by-2 DOI sum table[i,j] P_i Q_j at angle pi/4."""
    p = np.array([[1.0, 0.0], [0.0, 0.0]])
    q = 0.5 * np.array([[1.0, 1.0], [1.0, 1.0]])
    ps = (p, np.eye(2) - p)
    qs = (q, np.eye(2) - q)
    return sum(table[i, j] * ps[i] @ qs[j] for i in range(2) for j in range(2))


def main() -> None:
    p = np.array([[1.0, 0.0], [0.0, 0.0]])
    q = 0.5 * np.array([[1.0, 1.0], [1.0, 1.0]])
    c = q @ p - p @ q
    assert abs(trace_norm(c) - 1.0) < 1e-14

    rng = np.random.default_rng(150804702)
    for _ in range(1000):
        table = rng.normal(size=(2, 2))
        t = doi(table)
        delta = table[0, 0] - table[0, 1] - table[1, 0] + table[1, 1]
        np.testing.assert_allclose(t.T - t, delta * c, atol=2e-14, rtol=2e-14)
        assert abs(trace_norm(t.T - t) - abs(delta)) < 5e-14

    # Exact asymptotic formulas are:
    # commutator partial sum = sum_{k<=K} k*2^k*(2^{-k-4})^2,
    # defect partial sum     = (1/16) sum_{k<=K} 1/k.
    previous_comm = 0.0
    previous_defect = 0.0
    for cutoff in (8, 16, 32, 64, 128, 256):
        comm = sum(k * 2**k * 2.0 ** (-2 * k - 8) for k in range(1, cutoff + 1))
        defect = sum(1.0 / (16 * k) for k in range(1, cutoff + 1))
        assert previous_comm <= comm < 1.0 / 128.0 + 1e-15
        assert defect > previous_defect
        previous_comm, previous_defect = comm, defect
        print(f"K={cutoff:3d} comm={comm:.15f} defect={defect:.15f}")

    assert abs(sum(k * 2.0 ** (-k - 8) for k in range(1, 1000)) - 1 / 128) < 1e-14
    print("PASS: block identity, trace norms, and partial-sum behavior verified")


if __name__ == "__main__":
    main()
