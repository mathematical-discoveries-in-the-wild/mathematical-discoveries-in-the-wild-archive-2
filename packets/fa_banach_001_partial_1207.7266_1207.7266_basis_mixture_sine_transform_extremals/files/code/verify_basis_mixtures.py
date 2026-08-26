#!/usr/bin/env python3
"""Numerical sanity checks for the basis-mixture theorem (not a proof)."""

from __future__ import annotations

import numpy as np


def random_rotation(rng: np.random.Generator, n: int) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def sphere_samples(rng: np.random.Generator, count: int, n: int) -> np.ndarray:
    x = rng.normal(size=(count, n))
    return x / np.linalg.norm(x, axis=1)[:, None]


def cross_support(x: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    coordinates = x @ rotation
    return np.sqrt(np.maximum(0.0, 1.0 - coordinates**2)).sum(axis=1)


def polar_proxy(support: np.ndarray, n: int) -> float:
    # V(K*)/kappa_n is the spherical mean of h_K^{-n}.
    return float(np.mean(support ** (-n)))


def sample_equator_generators(
    rng: np.random.Generator,
    rotations: list[np.ndarray],
    weights: np.ndarray,
    count: int,
) -> np.ndarray:
    """Sample zonoid generators for a mixture of 3D cross measures."""
    mix = rng.choice(len(rotations), size=count, p=weights)
    axis = rng.integers(0, 3, size=count)
    normals = np.stack([rotations[j][:, axis[k]] for k, j in enumerate(mix)])
    g = rng.normal(size=(count, 3))
    g -= np.sum(g * normals, axis=1)[:, None] * normals
    return g / np.linalg.norm(g, axis=1)[:, None]


def determinant_proxy(
    rng: np.random.Generator,
    rotations: list[np.ndarray],
    weights: np.ndarray,
    count: int,
) -> float:
    # In dimension three, zonoid volume is a common positive constant times
    # E|det(v1,v2,v3)|.  The constant cancels in comparisons.
    a = sample_equator_generators(rng, rotations, weights, count)
    b = sample_equator_generators(rng, rotations, weights, count)
    c = sample_equator_generators(rng, rotations, weights, count)
    return float(np.mean(np.abs(np.einsum("ij,ij->i", a, np.cross(b, c)))))


def main() -> None:
    rng = np.random.default_rng(12077266)
    n = 3
    rotations = [np.eye(n)] + [random_rotation(rng, n) for _ in range(4)]
    weights = np.array([0.13, 0.17, 0.19, 0.23, 0.28])

    # Each cross contributes I to its second moment.
    moment = sum(w * (r @ r.T) for w, r in zip(weights, rotations))
    assert np.allclose(moment, np.eye(n), atol=1e-12)

    x = sphere_samples(rng, 500_000, n)
    component_supports = np.stack([cross_support(x, r) for r in rotations])
    mixed_support = weights @ component_supports

    # Pointwise Jensen is the exact polar-volume argument.
    lhs = mixed_support ** (-n)
    rhs = weights @ (component_supports ** (-n))
    assert np.all(lhs <= rhs + 2e-14)

    cross_polar = polar_proxy(component_supports[0], n)
    mixed_polar = polar_proxy(mixed_support, n)
    assert mixed_polar < cross_polar

    # Independent Monte Carlo sanity check for the primal zonoid volume.
    cross_det = determinant_proxy(rng, [np.eye(n)], np.array([1.0]), 600_000)
    mixed_det = determinant_proxy(rng, rotations, weights, 600_000)
    assert mixed_det > cross_det + 5e-4

    print(f"polar proxy: mixed={mixed_polar:.9f} cross={cross_polar:.9f}")
    print(f"primal determinant proxy: mixed={mixed_det:.9f} cross={cross_det:.9f}")
    print("PASS: basis-mixture sanity checks")


if __name__ == "__main__":
    main()
