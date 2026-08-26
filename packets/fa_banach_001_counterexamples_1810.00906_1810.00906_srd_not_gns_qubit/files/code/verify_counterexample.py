#!/usr/bin/env python3
"""Numerically verify the explicit qubit SRD-not-GNS counterexample."""

from __future__ import annotations

import numpy as np


def dissipator(v: np.ndarray, a: np.ndarray) -> np.ndarray:
    vv = v.conj().T @ v
    return v.conj().T @ a @ v - 0.5 * (vv @ a + a @ vv)


def srd_offdiag_weight(p0: float, p1: float, alpha: float) -> float:
    if abs(alpha - 1.0) < 1.0e-12:
        return (p0 - p1) / np.log(p0 / p1)
    numerator = (alpha - 1.0) * (p0 ** (1.0 / alpha) - p1 ** (1.0 / alpha))
    denominator = p1 ** ((1.0 - alpha) / alpha) - p0 ** ((1.0 - alpha) / alpha)
    return numerator / denominator


def main() -> None:
    a, b, c = 1.0, 3.0, 1.0
    e00 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    e11 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    e01 = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    e10 = e01.conj().T
    basis = [e00, e11, e01, e10]

    v_plus = np.sqrt(a) * e10
    v_minus = np.sqrt(b) * e01
    v_x = np.sqrt(c) * (e01 + e10)
    lindblad_ops = [v_plus, v_minus, v_x]

    def generator(x: np.ndarray) -> np.ndarray:
        return sum((dissipator(v, x) for v in lindblad_ops), np.zeros_like(x))

    matrix = np.column_stack(
        [np.array([np.vdot(e, generator(x)) for e in basis]) for x in basis]
    )

    rate_01, rate_10 = a + c, b + c
    p0 = rate_10 / (rate_01 + rate_10)
    p1 = rate_01 / (rate_01 + rate_10)
    sigma = np.array([p0, p1, 0.0, 0.0], dtype=complex)

    expected = np.array(
        [
            [-rate_01, rate_01, 0.0, 0.0],
            [rate_10, -rate_10, 0.0, 0.0],
            [0.0, 0.0, -(a + b) / 2.0 - c, c],
            [0.0, 0.0, c, -(a + b) / 2.0 - c],
        ],
        dtype=complex,
    )
    assert np.allclose(matrix, expected)
    assert np.allclose(matrix.conj().T @ sigma, 0.0)
    assert np.allclose(generator(np.eye(2)), 0.0)

    alphas = [0.2, 0.5, 1.0, 1.5, 2.0, 4.0, 10.0]
    srd_residuals = []
    for alpha in alphas:
        f = srd_offdiag_weight(p0, p1, alpha)
        weight = np.diag([p0, p1, f, f])
        residual = weight @ matrix - matrix.conj().T @ weight
        srd_residuals.append(np.linalg.norm(residual))
    assert max(srd_residuals) < 1.0e-12

    gns_weight = np.diag([p0, p1, p1, p0])
    gns_residual = gns_weight @ matrix - matrix.conj().T @ gns_weight
    assert np.linalg.norm(gns_residual) > 0.1

    eigenvalues = np.sort(np.linalg.eigvals(matrix).real)
    expected_eigenvalues = np.sort(
        np.array([0.0, -(rate_01 + rate_10), -(a + b) / 2.0, -(a + b) / 2.0 - 2.0 * c])
    )
    assert np.allclose(eigenvalues, expected_eigenvalues)

    print("parameters:", {"a": a, "b": b, "c": c})
    print("stationary_state:", np.diag([p0, p1]))
    print("generator_basis_order: E00,E11,E01,E10")
    print(matrix.real)
    print("eigenvalues:", eigenvalues)
    print("max_SRD_self_adjointness_residual:", max(srd_residuals))
    print("GNS_self_adjointness_residual:", np.linalg.norm(gns_residual))
    print("PASS")


if __name__ == "__main__":
    main()
