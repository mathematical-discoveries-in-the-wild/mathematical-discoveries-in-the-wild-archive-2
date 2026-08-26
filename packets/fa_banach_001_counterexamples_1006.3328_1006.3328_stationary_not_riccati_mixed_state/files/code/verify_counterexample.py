#!/usr/bin/env python3
"""Exact finite-dimensional checks for the arXiv:1006.3328 counterexample."""

from fractions import Fraction


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


lambda_plus = [3, 1]
lambda_minus = [-3, -1]
sylvester_coefficients = [
    [lambda_plus[j] - lambda_minus[i] for j in range(2)] for i in range(2)
]
assert sylvester_coefficients == [[6, 4], [4, 2]]
assert all(c != 0 for row in sylvester_coefficients for c in row)

# Basis: |0,e_1>, |0,e_2>, |1,e_1>, |1,e_2>.
h = [[Fraction(0) for _ in range(4)] for _ in range(4)]
for i, value in enumerate([3, 1, -3, -1]):
    h[i][i] = Fraction(value)

a = Fraction(1, 3)
omega_total = [[Fraction(0) for _ in range(4)] for _ in range(4)]
for i, value in enumerate([a / 2, a / 2, (1 - a) / 2, (1 - a) / 2]):
    omega_total[i][i] = value

commutator = subtract(matmul(h, omega_total), matmul(omega_total, h))
assert all(value == 0 for row in commutator for value in row)

partial_trace = [
    [omega_total[0][0] + omega_total[1][1], Fraction(0)],
    [Fraction(0), omega_total[2][2] + omega_total[3][3]],
]
assert partial_trace == [[a, 0], [0, 1 - a]]

print("Sylvester coefficients:", sylvester_coefficients)
print("Commutator vanishes: yes")
print("Reduced state:", partial_trace)
print("All exact checks passed.")
