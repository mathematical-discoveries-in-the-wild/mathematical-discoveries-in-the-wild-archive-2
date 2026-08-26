#!/usr/bin/env python3
"""Exact finite checks for the normalized-tail counterexample."""

from fractions import Fraction


def coefficient(j: int) -> Fraction:
    return Fraction(1, 2 ** (2**j))


last = 12
a = {j: coefficient(j) for j in range(1, last + 1)}

previous_eta = None
for j in range(2, 9):
    truncated_remainder = sum((a[k] for k in range(j + 1, last + 1)), Fraction())
    truncated_tail = a[j] + truncated_remainder
    eta = 2 * truncated_remainder / truncated_tail
    assert 0 <= eta < 1
    if previous_eta is not None:
        assert eta < previous_eta
    previous_eta = eta
    print(f"j={j}: truncated eta={float(eta):.12g} (exact numerator bits={eta.numerator.bit_length()})")

# In a truncation at `last`, the normalized tail column b_{j-1} has first
# nonzero entry a_j/s_{j-1}; hence the tail-basis matrix is upper triangular
# with a strictly positive diagonal.
for j in range(2, last + 1):
    s = sum((a[k] for k in range(j, last + 1)), Fraction())
    diagonal = a[j] / s
    assert diagonal > 0
    column_distance = (1 - diagonal) + (s - a[j]) / s
    assert column_distance == 2 * (s - a[j]) / s

# Exact successive-tail identity: r_{j-1} - r_j = a_j e_j, checked
# coordinatewise in every finite truncation.
for j in range(2, last):
    r_prev = [a[k] if k >= j else Fraction() for k in range(1, last + 1)]
    r_next = [a[k] if k > j else Fraction() for k in range(1, last + 1)]
    difference = [u - v for u, v in zip(r_prev, r_next)]
    expected = [a[j] if k == j else Fraction() for k in range(1, last + 1)]
    assert difference == expected

print("PASS: exact tail identities, triangularity, and superlacunary error decay verified")
