#!/usr/bin/env python3
"""Sanity checks for the three-plane counterexample to Problem 5.4.

The proof in main.tex is exact and independent of this script.  Here we check
the incidence obstruction exactly and sample arbitrary fourth subspaces to
confirm that the lifted measurement kernel contains an indefinite singular
matrix (hence an ambiguity pair).
"""

from __future__ import annotations

import numpy as np
import sympy as sp


def projection_from_columns(columns: sp.Matrix) -> sp.Matrix:
    """Exact orthogonal projection onto the rational column span."""
    if columns.cols == 0:
        return sp.zeros(3)
    gram = columns.T * columns
    return sp.simplify(columns * gram.inv() * columns.T)


def plane_projection(normal: sp.Matrix) -> sp.Matrix:
    return sp.eye(3) - normal * normal.T / (normal.dot(normal))


def sym_from_coordinates(v: sp.Matrix) -> sp.Matrix:
    a, b, c, d, e, f = v
    return sp.Matrix([[a, b, c], [b, d, e], [c, e, f]])


def measurement_row(p: sp.Matrix) -> sp.Matrix:
    # tr(PQ), for Q=[[a,b,c],[b,d,e],[c,e,f]].
    return sp.Matrix([[p[0, 0], 2 * p[0, 1], 2 * p[0, 2],
                       p[1, 1], 2 * p[1, 2], p[2, 2]]])


def singular_indefinite_witness(projections: list[sp.Matrix]) -> sp.Matrix:
    measurement = sp.Matrix.vstack(*(measurement_row(p) for p in projections))
    kernel = measurement.nullspace()
    assert len(kernel) >= 2
    a = sym_from_coordinates(kernel[0])
    b = sym_from_coordinates(kernel[1])
    t = sp.symbols("t", real=True)
    polynomial = sp.Poly(sp.expand((a + t * b).det()), t)

    candidates: list[sp.Matrix] = []
    if b.det() == 0:
        candidates.append(b)
    if polynomial.is_zero:
        candidates.append(a)
    else:
        for root in sp.nroots(polynomial):
            if abs(complex(root).imag) < 1e-9:
                candidates.append(a + float(sp.re(root)) * b)

    for q in candidates:
        qn = np.array(q.evalf(), dtype=float)
        eigenvalues = np.linalg.eigvalsh(qn)
        if eigenvalues[0] < -1e-7 and eigenvalues[-1] > 1e-7:
            residual = max(abs(float(sp.trace(p * q).evalf())) for p in projections)
            assert residual < 1e-7
            assert abs(float(q.det().evalf())) < 1e-6
            return q
    raise AssertionError("sample did not yield the expected indefinite singular witness")


def random_rational_subspace(rng: np.random.Generator, rank: int) -> sp.Matrix:
    if rank == 0:
        return sp.zeros(3)
    if rank == 3:
        return sp.eye(3)
    while True:
        raw = rng.integers(-4, 5, size=(3, rank))
        columns = sp.Matrix(raw.tolist())
        if columns.rank() == rank:
            return projection_from_columns(columns)


def main() -> None:
    e1 = sp.Matrix([1, 0, 0])
    e2 = sp.Matrix([0, 1, 0])
    n3 = sp.Matrix([1, 1, 1])
    normals = [e1, e2, n3]
    projections = [plane_projection(n) for n in normals]

    assert sp.Matrix.hstack(*normals).det() == 1
    assert all(p.rank() == 2 and p * p == p and p.T == p for p in projections)

    # If H=W_k, the only possible one-dimensional first span would be the
    # intersection of the other two planes.  It is not orthogonal to the
    # indicated intersection with H, for each of the three choices of k.
    dot_obstructions = []
    for k in range(3):
        i, j = [idx for idx in range(3) if idx != k]
        line_other_two = normals[i].cross(normals[j])
        line_i_with_h = normals[i].cross(normals[k])
        dot_obstructions.append(sp.expand(line_other_two.dot(line_i_with_h)))
    assert all(value != 0 for value in dot_obstructions)

    rng = np.random.default_rng(150806687)
    sample_count = 0
    for rank in range(4):
        repetitions = 1 if rank in (0, 3) else 50
        for _ in range(repetitions):
            p4 = random_rational_subspace(rng, rank)
            singular_indefinite_witness(projections + [p4])
            sample_count += 1

    print("three plane projections verified exactly")
    print("partition dot-product obstructions:", dot_obstructions)
    print("fourth-subspace samples checked:", sample_count)
    print("all sampled lifted kernels contained an indefinite singular witness")


if __name__ == "__main__":
    main()
