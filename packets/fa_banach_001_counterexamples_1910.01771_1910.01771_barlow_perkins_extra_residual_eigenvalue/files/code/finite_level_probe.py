"""Finite-level probe for the Barlow--Perkins Dirichlet half problem.

For a chosen spectral parameter lambda, solve the lambda-eigenfunction
extension on a level-m finite gasket with antisymmetric outer boundary data.
The scaling is chosen so that the two vertices beside the fixed apex have
values +1 and -1 when spectral decimation behaves as expected.
"""

from __future__ import annotations

import argparse

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


Point = tuple[int, int]
Triangle = tuple[Point, Point, Point]


def midpoint(x: Point, y: Point) -> Point:
    return ((x[0] + y[0]) // 2, (x[1] + y[1]) // 2)


def gasket_graph(level: int) -> tuple[list[Point], dict[Point, set[Point]]]:
    size = 2**level
    triangles: list[Triangle] = [((0, 0), (size, 0), (0, size))]
    for _ in range(level):
        refined: list[Triangle] = []
        for a, b, c in triangles:
            ab, ac, bc = midpoint(a, b), midpoint(a, c), midpoint(b, c)
            refined.extend(((a, ab, ac), (ab, b, bc), (ac, bc, c)))
        triangles = refined

    adjacency: dict[Point, set[Point]] = {}
    for triangle in triangles:
        for x in triangle:
            adjacency.setdefault(x, set())
        for i in range(3):
            for j in range(i + 1, 3):
                x, y = triangle[i], triangle[j]
                adjacency[x].add(y)
                adjacency[y].add(x)
    return sorted(adjacency), adjacency


def iterate_r(lam: float, level: int) -> float:
    for _ in range(level):
        lam = lam * (5.0 - lam)
    return lam


def product_p(lam: float, level: int) -> float:
    product = 1.0
    for _ in range(level):
        product *= (6.0 - lam) / ((2.0 - lam) * (5.0 - lam))
        lam = lam * (5.0 - lam)
    return product


def solve_level(level: int, lam: float, mode: str) -> tuple[dict[Point, float], float]:
    vertices, adjacency = gasket_graph(level)
    size = 2**level
    q_left, q_right, q_apex = (0, 0), (size, 0), (0, size)
    if mode == "antisymmetric":
        outer_amplitude = iterate_r(lam, level) / lam
        right_amplitude = -outer_amplitude
    else:
        outer_amplitude = 1.0 / product_p(lam, level)
        right_amplitude = outer_amplitude
    boundary = {q_left: outer_amplitude, q_right: right_amplitude, q_apex: 0.0}
    interior = [x for x in vertices if x not in boundary]
    index = {x: i for i, x in enumerate(interior)}

    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    rhs = np.zeros(len(interior))
    for x in interior:
        row = index[x]
        rows.append(row)
        cols.append(row)
        data.append(4.0 - lam)
        for y in adjacency[x]:
            if y in index:
                rows.append(row)
                cols.append(index[y])
                data.append(-1.0)
            else:
                rhs[row] += boundary[y]

    values = dict(boundary)
    solution = spsolve(csr_matrix((data, (rows, cols)), shape=(len(interior),) * 2), rhs)
    values.update({x: float(solution[index[x]]) for x in interior})
    return values, outer_amplitude


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda-value", type=float, default=3.0 - np.sqrt(3.0))
    parser.add_argument("--max-level", type=int, default=8)
    parser.add_argument("--mode", choices=("antisymmetric", "symmetric"), default="antisymmetric")
    args = parser.parse_args()

    print("lambda", args.lambda_value)
    for level in range(1, args.max_level + 1):
        values, outer = solve_level(level, args.lambda_value, args.mode)
        size = 2**level
        inner_left = values[(0, size - 1)]
        inner_right = values[(1, size - 1)]
        maximum = max(abs(value) for value in values.values())
        print(
            level,
            "vertices", len(values),
            "outer", f"{outer:.12g}",
            "inner", f"({inner_left:.12g},{inner_right:.12g})",
            "sup", f"{maximum:.12g}",
        )


if __name__ == "__main__":
    main()
