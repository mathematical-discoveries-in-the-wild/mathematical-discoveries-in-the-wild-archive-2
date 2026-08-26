#!/usr/bin/env python3
"""Stress-test the codimension-one Schatten approximation formula.

This script supplies numerical checks only.  The packet proof uses Schatten
Hölder duality and its equality case.
"""

from __future__ import annotations

import argparse

import numpy as np
from scipy.special import logsumexp


def schatten(matrix: np.ndarray, p: float) -> float:
    singular = np.linalg.svd(matrix, compute_uv=False)
    positive = singular[singular > 0]
    return float(np.exp(logsumexp(p * np.log(positive)) / p))


def formula_residual(
    g: np.ndarray, c: complex, p: float
) -> tuple[np.ndarray, np.ndarray]:
    u, singular, vh = np.linalg.svd(g, full_matrices=False)
    positive = singular > 1e-12 * singular[0]
    u = u[:, positive]
    singular = singular[positive]
    vh = vh[positive, :]
    phase = c / abs(c)
    q = p / (p - 1.0)
    denominator = np.sum(singular**q)
    residual_p = (
        phase
        * abs(c)
        / denominator
        * (u @ np.diag(singular ** (q - 1.0)) @ vh)
    )
    residual_strict = (
        phase * abs(c) / np.sum(singular) * (u @ vh)
    )
    return residual_p, residual_strict


def project_to_kernel(g: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    return matrix - g * (np.vdot(g, matrix) / np.vdot(g, g))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=260307498)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    max_feasibility_error = 0.0
    min_sampled_slack = np.inf
    max_p200_limit_error = 0.0

    for trial in range(args.trials):
        m, n = 3 + trial % 2, 4
        rank = 1 + trial % min(m, n)
        left, _ = np.linalg.qr(
            rng.normal(size=(m, rank)) + 1j * rng.normal(size=(m, rank))
        )
        right, _ = np.linalg.qr(
            rng.normal(size=(n, rank)) + 1j * rng.normal(size=(n, rank))
        )
        singular = np.exp(rng.uniform(-2.0, 1.0, size=rank))
        g = left @ np.diag(singular) @ np.conjugate(right).T
        a = rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))
        c = np.vdot(g, a)
        if abs(c) < 1e-8:
            continue

        for p in (2.0, 4.0, 10.0, 50.0, 200.0):
            residual, strict = formula_residual(g, c, p)
            max_feasibility_error = max(
                max_feasibility_error, abs(np.vdot(g, residual) - c)
            )
            base = schatten(residual, p)
            for _ in range(20):
                direction = rng.normal(size=(m, n)) + 1j * rng.normal(
                    size=(m, n)
                )
                direction = project_to_kernel(g, direction)
                scale = 10.0 ** rng.uniform(-3.0, 1.0)
                competitor = residual + scale * direction
                min_sampled_slack = min(
                    min_sampled_slack, schatten(competitor, p) - base
                )
            if p == 200.0:
                max_p200_limit_error = max(
                    max_p200_limit_error, np.linalg.norm(residual - strict, "fro")
                )

    print(f"trials={args.trials}")
    print(f"max_feasibility_error={max_feasibility_error:.3e}")
    print(f"min_sampled_optimality_slack={min_sampled_slack:.3e}")
    print(f"max_p200_to_strict_frobenius_error={max_p200_limit_error:.3e}")
    if max_feasibility_error > 1e-8 or min_sampled_slack < -1e-9:
        raise SystemExit("numerical check failed")


if __name__ == "__main__":
    main()
