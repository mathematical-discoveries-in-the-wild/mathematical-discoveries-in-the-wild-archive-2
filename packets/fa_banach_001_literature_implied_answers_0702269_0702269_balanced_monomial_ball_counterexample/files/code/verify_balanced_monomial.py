"""Exact arithmetic sanity check for the balanced-monomial counterexamples."""

from fractions import Fraction


def main() -> None:
    for dimension in range(2, 21):
        # Compare squares to avoid floating point:
        # derivative^2 = d^d, source_bound^2 = d^(d-1).
        derivative_sq = dimension**dimension
        source_sq = dimension ** (dimension - 1)
        ratio_sq = Fraction(derivative_sq, source_sq)
        assert ratio_sq == dimension
        assert derivative_sq > source_sq
        print(dimension, "ratio_squared", ratio_sq)


if __name__ == "__main__":
    main()

