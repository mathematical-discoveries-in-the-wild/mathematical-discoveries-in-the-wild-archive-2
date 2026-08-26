"""Numerical stress test for the radial C^{1,alpha} counterexample."""

from __future__ import annotations

import numpy as np


def j_alpha(x: np.ndarray, alpha: float) -> np.ndarray:
    norm = np.linalg.norm(x)
    if norm == 0.0:
        return np.zeros_like(x)
    return norm ** (alpha - 1.0) * x


def potential(x: np.ndarray, alpha: float) -> float:
    return np.linalg.norm(x) ** (1.0 + alpha) / (1.0 + alpha)


def main() -> None:
    rng = np.random.default_rng(200401660)
    for alpha in (0.15, 0.35, 0.5, 0.8, 0.95):
        max_holder_ratio = 0.0
        max_taylor_ratio = 0.0
        for dimension in (1, 2, 5, 20, 100):
            for _ in range(2000):
                scale_x = 10.0 ** rng.uniform(-6.0, 6.0)
                scale_y = 10.0 ** rng.uniform(-6.0, 6.0)
                x = scale_x * rng.normal(size=dimension)
                y = scale_y * rng.normal(size=dimension)
                distance = np.linalg.norm(x - y)
                if distance == 0.0:
                    continue
                holder_ratio = (
                    np.linalg.norm(j_alpha(x, alpha) - j_alpha(y, alpha))
                    / distance**alpha
                )
                remainder = abs(
                    potential(y, alpha)
                    - potential(x, alpha)
                    - np.dot(j_alpha(x, alpha), y - x)
                )
                taylor_ratio = remainder / distance ** (1.0 + alpha)
                max_holder_ratio = max(max_holder_ratio, holder_ratio)
                max_taylor_ratio = max(max_taylor_ratio, taylor_ratio)

        assert max_holder_ratio <= 3.0 + 1e-12
        assert max_taylor_ratio <= 3.0 / (1.0 + alpha) + 1e-12
        support_ratios = [t ** (1.0 - alpha) for t in (1.0, 1e3, 1e6)]
        assert support_ratios[0] < support_ratios[1] < support_ratios[2]
        print(
            f"alpha={alpha:.2f} "
            f"max_holder_ratio={max_holder_ratio:.8f} "
            f"max_taylor_ratio={max_taylor_ratio:.8f} "
            f"support_ratio_at_1e6={support_ratios[-1]:.8f}"
        )
    print("all sampled radial Hölder and Taylor checks passed")


if __name__ == "__main__":
    main()
