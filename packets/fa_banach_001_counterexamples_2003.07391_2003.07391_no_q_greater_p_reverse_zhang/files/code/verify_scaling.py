#!/usr/bin/env python3
"""Check the exponent identity behind the anisotropic counterexample."""

from fractions import Fraction


CASES = [
    (2, 1, 2),
    (3, 2, 5 / 2),
    (5, 2, 4),
    (7, 7, 8),
]


def exponent(n: int, p: float, q: float) -> float:
    affine = 1 / p - 1 / n
    rhs = (n - 1) / (n * q) + (1 / p - 1) / n
    return affine - rhs


def main() -> None:
    # Exact symbolic simplification using rational placeholders.
    n, p, q = Fraction(11), Fraction(5), Fraction(7)
    direct = 1 / p - 1 / n - (n - 1) / (n * q) - (1 / p - 1) / n
    expected = (n - 1) / n * (1 / p - 1 / q)
    assert direct == expected

    for n_i, p_i, q_i in CASES:
        value = exponent(n_i, p_i, q_i)
        assert value > 0
        print(f"n={n_i}, p={p_i}, q={q_i}: decay exponent={value:.12g}")


if __name__ == "__main__":
    main()

