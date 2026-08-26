#!/usr/bin/env python3
"""Deterministic checks for the ell-infinity K-set results in the packet.

The proofs are analytic.  This script independently checks their finite
matrix consequences: the vertex theorem, the arbitrary-face factorization,
the near-vertex family in dimension three, the two-dimensional classification,
and the sharp stochastic obstruction.
"""

from __future__ import annotations

import itertools
import math

import numpy as np
from scipy.optimize import linprog


TOL = 1.0e-9


def vertices(n: int) -> list[np.ndarray]:
    return [np.asarray(s, dtype=float) for s in itertools.product((-1, 1), repeat=n)]


def step_vertex_basis(n: int) -> np.ndarray:
    """Columns form the consecutive-sign vertex basis used in the proof."""
    return np.asarray(
        [[1 if column >= row else -1 for column in range(n)] for row in range(n)],
        dtype=float,
    )


def is_invertible(a: np.ndarray) -> bool:
    return abs(np.linalg.det(a)) > TOL


def is_scalar_signed_permutation(a: np.ndarray) -> bool:
    """Whether a is zero or a scalar multiple of a signed permutation."""
    if np.max(np.abs(a)) <= TOL:
        return True
    nz = np.abs(a) > TOL
    if not (np.all(nz.sum(axis=0) == 1) and np.all(nz.sum(axis=1) == 1)):
        return False
    magnitudes = np.abs(a[nz])
    return np.allclose(magnitudes, magnitudes[0], atol=TOL, rtol=0.0)


def is_signed_permutation(a: np.ndarray) -> bool:
    return is_scalar_signed_permutation(a) and np.allclose(
        np.max(np.abs(a)), 1.0, atol=TOL, rtol=0.0
    )


def local_inverse_matrices(x: np.ndarray, v: np.ndarray) -> list[np.ndarray]:
    """Return D_x T^{-1} D_v for each paired source/image vertex."""
    t = v @ np.linalg.inv(x)
    t_inv = np.linalg.inv(t)
    return [np.diag(x[:, i]) @ t_inv @ np.diag(v[:, i]) for i in range(x.shape[1])]


def is_locally_admissible(x: np.ndarray, v: np.ndarray) -> bool:
    return all(np.min(m) >= -TOL for m in local_inverse_matrices(x, v))


def preserves_at(t: np.ndarray, x: np.ndarray) -> bool:
    """Test the exact norming-simplex factorization by a small feasibility LP."""
    w = t @ x
    c = np.max(np.abs(w))
    if c <= TOL:
        return True

    source_active = np.flatnonzero(np.abs(np.abs(x) - 1.0) <= TOL)
    target_active = np.flatnonzero(np.abs(np.abs(w) - c) <= TOL)
    pulled_back = np.asarray(
        [np.sign(w[j]) * t[j, :] / c for j in target_active], dtype=float
    )

    for i in source_active:
        source_extreme = np.zeros(len(x))
        source_extreme[i] = np.sign(x[i])
        a_eq = np.vstack([pulled_back.T, np.ones(len(target_active))])
        b_eq = np.concatenate([source_extreme, [1.0]])
        result = linprog(
            np.zeros(len(target_active)),
            A_eq=a_eq,
            b_eq=b_eq,
            bounds=(0.0, None),
            method="highs",
        )
        if not result.success:
            return False
    return True


def preserves_set(t: np.ndarray, points: list[np.ndarray]) -> bool:
    return all(preserves_at(t, x) for x in points)


def exhaustive_step_basis_checks() -> None:
    for n in (2, 3, 4):
        x = step_vertex_basis(n)
        vs = vertices(n)
        admissible = 0
        invertible_images = 0
        for indices in itertools.product(range(len(vs)), repeat=n):
            v = np.column_stack([vs[index] for index in indices])
            if not is_invertible(v):
                continue
            invertible_images += 1
            if not is_locally_admissible(x, v):
                continue
            admissible += 1
            t = v @ np.linalg.inv(x)
            assert is_signed_permutation(t), (n, indices, t)

        expected = (2**n) * math.factorial(n)
        assert admissible == expected, (n, admissible, expected)
        print(
            f"dimension {n}: {invertible_images} invertible image tuples, "
            f"{admissible} admissible, all {expected} are signed permutations"
        )


def positive_inverse_grid_checks() -> None:
    rng = np.random.default_rng(240708900)
    total = 0
    for n in (2, 3, 4, 5):
        grid = list(itertools.product((-1.0, 0.0, 1.0), repeat=n))
        for _ in range(25):
            while True:
                r = rng.uniform(0.05, 1.0, size=(n, n))
                r /= r.sum(axis=1, keepdims=True)
                if is_invertible(r):
                    break
            s = np.linalg.inv(r)
            assert np.allclose(s @ np.ones(n), np.ones(n), atol=TOL, rtol=0.0)
            assert np.min(r) > 0.0
            for raw in grid:
                z = np.asarray(raw)
                if np.min(z) <= 0.0 <= np.max(z):
                    sz = s @ z
                    assert not np.all(sz > TOL)
                    assert not np.all(sz < -TOL)
                    total += 1
    print(f"positive-inverse criterion: {total} mixed-sign grid vectors checked")


def random_basis_row_matching_checks() -> None:
    rng = np.random.default_rng(89002407)
    total = 0
    for n in (3, 4, 5, 6, 7):
        vs = vertices(n)
        for _ in range(200):
            while True:
                x = np.column_stack([vs[int(rng.integers(len(vs)))] for _ in range(n)])
                if is_invertible(x):
                    break
            permutation = rng.permutation(n)
            signs = rng.choice((-1.0, 1.0), size=n)
            p = np.zeros((n, n))
            p[np.arange(n), permutation] = signs
            v = p @ x
            assert is_locally_admissible(x, v)
            assert is_signed_permutation(v @ np.linalg.inv(x))
            total += 1
    print(f"row-pattern matching: {total} random vertex bases and cube isometries checked")


def exhaustive_near_vertex_dimension_three() -> None:
    points = [
        np.asarray((0.0, 1.0, 1.0)),
        np.asarray((1.0, 0.0, 1.0)),
        np.asarray((1.0, 1.0, 0.0)),
    ]
    preserving_nonzero = 0
    for entries in itertools.product((-1.0, 0.0, 1.0), repeat=9):
        t = np.asarray(entries).reshape(3, 3)
        if not preserves_set(t, points):
            continue
        assert is_scalar_signed_permutation(t), t
        if np.max(np.abs(t)) > TOL:
            preserving_nonzero += 1
    assert preserving_nonzero == 48, preserving_nonzero
    print(
        "near-vertex frame in dimension 3: all 19,683 ternary matrices checked; "
        "the 48 nonzero preservers are signed permutations"
    )


def random_near_vertex_checks() -> None:
    rng = np.random.default_rng(711240708900)
    total = 0
    for n in (3, 4, 5, 6, 7):
        for _ in range(40):
            parameters = rng.uniform(-0.95, 0.95, size=n)
            points = []
            for i, parameter in enumerate(parameters):
                x = np.ones(n)
                x[i] = parameter
                points.append(x)
            assert is_invertible(np.column_stack(points))

            permutation = rng.permutation(n)
            signs = rng.choice((-1.0, 1.0), size=n)
            p = np.zeros((n, n))
            p[np.arange(n), permutation] = signs
            assert preserves_set(p, points)
            total += 1
    print(f"near-vertex family: {total} random frames and cube isometries checked")


def dimension_two_classification_checks() -> None:
    vertex = np.asarray((1.0, 1.0))
    smooth_one = np.asarray((1.0, 0.2))
    smooth_two = np.asarray((-0.3, 1.0))
    triple = [vertex, smooth_one, smooth_two]

    preserving_nonzero = 0
    for entries in itertools.product(range(-2, 3), repeat=4):
        t = np.asarray(entries, dtype=float).reshape(2, 2)
        if not preserves_set(t, triple):
            continue
        assert is_scalar_signed_permutation(t), t
        if np.max(np.abs(t)) > TOL:
            preserving_nonzero += 1
    assert preserving_nonzero == 16, preserving_nonzero

    diagonal = np.diag((1.0, 1.2))
    assert preserves_set(diagonal, [smooth_one, smooth_two])
    assert not is_scalar_signed_permutation(diagonal)

    r_one = np.asarray(((1.0, 0.0), (0.2, 0.8)))
    t_one = np.linalg.inv(r_one)
    assert preserves_set(t_one, [vertex, smooth_one])
    assert not is_scalar_signed_permutation(t_one)

    r_two = np.asarray(((0.8, 0.2), (0.0, 1.0)))
    t_two = np.linalg.inv(r_two)
    assert preserves_set(t_two, [vertex, smooth_two])
    assert not is_scalar_signed_permutation(t_two)
    print(
        "dimension 2: representative vertex/smooth/smooth triple and all proper "
        "pair types checked; 625 integer matrices exhausted"
    )


def stochastic_obstruction_check() -> None:
    t = np.ones((3, 3)) - 2.0 * np.eye(3)
    r = 0.5 * (np.ones((3, 3)) - np.eye(3))
    assert np.allclose(np.linalg.inv(t), r, atol=TOL, rtol=0.0)
    points = [np.ones(3), *[np.eye(3)[:, i] for i in range(3)]]
    assert preserves_set(t, points)
    assert not is_scalar_signed_permutation(t)
    print("stochastic obstruction: T=J-2I preserves at {1,e1,e2,e3} and is not an isometry")


def main() -> None:
    exhaustive_step_basis_checks()
    positive_inverse_grid_checks()
    random_basis_row_matching_checks()
    exhaustive_near_vertex_dimension_three()
    random_near_vertex_checks()
    dimension_two_classification_checks()
    stochastic_obstruction_check()
    print("ALL UNRESTRICTED K-SET PROGRAM CHECKS PASSED")


if __name__ == "__main__":
    main()
