#!/usr/bin/env python3
"""Finite cyclic-grid audit of the three-phase resolvent counterexample.

The proof is infinite-dimensional.  These discretizations verify the exact
block algebra and exhibit the comparison constants diverging with grid size.
"""

from __future__ import annotations

import numpy as np


def poisson_kernel(theta: np.ndarray, r: float = 0.5) -> np.ndarray:
    return (1.0 - r * r) / (1.0 - 2.0 * r * np.cos(theta) + r * r)


def poisson_matrix(n: int, r: float = 0.5) -> np.ndarray:
    theta = 2.0 * np.pi * np.arange(n) / n
    weights = poisson_kernel(theta, r)
    weights /= weights.sum()
    return np.vstack([np.roll(weights, i) for i in range(n)])


def audit(n: int, delta: float = 0.5) -> tuple[float, float, float]:
    k = poisson_matrix(n)
    ident = np.eye(n)
    zero = np.zeros_like(k)
    q = np.block([[zero, ident, zero], [zero, zero, ident], [k, zero, zero]])
    q3_expected = np.block([[k, zero, zero], [zero, k, zero], [zero, zero, k]])
    q3_error = float(np.max(np.abs(np.linalg.matrix_power(q, 3) - q3_expected)))

    h = np.linalg.inv(ident + delta**3 * k)
    s_formula = np.block(
        [
            [delta**2 * k @ h, h, -delta * h],
            [-delta * k @ h, delta**2 * k @ h, h],
            [k @ h, -delta * k @ h, delta**2 * k @ h],
        ]
    )
    s_direct = q @ np.linalg.inv(np.eye(3 * n) + delta * q)
    resolvent_error = float(np.max(np.abs(s_direct - s_formula)))

    # P has every matrix entry 1/(3n).  Hence S >= -cP iff every entry of
    # S is at least -c/(3n), and the least possible c is the number below.
    comparison_constant = float(3.0 * n * max(0.0, -float(s_direct.min())))

    if float(k.min()) <= 0.0:
        raise AssertionError("discrete Poisson matrix lost positivity")
    if not np.allclose(k.sum(axis=1), 1.0, atol=2e-12):
        raise AssertionError("discrete Poisson matrix is not Markov")
    if q3_error > 2e-12 or resolvent_error > 2e-11:
        raise AssertionError("block or resolvent identity failed")
    return q3_error, resolvent_error, comparison_constant


def main() -> None:
    sizes = (12, 24, 48, 96, 192)
    constants = []
    print("N  cube_error  resolvent_error  least_c  least_c/N")
    for n in sizes:
        cube_error, resolvent_error, c = audit(n)
        constants.append(c)
        print(f"{n:3d} {cube_error:11.3e} {resolvent_error:16.3e} "
              f"{c:8.3f} {c/n:10.6f}")
    if not all(y > 1.8 * x for x, y in zip(constants, constants[1:])):
        raise AssertionError("comparison constants did not grow essentially linearly")
    print("PASS: exact block identities hold and rank-one constants diverge.")


if __name__ == "__main__":
    main()
