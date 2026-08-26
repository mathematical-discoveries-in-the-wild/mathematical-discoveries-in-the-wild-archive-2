#!/usr/bin/env python3
"""Monte Carlo regression check for the cone-measure concentration scale."""

from __future__ import annotations

import math
import numpy as np


def sample_ratios(p: float, n: int, k: int, samples: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out: list[np.ndarray] = []
    remaining = samples
    while remaining:
        batch = min(1000, remaining)
        y = rng.gamma(shape=1.0 / p, scale=1.0, size=(batch, n))
        shares = y / y.sum(axis=1, keepdims=True)
        kth_power = np.partition(shares, n - k, axis=1)[:, n - k]
        xk = kth_power ** (1.0 / p)
        scale = (math.log(math.e * n / k) / n) ** (1.0 / p)
        out.append(xk / scale)
        remaining -= batch
    return np.concatenate(out)


def main() -> None:
    samples = 12_000
    print("p n k q10 q50 q90 (ratios to [log(en/k)/n]^(1/p))")
    seed = 20260811
    for p in (0.5, 1.0, 2.0):
        for n in (200, 800):
            for k in (1, 5, max(10, n // 20)):
                ratios = sample_ratios(p, n, k, samples, seed)
                q10, q50, q90 = np.quantile(ratios, (0.1, 0.5, 0.9))
                print(f"{p:3.1f} {n:4d} {k:3d} {q10:7.3f} {q50:7.3f} {q90:7.3f}")
                seed += 1


if __name__ == "__main__":
    main()

