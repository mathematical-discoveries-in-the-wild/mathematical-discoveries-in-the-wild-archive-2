#!/usr/bin/env python3
"""Exact checks for complete-graph cosparse projection dynamic programs.

The verifier compares the dynamic program against exhaustive enumeration of
all set partitions.  Arithmetic is rational, so every reported equality is
exact rather than tolerance-based.
"""

from __future__ import annotations

import argparse
import itertools
import random
from fractions import Fraction
from typing import Iterable, Iterator, Sequence


Q = Fraction


def set_partitions(n: int) -> Iterator[tuple[tuple[int, ...], ...]]:
    """Generate each set partition of range(n) once."""

    if n == 0:
        yield ()
        return

    blocks: list[list[int]] = [[0]]

    def visit(i: int) -> Iterator[tuple[tuple[int, ...], ...]]:
        if i == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            block.append(i)
            yield from visit(i + 1)
            block.pop()
        blocks.append([i])
        yield from visit(i + 1)
        blocks.pop()

    yield from visit(1)


def partition_sse(values: Sequence[Q], partition: Sequence[Sequence[int]]) -> Q:
    total = Q(0)
    for block in partition:
        mean = sum((values[i] for i in block), Q(0)) / len(block)
        total += sum(((values[i] - mean) ** 2 for i in block), Q(0))
    return total


def pair_zeros(partition: Sequence[Sequence[int]]) -> int:
    return sum(len(block) * (len(block) - 1) // 2 for block in partition)


def brute_profiles(values: Sequence[Q]) -> tuple[list[Q], list[Q]]:
    """Return exact optimum costs for every incidence and tight cosparsity."""

    n = len(values)
    edges = n * (n - 1) // 2
    incidence: list[Q | None] = [None] * (edges + 1)
    tight: list[Q | None] = [None] * (edges + 2)
    mean = sum(values, Q(0)) / n
    zero_mean_penalty = n * mean * mean

    def update(profile: list[Q | None], zeros: int, cost: Q) -> None:
        for ell in range(zeros + 1):
            if profile[ell] is None or cost < profile[ell]:
                profile[ell] = cost

    for partition in set_partitions(n):
        zeros = pair_zeros(partition)
        cost = partition_sse(values, partition)
        update(incidence, zeros, cost)

        # Unconstrained block means preserve the global sum.
        dc_zero = int(sum(values, Q(0)) == 0)
        update(tight, zeros + dc_zero, cost)

        # Enforcing the appended all-ones row shifts every block mean by
        # the global mean and adds the same partition-independent penalty.
        update(tight, zeros + 1, cost + zero_mean_penalty)

    assert all(value is not None for value in incidence)
    assert all(value is not None for value in tight)
    return [value for value in incidence if value is not None], [
        value for value in tight if value is not None
    ]


def interval_sse(prefix: Sequence[Q], prefix2: Sequence[Q], lo: int, hi: int) -> Q:
    count = hi - lo
    total = prefix[hi] - prefix[lo]
    total2 = prefix2[hi] - prefix2[lo]
    return total2 - total * total / count


def incidence_dp_table(
    values: Sequence[Q],
) -> tuple[list[tuple[Q, int]], list[list[Q | None]], list[list[tuple[int, int] | None]]]:
    """Dynamic program indexed by prefix length and exact zero-pair count."""

    items = sorted((value, index) for index, value in enumerate(values))
    ordered = [value for value, _ in items]
    n = len(values)
    edges = n * (n - 1) // 2
    prefix = [Q(0)]
    prefix2 = [Q(0)]
    for value in ordered:
        prefix.append(prefix[-1] + value)
        prefix2.append(prefix2[-1] + value * value)

    dp: list[list[Q | None]] = [[None] * (edges + 1) for _ in range(n + 1)]
    prev: list[list[tuple[int, int] | None]] = [
        [None] * (edges + 1) for _ in range(n + 1)
    ]
    dp[0][0] = Q(0)
    for hi in range(1, n + 1):
        for lo in range(hi):
            size = hi - lo
            added = size * (size - 1) // 2
            cost = interval_sse(prefix, prefix2, lo, hi)
            for old_zeros, old_cost in enumerate(dp[lo]):
                if old_cost is None:
                    continue
                zeros = old_zeros + added
                candidate = old_cost + cost
                if dp[hi][zeros] is None or candidate < dp[hi][zeros]:
                    dp[hi][zeros] = candidate
                    prev[hi][zeros] = (lo, old_zeros)
    return items, dp, prev


def recover_projection(
    values: Sequence[Q],
    items: Sequence[tuple[Q, int]],
    dp: Sequence[Sequence[Q | None]],
    prev: Sequence[Sequence[tuple[int, int] | None]],
    ell: int,
) -> tuple[Q, list[Q]]:
    """Recover an exact complete-graph incidence projection."""

    n = len(values)
    edges = n * (n - 1) // 2
    if not 0 <= ell <= edges:
        raise ValueError("incidence cosparsity is outside [0, n(n-1)/2]")
    feasible = [(cost, zeros) for zeros, cost in enumerate(dp[n]) if cost is not None and zeros >= ell]
    cost, zeros = min(feasible)
    blocks: list[tuple[int, int]] = []
    hi = n
    while hi:
        step = prev[hi][zeros]
        assert step is not None
        lo, old_zeros = step
        blocks.append((lo, hi))
        hi, zeros = lo, old_zeros
    blocks.reverse()

    projected = [Q(0)] * n
    for lo, hi in blocks:
        mean = sum((items[i][0] for i in range(lo, hi)), Q(0)) / (hi - lo)
        for i in range(lo, hi):
            projected[items[i][1]] = mean
    return cost, projected


def incidence_projection(values: Sequence[Q], ell: int) -> tuple[Q, list[Q]]:
    items, dp, prev = incidence_dp_table(values)
    return recover_projection(values, items, dp, prev, ell)


def tight_projection(values: Sequence[Q], ell: int) -> tuple[Q, list[Q]]:
    """Project for Omega=[B_Kn; 1^T], where Omega^T Omega=nI."""

    n = len(values)
    edges = n * (n - 1) // 2
    if not 0 <= ell <= edges + 1:
        raise ValueError("tight cosparsity is outside [0, n(n-1)/2+1]")
    items, dp, prev = incidence_dp_table(values)

    choices: list[tuple[Q, list[Q]]] = []
    if ell <= edges:
        choices.append(recover_projection(values, items, dp, prev, ell))
    if ell >= 1:
        base_cost, base_vector = recover_projection(values, items, dp, prev, ell - 1)
        mean = sum(values, Q(0)) / n
        choices.append((base_cost + n * mean * mean, [value - mean for value in base_vector]))
    return min(choices, key=lambda item: item[0])


def squared_error(values: Sequence[Q], projected: Sequence[Q]) -> Q:
    return sum(((a - b) ** 2 for a, b in zip(values, projected)), Q(0))


def actual_pair_zeros(projected: Sequence[Q]) -> int:
    return sum(
        projected[i] == projected[j]
        for i in range(len(projected))
        for j in range(i + 1, len(projected))
    )


def verify_vector(raw_values: Sequence[int]) -> int:
    values = [Q(value) for value in raw_values]
    n = len(values)
    edges = n * (n - 1) // 2
    brute_incidence, brute_tight = brute_profiles(values)
    comparisons = 0

    for ell in range(edges + 1):
        cost, projected = incidence_projection(values, ell)
        assert cost == brute_incidence[ell]
        assert cost == squared_error(values, projected)
        assert actual_pair_zeros(projected) >= ell
        comparisons += 1

    for ell in range(edges + 2):
        cost, projected = tight_projection(values, ell)
        assert cost == brute_tight[ell]
        assert cost == squared_error(values, projected)
        zeros = actual_pair_zeros(projected) + int(sum(projected, Q(0)) == 0)
        assert zeros >= ell
        comparisons += 1
    return comparisons


def run(exhaustive_n: int, random_cases: int, seed: int) -> None:
    vectors = 0
    comparisons = 0
    for n in range(1, exhaustive_n + 1):
        for values in itertools.product((-1, 0, 1), repeat=n):
            comparisons += verify_vector(values)
            vectors += 1

    rng = random.Random(seed)
    for n in (7, 8):
        for _ in range(random_cases):
            values = [rng.randint(-4, 4) for _ in range(n)]
            comparisons += verify_vector(values)
            vectors += 1

    example = [Q(-3), Q(-2), Q(0), Q(1), Q(5)]
    inc_cost, inc_vector = incidence_projection(example, 4)
    tight_cost, tight_vector = tight_projection(example, 5)
    print(f"verified vector instances: {vectors}")
    print(f"verified optimum/projection comparisons: {comparisons}")
    print(f"incidence example ell=4: cost={inc_cost}, projection={inc_vector}")
    print(f"tight example ell=5: cost={tight_cost}, projection={tight_vector}")
    print("all exhaustive comparisons passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive-n", type=int, default=6)
    parser.add_argument("--random-cases", type=int, default=40)
    parser.add_argument("--seed", type=int, default=12072456)
    args = parser.parse_args()
    run(args.exhaustive_n, args.random_cases, args.seed)


if __name__ == "__main__":
    main()
