"""Independent numerical/symbolic checks for the 2202.06343 counterexample.

The proof in main.tex is exact and does not depend on this script.
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp


def in_omega(x: float) -> bool:
    return (0.0 <= x < 2.0) or (3.0 <= x < 4.0)


def main() -> None:
    c = sp.symbols("c", real=True)
    squared_modulus = 8 * c**3 + 4 * c**2 - 4 * c + 1
    critical_points = sp.solve(sp.diff(squared_modulus, c), c)
    candidates = [-sp.Integer(1), sp.Integer(1), *critical_points]
    values = [(point, sp.simplify(squared_modulus.subs(c, point))) for point in candidates]
    exact_min = (sp.Integer(47) - 14 * sp.sqrt(7)) / 27

    assert min(value for _, value in values) == exact_min
    assert max(value for _, value in values) == 9
    assert exact_min > 0

    # Multi-tiling count away from the null set of integer boundaries.
    for x in np.linspace(-4.875, 4.875, 80):
        count = sum(in_omega(x - n) for n in range(-12, 13))
        assert count == 3, (x, count)

    theta = np.linspace(0.0, 2.0 * math.pi, 1_000_001)
    z = np.exp(1j * theta)
    sampled = np.abs(1.0 + z + z**3) ** 2
    assert sampled.min() > 0.3688
    assert abs(sampled.max() - 9.0) < 1e-12

    print("critical values:")
    for point, value in values:
        print(f"  c={point}: {value} = {float(value):.12f}")
    print(f"exact lower Riesz bound: {exact_min} = {float(exact_min):.12f}")
    print("upper Riesz bound: 9")
    print("sampled multi-tiling count: 3 at all 80 test points")
    print("all checks passed")


if __name__ == "__main__":
    main()
