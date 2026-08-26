#!/usr/bin/env python3
"""Numerical sanity checks for the circle shape-optimization packet.

The theorem proofs are exact; this script only illustrates their finite-grid
counterparts.
"""

from __future__ import annotations

import math
import random

import numpy as np


def checkerboard_grid(points: int, cells: int, fraction: float) -> np.ndarray:
    x = (np.arange(points) + 0.5) / points
    return ((x * cells) % 1.0 < fraction).astype(float)


def min_circular_window(values: np.ndarray, width: int) -> float:
    doubled = np.concatenate([values, values])
    sums = np.convolve(doubled, np.ones(width), mode="valid")[: len(values)]
    return float(np.min(sums) / width)


def fourier_flat_cells(cells: int, fraction: float, trials: int = 300) -> float:
    rng = random.Random(160701535 + cells)
    count = round(fraction * cells)
    best = float("inf")
    for _ in range(trials):
        chosen = rng.sample(range(cells), count)
        indicator = np.zeros(cells)
        indicator[chosen] = 1.0
        coeffs = np.fft.fft(indicator) / cells
        best = min(best, float(np.max(np.abs(coeffs[1:]))))
    return best


def main() -> None:
    fraction = 0.37
    points = 131_072
    window_fraction = math.sqrt(2.0) - 1.0
    width = round(window_fraction * points)
    for cells in (16, 64, 256, 1024):
        values = checkerboard_grid(points, cells, fraction)
        minimum = min_circular_window(values, width)
        print(
            f"checkerboard cells={cells:4d}: min window density={minimum:.7f}, "
            f"error={minimum-fraction:+.3e}"
        )

    for cells in (32, 64, 128, 256, 512):
        flatness = fourier_flat_cells(cells, fraction)
        print(f"random {cells:4d}-cell Fourier max={flatness:.6f}")

    # For L=1/2, a half-circle is an antipodal selector and all even
    # nonzero Fourier coefficients vanish on a sufficiently fine grid.
    grid = np.arange(points) / points
    selector = (grid < 0.5).astype(float)
    coeffs = np.fft.fft(selector) / points
    even_max = float(np.max(np.abs(coeffs[2:points // 2:2])))
    print(f"half-circle even Fourier max={even_max:.3e}")


if __name__ == "__main__":
    main()
