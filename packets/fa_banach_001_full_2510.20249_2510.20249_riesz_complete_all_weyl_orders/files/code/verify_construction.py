#!/usr/bin/env python3
"""Finite checks for the all-Weyl-orders Riesz-complete construction."""

from __future__ import annotations

import math

import numpy as np


def locations(kind: str, n: int, rho: float | None = None) -> np.ndarray:
    j = np.arange(1, n + 1, dtype=float)
    if kind == "finite":
        assert rho is not None and rho > 0
        return j ** (1.0 / rho)
    if kind == "zero":
        return np.exp(np.sqrt(j))
    if kind == "infinite":
        return np.log(j + 1.0)
    raise ValueError(kind)


def heights(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    gaps = np.diff(x)
    d = np.empty_like(x)
    d[0] = min(1.0, gaps[0])
    d[-1] = min(1.0, gaps[-1])
    if len(x) > 2:
        d[1:-1] = np.minimum(1.0, np.minimum(gaps[:-1], gaps[1:]))
    j = np.arange(1, len(x) + 1, dtype=float)
    return d, np.exp2(-j) * d


def check_separation(x: np.ndarray) -> tuple[float, float]:
    d, y = heights(x)
    dx = x[:, None] - x[None, :]
    yy = y[:, None] + y[None, :]
    u = 4.0 * y[:, None] * y[None, :] / (dx * dx + yy * yy)
    np.fill_diagonal(u, 0.0)
    j = np.arange(1, len(x) + 1, dtype=float)
    bound = 4.0 * np.exp2(-j[:, None] - j[None, :])
    np.fill_diagonal(bound, 0.0)
    if np.max(u - bound) > 1e-13:
        raise AssertionError("analytic pair bound failed")
    log_products = 0.5 * np.sum(np.log1p(-u), axis=1)
    min_product = float(np.exp(np.min(log_products)))
    if min_product < math.exp(-2.0) - 1e-12:
        raise AssertionError("uniform product bound failed")
    return float(np.max(u)), min_product


def phase_height(x: np.ndarray, y: np.ndarray, r: float) -> float:
    # Integrate H(r)=int sum a_n(t) d(log t) on a logarithmic mesh.
    lo = min(1e-7, x[0] / 1000.0)
    s = np.linspace(math.log(lo), math.log(r), 12000)
    t = np.exp(s)
    total = np.zeros_like(t)
    for xn, yn in zip(x, y):
        total += (np.arctan((t - xn) / yn) + np.arctan((t + xn) / yn)) / math.pi
    return float(np.trapz(total, s))


def main() -> None:
    cases = [
        ("finite", 0.5),
        ("finite", 1.0),
        ("finite", 2.0),
        ("finite", 4.0),
        ("zero", None),
        ("infinite", None),
    ]
    for kind, rho in cases:
        x = locations(kind, 500, rho)
        d, y = heights(x)
        max_u, min_product = check_separation(x)
        cutoff = float(x[180])
        h = phase_height(x[:300], y[:300], cutoff)
        label = f"rho={rho}" if rho is not None else kind
        print(
            f"{label:>10}: max_u={max_u:.6g}, "
            f"min_product={min_product:.9f}, phase_height={h:.6g}"
        )
    print("all construction checks passed")


if __name__ == "__main__":
    main()
