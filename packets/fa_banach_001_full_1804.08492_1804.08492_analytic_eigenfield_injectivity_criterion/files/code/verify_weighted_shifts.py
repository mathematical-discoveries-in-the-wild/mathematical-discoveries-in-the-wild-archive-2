#!/usr/bin/env python3
"""Check the weighted-shift formulas used in the solution packet."""

from __future__ import annotations

import math


def geometric_product_root(weights: list[float]) -> list[float]:
    product = 1.0
    roots: list[float] = []
    for n, weight in enumerate(weights, start=1):
        product *= weight
        roots.append(product ** (1.0 / n))
    return roots


def main() -> None:
    cutoff = 40
    compact_weights = [1.0 / (n + 1) for n in range(cutoff)]
    unit_weights = [1.0] * cutoff

    compact_roots = geometric_product_root(compact_weights)
    unit_roots = geometric_product_root(unit_weights)

    # For w_n=1/(n+1), the forced n-th coefficient is n!.
    for n in range(1, 12):
        product = math.prod(compact_weights[:n])
        assert math.isclose(1.0 / product, math.factorial(n))

    # e_0=(T*)^n(n! e_n), so the hyperrange condition fails.
    for n in range(1, 12):
        product = math.prod(compact_weights[:n])
        assert math.isclose(product * math.factorial(n), 1.0)

    assert all(math.isclose(value, 1.0) for value in unit_roots)
    assert compact_roots[-1] < 0.08

    print("weighted-shift verification passed")
    print(f"unweighted geometric root at n={cutoff}: {unit_roots[-1]:.12f}")
    print(f"compact w_n=1/(n+1) root at n={cutoff}: {compact_roots[-1]:.12f}")
    print(f"forced coefficient at n=11: {math.factorial(11)}")


if __name__ == "__main__":
    main()
