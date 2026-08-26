#!/usr/bin/env python3
"""Rigorous interval certificate for the h_1 Gabor frame at ab=4/7.

The proof packet explains why the quantity T/D below controls a selected
Zibulski--Zeevi determinant.  All interval operations use outward-rounded
mpmath interval arithmetic.  The exact Fraction checks prove that every
non-dominant Zak monomial has a larger Gaussian exponent, so the worst
rectangle is the square lattice a=b=sqrt(4/7).
"""

import itertools
from fractions import Fraction

from mpmath import iv


iv.dps = 50
P = 4
Q = 7
BOXES_PER_HALF = 512
ZAK_CUTOFF = 2
K_SQUARE = iv.pi * iv.mpf(4) / 7
PERMUTATIONS = tuple(itertools.permutations(range(P)))


HALVES = (
    {
        "name": "0 <= y <= 1/8",
        "interval": (Fraction(0), Fraction(1, 8)),
        "columns": (1, 4, 5, 6),
        "lead": (3, 2, 1, 0),
        "base": (
            (Fraction(1), Fraction(-3), Fraction(-2), Fraction(-1)),
            (Fraction(11, 4), Fraction(-5, 4), Fraction(-1, 4), Fraction(3, 4)),
            (Fraction(-5, 2), Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)),
            (Fraction(-3, 4), Fraction(9, 4), Fraction(13, 4), Fraction(-11, 4)),
        ),
    },
    {
        "name": "1/8 <= y <= 1/4",
        "interval": (Fraction(1, 8), Fraction(1, 4)),
        "columns": (0, 1, 4, 6),
        "lead": (0, 3, 2, 1),
        "base": (
            (Fraction(0), Fraction(1), Fraction(-3), Fraction(-1)),
            (Fraction(7, 4), Fraction(11, 4), Fraction(-5, 4), Fraction(3, 4)),
            (Fraction(-7, 2), Fraction(-5, 2), Fraction(1, 2), Fraction(5, 2)),
            (Fraction(-7, 4), Fraction(-3, 4), Fraction(9, 4), Fraction(-11, 4)),
        ),
    },
)


def fraction_interval(value):
    return iv.mpf(value.numerator) / value.denominator


def phi(c):
    """Dimensionless magnitude |c| exp(-(4*pi/7)c^2)."""
    return abs(c) * iv.exp(-K_SQUARE * c * c)


def zak_tail_bound(cutoff):
    """Bound both centered tails |n| >= cutoff+1.

    Every centered coefficient lies in [-7/2,7/2].  With
    A=7(cutoff+1)-7/2 and g(u)=u exp(-(4*pi/7)u^2), monotonicity gives
      2 sum_{n=cutoff+1}^infty g(7n-7/2)
      <= 2 (g(A) + (1/7) integral_A^infty g(u)du).
    """
    a = iv.mpf(Q * (cutoff + 1)) - iv.mpf(Q) / 2
    exponential = iv.exp(-K_SQUARE * a * a)
    return 2 * (a * exponential + exponential / (2 * Q * K_SQUARE))


def square_sum(base, permutation, y):
    return sum((y + base[row][col]) ** 2 for row, col in enumerate(permutation))


def derived_centered_base(row, original_column, sample_y):
    raw = sample_y + Fraction(original_column) + Fraction(Q * row, P)
    nearest_period = (raw / Q + Fraction(1, 2)).numerator // (raw / Q + Fraction(1, 2)).denominator
    return Fraction(original_column) + Fraction(Q * row, P) - Q * nearest_period


def exact_geometry_checks(half):
    y0, y1 = half["interval"]
    base = half["base"]
    lead = half["lead"]
    sample_y = (y0 + y1) / 2

    derived = tuple(
        tuple(derived_centered_base(row, original_column, sample_y) for original_column in half["columns"])
        for row in range(P)
    )
    if derived != base:
        raise AssertionError(f"centered matrix mismatch: derived={derived}, recorded={base}")

    max_abs = max(
        abs(y + base[row][col])
        for y in (y0, y1)
        for row in range(P)
        for col in range(P)
    )
    if max_abs > Fraction(27, 8):
        raise AssertionError(f"unexpected centered coefficient: {max_abs}")

    lead_min_abs = None
    for row, col in enumerate(lead):
        left = y0 + base[row][col]
        right = y1 + base[row][col]
        if left * right <= 0:
            raise AssertionError(
                f"dominant factor crosses zero: row={row}, col={col}, "
                f"range=[{left},{right}]"
            )
        factor_min = min(abs(left), abs(right))
        lead_min_abs = factor_min if lead_min_abs is None else min(lead_min_abs, factor_min)
    if lead_min_abs < Fraction(1, 8):
        raise AssertionError(f"dominant factor can vanish: {lead_min_abs}")

    min_permutation_gap = None
    for permutation in PERMUTATIONS:
        if permutation == lead:
            continue
        endpoint_gaps = (
            square_sum(base, permutation, y0) - square_sum(base, lead, y0),
            square_sum(base, permutation, y1) - square_sum(base, lead, y1),
        )
        # The y^2 terms cancel, so the gap is affine and its minimum is at
        # one of the two endpoints.
        gap = min(endpoint_gaps)
        min_permutation_gap = gap if min_permutation_gap is None else min(min_permutation_gap, gap)
    if min_permutation_gap < Fraction(7, 2):
        raise AssertionError(f"nearest-term assignment gap too small: {min_permutation_gap}")

    # Replacing a centered coefficient c by c +/- 7 changes its square by
    # at least 49 - 14|c|.  More distant translates cost still more.
    min_translate_gap = Fraction(49) - Fraction(14) * max_abs
    if min_translate_gap < Fraction(7, 4):
        raise AssertionError(f"translate gap too small: {min_translate_gap}")
    return max_abs, lead_min_abs, min_permutation_gap, min_translate_gap


def interval_certificate(half):
    y0, y1 = half["interval"]
    base = half["base"]
    lead = half["lead"]
    tail = zak_tail_bound(ZAK_CUTOFF)
    worst_upper = 0.0
    worst_box = None
    worst_interval = None

    for box in range(BOXES_PER_HALF):
        lo = y0 + (y1 - y0) * Fraction(box, BOXES_PER_HALF)
        hi = y0 + (y1 - y0) * Fraction(box + 1, BOXES_PER_HALF)
        lo_iv = fraction_interval(lo)
        hi_iv = fraction_interval(hi)
        y = iv.mpf([lo_iv.a, hi_iv.b])

        entry_sums = [[None] * P for _ in range(P)]
        for row in range(P):
            for col in range(P):
                c = y + fraction_interval(base[row][col])
                magnitude_sum = iv.mpf(0)
                for shift in range(-ZAK_CUTOFF, ZAK_CUTOFF + 1):
                    magnitude_sum += phi(c - Q * shift)
                entry_sums[row][col] = magnitude_sum + tail

        total_absolute_mass = iv.mpf(0)
        for permutation in PERMUTATIONS:
            product = iv.mpf(1)
            for row, col in enumerate(permutation):
                product *= entry_sums[row][col]
            total_absolute_mass += product

        dominant = iv.mpf(1)
        for row, col in enumerate(lead):
            c = y + fraction_interval(base[row][col])
            dominant *= phi(c)

        ratio = total_absolute_mass / dominant
        upper = float(ratio.b)
        if upper > worst_upper:
            worst_upper = upper
            worst_box = (lo, hi)
            worst_interval = ratio

    if not worst_upper < 2.0:
        raise AssertionError(f"dominance failed: upper T/D={worst_upper}")
    return worst_upper, worst_box, worst_interval, tail


def main():
    print("Exact exponent geometry")
    for half in HALVES:
        max_abs, lead_min, perm_gap, translate_gap = exact_geometry_checks(half)
        print(
            f"  {half['name']}: columns={half['columns']}, lead={half['lead']}, "
            f"max|c|={max_abs}, min dominant |c|={lead_min}, "
            f"permutation gap>={perm_gap}, translate gap>={translate_gap}"
        )

    print("Outward-rounded interval dominance at alpha^2=4/7")
    for half in HALVES:
        upper, box, ratio, tail = interval_certificate(half)
        print(
            f"  {half['name']}: worst T/D interval={ratio}; "
            f"upper={upper:.16f}; box=[{box[0]},{box[1]}]"
        )
        print(f"    per-entry omitted-tail bound={tail}")
    print("PASS: T/D < 2 on both halves; every selected determinant is nonzero.")
    print("PASS: positive exact exponent gaps make T/D nonincreasing for alpha>=sqrt(4/7).")


if __name__ == "__main__":
    main()
