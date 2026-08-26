#!/usr/bin/env python3
"""Exact rational audit of exponent identities in the crude-atom reduction."""

from fractions import Fraction


def main() -> None:
    checks = 0
    pairs = 0
    for p_num in range(1, 100):
        p = Fraction(p_num, 100)
        for q_num in range(201, 401, 2):
            q = Fraction(q_num, 100)
            inv_u = 1 / p - 1
            inv_s = 1 / p - Fraction(1, 2)
            inv_v = Fraction(1, 2) * (1 / p - 1 / q)
            gap = Fraction(1 - p, 2 * p) + Fraction(1, 2 * q)

            assert inv_s - inv_v == gap
            assert gap > 0
            assert inv_v < inv_s  # v > s, hence L_v embeds in L_s.
            assert Fraction(1, 2) + inv_s == 1 / p
            assert inv_v == Fraction(1, 2) * (inv_u + 1 - 1 / q)

            # Atom normalization cancellations used in the two directions.
            assert (1 - 1 / p) + Fraction(1, 2) - 1 == Fraction(1, 2) - 1 / p
            assert -1 / q + (1 / q - 1 / p) == -1 / p

            checks += 7
            pairs += 1

    print(f"passed {checks:,} exact checks on {pairs:,} admissible (p,q) pairs")


if __name__ == "__main__":
    main()

