#!/usr/bin/env python3
"""Regression checks for the exterior-ball radial weighted p-harmonic flux.

This is not the proof.  It checks the exponent branches and the identity
    (r-R)^(-alpha) r^(N-1) |u'|^(p-2) u' = +/- 1
for a grid of representative parameters and radii.
"""

from __future__ import annotations


def q(N: int, p: float, alpha: float, R: float, r: float) -> float:
    return (r - R) ** (alpha / (p - 1.0)) * r ** (-(N - 1.0) / (p - 1.0))


def flux(N: int, p: float, alpha: float, R: float, r: float, sign: int) -> float:
    derivative = sign * q(N, p, alpha, R, r)
    return (
        (r - R) ** (-alpha)
        * r ** (N - 1.0)
        * abs(derivative) ** (p - 2.0)
        * derivative
    )


def main() -> None:
    checked = 0
    for N in (2, 3, 7):
        for p in (1.2, 2.0, 4.5):
            alphas = (
                1.0 - p,
                N - p,
                -7.0,
                0.25,
                8.0,
            )
            for alpha in alphas:
                if alpha > 1.0 - p:
                    # Boundary primitive: exponent must be > -1.
                    assert alpha / (p - 1.0) > -1.0
                    sign = 1
                else:
                    # Tail primitive: infinity exponent must be < -1.
                    infinity_exponent = (alpha - (N - 1.0)) / (p - 1.0)
                    assert infinity_exponent < -1.0
                    sign = -1
                for R in (0.3, 1.0, 4.0):
                    for multiple in (1.0001, 1.01, 1.5, 3.0, 100.0):
                        r = R * multiple
                        value = flux(N, p, alpha, R, r, sign)
                        assert abs(value - sign) < 2.0e-10, (
                            N,
                            p,
                            alpha,
                            R,
                            r,
                            value,
                        )
                        checked += 1
    print(f"PASS: {checked} radial flux identities and branch checks")


if __name__ == "__main__":
    main()

