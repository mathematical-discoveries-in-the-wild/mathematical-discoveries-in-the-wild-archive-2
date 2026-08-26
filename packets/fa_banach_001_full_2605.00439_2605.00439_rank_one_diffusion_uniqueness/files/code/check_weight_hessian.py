#!/usr/bin/env python3
"""Sanity check for the polynomial weight Hessian bound; not part of the proof."""

from __future__ import annotations

import math
import random


def directional_second(x: list[float], e: list[float], p: float) -> tuple[float, float]:
    radius2 = sum(value * value for value in x)
    norm_e2 = sum(value * value for value in e)
    dot = sum(a * b for a, b in zip(x, e))
    weight = (1.0 + radius2) ** (-p)
    exact = (
        -2.0 * p * norm_e2 * (1.0 + radius2) ** (-p - 1.0)
        + 4.0 * p * (p + 1.0) * dot * dot * (1.0 + radius2) ** (-p - 2.0)
    )
    return exact, weight


def main() -> None:
    generator = random.Random(260500439)
    for dimension in (1, 2, 5, 12):
        p = dimension / 2.0 + 1.0
        constant = 2.0 * p + 4.0 * p * (p + 1.0)
        worst_ratio = 0.0
        for _ in range(20_000):
            x = [generator.uniform(-100.0, 100.0) for _ in range(dimension)]
            e = [generator.uniform(-3.0, 3.0) for _ in range(dimension)]
            norm_e2 = sum(value * value for value in e)
            if norm_e2 == 0.0:
                continue
            exact, weight = directional_second(x, e, p)
            ratio = abs(exact) / (norm_e2 * weight)
            worst_ratio = max(worst_ratio, ratio)
            assert ratio <= constant * (1.0 + 1e-12)
        print(
            f"dimension={dimension} p={p:g} "
            f"sample_worst={worst_ratio:.8g} proof_constant={constant:g}"
        )
    print("all directional Hessian checks passed")


if __name__ == "__main__":
    main()
