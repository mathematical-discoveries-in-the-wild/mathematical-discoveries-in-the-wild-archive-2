"""Exact-rational sanity checks for the rank-one incidence decomposition."""

from fractions import Fraction
from itertools import product


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def mat_vec(a, x):
    return [dot(row, x) for row in a]


def mat_mul(a, b):
    cols = list(zip(*b))
    return [[dot(row, col) for col in cols] for row in a]


def projection(u):
    q = dot(u, u)
    assert q != 0
    return [[ui * uj / q for uj in u] for ui in u]


def transpose(a):
    return [list(col) for col in zip(*a)]


def e(j, m):
    return [Fraction(int(i == j)) for i in range(m)]


def main():
    identity_checks = 0
    witness_checks = 0
    for m in range(2, 7):
        vectors = [
            e(0, m),
            e(1, m),
            [Fraction(i + 1) for i in range(m)],
            [Fraction((-1) ** i * (i + 1)) for i in range(m)],
        ]
        x = [Fraction(i + 2) for i in range(m)]
        y = [Fraction(2 * i - 1) for i in range(m)]
        for u in vectors:
            p = projection(u)
            assert p == transpose(p)
            assert mat_mul(p, p) == p
            lhs = dot(y, mat_vec(p, x)) * dot(u, u)
            rhs = dot(u, y) * dot(u, x)
            assert lhs == rhs
            identity_checks += 1

        x0, y0 = e(0, m), e(1, m)
        for n in range(1, 5):
            for pattern in product("XY", repeat=n):
                us = [y0 if choice == "X" else x0 for choice in pattern]
                recovered = []
                for u in us:
                    p = projection(u)
                    px_zero = all(v == 0 for v in mat_vec(p, x0))
                    py_zero = all(v == 0 for v in mat_vec(p, y0))
                    assert px_zero != py_zero
                    recovered.append("X" if px_zero else "Y")
                assert tuple(recovered) == pattern
                witness_checks += 1

    print(f"identity checks: {identity_checks}")
    print(f"pattern witness checks: {witness_checks}")
    print("all exact-rational checks passed")


if __name__ == "__main__":
    main()
