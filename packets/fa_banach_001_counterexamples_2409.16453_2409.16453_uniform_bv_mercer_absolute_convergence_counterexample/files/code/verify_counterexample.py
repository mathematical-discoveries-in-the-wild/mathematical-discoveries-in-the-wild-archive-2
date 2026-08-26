#!/usr/bin/env python3
"""Sanity checks for the uniform-BV Mercer SVE counterexample.

The packet contains an exact proof.  This script only checks finite versions
of the coefficient telescoping and samples the two analytic phenomena that
drive the construction.
"""

from decimal import Decimal, getcontext
from math import log, pi, sin


getcontext().prec = 70


def b_dec(n: int) -> Decimal:
    return Decimal(1) / Decimal(n + 2).ln()


def d_dec(n: int) -> Decimal:
    return b_dec(n) - b_dec(n + 1)


def delta2_dec(n: int) -> Decimal:
    return b_dec(n) - 2 * b_dec(n + 1) + b_dec(n + 2)


def finite_telescoping_checks() -> None:
    max_n = 5000
    assert all(b_dec(n) > b_dec(n + 1) > 0 for n in range(max_n))
    assert all(delta2_dec(n) > 0 for n in range(max_n))

    tol = Decimal("1e-58")
    for m in (5, 25, 100, 1000):
        lhs_mass = sum(
            (Decimal(n + 1) * delta2_dec(n) for n in range(m + 1)),
            Decimal(0),
        )
        rhs_mass = b_dec(0) - b_dec(m + 1) - Decimal(m + 1) * d_dec(m + 1)
        assert abs(lhs_mass - rhs_mass) < tol

        for k in (1, min(3, m), min(17, m)):
            lhs_coeff = sum(
                (
                    Decimal(n + 1 - k) * delta2_dec(n)
                    for n in range(k, m + 1)
                ),
                Decimal(0),
            )
            rhs_coeff = (
                b_dec(k)
                - b_dec(m + 1)
                - Decimal(m + 1 - k) * d_dec(m + 1)
            )
            assert abs(lhs_coeff - rhs_coeff) < tol

    print("PASS: b_n is decreasing and convex for n=0,...,5000")
    print("PASS: finite Fejer mass/coefficient telescoping identities")


def sampled_uniform_tail_checks() -> None:
    # This is intentionally only numerical evidence.  The packet proves the
    # uniform Cauchy estimate by an Abel/Dirichlet argument.
    m = 5000
    grid = [pi * j / 400 for j in range(401)]
    previous = None
    for n0 in (20, 50, 100, 200):
        max_tail = 0.0
        for t in grid:
            value = sum(
                sin(n * t) / (n * log(n + 2)) for n in range(n0, m + 1)
            )
            max_tail = max(max_tail, abs(value))
        print(f"sampled sup tail N={n0:3d}, M={m}: {max_tail:.6e}")
        if previous is not None:
            assert max_tail < previous
        previous = max_tail
    print("PASS: sampled sine-series tails decrease on a 401-point grid")


def divergent_point_checks() -> None:
    previous = 0.0
    for cutoff in (100, 1000, 10_000, 100_000, 1_000_000):
        total = 0.5 * sum(
            1.0 / (n * log(n + 2)) for n in range(1, cutoff + 1, 2)
        )
        assert total > previous
        previous = total
        print(f"absolute partial sum at (pi/4,pi/4), N={cutoff:7d}: {total:.8f}")
    print("PASS: absolute partial sums grow; the proof supplies divergence")


def spectrum_checks() -> None:
    values = [1.0 / (n * log(n + 2)) for n in range(1, 5001)]
    assert all(values[n] > values[n + 1] > 0 for n in range(len(values) - 1))
    assert sum(x * x for x in values) < float("inf")
    print("PASS: first 5000 positive singular coefficients are strictly decreasing")
    print("PASS: sampled coefficient square sum is finite")


if __name__ == "__main__":
    finite_telescoping_checks()
    sampled_uniform_tail_checks()
    divergent_point_checks()
    spectrum_checks()
    print("ALL SANITY CHECKS PASSED")

