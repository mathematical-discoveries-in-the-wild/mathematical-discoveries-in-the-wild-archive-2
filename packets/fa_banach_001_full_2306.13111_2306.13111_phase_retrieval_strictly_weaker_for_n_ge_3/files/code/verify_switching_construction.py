"""Exact checks for the construction in the arXiv:2306.13111 packet."""

from __future__ import annotations

import itertools

import sympy as sp


def vandermonde_column(t: int, d: int) -> sp.Matrix:
    return sp.Matrix([sp.Integer(t) ** j for j in range(d)])


def sorted_projection_multiset(rows: list[sp.Matrix], a: sp.Matrix) -> list[sp.Expr]:
    return sorted((sp.expand(row.dot(a)) for row in rows), key=sp.default_sort_key)


def check_dimension(d: int) -> None:
    columns = [vandermonde_column(t, d) for t in range(1, 2 * d)]

    # Every d-column determinant is a nonzero Vandermonde determinant.
    for subset in itertools.combinations(range(2 * d - 1), d):
        determinant = sp.Matrix.hstack(*(columns[j] for j in subset)).det()
        assert determinant != 0

    left = columns[: d - 1]
    right = columns[d - 1 : 2 * d - 2]
    last = columns[-1]

    left_matrix = sp.Matrix.hstack(*left)
    right_matrix = sp.Matrix.hstack(*right)
    u = left_matrix.T.nullspace()[0]
    v = right_matrix.T.nullspace()[0]
    assert last.dot(u) != 0
    assert last.dot(v) != 0

    r1 = sp.expand(last.dot(v)) * u
    r2 = -sp.expand(last.dot(u)) * v
    r3 = -(r1 + r2)
    rows_x = [r1, r2, r3]
    rows_y = [-r1, -r2, -r3]

    assert all(row != sp.zeros(d, 1) for row in rows_x)
    assert r1 + r2 + r3 == sp.zeros(d, 1)
    for column in columns:
        assert sorted_projection_multiset(rows_x, column) == sorted_projection_multiset(
            rows_y, column
        )

    tuples_x = [tuple(row) for row in rows_x]
    tuples_y = [tuple(row) for row in rows_y]
    assert sorted(tuples_x, key=str) != sorted(tuples_y, key=str)


def check_metric_slice() -> None:
    examples = [
        (sp.Matrix([1, 2, -3]), sp.Matrix([2, -1, 4])),
        (sp.Matrix([0, 0, 0]), sp.Matrix([1, -2, 1])),
        (sp.Matrix([3, -2, 5]), sp.Matrix([-3, 2, -5])),
    ]
    for x, y in examples:
        phase_squared = min((x - y).dot(x - y), (x + y).dot(x + y))
        c = x.dot(y)
        matching_squared = 2 * x.dot(x) + 2 * y.dot(y) - 4 * abs(c)
        assert sp.expand(matching_squared - 2 * phase_squared) == 0


def main() -> None:
    for dimension in range(2, 9):
        check_dimension(dimension)
        print(f"d={dimension}: full-spark and switching checks passed")
    check_metric_slice()
    print("scaled metric-slice checks passed")


if __name__ == "__main__":
    main()
