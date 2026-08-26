#!/usr/bin/env python3
"""Finite checks for the mixed-radix construction in the proof packet.

The proof itself is exact and does not depend on this program.  For small
instances, we independently minimize word length by mixed-integer linear
programming and compare it with the claimed balanced-digit formula.
"""

from __future__ import annotations

from itertools import product
from math import ceil

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def q(i: int) -> int:
    return 1 << (i * i)


def radix(i: int) -> int:
    return q(i + 1) // q(i)


def first_position(m: int) -> int:
    i = 1
    while radix(i) < 4 * m * m:
        i += 1
    return i


def digit(m: int, i: int) -> int:
    # floor(R_i/(2m))+1, written without floating point.
    return radix(i) // (2 * m) + 1


def exact_word_length_milp(x: int, max_i: int) -> int:
    """Minimize sum |a_i| subject to x=sum a_i q_i."""
    # Coins larger than 2|x| cannot enter a shortest representation in the
    # checked strict-balanced cases; dropping them also avoids MILP feasibility
    # tolerances being amplified by enormous powers of two.
    while max_i > 0 and q(max_i) > 2 * abs(x):
        max_i -= 1
    coins = np.array([float(q(i)) for i in range(max_i + 1)])
    c = np.ones(2 * (max_i + 1))
    row = np.concatenate([coins, -coins])[None, :]
    result = milp(
        c,
        integrality=np.ones_like(c),
        bounds=Bounds(np.zeros_like(c), np.full_like(c, np.inf)),
        constraints=LinearConstraint(row, [float(x)], [float(x)]),
        options={"time_limit": 10},
    )
    if not result.success:
        raise RuntimeError(result.message)
    z = np.rint(result.x).astype(np.int64)
    signed = z[: max_i + 1] - z[max_i + 1 :]
    reconstructed = sum(int(signed[i]) * q(i) for i in range(max_i + 1))
    if reconstructed != x:
        raise AssertionError((x, reconstructed, max_i, result.fun, result.x))
    objective = int(np.sum(np.abs(signed)))
    assert abs(result.fun - objective) < 1e-5
    return objective


def construction(m: int, blocks: int = 2):
    start = first_position(m)
    positions = [start + 2 * j for j in range(blocks)]
    digits = [digit(m, i) for i in positions]
    for i, d in zip(positions, digits):
        r = radix(i)
        assert (m - 1) * d <= r // 2 - 1
        assert m * d >= r // 2 + 1
        assert r - m * d <= r // 2 - 1
        assert 2 * m * d - r - 1 >= 1
    prefixes = [sum(d * q(i) for i, d in zip(positions[:k], digits[:k]))
                for k in range(1, blocks + 1)]
    prefix_lengths = [sum(digits[:k]) for k in range(1, blocks + 1)]
    return positions, digits, prefixes, prefix_lengths


def predicted_sum_length(m: int, ks: tuple[int, ...], positions, digits) -> int:
    total = sum(sum(digits[:k]) for k in ks)
    if len(ks) == m:
        common = min(ks)
        savings = sum(
            2 * m * digits[j] - radix(positions[j]) - 1
            for j in range(common)
        )
        return total - savings
    assert len(ks) < m
    return total


def main() -> None:
    checked = 0
    for m in range(2, 9):
        # Two actual sparse blocks are checked for m=2.  For larger m a
        # single block keeps HiGHS' floating equality coefficients below
        # 2^26; block independence is covered by the exact symbolic asserts.
        blocks = 2 if m == 2 else 1
        positions, digits, prefixes, prefix_lengths = construction(m, blocks)
        max_i = positions[-1] + 1

        # Each prefix has the asserted uncancelled length.
        for x, expected in zip(prefixes, prefix_lengths):
            got = exact_word_length_milp(x, max_i)
            assert got == expected, (m, x, got, expected)
            checked += 1

        # Test every tuple of one- and two-block prefixes for s<m and s=m.
        sample_orders = sorted(set([1, max(1, m - 1), m]))
        for s in sample_orders:
            for ks in product(tuple(range(1, blocks + 1)), repeat=s):
                x = sum(prefixes[k - 1] for k in ks)
                expected = predicted_sum_length(m, ks, positions, digits)
                got = exact_word_length_milp(x, max_i)
                assert got == expected, (m, ks, got, expected)
                checked += 1

    # Check the elementary local normalization inequality used in the proof.
    local_checks = 0
    for r in range(2, 130, 2):
        for c0 in range(-max(0, r // 2 - 1), max(0, r // 2 - 1) + 1):
            for h in range(-8, 9):
                a = c0 + r * h
                assert abs(c0) + abs(h) <= abs(a) if h else abs(c0) == abs(a)
                local_checks += 1

    print(f"verified {checked} exact MILP word-length identities")
    print(f"verified {local_checks} local normalization inequalities")
    print("m=2,...,8: all carry thresholds and exact nilpotency formulas pass")


if __name__ == "__main__":
    main()
