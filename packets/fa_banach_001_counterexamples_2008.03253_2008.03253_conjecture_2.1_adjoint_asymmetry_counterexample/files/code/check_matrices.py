#!/usr/bin/env python3
"""Finite sanity checks for the square-zero Conjecture 2.1 counterexample.

The packet proof is symbolic.  This script only checks representative numeric
instances of its two 2-by-2 matrix identities.
"""


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def close(a, b, tolerance=1e-12):
    return all(abs(a[i][j] - b[i][j]) <= tolerance for i in range(2) for j in range(2))


def main():
    n = [[0j, 1 + 0j], [0j, 0j]]
    n_star = [[0j, 0j], [1 + 0j, 0j]]
    zero = [[0j, 0j], [0j, 0j]]
    identity = [[1 + 0j, 0j], [0j, 1 + 0j]]

    tested = 0
    for a in (0.25, 1.0, 3.0):
        for b in (0.5, 1.0, 4.0):
            for alpha in (1 + 0j, -1 + 0j, 1j, 2 - 3j):
                non_adjoint = add(scale(a, n), scale(alpha * b, n))
                adjoint = add(scale(a, n_star), scale(alpha * b, n))

                assert close(multiply(non_adjoint, non_adjoint), zero)
                assert close(multiply(adjoint, adjoint), scale(alpha * a * b, identity))
                tested += 1

    print(f"{tested} matrix instances passed")


if __name__ == "__main__":
    main()
