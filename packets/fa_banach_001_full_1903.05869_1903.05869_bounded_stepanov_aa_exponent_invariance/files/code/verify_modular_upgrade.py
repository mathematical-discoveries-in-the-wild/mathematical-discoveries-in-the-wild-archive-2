#!/usr/bin/env python3
"""Finite-grid checks for the modular inequality used in the proof."""

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(190305869)
    checks = 0
    for grid_size in (127, 509, 2039):
        for _ in range(400):
            p = rng.uniform(1.0, 9.0, size=grid_size)
            p_plus = float(p.max())
            bound = float(rng.uniform(0.05, 4.0))
            epsilon = float(rng.uniform(0.02, 3.0))
            difference = rng.uniform(0.0, bound, size=grid_size)
            difference *= rng.random(grid_size) < rng.uniform(0.001, 0.2)
            u = difference / epsilon
            modular = float(np.mean(u**p))
            rhs = (1.0 + (bound / epsilon) ** (p_plus - 1.0)) * float(
                np.mean(difference)
            ) / epsilon
            if modular > rhs * (1.0 + 2e-12) + 2e-12:
                raise AssertionError((modular, rhs))
            checks += 1
    print(f"PASS: {checks} variable-exponent modular checks")
    print("verified rho(u/eps) <= [1+(B/eps)^(p+-1)] ||u||_1/eps")


if __name__ == "__main__":
    main()
