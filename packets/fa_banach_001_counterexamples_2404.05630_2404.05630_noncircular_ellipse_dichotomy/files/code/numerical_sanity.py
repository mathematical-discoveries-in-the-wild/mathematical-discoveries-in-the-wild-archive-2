"""Deterministic sign checks for the ellipse counterexample packet.

This is not part of the proof.  It checks the explicit one-dimensional
formulas for an ellipse of semiaxis ratio 2 and a mildly thin ellipsoid.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def angular_second_moment(p: float, axis_ratio: float = 2.0) -> float:
    theta = np.linspace(0.0, 2.0 * np.pi, 400_000, endpoint=False)
    weight = (
        (np.cos(theta) / axis_ratio) ** 2 + np.sin(theta) ** 2
    ) ** (-(2.0 + p) / 2.0)
    return abs(np.mean(weight * np.exp(2j * theta))) / np.mean(weight)


def concentrated_q_mean(p: float, delta: float) -> float:
    alpha = (4.0 + p) / 2.0

    def density(t: float) -> float:
        return delta**2 * (delta**2 * t + 1.0 - t) ** (-alpha)

    split = max(0.0, 1.0 - delta**2)
    mass = quad(density, 0.0, split, epsabs=1e-12, limit=300)[0]
    mass += quad(density, split, 1.0, epsabs=1e-12, limit=300)[0]
    moment = quad(lambda t: t * density(t), 0.0, split, epsabs=1e-12, limit=300)[0]
    moment += quad(
        lambda t: t * density(t), split, 1.0, epsabs=1e-12, limit=300
    )[0]
    return moment / mass


def main() -> None:
    print("p        r_2        a          T-margin    <phi,mu>/mass")
    for p in (-1.9, -1.5, -1.0, -0.5, -0.1):
        r_2 = angular_second_moment(p)
        a = 0.5 * (1.0 + 2.0 / (1.0 + r_2))
        transform_margin = 1.0 - a * (1.0 + r_2) / 2.0
        q_mean = concentrated_q_mean(p, delta=0.1)
        pairing = 1.0 - a * q_mean
        print(
            f"{p:4.1f}  {r_2:10.7f}  {a:10.7f}  "
            f"{transform_margin:10.7f}  {pairing:14.7f}"
        )
        assert transform_margin > 0.0
        assert pairing < 0.0


if __name__ == "__main__":
    main()
