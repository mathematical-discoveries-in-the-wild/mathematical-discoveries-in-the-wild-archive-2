#!/usr/bin/env python3
"""Finite Fourier/grid sanity checks for the near-log Ornstein construction.

This script is not part of the proof.  It enumerates the Riesz-product Fourier
coefficients, applies the derivative multipliers, and estimates normalized L1
norms by a uniform FFT grid for small n and M.
"""

from __future__ import annotations

import argparse
from collections import defaultdict

import numpy as np


def riesz_coefficients(
    n: int, m: int
) -> tuple[dict[tuple[int, int], float], dict[tuple[int, int], float]]:
    coeffs: dict[tuple[int, int], float] = {(0, 0): 1.0}
    alternating: dict[tuple[int, int], float] = defaultdict(float)
    for k in range(1, n + 1):
        ax, ay = m**k, ((-1) ** k) * m**k
        updated: dict[tuple[int, int], float] = defaultdict(float)
        for (qx, qy), value in coeffs.items():
            updated[(qx, qy)] += value
            updated[(qx + ax, qy + ay)] += value / 2.0
            updated[(qx - ax, qy - ay)] += value / 2.0
            alternating[(qx + ax, qy + ay)] += ((-1) ** k) * value / 2.0
            alternating[(qx - ax, qy - ay)] += ((-1) ** k) * value / 2.0
        coeffs = dict(updated)
    coeffs[(0, 0)] -= 1.0
    return (
        {q: c for q, c in coeffs.items() if abs(c) > 1e-15},
        {q: c for q, c in alternating.items() if abs(c) > 1e-15},
    )


def grid_l1(
    coeffs: dict[tuple[int, int], complex], grid_size: int
) -> float:
    spectrum = np.zeros((grid_size, grid_size), dtype=np.complex128)
    for (qx, qy), value in coeffs.items():
        spectrum[qx % grid_size, qy % grid_size] += value
    values = np.fft.ifft2(spectrum) * (grid_size**2)
    return float(np.mean(np.abs(values)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--m", type=int, default=4)
    parser.add_argument("--grid", type=int, default=1024)
    args = parser.parse_args()

    r_hat, alternating_hat = riesz_coefficients(args.n, args.m)
    max_frequency = max(max(abs(x), abs(y)) for x, y in r_hat)
    if args.grid <= 2 * max_frequency:
        raise SystemExit(
            f"grid={args.grid} aliases max frequency {max_frequency}; "
            f"use grid > {2 * max_frequency}"
        )

    xx = dict(r_hat)
    xy = {(x, y): (y / x) * c for (x, y), c in r_hat.items()}
    yy = {(x, y): ((y / x) ** 2) * c for (x, y), c in r_hat.items()}

    xx_norm = grid_l1(xx, args.grid)
    xy_norm = grid_l1(xy, args.grid)
    yy_norm = grid_l1(yy, args.grid)
    alternating_norm = grid_l1(alternating_hat, args.grid)
    mixed_error = grid_l1(
        {q: xy.get(q, 0.0) - alternating_hat.get(q, 0.0) for q in r_hat},
        args.grid,
    )
    pure_error = grid_l1(
        {q: yy.get(q, 0.0) - r_hat.get(q, 0.0) for q in r_hat},
        args.grid,
    )
    ratio = xy_norm / (xx_norm + yy_norm)

    print(f"n={args.n} m={args.m} support={len(r_hat)} maxfreq={max_frequency}")
    print(f"||W_xx||_1 ≈ {xx_norm:.10f}")
    print(f"||W_xy||_1 ≈ {xy_norm:.10f}")
    print(f"||W_yy||_1 ≈ {yy_norm:.10f}")
    print(f"||alt main|| ≈ {alternating_norm:.10f}")
    print(f"mixed error  ≈ {mixed_error:.10f}")
    print(f"pure error   ≈ {pure_error:.10f}")
    print(f"ratio       ≈ {ratio:.10f}")


if __name__ == "__main__":
    main()
