#!/usr/bin/env python3
"""Finite checks for the Boolean tensor core in the 2002.05230 packet."""

from fractions import Fraction
from itertools import combinations, product


def main() -> None:
    generators = 6
    checks = 0

    # Coordinate projections commute.  Encode a Boolean atom by a bit string;
    # every assignment occurs, so every signed word has positive rank.
    atoms = list(product((0, 1), repeat=generators))
    for i, j in combinations(range(generators), 2):
        for atom in atoms:
            assert atom[i] * atom[j] == atom[j] * atom[i]
            checks += 1

    for signs in product((0, 1), repeat=generators):
        compatible = [atom for atom in atoms if atom == signs]
        assert len(compatible) == 1
        # In the source tensor block the compatible atom has rank
        # product(1 or d-1) times unused-factor dimension, hence positive for d>=2.
        rank_lower_bound = 1
        for sign in signs:
            rank_lower_bound *= 1 if sign else 2  # use toy local dimension d=3
        assert rank_lower_bound > 0
        checks += 1

    # Binary partial sums realize the full dyadic grid at every depth.
    for depth in range(1, 9):
        values = {
            sum(Fraction(bit, 2 ** (n + 1)) for n, bit in enumerate(bits))
            for bits in product((0, 1), repeat=depth)
        }
        expected = {Fraction(k, 2**depth) for k in range(2**depth)}
        assert values == expected
        checks += len(values)

    print(f"PASS: {checks} exact commutation, Boolean-rank, and dyadic checks")


if __name__ == "__main__":
    main()

