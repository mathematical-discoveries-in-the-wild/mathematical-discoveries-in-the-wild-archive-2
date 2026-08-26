#!/usr/bin/env python3
"""Stable numerical checks for the variable-exponent BMO counterexample."""

from __future__ import annotations

import math


def log_power_mean(log_a: float, log_b: float, q: float, p: float) -> float:
    """Return log(((1-q)a^p+q b^p)^(1/p)) without overflow."""
    x = p * log_a
    y = p * log_b
    m = max(x, y)
    z = (1.0 - q) * math.exp(x - m) + q * math.exp(y - m)
    return (m + math.log(z)) / p


def parameters(log_l: float) -> tuple[float, float, float, float, float]:
    a = log_l
    b = math.log(a)
    q = 1.0 / b
    p = 1.0 / (a * a * b)
    log_s = -(b - 1.0) * a
    return a, b, q, p, log_s


def main() -> None:
    # The first value corresponds to b=2; a dimension-dependent proof cutoff
    # can only make the inequalities stronger.
    log_lengths = [math.e**2, 10.0, 20.0, 100.0, 1_000.0, 1_000_000.0]
    max_affine = 0.0
    max_bmo_factor = 0.0

    for log_l in log_lengths:
        a, b, q, p, log_s = parameters(log_l)
        log_a_scale = log_l - math.log(2.0)
        log_b_scale = log_s - math.log(2.0)

        log_affine = log_power_mean(log_a_scale, log_b_scale, q, p)
        log_affine -= math.log1p(p) / p
        affine = math.exp(log_affine)
        max_affine = max(max_affine, affine)

        d = a * b
        log_r = math.log(6.0 * (1.0 + d))
        bmo_factor = math.exp(log_power_mean(0.0, log_r, q, p))
        max_bmo_factor = max(max_bmo_factor, bmo_factor)

        assert abs(p * d - 1.0 / a) <= 1e-12
        assert abs((1.0 - q) * log_l + q * log_s) <= 1e-9 * max(1.0, log_l)
        assert affine <= 0.5 * math.exp(0.500001)
        assert q * log_r < 3.0
        assert p * log_r < 0.1
        assert bmo_factor < math.exp(6.0)

        print(
            f"log L={log_l:10.3g}  q={q:.6g}  p={p:.6g}  "
            f"affine={affine:.8f}  BMO-factor={bmo_factor:.8f}"
        )

    print(f"max affine norm sampled: {max_affine:.8f}")
    print(f"max BMO mixture factor sampled: {max_bmo_factor:.8f}")
    print("parameter identities and analytic bounds: PASS")


if __name__ == "__main__":
    main()
