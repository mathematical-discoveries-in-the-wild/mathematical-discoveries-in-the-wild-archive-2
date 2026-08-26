#!/usr/bin/env python3
"""Finite-dimensional sanity checks for the cyclic weighted M-splitting.

These checks illustrate the algebraic identities used in the proof.  They do
not verify the infinite-dimensional M-ideal/proximinality theorem.
"""

from __future__ import annotations

import numpy as np


def opnorm(x: np.ndarray) -> float:
    return float(np.linalg.svd(x, compute_uv=False)[0])


def main() -> None:
    rng = np.random.default_rng(12064022)
    n = 8
    r = 3
    q = np.diag([1.0] * r + [0.0] * (n - r)).astype(complex)
    q0 = np.eye(n, dtype=complex) - q

    # a, c=b*b, and f=d^(-1/2) all commute with q; c also commutes with a.
    a_diag = np.array([1.0] * r + [0.83, 0.71, 0.59, 0.43, 0.22])
    c_diag = np.array([0.7, 1.1, 0.4, 1.6, 0.8, 1.3, 0.5, 1.9])
    d_diag = np.array([1.4, 1.5, 1.2, 2.0, 1.7, 2.2, 1.1, 2.4])
    a = np.diag(a_diag).astype(complex)
    c = np.diag(c_diag).astype(complex)
    f = np.diag(d_diag ** -0.5).astype(complex)

    # A left unitary factor makes b generally fail to commute with q while
    # preserving b*b=c, matching the one-sided nature of the theorem.
    g = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    u, _ = np.linalg.qr(g)
    b = u @ np.diag(np.sqrt(c_diag))

    worst_cross = 0.0
    worst_split = 0.0
    for _ in range(200):
        hc = rng.normal(size=5) + 1j * rng.normal(size=5)
        kc = rng.normal(size=5) + 1j * rng.normal(size=5)
        h = sum(hc[j] * np.linalg.matrix_power(a, j) for j in range(5))
        k = sum(kc[j] * np.linalg.matrix_power(a, j) for j in range(5))
        x = b @ h @ f
        y = b @ k @ f
        cross = (x @ q).conj().T @ (y @ q0)
        worst_cross = max(worst_cross, opnorm(cross))
        split_error = abs(opnorm(x) - max(opnorm(x @ q), opnorm(x @ q0)))
        worst_split = max(worst_split, split_error)

    compression = opnorm(b @ f @ q)
    expected_compression = float(np.sqrt(np.max(c_diag[:r] / d_diag[:r])))

    print(f"mixed-product residual: {worst_cross:.3e}")
    print(f"max-norm split residual: {worst_split:.3e}")
    print(f"compression norm: {compression:.12f}")
    print(f"expected compression: {expected_compression:.12f}")

    assert worst_cross < 1e-11
    assert worst_split < 1e-11
    assert abs(compression - expected_compression) < 1e-11
    assert compression <= 1.0 + 1e-12
    print("PASS")


if __name__ == "__main__":
    main()
