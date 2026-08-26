"""Finite arithmetic check for the block lower bound in the packet."""

from math import fsum


for cutoff in (1, 2, 5, 10, 100, 1000):
    l1_mass = fsum(1.0 / (k * k) for k in range(1, cutoff + 1))
    proved_square_lower_bound = 0.5 * fsum(1.0 / k for k in range(1, cutoff + 1))
    print(
        f"K={cutoff:4d}  terminal_L1={l1_mass:.12f}  "
        f"square_L1_lower_bound={proved_square_lower_bound:.12f}"
    )

