#!/usr/bin/env python3
"""Exact certificate for a two-variable wild-disc MNAE point.

Floating point is used only to *propose* two rational approximate inverses.
Every inequality on which the proof depends is then checked with Python
integers and fractions.  Thus a successful run is an exact certificate.
"""

from fractions import Fraction
from hashlib import sha256

import numpy as np


N = 8
D = 10**15
PAIRS = [(i, j) for i in range(N) for j in range(i, N)]
S = len(PAIRS)

X_NUM = [
    [-3, 5, -3, 1, -3, -4, -3, 0],
    [5, -1, 5, -3, -5, -2, 3, -1],
    [-3, 5, 2, -2, 1, 3, 0, 1],
    [1, -3, -2, 5, -4, 3, -2, 2],
    [-3, -5, 1, -4, 3, -5, 1, 1],
    [-4, -2, 3, 3, -5, 3, -5, -1],
    [-3, 3, 0, -2, 1, -5, 2, -5],
    [0, -1, 1, 2, 1, -1, -5, 1],
]

Z_NUM = [
    [5, 3, -1, 0, 1, 5, -4, 2],
    [1, 2, -3, -5, -1, -5, 0, -5],
    [5, -3, 5, 3, -3, 1, -5, 0],
]

# A_NUM / 10^15 is a rational approximate signed square root of
# P = I - X^2 - Z^T Z.  The exact Y used in the theorem is supplied by the
# contraction argument below, rather than by floating-point diagonalization.
A_NUM = [
    [469136539517107, 418057100896713, -513730559248146, -19705331325464, 115589350876164, 315461324061599, -262136144216438, 126120353785681],
    [418057100896713, 226044565094389, 316155862074043, -591487703586026, -404383337428309, -102525629138037, 105847039317755, -68076824009979],
    [-513730559248146, 316155862074043, 343845406695791, -286080313659530, -5713670391864, 441714042553604, -342388858747631, 160943853597458],
    [-19705331325464, -591487703586026, -286080313659530, -185003309748076, -525675862063652, 313713354292056, -197186242248850, 47691229959701],
    [115589350876164, -404383337428309, -5713670391864, -525675862063652, 647636604497521, 110185471831049, -79262335507014, 209718944007],
    [315461324061599, -102525629138037, 441714042553604, 313713354292056, 110185471831049, 546819792547518, 306432223723976, -160736732966099],
    [-262136144216438, 105847039317755, -342388858747631, -197186242248850, -79262335507014, 306432223723976, 721476885267441, 110205575101764],
    [126120353785681, -68076824009979, 160943853597458, 47691229959701, 209718944007, -160736732966099, 110205575101764, 918313788896616],
]

# Columns of K_NUM / 42 form a basis of ker Z.
K_NUM = [
    [39, 34, 58, 31, 62],
    [-108, -92, -236, 10, -190],
    [-129, -64, -208, 17, -176],
    [42, 0, 0, 0, 0],
    [0, 42, 0, 0, 0],
    [0, 0, 42, 0, 0],
    [0, 0, 0, 42, 0],
    [0, 0, 0, 0, 42],
]

# Rows selected from the 121-by-108 matrix-extreme coefficient matrix.
SELECTED_ROWS = [
    48, 55, 53, 54, 52, 49, 51, 50, 71, 70, 64, 69, 68, 66, 65, 67,
    63, 61, 60, 56, 62, 59, 58, 57, 120, 103, 102, 100, 96, 78, 101,
    99, 88, 76, 72, 94, 92, 77, 93, 74, 90, 97, 28, 111, 107, 110,
    108, 75, 104, 84, 86, 83, 11, 24, 109, 12, 27, 80, 95, 36, 29,
    73, 106, 8, 85, 82, 25, 13, 10, 32, 37, 34, 0, 81, 3, 5, 14,
    1, 38, 87, 39, 15, 33, 35, 89, 40, 105, 42, 45, 9, 79, 18, 16,
    44, 22, 118, 119, 17, 117, 26, 116, 112, 98, 46, 4, 31, 7, 41,
]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(N))
            for i in range(N)]


def decimal_upper(value, digits=12):
    """Human-readable decimal; pass/fail decisions never use this value."""
    return f"{float(value):.{digits}e}"


def exact_approx_inverse_certificate(matrix_num, denominator, rounding_den):
    """Return exact bounds from a rounded numerical approximate inverse.

    If R is the generated rational matrix and e=||I-RM||_infinity<1,
    then ||M^{-1}||_infinity <= ||R||_infinity/(1-e).
    """
    size = len(matrix_num)
    floating = np.asarray(matrix_num, dtype=float) / float(denominator)
    proposed = np.linalg.inv(floating)
    r_num = [
        [int(round(proposed[i, j] * rounding_den)) for j in range(size)]
        for i in range(size)
    ]

    # Sparse exact multiplication R_num * matrix_num.
    sparse_rows = [
        [(j, value) for j, value in enumerate(row) if value]
        for row in matrix_num
    ]
    residual_row_max = 0
    inverse_row_max = 0
    product_den = rounding_den * denominator
    for i, r_row in enumerate(r_num):
        inverse_row_max = max(inverse_row_max, sum(abs(v) for v in r_row))
        product_row = [0] * size
        for k, r_ik in enumerate(r_row):
            if r_ik:
                for j, m_kj in sparse_rows[k]:
                    product_row[j] += r_ik * m_kj
        residual_row_sum = sum(
            abs((product_den if i == j else 0) - product_row[j])
            for j in range(size)
        )
        residual_row_max = max(residual_row_max, residual_row_sum)

    epsilon = Fraction(residual_row_max, product_den)
    r_norm = Fraction(inverse_row_max, rounding_den)
    assert epsilon < 1
    inverse_bound = r_norm / (1 - epsilon)
    digest_payload = ",".join(str(v) for row in r_num for v in row).encode()
    return epsilon, inverse_bound, sha256(digest_payload).hexdigest()


def lyapunov_numerator():
    """Matrix of H -> AH+HA on upper-triangular coordinates, scaled by D."""
    result = [[0] * S for _ in range(S)]
    for column, (a, b) in enumerate(PAIRS):
        for row, (i, j) in enumerate(PAIRS):
            value = 0
            if j == a:
                value += A_NUM[i][b]
            if a != b and j == b:
                value += A_NUM[i][a]
            if i == a:
                value += A_NUM[b][j]
            if a != b and i == b:
                value += A_NUM[a][j]
            result[row][column] = value
    return result


def symmetric_times_vector_rows(vector_num, scale):
    """Coefficient rows for B -> B vector_num, multiplied by scale."""
    result = [[0] * S for _ in range(N)]
    for column, (i, j) in enumerate(PAIRS):
        if i == j:
            result[i][column] = vector_num[i] * scale
        else:
            result[i][column] = vector_num[j] * scale
            result[j][column] = vector_num[i] * scale
    return result


def matrix_extreme_numerator():
    """The 121-by-108 coefficient matrix at A, with denominator 1260 D.

    For each column v of K it encodes
      B0 v - B1 Xv - B2 Av = 0,
      B1 v - B0 Xv = 0,
      B2 v - B0 Av = 0,
    and the final row is tr(B0 + X B1 + A B2)=0.
    """
    common_den = 1260 * D
    rows = []
    for column in range(5):
        v_num = [K_NUM[i][column] for i in range(N)]
        xv_num = matvec(X_NUM, v_num)
        av_num = matvec(A_NUM, v_num)
        bv = symmetric_times_vector_rows(v_num, 30 * D)
        bx = symmetric_times_vector_rows(xv_num, D)
        ba = symmetric_times_vector_rows(av_num, 30)
        for i in range(N):
            rows.append(bv[i] + [-x for x in bx[i]] + [-x for x in ba[i]])
        for i in range(N):
            rows.append([-x for x in bx[i]] + bv[i] + [0] * S)
        for i in range(N):
            rows.append([-x for x in ba[i]] + [0] * S + bv[i])

    trace_row = [0] * (3 * S)
    for column, (i, j) in enumerate(PAIRS):
        factor = 1 if i == j else 2
        if i == j:
            trace_row[column] = common_den
        trace_row[S + column] = factor * X_NUM[i][j] * 42 * D
        trace_row[2 * S + column] = factor * A_NUM[i][j] * 1260
    rows.append(trace_row)
    assert len(rows) == 121 and all(len(row) == 108 for row in rows)
    return rows, common_den


def main():
    assert A_NUM == transpose(A_NUM)
    assert X_NUM == transpose(X_NUM)
    assert len(SELECTED_ROWS) == 108 and len(set(SELECTED_ROWS)) == 108
    assert matmul(Z_NUM, K_NUM) == [[0] * 5 for _ in range(3)]
    # The first three columns of Z have nonzero determinant, so rank Z=3.
    z_minor_det = (
        Z_NUM[0][0] * (Z_NUM[1][1] * Z_NUM[2][2] - Z_NUM[1][2] * Z_NUM[2][1])
        - Z_NUM[0][1] * (Z_NUM[1][0] * Z_NUM[2][2] - Z_NUM[1][2] * Z_NUM[2][0])
        + Z_NUM[0][2] * (Z_NUM[1][0] * Z_NUM[2][1] - Z_NUM[1][1] * Z_NUM[2][0])
    )
    assert z_minor_det != 0

    x_squared = matmul(X_NUM, X_NUM)
    ztz = matmul(transpose(Z_NUM), Z_NUM)
    # P_NUM / 900 = I-X^2-Z^T Z.
    p_num = [
        [900 * (i == j) - x_squared[i][j] - ztz[i][j] for j in range(N)]
        for i in range(N)
    ]
    a_squared = matmul(A_NUM, A_NUM)
    residual_num = [
        [900 * a_squared[i][j] - D * D * p_num[i][j] for j in range(N)]
        for i in range(N)
    ]
    rho = Fraction(
        max(abs(v) for row in residual_num for v in row),
        900 * D * D,
    )

    lyapunov = lyapunov_numerator()
    eps_l, beta, digest_l = exact_approx_inverse_certificate(
        lyapunov, D, 10**10
    )
    # On symmetric matrices with the entrywise max norm,
    # ||H^2-G^2||_max <= 2 N r ||H-G||_max in a radius-r ball.
    contraction_constant = 4 * N * beta * beta * rho
    root_radius = 2 * beta * rho
    assert contraction_constant < 1
    assert rho < Fraction(1265, 10**18)
    assert eps_l < Fraction(1827, 10**12)
    assert beta < 1192
    assert contraction_constant < Fraction(5748, 10**11)
    assert root_radius < Fraction(3014, 10**15)

    coefficient_rows, coefficient_den = matrix_extreme_numerator()
    minor = [coefficient_rows[i] for i in SELECTED_ROWS]
    eps_m, gamma, digest_m = exact_approx_inverse_certificate(
        minor, coefficient_den, 10**8
    )

    # Only equations involving Av and the trace row change when A is replaced
    # by Y.  For v a column of K/42, their row-sum perturbation is at most
    # N ||v||_1 ||Y-A||_max; the trace-row bound is N^2 ||Y-A||_max.
    max_k_l1_num = max(
        sum(abs(K_NUM[i][column]) for i in range(N)) for column in range(5)
    )
    perturbation_factor = max(Fraction(N * max_k_l1_num, 42), N * N)
    rank_stability_constant = gamma * perturbation_factor * root_radius
    assert rank_stability_constant < 1
    assert max_k_l1_num == 544
    assert perturbation_factor == Fraction(2176, 21)
    assert eps_m < Fraction(2075, 10**9)
    assert gamma < 3146
    assert rank_stability_constant < Fraction(9824, 10**10)

    print("EXACT CERTIFICATE: PASS")
    print(f"rank(Z) certificate minor determinant = {z_minor_det}")
    print(f"dim ker(Z^T Z) = {N - 3}")
    print(f"square-root residual rho <= {decimal_upper(rho)}")
    print(f"Lyapunov inverse residual epsilon_L <= {decimal_upper(eps_l)}")
    print(f"Lyapunov inverse norm beta <= {decimal_upper(beta)}")
    print(f"contraction constant q <= {decimal_upper(contraction_constant)} < 1")
    print(f"root radius delta <= {decimal_upper(root_radius)}")
    print(f"minor inverse residual epsilon_M <= {decimal_upper(eps_m)}")
    print(f"minor inverse norm gamma <= {decimal_upper(gamma)}")
    print(f"coefficient perturbation factor c = {float(perturbation_factor):.12f}")
    print(f"rank-stability constant gamma*c*delta <= {decimal_upper(rank_stability_constant)} < 1")
    print(f"Arveson system: 3*5 = 15 equations < 2*8 = 16 unknowns")
    print(f"Lyapunov inverse numerator sha256 = {digest_l}")
    print(f"minor inverse numerator sha256 = {digest_m}")


if __name__ == "__main__":
    main()
