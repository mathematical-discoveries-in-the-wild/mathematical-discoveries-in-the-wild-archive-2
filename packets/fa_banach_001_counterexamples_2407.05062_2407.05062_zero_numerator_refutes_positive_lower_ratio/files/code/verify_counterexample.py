"""Exact scalar audit for the counterexample to Remark 2 of arXiv:2407.05062."""

from fractions import Fraction


def phi(value: Fraction) -> Fraction:
    """The source-admissible polynomial map X |-> X^2-X^3."""
    return value**2 - value**3


f_of_a = Fraction(1)
numerator = phi(f_of_a)
assert numerator == 0

alpha_2 = Fraction(1)
for denominator in (Fraction(-7), Fraction(-1, 3), Fraction(1, 5), Fraction(11)):
    assert denominator != 0
    ratio = numerator / denominator
    assert ratio == 0
    assert not (ratio >= alpha_2)

# The k=1 averaged expression has the same numerator.
weight = Fraction(1)
averaged_numerator = weight * numerator
assert averaged_numerator == 0

print("PASS: every tested nonzero denominator gives ratio 0 < alpha_2=1")
