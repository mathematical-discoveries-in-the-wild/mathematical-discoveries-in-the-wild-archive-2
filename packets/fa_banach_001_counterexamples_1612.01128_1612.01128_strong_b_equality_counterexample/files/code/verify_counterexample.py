"""Deterministic checks for the box counterexample in the packet.

The proof is exact and does not depend on this script.  These checks guard
against transcription errors in the endpoint widths, constant volume, and
the first-variation calculation used in the scope discussion.
"""

from math import e, isclose, pi


a = 0.5
grid = [j / 1000 for j in range(1001)]
min_width_2 = min(2 * e**s for s in grid)
min_width_3 = min(3 * e ** (-s) for s in grid)
assert min_width_2 >= 1
assert min_width_3 >= 1

# Cross-sectional integration over |x_1| <= a.
constant_volume = 2 * pi * (a - a**3 / 3)
assert isclose(constant_volume, 11 * pi / 12, rel_tol=0, abs_tol=1e-15)

# First variation along A=diag(-2,1,1): 4*pi*a*(1-a^2)>0.
first_variation = 4 * pi * a * (1 - a**2)
assert first_variation > 0

print(f"min second half-width on [0,1]: {min_width_2:.12f}")
print(f"min third half-width on [0,1]:  {min_width_3:.12f}")
print(f"constant intersection volume:    {constant_volume:.12f}")
print(f"first variation at the ball:     {first_variation:.12f}")
