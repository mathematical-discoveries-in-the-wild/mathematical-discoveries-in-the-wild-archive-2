#!/usr/bin/env python3
"""Numerical consistency checks for the explicit Gaussian feature curve."""

from __future__ import annotations

import math

import numpy as np


def feature(t: float, lam: float, terms: int = 180) -> np.ndarray:
    """Return a stable finite truncation of the real Gaussian feature curve."""
    out = np.empty(terms, dtype=float)
    out[0] = math.exp(-lam * t * t)
    scale = math.sqrt(2.0 * lam) * t
    for n in range(1, terms):
        out[n] = out[n - 1] * scale / math.sqrt(n)
    return out


def main() -> None:
    cases = [
        (0.1, -1.0, 0.75),
        (1.0, -0.4, 0.9),
        (5.0, -0.25, 0.3),
    ]
    print("feature-series checks")
    for lam, s, t in cases:
        lhs = float(feature(s, lam) @ feature(t, lam))
        rhs = math.exp(-lam * (s - t) ** 2)
        err = abs(lhs - rhs)
        print(f"lambda={lam:g} s={s:g} t={t:g} error={err:.3e}")
        assert err < 2e-13

    print("periodicity obstructions")
    for lam, period in [(0.1, 1.0), (1.0, 2.0), (5.0, 0.5)]:
        separation_sq = 2.0 * (1.0 - math.exp(-lam * period * period))
        print(
            f"lambda={lam:g} L={period:g} "
            f"||psi(0)-psi(L)||^2={separation_sq:.12g}"
        )
        assert separation_sq > 0.0

    print("all checks passed")


if __name__ == "__main__":
    main()
