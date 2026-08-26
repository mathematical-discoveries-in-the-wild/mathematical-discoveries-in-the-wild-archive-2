#!/usr/bin/env python3
"""Exact finite-grid checks for the interval-min semilattice example.

These checks illustrate the algebraic identities. Continuity and the
infinite-dimensional non-classification proof are established in main.tex.
"""

from fractions import Fraction


grid = [Fraction(j, 40) for j in range(41)]

for x in grid:
    assert min(x, 1) == x
    assert min(x, x) == x
    for y in grid:
        assert min(x, y) == min(y, x)
        for z in grid:
            assert min(min(x, y), z) == min(x, min(y, z))

# The only invertible grid element for the identity 1 is 1 itself.
invertible = [x for x in grid if any(min(x, y) == 1 and min(y, x) == 1 for y in grid)]
assert invertible == [Fraction(1)]

# Every generator f(min(s,t))g(t) is constant in s along t=0.  The target
# F(s,t)=s has best uniform constant approximation error 1/2 on that line.
best_constant_error = min(max(abs(x - c) for x in grid) for c in grid)
assert best_constant_error == Fraction(1, 2)

print("checked associativity/commutativity on 41^3 triples")
print("only the identity is invertible on the grid")
print("finite-grid cancellation obstruction =", best_constant_error)
print("all exact checks passed")

