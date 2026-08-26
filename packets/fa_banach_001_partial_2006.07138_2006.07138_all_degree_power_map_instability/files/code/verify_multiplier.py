#!/usr/bin/env python3
"""High-precision regression checks for the all-degree multiplier identity.

This script is evidence against algebraic/transcription errors, not a proof.
The packet proof uses the exact cosecant root-sum and beta-integral identities.
"""

import mpmath as mp


mp.mp.dps = 50


def closed_q1(p: mp.mpf) -> mp.mpf:
    return (
        (8 - p)
        * mp.power(2, p + 1)
        * mp.power(mp.pi, mp.mpf("1.5"))
        * mp.gamma((1 + p) / 2)
        / mp.gamma(3 + p / 2)
    )


def quadratic_form(p: mp.mpf, q: int) -> mp.mpf:
    """Return Q_{p,q}(cos(3q theta)) by direct one-dimensional quadrature."""

    def integrand(t: mp.mpf) -> mp.mpf:
        denominator = 4 * mp.sin(t / 2) ** 2
        if abs(denominator) < mp.mpf("1e-45"):
            return mp.mpf(0)
        target_factor = abs(2 * mp.sin(q * t / 2)) ** (p - 2)
        kernel = (
            target_factor
            * (p * mp.cos(q * t / 2) ** 2 - 1)
            / denominator
        )
        return 2 * mp.pi * kernel * (1 - mp.cos(3 * q * t))

    cuts = [2 * mp.pi * j / q for j in range(q + 1)]
    return mp.fsum(mp.quad(integrand, [cuts[j], cuts[j + 1]]) for j in range(q))


def check_root_sum(q: int, x: mp.mpf) -> None:
    lhs = mp.fsum(
        1 / mp.sin((x + 2 * mp.pi * j) / (2 * q)) ** 2 for j in range(q)
    )
    rhs = q**2 / mp.sin(x / 2) ** 2
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-45"))


def main() -> None:
    for q in (1, 2, 3, 5):
        check_root_sum(q, mp.mpf("0.731"))

    for p_integer in (9, 10, 12):
        p = mp.mpf(p_integer)
        q1 = closed_q1(p)
        assert q1 < 0
        for q in (1, 2, 3, 5):
            numerical = quadratic_form(p, q)
            expected = q * q1
            error = abs(numerical - expected)
            assert mp.almosteq(numerical, expected, rel_eps=mp.mpf("1e-40"))
            print(
                f"p={p_integer:2d} q={q:2d} "
                f"Q={mp.nstr(numerical, 18)} error={mp.nstr(error, 5)}"
            )

    print("all multiplier checks passed")


if __name__ == "__main__":
    main()

