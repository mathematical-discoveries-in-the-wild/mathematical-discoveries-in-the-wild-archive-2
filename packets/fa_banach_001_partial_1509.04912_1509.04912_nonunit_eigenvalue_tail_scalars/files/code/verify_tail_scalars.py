"""Finite sanity checks for the explicit tail-universal scalar sets.

The proof is analytic. This script only checks the lattice approximation and
the two non-density scale estimates for representative nonunit eigenvalues.
"""

import cmath
import math


TARGETS = [0j, 1 + 2j, -3.25 + 0.4j, 5.5 - 4.75j]
EIGENVALUES = [2 * cmath.exp(0.37j), 0.5 * cmath.exp(-0.61j)]
N_VALUES = [8, 16, 32, 64]


def nearest_grid_point(z: complex, n: int) -> complex:
    j = round(n * z.real)
    k = round(n * z.imag)
    assert j * j + k * k <= n**4
    return complex(j, k) / n


for lam in EIGENVALUES:
    radius = abs(lam)
    max_error = 0.0
    for n in N_VALUES:
        for target in TARGETS:
            lattice_point = nearest_grid_point(target, n)
            gamma = lattice_point / (lam**n)
            recovered = (lam**n) * gamma
            error = abs(recovered - target)
            max_error = max(max_error, error)
            assert error <= math.sqrt(2) / (2 * n) + 1e-10
    if radius > 1:
        scale_values = [n * radius ** (-n) for n in N_VALUES]
        assert all(a > b for a, b in zip(scale_values, scale_values[1:]))
        scale_label = "block outer radii"
    else:
        scale_values = [radius ** (-n) / n for n in N_VALUES]
        assert all(a < b for a, b in zip(scale_values, scale_values[1:]))
        scale_label = "nonzero block inner radii"
    print(f"lambda modulus: {radius:.6g}")
    print(f"maximum lattice recovery error: {max_error:.6g}")
    print(f"{scale_label}: " + ", ".join(f"{x:.6g}" for x in scale_values))

print("all finite sanity checks passed")
