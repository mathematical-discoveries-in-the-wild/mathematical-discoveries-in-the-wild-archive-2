"""Numerical checks for the 2104.04498 Fourier-kernel partial result.

These checks confirm formulas and test sample families.  They are not used as
proof: the packet contains the exact Fourier and remainder arguments.
"""

from __future__ import annotations

import math
import numpy as np


def q_kernel(x: np.ndarray, y: np.ndarray, ax: np.ndarray, ay: np.ndarray) -> np.ndarray:
    c = np.cos(y - x)
    s2 = np.sin(y - x) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        return (2.0 * c * ax * ay - c**2 * (ax**2 + ay**2)) / s2


def quadratic_mode(mode: int, count: int = 1200) -> float:
    """Midpoint quadrature for Q[cos(mode*x)], with the diagonal omitted."""
    step = math.pi / count
    x = (np.arange(count) + 0.5) * step
    a = np.cos(mode * x)
    total = 0.0
    block = 120
    for start in range(0, count, block):
        rows = np.arange(start, min(start + block, count))
        xx = x[rows, None]
        yy = x[None, :]
        aa = a[rows, None]
        bb = a[None, :]
        values = q_kernel(xx, yy, aa, bb)
        values[np.arange(len(rows)), rows] = 0.0
        total += values.sum()
    return 0.5 * step**2 * total


def p_value(x: float, y: float, ax: float, ay: float) -> float:
    c = math.cos(y - x)
    s2 = math.sin(y - x) ** 2
    return (s2 - ax * ax - ay * ay + 2.0 * c * ax * ay) / (
        s2 * (1.0 - ax * ax) * (1.0 - ay * ay)
    )


def check_nonlinear_identity(seed: int = 7, trials: int = 1000) -> float:
    rng = np.random.default_rng(seed)
    error = 0.0
    for _ in range(trials):
        x, y = sorted(rng.uniform(0.0, math.pi, size=2))
        if y - x < 1.0e-3:
            continue
        ax, ay = rng.uniform(-0.7, 0.7, size=2)
        c = math.cos(y - x)
        s2 = math.sin(y - x) ** 2
        q = (2.0 * c * ax * ay - c * c * (ax * ax + ay * ay)) / s2
        rhs = (q - ax * ax * ay * ay) / ((1.0 - ax * ax) * (1.0 - ay * ay))
        error = max(error, abs((p_value(x, y, ax, ay) - 1.0) - rhs))
    return error


if __name__ == "__main__":
    print("mode  quadrature Q       exact Q             error")
    for n in range(1, 12, 2):
        numeric = quadratic_mode(n)
        exact = -(math.pi**2 / 2.0) * (n - 1)
        print(f"{n:4d}  {numeric: .10f}  {exact: .10f}  {numeric-exact: .3e}")
    print("max nonlinear identity error:", check_nonlinear_identity())
