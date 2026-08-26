#!/usr/bin/env python3
"""Deterministic bookkeeping checks for the 1/4 WKB exponent upgrade."""

from __future__ import annotations

import math


DERIVATIVE_MULTIINDICES = {
    "T": (1, 2),
    "G_low": (1, 2),
    "G_zzww": (2, 2),
    "G_zwww": (1, 3),
}


def main() -> None:
    total_orders = {name: sum(index) for name, index in DERIVATIVE_MULTIINDICES.items()}
    assert total_orders == {"T": 3, "G_low": 3, "G_zzww": 4, "G_zwww": 4}

    # The source takes the worst fixed-origin Cauchy denominator in each
    # variable: (max z derivative + 1) + (max w derivative + 1) = 3 + 4.
    source_combined_loss = (
        max(index[0] for index in DERIVATIVE_MULTIINDICES.values())
        + 1
        + max(index[1] for index in DERIVATIVE_MULTIINDICES.values())
        + 1
    )
    centered_loss = max(total_orders.values())
    assert source_combined_loss == 7
    assert centered_loss == 4

    # Check the exact optimal-truncation inequality on a deterministic grid.
    for mass in (0.25, 1.0, 3.0, 11.0):
        for exponent in range(8, 81):
            h = 2.0 ** (-exponent / 4.0)
            n = math.floor((math.e * mass * h) ** (-0.25))
            if n < 1:
                continue
            assert mass * h * n**4 <= 1.0 / math.e + 1e-14
            terminal = (mass * h * n**4) ** n
            assert terminal <= math.exp(-n) * (1.0 + 1e-12)

    print("derivative_total_orders", total_orders)
    print("source_origin_centered_combined_loss", source_combined_loss)
    print("local_centered_max_total_loss", centered_loss)
    print("optimal_truncation_grid", "PASS")


if __name__ == "__main__":
    main()

