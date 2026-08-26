"""Numerical sanity checks for the mixed-exponent Radon counterexample."""

from __future__ import annotations

import math
import random

import numpy as np


P = 4.0
Q = P / (P - 1.0)


def mixed_norm(v: np.ndarray) -> float:
    x, y = map(float, v)
    exponent = P if x * y >= 0.0 else Q
    return (abs(x) ** exponent + abs(y) ** exponent) ** (1.0 / exponent)


def norming(v: np.ndarray) -> np.ndarray:
    nrm = mixed_norm(v)
    if nrm == 0.0:
        raise ValueError("zero has no norming functional")
    a = v / nrm
    exponent = P if a[0] * a[1] >= 0.0 else Q
    return np.sign(a) * np.abs(a) ** (exponent - 1.0)


def radon_partner(a: np.ndarray) -> np.ndarray:
    functional = norming(a)
    return np.array([-functional[1], functional[0]])


def x_norm(x: np.ndarray) -> float:
    return math.hypot(mixed_norm(x[:2]), float(np.linalg.norm(x[2:])))


def x_norming(x: np.ndarray) -> np.ndarray:
    total = x_norm(x)
    u = x[:2]
    r = mixed_norm(u)
    first = np.zeros(2) if r == 0.0 else r * norming(u)
    return np.concatenate([first, x[2:]]) / total


def make_basis(x: np.ndarray) -> np.ndarray:
    n = len(x)
    u, h = x[:2], x[2:]
    r, s = mixed_norm(u), float(np.linalg.norm(h))
    a = np.array([1.0, 0.0]) if r == 0.0 else u / r
    b = radon_partner(a)
    c1 = np.zeros(n - 2)
    if s == 0.0:
        c1[0] = 1.0
    else:
        c1 = h / s

    # Deterministically complete c1 by Gram--Schmidt.
    cs = [c1]
    for standard in np.eye(n - 2):
        candidate = standard.copy()
        for c in cs:
            candidate -= np.dot(candidate, c) * c
        length = np.linalg.norm(candidate)
        if length > 1e-10:
            cs.append(candidate / length)
        if len(cs) == n - 2:
            break

    vectors = [
        np.concatenate([r * a, s * c1]),
        np.concatenate([-s * a, r * c1]),
        np.concatenate([b, np.zeros(n - 2)]),
    ]
    vectors.extend(np.concatenate([np.zeros(2), c]) for c in cs[1:])
    return np.column_stack(vectors)


def check() -> None:
    rng = random.Random(14075016)
    assert abs(mixed_norm(np.array([1.0, 1.0])) ** 2
               + mixed_norm(np.array([1.0, -1.0])) ** 2 - 4.0) > 0.1

    for _ in range(500):
        a = np.array([rng.uniform(-2, 2), rng.uniform(-2, 2)])
        if np.linalg.norm(a) < 1e-8:
            continue
        a /= mixed_norm(a)
        b = radon_partner(a)
        assert abs(mixed_norm(b) - 1.0) < 2e-12
        assert abs(np.dot(norming(a), b)) < 2e-12
        assert abs(np.dot(norming(b), a)) < 2e-12

    for n in range(3, 8):
        tests = [np.eye(n)[i] for i in range(n)]
        tests += [-np.eye(n)[i] for i in range(n)]
        for _ in range(100):
            raw = np.array([rng.uniform(-2, 2) for _ in range(n)])
            tests.append(raw / x_norm(raw))
        for x in tests:
            basis = make_basis(x)
            assert basis.shape == (n, n)
            assert abs(np.linalg.det(basis)) > 1e-10
            norms = np.array([x_norm(basis[:, i]) for i in range(n)])
            assert np.max(np.abs(norms - 1.0)) < 3e-11
            functionals = np.row_stack(
                [x_norming(basis[:, i]) for i in range(n)]
            )
            assert np.max(np.abs(functionals @ basis - np.eye(n))) < 3e-10

    print("verified mixed Radon identities in 500 directions")
    print("verified prescribed-vector bases in dimensions 3 through 7")
    print("verified explicit failure of the parallelogram law")


if __name__ == "__main__":
    check()

