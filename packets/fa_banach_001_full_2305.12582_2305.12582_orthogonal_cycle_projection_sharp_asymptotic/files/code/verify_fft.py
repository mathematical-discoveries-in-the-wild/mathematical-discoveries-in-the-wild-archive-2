#!/usr/bin/env python3
"""FFT sanity check for the orthogonal cycle projection on Z_n^2.

This evaluates the exact 2-by-2 Fourier multiplier of the complementary cut
projection.  Floating-point agreement is evidence only and is not used in the
proof.
"""

from fractions import Fraction
import math
import numpy as np


def projection_norm(n: int) -> float:
    theta = 2.0 * math.pi * np.arange(n) / n
    a = np.exp(1j * theta) - 1.0
    a1, a2 = np.meshgrid(a, a, indexing="ij")
    lap = np.abs(a1) ** 2 + np.abs(a2) ** 2
    lap[0, 0] = 1.0

    k11 = np.fft.ifft2(a1 * np.conj(a1) / lap).real
    k21 = np.fft.ifft2(a2 * np.conj(a1) / lap).real

    # A column of P_orth = I-Q: only the diagonal entry changes.
    k11[0, 0] -= 1.0
    return float(np.abs(k11).sum() + np.abs(k21).sum())


def main() -> None:
    expected = {
        3: Fraction(19, 9),
        4: Fraction(41, 16),
        5: Fraction(69, 25),
        6: Fraction(3839, 1260),
    }
    for n in (3, 4, 5, 6, 8, 16, 32, 64, 128, 256, 512):
        value = projection_norm(n)
        residual = value - (4.0 / math.pi) * math.log(n)
        tag = ""
        if n in expected:
            error = abs(value - float(expected[n]))
            assert error < 1e-10, (n, value, expected[n], error)
            tag = f" exact={expected[n]}"
        print(f"n={n:3d} norm={value:.12f} residual={residual:.12f}{tag}")


if __name__ == "__main__":
    main()
