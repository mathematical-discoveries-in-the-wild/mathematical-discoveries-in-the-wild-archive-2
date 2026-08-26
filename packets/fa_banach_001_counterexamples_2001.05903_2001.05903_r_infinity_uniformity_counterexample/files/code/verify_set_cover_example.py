#!/usr/bin/env python3
"""Exact finite checks for the set-cover outer-measure counterexample.

The proof is symbolic.  This script independently enumerates the finite set
systems for modest N and checks the two set-cover numbers used in the packet.
"""

from __future__ import annotations

from argparse import ArgumentParser
from itertools import combinations


def least_cover_size(universe: set[tuple[int, ...]], generators: list[set[tuple[int, ...]]]) -> int:
    for size in range(len(generators) + 1):
        for chosen in combinations(range(len(generators)), size):
            covered: set[tuple[int, ...]] = set()
            for index in chosen:
                covered.update(generators[index])
            if universe <= covered:
                return size
    raise AssertionError("the listed generators do not cover the universe")


def check(n: int, k: int) -> None:
    labels = range(n)
    points = set(combinations(labels, k))
    generators = [{point for point in points if i in point} for i in labels]

    assert all(generators)
    assert all(least_cover_size(generator, generators) == 1 for generator in generators)
    assert least_cover_size(points, generators) == n - k + 1
    assert all(sum(point in generator for generator in generators) == k for point in points)

    p_values = (1.25, 1.5, 2.0, 3.0, 5.0)
    ratios = {
        p: k * (n - k + 1) ** (1.0 / p) / n
        for p in p_values
    }
    formatted = ", ".join(f"p={p:g}: {ratio:.6f}" for p, ratio in ratios.items())
    print(
        f"N={n:2d}, k={k:2d}, |X|={len(points):5d}, "
        f"mu(X)={n-k+1:2d}; triangle ratios [{formatted}]"
    )


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--max-n", type=int, default=10)
    args = parser.parse_args()
    if args.max_n < 2:
        raise SystemExit("--max-n must be at least 2")

    for n in range(2, args.max_n + 1):
        check(n, n // 2)
    print("all exact set-cover and incidence checks passed")


if __name__ == "__main__":
    main()
