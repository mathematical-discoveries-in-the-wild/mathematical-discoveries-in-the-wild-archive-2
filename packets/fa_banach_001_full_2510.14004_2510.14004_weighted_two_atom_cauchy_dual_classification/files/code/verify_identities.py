#!/usr/bin/env python3
"""Exact algebra checks for the weighted two-atom CDSP classification.

The script verifies the elimination used for unequal weights, the closed
formulas used in the equal-weight simple-pole cases, and the negative leading
coefficient of the repeated-pole finite-difference minor.
"""

import sympy as s


def unequal_weight_checks() -> None:
    b, C, d, H, chi = s.symbols("b C d H chi", nonzero=True)
    m = b * (C + 4) / (b + 1)
    n = -b * d / (b - 1)
    uv = (m**2 - n**2) / 4

    # The physical coefficient relation solved for H=cos(gamma)^2.
    H_phys = s.factor(
        (2 * b * (C + 1) - b**2 - 1 - n**2) / (4 * (uv - b))
    )
    N_H = (
        -2 * C * b**3
        + 4 * C * b**2
        - 2 * C * b
        + b**4
        - 4 * b**3
        + b**2 * d**2
        + 6 * b**2
        - 4 * b
        + 1
    )
    D_H = (
        -C**2 * b**3
        + 2 * C**2 * b**2
        - C**2 * b
        - 8 * C * b**3
        + 16 * C * b**2
        - 8 * C * b
        + 4 * b**4
        + b**3 * d**2
        - 16 * b**3
        + 2 * b**2 * d**2
        + 24 * b**2
        + b * d**2
        - 16 * b
        + 4
    )
    assert s.factor(H_phys - (b + 1) ** 2 * N_H / (b * D_H)) == 0

    # Root geometry: P=(R+b/R)cos(phi), Q=(R-b/R)sin(phi).
    P2 = b**2 * (C + 4) ** 2 * H / (b + 1) ** 2
    Q2 = b**2 * d**2 * (1 - H) / (b - 1) ** 2
    root_equation = s.expand(P2 * chi - Q2 * (1 - chi) - 4 * b * chi * (1 - chi))
    realness_equation = s.expand(
        d**2 * (1 - H) * (1 - chi)
        - C * (C + 4) * H * chi
        + 4 * C * chi * (1 - chi)
    )
    resultant = s.factor(
        s.cancel(s.resultant(root_equation, realness_equation, chi).subs(H, H_phys))
    )
    L0 = b**2 - (C + 2) * b + 1
    expected = (
        16
        * d**2
        * (-C + d)
        * (C + d)
        * (C + 4)
        * (b - 1) ** 2
        * L0**5
        * N_H
        / D_H**3
    )
    assert s.factor(resultant - expected) == 0
    compact = (
        H_phys
        * b**3
        * d**2
        * (d**2 - C**2)
        * (C + 4)
        * L0**5
        / ((uv - b) ** 2 * (b - 1) ** 2 * (b + 1) ** 6)
    )
    assert s.factor(resultant - compact) == 0

    # If uv=b, the two remaining coefficient equations force L0=0 and
    # then |d|=C, impossible for two positive weights.
    d2_from_physical = (b - 1) ** 2 * (2 * b * C - (b - 1) ** 2) / b**2
    uv_equation = s.factor((m**2 - n**2 - 4 * b).subs(d**2, d2_from_physical))
    assert s.factor(uv_equation - L0**2 / (b + 1) ** 2) == 0

    # If L0=0 but uv!=b, the physical relation reduces to
    # ((b-1)^2-n^2)(H-1)=0.
    C_l0 = (b - 1) ** 2 / b
    physical = b**2 + 1 + n**2 + 4 * uv * H - 2 * b * (C + 1 + 2 * H)
    reduced = s.factor(physical.subs(C, C_l0))
    target = s.factor(((b - 1) ** 2 - n.subs(C, C_l0) ** 2) * (H - 1))
    assert s.factor(reduced - target) == 0


def equal_weight_checks() -> None:
    b, c = s.symbols("b c", positive=True)
    a = b * (c + 2) / (b + 1)
    h2 = s.factor((2 * b * (2 * c + 1) - b**2 - 1) / (4 * (a**2 - b)))
    A22 = -(b**3 - 4 * b**2 * c - 3 * b**2 + 3 * b - 1) / (b + 1)
    A11 = 4 * b * c - A22

    # Common-ray cross Gram value.
    E_common = s.factor(A11 - 4 * a * b * c * h2 + b * A22)
    expected = -(
        b**2 - 2 * b * c - 2 * b + 1
    ) ** 3 / ((b + 1) * (b**2 - b * c**2 - 4 * b * c - 2 * b + 1))
    assert s.factor(E_common - expected) == 0

    # The only possible zero of the numerator would force coincident support.
    c_zero = (b - 1) ** 2 / (2 * b)
    assert s.factor(h2.subs(c, c_zero) - 1) == 0

    # The denominator is exactly the nonzero discriminant factor.
    denominator = b**2 - b * c**2 - 4 * b * c - 2 * b + 1
    assert s.factor(denominator + (b + 1) ** 2 * (a**2 - b) / b) == 0


def repeated_pole_checks() -> None:
    R, ell = s.symbols("R ell", positive=True)
    A11, A12, A22 = s.symbols("A11 A12 A22", real=True)
    x = R**-2

    # Binomial sums after extracting the positive factor (1-x)^(ell-2).
    F0 = (1 - x) ** 2
    F1 = -ell * x * (1 - x)
    F2 = ell * (ell - 1) * x**2 - ell * x * (1 - x)
    rows = []
    for m in range(2):
        row = []
        for n in range(2):
            am, an = m + 1, n + 1
            entry = A11 * (am * an * F0 + (am + an) * F1 + F2)
            entry += A12 * R * (
                (am * (an - 1) + (am - 1) * an) * F0
                + (2 * am + 2 * an - 2) * F1
                + 2 * F2
            )
            entry += A22 * R**2 * (
                (am - 1) * (an - 1) * F0
                + (am + an - 2) * F1
                + F2
            )
            row.append(s.expand(entry))
        rows.append(row)
    determinant = s.factor(s.Matrix(rows).det())
    slope = s.factor(s.Poly(determinant, ell).coeff_monomial(ell))
    expected_slope = -(R**2 - 1) ** 2 * (
        A11 + 2 * R * A12 + R**2 * A22
    ) ** 2 / R**6
    assert s.factor(slope - expected_slope) == 0

    # At the physical repeated root, the square is strictly nonzero.
    c, Y = s.symbols("c Y", positive=True)
    b = R**2
    a22 = -(b**3 - 4 * b**2 * c - 3 * b**2 + 3 * b - 1) / (b + 1)
    a11 = 4 * b * c - a22
    a12 = -2 * R * c * (R**2 + 1) / (c + 2)
    J = s.factor(a11 + 2 * R * a12 + R**2 * a22)
    K = (
        -(c + 2) * (R**8 + 1)
        + 4 * (c**2 + 2 * c + 2) * (R**6 + R**2)
        - (14 * c + 12) * R**4
    )
    assert s.factor(J - K / ((R**2 + 1) * (c + 2))) == 0
    K_over_R4 = (
        -(c + 2) * (Y**4 - 4 * Y**2 + 2)
        + 4 * (c**2 + 2 * c + 2) * (Y**2 - 2)
        - (14 * c + 12)
    )
    Y2 = 4 * (c + 2) ** 2 / (c + 4)
    assert s.factor(K_over_R4.subs(Y**2, Y2) - 8 * c**2 * (c + 2) ** 2 / (c + 4) ** 2) == 0


if __name__ == "__main__":
    unequal_weight_checks()
    equal_weight_checks()
    repeated_pole_checks()
    print("all exact weighted two-atom identities verified")
