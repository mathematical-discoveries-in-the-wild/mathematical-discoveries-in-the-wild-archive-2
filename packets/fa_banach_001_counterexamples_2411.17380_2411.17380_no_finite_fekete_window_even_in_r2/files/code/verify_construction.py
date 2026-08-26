#!/usr/bin/env python3
"""Finite regression checks for the block counterexample in the packet."""

from __future__ import annotations

import math


C = 0.25
S1 = math.pi**2 / 48.0


def f(n: int) -> int:
    return n * n + 1


def boundaries(count: int) -> list[int]:
    values = [1, 2]
    while len(values) < count:
        cutoff = values[-1]
        next_value = max(cutoff, max(f(n) for n in range(1, cutoff))) + 1
        values.append(next_value)
    return values


def block_index(n: int, ns: list[int]) -> int:
    for k in range(len(ns) - 1):
        if ns[k] <= n < ns[k + 1]:
            return k + 1  # mathematical indexing
    raise ValueError(f"index {n} is outside the constructed blocks")


def slack(k: int, tail_terms: int = 2_000_000) -> float:
    # Exact identity: sum_{j=k}^infty j^-2 = pi^2/6-sum_{j<k}j^-2.
    del tail_terms
    return 2 * C * C * (math.pi**2 / 6 - sum(1 / (j * j) for j in range(1, k)))


def angle(k: int) -> float:
    return C * sum(1 / j for j in range(1, k))


def vector(n: int, ns: list[int]) -> tuple[float, float]:
    k = block_index(n, ns)
    r = n * (1 + slack(k))
    a = angle(k)
    return r * math.cos(a), r * math.sin(a)


def norm(x: tuple[float, float]) -> float:
    return math.hypot(*x)


def main() -> None:
    assert (1 + S1) ** 2 < 2
    ns = boundaries(8)
    max_index = ns[-1] - 1
    checked = 0
    # Keep the exhaustive prefix modest; the block formulas are exact.
    for n in range(1, min(80, max_index) + 1):
        for m in range(n, min(f(n), 2_000, max_index - n) + 1):
            vn = vector(n, ns)
            vm = vector(m, ns)
            vnm = vector(n + m, ns)
            rhs = norm((vn[0] + vm[0], vn[1] + vm[1]))
            lhs = norm(vnm)
            if lhs > rhs + 1e-9 * max(1.0, rhs):
                raise AssertionError((n, m, lhs, rhs))
            checked += 1
    print(f"constant_ok={(1 + S1) ** 2:.12f} < 2")
    print(f"boundaries={ns[:7]}")
    print(f"verified_pairs={checked}")


if __name__ == "__main__":
    main()
