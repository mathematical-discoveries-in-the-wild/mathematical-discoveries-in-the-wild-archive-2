#!/usr/bin/env python3
"""Finite-block checks for the sharp gamma+1 construction.

This is numerical evidence only.  The proof in main.tex is analytic.
"""

from __future__ import annotations

import math


def lp_norm(values: list[float], q: float) -> float:
    if math.isinf(q):
        return max(values)
    return sum(x**q for x in values) ** (1.0 / q)


def check_block(b: float, gamma: float, alpha: float, radius: float) -> None:
    w = math.exp(-b * radius)
    n = int(math.exp(alpha * radius))
    ell_r = radius**gamma  # L == 1 in the numerical check
    z = [(ell_r / (k * w)) ** (1.0 / b) for k in range(1, n + 1)]
    y = sum(x**b for x in z) ** (1.0 / b)
    coeff = [x ** (b - 1.0) / y ** (b - 1.0) for x in z]
    b_dual = b / (b - 1.0)

    print(f"R={radius:4.1f} N={n:7d}  ||a||_b'={lp_norm(coeff, b_dual):.12f}")
    for p in (1.0, 1.25, 1.5, b):
        if p > b:
            continue
        p_dual = math.inf if p == 1.0 else p / (p - 1.0)
        print(f"    p={p:4.2f}  ||a||_p'={lp_norm(coeff, p_dual):.12f}")

    harmonic_gain = w * y**b / ell_r
    output_scale = w * y**b / (math.log(y) ** (gamma + 1.0))
    beta = gamma + 0.5
    smaller_exponent_ratio = w * y**b / (math.log(y) ** beta)
    print(f"    harmonic gain={harmonic_gain:.8f}  log(N)={math.log(n):.8f}")
    print(f"    gamma+1 normalized scale={output_scale:.8f}")
    print(f"    beta={beta:.2f} obstruction ratio={smaller_exponent_ratio:.8f}")


def main() -> None:
    b = 2.0
    gamma = 0.5
    alpha = 0.8
    for radius in (4.0, 6.0, 8.0, 10.0, 12.0):
        check_block(b, gamma, alpha, radius)


if __name__ == "__main__":
    main()
