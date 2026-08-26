#!/usr/bin/env python3
"""Exact-arithmetic verification for the n=2 structured counterexample.

This script is supplementary: the packet contains the proof.  It rechecks all
coefficient identities, Schur--Cohn positivity polynomials, spectral
partitions, and the three exact dual separation certificates.
"""

from __future__ import annotations

import itertools

import sympy as sp


Q = sp.Rational
z, w, t, x = sp.symbols("z w t x")

c10 = -Q(111, 200)
c20 = -Q(69, 250)
c01 = Q(43, 50)
c11 = Q(5451, 20000)
c02 = -Q(1197, 10000)

poly = sp.expand(
    1
    + c10 * (z + w)
    + c20 * (z + w) ** 2
    + c01 * z * w
    + c11 * (z + w) * z * w
    + c02 * (z * w) ** 2
)


def assert_positive_definite_2x2(matrix: sp.Matrix) -> None:
    assert matrix == matrix.T
    assert matrix[0, 0] > 0
    assert sp.factor(matrix.det()) > 0


def assert_negative_definite_2x2(matrix: sp.Matrix) -> None:
    assert matrix == matrix.T
    assert matrix[0, 0] < 0
    assert sp.factor(matrix.det()) > 0


def canonical_pair(indices: tuple[int, int]) -> tuple[sp.Matrix, sp.Matrix]:
    lambdas = [Q(3, 10), Q(3, 4), -Q(7, 10), Q(19, 25)]
    complement = [j for j in range(4) if j not in indices]
    b1, b2 = (lambdas[j] for j in indices)
    l3, l4 = (lambdas[j] for j in complement)
    trace_c = l3 + l4
    det_c = l3 * l4
    rhs = 4 * c20 - b1 * b2 - det_c
    u = sp.factor((rhs - b1 * trace_c) / (b2 - b1))
    v = sp.factor(trace_c - u)
    r = sp.factor(u * v - det_c)
    return sp.diag(b1, b2), sp.Matrix([[u, 1], [r, v]])


def main() -> None:
    # A rational algebraic realization, used only to recheck the displayed
    # polynomial (these B,C are deliberately not a common contraction pair).
    b0 = sp.Matrix([[Q(3, 10), 3], [0, Q(3, 4)]])
    c0 = sp.Matrix([[-Q(7, 10), 0], [Q(1, 6), Q(19, 25)]])
    a0 = (b0 + c0) / 2
    d0 = b0 * c0
    det_poly = sp.expand((sp.eye(2) - (z + w) * a0 + z * w * d0).det())
    assert sp.expand(det_poly - poly) == 0

    expected_expansion = (
        1
        - Q(111, 200) * (z + w)
        - Q(69, 250) * (z**2 + w**2)
        + Q(77, 250) * z * w
        + Q(5451, 20000) * (z**2 * w + z * w**2)
        - Q(1197, 10000) * z**2 * w**2
    )
    assert sp.expand(poly - expected_expansion) == 0

    # Exact Schur--Cohn expressions on |w|=1, written as polynomials in
    # x=Re(w).  Positivity follows from endpoint checks and concavity/convexity.
    p_l = 734_995_123 - 235_177_572 * x - 494_459_520 * x**2
    f1 = 3680 * x**2 + 1883 * x - 5801
    f2 = 2_807_315_892_240 * x**2 + 150_481_096_164 * x - 2_964_727_540_151
    assert p_l.subs(x, -1) == 475_713_175 > 0
    assert p_l.subs(x, 1) == 5_358_031 > 0
    assert f1.subs(x, -1) == -4004 < 0
    assert f1.subs(x, 1) == -238 < 0
    assert f2.subs(x, -1) == -307_892_744_075 < 0
    assert f2.subs(x, 1) == -6_930_551_747 < 0

    alpha = c20 + c11 * w + c02 * w**2
    beta = c10 + (2 * c20 + c01) * w + c11 * w**2
    gamma = 1 + c10 * w + c20 * w**2
    star = lambda expr: sp.expand(expr.subs(w, 1 / w))
    ell = sp.factor(gamma * star(gamma) - alpha * star(alpha))
    m = sp.factor(star(gamma) * beta - alpha * star(beta))
    n_expr = sp.factor(ell**2 - m * star(m))
    # Substitute w+w^{-1}=2x by matching the symmetric Laurent coefficients.
    ell_x = p_l / Q(400_000_000)
    n_x = 3 * f1 * f2 / Q(40_000_000_000_000_000)
    assert symmetric_laurent_to_x(ell, w, x) == sp.expand(ell_x)
    assert symmetric_laurent_to_x(n_expr, w, x) == sp.expand(n_x)
    assert Q(111, 200) + Q(69, 250) < 1  # p(z,0) is zero-free on |z|<=1.

    diagonal = sp.factor(poly.subs({z: t, w: t}))
    expected_diagonal = -(3 * t - 10) * (3 * t - 4) * (7 * t + 10) * (19 * t - 25) / 10000
    assert sp.simplify(diagonal - expected_diagonal) == 0

    # One representative from each complementary 2+2 spectral partition.
    certificates = {
        (0, 2): (
            sp.Matrix([[33_335_537, -37_673_850], [-37_673_850, 42_576_768]]),
            sp.Matrix([[23_136_281, -4_691_714], [-4_691_714, 951_414]]),
        ),
        (0, 1): (
            sp.Matrix([[13_149_208, 32_661_562], [32_661_562, 81_130_750]]),
            sp.Matrix([[595_772, -1_744_823], [-1_744_823, 5_124_270]]),
        ),
        (0, 3): (
            sp.Matrix([[13_137_533, 32_657_413], [32_657_413, 81_181_395]]),
            sp.Matrix([[661_546, -1_808_353], [-1_808_353, 5_019_526]]),
        ),
    }

    expected_canonical_c = {
        (0, 2): sp.Matrix([[Q(1917, 1000), 1], [-Q(1350219, 1000000), -Q(407, 1000)]]),
        (0, 1): sp.Matrix([[-Q(163, 90), 1], [-Q(1157, 405), Q(421, 225)]]),
        (0, 3): sp.Matrix([[-Q(411, 230), 1], [-Q(5835, 2116), Q(169, 92)]]),
    }

    for indices, (dual_x, dual_y) in certificates.items():
        bmat, cmat = canonical_pair(indices)
        assert cmat == expected_canonical_c[indices]
        assert_positive_definite_2x2(dual_x)
        assert_positive_definite_2x2(dual_y)
        separator = sp.factor(
            dual_x - bmat * dual_x * bmat.T + dual_y - cmat * dual_y * cmat.T
        )
        assert_negative_definite_2x2(separator)
        print(
            f"partition {indices}: det(X)={dual_x.det()}, det(Y)={dual_y.det()}, "
            f"Z11={separator[0,0]}, det(Z)={sp.factor(separator.det())}"
        )

    # The six assignments are the three checked partitions and their
    # complements, which merely interchange B and C.
    all_partitions = set(itertools.combinations(range(4), 2))
    checked = set(certificates)
    checked_with_complements = checked | {
        tuple(j for j in range(4) if j not in indices) for indices in checked
    }
    assert all_partitions == checked_with_complements
    print("all exact checks passed")


def symmetric_laurent_to_x(expr: sp.Expr, variable: sp.Symbol, real_x: sp.Symbol) -> sp.Expr:
    terms: dict[int, sp.Expr] = {}
    for term in sp.Add.make_args(sp.expand(expr)):
        coefficient, exponent = term.as_coeff_exponent(variable)
        terms[int(exponent)] = terms.get(int(exponent), 0) + coefficient
    degree = max(abs(exponent) for exponent in terms)
    result = terms.get(0, 0)
    for exponent in range(1, degree + 1):
        assert sp.simplify(terms.get(exponent, 0) - terms.get(-exponent, 0)) == 0
        result += 2 * terms.get(exponent, 0) * sp.chebyshevt(exponent, real_x)
    return sp.expand(result)


if __name__ == "__main__":
    main()
