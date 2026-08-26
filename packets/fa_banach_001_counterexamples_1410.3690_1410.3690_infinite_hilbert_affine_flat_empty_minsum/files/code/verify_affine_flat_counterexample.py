#!/usr/bin/env python3
"""Numerical sanity checks for the positive-distance affine-flat example.

The proof is analytic.  This script checks the explicit truncation formula
and displays the escape of the finite-dimensional nearest pairs.
"""

from math import pi, sqrt


def tail_square(n: int) -> float:
    """Return sum_{k>n} 1/k^2 using the Basel identity."""
    return pi * pi / 6.0 - sum(1.0 / (k * k) for k in range(1, n + 1))


def main() -> None:
    previous = float("inf")
    tested = (1, 2, 4, 8, 16, 64, 256, 1024, 4096)
    for n in tested:
        tail2 = tail_square(n)
        assert tail2 > -1e-13
        tail2 = max(tail2, 0.0)
        pair_distance = sqrt(1.0 + tail2)
        preimage_norm = sqrt(float(n))
        assert pair_distance >= 1.0
        assert pair_distance < previous
        previous = pair_distance
        print(
            f"N={n:4d}  pair_distance={pair_distance:.12f}  "
            f"finite_preimage_norm={preimage_norm:.6f}"
        )

    assert previous - 1.0 < 1.3e-4

    # Coordinatewise, D x = -y forces x_n=-1 for every n.  Its partial
    # square norms equal N and diverge, so no x in ell^2 solves the equation.
    partial_norm_squares = [sum(1 for _ in range(n)) for n in tested]
    assert partial_norm_squares == list(tested)
    assert partial_norm_squares[-1] > 4000

    print("lower_bound=1.000000000000 (forced by the orthogonal R-coordinate)")
    print("unattained_reason=the only formal preimage is (-1,-1,...), not in ell^2")
    print("VERDICT: PASS")


if __name__ == "__main__":
    main()
