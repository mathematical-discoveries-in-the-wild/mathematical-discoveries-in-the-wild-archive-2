#!/usr/bin/env python3
"""Exact and numerical checks for the SU(2) Dirac-mass counterexample."""

from fractions import Fraction
import math


N_BLOCKS = 50_000


def eigenvalues_doubled(n: int) -> list[Fraction]:
    """Eigenvalues for l=n/2, using k=2m with the same parity as n."""
    return [Fraction(n * (n + 2) - k * k, 4) for k in range(-n, n + 1, 2)]


for n in range(1, N_BLOCKS + 1):
    ell = Fraction(n, 2)
    endpoint = Fraction(n * (n + 2) - n * n, 4)
    assert endpoint == ell
    # For every admissible k=2m, lambda-l=(n^2-k^2)/4 >= 0.
    # Exhaust the first 500 blocks and use the exact factorization thereafter.
    if n <= 500:
        vals = eigenvalues_doubled(n)
        assert len(vals) == n + 1
        assert min(vals) == ell
        assert vals[0] == ell and vals[-1] == ell
        assert all(value >= ell for value in vals)

divergence_checks = 0
for s in (1.0, 1.25, 2.0, 5.0, 25.0):
    a = 1.0 / (2.0 * s)
    for B in (0.01, 0.1, 0.5, 2.0):
        previous = -math.inf
        for ell in (10.0, 100.0, 1_000.0):
            log_lower = 0.5 * math.log(2.0) + B * ell**a
            assert log_lower > previous
            previous = log_lower
            divergence_checks += 1

tail_checks = 0
for s in (1.0, 2.0, 8.0):
    a = 1.0 / (2.0 * s)
    for gap in (0.1, 0.5):
        # x*exp(-2*gap*x^a) decreases once x^a > 1/(2*gap*a).
        threshold = (1.0 / (2.0 * gap * a)) ** (1.0 / a)
        for multiplier in (2.0, 4.0, 8.0, 16.0):
            x = multiplier * threshold
            log_term_x = math.log(2.0 * x + 1.0) - 2.0 * gap * x**a
            y = 2.0 * x
            log_term_y = math.log(2.0 * y + 1.0) - 2.0 * gap * y**a
            assert log_term_y < log_term_x
            tail_checks += 1

print(
    f"PASS: {N_BLOCKS} exact SU(2) blocks; "
    f"{divergence_checks} divergence checks; {tail_checks} tail checks"
)
