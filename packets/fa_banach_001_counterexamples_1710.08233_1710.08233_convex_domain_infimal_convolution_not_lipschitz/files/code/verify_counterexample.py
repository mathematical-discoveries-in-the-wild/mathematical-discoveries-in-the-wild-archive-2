#!/usr/bin/env python3
"""Regression checks for the disk-lens infimal-convolution counterexample."""

from decimal import Decimal, getcontext
from fractions import Fraction


def exact_minimax_grid_check() -> int:
    checks = 0
    for ti in range(151):
        t = Fraction(ti, 75)  # 0 <= t <= 2
        target = t * t / 4
        # A wide grid is enough for a regression check; the proof is symbolic.
        for si in range(-400, 601):
            s = Fraction(si, 200)
            lhs = max(s * s, (t - s) * (t - s))
            assert lhs >= target
            checks += 1
        s_eq = t / 2
        assert max(s_eq * s_eq, (t - s_eq) ** 2) == target
    return checks


def quotient_checks() -> None:
    getcontext().prec = 50
    previous_closed = Decimal(0)
    previous_open = Decimal(0)
    print("epsilon       closed quotient       open-interior quotient")
    for exponent in range(1, 8):
        eps = Decimal(10) ** (-exponent)
        closed = (Decimal(1) / eps - Decimal(1) / 4).sqrt()
        # |h(2-eps)-h(2-2eps)| / eps.
        open_q = (
            (2 * eps - eps * eps).sqrt()
            - (eps - eps * eps / 4).sqrt()
        ) / eps
        assert closed > previous_closed
        assert open_q > previous_open
        previous_closed = closed
        previous_open = open_q
        print(f"1e-{exponent:<2d}        {closed:>18.10f}    {open_q:>18.10f}")


def main() -> None:
    checks = exact_minimax_grid_check()
    print(f"exact scalar minimax inequalities passed: {checks}")
    quotient_checks()
    print("all disk-lens counterexample checks passed")


if __name__ == "__main__":
    main()

