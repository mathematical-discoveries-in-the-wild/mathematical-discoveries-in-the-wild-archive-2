#!/usr/bin/env python3
"""Random-start stress test for stationary roots in the source ring model.

This is numerical evidence only.  The packet proof is analytic.
"""

from __future__ import annotations

import argparse

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import root


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=float, default=2.2)
    parser.add_argument("--j1", type=float, default=1.5)
    parser.add_argument("--nodes", type=int, default=500)
    parser.add_argument("--starts", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument(
        "--lambdas",
        type=float,
        nargs="+",
        default=[1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 60, 100, 200],
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    a = np.sqrt(args.j1)
    q, weights = leggauss(args.nodes)
    x = (np.pi / 2) * q
    weights = weights / 2  # (1/pi) dx = (1/2) dq
    cosine = np.cos(args.alpha * x)
    sine = np.sin(args.alpha * x)

    def sigmoid0(z: np.ndarray) -> np.ndarray:
        return 0.5 * np.tanh(z / 2)

    def residual(v: np.ndarray, lam: float) -> np.ndarray:
        potential = v[0] + a * v[1] * cosine + a * v[2] * sine
        values = sigmoid0(lam * potential)
        return np.array(
            [
                v[0] + np.dot(weights, values),
                v[1] - a * np.dot(weights, values * cosine),
                v[2] - a * np.dot(weights, values * sine),
            ]
        )

    rng = np.random.default_rng(args.seed)
    for lam in args.lambdas:
        solutions: list[np.ndarray] = []
        for start in rng.uniform(-2, 2, (args.starts, 3)):
            candidate = root(lambda v: residual(v, lam), start, method="lm").x
            if np.linalg.norm(residual(candidate, lam)) >= 1e-9:
                continue
            if not any(np.linalg.norm(candidate - old) < 1e-5 for old in solutions):
                solutions.append(candidate)
        mixed = [
            v
            for v in solutions
            if abs(v[2]) > 1e-5 and np.linalg.norm(v[:2]) > 1e-5
        ]
        print(f"lambda={lam:g} roots={len(solutions)} mixed={len(mixed)}")


if __name__ == "__main__":
    main()
