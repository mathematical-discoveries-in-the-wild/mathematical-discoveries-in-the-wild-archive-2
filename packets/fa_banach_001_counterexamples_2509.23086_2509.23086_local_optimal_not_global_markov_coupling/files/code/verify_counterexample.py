"""Exact checks for the three-state Markovian-coupling counterexample."""

from itertools import product
from math import exp


N = 3
F = (1, 2, 0)
G = (1, 0, 1)
C = (7, 6, 0, 10, 2, 10, 6, 9, 1)
STAR = (1, 0, 1, 0, 1, 0, 1, 0, 1)
ALT = (1, 0, 1, 0, 1, 0, 1, 0, 0)


def mixed_differences():
    out = []
    for x in range(N):
        for y in range(N):
            out.append(
                C[N * F[x] + G[y]]
                - C[N * F[x] + y]
                - C[N * x + G[y]]
                + C[N * x + y]
            )
    return tuple(out)


def generator(policy):
    q = [[0] * (N * N) for _ in range(N * N)]
    for x in range(N):
        for y in range(N):
            i = N * x + y
            s = policy[i]
            for a, b, rate in (
                (F[x], G[y], s),
                (F[x], y, 1 - s),
                (x, G[y], 1 - s),
            ):
                j = N * a + b
                if j != i:
                    q[i][j] += rate
            q[i][i] = -sum(q[i])
    return q


def matvec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def add_twice_identity(q):
    return tuple(
        tuple(q[i][j] + (2 if i == j else 0) for j in range(N * N))
        for i in range(N * N)
    )


d = mixed_differences()
assert d == (-7, 7, -14, 11, -11, 16, -4, 4, -2)
assert STAR == tuple(int(value < 0) for value in d)

q_star = generator(STAR)
star_derivative = matvec(q_star, C)
for policy in product((0, 1), repeat=N * N):
    derivative = matvec(generator(policy), C)
    assert all(a <= b for a, b in zip(star_derivative, derivative))

r_star = add_twice_identity(q_star)
r_alt = add_twice_identity(generator(ALT))
v_star = C
v_alt = C
deltas = []
for _ in range(25):
    deltas.append(v_star[8] - v_alt[8])
    v_star = matvec(r_star, v_star)
    v_alt = matvec(r_alt, v_alt)

assert deltas[0] == 0
assert deltas[1] == -2
assert all(value == 2 for value in deltas[2:])

gap = 2 * exp(-4) * (exp(2) - 5)
assert gap > 0
print("mixed differences:", d)
print("uniformized differences:", deltas[:10])
print("exact gap: 2*exp(-4)*(exp(2)-5)")
print("decimal gap:", gap)

