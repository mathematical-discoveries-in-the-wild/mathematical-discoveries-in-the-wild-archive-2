"""Numerical sanity check for the exact quadratic slab identity.

This is not part of the proof.
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(240702296)
    worst = 0.0
    checked = 0
    for n in (2, 3, 5, 8):
        for _ in range(500):
            mats = []
            for _j in range(2):
                raw = rng.normal(size=(n, n))
                mats.append((raw + raw.T) / 2)
            avec = [rng.normal(size=n) for _j in range(2)]
            const = rng.normal(size=2)
            lam = rng.normal(size=2)
            mu = rng.normal(size=2)
            lam /= np.linalg.norm(lam)
            mu /= np.linalg.norm(mu)

            alam = lam[0] * mats[0] + lam[1] * mats[1]
            amu = mu[0] * mats[0] + mu[1] * mats[1]
            if abs(np.linalg.det(alam)) < 1e-7 or abs(np.linalg.det(amu)) < 1e-7:
                continue
            blam = lam[0] * avec[0] + lam[1] * avec[1]
            bmu = mu[0] * avec[0] + mu[1] * avec[1]
            x = np.linalg.solve(alam, -blam)
            z = np.linalg.solve(amu, -bmu)

            def value(v: np.ndarray) -> np.ndarray:
                return np.array(
                    [
                        const[j]
                        + 2 * avec[j] @ v
                        + v @ mats[j] @ v
                        for j in range(2)
                    ]
                )

            h = z - x
            lhs = (lam + mu) @ (value(z) - value(x))
            rhs = h @ (
                (lam[0] - mu[0]) * mats[0]
                + (lam[1] - mu[1]) * mats[1]
            ) @ h
            scale = 1.0 + abs(lhs) + abs(rhs)
            worst = max(worst, abs(lhs - rhs) / scale)
            checked += 1

    print(f"checked={checked}")
    print(f"worst_scaled_error={worst:.3e}")
    if checked < 1000 or worst > 1e-10:
        raise SystemExit("slab identity check failed")


if __name__ == "__main__":
    main()

