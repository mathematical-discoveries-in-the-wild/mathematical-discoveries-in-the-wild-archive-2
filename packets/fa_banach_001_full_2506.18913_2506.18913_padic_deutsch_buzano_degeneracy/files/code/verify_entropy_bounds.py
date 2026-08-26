#!/usr/bin/env python3
"""Exact arithmetic audit for the Q_p entropy and Buzano examples."""

from fractions import Fraction


def entropy_logp_coefficient(p: int, valuation: int) -> Fraction:
    """Return c with -|a|_p^2 log(|a|_p^2) = c log(p)."""
    if valuation == 0:
        return Fraction(0)
    return Fraction(2 * valuation, p ** (2 * valuation))


def vp(integer: int, p: int) -> int:
    if integer == 0:
        return 10**9
    integer = abs(integer)
    exponent = 0
    while integer % p == 0:
        exponent += 1
        integer //= p
    return exponent


def padic_abs(integer: int, p: int) -> Fraction:
    exponent = vp(integer, p)
    return Fraction(0) if exponent == 10**9 else Fraction(1, p**exponent)


def sup_norm(vector: tuple[int, ...], p: int) -> Fraction:
    return max(padic_abs(entry, p) for entry in vector)


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def main() -> None:
    # The nonzero Q_p values at most one are p^{-m}.  Their entropy
    # coefficients decrease strictly after m=1.
    for p in (2, 3, 5, 7, 11):
        coefficients = [entropy_logp_coefficient(p, m) for m in range(1, 9)]
        assert coefficients[0] == Fraction(2, p * p)
        assert all(a > b for a, b in zip(coefficients, coefficients[1:]))

    # Q_2^8, equal canonical bases, x=(1,2,...,2): the entropy sum is
    # 7 log 2, whereas Deutsch's classical upper bound is 6 log 2.
    n = 8
    entropy_sum_log2 = 2 * (n - 1) * entropy_logp_coefficient(2, 1)
    deutsch_upper_log2 = 2 * 3
    assert entropy_sum_log2 == 7
    assert entropy_sum_log2 > deutsch_upper_log2

    # Orthogonal Buzano obstruction over every Q_p:
    # tau=e1, omega=e2, h=e1+e2 has both factors and all norms equal to one.
    tau, omega, h = (1, 0), (0, 1), (1, 1)
    for p in (2, 3, 5, 7):
        assert dot(tau, omega) == 0
        lhs = padic_abs(dot(tau, h), p) * padic_abs(dot(h, omega), p)
        rhs = sup_norm(tau, p) * sup_norm(h, p) ** 2 * sup_norm(omega, p)
        assert lhs == rhs == 1

    print("Q_p entropy coefficient is maximized at valuation one")
    print("Q_2^8 entropy sum / log(2):", entropy_sum_log2)
    print("classical upper bound / log(2):", deutsch_upper_log2)
    print("orthogonal Buzano example attains the product bound")
    print("all exact checks passed")


if __name__ == "__main__":
    main()
