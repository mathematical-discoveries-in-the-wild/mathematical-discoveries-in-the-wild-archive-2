"""High-precision sanity checks for the affine-lognormal construction.

These checks are not used by the proof.  The proof obtains a nonzero Cauchy
pairing from injectivity of the Cauchy transform and does not depend on the
sample point z=-i tested here.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80
SQRT_TWO_PI = mp.sqrt(2 * mp.pi)


def normal_density(y: mp.mpf) -> mp.mpf:
    return mp.exp(-(y * y) / 2) / SQRT_TWO_PI


def closed_moment(n: int) -> mp.mpf:
    """Imaginary part of E exp((n+2*pi*i)Y), which is exactly zero."""

    return mp.im(mp.exp((mp.mpf(n) + 2j * mp.pi) ** 2 / 2))


def cauchy_at_minus_i() -> mp.mpc:
    """Numerically evaluate F(-i) after x=exp(y)."""

    def integrand(y: mp.mpf) -> mp.mpc:
        return (
            mp.sin(2 * mp.pi * y)
            * normal_density(y)
            / (mp.exp(y) + 1j)
        )

    return mp.quad(integrand, [-mp.inf, -8, -3, 0, 3, 8, mp.inf])


def main() -> None:
    print("closed-form lognormal moment residuals")
    for n in range(9):
        print(f"n={n}: {mp.nstr(closed_moment(n), 12)}")

    value = cauchy_at_minus_i()
    print("F(-i) numerical sample:", mp.nstr(value, 40))
    print("i*F(-i), the unshifted resolvent pairing:", mp.nstr(1j * value, 40))


if __name__ == "__main__":
    main()

