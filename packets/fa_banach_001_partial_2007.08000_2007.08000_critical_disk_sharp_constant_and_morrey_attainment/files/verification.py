"""Numerical audit for the critical two-dimensional disk extremal."""

from math import pi

from scipy.integrate import quad
from scipy.special import jn_zeros, jv, jvp


j = float(jn_zeros(0, 1)[0])
j1_at_j = float(jv(1, j))

denominator = pi * quad(lambda r: jv(1, j * r) ** 2 * r, 0.0, 1.0)[0]


def interior_density(r):
    radial = j * jvp(1, j * r)
    angular = j / 2.0 if r == 0.0 else jv(1, j * r) / r
    return (radial * radial + angular * angular) * r


interior_energy = pi * quad(interior_density, 0.0, 1.0)[0]
exterior_energy = pi * j1_at_j**2
quotient = (interior_energy + exterior_energy) / denominator

assert abs(j * jvp(1, j) + jv(1, j)) < 1e-12
assert abs(quotient - j * j) < 1e-10
assert j < float(jn_zeros(1, 1)[0])

print(f"j_0,1 = {j:.15f}")
print(f"sharp constant = {1.0 / (j*j):.15f}")
print(f"denominator = {denominator:.15f}")
print(f"interior energy = {interior_energy:.15f}")
print(f"exterior energy = {exterior_energy:.15f}")
print(f"Rayleigh quotient = {quotient:.15f}")

