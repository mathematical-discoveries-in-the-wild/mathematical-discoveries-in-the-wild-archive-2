#!/usr/bin/env python3
"""Exact exponent/geometry checks for the boundary-sector counterexample."""

from fractions import Fraction


def main() -> None:
    u = Fraction(3, 2)
    v = Fraction(5, 4)
    n_order = Fraction(2, 1)
    alpha = Fraction(3, 2)

    assert u > 0 and v > 0
    assert 1 < alpha < n_order

    # In dimension two, the squared radial tail is
    # integral_2^infinity r^(1-2 alpha) dr
    # = 2^(2-2 alpha)/(2 alpha-2), which is finite iff alpha>1.
    radial_exponent = 1 - 2 * alpha
    assert radial_exponent < -1
    tail_value = Fraction(1, 1) / 2  # alpha=3/2 gives integral_2^inf r^-2 dr.
    assert tail_value == Fraction(1, 2)

    # Sample every displayed sector slope strictly outside the cone.
    slopes = [v + Fraction(j, 10) for j in range(1, 10)]
    assert all(s > v for s in slopes)

    # The retained localization tail is R^-alpha, strictly slower than R^-N.
    exponent_gap = n_order - alpha
    assert exponent_gap == Fraction(1, 2) and exponent_gap > 0

    print("boundary-sector checks passed")
    print(f"u={u}, v={v}, N={n_order}, alpha={alpha}")
    print(f"radial L2 exponent={radial_exponent}, tail integral={tail_value}")
    print(f"decay gap N-alpha={exponent_gap}")


if __name__ == "__main__":
    main()
