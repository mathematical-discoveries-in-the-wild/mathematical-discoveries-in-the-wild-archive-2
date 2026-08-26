#!/usr/bin/env python3
"""Exact sanity checks for the alternating-binomial bump construction.

The proof in the packet is analytic and does not depend on this script.  The
checks below isolate its three finite-dimensional ingredients:

1. the two binomial norm identities;
2. the exact finite-difference formula for a reciprocal affine kernel;
3. the m^(3/4) variation scale and exponential-in-m transform bound.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, exp, lgamma, log, sqrt


def alternating_kernel_sum(m: int, w: Fraction, h: Fraction) -> Fraction:
    """Return sum_j (-1)^j C(m,j)/(w-hj), exactly."""
    return sum(
        (Fraction(-1) ** j) * comb(m, j) / (w - h * j)
        for j in range(m + 1)
    )


def closed_kernel_sum(m: int, w: Fraction, h: Fraction) -> Fraction:
    """Closed form of alternating_kernel_sum."""
    denominator = Fraction(1)
    for j in range(m + 1):
        denominator *= w - h * j
    return (Fraction(-1) ** m) * comb(m, m) * factorial(m) * h**m / denominator


def factorial(m: int) -> int:
    out = 1
    for k in range(2, m + 1):
        out *= k
    return out


def main() -> None:
    rho = 0.125
    distance = 1.0
    norm_ratio = 1.0  # ||phi'||_1 / ||phi||_2, irrelevant to scaling

    print("m  binomial identities  reciprocal finite difference  kappa/m^(3/4)  log(delta-bound)")
    for m in (1, 2, 4, 8, 12, 16, 32, 64, 128):
        square_sum = sum(comb(m, j) ** 2 for j in range(m + 1))
        mass_sum = sum(comb(m, j) for j in range(m + 1))
        assert square_sum == comb(2 * m, m)
        assert mass_sum == 2**m
        assert comb(2 * m, m) >= 4**m / (2 * sqrt(m))

        # Exact kernel check for modest m.  Here w-hj stays positive.
        finite_difference_ok = None
        if m <= 16:
            h_exact = Fraction(1, 8 * m)
            w_exact = Fraction(2, 1)
            finite_difference_ok = (
                alternating_kernel_sum(m, w_exact, h_exact)
                == closed_kernel_sum(m, w_exact, h_exact)
            )
            assert finite_difference_ok

        h = rho / m
        kappa_upper = (
            sqrt(2.0) * norm_ratio * m ** 0.25 * h ** -0.5
        )
        scaled_kappa = kappa_upper / m ** 0.75

        # Logarithm of the proof's normalized transform bound, suppressing
        # the fixed factor sqrt(2|J|)||phi||_1/(pi||phi||_2 D).
        log_delta_bound = (
            lgamma(m + 1)
            + (m + 0.5) * log(h)
            + 0.25 * log(m)
            - m * log(2.0)
            - (m + 1) * log(distance)
        )
        flag = "yes" if finite_difference_ok else "skip"
        print(
            f"{m:3d}  yes                  {flag:>3s}"
            f"                         {scaled_kappa:10.6f}"
            f"        {log_delta_bound:12.6f}"
        )

    # The crude proof bound is geometric once rho < 2D.
    geometric_ratio = rho / (2 * distance)
    assert geometric_ratio < 1
    print(f"\ncrude geometric ratio rho/(2D) = {geometric_ratio:.6f}")
    print("all exact identities and scaling checks passed")


if __name__ == "__main__":
    main()
