#!/usr/bin/env python3
"""Check the constants in the delayed-channel counterexample."""

from __future__ import annotations

import math


def product_tv(m: int, c: float) -> float:
    """TV between m biased signs of mean c and m fair signs."""
    q = 2.0 ** (-m)
    likelihood = (1.0 - c) ** m
    ratio = (1.0 + c) / (1.0 - c)
    total = 0.0
    for k in range(m + 1):
        total += q * abs(likelihood - 1.0)
        if k < m:
            q *= (m - k) / (k + 1)
            likelihood *= ratio
    return 0.5 * total


def main() -> None:
    length = 1024
    c = 1.0 / length
    max_eta_row_sum = length * c
    conjectured_rhs = 1.0 + max_eta_row_sum

    analytic_lhs = (
        math.sqrt(length) / (6.0 * math.sqrt(3.0))
        - math.exp(0.5)
        * (length + 1)
        / (8.0 * math.sqrt(2.0) * length)
    )
    exact_product_lower_lhs = 0.5 * sum(
        product_tv(m, c) for m in range(1, length + 1)
    )

    print(f"L={length}, n={2 * length}, c={c:.12g}")
    print(f"max eta row sum={max_eta_row_sum:.12g}")
    print(f"conjectured RHS={conjectured_rhs:.12g}")
    print(f"analytic lower bound on LHS={analytic_lhs:.12g}")
    print(f"exact binomial lower value for LHS={exact_product_lower_lhs:.12g}")

    assert math.isclose(max_eta_row_sum, 1.0)
    assert analytic_lhs > conjectured_rhs
    assert exact_product_lower_lhs > analytic_lhs


if __name__ == "__main__":
    main()
