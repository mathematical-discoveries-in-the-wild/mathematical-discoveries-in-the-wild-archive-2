#!/usr/bin/env python3
"""Sanity-check the two-datum algebra in the solution packet."""

from __future__ import annotations

from math import isclose, sqrt


def in_critical_interval(x: float, y: float, alpha: float, epsilon: float) -> bool:
    return 0.5 * (x - y) ** 2 <= alpha * epsilon + 1e-12


def check(alpha: float, epsilon: float) -> None:
    assert alpha > 0 and epsilon > 0
    rho = sqrt(2.0 * alpha * epsilon)
    for datum in (0.0, rho):
        assert in_critical_interval(0.0, datum, alpha, epsilon)
        assert in_critical_interval(rho, datum, alpha, epsilon)

    # Equality of a hypothetical modified Tikhonov objective at 0 and rho
    # requires these two mutually inconsistent values of S(0)-S(rho).
    required_difference_at_datum_zero = rho**2 / (2.0 * alpha)
    required_difference_at_datum_rho = -rho**2 / (2.0 * alpha)
    assert isclose(required_difference_at_datum_zero, epsilon)
    assert isclose(required_difference_at_datum_rho, -epsilon)
    assert not isclose(
        required_difference_at_datum_zero,
        required_difference_at_datum_rho,
    )


def main() -> None:
    for alpha, epsilon in ((1.0, 0.5), (0.25, 3.0), (7.0, 0.125)):
        check(alpha, epsilon)
    print("all checks passed")


if __name__ == "__main__":
    main()

