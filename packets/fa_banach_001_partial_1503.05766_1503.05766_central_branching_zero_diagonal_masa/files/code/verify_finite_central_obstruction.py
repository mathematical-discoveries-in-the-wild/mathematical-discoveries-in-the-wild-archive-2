#!/usr/bin/env python3
"""Exhaust the projection ranks in the finite central obstruction model."""

from fractions import Fraction


def pairing(rank: int, scalar_projection: int) -> Fraction:
    """tau((I_2 direct_sum -1)(p direct_sum e)) for rank(p)=rank."""
    return Fraction(rank, 4) - Fraction(scalar_projection, 2)


def main() -> None:
    zeros = []
    for rank in range(3):
        for scalar_projection in range(2):
            value = pairing(rank, scalar_projection)
            print(
                f"rank={rank} e={scalar_projection} pairing={value}"
            )
            if value == 0:
                zeros.append((rank, scalar_projection))

    assert zeros == [(0, 0), (2, 1)]
    print("VERDICT: PASS")
    print("zero-pairing projections occur only at 0 and 1")


if __name__ == "__main__":
    main()
