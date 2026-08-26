"""Numerical regression checks for the rank-one factorization lemma."""

from __future__ import annotations

import numpy as np


def schatten_norm(a: np.ndarray, p: float) -> float:
    return float(np.linalg.norm(np.linalg.svd(a, compute_uv=False), ord=p))


def check(seed: int, n: int, p: float) -> None:
    rng = np.random.default_rng(seed)
    mats = [rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(4)]
    a, b, x, y = mats
    q = p / (p - 1.0)

    lhs = (a * b) @ (x * y)
    pieces = []
    cost = 0.0
    for k in range(n):
        pk = np.outer(a[:, k], x[k, :])
        qk = np.outer(b[:, k], y[k, :])
        pieces.append(pk * qk)
        cost += schatten_norm(pk, p) * schatten_norm(qk, q)
    reconstructed = sum(pieces, np.zeros_like(lhs))

    product_bound = (
        schatten_norm(a, p)
        * schatten_norm(x, p)
        * schatten_norm(b, q)
        * schatten_norm(y, q)
    )
    assert np.allclose(lhs, reconstructed, rtol=1e-11, atol=1e-11)
    assert cost <= product_bound * (1.0 + 1e-11)


def main() -> None:
    for p in (2.0, 2.5, 3.0, 4.0, 8.0):
        for seed in range(20):
            check(seed=seed, n=2 + seed % 6, p=p)
    print("PASS: 100 factorization identities and Schatten-norm bounds")


if __name__ == "__main__":
    main()
