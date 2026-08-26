"""Deterministic sanity checks for the arXiv:1303.4733 counterexample.

This checks finite instances of the coordinate identities used in the proof.
It is not a substitute for the symbolic argument in main.tex.
"""

from __future__ import annotations

import math
import random


def weight(n: int) -> float:
    """The proof indexes coordinates from 1."""
    return 2.0 ** (-n)


def star_norm(x: dict[int, float]) -> float:
    l1 = sum(abs(value) for value in x.values())
    q2 = sum(weight(n) * value * value for n, value in x.items())
    return l1 + math.sqrt(q2)


def subtract(x: dict[int, float], y: dict[int, float]) -> dict[int, float]:
    result = dict(x)
    for n, value in y.items():
        result[n] = result.get(n, 0.0) - value
        if result[n] == 0.0:
            result.pop(n)
    return result


def scaled_random_vector(rng: random.Random, dimension: int) -> dict[int, float]:
    x = {n: rng.uniform(-1.0, 1.0) for n in range(1, dimension + 1)}
    current = star_norm(x)
    scale = rng.uniform(0.0, 0.49) / current
    return {n: scale * value for n, value in x.items()}


def main() -> None:
    rng = random.Random(13034733)
    dominance_checks = 0
    strict_midpoint_checks = 0

    # For a fixed n, m=n+200 makes the extra tail weight negligible.
    for _ in range(500):
        x = scaled_random_vector(rng, 24)
        assert star_norm(x) < 0.5
        for n in range(1, 25):
            m = n + 200
            a = {n: 1.0}
            p = {n: 0.5, m: 0.5}
            da = star_norm(subtract(x, a))
            dp = star_norm(subtract(x, p))
            assert dp < da + 1e-13, (n, da, dp)
            dominance_checks += 1

    # Random finite midpoint tests for strict convexity.
    for _ in range(500):
        x = scaled_random_vector(rng, 16)
        y = scaled_random_vector(rng, 16)
        nx = star_norm(x)
        ny = star_norm(y)
        if nx == 0.0 or ny == 0.0:
            continue
        x = {n: value / nx for n, value in x.items()}
        y = {n: value / ny for n, value in y.items()}
        midpoint = {
            n: 0.5 * (x.get(n, 0.0) + y.get(n, 0.0))
            for n in set(x) | set(y)
        }
        assert star_norm(midpoint) < 1.0 - 1e-12
        strict_midpoint_checks += 1

    # Exact l1 site-separation pattern on a finite window.
    for n in range(1, 12):
        for m in range(n + 1, 13):
            p = {n: 0.5, m: 0.5}
            for k in range(1, 13):
                l1_distance = sum(abs(value) for value in subtract(p, {k: 1.0}).values())
                expected = 1.0 if k in (n, m) else 2.0
                assert l1_distance == expected

    print(
        "verified",
        dominance_checks,
        "finite dominance comparisons and",
        strict_midpoint_checks,
        "strict-midpoint samples",
    )


if __name__ == "__main__":
    main()
