#!/usr/bin/env python3
"""Finite-dimensional sanity check for the thickened-ball obstruction.

For small real matrices this enumerates sample sets and vertices of the
sampling polytope, computes the best one-sided constant numerically, and
checks the zero-data pair used in the converse proof.
"""

from itertools import combinations, product

import numpy as np


def lp_norm(v: np.ndarray, weights: np.ndarray, p: float) -> float:
    return float(np.sum(weights * np.abs(v) ** p) ** (1.0 / p))


def sample_constant(a: np.ndarray, weights: np.ndarray, sample, p: float):
    """Return max ||A c||_p subject to |A_sample c| <= 1 and a maximizer."""
    s = a[list(sample), :]
    n = a.shape[1]
    if np.linalg.svd(s, compute_uv=False)[-1] < 1e-9:
        return float("inf"), None

    best = -1.0
    best_c = None
    for active in combinations(range(len(sample)), n):
        block = s[list(active), :]
        if abs(np.linalg.det(block)) < 1e-10:
            continue
        for signs in product((-1.0, 1.0), repeat=n):
            c = np.linalg.solve(block, np.asarray(signs))
            if np.max(np.abs(s @ c)) <= 1.0 + 1e-8:
                value = lp_norm(a @ c, weights, p)
                if value > best:
                    best, best_c = value, c
    assert best_c is not None
    return best, best_c


def run(phase: float, p: float = 3.5, points: int = 16, dim: int = 2, m: int = 2):
    assert dim == 2
    theta = phase + 2.0 * np.pi * np.arange(points) / points
    a = np.column_stack((np.cos(theta), np.sin(theta)))
    weights = np.full(points, 1.0 / points)

    records = []
    for sample in combinations(range(points), m):
        d_sample, c = sample_constant(a, weights, sample, p)
        records.append((d_sample, sample, c))
    d_best = min(record[0] for record in records)
    assert np.isfinite(d_best) and d_best > 1.0 + 1e-8
    epsilon = 1.0 / d_best

    for d_sample, sample, c in records:
        if c is None:
            _, _, vh = np.linalg.svd(a[list(sample), :])
            c = vh[-1]
        x = a @ c
        x /= lp_norm(x, weights, p)
        assert np.max(np.abs(x[list(sample)])) <= epsilon + 2e-7

        h = np.zeros(points)
        h[list(sample)] = -x[list(sample)]
        f = x + h
        assert np.max(np.abs(h)) <= epsilon + 2e-7
        assert np.max(np.abs(f[list(sample)])) <= 2e-7
        assert lp_norm(f, weights, p) + 2e-7 >= 1.0 - epsilon
        assert lp_norm(f, weights, p) / epsilon + 2e-6 >= d_best - 1.0

    return d_best, len(records)


if __name__ == "__main__":
    for seed in range(20):
        phase = seed * np.pi / 317.0
        d_best, count = run(phase)
        print(f"phase={phase:.8f} sample_sets={count:3d} D_best={d_best:.8f}")
    print("ALL FINITE OBSTRUCTION CHECKS PASSED")
