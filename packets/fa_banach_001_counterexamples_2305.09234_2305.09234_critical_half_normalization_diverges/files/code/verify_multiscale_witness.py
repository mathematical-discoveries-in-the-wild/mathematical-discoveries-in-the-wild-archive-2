#!/usr/bin/env python3
"""Regression checks for the critical alpha=1/2 assignment packet.

The proof is analytic.  This script checks the exact moment formulas, samples
the universal Hoelder bound for signed dyadic tent sums, and confirms on small
random instances that the constructed dual witness never exceeds the primal
Hungarian assignment cost after division by the proved constant 14.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.optimize import linear_sum_assignment


def tents(x: np.ndarray, level: int) -> np.ndarray:
    """Values of all unit dyadic tents at one level."""
    cells = 2**level
    centers = (np.arange(cells) + 0.5) / cells
    return np.maximum(1.0 - 2.0 * cells * np.abs(x[:, None] - centers), 0.0)


def witness_discrepancy(x: np.ndarray, y: np.ndarray, levels: int) -> float:
    """Unnormalised signed multiscale dual value."""
    total = 0.0
    for level in range(levels):
        discrepancy = tents(x, level).sum(axis=0) - tents(y, level).sum(axis=0)
        total += 2.0 ** (-level / 2.0) * np.abs(discrepancy).sum()
    return float(total)


def evaluate_signed_sum(grid: np.ndarray, signs: list[np.ndarray]) -> np.ndarray:
    values = np.zeros_like(grid)
    for level, level_signs in enumerate(signs):
        values += 2.0 ** (-level / 2.0) * tents(grid, level) @ level_signs
    return values


def check_exact_moments() -> None:
    for level in range(14):
        h = 2.0**(-level)
        first = h / 2.0
        second = h / 3.0
        variance_difference = 2.0 * (second - first**2)
        assert variance_difference >= h / 6.0 - 1e-15
        # If n h >= 12, then n Var(Z) >= 2, exactly the threshold used
        # to turn E[S^4] <= nv + 3 (nv)^2 into E[S^4] <= 4 (nv)^2.
        n = math.ceil(12.0 / h)
        nv = n * variance_difference
        assert nv >= 2.0 - 1e-12
        assert nv + 3.0 * nv**2 <= 4.0 * nv**2 + 1e-10


def check_hoelder_bound(rng: np.random.Generator) -> float:
    grid = np.linspace(0.0, 1.0, 4097)
    worst = 0.0
    for _ in range(12):
        signs = [rng.choice([-1.0, 1.0], size=2**j) for j in range(10)]
        values = evaluate_signed_sum(grid, signs)
        left = rng.integers(0, len(grid) - 1, size=250_000)
        right = rng.integers(1, len(grid), size=250_000)
        lo = np.minimum(left, right)
        hi = np.maximum(left, right)
        keep = lo != hi
        ratios = np.abs(values[hi[keep]] - values[lo[keep]]) / np.sqrt(
            grid[hi[keep]] - grid[lo[keep]]
        )
        worst = max(worst, float(ratios.max(initial=0.0)))
    assert worst <= 14.0 + 1e-12
    return worst


def check_primal_dual(rng: np.random.Generator) -> list[tuple[int, float, float]]:
    summaries: list[tuple[int, float, float]] = []
    for n in (32, 64, 128, 256):
        ratios = []
        scaled = []
        levels = max(1, math.floor(math.log2(n / 12.0)) + 1)
        for _ in range(20):
            x = rng.random(n)
            y = rng.random(n)
            cost = np.sqrt(np.abs(x[:, None] - y[None, :]))
            rows, cols = linear_sum_assignment(cost)
            primal = float(cost[rows, cols].sum())
            dual = witness_discrepancy(x, y, levels) / 14.0
            assert dual <= primal + 1e-9
            ratios.append(dual / primal)
            scaled.append(primal / (math.sqrt(n) * math.log(n)))
        summaries.append((n, float(np.median(ratios)), float(np.median(scaled))))
    return summaries


def main() -> None:
    rng = np.random.default_rng(230509234)
    check_exact_moments()
    worst = check_hoelder_bound(rng)
    summaries = check_primal_dual(rng)
    print("exact moment inequalities: PASS (levels 0..13)")
    print(f"sampled signed-sum Hoelder ratio: {worst:.6f} <= 14")
    print("primal-dual checks: PASS (20 trials per n)")
    for n, median_fraction, median_scaled in summaries:
        print(
            f"n={n:3d}  median((witness/14)/M)={median_fraction:.6f}  "
            f"median(M/(sqrt(n) log n))={median_scaled:.6f}"
        )
    print("All regression checks passed.  These checks supplement, not replace, the proof.")


if __name__ == "__main__":
    main()
