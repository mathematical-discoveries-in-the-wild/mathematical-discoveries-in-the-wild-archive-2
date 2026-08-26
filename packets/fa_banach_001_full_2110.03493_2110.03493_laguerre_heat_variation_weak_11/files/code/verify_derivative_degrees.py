#!/usr/bin/env python3
"""Exact symbolic audit for the Mehler-component derivative numerators."""

import sympy as sp


r, A, X, Y, Z = sp.symbols("r A X Y Z")
xi, yi, si = sp.symbols("x_i y_i s_i")

q = X * r**2 - 2 * Z * r + Y
G = (1 - r**2) ** (-A) * sp.exp(-q / (1 - r**2))

P0 = sp.factor(sp.diff(sp.log(G), r) * (1 - r**2) ** 2 / 2)

px = r**2 * xi - r * yi * si
py = yi - r * xi * si

Px = sp.factor(
    sp.diff(px * G / (1 - r**2), r) * (1 - r**2) ** 3 / G
)
Py = sp.factor(
    sp.diff(py * G / (1 - r**2), r) * (1 - r**2) ** 3 / G
)

assert sp.expand(P0) == sp.expand(
    Z + (A - X - Y) * r + Z * r**2 - A * r**3
)
assert sp.degree(P0, r) <= 3
assert sp.degree(Px, r) <= 5
assert sp.degree(Py, r) <= 4

print("P0 =", sp.collect(sp.expand(P0), r))
print("degree(P0) =", sp.degree(P0, r))
print("Px =", sp.collect(sp.expand(Px), r))
print("degree(Px) =", sp.degree(Px, r))
print("Py =", sp.collect(sp.expand(Py), r))
print("degree(Py) =", sp.degree(Py, r))
print("all symbolic assertions passed")

