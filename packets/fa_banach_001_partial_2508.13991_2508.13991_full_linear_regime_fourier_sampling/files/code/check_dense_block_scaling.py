#!/usr/bin/env python3
"""Numerically check the dense unsampled-block norm-ratio scaling.

The proof is analytic. This script only checks representative one-dimensional
frequency blocks after deleting half their frequencies.
"""

from __future__ import annotations

import argparse

import numpy as np


def lp_norm(values: np.ndarray, p: float) -> float:
    if np.isinf(p):
        return float(np.max(np.abs(values)))
    return float(np.mean(np.abs(values) ** p) ** (1.0 / p))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=40)
    parser.add_argument("--seed", type=int, default=250813991)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    pairs = ((2.0, 4.0), (3.0, 6.0), (2.0, np.inf))
    minima = {pair: np.inf for pair in pairs}
    max_removed_coefficient = 0.0

    for n_scale in (16, 32, 64, 128):
        frequencies = np.arange(n_scale, 2 * n_scale)
        grid = 2.0 * np.pi * np.arange(128 * n_scale) / (128 * n_scale)
        phases = np.exp(1j * np.outer(grid, frequencies))

        for _ in range(args.trials):
            kept = rng.choice(n_scale, size=n_scale // 2, replace=False)
            mask = np.zeros(n_scale, dtype=bool)
            mask[kept] = True
            values = np.sum(phases[:, mask], axis=1)
            coefficients = mask.astype(float)
            max_removed_coefficient = max(
                max_removed_coefficient,
                float(np.max(np.abs(coefficients[~mask]))),
            )

            for q, p in pairs:
                ratio = lp_norm(values, p) / lp_norm(values, q)
                expected_power = 1.0 / q - (0.0 if np.isinf(p) else 1.0 / p)
                scaled = ratio / (n_scale**expected_power)
                minima[(q, p)] = min(minima[(q, p)], scaled)

    print(f"trials_per_scale={args.trials}")
    print(f"max_removed_coefficient={max_removed_coefficient:.3e}")
    for (q, p), value in minima.items():
        p_label = "inf" if np.isinf(p) else f"{p:g}"
        print(f"min_scaled_ratio_q{q:g}_p{p_label}={value:.6f}")

    if max_removed_coefficient != 0.0 or min(minima.values()) <= 0.0:
        raise SystemExit("dense-block numerical check failed")


if __name__ == "__main__":
    main()
