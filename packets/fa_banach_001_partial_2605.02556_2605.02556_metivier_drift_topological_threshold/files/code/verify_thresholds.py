#!/usr/bin/env python3
"""Exact arithmetic checks for the threshold calculation in the packet."""

from fractions import Fraction


def check(d1: int, d2: int, eps: Fraction = Fraction(1, 100)) -> None:
    if not (d1 > d2 >= 1):
        raise ValueError("The source uses d1>d2>=1 for Métivier groups")
    d = d1 + d2
    q_hom = d1 + 2 * d2
    eta = eps / 4
    beta = Fraction(d2, 2) - eta
    sigma = Fraction(d, 2) + eps / 2
    a = Fraction(q_hom, 2) - beta - Fraction(1, 2)
    theta = Fraction(d1 + 3 * d2 - 1, 4) - beta
    target_endpoint = Fraction(d, 2) + eps
    parameters = (sigma, theta + 1, a + Fraction(1, 2))

    assert beta >= 0
    assert beta < Fraction(d2, 2)
    assert Fraction(d + 3, 4) <= Fraction(d, 2)
    assert max(parameters) < target_endpoint

    print(
        f"(d1,d2)=({d1},{d2}) d={d}: "
        f"sigma={sigma}, theta+1={theta + 1}, a+1/2={a + Fraction(1, 2)}, "
        f"target={target_endpoint}"
    )


def main() -> None:
    # Includes the three-dimensional Heisenberg edge case, where
    # (d+3)/4=d/2, and several larger dimension patterns.
    for dimensions in ((2, 1), (4, 1), (4, 2), (6, 1), (8, 3), (12, 5)):
        check(*dimensions)
    print("all exact threshold checks passed")


if __name__ == "__main__":
    main()
