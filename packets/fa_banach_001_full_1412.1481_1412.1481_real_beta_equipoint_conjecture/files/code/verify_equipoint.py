#!/usr/bin/env python3
"""Numerical diagnostics for the proof of Conjecture 1.13 in arXiv:1412.1481.

These checks are not used as proof.  They compare the original incomplete-beta
gap with the transformed integral, test the exact weighted cancellation, check
the analytic one-crossing description, and scan a broad parameter box.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, betaln


def direct_gap(a: float, b: float) -> float:
    """Right side minus left side of the conjectured probability inequality."""
    m = a / (a + b)
    return float(betainc(a + 1.0, b, m) + betainc(a, b + 1.0, m) - 1.0)


def transformed_data(a: float, b: float) -> tuple[float, float, float, float]:
    """Return H, weighted H, crossing c, and the normalized reconstructed gap."""
    q = a / b
    d = a + b

    def p(u: float) -> float:
        return u**a / (1.0 + q * u) ** (d + 1.0)

    def r(u: float) -> float:
        return u**b / (q + u) ** (d + 1.0)

    h = quad(lambda u: p(u) - r(u), 0.0, 1.0, epsabs=2e-13, epsrel=2e-13)[0]
    weighted = quad(
        lambda u: ((1.0 - u) / u) * (p(u) - r(u)),
        0.0,
        1.0,
        epsabs=2e-13,
        epsrel=2e-13,
    )[0]

    # Smaller root of b*q*u^2 - (2*b*q+q+1)*u + b*q.
    root_sum = 2.0 + (q + 1.0) / (b * q)
    crossing_stationary = 0.5 * (root_sum - math.sqrt(root_sum**2 - 4.0))

    # The probability gap is (d/B(a,b))*(q^a/b)*H.
    log_scale = math.log(d) - betaln(a, b) + a * math.log(q) - math.log(b)
    reconstructed = math.exp(log_scale) * h
    return h, weighted, crossing_stationary, reconstructed


def check_representative_cases() -> None:
    direct_cases = [
        (0.08, 0.03),
        (0.2, 0.2),
        (0.7, 0.1),
        (1.0, 0.5),
        (2.0, 1.0),
        (5.0, 2.0),
        (10.0, 9.0),
        (40.0, 3.0),
    ]
    transformed_cases = [
        # Direct quadrature of the weighted integrand is deliberately kept
        # away from very small b, where u^(b-1) is integrable but numerically
        # ill-conditioned.  The random incomplete-beta scan below still
        # covers those small-parameter cases.
        (1.0, 0.5),
        (2.0, 1.0),
        (5.0, 2.0),
        (10.0, 9.0),
        (40.0, 3.0),
    ]

    print("direct incomplete-beta cases")
    for a, b in direct_cases:
        gap = direct_gap(a, b)
        print(f"a={a:8g} b={b:8g} gap={gap:+.12e}")
        assert gap >= -2e-12

    print("transformed-integral cases")
    for a, b in transformed_cases:
        gap = direct_gap(a, b)
        h, weighted, stationary, reconstructed = transformed_data(a, b)
        print(
            f"a={a:8g} b={b:8g} gap={gap:+.12e} H={h:+.12e} "
            f"weighted={weighted:+.3e} stationary={stationary:.8f} "
            f"reconstructed={reconstructed:+.12e}"
        )
        assert gap >= -2e-12
        assert abs(weighted) <= 2e-9
        assert abs(gap - reconstructed) <= 2e-9 * max(1.0, abs(gap))
        if a > b:
            assert h > 0.0
            assert 0.0 < stationary < 1.0
        else:
            assert abs(h) <= 2e-12


def random_scan(count: int = 250_000, seed: int = 20260809) -> None:
    rng = np.random.default_rng(seed)
    # total scale from 10^-3 to 10^3; mean in [1/2, 1-10^-7].
    total = 10.0 ** rng.uniform(-3.0, 3.0, count)
    mean = rng.uniform(0.5, 1.0 - 1e-7, count)
    a = total * mean
    b = total * (1.0 - mean)
    values = betainc(a + 1.0, b, mean) + betainc(a, b + 1.0, mean) - 1.0
    idx = int(np.nanargmin(values))
    print(
        "random scan",
        f"count={count}",
        f"minimum={values[idx]:+.12e}",
        f"a={a[idx]:.12g}",
        f"b={b[idx]:.12g}",
    )
    # Tiny negative values can occur from cancellation near a=b.
    assert values[idx] >= -5e-12


if __name__ == "__main__":
    check_representative_cases()
    random_scan()
    print("all diagnostics passed")
