#!/usr/bin/env python3
"""Numerically probe even-moment extremizers on one Boolean Fourier level."""

from itertools import combinations
import argparse
import numpy as np
from scipy.optimize import minimize


def walsh_level(n: int, a: int):
    points = np.arange(1 << n, dtype=np.uint64)
    sets = list(combinations(range(n), a))
    w = np.empty((1 << n, len(sets)), dtype=float)
    for j, subset in enumerate(sets):
        mask = sum(1 << k for k in subset)
        parity = np.fromiter(
            (((int(x) & mask).bit_count() & 1) for x in points),
            dtype=np.int8,
            count=1 << n,
        )
        w[:, j] = 1.0 - 2.0 * parity
    return w, sets


def optimize(n: int, a: int, p: int, restarts: int, seed: int):
    w, sets = walsh_level(n, a)
    d = w.shape[1]

    def normalized(x):
        return x / np.linalg.norm(x)

    def objective(x):
        c = normalized(x)
        vals = w @ c
        return -np.mean(vals ** p)

    def gradient(x):
        r = np.linalg.norm(x)
        c = x / r
        vals = w @ c
        grad_c = -(p / w.shape[0]) * (w.T @ (vals ** (p - 1)))
        return (grad_c - c * np.dot(c, grad_c)) / r

    rng = np.random.default_rng(seed)
    starts = [np.ones(d)]
    starts += [rng.normal(size=d) for _ in range(restarts)]
    best = None
    for start in starts:
        result = minimize(
            objective,
            start,
            jac=gradient,
            method="BFGS",
            options={"gtol": 1e-11, "maxiter": 4000},
        )
        c = normalized(result.x)
        moment = -objective(c)
        if best is None or moment > best[0]:
            best = moment, c, result.success, result.message

    sym = np.ones(d) / np.sqrt(d)
    sym_moment = -objective(sym)
    print(f"n={n} a={a} p={p} d={d}")
    print(f"symmetric moment={sym_moment:.15g}")
    print(f"best moment={best[0]:.15g} ratio={best[0]/sym_moment:.15g}")
    print(f"success={best[2]} message={best[3]}")
    order = np.argsort(-np.abs(best[1]))
    for j in order[: min(20, d)]:
        print(f"{sets[j]} {best[1][j]:+.12g}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("a", type=int)
    parser.add_argument("p", type=int)
    parser.add_argument("--restarts", type=int, default=30)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    optimize(args.n, args.a, args.p, args.restarts, args.seed)
