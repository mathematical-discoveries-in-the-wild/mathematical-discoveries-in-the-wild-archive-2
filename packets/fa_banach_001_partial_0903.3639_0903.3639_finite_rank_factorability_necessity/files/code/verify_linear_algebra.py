#!/usr/bin/env python3
"""Numerical checks for the pointwise linear-algebra step in the packet."""

from __future__ import annotations

import numpy as np


def positive_sqrt(w: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(w)
    return (vecs * np.sqrt(np.maximum(vals, 0.0))) @ vecs.conj().T


def run(seed: int = 9033639) -> None:
    rng = np.random.default_rng(seed)
    worst = {
        "gram": 0.0,
        "intertwining": 0.0,
        "projection": 0.0,
        "isometry": 0.0,
        "factor_product": 0.0,
        "order_eigenvalue": float("inf"),
        "log_determinant_gap": float("inf"),
    }

    for r in range(1, 7):
        for n in range(r, r + 5):
            for _ in range(40):
                b = np.eye(r) + 0.2 * (
                    rng.normal(size=(r, r)) + 1j * rng.normal(size=(r, r))
                )
                tail = rng.normal(size=(r, n - r)) + 1j * rng.normal(size=(r, n - r))
                a = np.concatenate((b, tail), axis=1)
                w = a @ a.conj().T
                q = positive_sqrt(w)
                astar = a.conj().T
                u = q @ np.linalg.pinv(astar)
                p = astar @ np.linalg.inv(w) @ a

                worst["gram"] = max(worst["gram"], np.linalg.norm(astar.conj().T @ astar - q.conj().T @ q))
                worst["intertwining"] = max(worst["intertwining"], np.linalg.norm(u @ astar - q))
                worst["projection"] = max(worst["projection"], np.linalg.norm(u.conj().T @ u - p))
                worst["isometry"] = max(worst["isometry"], np.linalg.norm((u @ astar).conj().T @ (u @ astar) - astar.conj().T @ astar))
                f = astar @ a
                worst["factor_product"] = max(worst["factor_product"], np.linalg.norm(u @ f - q @ a))

                order_min = np.linalg.eigvalsh(w - b @ b.conj().T).min()
                worst["order_eigenvalue"] = min(worst["order_eigenvalue"], order_min)
                eig_w = np.linalg.eigvalsh(w)
                singular_b = np.linalg.svd(b, compute_uv=False)
                assert eig_w.min() > 0.0 and singular_b.min() > 0.0
                logdet_w = np.log(eig_w).sum()
                logabsdet_b = np.log(singular_b).sum()
                worst["log_determinant_gap"] = min(
                    worst["log_determinant_gap"], logdet_w - 2.0 * logabsdet_b
                )

    tolerance = 2.0e-9
    assert worst["gram"] < tolerance
    assert worst["intertwining"] < tolerance
    assert worst["projection"] < tolerance
    assert worst["isometry"] < tolerance
    assert worst["factor_product"] < tolerance
    assert worst["order_eigenvalue"] > -tolerance
    assert worst["log_determinant_gap"] > -tolerance

    print("finite-output partial-isometry checks: PASS")
    for key, value in worst.items():
        print(f"{key}: {value:.6e}")


if __name__ == "__main__":
    run()
