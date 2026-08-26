#!/usr/bin/env python3
"""Exact checks for the all-order boundary-square identity.

This is supporting verification, not a substitute for the symbolic proof in
the packet.  The default range is deliberately modest because all
coefficients are exact rationals and grow quickly.
"""

from __future__ import annotations

import argparse
import sympy as sp


def jacobi_square_coefficients(m: int, u: sp.Symbol) -> list[sp.Integer]:
    p = sum(
        (-1) ** j
        * sp.binomial(m, j)
        * sp.binomial(m + j + 1, j)
        * u**j
        for j in range(m + 1)
    )
    poly = sp.Poly(sp.expand(p**2), u)
    return [poly.nth(k) for k in range(2 * m + 1)]


def spectral_polynomial(m: int, s: sp.Symbol, u: sp.Symbol) -> sp.Expr:
    b = jacobi_square_coefficients(m, u)
    return sp.expand(
        sum(
            b[k] * sp.rf(1 + s, k) * sp.rf(2 - s, k) / sp.rf(2, k) ** 2
            for k in range(2 * m + 1)
        )
    )


def cdh_monic(d: int, q: sp.Symbol) -> sp.Expr:
    if d == 0:
        return sp.Integer(1)
    c0 = sp.Integer(1)
    c1 = q - 4
    if d == 1:
        return c1
    for j in range(2, d + 1):
        c0, c1 = c1, sp.expand(
            (q - 2 * j * (j + 1)) * c1 - j**2 * (j**2 - 1) * c0
        )
    return c1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=12)
    args = parser.parse_args()

    s, u, q = sp.symbols("s u q")
    previous = sp.Integer(1)
    for m in range(1, args.max_m + 1):
        current = spectral_polynomial(m, s, u)
        delta = sp.expand(current - previous)
        lhs = sp.expand((delta + delta.subs(s, -s)) / 2)
        c = cdh_monic(m - 1, q)
        rhs = sp.expand(
            s**2
            * (s**2 - 1)
            * c.subs(q, s * (1 - s))
            * c.subs(q, -s * (1 + s))
            / (sp.factorial(m) * sp.factorial(m + 1)) ** 2
        )
        residual = sp.Poly(sp.together(lhs - rhs), s)
        assert residual.is_zero, (m, residual.as_expr())
        assert sp.expand(current.subs(s, 1 - s) - current) == 0
        print(f"m={m:2d} exact identity and symmetry: PASS")
        previous = current


if __name__ == "__main__":
    main()
