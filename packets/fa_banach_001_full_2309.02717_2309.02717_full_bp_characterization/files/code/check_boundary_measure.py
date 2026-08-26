#!/usr/bin/env python3
"""Numerical sanity check for the full B_p boundary example."""

from __future__ import annotations

import math

from scipy.integrate import quad


def moment(alpha: float, n: int) -> float:
    # Scale u=v/(n+1), so the mass stays on a fixed v-window as n grows.
    # QUADPACK's algebraic weight handles v^(alpha-1) when alpha<1.
    scale = float(n + 1)
    upper = min(scale, 50.0)

    def smooth_part(v: float) -> float:
        if v == 0.0:
            return 0.0
        return ((1.0 - v / scale) ** n) / math.log(math.e * scale / v)

    scaled = quad(
        smooth_part,
        0.0,
        upper,
        weight="alg",
        wvar=(alpha - 1.0, 0.0),
        epsabs=1e-12,
        epsrel=1e-10,
        limit=300,
    )[0]
    return scaled / (scale ** alpha)


def main() -> None:
    cases = ((1.5, 0.5), (2.0, 1.0), (3.0, 1.5), (4.0, 2.0))
    for p, alpha in cases:
        print(f"p={p}, alpha={alpha}")
        for n in (32, 64, 128, 256, 512):
            mu_n = moment(alpha, n)
            scaled = mu_n * (n ** alpha) * math.log(n)
            print(f"  n={n:4d}  n^alpha log(n) mu_n={scaled:.8f}")

        # A finite-window proxy for
        # log(e*m)^(p-1) * sum_{n>=m} n^(p*alpha-1) mu_n^p.
        m = 64
        upper = 1024
        tail = 0.0
        for n in range(m, upper + 1):
            mu_n = moment(alpha, n)
            tail += ((n + 1) ** (p * alpha - 1.0)) * (mu_n ** p)
        phi = (math.log(math.e * m) ** (p - 1.0)) * tail
        print(f"  truncated Phi (m={m}, N={upper}): {phi:.8f}")


if __name__ == "__main__":
    main()
