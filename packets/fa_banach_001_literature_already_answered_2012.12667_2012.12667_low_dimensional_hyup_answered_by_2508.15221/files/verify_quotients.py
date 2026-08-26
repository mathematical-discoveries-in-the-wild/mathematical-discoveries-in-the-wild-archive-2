"""Exact quotient check for u(x)=x_1 exp(-|x|)."""

from fractions import Fraction
from math import factorial


def gamma_integer(n: int) -> int:
    """Gamma(n) for a positive integer n."""
    return factorial(n - 1)


def quotient(n: int) -> Fraction:
    a = Fraction(gamma_integer(n + 2), 2 ** (n + 2))
    a += Fraction((n + 1) * gamma_integer(n), 2**n)
    b = Fraction(gamma_integer(n + 2), 2 ** (n + 2))
    c = Fraction(gamma_integer(n + 1), 2 ** (n + 1))
    c += Fraction(gamma_integer(n - 1), 2 ** (n - 1))
    return a * b / (c * c)


expected = {2: Fraction(3, 4), 3: Fraction(84, 25), 4: Fraction(225, 32)}
for dimension, value in expected.items():
    actual = quotient(dimension)
    target = Fraction((dimension + 1) ** 2, 4)
    assert actual == value
    relation = "<" if actual < target else ">="
    print(f"N={dimension}: Q={actual} {relation} target={target}")
