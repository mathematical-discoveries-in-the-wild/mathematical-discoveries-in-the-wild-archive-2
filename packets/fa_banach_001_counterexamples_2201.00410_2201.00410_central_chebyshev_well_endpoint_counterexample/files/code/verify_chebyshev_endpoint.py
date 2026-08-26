#!/usr/bin/env python3
"""Checks for the central Chebyshev-well endpoint counterexample.

The packet proof is exact.  These symbolic and numerical checks guard against
sign, endpoint, and transcription mistakes.
"""

import math

import sympy as sp


def chebyshev_value(kappa: int, value: sp.Expr) -> sp.Expr:
    x = sp.symbols("x")
    return sp.expand(sp.chebyshevt(kappa, x)).subs(x, value)


def main() -> None:
    # Exact rational counterexample to Conjecture 7.4.
    a = sp.Rational(-1, 2)
    b = sp.Rational(1, 2)
    assert sp.simplify(chebyshev_value(2, a) - chebyshev_value(2, b)) == 0
    assert -1 < a < 0 < b < 1
    assert -a == b  # The claimed strict inequality is equality.

    # Exact identity controlling every adjacent pair.
    alpha, s = sp.symbols("alpha s", real=True)
    identity = (
        2 * sp.cos(alpha)
        - sp.cos(alpha + s)
        - sp.cos(alpha - s)
        - 2 * sp.cos(alpha) * (1 - sp.cos(s))
    )
    assert sp.trigsimp(identity) == 0

    # Exact empty-interval endpoint instances of Theorems 7.1 and 7.2.
    for kappa, j in [(6, 3), (4, 2)]:
        lower = sp.cos(sp.pi * j / kappa) ** 2
        upper = (
            sp.cos(sp.pi * (j - 1) / kappa)
            * sp.cos(sp.pi * j / kappa)
        )
        assert sp.simplify(lower) == 0
        assert sp.simplify(upper) == 0

    # Finite-grid check of the complete sign classification and equal values.
    cases = 0
    for kappa in range(2, 42):
        for j in range(1, kappa):
            alpha_f = j * math.pi / kappa
            for numerator in range(1, 10):
                s_f = numerator * math.pi / (10 * kappa)
                left = math.cos(alpha_f + s_f)
                right = math.cos(alpha_f - s_f)
                t_left = math.cos(kappa * math.acos(left))
                t_right = math.cos(kappa * math.acos(right))
                assert abs(t_left - t_right) < 2e-12

                difference = (
                    (math.cos(alpha_f) - left)
                    - (right - math.cos(alpha_f))
                )
                predicted = 2 * math.cos(alpha_f) * (1 - math.cos(s_f))
                assert abs(difference - predicted) < 2e-14
                if 2 * j < kappa:
                    assert difference > 0
                elif 2 * j == kappa:
                    assert abs(difference) < 2e-14
                else:
                    assert difference < 0
                cases += 1

    print(
        "verified: exact kappa=2 counterexample; exact kappa=4,6 empty "
        f"intervals; symbolic identity; {cases} branch-grid cases"
    )


if __name__ == "__main__":
    main()

