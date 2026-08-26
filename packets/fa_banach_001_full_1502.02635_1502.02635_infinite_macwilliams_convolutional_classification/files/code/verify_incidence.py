#!/usr/bin/env python3
"""Exact finite checks for the projective incidence Gram formula.

The proof packet is symbolic.  This script merely enumerates small prime-field
cases as a guard against an incidence-count or normalization mistake.
"""

from __future__ import annotations

from itertools import product


def projective_representatives(q: int, d: int) -> list[tuple[int, ...]]:
    reps: set[tuple[int, ...]] = set()
    for vector in product(range(q), repeat=d):
        if not any(vector):
            continue
        pivot = next(value for value in vector if value)
        inverse = pow(pivot, -1, q)
        reps.add(tuple((inverse * value) % q for value in vector))
    return sorted(reps)


def dot(left: tuple[int, ...], right: tuple[int, ...], q: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % q


def check_case(q: int, d: int) -> tuple[int, int, int]:
    points = projective_representatives(q, d)
    functionals = projective_representatives(q, d)
    expected_size = (q**d - 1) // (q - 1)
    assert len(points) == len(functionals) == expected_size

    incidence = [
        [int(dot(point, functional, q) != 0) for functional in functionals]
        for point in points
    ]
    diagonal = q ** (d - 1)
    off_diagonal = 0 if d == 1 else q ** (d - 2) * (q - 1)
    for row_index, row in enumerate(incidence):
        for other_index, other in enumerate(incidence):
            gram_entry = sum(a * b for a, b in zip(row, other))
            expected = diagonal if row_index == other_index else off_diagonal
            assert gram_entry == expected, (q, d, row_index, other_index)

    # The Gram matrix is (diagonal-off) I + off J.  These are its two
    # eigenvalues, both strictly positive; hence the incidence matrix is full
    # rank over the reals.
    transverse_eigenvalue = diagonal - off_diagonal
    constant_eigenvalue = diagonal + (expected_size - 1) * off_diagonal
    assert transverse_eigenvalue > 0 and constant_eigenvalue > 0
    return expected_size, transverse_eigenvalue, constant_eigenvalue


def main() -> None:
    cases = 0
    largest_matrix = 0
    for q in (2, 3, 5):
        for d in range(1, 5):
            size, transverse, constant = check_case(q, d)
            cases += 1
            largest_matrix = max(largest_matrix, size)
            print(
                f"q={q} d={d} size={size} "
                f"eigenvalues={transverse},{constant} PASS"
            )
    print(f"cases={cases}")
    print(f"largest_matrix={largest_matrix}x{largest_matrix}")
    print("status=PASS")


if __name__ == "__main__":
    main()
