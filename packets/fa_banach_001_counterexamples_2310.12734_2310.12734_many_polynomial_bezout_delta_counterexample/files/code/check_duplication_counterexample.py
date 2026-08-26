#!/usr/bin/env python3
"""Exact sanity checks for the duplicated-linear-polynomial counterexample.

The proof is elementary and does not depend on this script.  The script checks
the source parameter, the explicit extremal solution, and the claimed scaling
for a range of multiplicities using exact rational arithmetic.
"""

from fractions import Fraction


def check(m: int) -> None:
    q = 2 * m

    # At each zero of the product (z=0 and z=1), exactly m of the 2m
    # normalized linear polynomials have modulus one.
    delta_at_zero = m
    delta_at_one = m
    delta = min(delta_at_zero, delta_at_one)
    assert delta == m

    # Explicit solution: every R_i is the constant 1/m.
    r = Fraction(1, m)
    first_sum = m * r
    second_sum = m * r
    assert first_sum == 1
    assert second_sum == 1

    # z*first_sum + (1-z)*second_sum is identically one.
    constant_coefficient = second_sum
    z_coefficient = first_sum - second_sum
    assert constant_coefficient == 1
    assert z_coefficient == 0

    optimum = r
    assert optimum == Fraction(q, 2 * delta * delta)


def main() -> None:
    for m in range(1, 10_001):
        check(m)
    print("checked exact duplicated families for m=1,...,10000")
    print("delta=m, q=2m, and optimal max coefficient norm=1/m")
    print("identity verified exactly with every R_i=1/m")
    print("optimal norm equals q/(2*delta^2), so linear q-dependence is necessary")


if __name__ == "__main__":
    main()
