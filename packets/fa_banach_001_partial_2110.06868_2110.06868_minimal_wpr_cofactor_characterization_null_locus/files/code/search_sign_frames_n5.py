#!/usr/bin/env python3
"""Exact search for 8-vector {+1,-1} weak-phase frames in R^5.

Rows are considered projectively, so their first coordinate is fixed to +1.
For a full-spark 8 x 5 matrix A, minimal weak phase retrieval is equivalent
to the following finite condition.  For every four-row subset I, if u and v
span ker(A_I) and ker(A_{I^c}), respectively, then

    u_j^2 / ||u||^2 = v_j^2 / ||v||^2    for j=1,...,5.

All arithmetic below is integral and exact.
"""

from __future__ import annotations

from itertools import combinations, product


def det(matrix: tuple[tuple[int, ...], ...] | list[list[int]]) -> int:
    """Bareiss determinant for a small integer square matrix."""
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) // previous
        previous = pivot_value
    return sign * a[-1][-1]


def cofactor_kernel(rows: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    """A nonzero cofactor vector spanning the kernel of a 4 x 5 matrix."""
    return tuple(
        (-1 if j % 2 else 1)
        * det(tuple(tuple(row[k] for k in range(5) if k != j) for row in rows))
        for j in range(5)
    )


def is_full_spark(rows: tuple[tuple[int, ...], ...]) -> bool:
    return all(det(tuple(rows[i] for i in subset)) for subset in combinations(range(8), 5))


def satisfies_minimal_wpr_condition(rows: tuple[tuple[int, ...], ...]) -> bool:
    universe = set(range(8))
    for subset in combinations(range(8), 4):
        # Check one representative from each complementary pair.
        if 0 not in subset:
            continue
        complement = tuple(sorted(universe.difference(subset)))
        u = cofactor_kernel(tuple(rows[i] for i in subset))
        v = cofactor_kernel(tuple(rows[i] for i in complement))
        u_norm2 = sum(x * x for x in u)
        v_norm2 = sum(x * x for x in v)
        if any(u[j] * u[j] * v_norm2 != v[j] * v[j] * u_norm2 for j in range(5)):
            return False
    return True


def main() -> None:
    projective_sign_rows = tuple((1,) + tail for tail in product((-1, 1), repeat=4))
    total = 0
    full_spark = 0
    solutions: list[tuple[tuple[int, ...], ...]] = []
    for indices in combinations(range(16), 8):
        total += 1
        rows = tuple(projective_sign_rows[i] for i in indices)
        if not is_full_spark(rows):
            continue
        full_spark += 1
        if satisfies_minimal_wpr_condition(rows):
            solutions.append(rows)

    print(f"projective row sets checked: {total}")
    print(f"full-spark row sets: {full_spark}")
    print(f"minimal-WPR solutions: {len(solutions)}")
    for solution_number, rows in enumerate(solutions, start=1):
        print(f"solution {solution_number}")
        for row in rows:
            print(" ".join(f"{entry:+d}" for entry in row))


if __name__ == "__main__":
    main()
