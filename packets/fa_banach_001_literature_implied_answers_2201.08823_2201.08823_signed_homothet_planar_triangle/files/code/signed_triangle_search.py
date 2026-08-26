#!/usr/bin/env python3
"""Search mixed-sign homothetic covers of the standard triangle.

Numerical optimization uses a triangular grid.  Candidate covers are then
certified exactly up to floating-point LP tolerances by enumerating the three
possible separating inequalities for every homothet.
"""

from __future__ import annotations

import argparse
import itertools
import math

import numpy as np
from scipy.optimize import differential_evolution, linprog


def triangle_grid(q: int) -> np.ndarray:
    return np.array([(i / q, j / q) for i in range(q + 1) for j in range(q + 1 - i)])


def inside_scores(points: np.ndarray, translations: np.ndarray, coeffs: np.ndarray) -> np.ndarray:
    x = points[:, 0, None]
    y = points[:, 1, None]
    tx = translations[None, :, 0]
    ty = translations[None, :, 1]
    c = coeffs[None, :]
    positive = c > 0
    mu = np.abs(c)
    m1 = np.where(positive, x - tx, tx - x)
    m2 = np.where(positive, y - ty, ty - y)
    m3 = np.where(positive, tx + ty + mu - x - y, x + y - tx - ty + mu)
    return np.minimum(np.minimum(m1, m2), m3)


def exact_uncovered_margin(translations: np.ndarray, coeffs: np.ndarray):
    """Return largest common strict-violation margin and its LP witness."""
    pieces = []
    for (tx, ty), c in zip(translations, coeffs):
        if c > 0:
            A = np.array([[-1.0, 0.0], [0.0, -1.0], [1.0, 1.0]])
            b = np.array([-tx, -ty, tx + ty + c])
        else:
            mu = -c
            A = np.array([[1.0, 0.0], [0.0, 1.0], [-1.0, -1.0]])
            b = np.array([tx, ty, -tx - ty + mu])
        pieces.append((A, b))

    kA = np.array([[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [1.0, 1.0, 0.0]])
    kb = np.array([0.0, 0.0, 1.0])
    best = (-math.inf, None, None)
    for choices in itertools.product(range(3), repeat=len(pieces)):
        rows = [kA]
        rhs = [kb]
        for (A, b), j in zip(pieces, choices):
            # a.x >= b + delta, equivalently -a.x + delta <= -b.
            rows.append(np.array([[-A[j, 0], -A[j, 1], 1.0]]))
            rhs.append(np.array([-b[j]]))
        res = linprog(
            np.array([0.0, 0.0, -1.0]),
            A_ub=np.vstack(rows),
            b_ub=np.concatenate(rhs),
            bounds=[(None, None), (None, None), (-10.0, 10.0)],
            method="highs",
        )
        if res.success and res.x[2] > best[0]:
            best = (float(res.x[2]), res.x[:2].copy(), choices)
    return best


def optimize(coeffs: np.ndarray, grid_q: int, seed: int, maxiter: int, popsize: int):
    points = triangle_grid(grid_q)

    def objective(z):
        translations = np.asarray(z).reshape((-1, 2))
        cover_score = inside_scores(points, translations, coeffs).max(axis=1)
        # Maximize the least coverage margin.
        return -float(cover_score.min())

    result = differential_evolution(
        objective,
        [(-1.0, 2.0)] * (2 * len(coeffs)),
        seed=seed,
        maxiter=maxiter,
        popsize=popsize,
        tol=1e-9,
        polish=True,
        updating="immediate",
        workers=1,
    )
    translations = result.x.reshape((-1, 2))
    exact = exact_uncovered_margin(translations, coeffs)
    return result, translations, exact


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("coeffs", nargs="+", type=float)
    parser.add_argument("--grid-q", type=int, default=45)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--maxiter", type=int, default=250)
    parser.add_argument("--popsize", type=int, default=12)
    args = parser.parse_args()
    coeffs = np.array(args.coeffs, dtype=float)
    result, translations, exact = optimize(coeffs, args.grid_q, args.seed, args.maxiter, args.popsize)
    print("coefficients", coeffs.tolist(), "sum_abs", float(np.abs(coeffs).sum()))
    print("grid_objective", float(result.fun), "grid_min_margin", -float(result.fun))
    print("translations")
    for c, t in zip(coeffs, translations):
        print(f"  {c:+.12g}: ({t[0]:+.12g}, {t[1]:+.12g})")
    print("exact_max_uncovered_margin", exact[0])
    print("exact_witness", None if exact[1] is None else exact[1].tolist())
    print("exact_choices", exact[2])


if __name__ == "__main__":
    main()
