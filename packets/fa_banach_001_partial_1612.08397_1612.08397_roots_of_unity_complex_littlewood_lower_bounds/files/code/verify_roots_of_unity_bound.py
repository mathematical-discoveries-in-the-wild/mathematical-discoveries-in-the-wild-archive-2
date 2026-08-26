"""Numerically corroborate the roots-of-unity lower-bound construction.

The proof in the packet is analytic.  This script only samples the one-variable
trigonometric maximum and compares it with the closed form.
"""

from __future__ import annotations

import cmath
import math


def cosine_sum(n: int, u: float) -> float:
    return sum(abs(math.cos(u + math.pi * k / n)) for k in range(n))


def sampled_cosine_max(n: int, samples: int = 200_001) -> float:
    # The sum is pi/n-periodic and even, so this is a fundamental half-cell.
    endpoint = math.pi / (2 * n)
    return max(cosine_sum(n, endpoint * j / (samples - 1)) for j in range(samples))


def matrix_numerator(n: int) -> float:
    zeta = cmath.exp(2j * math.pi / n)
    rows = [(1 + 0j, zeta**k) for k in range(n)]
    return sum(math.sqrt(abs(a) ** 2 + abs(b) ** 2) for a, b in rows)


def main() -> None:
    print(" n   sampled max       exact max         ratio             lower bound")
    for n in range(2, 13):
        sampled = 2 * sampled_cosine_max(n)
        exact_norm = 2 / math.sin(math.pi / (2 * n))
        ratio = matrix_numerator(n) / sampled
        exact_ratio = n * math.sin(math.pi / (2 * n)) / math.sqrt(2)
        assert abs(sampled - exact_norm) < 2e-9
        assert abs(ratio - exact_ratio) < 2e-9
        print(
            f"{n:2d}  {sampled:16.12f}  {exact_norm:16.12f}"
            f"  {ratio:16.12f}  {exact_ratio:16.12f}"
        )


if __name__ == "__main__":
    main()
