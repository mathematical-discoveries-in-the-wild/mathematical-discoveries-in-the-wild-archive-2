#!/usr/bin/env python3
"""Arithmetic checks for the arXiv:2605.20486 counterexample packet.

The proof is analytic; this script checks its explicit parameter formulas and
representative cross-branch quotient bounds. It is not a substitute for the
topological or slope arguments in main.tex.
"""

from __future__ import annotations

import math


def epsilon(n: int) -> float:
    return 2.0 ** (-n - 3)


def dogleg_length(eps: float) -> float:
    return eps * (
        math.sqrt(5.0) / 2.0
        + math.sqrt(0.25 + (1.0 - eps) ** 2)
    )


def main() -> None:
    minimum_excess = float("inf")
    previous_ratio = 0.0
    for n in range(1, 41):
        eps = epsilon(n)
        alpha = dogleg_length(eps)
        total_length = alpha + 1.0 - 2.0 * eps
        set_descent_ratio = 2.0 / math.sqrt(1.0 + eps * eps)

        assert alpha > 2.0 * eps
        assert total_length > 1.0
        assert 1.0 < set_descent_ratio <= 2.0
        assert set_descent_ratio >= previous_ratio

        # For a limit point t and a finite-tail point r, every positive
        # cross-branch descent has numerator at most max(t-r, 0), while the
        # Euclidean denominator is sqrt((t-r)^2 + eps^4).
        for horizontal_gap in (eps / 3.0, eps, 3.0 * eps):
            upper_ratio = horizontal_gap / math.sqrt(
                horizontal_gap * horizontal_gap + eps**4
            )
            assert upper_ratio <= 1.0

        minimum_excess = min(minimum_excess, alpha - 2.0 * eps)
        previous_ratio = set_descent_ratio

    print("checked branches: 40")
    print(f"minimum sampled dogleg excess: {minimum_excess:.17g}")
    print(f"last closed-set descent quotient: {previous_ratio:.17g}")
    print("all checks passed")


if __name__ == "__main__":
    main()
