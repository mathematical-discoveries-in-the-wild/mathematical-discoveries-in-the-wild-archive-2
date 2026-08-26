#!/usr/bin/env python3
"""Finite checks for the two combinatorial identities used in the packet."""

from itertools import combinations, permutations


def subsets(n):
    values = range(n)
    for size in range(n + 1):
        for subset in combinations(values, size):
            yield frozenset(subset)


def inclusion_exclusion_coefficient(n, used):
    return sum(
        (-1) ** (n - len(container))
        for container in subsets(n)
        if used <= container
    )


def is_rotation(perm):
    n = len(perm)
    return any(tuple(perm) == tuple(range(shift, n)) + tuple(range(shift))
               for shift in range(n))


def avoids_forbidden_backward_edges(perm):
    n = len(perm)
    for source, target in zip(perm, perm[1:] + perm[:1]):
        # In one-based notation, every j -> i with j > i is forbidden,
        # except the closing edge n -> 1.
        if source > target and not (source == n - 1 and target == 0):
            return False
    return True


def main():
    for n in range(2, 9):
        universe = frozenset(range(n))
        for used in subsets(n):
            expected = 1 if used == universe else 0
            assert inclusion_exclusion_coefficient(n, used) == expected

        survivors = [
            perm for perm in permutations(range(n))
            if avoids_forbidden_backward_edges(perm)
        ]
        assert len(survivors) == n
        assert all(is_rotation(perm) for perm in survivors)
        print(f"n={n}: Boolean coefficients OK; {n} rotations survive")


if __name__ == "__main__":
    main()

