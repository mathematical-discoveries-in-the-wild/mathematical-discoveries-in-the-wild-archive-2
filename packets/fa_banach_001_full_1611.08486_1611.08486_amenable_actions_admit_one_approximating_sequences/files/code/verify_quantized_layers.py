#!/usr/bin/env python3
"""Finite checks for the quantized level-set inequalities in the packet.

This script is only a regression/sanity check.  The packet contains the proof.
"""

from __future__ import annotations

import math
import random


def layer_count(value: float, delta: float, n_layers: int) -> int:
    return sum(value >= j * delta for j in range(1, n_layers + 1))


def main() -> None:
    rng = random.Random(161108486)
    scalar_cases = 50_000
    vector_cases = 5_000

    for _ in range(scalar_cases):
        maximum = 10 ** rng.uniform(-3.0, 3.0)
        n_layers = rng.randint(1, 500)
        delta = maximum / n_layers
        a = rng.random() * maximum
        b = rng.random() * maximum
        lhs = delta * abs(
            layer_count(a, delta, n_layers)
            - layer_count(b, delta, n_layers)
        )
        assert lhs <= abs(a - b) + delta + 1e-10 * max(1.0, maximum)

    for _ in range(vector_cases):
        size = rng.randint(1, 80)
        raw = [rng.expovariate(1.0) for _ in range(size)]
        total = sum(raw)
        p = [v / total for v in raw]
        maximum = max(p)
        n_layers = rng.randint(1, 500)
        delta = maximum / n_layers
        volume = sum(layer_count(v, delta, n_layers) for v in p)
        target = math.ceil(1.0 / delta)
        deficit = target - volume
        assert 0 <= deficit <= size + 1
        assert target >= 1.0 / delta

    print(
        "PASS: checked "
        f"{scalar_cases} scalar layer inequalities and "
        f"{vector_cases} discrete exact-volume bounds."
    )


if __name__ == "__main__":
    main()
