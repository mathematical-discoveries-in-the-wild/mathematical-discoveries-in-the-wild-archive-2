"""Optional finite-polynomial sanity check; not part of the proof."""

from __future__ import annotations

import numpy as np
from scipy.integrate import simpson


def trial(rng: np.random.Generator, n: int, grid: int = 200_001) -> float:
    a = rng.normal(size=n) / np.sqrt(np.arange(1, n + 1))
    t = np.linspace(1e-8, np.pi - 1e-8, grid)
    f = np.sin(np.outer(t, np.arange(1, n + 1))) @ a
    lhs = np.sum(a * a / np.arange(1, n + 1))
    integral = simpson(np.abs(f) ** 1.5 * np.sqrt(np.sin(t)), x=t)
    return float(lhs / integral ** (4.0 / 3.0))


if __name__ == "__main__":
    random = np.random.default_rng(12092970)
    for degree in (4, 8, 16, 32, 64):
        ratios = [trial(random, degree) for _ in range(8)]
        print(degree, max(ratios), np.mean(ratios))
