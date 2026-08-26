#!/usr/bin/env python3
"""Exact checks for the counterexample packet for arXiv:2510.00645."""

from fractions import Fraction as F


def main() -> None:
    # Atomic prototype: mu = delta_1 + delta_2 + 6 delta_3,
    # f(t)=2^(1-t), N(t)=t, and 2<h<3.
    phi_h = F(2)
    u = F(1) + F(1, 2)
    v = u + 6 * F(1, 4)
    lhs = F(1) + 2 * F(1, 2) + 6 * 3 * F(1, 4)

    assert u == F(3, 2)
    assert v == F(3)
    assert u * 2 == v
    assert (v / u) * phi_h == 4
    assert lhs == F(13, 2)

    # Literal generalized-inverse formula includes all six units at t=3.
    literal_quantile_moment = F(1) + F(2) + 6 * F(3)
    literal_rhs = (u / phi_h) * literal_quantile_moment
    assert literal_rhs == F(63, 4)
    assert lhs < literal_rhs

    # Fractional quantile: first four units of mu contain only two units
    # of the atom at t=3.
    fractional_quantile_moment = F(1) + F(2) + 2 * F(3)
    fractional_rhs = (u / phi_h) * fractional_quantile_moment
    assert fractional_rhs == F(27, 4)
    assert fractional_rhs - lhs == F(1, 4)

    # Smooth bump proof uses epsilon=1/100.  These are the rigorous lower
    # coefficient for the proposed RHS and upper coefficient for the LHS,
    # both after division by A>0.
    eps = F(1, 100)
    rhs_lower = F(27, 4) - F(3, 2) * eps
    lhs_upper = F(13, 2) + 3 * eps
    assert rhs_lower - lhs_upper == F(1, 4) - F(9, 2) * eps
    assert rhs_lower > lhs_upper

    # Parameter family: the fractional-quantile gap is (1-r)/2.
    for k in range(1, 100):
        r = F(k, 100)
        weight = (1 + r) / (r * r)
        family_lhs = 1 + 2 * r + 3 * weight * r * r
        family_rhs = F(9, 2) * (1 + r)
        assert family_rhs - family_lhs == (1 - r) / 2

    print("all exact checks passed")
    print(f"atomic fractional gap = {fractional_rhs - lhs}")
    print(f"smooth certified gap/A at epsilon=1/100 = {rhs_lower - lhs_upper}")


if __name__ == "__main__":
    main()
