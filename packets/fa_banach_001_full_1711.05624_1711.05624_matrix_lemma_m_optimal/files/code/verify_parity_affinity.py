#!/usr/bin/env python3
"""Small-instance checks for the parity-affinity identity in the packet."""

from __future__ import annotations

import itertools
import math
from collections import Counter

import numpy as np


def parity_mask(word: tuple[int, ...]) -> int:
    mask = 0
    for symbol in word:
        mask ^= 1 << symbol
    return mask


def check(n: int, m: int, r: int) -> None:
    words = list(itertools.product(range(n), repeat=m))
    counts = Counter(parity_mask(word) for word in words)
    total = len(words)
    edge = (1 << (2 * r)) - 1

    affinity = sum(
        math.sqrt(count * counts.get(mask ^ edge, 0))
        for mask, count in counts.items()
    ) / total

    transition = np.fromiter(
        (
            1.0 if parity_mask(u) ^ parity_mask(v) == edge else 0.0
            for u in words
            for v in words
        ),
        dtype=float,
        count=total * total,
    ).reshape((total, total))
    nuclear_ratio = np.linalg.svd(transition, compute_uv=False).sum() / total

    marginal: Counter[int] = Counter()
    for mask, count in counts.items():
        marginal[mask & edge] += count
    projected_affinity = sum(
        math.sqrt(marginal[z] * marginal[edge ^ z]) for z in range(1 << (2 * r))
    ) / total

    tail_bound = 0.0
    lam = 2 * r * m / n
    for z in range(1 << (2 * r)):
        h = z.bit_count()
        left = 1.0 if h == 0 else lam**h / math.factorial(h)
        j = 2 * r - h
        right = 1.0 if j == 0 else lam**j / math.factorial(j)
        tail_bound += math.sqrt(left * right)

    assert abs(affinity - nuclear_ratio) < 1e-9
    assert affinity <= projected_affinity + 1e-12
    print(
        f"n={n} m={m} r={r} N={total} "
        f"affinity={affinity:.12g} projected={projected_affinity:.12g} "
        f"factorial_bound={tail_bound:.12g}"
    )


if __name__ == "__main__":
    check(n=5, m=2, r=1)
    check(n=12, m=1, r=2)
    check(n=6, m=2, r=2)
    check(n=6, m=3, r=2)
