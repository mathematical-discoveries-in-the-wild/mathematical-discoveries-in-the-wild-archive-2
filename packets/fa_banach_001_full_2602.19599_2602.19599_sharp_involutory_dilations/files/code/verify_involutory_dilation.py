#!/usr/bin/env python3
"""Independent exact/numerical checks for the 2602.19599 proof packet."""

from __future__ import annotations

import numpy as np
import sympy as sp


def exact_checks() -> int:
    rng = np.random.default_rng(260219599)
    checks = 0
    for n in range(1, 6):
        for _ in range(8):
            entries = rng.integers(-4, 5, size=(n, n))
            A = sp.Matrix(entries.tolist()) / sp.Integer(5)
            I = sp.eye(n)
            Z = sp.zeros(n)
            S = A.row_join(I + A).col_join((I - A).row_join(-A))
            K = I.row_join(I).col_join(I.row_join(-I))
            Q = I.row_join(Z).col_join((2 * A).row_join(-I))
            assert S * S == sp.eye(2 * n)
            assert K * S * K == 2 * Q
            checks += 2

    a, lam = sp.symbols("a lam", nonnegative=True)
    M = sp.Matrix([[1 + 4 * a**2, 2 * a], [2 * a, 1]])
    charpoly = sp.factor((lam * sp.eye(2) - M).det())
    expected = sp.expand(lam**2 - (2 + 4 * a**2) * lam + 1)
    assert sp.expand(charpoly - expected) == 0
    root = (a + sp.sqrt(1 + a**2)) ** 2
    assert sp.simplify(expected.subs(lam, root)) == 0
    return checks + 2


def numerical_checks() -> tuple[int, float]:
    rng = np.random.default_rng(19599)
    checks = 0
    worst = 0.0
    for complex_case in (False, True):
        for n in range(1, 9):
            for scale in (0.0, 0.05, 0.2, 0.5, 0.9, 1.0, 1.7):
                for _ in range(10):
                    A = rng.normal(size=(n, n))
                    if complex_case:
                        A = A + 1j * rng.normal(size=(n, n))
                    raw_norm = np.linalg.norm(A, 2)
                    A = np.zeros_like(A) if scale == 0 else A * (scale / raw_norm)
                    I = np.eye(n, dtype=A.dtype)
                    S = np.block([[A, I + A], [I - A, -A]])
                    a = np.linalg.norm(A, 2)
                    predicted = a + np.sqrt(1 + a * a)
                    observed = np.linalg.norm(S, 2)
                    err = abs(observed - predicted)
                    worst = max(worst, err)
                    assert err <= 2e-12 * max(1.0, predicted)
                    assert np.linalg.norm(S @ S - np.eye(2 * n), 2) <= 2e-12
                    checks += 2
    return checks, worst


def endpoint_checks() -> int:
    rt2 = np.sqrt(2.0)
    T = np.array([[0.0, 1.0 + rt2], [rt2 - 1.0, 0.0]])
    assert np.allclose(T @ T, np.eye(2), atol=1e-14)
    assert abs(np.linalg.norm(T, 2) - (1.0 + rt2)) < 1e-14
    for a in np.linspace(-1.0, 1.0, 101):
        R = np.array([[a, np.sqrt(max(0.0, 1.0 - a * a))],
                      [np.sqrt(max(0.0, 1.0 - a * a)), -a]])
        assert np.allclose(R @ R, np.eye(2), atol=1e-14)
        assert abs(np.linalg.norm(R, 2) - 1.0) < 1e-14
    return 204


def main() -> None:
    exact = exact_checks()
    numerical, worst = numerical_checks()
    endpoints = endpoint_checks()
    print(f"exact symbolic assertions: {exact}")
    print(f"floating singular-value/involution assertions: {numerical}")
    print(f"endpoint and real-scalar assertions: {endpoints}")
    print(f"largest norm-formula error: {worst:.3e}")
    print("all involutory-dilation checks passed")


if __name__ == "__main__":
    main()
