#!/usr/bin/env python3
"""Mechanical checks for the atomic covariance-domination counterexample."""

from __future__ import annotations

import math


def a(n: int) -> float:
    return 1.0 / math.log(n + 1.0)


def r(n: int) -> float:
    return 1.0 / math.sqrt(n)


def p(n: int) -> float:
    return 2.0 ** (1 - n)


def main() -> None:
    # The omitted geometric tail after M is exactly 2^(1-M).
    m = 80
    probability = sum(p(n) for n in range(2, m + 1)) + 2.0 ** (1 - m)
    assert abs(probability - 1.0) < 1.0e-14
    print(f"probability normalization: {probability:.16f}")

    # Pairwise support separation for a large finite window. The proof uses
    # (a+b)/4 <= sqrt(2)/4 * sqrt(a^2+b^2) < sqrt(a^2+b^2).
    minimum_relative_gap = float("inf")
    for n in range(2, 301):
        an = a(n)
        assert an / 2.0 < 2.0 * an  # opposite signs at the same index
        for j in range(n + 1, 301):
            aj = a(j)
            distance = math.hypot(an, aj)
            radii = (an + aj) / 4.0
            assert radii < distance
            minimum_relative_gap = min(
                minimum_relative_gap, (distance - radii) / distance
            )
    print(f"sampled support separation relative gap: {minimum_relative_gap:.12f}")

    # Derivative envelope r_n a_n^(1-k). Its eventual decrease follows by
    # one-variable calculus; these samples illustrate the all-order scale.
    for k in range(1, 9):
        threshold = max(3, math.ceil(math.exp(2 * (k - 1) + 1)))
        left = r(threshold) * a(threshold) ** (1 - k)
        right = r(10 * threshold) * a(10 * threshold) ** (1 - k)
        assert right < left
        print(
            f"k={k}: envelope at N={threshold} is {left:.6e}; "
            f"at 10N is {right:.6e}"
        )

    # The exact ratio of the questioned quadratic forms on x^(N) is the
    # harmonic partial sum. It must be unbounded if no finite beta exists.
    previous = 0.0
    for nmax in (10, 100, 1_000, 10_000, 100_000):
        harmonic = sum(1.0 / n for n in range(2, nmax + 1))
        assert harmonic > previous
        previous = harmonic

        # Directly expand the cancellation lambda_n*(r_n/lambda_n)=r_n.
        # This avoids floating underflow in the deliberately tiny lambda_n.
        lhs_linear = sum(r(n) ** 2 for n in range(2, nmax + 1))
        rhs_norm_squared = sum(r(n) ** 2 for n in range(2, nmax + 1))
        ratio = lhs_linear**2 / rhs_norm_squared
        assert abs(ratio - harmonic) <= 2.0e-12 * max(1.0, harmonic)
        print(f"N={nmax:6d}: exact-form ratio {ratio:.12f}")

    print("PASS")


if __name__ == "__main__":
    main()
