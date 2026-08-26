#!/usr/bin/env python3
"""Check relative l_infinity inradii of tetrahedral cube partitions.

The ambient cube is [0,1]^3, whose radius for the l_infinity unit ball
[-1,1]^3 is 1/2.  For a tetrahedron T={x: a_j x <= b_j}, the largest
axis-parallel cube c+r[-1,1]^3 contained in T is obtained from the LP

    maximize r,  a_j c + r ||a_j||_1 <= b_j.

The script verifies volumes and reports the sum of these radii.
"""

from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def tetra_volume(vertices: np.ndarray) -> float:
    return abs(np.linalg.det((vertices[1:] - vertices[0]).T)) / 6.0


def linf_inradius(vertices: np.ndarray) -> tuple[float, np.ndarray]:
    hull = ConvexHull(vertices)
    # hull.equations rows are normal.x + offset <= 0 in the hull.
    normals = hull.equations[:, :3]
    offsets = hull.equations[:, 3]
    aub = np.column_stack((normals, np.abs(normals).sum(axis=1)))
    bub = -offsets
    objective = np.array([0.0, 0.0, 0.0, -1.0])
    result = linprog(
        objective,
        A_ub=aub,
        b_ub=bub,
        bounds=[(None, None), (None, None), (None, None), (0.0, None)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.x[3]), result.x[:3]


def report(name: str, vertices: np.ndarray, tetrahedra: list[tuple[int, ...]]) -> None:
    print(name)
    volume_sum = 0.0
    radius_sum = 0.0
    for index, simplex in enumerate(tetrahedra, start=1):
        tetra = vertices[np.array(simplex)]
        volume = tetra_volume(tetra)
        radius, center = linf_inradius(tetra)
        volume_sum += volume
        radius_sum += radius
        print(
            f"  T{index}: vertices={simplex} volume={volume:.12g} "
            f"radius={radius:.12g} center={np.round(center, 12).tolist()}"
        )
    print(f"  total volume={volume_sum:.12g}")
    print(f"  sum radii={radius_sum:.12g}")
    print(f"  ratio to cube radius 1/2={2.0 * radius_sum:.12g}")


def main() -> None:
    vertices = np.array(list(itertools.product([0.0, 1.0], repeat=3)))
    by_bits = {tuple(map(int, vertex)): i for i, vertex in enumerate(vertices)}

    def idx(*bits: tuple[int, int, int]) -> tuple[int, ...]:
        return tuple(by_bits[bit] for bit in bits)

    five_tetrahedra = [
        idx((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)),
        idx((1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1)),
        idx((1, 1, 1), (1, 0, 0), (1, 1, 0), (0, 1, 0)),
        idx((1, 1, 1), (1, 0, 0), (1, 0, 1), (0, 0, 1)),
        idx((1, 1, 1), (0, 1, 0), (0, 1, 1), (0, 0, 1)),
    ]

    # The standard Freudenthal triangulation into the six order chambers.
    six_tetrahedra: list[tuple[int, ...]] = []
    origin = np.array([0, 0, 0], dtype=int)
    for permutation in itertools.permutations(range(3)):
        chain = [origin.copy()]
        current = origin.copy()
        for coordinate in permutation:
            current = current.copy()
            current[coordinate] = 1
            chain.append(current)
        six_tetrahedra.append(tuple(by_bits[tuple(point)] for point in chain))

    report("Five-tetrahedron partition", vertices, five_tetrahedra)
    report("Six-tetrahedron Freudenthal partition", vertices, six_tetrahedra)


if __name__ == "__main__":
    main()

