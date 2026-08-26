#!/usr/bin/env python3
"""Numerical sanity checks for the analytic 3x3 counterexample."""

from __future__ import annotations

import math

import numpy as np


def matrices(x: float, a: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    s = (1.0 + x * x) ** (a / 2.0)
    lam = np.diag([1.0 / s, 2.0 / s, 4.0 * s])
    c, q = math.cos(x), math.sin(x)
    u = np.array([[c, -q, 0.0], [q, c, 0.0], [0.0, 0.0, 1.0]])
    w = u.T @ lam @ u
    d = np.diag([1.0 / s, 1.0 / s, 4.0 * s])
    return lam, w, d


def midpoint_integral(f, left: float, right: float, count: int = 200_000) -> float:
    step = (right - left) / count
    return step * sum(f(left + (k + 0.5) * step) for k in range(count))


def main() -> None:
    for a in (0.2, 0.5, 0.8):
        for x in (-100.0, -2.3, 0.0, 0.7, 19.0):
            lam, w, d = matrices(x, a)
            eig = np.diag(lam)
            assert eig[0] < eig[1] < eig[2]
            assert np.linalg.eigvalsh(w - d).min() > -1e-10
            assert np.linalg.eigvalsh(2.0 * d - w).min() > -1e-10

        print(f"a={a}: Loewner and simple-spectrum checks passed")
        for n in (1, 4, 16, 64):
            left, right = 2.0 * math.pi * n, 2.0 * math.pi * (n + 1)
            nu_mass = midpoint_integral(
                lambda x: 0.5 * (1.0 + x * x) ** (-a / 2.0), left, right
            )
            quotient = 4.0 / nu_mass
            print(f"  N={n:2d}: nu(I_N)={nu_mass:.8g}, BMO quotient={quotient:.8g}")


if __name__ == "__main__":
    main()

