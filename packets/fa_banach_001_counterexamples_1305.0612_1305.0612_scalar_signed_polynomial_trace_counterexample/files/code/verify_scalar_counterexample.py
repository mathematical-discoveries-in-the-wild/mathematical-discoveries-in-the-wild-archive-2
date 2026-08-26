#!/usr/bin/env python3
"""Exact rational checks for the scalar signed-trace counterexamples."""

from fractions import Fraction


def pos(x: Fraction) -> Fraction:
    return max(x, Fraction(0))


def neg(x: Fraction) -> Fraction:
    return max(-x, Fraction(0))


def sides(a: Fraction, b: Fraction, c: Fraction, q: int, s: Fraction):
    d = a - b
    lhs = c * (a**q - b**q)
    rhs = Fraction(q, 2) * (
        (s * pos(d) ** 2 + s**-1 * pos(c) ** 2) * abs(a) ** (q - 1)
        + (s * neg(d) ** 2 + s**-1 * neg(c) ** 2) * abs(b) ** (q - 1)
    )
    return lhs, rhs


def main() -> None:
    # Fully invertible, odd-power counterexample from the packet.
    lhs, rhs = sides(Fraction(1, 100), Fraction(-1), Fraction(1), 3, Fraction(1))
    assert lhs == Fraction(1_000_001, 1_000_000)
    assert rhs == Fraction(60_603, 200_000_000)
    assert lhs > rhs
    print(f"q=3 invertible example: lhs={lhs} rhs={rhs}")

    # Uniform scalar family: A=0, B=-1, C=(-1)^(q+1), s=q.
    for q in range(2, 31):
        c = Fraction((-1) ** (q + 1))
        lhs, rhs = sides(Fraction(0), Fraction(-1), c, q, Fraction(q))
        assert lhs == 1
        assert rhs == (Fraction(0) if q % 2 else Fraction(1, 2))
        assert lhs > rhs
    print("uniform family q=2,...,30: PASS")
    print("PASS")


if __name__ == "__main__":
    main()
