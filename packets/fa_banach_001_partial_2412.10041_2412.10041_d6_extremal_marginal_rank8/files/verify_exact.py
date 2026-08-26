"""Exact verification of the d=6, Choi-rank 8 construction.

No floating-point arithmetic or third-party package is used. Gaussian
integers are pairs (real, imaginary). The extremality minor is reduced by
the homomorphism Z[i] to F_101 that sends i to 10.
"""

from __future__ import annotations

G = tuple[int, int]
ZERO: G = (0, 0)
ONE: G = (1, 0)
D = 6
R = 8
PRIME = 101
I_MOD = 10

PERMUTATIONS = [
    [2, 3, 4, 1, 0, 5],
    [0, 4, 1, 5, 3, 2],
    [2, 0, 5, 1, 3, 4],
    [3, 4, 2, 0, 5, 1],
    [3, 5, 1, 0, 4, 2],
    [0, 3, 2, 5, 4, 1],
    [0, 1, 3, 2, 5, 4],
    [4, 3, 5, 0, 1, 2],
]

WEIGHTS = [
    [8, 8, 8, 6, 1, 4],
    [7, 7, 3, 5, 6, 7],
    [4, 2, 2, 7, 7, 2],
    [3, 3, 5, 4, 8, 8],
    [2, 6, 4, 8, 4, 1],
    [6, 5, 6, 1, 5, 5],
    [5, 1, 1, 2, 3, 6],
    [1, 4, 7, 3, 2, 3],
]

# Codes 0,1,2,3 mean 1,-1,i,-i.
PHASE_CODES = [
    [1, 3, 3, 2, 0, 0],
    [0, 1, 1, 1, 1, 3],
    [0, 0, 0, 1, 2, 2],
    [1, 0, 2, 0, 3, 2],
    [0, 2, 2, 3, 2, 2],
    [0, 0, 0, 1, 2, 2],
    [2, 1, 3, 2, 2, 1],
    [1, 3, 0, 1, 1, 2],
]
PHASES: tuple[G, ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


def add(x: G, y: G) -> G:
    return (x[0] + y[0], x[1] + y[1])


def mul(x: G, y: G) -> G:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def conj(x: G) -> G:
    return (x[0], -x[1])


def scale(n: int, x: G) -> G:
    return (n * x[0], n * x[1])


def zero_matrix() -> list[list[G]]:
    return [[ZERO for _ in range(D)] for _ in range(D)]


def adjoint(a: list[list[G]]) -> list[list[G]]:
    return [[conj(a[c][r]) for c in range(D)] for r in range(D)]


def matmul(a: list[list[G]], b: list[list[G]]) -> list[list[G]]:
    out = zero_matrix()
    for r in range(D):
        for c in range(D):
            value = ZERO
            for k in range(D):
                value = add(value, mul(a[r][k], b[k][c]))
            out[r][c] = value
    return out


def matsum(items: list[list[list[G]]]) -> list[list[G]]:
    out = zero_matrix()
    for item in items:
        for r in range(D):
            for c in range(D):
                out[r][c] = add(out[r][c], item[r][c])
    return out


def flatten(a: list[list[G]]) -> list[G]:
    return [a[r][c] for r in range(D) for c in range(D)]


def to_mod(x: G) -> int:
    return (x[0] + I_MOD * x[1]) % PRIME


def determinant_mod(a: list[list[int]]) -> int:
    a = [[entry % PRIME for entry in row] for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    det = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det % PRIME
        pivot_value = a[col][col]
        det = det * pivot_value % PRIME
        inverse = pow(pivot_value, PRIME - 2, PRIME)
        for r in range(col + 1, n):
            factor = a[r][col] * inverse % PRIME
            if factor:
                a[r] = [
                    (a[r][c] - factor * a[col][c]) % PRIME for c in range(n)
                ]
    return det


def main() -> None:
    kraus = []
    for j in range(R):
        w = zero_matrix()
        for input_column in range(D):
            output_row = PERMUTATIONS[j][input_column]
            w[output_row][input_column] = scale(
                WEIGHTS[j][input_column], PHASES[PHASE_CODES[j][input_column]]
            )
        kraus.append(w)

    left_normalization = matsum([matmul(adjoint(w), w) for w in kraus])
    right_normalization = matsum([matmul(w, adjoint(w)) for w in kraus])
    target = [[scale(204, ONE) if r == c else ZERO for c in range(D)] for r in range(D)]
    assert left_normalization == target
    assert right_normalization == target

    columns: list[list[G]] = []
    for i in range(R):
        for j in range(R):
            left = matmul(adjoint(kraus[i]), kraus[j])
            right = matmul(kraus[j], adjoint(kraus[i]))
            columns.append(flatten(left) + flatten(right))

    rows = [[to_mod(columns[c][r]) for c in range(R * R)] for r in range(2 * D * D)]
    leading_minor = rows[: R * R]
    det = determinant_mod(leading_minor)
    assert det == 19

    print("sum_j W_j^* W_j = 204 I_6")
    print("sum_j W_j W_j^* = 204 I_6")
    print("leading 64-by-64 extremality minor modulo 101 =", det)
    print("certificate verified")


if __name__ == "__main__":
    main()
