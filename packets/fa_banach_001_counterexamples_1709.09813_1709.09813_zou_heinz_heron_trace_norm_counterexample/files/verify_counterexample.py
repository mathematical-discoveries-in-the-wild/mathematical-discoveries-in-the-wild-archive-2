"""Exact-rational interval certificate for the 2x2 trace-norm counterexample."""

from __future__ import annotations

from fractions import Fraction as F
from math import factorial

I = tuple[F, F]


def add(a: I, b: I) -> I:
    return a[0] + b[0], a[1] + b[1]


def neg(a: I) -> I:
    return -a[1], -a[0]


def sub(a: I, b: I) -> I:
    return add(a, neg(b))


def mul(a: I, b: I) -> I:
    vals = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(vals), max(vals)


def exact(x: F) -> I:
    return x, x


def cosh_interval(x: F, n: int = 24) -> I:
    x = abs(x)
    lo = sum((x ** (2 * j)) / factorial(2 * j) for j in range(n + 1))
    first = (x ** (2 * n + 2)) / factorial(2 * n + 2)
    ratio = x * x / ((2 * n + 4) * (2 * n + 3))
    return lo, lo + first / (1 - ratio)


def sum_i(xs) -> I:
    out = exact(F(0))
    for x in xs:
        out = add(out, x)
    return out


def trace_norm_square(m: list[list[I]]) -> tuple[I, I]:
    """Return interval for ||m||_1^2 and det(m), assuming real 2x2 m."""
    frob2 = sum_i(mul(x, x) for row in m for x in row)
    det = sub(mul(m[0][0], m[1][1]), mul(m[0][1], m[1][0]))
    assert det[0] > 0
    return add(frob2, mul(exact(F(2)), det)), det


def fmt(x: F) -> str:
    return f"{float(x):.16g}"


def main() -> None:
    h = [F(3, 10), F(13, 10)]
    k = [F(0), F(9, 10)]
    s = F(7, 10)
    t0 = [[F(5, 10), F(-8, 10)], [F(-1, 10), F(4, 10)]]

    def scaled(scale: F) -> list[list[I]]:
        return [
            [mul(exact(t0[i][j]), cosh_interval(scale * (h[i] - k[j]))) for j in range(2)]
            for i in range(2)
        ]

    t = [[exact(x) for x in row] for row in t0]
    y = scaled(s)
    z = scaled(F(1))
    t_sq, t_det = trace_norm_square(t)
    y_sq, y_det = trace_norm_square(y)
    z_sq, z_det = trace_norm_square(z)

    q_y = F(589, 500)       # 1.178
    q_t = F(5701, 5000)     # 1.1402
    q_z = F(12153, 10000)   # 1.2153
    assert y_sq[0] > q_y * q_y
    assert t_sq[1] < q_t * q_t
    assert z_sq[1] < q_z * q_z

    rhs = (1 - s * s) * q_t + s * s * q_z
    margin = q_y - rhs
    assert margin > 0

    print("CERTIFIED")
    print("det(Y) lower bound:", fmt(y_det[0]))
    print("det(Z) lower bound:", fmt(z_det[0]))
    print("square margin proving ||Y||_1 > 1.178:", fmt(y_sq[0] - q_y * q_y))
    print("square margin proving ||T||_1 < 1.1402:", fmt(q_t * q_t - t_sq[1]))
    print("square margin proving ||Z||_1 < 1.2153:", fmt(q_z * q_z - z_sq[1]))
    print("RHS strict upper bound:", fmt(rhs))
    print("final certified norm margin:", fmt(margin), f"({margin.numerator}/{margin.denominator})")


if __name__ == "__main__":
    main()
