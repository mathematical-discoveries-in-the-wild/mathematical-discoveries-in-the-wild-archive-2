#!/usr/bin/env python3
"""Finite-dimensional checks for the graph-projection LCE construction."""

from __future__ import annotations

import numpy as np


def main() -> None:
    n = 12
    eye = np.eye(n)

    # Coordinates are D plus E, with half-weighted inner product.
    weight = 0.5 * np.eye(2 * n)
    graph_basis = np.vstack([eye, eye])
    gram = graph_basis.T @ weight @ graph_basis
    assert np.allclose(gram, eye)

    # Orthogonal projection for the weighted inner product.
    projection = graph_basis @ graph_basis.T @ weight
    assert np.allclose(projection @ projection, projection)
    assert np.allclose(projection.T @ weight, weight @ projection)
    assert np.linalg.matrix_rank(projection) == n

    coeff = np.array([(-1.0) ** j / (j + 1.0) for j in range(n)])
    for k in range(n):
        tail = coeff.copy()
        tail[:k] = 0.0
        source = np.concatenate([tail, np.zeros(n)])
        expected = 0.5 * np.concatenate([tail, tail])
        assert np.allclose(projection @ source, expected)

    # The coordinate random variable V=sum tau_n s_n e_n has covariance
    # diag(tau_n^2) because the s_n are orthonormal.
    tau = 2.0 ** (-np.arange(1, n + 1, dtype=float))
    covariance = np.diag(tau**2)
    assert np.all(np.linalg.eigvalsh(covariance) > 0)
    assert np.linalg.matrix_rank(covariance) == n

    # In the infinite model, disjoint support gives ||Y||_2^2=sum c_n^2
    # (up to the direct-sum factor 1/2).
    finite_dominator_norm_sq = 0.5 * np.dot(coeff, coeff)
    assert finite_dominator_norm_sq < np.inf

    print("graph Gram error:", np.linalg.norm(gram - eye))
    print("projection idempotence error:", np.linalg.norm(projection @ projection - projection))
    print("finite covariance rank:", np.linalg.matrix_rank(covariance))
    print("all finite graph-projection checks passed")


if __name__ == "__main__":
    main()
