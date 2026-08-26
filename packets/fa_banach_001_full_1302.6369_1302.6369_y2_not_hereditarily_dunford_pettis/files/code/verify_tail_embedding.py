#!/usr/bin/env python3
"""Finite-support sanity checks for the tail-diagonal embedding inequality.

This does not prove the infinite-dimensional theorem. Zeros beyond the stored
vector represent the arbitrarily far filler coordinates used in the proof.
"""

from itertools import combinations
from random import Random


def A(x, p):
    """Compute A_p for a finitely supported vector, using one-based p."""
    tail = range(p, len(x))  # zero-based indices strictly after coordinate p
    best = 0.0
    for r in range(min(p, len(x) - p) + 1):
        for chosen in combinations(tail, r):
            value = x[p - 1] + sum(x[j] for j in chosen)
            best = max(best, abs(value))
    return best


def tail(x, p):
    return [0.0] * (p - 1) + list(x[p - 1 :])


def xnorm(x, p):
    return max(A(x, q) for q in range(1, p + 1))


def main():
    rng = Random(20260811)
    checks = 0
    for length in range(2, 13):
        for _ in range(500):
            x = [rng.randint(-7, 7) / 5 for _ in range(length)]
            for p in range(1, min(6, length) + 1):
                ap = A(x, p)
                value = xnorm(tail(x, p), p)
                assert ap <= value + 1e-12
                assert value <= 2 * ap + 1e-12
                checks += 1
    print(f"tail-embedding inequalities passed: {checks}")


if __name__ == "__main__":
    main()
