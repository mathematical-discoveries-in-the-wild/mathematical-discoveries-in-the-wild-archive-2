#!/usr/bin/env python3
"""Checks supporting the C3 exceptional-pair proof.

The proof itself is symbolic and uniform. This script verifies:
1. the quaternion conjugation construction on random coefficient triples;
2. exact one-dimensional centralizer intersection for the rational
   quaternionic-unitary change of basis used to attain codimension one.
"""

from __future__ import annotations

import numpy as np
import sympy as sp


def qmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    aw, av = a[0], a[1:]
    bw, bv = b[0], b[1:]
    return np.r_[aw * bw - av @ bv, aw * bv + bw * av + np.cross(av, bv)]


def qconj(a: np.ndarray) -> np.ndarray:
    return np.r_[a[0], -a[1:]]


def qinv(a: np.ndarray) -> np.ndarray:
    return qconj(a) / (a @ a)


def random_construction_checks(trials: int = 20_000, seed: int = 20260817) -> None:
    rng = np.random.default_rng(seed)
    axis_i = np.array([0.0, 1.0, 0.0, 0.0])
    for _ in range(trials):
        r = rng.normal(size=(3, 4))
        if np.linalg.norm(r[2]) > 1e-10:
            q = qmul(qmul(qinv(r[2]), axis_i), r[2])
            a = []
            for j in range(2):
                a.append(qmul(qmul(r[j], q), qinv(r[j])))
            a.append(axis_i)
        else:
            q = axis_i
            a = [
                qmul(qmul(r[j], q), qinv(r[j]))
                if np.linalg.norm(r[j]) > 1e-10
                else np.zeros(4)
                for j in range(2)
            ]
            a.append(np.zeros(4))

        for j in range(3):
            assert abs(a[j][0]) < 1e-9
            assert np.linalg.norm(qmul(a[j], r[j]) - qmul(r[j], q)) < 1e-8
        assert np.linalg.norm(a[2][2:]) < 1e-9


def exact_minimal_intersection_check() -> None:
    # Householder reflection I-2uu^T for u=(1,2,2)/3.
    O = sp.Matrix([[7, -4, -4], [-4, 1, -8], [-4, -8, 1]]) / 9
    assert O.T * O == sp.eye(3)
    assert all(O[2, j] != 0 for j in range(3))

    # Diagonal centralizer coefficients:
    # a1=x1*i+y1*j+z1*k, a2=x2*i+y2*j+z2*k, a3=t*i.
    x1, y1, z1, x2, y2, z2, t = sp.symbols("x1 y1 z1 x2 y2 z2 t")
    coeffs = [
        sp.Matrix([x1, y1, z1]),
        sp.Matrix([x2, y2, z2]),
        sp.Matrix([t, 0, 0]),
    ]
    equations = []
    for row in (0, 1):
        off_block = sum(
            (O[row, j] * O[2, j] * coeffs[j] for j in range(3)),
            sp.zeros(3, 1),
        )
        equations.extend(off_block)
    M, _ = sp.linear_eq_to_matrix(equations, [x1, y1, z1, x2, y2, z2, t])
    assert M.rank() == 6
    kernel = M.nullspace()
    assert len(kernel) == 1
    assert kernel[0] == sp.Matrix([1, 0, 0, 1, 0, 0, 1])

    dim_sp3 = 3 * (2 * 3 + 1)
    assert dim_sp3 == 21
    assert 21 - len(kernel) == 20
    print("exact constraint rank:", M.rank())
    print("intersection basis:", list(kernel[0]))
    print("maximal product-map rank:", 20)


if __name__ == "__main__":
    random_construction_checks()
    exact_minimal_intersection_check()
    print("all checks passed")
