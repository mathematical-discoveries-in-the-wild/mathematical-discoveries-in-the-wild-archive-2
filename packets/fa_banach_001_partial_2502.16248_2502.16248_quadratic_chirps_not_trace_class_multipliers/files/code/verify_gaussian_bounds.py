#!/usr/bin/env python3
"""Sanity checks for the squeezed-Gaussian chirp bounds.

The packet proof is analytic; this script only reproduces its closed formulas
at high precision and checks the predicted divergence numerically.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def sine_hs_squared(d: int, r: mp.mpf) -> mp.mpf:
    term = mp.power(r - 2j, -mp.mpf(d) / 2) * mp.power(
        1 / r - 2j, -mp.mpf(d) / 2
    )
    return (1 - mp.re(term)) / 2


def oscillatory_modulus(d: int, r: mp.mpf) -> mp.mpf:
    return mp.power((r * r + 4) * (r ** -2 + 4), -mp.mpf(d) / 4)


def main() -> None:
    for d in (1, 2, 3, 4):
        universal = (1 - mp.power(5, -mp.mpf(d) / 2)) / 2
        print(f"dimension={d} universal_HS2_lower={mp.nstr(universal, 18)}")
        for r_text in ("0.1", "1", "10", "100"):
            r = mp.mpf(r_text)
            hs2 = sine_hs_squared(d, r)
            mod = oscillatory_modulus(d, r)
            trace_lower = universal * mp.power(r / 2, mp.mpf(d) / 2)
            product = (r * r + 4) * (r ** -2 + 4)
            assert product >= 25
            assert mod <= mp.power(5, -mp.mpf(d) / 2)
            assert hs2 >= universal
            print(
                "  r=", r_text,
                " HS2=", mp.nstr(hs2, 18),
                " oscillatory_modulus=", mp.nstr(mod, 18),
                " trace_lower=", mp.nstr(trace_lower, 18),
                sep="",
            )

    print("all closed-form checks passed")


if __name__ == "__main__":
    main()

