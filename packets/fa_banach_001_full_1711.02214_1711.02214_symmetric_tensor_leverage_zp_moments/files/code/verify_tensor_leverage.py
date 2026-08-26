#!/usr/bin/env python3
"""Numerical normalization checks for the symmetric-tensor leverage proof."""

from __future__ import annotations

import itertools
import math

import numpy as np


def multiindices(n: int, k: int):
    if n == 1:
        yield (k,)
        return
    for first in range(k + 1):
        for tail in multiindices(n - 1, k - first):
            yield (first,) + tail


def feature(x: np.ndarray, k: int) -> np.ndarray:
    """Coordinates for which <feature(x),feature(t)> = <x,t>**k."""
    n = len(x)
    out = []
    for alpha in multiindices(n, k):
        multinomial = math.factorial(k)
        monomial = 1.0
        for xi, ai in zip(x, alpha):
            multinomial /= math.factorial(ai)
            monomial *= xi**ai
        out.append(math.sqrt(multinomial) * monomial)
    return np.asarray(out)


def check_case(points: np.ndarray, weights: np.ndarray, k: int) -> tuple[int, float]:
    phis = np.stack([feature(x, k) for x in points])
    a = (phis.T * weights) @ phis
    a_pinv = np.linalg.pinv(a, rcond=1e-12)
    rank = int(np.linalg.matrix_rank(a, tol=1e-10))
    leverage = np.einsum("ij,jk,ik->i", phis, a_pinv, phis)

    trace_identity = float(weights @ leverage)
    if not np.isclose(trace_identity, rank, atol=2e-9, rtol=2e-9):
        raise AssertionError((trace_identity, rank))

    # In R^2 the rank-one supremum can be densely sampled on the unit circle.
    theta = np.linspace(0.0, 2.0 * np.pi, 60001, endpoint=False)
    directions = np.stack([np.cos(theta), np.sin(theta)], axis=1)
    projections = directions @ points.T
    denominator = np.sqrt((np.abs(projections) ** (2 * k)) @ weights)
    worst_ratio = 0.0
    for i, x in enumerate(points):
        numerator = np.abs(directions @ x) ** k
        sampled_sup_squared = float(np.max((numerator / denominator) ** 2))
        if sampled_sup_squared > leverage[i] * (1.0 + 3e-8) + 3e-8:
            raise AssertionError((sampled_sup_squared, leverage[i]))
        worst_ratio = max(worst_ratio, sampled_sup_squared / leverage[i])
    return rank, worst_ratio


def main() -> None:
    rng = np.random.default_rng(171102214)
    cases = 0
    minimum_ratio = 1.0
    for k in range(1, 6):
        for support_size in (2, 3, 5, 8):
            for _ in range(4):
                points = rng.normal(size=(support_size, 2))
                # Force several singular lifted moment matrices without making
                # the underlying two-dimensional support degenerate.
                points[0] += np.array([1.0, -0.4])
                points /= np.linalg.norm(points, axis=1, keepdims=True)
                raw = rng.uniform(0.1, 1.0, size=support_size)
                weights = raw / raw.sum()
                rank, ratio = check_case(points, weights, k)
                expected_dim = k + 1
                if rank > expected_dim:
                    raise AssertionError((rank, expected_dim))
                minimum_ratio = min(minimum_ratio, ratio)
                cases += 1
    print(f"PASS: {cases} finite-distribution cases")
    print("checked E leverage = rank, including singular lifted matrices")
    print(f"smallest sampled rank-one/full-tensor squared ratio: {minimum_ratio:.6f}")


if __name__ == "__main__":
    main()
