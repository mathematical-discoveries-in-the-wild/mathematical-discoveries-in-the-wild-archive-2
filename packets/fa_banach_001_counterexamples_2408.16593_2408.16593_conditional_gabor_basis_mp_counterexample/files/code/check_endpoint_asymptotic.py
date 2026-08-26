#!/usr/bin/env python3
"""Finite sanity check for the endpoint Fourier asymptotic.

This is diagnostic only.  The proof in main.tex is analytic.
"""

from __future__ import annotations

import mpmath as mp


def coefficient(delta: mp.mpf, n: int) -> mp.mpc:
    """Fourier coefficient of the two-endpoint model t^-d+(1-t)^-d."""
    f = lambda t: (t ** (-delta) + (1 - t) ** (-delta)) * mp.exp(
        -2j * mp.pi * n * t
    )
    return mp.quad(f, [0, mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), 1])


def predicted_constant(delta: mp.mpf) -> mp.mpf:
    return (
        2
        * mp.gamma(1 - delta)
        * (2 * mp.pi) ** (delta - 1)
        * mp.sin(mp.pi * delta / 2)
    )


def main() -> None:
    mp.mp.dps = 40
    delta = mp.mpf("0.2")
    target = predicted_constant(delta)
    print(f"delta={mp.nstr(delta, 8)}")
    print(f"predicted C_delta={mp.nstr(target, 14)}")
    errors = []
    for n in (10, 25, 50, 100, 200):
        scaled = mp.re(coefficient(delta, n)) * n ** (1 - delta)
        error = abs(scaled - target)
        errors.append(error)
        print(
            f"n={n:3d} scaled={mp.nstr(scaled, 14)} "
            f"abs_error={mp.nstr(error, 8)}"
        )
    assert target > 0
    assert errors[-1] < errors[0]
    assert errors[-1] < mp.mpf("0.01")
    print("PASS: positive constant and convergence at the predicted scale")


if __name__ == "__main__":
    main()
