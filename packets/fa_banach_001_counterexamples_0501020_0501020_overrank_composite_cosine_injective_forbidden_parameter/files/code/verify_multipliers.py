#!/usr/bin/env python3
"""Numerically compare the Legendre integrals with their exact formula."""

import mpmath as mp


def main() -> None:
    mp.mp.dps = 70
    a = mp.mpf("0.5")
    base = mp.beta(mp.mpf("0.5"), a + 1)
    worst = mp.mpf("0")
    for k in range(9):
        numerical = mp.quad(
            lambda t: (1 - t * t) ** a * mp.legendre(2 * k, t),
            [-1, 0, 1],
        )
        closed = (
            base
            * mp.rf(-a, k)
            * mp.rf(mp.mpf("0.5"), k)
            / (mp.factorial(k) * mp.rf(a + mp.mpf("1.5"), k))
        )
        error = abs(numerical - closed)
        worst = max(worst, error)
        if closed == 0:
            raise AssertionError(f"unexpected zero multiplier at k={k}")
        print(f"k={k:2d} integral={mp.nstr(numerical, 24)} error={mp.nstr(error, 4)}")
    print(f"worst absolute error: {mp.nstr(worst, 6)}")
    if worst > mp.mpf("1e-50"):
        raise AssertionError("quadrature/formula mismatch")


if __name__ == "__main__":
    main()
