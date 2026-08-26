#!/usr/bin/env python3
"""Finite diagnostics for the stopped-martingale Heisenberg curve.

The proof is analytic.  This script checks its scale formula and a finite
piecewise-constant realization; it is not a substitute for the proof.
"""

from __future__ import annotations

import math

import numpy as np


def exponent_checks() -> None:
    for alpha in (2.0, 3.0, 3.8):
        p = 0.5 * (0.5 + 2.0 / alpha)
        q = alpha / 2.0
        assert 2.0 * p > 1.0
        assert p * q < 1.0
        square_sum = sum(j ** (-2.0 * p) for j in range(1, 200_001))
        energy_sum = sum(j ** (-p * q) for j in range(1, 200_001))
        print(
            f"alpha={alpha:.1f} p={p:.6f} "
            f"partial_square_sum={square_sum:.6f} "
            f"partial_energy_sum={energy_sum:.6f}"
        )


def exact_haar_check() -> None:
    # For y in [0,1/8], x in [7/8,1], the unit Haar contribution is
    # (2x-1)(1-2y)/4 and therefore at least 9/64.
    grid = np.linspace(0.0, 0.125, 257)
    vals = []
    for y in grid:
        for x in 1.0 - grid:
            vals.append((2.0 * x - 1.0) * (1.0 - 2.0 * y) / 4.0)
    minimum = min(vals)
    assert abs(minimum - 9.0 / 64.0) < 1e-14
    tail_bound = 3.0 / (2**8 - 1)
    assert tail_bound < 0.5 * minimum
    print(f"haar_min={minimum:.12f} tail_bound={tail_bound:.12f}")


def finite_curve_check() -> None:
    alpha = 3.0
    p = 0.5 * (0.5 + 2.0 / alpha)
    c = 0.05
    spacing = 4
    stages = 4
    # Four unused terminal bits make the outer-eighth test points exact even
    # for the last updated parent interval.
    final_level = spacing * stages + 4
    cells = 2**final_level
    index = np.arange(cells, dtype=np.int64)
    martingale = np.zeros(cells, dtype=float)
    active = np.ones(cells, dtype=bool)
    active_at_stage: list[np.ndarray] = []
    epsilons: list[float] = []

    for j in range(1, stages + 1):
        active_at_stage.append(active.copy())
        eps = c * j ** (-p)
        epsilons.append(eps)
        level = spacing * j
        bit = (index >> (final_level - level)) & 1
        rademacher = 1.0 - 2.0 * bit
        martingale += eps * active * rademacher
        active &= np.abs(martingale) < 0.5

    dx = 1.0 / cells
    f = np.zeros(cells + 1)
    f[1:] = np.cumsum(martingale) * dx
    primitive = np.zeros(cells + 1)
    primitive[1:] = np.cumsum(f[:-1] * dx + 0.5 * martingale * dx * dx)

    minima = []
    for j in range(1, stages + 1):
        level = spacing * j
        parent_cells = 2 ** (final_level - (level - 1))
        eps = epsilons[j - 1]
        ratios = []
        for start in range(0, cells, parent_cells):
            if not active_at_stage[j - 1][start]:
                continue
            y = start + parent_cells // 8
            x = start + 7 * parent_cells // 8
            h = (x - y) * dx
            error = primitive[x] - primitive[y] - 0.5 * (f[x] + f[y]) * h
            ell = parent_cells * dx
            ratios.append(abs(error) / (eps * ell * ell))
        minima.append(min(ratios))

    # Spacing four is deliberately smaller than the proof's spacing eight,
    # so this is a reasonably adversarial finite test.
    print("raw_finite_min_ratios=" + ",".join(f"{v:.8f}" for v in minima))
    assert min(minima) > 0.08
    variance_budget = sum(e * e for e in epsilons)
    assert np.max(np.abs(martingale)) < 0.5
    print(
        "finite_min_ratios=" + ",".join(f"{v:.8f}" for v in minima),
        f"finite_variance={variance_budget:.8f}",
        f"finite_active_fraction={active.mean():.8f}",
    )


if __name__ == "__main__":
    exact_haar_check()
    exponent_checks()
    finite_curve_check()
    print("all finite diagnostics passed")
