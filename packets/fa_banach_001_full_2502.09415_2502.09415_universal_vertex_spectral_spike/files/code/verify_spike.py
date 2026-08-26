#!/usr/bin/env python3
"""Reproducible checks for the universal-vertex spectral-spike theorem."""

from __future__ import annotations

import math

import numpy as np


def torus_distance(i: int, j: int, n: int) -> int:
    gap = abs(i - j)
    return min(gap, n - gap)


def simulated_check(seed: int = 250209415) -> None:
    rng = np.random.default_rng(seed)
    n, alpha, tau, sigma = 180, 0.15, 4.0, 1.5
    beta = tau - 1.0
    diameter = n // 2
    weights = 1.0 + rng.pareto(beta, size=n)
    saturated = np.flatnonzero(weights >= diameter**alpha)

    adjacency = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            distance = torus_distance(i, j, n)
            low, high = sorted((weights[i], weights[j]))
            kernel = high * low**sigma
            probability = min(kernel / distance**alpha, 1.0)
            edge = float(rng.random() < probability)
            adjacency[i, j] = adjacency[j, i] = edge

    if saturated.size:
        assert np.all(adjacency[saturated, :].sum(axis=1) == n - 1)
        anchor = saturated[0]
        for vertex in saturated[1:]:
            vector = np.zeros(n)
            vector[vertex], vector[anchor] = 1.0, -1.0
            assert np.allclose(adjacency @ vector, -vector)

    eigenvalues = np.linalg.eigvalsh(adjacency)
    multiplicity = int(np.count_nonzero(np.isclose(eigenvalues, -1.0, atol=1e-8)))
    assert multiplicity >= max(saturated.size - 1, 0)
    print(
        "seeded check:",
        f"saturated={saturated.size}",
        f"multiplicity(-1)={multiplicity}",
    )


def source_figure_calibration() -> None:
    n, alpha, tau = 5000, 0.1, 4.0
    diameter = n // 2
    q = diameter ** (-alpha * (tau - 1.0))
    expected = n * q
    c_n = 2.0 * sum(r ** (-alpha) for r in range(1, diameter))
    c_n += diameter ** (-alpha)
    print(
        "source Figure 1 (right):",
        f"E[M_N]={expected:.12f}",
        f"forced_mass~={(expected - 1.0) / n:.12f}",
        f"eigenvalue={-1.0 / math.sqrt(c_n):.12f}",
    )
    assert abs(expected - 478.1762498950183) < 1e-10
    assert abs(-1.0 / math.sqrt(c_n) + 0.019844326442737537) < 1e-12


if __name__ == "__main__":
    simulated_check()
    source_figure_calibration()
