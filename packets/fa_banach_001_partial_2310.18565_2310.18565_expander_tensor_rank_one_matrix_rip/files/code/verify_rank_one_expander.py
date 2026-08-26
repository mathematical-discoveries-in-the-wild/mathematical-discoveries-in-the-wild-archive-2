#!/usr/bin/env python3
"""Finite regression checks for the rank-one expander-tensor proof.

The theorem is proved symbolically in main.tex.  This script checks its core
identities on explicit finite frames and reproducibly generated regular
bipartite multigraphs.  It is not a substitute for the proof or for the
all-dimensions explicit constructions cited there.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def sign_frame(n: int) -> np.ndarray:
    """All 2^n sign rows, scaled to make B^* B = I."""
    signs = np.asarray(list(itertools.product((-1.0, 1.0), repeat=n)))
    return signs / math.sqrt(signs.shape[0])


def permutation_multigraph(m: int, degree: int, seed: int):
    """A d-regular bipartite multigraph as a union of permutations."""
    rng = np.random.default_rng(seed)
    perms = np.stack([rng.permutation(m) for _ in range(degree)])
    adjacency = np.zeros((m, m), dtype=float)
    left = np.arange(m)
    for perm in perms:
        adjacency[left, perm] += 1.0
    singular = np.linalg.svd(adjacency, compute_uv=False)
    theta = float(singular[1] / degree)
    assert np.all(adjacency.sum(axis=0) == degree)
    assert np.all(adjacency.sum(axis=1) == degree)
    return perms, adjacency, theta


def edge_sum(perms: np.ndarray, f: np.ndarray, g: np.ndarray) -> float:
    return float(sum(np.dot(f, g[perm]) for perm in perms))


def sample_vectors(n: int, complex_field: bool, seed: int):
    rng = np.random.default_rng(seed)
    vectors = [np.eye(n, dtype=complex if complex_field else float)[j]
               for j in range(n)]
    vectors.append(np.ones(n, dtype=complex if complex_field else float))
    for _ in range(80):
        if complex_field:
            x = rng.normal(size=n) + 1j * rng.normal(size=n)
        else:
            x = rng.normal(size=n)
        vectors.append(x)
    return [x / np.linalg.norm(x) for x in vectors]


def verify_field(B: np.ndarray, a: float, b: float, degree: int,
                 seed: int, label: str, complex_field: bool) -> None:
    m, n = B.shape
    eye_error = np.linalg.norm(B.conj().T @ B - np.eye(n), ord=2)
    assert eye_error < 2e-12

    perms, adjacency, theta = permutation_multigraph(m, degree, seed)
    assert theta < a * a
    alpha = degree * (a * a - theta)
    beta = degree * (b * b + theta)
    delta = (beta - alpha) / (beta + alpha)
    scale = 2.0 / (alpha + beta)

    vectors = sample_vectors(n, complex_field, seed + 1)
    flat_ratios = []
    for x in vectors:
        ratio = np.linalg.norm(B @ x, 1) / (math.sqrt(m) * np.linalg.norm(x))
        flat_ratios.append(float(ratio))
        assert ratio >= a - 2e-12
        assert ratio <= b + 2e-12

    checked = 0
    worst_lower_slack = math.inf
    worst_upper_slack = math.inf
    for u in vectors[:45]:
        for v in vectors[20:65]:
            f = np.abs(B @ u)
            g = np.abs(B @ v)
            sampled = edge_sum(perms, f, g)
            frob = np.linalg.norm(u) * np.linalg.norm(v)

            # Mixing identity and its spectral error bound.
            mean_term = degree / m * f.sum() * g.sum()
            error = abs(sampled - mean_term)
            assert error <= degree * theta * np.linalg.norm(f) * np.linalg.norm(g) + 2e-10

            # Direct Frobenius-pairing factorization for one retained edge.
            j = checked % m
            k = int(perms[checked % degree, j])
            bj = B[j, :].conj()
            bk = B[k, :].conj()
            A = np.outer(bj, bk.conj())
            X = np.outer(u, v.conj())
            direct = abs(np.vdot(A, X))
            assert abs(direct - f[j] * g[k]) < 2e-11

            assert sampled >= alpha * frob - 2e-10
            assert sampled <= beta * frob + 2e-10
            rescaled = scale * sampled
            assert rescaled >= (1.0 - delta) * frob - 2e-10
            assert rescaled <= (1.0 + delta) * frob + 2e-10
            worst_lower_slack = min(worst_lower_slack,
                                    rescaled - (1.0 - delta) * frob)
            worst_upper_slack = min(worst_upper_slack,
                                    (1.0 + delta) * frob - rescaled)
            checked += 1

    print(
        f"{label}: n={n}, M={m}, d={degree}, theta={theta:.6f}, "
        f"flat_sample=[{min(flat_ratios):.6f},{max(flat_ratios):.6f}], "
        f"delta_bound={delta:.6f}, pairs={checked}, "
        f"slack=[{worst_lower_slack:.3e},{worst_upper_slack:.3e}]"
    )


def main() -> None:
    # Real all-sign frame.  The sharp p=1 Khintchine inequality gives a=1/sqrt(2),
    # while tightness gives b=1.
    B_real = sign_frame(8)
    verify_field(
        B_real,
        a=1.0 / math.sqrt(2.0),
        b=1.0,
        degree=48,
        seed=231018565,
        label="real",
        complex_field=False,
    )

    # Complexification of a real all-sign tight frame in dimension 2n.
    # Phase averaging gives the uniform lower constant pi/4; tightness gives b=1.
    R = sign_frame(6)
    P, Q = R[:, :3], R[:, 3:]
    B_complex = (P - 1j * Q) / math.sqrt(2.0)
    verify_field(
        B_complex,
        a=math.pi / 4.0,
        b=1.0,
        degree=32,
        seed=231018566,
        label="complex",
        complex_field=True,
    )

    print("VERIFIED: tight frames, expander mixing, factorization, and rank-one RIP bounds")


if __name__ == "__main__":
    main()
