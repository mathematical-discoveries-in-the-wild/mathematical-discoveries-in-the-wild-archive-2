#!/usr/bin/env python3
"""Exact sanity checks for the lacunary-gap proof.

This does not replace the symbolic proof in main.tex.  It checks the residue
classes, integer endpoints, margin implication, and exact endpoint ratios on
representative finite ranges using only integer/Fraction arithmetic.
"""

from fractions import Fraction


def selected(j: int) -> bool:
    return j % 5 in (0, 2)


def check_margin(d: int, p: int, max_s: int = 20) -> None:
    for s in range(1, max_s + 1):
        margin = 2 ** (s + 1 + p)
        support_radius = 2**s + d
        assert margin >= 2 ** (s + 1) + 2 * d + 1
        assert margin > support_radius


def main() -> None:
    # Representative d and a p satisfying the source's uniform inequality.
    d = 17
    p = 5
    check_margin(d, p)

    ratios = []
    for q in range(1, 13):
        assert not selected(5 * q + 3)
        assert not selected(5 * q + 4)
        left = 2 ** (5 * q + 3)
        middle = 2 ** (5 * q + 4)
        right = 2 ** (5 * q + 5)
        n_q = left - 1
        m_q = right - 1
        assert middle == 2 * left
        assert right == 2 * middle == 4 * left
        ratios.append(Fraction(n_q, m_q))

    errors = [abs(ratio - Fraction(1, 4)) for ratio in ratios]
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    print("residue and integer-endpoint checks: PASS")
    print("margin-to-support containment checks: PASS")
    print("last exact N_q/M_q ratio:", ratios[-1])
    print("last exact error from 1/4:", errors[-1])


if __name__ == "__main__":
    main()
