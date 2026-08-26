"""High-precision regression check for the exact hexagonal Zak zeros.

This script is not part of the proof.  It evaluates the generalized first
Hermite Zak series, its real Jacobian, and the Gaussian Zak-norm symmetry.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 80

SQRT3 = mp.sqrt(3)
A = mp.sqrt(2 / SQRT3)
S = mp.mpf(1) / 2
Q = 1 / A**2 - 1j * S
K = 70


def zak_h1(x: mp.mpf, omega: mp.mpf) -> mp.mpc:
    """Zak series with the irrelevant nonzero normalization omitted."""
    return mp.fsum(
        [
            ((k - x) / A)
            * mp.exp(-mp.pi * ((k - x) / A) ** 2)
            * mp.exp(1j * mp.pi * S * (k - x) ** 2)
            * mp.exp(2j * mp.pi * k * omega)
            for k in range(-K, K + 1)
        ]
    )


def zak_gaussian(x: mp.mpf, omega: mp.mpf) -> mp.mpc:
    return mp.fsum(
        [
            mp.exp(-mp.pi * Q * (k - x) ** 2)
            * mp.exp(2j * mp.pi * k * omega)
            for k in range(-K, K + 1)
        ]
    )


def jacobian_det(x: mp.mpf, omega: mp.mpf) -> mp.mpf:
    fx = mp.diff(lambda xx: zak_h1(xx, omega), x)
    fw = mp.diff(lambda ww: zak_h1(x, ww), omega)
    return mp.re(fx) * mp.im(fw) - mp.im(fx) * mp.re(fw)


def affine_symmetry(x: mp.mpf, omega: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    return ((x - omega + mp.mpf(1) / 2) % 1, x % 1)


def main() -> None:
    points = [
        (mp.mpf(0), mp.mpf(0)),
        (mp.mpf(1) / 2, mp.mpf(0)),
        (mp.mpf(0), mp.mpf(1) / 2),
        (mp.mpf(1) / 6, mp.mpf(5) / 6),
        (mp.mpf(5) / 6, mp.mpf(1) / 6),
    ]
    print(f"a = {mp.nstr(A, 30)}, s = 1/2")
    for point in points:
        value = zak_h1(*point)
        determinant = jacobian_det(*point)
        print(
            point,
            "|Z h1| =",
            mp.nstr(abs(value), 8),
            "Jacobian det =",
            mp.nstr(determinant, 20),
        )

    samples = [
        (mp.mpf("0.12"), mp.mpf("0.34")),
        (mp.mpf("0.7"), mp.mpf("0.2")),
        (mp.mpf("0.1"), mp.mpf("0.9")),
    ]
    for point in samples:
        image = affine_symmetry(*point)
        error = abs(
            abs(zak_gaussian(*point)) ** 2
            - abs(zak_gaussian(*image)) ** 2
        )
        print("symmetry", point, "->", image, "error =", mp.nstr(error, 8))


if __name__ == "__main__":
    main()

