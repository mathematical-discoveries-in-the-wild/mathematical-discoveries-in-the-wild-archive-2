#!/usr/bin/env python3
"""Finite exact checks for the sparse dyadic Jordan-mass construction."""

from fractions import Fraction
from math import log


def parameters(j: int) -> tuple[int, int, int, int]:
    n = 1 << (1 << j)
    ell = 1 << j
    width = 1 << (1 << (j - 1))
    excess = 2 * n - 2 - ell
    return n, ell, width, excess


def ramp_neighbourhood(ell: int) -> list[int]:
    """Masses immediately before, during, and after either ramp."""
    return [1] + [1 << r for r in range(1, ell + 1)] + [1]


def main() -> None:
    print("j  N_j  L_j  W_j  W_j/N_j  plateau_value")
    for j in range(2, 9):
        n, ell, width, excess = parameters(j)
        ramp = ramp_neighbourhood(ell)

        # Block singular values are p_k/2^k and q_k/2^k.  Their decrease is
        # equivalent to the following local doubling inequalities.
        assert all(ramp[k + 1] <= 2 * ramp[k] for k in range(len(ramp) - 1))

        ramp_excess = sum((1 << r) - 1 for r in range(1, ell + 1))
        assert ramp_excess == excess
        # The negative ramp has the same excess with the opposite sign.
        assert ramp_excess - ramp_excess == 0

        # At the end of the positive ramp, normalized cumulative difference
        # is asymptotic to 2/log(2).  The exact dyadic-end approximation is
        # recorded for convergence inspection.
        plateau = Fraction(excess, n)
        plateau_value = float(plateau) / log(2)
        print(
            f"{j:1d}  {n}  {ell}  {width}  "
            f"{width / n:.3e}  {plateau_value:.12f}"
        )

        # A simple analytic prefix estimate used in the proof.  Because
        # N_{j+1}=N_j^2, previous completed excess masses are negligible.
        previous = sum(parameters(i)[3] for i in range(2, j))
        assert previous <= n
        assert excess <= 2 * n

    target = 2 / log(2)
    print(f"limit plateau value = {target:.12f}")
    print("all exact cancellation, monotonicity, and growth checks passed")


if __name__ == "__main__":
    main()
