#!/usr/bin/env python3
"""Exhaustive guards for the finite complementary-spectrum theorem.

The proof is symbolic.  This script enumerates all normalized odd-head spectra
in several small mixed-radix quotients and checks direct tiling by the negative
canonical even-head spectrum.
"""

from itertools import combinations, product
from math import comb


def products(radices):
    out = []
    value = 1
    for radix in radices:
        value *= radix
        out.append(value)
    return out


def layer(value, mod, radices):
    """Return the first mixed-radix layer of a nonzero residue."""
    value %= mod
    if value == 0:
        return None
    divisor = 1
    for index, radix in enumerate(radices, start=1):
        if value % (divisor * radix):
            return index
        divisor *= radix
    raise AssertionError("nonzero residue had no layer")


def canonical_even(radices):
    ps = products(radices)
    modulus = ps[-1]
    digit_sets = []
    for index in range(2, len(radices) + 1, 2):
        place = ps[index - 2]
        digit_sets.append([place * digit for digit in range(radices[index - 1])])
    return {(-sum(digits)) % modulus for digits in product(*digit_sets)}


def check_case(radices, exhaustive_limit=2_000_000):
    assert len(radices) % 2 == 0
    ps = products(radices)
    modulus = ps[-1]
    odd_size = 1
    for index in range(0, len(radices), 2):
        odd_size *= radices[index]
    cases = comb(modulus - 1, odd_size - 1)
    if cases > exhaustive_limit:
        raise ValueError(f"case {radices} requires {cases} candidates")

    even = canonical_even(radices)
    expected_even = modulus // odd_size
    assert len(even) == expected_even

    spectra = 0
    for tail in combinations(range(1, modulus), odd_size - 1):
        odd = (0,) + tail
        differences = (a - b for a, b in combinations(odd, 2))
        if not all(layer(d, modulus, radices) % 2 == 1 for d in differences):
            continue
        spectra += 1
        sums = {(a + b) % modulus for a in odd for b in even}
        assert len(sums) == modulus, (radices, odd, sorted(even))
    assert spectra > 0
    return spectra


def main():
    cases = ([2, 2, 2, 2], [2, 3, 2, 2], [2, 2, 3, 2], [3, 2, 2, 2])
    total = 0
    for radices in cases:
        spectra = check_case(radices)
        total += spectra
        print(f"radices={radices}: checked {spectra} normalized spectra")
    print(f"PASS: {total} finite spectra, no tiling failure")


if __name__ == "__main__":
    main()
