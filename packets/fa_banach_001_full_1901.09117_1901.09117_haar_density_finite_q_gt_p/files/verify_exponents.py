#!/usr/bin/env python3
"""Finite checks for the discrete convolution in the Haar-density proof.

This is a sanity check, not a substitute for the analytic local-means lemma.
"""

from __future__ import annotations

import math


def weight(p: float, m: int) -> float:
    if m <= 0:
        return 2.0 ** (p * m)
    return 2.0 ** (-(1.0 - p) * m)


def mixed_cost(p: float, q: float, count: int) -> float:
    """Compute ||nu * W||_(q/p)^(1/p) on a safely truncated range."""
    r = q / p
    n0 = int(math.log2(count)) + 5
    levels = range(n0 + 1, n0 + count + 1)
    k_max = n0 + count + 240
    values = []
    for k in range(k_max + 1):
        conv = sum(weight(p, k - n) / count for n in levels)
        values.append(conv)
    return sum(v**r for v in values) ** (1.0 / q)


def main() -> None:
    samples = [
        (0.50, 0.75),
        (2.0 / 3.0, 0.80),
        (0.75, 0.90),
        (0.80, 1.40),
    ]
    counts = (32, 64, 128, 256)
    for p, q in samples:
        exponent = 1.0 / q - 1.0 / p
        assert q > p and exponent < 0.0
        costs = [mixed_cost(p, q, count) for count in counts]
        assert all(b < a for a, b in zip(costs, costs[1:]))
        normalized = [
            cost / (count**exponent)
            for count, cost in zip(counts, costs)
        ]
        assert max(normalized) / min(normalized) < 1.16
        print(
            f"p={p:.6f} q={q:.6f} exponent={exponent:.6f} "
            f"costs={[round(x, 6) for x in costs]} "
            f"normalized={[round(x, 6) for x in normalized]}"
        )

    print("All finite convolution and exponent checks passed.")


if __name__ == "__main__":
    main()
