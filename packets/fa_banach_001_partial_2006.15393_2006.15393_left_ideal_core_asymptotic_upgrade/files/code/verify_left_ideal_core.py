#!/usr/bin/env python3
"""Exhaustively verify the finite cyclic least-left-ideal examples."""

from itertools import combinations


def elements(n):
    return [(g, i) for g in range(n) for i in (0, 1)]


def multiply(a, b, n):
    return ((a[0] + b[0]) % n, min(a[1], b[1]))


def is_left_ideal(subset, universe, n):
    subset = set(subset)
    return bool(subset) and all(
        multiply(s, x, n) in subset for s in universe for x in subset
    )


def powerset_nonempty(items):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def check(n):
    universe = elements(n)
    whole = set(universe)
    core = {(g, 0) for g in range(n)}

    assert all(
        multiply(multiply(a, b, n), c, n)
        == multiply(a, multiply(b, c, n), n)
        for a in universe
        for b in universe
        for c in universe
    )
    assert all(
        multiply(a, b, n) == multiply(b, a, n)
        for a in universe
        for b in universe
    )

    ideals = [set(part) for part in powerset_nonempty(universe)
              if is_left_ideal(part, universe, n)]
    assert is_left_ideal(core, universe, n)
    assert all(core <= ideal for ideal in ideals)

    for t in universe:
        principal = {multiply(s, t, n) for s in universe}
        assert principal == (core if t[1] == 0 else whole)

    return len(ideals), sorted(len(ideal) for ideal in ideals)


def main():
    print("finite cyclic least-left-ideal verification")
    for n in range(2, 8):
        count, sizes = check(n)
        print(f"n={n}: PASS; left_ideals={count}; sizes={sizes}")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
