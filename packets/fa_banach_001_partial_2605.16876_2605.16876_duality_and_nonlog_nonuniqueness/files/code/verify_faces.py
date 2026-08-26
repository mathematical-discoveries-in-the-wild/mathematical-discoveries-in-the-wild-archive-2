#!/usr/bin/env python3
"""Interval certificate for the Poincare--Miranda face signs.

This verifies the explicit s=1/100 example in the accompanying packet.  All
rectangle endpoints and subdivisions are created from exact decimal strings;
mpmath.iv performs outward-rounded interval arithmetic.
"""

from decimal import Decimal, getcontext

from mpmath import iv


iv.dps = 50
getcontext().prec = 50

ZERO = iv.mpf("0")
ONE = iv.mpf("1")
S_PARAM = iv.mpf("0.01")


def matmul(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(2)), ZERO) for j in range(2)]
        for i in range(2)
    ]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def tanh_interval(x):
    e2x = iv.exp(2 * x)
    return (e2x - ONE) / (e2x + ONE)


def exp_traceless(u, v):
    """exp(u*S+v*T), where S^2=T^2=I and ST=-TS."""

    radius = iv.sqrt(u * u + v * v)
    er = iv.exp(radius)
    em = iv.exp(-radius)
    cosh_r = (er + em) / 2
    sinh_over_r = (er - em) / (2 * radius)
    return [
        [cosh_r + sinh_over_r * u, sinh_over_r * v],
        [sinh_over_r * v, cosh_r - sinh_over_r * u],
    ]


def build_data(s):
    if s is None:
        x0 = exp_traceless(iv.mpf("3"), ZERO)
        b_matrices = [
            x0,
            exp_traceless(ZERO, iv.mpf("1.9")),
            exp_traceless(iv.mpf("-3"), iv.mpf("-1.9")),
        ]
        return [matmul(matmul(b, x0), b) for b in b_matrices]

    a_s = (2 / s) * tanh_interval(3 * s / 2)
    b_s = (2 / s) * tanh_interval(iv.mpf("1.9") * s / 2)
    r_s = iv.sqrt(a_s * a_s + b_s * b_s)
    q = s * r_s / 2
    q_s = iv.log((ONE + q) / (ONE - q)) / s
    u3 = -q_s * a_s / r_s
    v3 = -q_s * b_s / r_s

    x0 = exp_traceless(iv.mpf("3"), ZERO)
    b_matrices = [
        x0,
        exp_traceless(ZERO, iv.mpf("1.9")),
        exp_traceless(u3, v3),
    ]
    return [matmul(matmul(b, x0), b) for b in b_matrices]


def face_function(u, v, s, data):
    """Return interval enclosures for (F1_s(u,v), F2_s(u,v))."""

    x_inverse = exp_traceless(-u, -v)
    f1 = ZERO
    f2 = ZERO
    for a in data:
        m = matadd(a, x_inverse)
        determinant = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        root_det = iv.sqrt(determinant)
        geometric = [[m[i][j] / root_det for j in range(2)] for i in range(2)]

        t = (geometric[0][0] + geometric[1][1]) / 2
        z = iv.sqrt(t * t - ONE)
        hyperbolic_radius = iv.log(t + z)
        if s is None:
            coefficient = hyperbolic_radius / z
        else:
            coefficient = (2 / s) * tanh_interval(s * hyperbolic_radius / 2) / z
        f1 += coefficient * (geometric[0][0] - geometric[1][1]) / 6
        f2 += coefficient * geometric[0][1] / 3
    return f1, f2


def decimal_interval(left, right):
    return iv.mpf([str(left), str(right)])


def certify_face(side, s, data, subdivisions=8000):
    u_min = Decimal("1.61247432825")
    u_max = Decimal("1.62347432825")
    v_min = Decimal("0.5194188906")
    v_max = Decimal("0.5254188906")
    count = Decimal(subdivisions)

    global_lower = float("inf")
    global_upper = float("-inf")
    failures = 0

    for index in range(subdivisions):
        fraction_left = Decimal(index) / count
        fraction_right = Decimal(index + 1) / count
        if side in ("u-", "u+"):
            u = iv.mpf(str(u_min if side == "u-" else u_max))
            left = v_min + (v_max - v_min) * fraction_left
            right = v_min + (v_max - v_min) * fraction_right
            v = decimal_interval(left, right)
            value = face_function(u, v, s, data)[0]
        else:
            v = iv.mpf(str(v_min if side == "v-" else v_max))
            left = u_min + (u_max - u_min) * fraction_left
            right = u_min + (u_max - u_min) * fraction_right
            u = decimal_interval(left, right)
            value = face_function(u, v, s, data)[1]

        lower = float(value.a)
        upper = float(value.b)
        global_lower = min(global_lower, lower)
        global_upper = max(global_upper, upper)

        should_be_positive = side in ("u-", "v-")
        if (should_be_positive and lower <= 0) or (
            not should_be_positive and upper >= 0
        ):
            failures += 1

    return global_lower, global_upper, failures


def main():
    all_results = {}
    for label, s in (("log", None), ("s=1/100", S_PARAM)):
        data = build_data(s)
        results = {}
        print(label)
        for side in ("u-", "u+", "v-", "v+"):
            results[side] = certify_face(side, s, data)
            lower, upper, failures = results[side]
            print(
                f"  {side}: enclosure=[{lower:.16g}, {upper:.16g}], "
                f"failures={failures}"
            )
        assert all(result[2] == 0 for result in results.values())
        all_results[label] = results

    results = all_results["s=1/100"]
    assert results["u-"][0] > 1.5e-4
    assert results["u+"][1] < -7.5e-5
    assert results["v-"][0] > 1.1e-4
    assert results["v+"][1] < -2.7e-5
    print("certified: all four Poincare--Miranda face signs have strict margin")


if __name__ == "__main__":
    main()
