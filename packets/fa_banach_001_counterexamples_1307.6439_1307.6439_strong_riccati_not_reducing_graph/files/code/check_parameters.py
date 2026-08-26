#!/usr/bin/env python3
"""Deterministic numerical checks for the explicit Riccati counterexample.

These checks illustrate the exact inequalities used in the proof.  They do
not replace the operator-theoretic argument in the solution packet.
"""

from cmath import sqrt
from fractions import Fraction


c = Fraction(3, 100)
eps = Fraction(1, 100)
r = 200

hilbert_norm_bound = c + 2 * eps
graph_norm_bound = c + eps * r + eps / r
series_ratio = hilbert_norm_bound * graph_norm_bound

# The characteristic polynomial is
#   (eps*r) z^2 + (c+i) z + eps/r.
a = complex(float(eps * r))
b = complex(float(c), 1.0)
d = complex(float(eps / r))
disc = b * b - 4 * a * d
roots = ((-b + sqrt(disc)) / (2 * a), (-b - sqrt(disc)) / (2 * a))

rouche_remainder_bound = (float(c * c) + 1.0) ** 0.5 + float(eps / r)

print(f"||X|| bound             = {hilbert_norm_bound} = {float(hilbert_norm_bound):.10f}")
print(f"||A X A^(-1)|| bound    = {graph_norm_bound} = {float(graph_norm_bound):.10f}")
print(f"series ratio             = {series_ratio} = {float(series_ratio):.10f}")
print(f"Rouche dominant term     = {float(eps*r):.10f}")
print(f"Rouche remainder bound   = {rouche_remainder_bound:.10f}")
for j, root in enumerate(roots, 1):
    print(f"root {j}                  = {root.real:+.12f}{root.imag:+.12f}i; |root|={abs(root):.12f}")

assert hilbert_norm_bound == Fraction(1, 20)
assert graph_norm_bound == Fraction(40601, 20000)
assert series_ratio == Fraction(40601, 400000)
assert series_ratio < 1
assert float(eps * r) > rouche_remainder_bound
assert all(abs(root) < 1 for root in roots)
print("all checks passed")
