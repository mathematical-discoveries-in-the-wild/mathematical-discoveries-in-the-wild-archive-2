"""Finite-cube sanity check for the sign-aligned even-moment inequality.

This is not part of the proof.
"""

from __future__ import annotations

import itertools
import random

import numpy as np


def walsh_matrix(n: int, masks: list[int]) -> np.ndarray:
    points = list(itertools.product((-1.0, 1.0), repeat=n))
    return np.asarray(
        [
            [
                np.prod([x[i] for i in range(n) if (mask >> i) & 1])
                for mask in masks
            ]
            for x in points
        ]
    )


def main() -> None:
    n, k = 6, 2
    masks = [mask for mask in range(1 << n) if mask.bit_count() >= k]
    degrees = np.asarray([mask.bit_count() for mask in masks], dtype=float)
    matrix = walsh_matrix(n, masks)
    rng = random.Random(14067855)
    worst = float("inf")
    for _ in range(500):
        coeffs = np.asarray([rng.random() for _ in masks])
        values = matrix @ coeffs
        laplacian_values = matrix @ (degrees * coeffs)
        ratio = np.mean(values**3 * laplacian_values) / np.mean(values**4)
        worst = min(worst, ratio / k)
    print(f"minimum sampled ratio E[f^3 Lf]/(k E[f^4]): {worst:.12f}")
    assert worst >= 1.0 - 1e-10


if __name__ == "__main__":
    main()

