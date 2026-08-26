#!/usr/bin/env python3
"""Exact certificate for K_2 < 313/1000.

This script uses only Python's standard-library Fraction class.  It expands
Q=psi/(1-a psi) through total degree eight by the denominator recurrence and
checks that the corresponding finite Bohr subsum of
F=(a-psi)/(1-a psi)=a-(1-a^2)Q exceeds one at r=313/1000.
"""

from fractions import Fraction as F

X = F(1, 6)
Y = 1 - X
A = F(999, 1000)
R = F(313, 1000)
MAX_DEGREE = 8

# If psi=N/P, then Q=N/(P-aN)=N/D, with
# N=zw-Xw-Yz and D=1+A_Z*z+A_W*w-A*zw.
A_Z = -X + A * Y
A_W = -Y + A * X


def numerator_coefficient(m: int, n: int) -> F:
    if (m, n) == (1, 1):
        return F(1)
    if (m, n) == (0, 1):
        return -X
    if (m, n) == (1, 0):
        return -Y
    return F(0)


def coefficients():
    q = {}
    layer_l1 = {}
    for total in range(1, MAX_DEGREE + 1):
        layer_l1[total] = F(0)
        for m in range(total + 1):
            n = total - m
            value = numerator_coefficient(m, n)
            if m:
                value -= A_Z * q.get((m - 1, n), F(0))
            if n:
                value -= A_W * q.get((m, n - 1), F(0))
            if m and n:
                value += A * q.get((m - 1, n - 1), F(0))
            q[m, n] = value
            layer_l1[total] += abs(value)
    return q, layer_l1


def main() -> None:
    q, layer_l1 = coefficients()

    # Independent recurrence residual check for every coefficient.
    for total in range(1, MAX_DEGREE + 1):
        for m in range(total + 1):
            n = total - m
            lhs = q[m, n]
            lhs += A_Z * q.get((m - 1, n), F(0))
            lhs += A_W * q.get((m, n - 1), F(0))
            lhs -= A * q.get((m - 1, n - 1), F(0))
            assert lhs == numerator_coefficient(m, n), (m, n, lhs)

    expected_layers = {
        1: F(1),
        2: F(21983, 18000),
        3: F(18642677, 12000000),
        4: F(950105595503, 648000000000),
        5: F(4751192992371613, 3888000000000000),
        6: F(39242182643309639173, 23328000000000000000),
        7: F(2191652817952769393981, 1093500000000000000000),
        8: F(
            1463094271925643860042526233,
            839808000000000000000000000,
        ),
    }
    assert layer_l1 == expected_layers

    weighted_sum = sum(layer_l1[k] * R**k for k in layer_l1)
    threshold = F(1, 1 + A)
    bohr_subsum = A + (1 - A * A) * weighted_sum
    expected_weighted_sum = F(
        420207945895146052725713514433991908771800854450393,
        839808000000000000000000000000000000000000000000000,
    )
    expected_margin = F(
        187683844396959398701315353549825634829908046335607,
        839808000000000000000000000000000000000000000000000000000,
    )
    assert weighted_sum == expected_weighted_sum
    assert weighted_sum > threshold
    assert bohr_subsum - 1 == expected_margin

    print(f"x={X}, a={A}, r={R}, max_degree={MAX_DEGREE}")
    for k in sorted(layer_l1):
        print(f"T_{k}={layer_l1[k]}")
    print(f"S_8={weighted_sum}")
    print(f"1/(1+a)={threshold}")
    print(f"Bohr finite subsum={bohr_subsum}")
    print(f"strict margin={expected_margin}")
    print("PASS: exact finite certificate proves K_2 < 313/1000")


if __name__ == "__main__":
    main()
