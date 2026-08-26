"""Finite-grid reconnaissance for Conjecture c:convex in arXiv:1806.07225.

This is only a route-finding computation.  It runs the paper's threshold
iteration from many random bang-bang initial conditions and reports distinct
high-energy stationary states on convex planar domains.
"""

from __future__ import annotations

import argparse
import numpy as np


def points_for_domain(n: int, domain: str) -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(-1.0, 1.0, n)
    xx, yy = np.meshgrid(x, x, indexing="xy")
    if domain == "square":
        mask = np.ones_like(xx, dtype=bool)
    elif domain == "rectangle":
        # Physical domain [-2,2] x [-1,1].
        xx = 2.0 * xx
        mask = np.ones_like(xx, dtype=bool)
    elif domain == "diamond":
        mask = np.abs(xx) + np.abs(yy) <= 1.000001
    elif domain == "triangle":
        # Convex isosceles triangle with vertices (-1,-1),(1,-1),(0,1).
        mask = (yy >= -1.000001) & (yy <= 1.0 - 2.0 * np.abs(xx) + 1e-6)
    else:
        raise ValueError(domain)
    return np.column_stack([xx[mask], yy[mask]]), mask


def signature(active: np.ndarray, points: np.ndarray) -> tuple[float, ...]:
    q = points[active]
    center = q.mean(axis=0)
    cov = np.cov(q.T, bias=True) if len(q) > 1 else np.zeros((2, 2))
    return tuple(np.round([*center, cov[0, 0], cov[1, 1], cov[0, 1]], 3))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=31)
    parser.add_argument("--seeds", type=int, default=40)
    args = parser.parse_args()
    rng = np.random.default_rng(20260813)

    for domain in ("square", "rectangle", "diamond", "triangle"):
        points, _ = points_for_domain(args.n, domain)
        delta = points[:, None, :] - points[None, :, :]
        dist = np.sqrt(np.sum(delta * delta, axis=2))
        total = len(points)
        for sigma in (0.08, 0.15, 0.3, 0.7, 1.5):
            kernel = np.exp(-dist / sigma)
            for fraction in (0.1, 0.25, 0.5, 0.75, 0.9):
                count = max(1, min(total - 1, round(fraction * total)))
                for background in (0.002, 0.02, 0.2, 2.0):
                    states: dict[bytes, tuple[float, tuple[float, ...]]] = {}
                    for _ in range(args.seeds):
                        active = np.zeros(total, dtype=bool)
                        active[rng.choice(total, count, replace=False)] = True
                        rho = background + active.astype(float)
                        old_energy = -np.inf
                        for _iteration in range(300):
                            potential = kernel @ rho
                            chosen = np.argpartition(potential, -count)[-count:]
                            next_active = np.zeros(total, dtype=bool)
                            next_active[chosen] = True
                            next_rho = background + next_active.astype(float)
                            energy = float(0.5 * next_rho @ kernel @ next_rho)
                            if np.array_equal(next_active, active):
                                break
                            # Two-cycles can occur from simultaneous thresholding.
                            if energy + 1e-8 < old_energy:
                                break
                            active, rho, old_energy = next_active, next_rho, energy
                        energy = float(0.5 * rho @ kernel @ rho) / total**2
                        states[active.tobytes()] = (energy, signature(active, points))
                    ranked = sorted(states.values(), reverse=True)
                    if len(ranked) > 1 and ranked[0][0] - ranked[1][0] < 2e-6:
                        print(
                            domain,
                            f"sig={sigma:g}",
                            f"frac={fraction:g}",
                            f"bg={background:g}",
                            f"states={len(ranked)}",
                            "top=",
                            ranked[:4],
                        )


if __name__ == "__main__":
    main()
