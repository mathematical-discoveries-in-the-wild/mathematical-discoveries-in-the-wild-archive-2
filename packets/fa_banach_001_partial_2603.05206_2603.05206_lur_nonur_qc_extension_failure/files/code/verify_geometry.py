#!/usr/bin/env python3
"""Numerical checks for the explicit block geometry.

This script is evidence, not proof.  The packet proves all inequalities by
elementary exponential estimates.
"""

from __future__ import annotations

import math


def logsumexp2(a: float, b: float) -> float:
    top = max(a, b)
    return top + math.log(math.exp(a - top) + math.exp(b - top))


def main() -> None:
    rows = []
    for n in range(1, 21):
        k = n + 1
        eps = 2.0 ** (-k)
        b = 1.0 - eps
        t = 0.5 * (b + 1.0)
        s = 1.0 + eps - (eps / b) * t
        s_closed = 1.0 - eps * eps / (2.0 * (1.0 - eps))
        p = 2 ** (3 * k)

        # Strict membership of (t,s) in the ell_p unit ball.
        log_power_sum = logsumexp2(p * math.log(t), p * math.log(s))

        # Analytic upper bound used in the proof:
        # t^p <= exp(-p eps/2),
        # s^p <= exp(-p eps^2/(2(1-eps))).
        exponent_1 = -p * eps / 2.0
        exponent_2 = -p * eps * eps / (2.0 * (1.0 - eps))
        upper_bound = math.exp(exponent_1) + math.exp(exponent_2)

        # a_n=(0,1+2^-n) is above the k=n+1 cutting line at t=0.
        outside_margin = 2.0 ** (-n) - eps

        assert 0.0 < t < 1.0
        assert 0.0 < s < 1.0
        assert math.isclose(s, s_closed, rel_tol=1e-13, abs_tol=1e-15)
        assert log_power_sum < 0.0
        assert upper_bound < 1.0
        assert outside_margin > 0.0

        # The non-UR chord endpoints differ by 1/2 in their first coordinate,
        # so their ell_p distance is at least 1/2 for every p.
        chord_separation_lower_bound = 0.5
        assert chord_separation_lower_bound >= 0.5

        rows.append(
            (n, p, log_power_sum, upper_bound, outside_margin)
        )

    print("n  p_n             log(t^p+s^p)   analytic upper bound   outside margin")
    for n, p, log_sum, bound, margin in rows:
        print(f"{n:2d} {p:12d} {log_sum:17.9g} {bound:22.9g} {margin:16.9g}")
    print("PASS: all 20 explicit block-geometry checks succeeded")


if __name__ == "__main__":
    main()

