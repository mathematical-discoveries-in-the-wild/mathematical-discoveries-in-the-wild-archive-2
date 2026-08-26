#!/usr/bin/env python3
"""Grid-search and LP-check signed homothetic covers of a convex polygon."""

from __future__ import annotations

import argparse
import itertools
import math

import numpy as np
from scipy.optimize import differential_evolution, linprog
from scipy.spatial import ConvexHull


def polygon_halfspaces(vertices: np.ndarray):
    hull = ConvexHull(vertices)
    # scipy equations are normal.x + offset <= 0 with unit normals.
    return hull.equations[:, :2], -hull.equations[:, 2], vertices[hull.vertices]


def polygon_grid(A: np.ndarray, b: np.ndarray, vertices: np.ndarray, q: int):
    lo = vertices.min(axis=0)
    hi = vertices.max(axis=0)
    xx = np.linspace(lo[0], hi[0], q + 1)
    yy = np.linspace(lo[1], hi[1], q + 1)
    points = np.array([(x, y) for x in xx for y in yy])
    return points[np.max(points @ A.T - b, axis=1) <= 1e-12]


def piece_halfspaces(A, b, translation, coeff):
    t = np.asarray(translation)
    if coeff > 0:
        return A, coeff * b + A @ t
    mu = -coeff
    return -A, mu * b - A @ t


def exact_uncovered_margin(A, b, translations, coeffs):
    pieces = [piece_halfspaces(A, b, t, c) for t, c in zip(translations, coeffs)]
    m = len(A)
    kA = np.column_stack((A, np.zeros(m)))
    best = (-math.inf, None, None)
    for choices in itertools.product(range(m), repeat=len(pieces)):
        rows = [kA]
        rhs = [b]
        for (P, q), j in zip(pieces, choices):
            rows.append(np.array([[-P[j, 0], -P[j, 1], 1.0]]))
            rhs.append(np.array([-q[j]]))
        res = linprog(
            np.array([0.0, 0.0, -1.0]),
            A_ub=np.vstack(rows), b_ub=np.concatenate(rhs),
            bounds=[(None, None), (None, None), (-10.0, 10.0)], method="highs",
        )
        if res.success and res.x[2] > best[0]:
            best = (float(res.x[2]), res.x[:2].copy(), choices)
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vertices", required=True, help="semicolon-separated x,y pairs")
    parser.add_argument("--coeffs", nargs="+", required=True, type=float)
    parser.add_argument("--grid-q", type=int, default=50)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--maxiter", type=int, default=250)
    parser.add_argument("--popsize", type=int, default=12)
    args = parser.parse_args()
    vertices = np.array([[float(z) for z in pair.split(",")] for pair in args.vertices.split(";")])
    coeffs = np.array(args.coeffs)
    A, b, vertices = polygon_halfspaces(vertices)
    points = polygon_grid(A, b, vertices, args.grid_q)
    span = vertices.max(axis=0) - vertices.min(axis=0)
    lo = vertices.min(axis=0) - span
    hi = vertices.max(axis=0) + span

    def objective(z):
        translations = np.asarray(z).reshape((-1, 2))
        scores = []
        for t, c in zip(translations, coeffs):
            P, q = piece_halfspaces(A, b, t, c)
            # Signed inward margin to the closest facet (P rows remain unit).
            scores.append(np.min(q[None, :] - points @ P.T, axis=1))
        return -float(np.max(np.column_stack(scores), axis=1).min())

    bounds = [(lo[j], hi[j]) for _ in coeffs for j in range(2)]
    result = differential_evolution(
        objective, bounds, seed=args.seed, maxiter=args.maxiter,
        popsize=args.popsize, tol=1e-9, polish=True, workers=1,
    )
    translations = result.x.reshape((-1, 2))
    exact = exact_uncovered_margin(A, b, translations, coeffs)
    print("vertices", vertices.tolist())
    print("coefficients", coeffs.tolist(), "sum_abs", float(np.abs(coeffs).sum()))
    print("grid_min_margin", -float(result.fun))
    for c, t in zip(coeffs, translations):
        print(f"  {c:+.12g}: ({t[0]:+.12g}, {t[1]:+.12g})")
    print("exact_max_uncovered_margin", exact[0])
    print("exact_witness", None if exact[1] is None else exact[1].tolist())
    print("exact_choices", exact[2])


if __name__ == "__main__":
    main()
