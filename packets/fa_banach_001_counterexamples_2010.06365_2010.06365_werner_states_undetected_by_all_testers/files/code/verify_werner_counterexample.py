"""Numerical and exact-arithmetic checks for the Werner-state counterexample.

This script is supplementary evidence only.  The packet proof is analytic.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np


def flip(d: int) -> np.ndarray:
    out = np.zeros((d * d, d * d))
    for i in range(d):
        for j in range(d):
            out[j * d + i, i * d + j] = 1.0
    return out


def gamma_invariant(d: int, a: float, b: float) -> float:
    c = 1.0 - 1.0 / d
    return max(abs(b), abs(a + b / d) + c * abs(b))


def envelope_formula(d: int, mu: float) -> float:
    return 1.0 + 2.0 * max(0.0, 1.0 / d - mu)


def grid_support(d: int, mu: float, points: int = 200_001) -> float:
    """Maximize over the exact two-dimensional invariant gamma_2 ball."""
    c = 1.0 - 1.0 / d
    f = 2.0 * mu - 1.0
    b = np.linspace(-1.0, 1.0, points)
    # For fixed b, the coefficient of A=a+b/d is +1, so optimal A is
    # the positive endpoint of |A| <= 1-c|b|.
    A = 1.0 - c * np.abs(b)
    return float(np.max(A + b * (f - 1.0 / d)))


def check_optimal_factorization_formula() -> None:
    rng = np.random.default_rng(20260811)
    for d in range(2, 9):
        c = 1.0 - 1.0 / d
        for _ in range(1000):
            a, b = rng.normal(size=2)
            A = a + b / d
            B, C = abs(b), abs(A)
            claimed = gamma_invariant(d, a, b)
            if B < 1.0e-12:
                constructed = C
            elif C <= B / d:
                x2 = C / B if C else 1.0 / (2.0 * d)
                e2 = max(1.0, x2 + c)
                g2 = max(B * B, C * C / x2 + c * B * B)
                constructed = np.sqrt(e2 * g2)
            else:
                x2 = C / B
                e2 = max(1.0, x2 + c)
                g2 = max(B * B, C * C / x2 + c * B * B)
                constructed = np.sqrt(e2 * g2)
            assert abs(constructed - claimed) < 2.0e-10


def main() -> None:
    d = 3
    F = flip(d)
    rho = (5.0 * np.eye(d * d) - 3.0 * F) / 36.0
    eigenvalues = np.linalg.eigvalsh(rho)
    assert eigenvalues.min() > -1.0e-13
    assert abs(np.trace(rho) - 1.0) < 1.0e-13
    assert abs(np.trace(F @ rho) + 1.0 / 3.0) < 1.0e-13

    # Exact rational identities for the displayed counterexample.
    assert 6 * Fraction(1, 18) + 3 * Fraction(2, 9) == 1
    assert 6 * Fraction(1, 18) - 3 * Fraction(2, 9) == Fraction(-1, 3)

    for d in range(2, 11):
        for mu in np.linspace(0.0, 1.0, 101):
            assert abs(grid_support(d, float(mu), 20_001) - envelope_formula(d, float(mu))) < 2.0e-4

    check_optimal_factorization_formula()
    print("d=3, mu=1/3: trace=1, rho>=0, Tr(F rho)=-1/3")
    print("tester envelope =", envelope_formula(3, 1.0 / 3.0))
    print("checked invariant support formula for d=2..10 and 101 mu values")
    print("checked the optimal factorization construction on 7000 random (a,b,d) cases")


if __name__ == "__main__":
    main()
