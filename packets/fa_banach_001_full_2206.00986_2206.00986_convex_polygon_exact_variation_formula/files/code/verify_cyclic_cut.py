#!/usr/bin/env python3
"""Stress tests for the cyclic-cut inequality in the convex-polygon proof."""

from __future__ import annotations

from itertools import product
import random


def cyclic_intervals(m: int) -> list[frozenset[int]]:
    intervals: set[frozenset[int]] = set()
    for start in range(m):
        for length in range(1, m):
            intervals.add(frozenset((start + j) % m for j in range(length)))
    return sorted(intervals, key=lambda x: (len(x), tuple(x)))


def cut_transitions(word: tuple[int, ...], block: frozenset[int]) -> int:
    return sum((a in block) != (b in block) for a, b in zip(word, word[1:]))


def cut_complexity(word: tuple[int, ...], intervals: list[frozenset[int]]) -> int:
    return max(cut_transitions(word, block) for block in intervals)


def cyclic_half_perimeter(values: tuple[complex, ...]) -> float:
    m = len(values)
    return 0.5 * sum(abs(values[i] - values[(i + 1) % m]) for i in range(m))


def curve_variation(word: tuple[int, ...], values: tuple[complex, ...]) -> float:
    return sum(abs(values[a] - values[b]) for a, b in zip(word, word[1:]))


def nonbacktracking_words(m: int, length: int):
    for first in range(m):
        stack = [(first,)]
        while stack:
            word = stack.pop()
            if len(word) == length:
                yield word
                continue
            stack.extend(word + (nxt,) for nxt in range(m) if nxt != word[-1])


def exhaustive_real_check() -> int:
    m = 4
    intervals = cyclic_intervals(m)
    assignments = list(product((-1.0, 0.0, 1.0), repeat=m))
    checked = 0
    for length in range(2, 10):
        for word in nonbacktracking_words(m, length):
            complexity = cut_complexity(word, intervals)
            for values in assignments:
                lhs = curve_variation(word, values)
                rhs = complexity * cyclic_half_perimeter(values)
                assert lhs <= rhs + 1e-12, (word, values, lhs, rhs)
                checked += 1
    return checked


def random_complex_check(trials: int = 20_000) -> int:
    rng = random.Random(220600986)
    checked = 0
    for _ in range(trials):
        m = rng.randint(4, 8)
        length = rng.randint(2, 40)
        word = [rng.randrange(m)]
        while len(word) < length:
            nxt = rng.randrange(m)
            if nxt != word[-1]:
                word.append(nxt)
        values = tuple(complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(m))
        intervals = cyclic_intervals(m)
        complexity = cut_complexity(tuple(word), intervals)
        lhs = curve_variation(tuple(word), values)
        rhs = complexity * cyclic_half_perimeter(values)
        assert lhs <= rhs + 1e-10, (m, word, values, lhs, rhs)
        checked += 1
    return checked


def main() -> None:
    exhaustive = exhaustive_real_check()
    random_checked = random_complex_check()
    print(f"exhaustive four-vertex real instances: {exhaustive}")
    print(f"deterministic random complex instances: {random_checked}")
    print("all cyclic-cut inequalities passed")


if __name__ == "__main__":
    main()
