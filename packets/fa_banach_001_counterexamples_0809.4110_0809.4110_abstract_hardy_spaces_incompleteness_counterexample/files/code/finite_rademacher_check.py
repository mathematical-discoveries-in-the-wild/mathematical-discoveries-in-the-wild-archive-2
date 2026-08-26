#!/usr/bin/env python3
"""Finite sanity checks for the abstract-Hardy incompleteness packet.

This script is not a proof.  It checks the finite dyadic Rademacher identities
used by the proof and prints weighted-norm tails for the Cauchy sequence.
"""

from itertools import product
from math import pi


def rademacher_value(n: int, j: int, depth: int) -> int:
    """Value of r_n at the midpoint of dyadic cell j of depth `depth`."""
    return 1 if ((j >> (depth - n)) & 1) == 0 else -1


def finite_expectation(values):
    return sum(values) / len(values)


def main() -> None:
    depth = 8
    sample_size = 2**depth
    rows = [
        [rademacher_value(n, j, depth) for j in range(sample_size)]
        for n in range(1, depth + 1)
    ]

    for i in range(depth):
        for j in range(depth):
            gram = finite_expectation([rows[i][k] * rows[j][k] for k in range(sample_size)])
            expected = 1 if i == j else 0
            assert gram == expected, (i, j, gram)

    tested = 0
    moment_depth = 6
    for coeffs in product((-1, 0, 1), repeat=moment_depth):
        if not any(coeffs):
            continue
        z = [
            sum(coeffs[n] * rows[n][j] for n in range(moment_depth))
            for j in range(sample_size)
        ]
        second = finite_expectation([value**2 for value in z])
        fourth = finite_expectation([value**4 for value in z])
        assert fourth <= 3 * second**2
        tested += 1

    def weighted_tail(start: int, stop: int = 1_000_000) -> float:
        return sum(1.0 / (n * n) for n in range(start + 1, stop + 1))

    print(f"orthogonality: exact for {depth} coordinates on {sample_size} dyadic cells")
    print(f"fourth-moment bound: passed for {tested} nonzero coefficient vectors")
    for start in (10, 100, 1000):
        tail = weighted_tail(start)
        print(f"sum_{{n>{start}}} 1/n^2 (truncated at 1e6): {tail:.9f}")
    print("all finite checks passed")


if __name__ == "__main__":
    main()
