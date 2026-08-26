#!/usr/bin/env python3
"""Check the numerical margins in the dual-(ddagger) reflexivity proof."""

from fractions import Fraction


def margins(eta: Fraction, tau: Fraction, error: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return scaling constant, separation lower bound, limit lower bound."""
    scale_denominator = 1 + tau + error
    separation = (2 * (1 - eta) - 2 * error) / scale_denominator
    limit_norm = (1 - eta - tau) / scale_denominator
    return scale_denominator, separation, limit_norm


def main() -> None:
    eta = tau = error = Fraction(1, 10)
    denominator, separation, limit_norm = margins(eta, tau, error)
    ddagger_upper = 1 - separation / 2

    assert denominator == Fraction(6, 5)
    assert separation == Fraction(4, 3)
    assert limit_norm == Fraction(2, 3)
    assert ddagger_upper == Fraction(1, 3)
    assert limit_norm > ddagger_upper

    # The proof uses strict approximation inequalities, so the two displayed
    # lower bounds are strict in the needed direction.
    print(f"common norm bound: {denominator}")
    print(f"separation lower bound: {separation}")
    print(f"limit norm lower bound: {limit_norm}")
    print(f"(ddagger) upper bound: {ddagger_upper}")
    print(f"contradiction margin: {limit_norm - ddagger_upper}")


if __name__ == "__main__":
    main()
