#!/usr/bin/env python3
"""Sanity checks for the arXiv:2507.06947 Conjecture 5.10 counterexample."""

from __future__ import annotations

import math
import numpy as np


def normals_and_weight(d: int, s: int) -> tuple[np.ndarray, float]:
    if not (1 <= s < d):
        raise ValueError("require 1 <= s < d")
    r = d - s
    p = math.sqrt(s / d)
    q = math.sqrt(r / d)
    rows = []
    for j in range(s):
        for k in range(r):
            for eps in (-1.0, 1.0):
                for delta in (-1.0, 1.0):
                    u = np.zeros(d)
                    u[j] = eps * p
                    u[s + k] = delta * q
                    rows.append(u)
    return np.asarray(rows), d / (4.0 * s * r)


def cube_constant(d: int, s: int) -> float:
    q, t = divmod(d, s)
    return math.sqrt((q + 1) ** t * q ** (s - t))


def check_pair(d: int, s: int) -> None:
    u, alpha = normals_and_weight(d, s)
    assert np.allclose(np.linalg.norm(u, axis=1), 1.0, atol=1e-12)
    assert np.linalg.matrix_rank(u) == d
    assert np.allclose(alpha * u.sum(axis=0), 0.0, atol=1e-12)
    john = alpha * np.einsum("ni,nj->ij", u, u)
    assert np.allclose(john, np.eye(d), atol=1e-12)
    assert math.isclose(alpha * len(u), d, rel_tol=1e-12)

    continuous = (d / s) ** (s / 2)
    conjectured = cube_constant(d, s)
    if d % s:
        assert continuous > conjectured + 1e-12
    else:
        assert math.isclose(continuous, conjectured, rel_tol=1e-12)


def main() -> None:
    for d in range(2, 16):
        for s in range(1, d):
            check_pair(d, s)

    d, s = 3, 2
    area_section = 4 * (d / s)
    conjectured_area = 4 * cube_constant(d, s)
    print(f"smallest case d={d}, s={s}")
    print(f"section area={area_section:.12g}")
    print(f"conjectured upper area={conjectured_area:.12g}")
    print("all unit-vector, spanning, John-identity, and volume checks passed")


if __name__ == "__main__":
    main()

