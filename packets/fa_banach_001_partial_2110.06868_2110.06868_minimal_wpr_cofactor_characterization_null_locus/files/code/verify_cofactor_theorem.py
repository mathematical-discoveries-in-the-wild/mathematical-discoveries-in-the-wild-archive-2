#!/usr/bin/env python3
"""Exact sanity checks for the cofactor characterization theorem.

This script is not a substitute for the proof.  It verifies the polynomial
identities on the published n=3 and n=4 examples and checks the explicit
witness showing that the hypersurface polynomial is nonzero.
"""

from __future__ import annotations

from itertools import combinations


def det(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Bareiss determinant for an integer square matrix."""
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
    n = len(rows[0])
    assert len(rows) == n - 1
    return tuple(
        (-1 if j % 2 else 1)
        * det(tuple(tuple(row[k] for k in range(n) if k != j) for row in rows))
        for j in range(n)
    )


def full_spark(rows: tuple[tuple[int, ...], ...]) -> bool:
    n = len(rows[0])
    return all(det(tuple(rows[i] for i in subset)) for subset in combinations(range(len(rows)), n))


def cofactor_equations_hold(rows: tuple[tuple[int, ...], ...]) -> bool:
    n = len(rows[0])
    m = len(rows)
    assert m == 2 * n - 2
    universe = set(range(m))
    for subset in combinations(range(m), n - 1):
        if 0 not in subset:
            continue
        complement = tuple(sorted(universe.difference(subset)))
        u = cofactor_kernel(tuple(rows[i] for i in subset))
        v = cofactor_kernel(tuple(rows[i] for i in complement))
        su = sum(x * x for x in u)
        sv = sum(x * x for x in v)
        if any(u[j] * u[j] * sv != v[j] * v[j] * su for j in range(n)):
            return False
    return True


def hypersurface_witness_value(n: int) -> int:
    identity = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
    rows = identity[:-1] + identity[1:]
    first = rows[: n - 1]
    last = rows[n - 1 :]
    u = cofactor_kernel(first)
    v = cofactor_kernel(last)
    su = sum(x * x for x in u)
    sv = sum(x * x for x in v)
    return u[-1] * u[-1] * sv - v[-1] * v[-1] * su


def main() -> None:
    example3 = (
        (1, 1, 1),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
    )
    example4 = (
        (1, 1, 1, -1),
        (-1, 1, 1, 1),
        (1, -1, 1, 1),
        (1, 1, -1, -1),
        (1, -1, 1, -1),
        (1, -1, -1, 1),
    )
    assert full_spark(example3)
    assert cofactor_equations_hold(example3)
    print("published n=3 example: full spark and all cofactor equations verified")

    # The published n=4 example is not full spark and has an explicit bad pair.
    assert not full_spark(example4)
    x = (2, 1, 0, 1)
    y = (0, -1, 0, 1)
    measurements_x = tuple(abs(sum(a * b for a, b in zip(row, x))) for row in example4)
    measurements_y = tuple(abs(sum(a * b for a, b in zip(row, y))) for row in example4)
    assert measurements_x == measurements_y == (2, 0, 2, 2, 0, 2)
    common_products = tuple(a * b for a, b in zip(x, y) if a and b)
    assert min(common_products) < 0 < max(common_products)
    print("published n=4 example: explicit equal-magnitude non-WPR pair verified")

    for n in range(2, 9):
        value = hypersurface_witness_value(n)
        assert value == 1
        print(f"n={n}: explicit witness gives nonzero hypersurface polynomial F=1")

    print("all exact checks passed")


if __name__ == "__main__":
    main()
