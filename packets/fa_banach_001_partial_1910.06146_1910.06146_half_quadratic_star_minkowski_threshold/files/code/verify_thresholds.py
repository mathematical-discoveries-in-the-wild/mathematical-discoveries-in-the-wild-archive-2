#!/usr/bin/env python3
"""Exact-integer checks for the sharpened star-shaped Minkowski threshold.

This script is a regression/sanity check.  The uniform threshold is proved
analytically in the accompanying packet.
"""

from math import comb


def delta(d: int, k: int) -> int:
    """Numerator of 1-alpha_{d,k}."""
    return (k - d + 2) * (k + 1) ** (d - 1) - k**d


def exact_cutoff(d: int) -> int:
    k = d - 1
    while delta(d, k) <= 0:
        k += 1
    return k


def main() -> None:
    expected = {
        3: 2,
        4: 5,
        5: 8,
        6: 13,
        7: 19,
        8: 25,
        9: 33,
        10: 42,
        11: 51,
        12: 62,
    }
    observed = {d: exact_cutoff(d) for d in expected}
    assert observed == expected, (observed, expected)

    # Closed-form theorem: strict positivity at k=binom(d,2)-1.
    for d in range(3, 1001):
        k = comb(d, 2) - 1
        assert k >= d - 1
        assert delta(d, k) > 0, (d, k, delta(d, k))

    # Exact integer cross-multiplication of
    # (1-1/x)^d < 1-(d-1)/x, with x=k+1.
    for d in range(3, 201):
        cutoff = exact_cutoff(d)
        for k in range(d - 1, cutoff + 8):
            x = k + 1
            normalized_numerator = x**d - (d - 1) * x ** (d - 1) - (x - 1) ** d
            assert delta(d, k) == normalized_numerator

    print("exact cutoffs d=3..12:", observed)
    print("closed-form strict positivity verified for d=3..1000")
    print("normalized-form equivalence verified for d=3..200")


if __name__ == "__main__":
    main()
