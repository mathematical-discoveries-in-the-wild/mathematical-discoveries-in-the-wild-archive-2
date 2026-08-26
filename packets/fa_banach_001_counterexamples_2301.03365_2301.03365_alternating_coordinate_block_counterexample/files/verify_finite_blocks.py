#!/usr/bin/env python3
"""Exact finite sanity checks; the general proof is in the packet."""

from itertools import product


def block(k):
    return list(range(k * k, (k + 1) * (k + 1)))


for k in range(1, 30):
    indices = block(k)
    signs = [(-1) ** (n - k * k) for n in indices]
    assert len(indices) == 2 * k + 1
    assert sum(signs) == 1
    running = 0
    for sign in signs:
        running += sign
        assert running in (0, 1)

# Exhaust the small coloring cases. A repeated color in one block creates
# a row with diagonal 1 and at least one off-diagonal interaction of size 1.
for colors in range(1, 5):
    size = colors + 1
    for coloring in product(range(colors), repeat=size):
        repeated = any(coloring.count(color) >= 2 for color in range(colors))
        assert repeated

print("EXACT FINITE CHECKS PASSED")
