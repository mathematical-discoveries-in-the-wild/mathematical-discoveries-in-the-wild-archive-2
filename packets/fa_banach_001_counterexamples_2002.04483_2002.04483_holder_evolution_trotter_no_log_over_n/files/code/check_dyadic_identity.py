"""Numerical checks for the dyadic Holder Trotter counterexample.

The proof is analytic.  This script checks the exact dyadic quadrature
identity for finite truncations and the resulting semigroup lower bound.
"""

from __future__ import annotations

import math


def tent(x: float) -> float:
    return abs(x - round(x))


def q_truncated(x: float, beta: float, levels: int) -> float:
    return sum(2.0 ** (-m * beta) * tent((2**m) * x) for m in range(levels))


def exact_integral(beta: float, levels: int) -> float:
    return 0.25 * sum(2.0 ** (-m * beta) for m in range(levels))


def left_sum(beta: float, levels: int, grid_power: int) -> float:
    n = 2**grid_power
    return sum(q_truncated(k / n, beta, levels) for k in range(n)) / n


def expected_error(beta: float, levels: int, grid_power: int) -> float:
    return 0.25 * sum(
        2.0 ** (-m * beta) for m in range(grid_power, levels)
    )


def main() -> None:
    beta = 0.63
    levels = 30
    q_integral = exact_integral(beta, levels)
    for grid_power in range(1, 13):
        n = 2**grid_power
        rsum = left_sum(beta, levels, grid_power)
        error = q_integral - rsum
        target = expected_error(beta, levels, grid_power)
        assert math.isclose(error, target, rel_tol=2e-11, abs_tol=2e-12)

        split_error = math.exp(-1.0 - rsum) - math.exp(-1.0 - q_integral)
        lower_bound = math.exp(-1.0 - q_integral) * error
        assert split_error >= lower_bound * (1.0 - 1e-12)

        print(
            f"n={n:5d} quadrature_error={error:.10e} "
            f"n^beta*error={n**beta * error:.10e} "
            f"split_error/(log(n)/n)={split_error / (math.log(n) / n):.6e}"
        )


if __name__ == "__main__":
    main()
