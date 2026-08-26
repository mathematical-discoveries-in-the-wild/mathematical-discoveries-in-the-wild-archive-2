"""Exact rational check for the rectangle counterexample."""

from fractions import Fraction


delta = Fraction(1, 10)


def square_probability(q: Fraction) -> Fraction:
    """Probability of [-q,q]^2 under normalized area on the parallelogram."""
    return q / 4 - delta / 8


mu_a = square_probability(Fraction(1))
mu_ab = Fraction(11, 10) / 4
mu_ac = Fraction(11, 10) / 4
mu_abc = square_probability(Fraction(21, 10))
defect = mu_a * mu_abc - mu_ab * mu_ac

expected = {
    "mu(A)": Fraction(19, 80),
    "mu(A+B)": Fraction(11, 40),
    "mu(A+C)": Fraction(11, 40),
    "mu(A+B+C)": Fraction(41, 80),
    "defect": Fraction(59, 1280),
}
actual = {
    "mu(A)": mu_a,
    "mu(A+B)": mu_ab,
    "mu(A+C)": mu_ac,
    "mu(A+B+C)": mu_abc,
    "defect": defect,
}

assert actual == expected, (actual, expected)
assert defect > 0

for name, value in actual.items():
    print(f"{name} = {value}")
print("exact counterexample check passed")
