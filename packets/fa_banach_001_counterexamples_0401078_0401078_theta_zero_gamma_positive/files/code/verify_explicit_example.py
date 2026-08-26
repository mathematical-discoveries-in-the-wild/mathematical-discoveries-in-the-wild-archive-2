#!/usr/bin/env python3
"""Exact checks for Q=(-1,1), alpha=1, epsilon=1/2."""

from fractions import Fraction


def main() -> None:
    eps = Fraction(1, 2)

    # Squared L2 norms: ||1||^2=2 and ||eps*x||^2=2 eps^2/3.
    low_sq = Fraction(2)
    high_sq = Fraction(2) * eps * eps / 3
    assert low_sq >= high_sq  # alpha=1 dominance condition for Theta.

    # For a constant P normalized to c=1 and line parameter t,
    # ||P+t(1+eps*x)||^2 / ||P||^2
    #   = (1+t)^2 + (eps^2/3)t^2.
    # Its exact minimum is eps^2/(3+eps^2).
    trace_ratio_min = eps * eps / (3 + eps * eps)
    assert trace_ratio_min == Fraction(1, 13)
    assert trace_ratio_min > 0

    print(f"low squared norm: {low_sq}")
    print(f"high squared norm: {high_sq}")
    print(f"exact normalized trace-distance minimum: {trace_ratio_min}")
    print("Theta test passes and the Gamma trace angle is strictly positive")


if __name__ == "__main__":
    main()
