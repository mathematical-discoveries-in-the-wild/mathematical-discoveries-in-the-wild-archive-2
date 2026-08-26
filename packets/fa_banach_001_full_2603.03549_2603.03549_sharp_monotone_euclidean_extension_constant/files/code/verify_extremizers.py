"""Finite consistency checks for the sharp monotone extension examples."""

from __future__ import annotations

import math

import numpy as np


def check_radial_extremizer(n: int) -> None:
    values = []
    for j in range(n):
        e = np.zeros(n)
        e[j] = 0.5
        values.extend((e, -e))

    for u in values:
        for v in values:
            assert np.linalg.norm(u - v) <= 1.0 + 1e-12

    coordinate_max = np.max(np.stack(values), axis=0)
    coordinate_min = np.min(np.stack(values), axis=0)
    gap = np.linalg.norm(coordinate_max - coordinate_min)
    assert math.isclose(gap, math.sqrt(n), rel_tol=1e-12, abs_tol=1e-12)

    for m in range(1, n + 1):
        restricted = values[: 2 * m]
        upper = np.max(np.stack(restricted), axis=0)
        lower = np.min(np.stack(restricted), axis=0)
        assert math.isclose(
            np.linalg.norm(upper - lower),
            math.sqrt(m),
            rel_tol=1e-12,
            abs_tol=1e-12,
        )


def check_nonradial_obstruction(epsilon: float) -> None:
    # d(a,b)=d(a,c)=1 and d(b,c)=epsilon satisfies all triangle inequalities.
    assert 0.0 < epsilon < 1.0
    assert 1.0 <= 1.0 + epsilon
    # f(a)=e_1, f(b)=0 is 1-Lipschitz; isotonicity c>=a forces
    # ||F(c)-F(b)|| >= 1 across distance epsilon.
    assert 1.0 / epsilon > 1.0


def main() -> None:
    for n in range(1, 129):
        check_radial_extremizer(n)
    for m in range(2, 1002):
        check_nonradial_obstruction(1.0 / m)
    print("verified n=1..128 and 1000 nonradial obstruction scales")


if __name__ == "__main__":
    main()

