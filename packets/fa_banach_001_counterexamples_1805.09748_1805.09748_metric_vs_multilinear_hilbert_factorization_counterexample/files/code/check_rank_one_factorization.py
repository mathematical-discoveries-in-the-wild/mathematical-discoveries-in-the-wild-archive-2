"""Numerical sanity checks for the rank-one cone estimates.

This script samples real rank-one tensors.  It is not used as evidence for
the proof; the inequalities checked here are proved symbolically in main.tex.
"""

from __future__ import annotations

import math
import numpy as np


def l1_normalize(x: np.ndarray) -> np.ndarray:
    return x / np.abs(x).sum()


def tensor(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return np.outer(u, v).reshape(-1)


def direction_feature(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    w = np.concatenate([u, v])
    return np.outer(w, w).reshape(-1) / np.linalg.norm(w)


def cone_feature(r: float, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return np.concatenate(([r], r * direction_feature(u, v)))


def check_dimension(m: int, trials: int, rng: np.random.Generator) -> None:
    worst_delta_over_rho = 0.0
    worst_e_over_rho = 0.0
    worst_rho_over_e = 0.0
    worst_cone_forward = 0.0
    worst_cone_inverse = 0.0

    for _ in range(trials):
        u = l1_normalize(rng.normal(size=m))
        v = l1_normalize(rng.normal(size=m))
        up = l1_normalize(rng.normal(size=m))
        vp = l1_normalize(rng.normal(size=m))
        a = tensor(u, v)
        b = tensor(up, vp)
        rho = np.abs(a - b).sum()
        delta = min(
            np.abs(u - up).sum() + np.abs(v - vp).sum(),
            np.abs(u + up).sum() + np.abs(v + vp).sum(),
        )
        e = np.linalg.norm(direction_feature(u, v) - direction_feature(up, vp))

        assert rho <= delta + 1e-10
        assert delta <= 8.0 * rho + 1e-10
        assert rho <= math.sqrt(2.0 * m) * e + 1e-10
        assert e <= 8.0 * math.sqrt(2.0) * rho + 1e-10

        worst_delta_over_rho = max(worst_delta_over_rho, delta / rho)
        worst_e_over_rho = max(worst_e_over_rho, e / rho)
        worst_rho_over_e = max(worst_rho_over_e, rho / e)

        r, s = rng.exponential(size=2)
        p, q = r * a, s * b
        d = np.abs(p - q).sum()
        D = np.linalg.norm(cone_feature(r, u, v) - cone_feature(s, up, vp))
        assert D <= 24.0 * math.sqrt(2.0) * d + 1e-10
        assert d <= 5.0 * math.sqrt(m) * D + 1e-10
        worst_cone_forward = max(worst_cone_forward, D / d)
        worst_cone_inverse = max(worst_cone_inverse, d / D)

    print(
        f"m={m:2d} trials={trials:6d} "
        f"max(delta/rho)={worst_delta_over_rho:.4f} "
        f"max(e/rho)={worst_e_over_rho:.4f} "
        f"max(rho/e)={worst_rho_over_e:.4f} "
        f"max(D/d)={worst_cone_forward:.4f} "
        f"max(d/D)={worst_cone_inverse:.4f}"
    )


def main() -> None:
    rng = np.random.default_rng(180509748)
    for m in (2, 4, 8):
        check_dimension(m, 20_000, rng)

    m0 = 2**15
    metric_bound = 120.0 * math.sqrt(2.0 * m0)
    multilinear_norm = float(m0)
    assert metric_bound < multilinear_norm
    print(
        f"finite strict gap: m={m0}, metric_bound={metric_bound:.0f}, "
        f"Gamma(J_m)={multilinear_norm:.0f}"
    )


if __name__ == "__main__":
    main()
