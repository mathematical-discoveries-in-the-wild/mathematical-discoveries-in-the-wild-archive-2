#!/usr/bin/env python3
"""Exact-rational checks for the two endpoint calculations."""

from fractions import Fraction


def q_value(m: int, t: int) -> Fraction:
    return Fraction(
        t * ((m - 3) ** 2 - (m - 5) * t),
        (t + m - 3) ** 2,
    )


def check(m: int, d: int) -> None:
    values = [(q_value(m, t), t) for t in range(1, m - 2)]
    qmax = max(q for q, _ in values)
    equality = [t for q, t in values if q == qmax]
    rank_bound = Fraction(m, 1 + qmax)
    print(f"m={m}, k={m-2}, qmax={qmax}, equality_t={equality}")
    print(f"rank lower bound={rank_bound}, target d={d}")
    assert rank_bound == d

    for t in equality:
        a = Fraction(m - 3 - t, t + m - 3)
        b = Fraction(-t, t + m - 3)
        row_sum = 1 + t * a + (m - 1 - t) * b
        print(f"  t={t}: a={a}, b={b}, row_sum={row_sum}")


if __name__ == "__main__":
    check(18, 6)
    check(42, 7)
