#!/usr/bin/env python3
"""Finite-truncation checks for the discrete RKHS counterexample.

This is a numerical sanity check only; the packet proof is exact.
"""

from __future__ import annotations

import math
import random


def objective(values: list[float]) -> float:
    return sum((x - 2.0 / n) ** 2 + x * x for n, x in enumerate(values, 1))


def main() -> None:
    rng = random.Random(240911679)
    for size in (10, 100, 1000, 10_000):
        optimizer = [1.0 / n for n in range(1, size + 1)]
        harmonic = sum(abs(x) for x in optimizer)
        square_norm = sum(x * x for x in optimizer)
        print(
            f"N={size:5d}  variation={harmonic:.9f}  "
            f"ell2_sq={square_norm:.9f}  J={objective(optimizer):.9f}"
        )

    size = 200
    optimizer = [1.0 / n for n in range(1, size + 1)]
    perturbation = [rng.uniform(-0.05, 0.05) for _ in range(size)]
    trial = [x + h for x, h in zip(optimizer, perturbation)]
    lhs = objective(trial) - objective(optimizer)
    rhs = 2.0 * sum(h * h for h in perturbation)
    if not math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError((lhs, rhs))
    print(f"complete-square residual: {lhs-rhs:+.3e}")


if __name__ == "__main__":
    main()
