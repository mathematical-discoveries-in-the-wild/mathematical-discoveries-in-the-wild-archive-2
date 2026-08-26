#!/usr/bin/env python3
"""Exact checks for the 2x2 witness and path-block identities."""

import sympy as sp


Z2 = sp.zeros(2)
E11 = sp.Matrix([[1, 0], [0, 0]])
E21 = sp.Matrix([[0, 0], [1, 0]])
FLIP = sp.Matrix([[0, 1], [1, 0]])

# This is the universal local witness used in all three zero-product arguments.
assert E11 * E21 == Z2
assert E11 * FLIP * E21 == E11

# A concrete g=3 path pencil, with layer sizes 1,2,2,1.
dims = [1, 2, 2, 1]
offsets = [0]
for size in dims:
    offsets.append(offsets[-1] + size)
d = offsets[-1]

connectors = [
    sp.Matrix([[1, 2]]),
    sp.Matrix([[1, 0], [3, 1]]),
    sp.Matrix([[2], [-1]]),
]

B = []
for j, connector in enumerate(connectors, start=1):
    matrix = sp.zeros(d)
    r0, r1 = offsets[j - 1], offsets[j]
    c0, c1 = offsets[j], offsets[j + 1]
    matrix[r0:r1, c0:c1] = connector
    B.append(matrix)

for j in range(3):
    for k in range(3):
        if k != j + 1:
            assert B[j] * B[k] == sp.zeros(d)
        if j != k:
            assert B[j] * B[k].conjugate().T == sp.zeros(d)
            assert B[j].conjugate().T * B[k] == sp.zeros(d)

# Exact block-conjugation check for one nontrivial orthogonal choice of W_r.
X = [
    sp.Matrix([[1, 2], [0, -1]]),
    sp.Matrix([[0, 1], [3, 0]]),
    sp.Matrix([[2, 0], [1, 1]]),
]
W = [sp.eye(2), FLIP, sp.diag(1, -1), sp.Matrix([[0, -1], [1, 0]])]

def pencil(variable_tuple):
    answer = sp.eye(2 * d)
    for coefficient, variable in zip(B, variable_tuple):
        term = sp.kronecker_product(coefficient, variable)
        answer += term + term.conjugate().T
    return answer

transformed = [W[j].conjugate().T * X[j] * W[j + 1] for j in range(3)]
block_unitary = sp.diag(*[sp.kronecker_product(sp.eye(size), W[r])
                          for r, size in enumerate(dims)])
assert pencil(transformed) == block_unitary.conjugate().T * pencil(X) * block_unitary

print("matrix-unit zero/nonzero witness passed")
print("all path-block zero-product relations passed")
print("exact block-conjugation identity passed")

