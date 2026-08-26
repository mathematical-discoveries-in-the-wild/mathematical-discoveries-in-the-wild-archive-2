#!/usr/bin/env python3
"""Regression checks for the constants in the expander separation proof."""

from math import exp, log


def check(r: float, d: int, log_n: float = 1000.0) -> None:
    assert 0.0 < r < 1.0 and d >= 3
    s = r / 2.0
    conjugate = s / (s - 1.0)
    kappa = -0.5 * log(1.0 - s)
    time_from_source = 0.25 * log((1.0 - conjugate) / (1.0 - s))
    assert abs(kappa - time_from_source) < 1e-12

    exponent = 2.0 / s - 1.0
    assert abs(exponent - (4.0 / r - 1.0)) < 1e-12

    # A conservative asymptotic ball-count constant.
    a_d = 1.0 / (3.0 * log(d - 1.0))
    theta = exp(-1.0 - 2.0 * exponent / a_d)
    distance = a_d * log_n
    time = theta * distance
    log_poisson_upper = distance * log(exp(1.0) * time / distance)
    log_required_lower = -exponent * log_n
    assert theta < exp(-1.0)
    assert log_poisson_upper < log_required_lower
    print(
        f"r={r:.2f}, d={d}: s'={conjugate:.6f}, "
        f"kappa={kappa:.6f}, A={exponent:.6f}, algebra passed"
    )


if __name__ == "__main__":
    for r_value in (0.1, 0.25, 0.5, 0.75, 0.99):
        for degree in (3, 4, 10):
            check(r_value, degree)
