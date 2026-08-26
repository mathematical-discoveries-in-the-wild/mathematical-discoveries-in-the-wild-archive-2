"""Exact symbolic verification of the rational counterexample."""

from sympy import Matrix, Rational


e1 = Matrix([[1, 0, 0]])
e2 = Matrix([[0, 1, 0]])
e3 = Matrix([[0, 0, 1]])
f = Matrix([[Rational(-4, 7), Rational(2, 7), Rational(6, 7)]])

source = Matrix(
    [
        [1, Rational(3, 4), -1],
        [-1, 1, -1],
        [Rational(-1, 6), -1, Rational(5, 6)],
    ]
)
target = Matrix(
    [
        [1, 1, -1],
        [1, -1, 1],
        [Rational(-5, 6), 1, Rational(1, 6)],
    ]
)
operator = Matrix([[4, -2, -6], [0, -7, 0], [-16, -6, -25]]) / 7

gx = [
    e1.col_join(-e2).col_join(-f),
    e2.col_join(-e3).col_join(-f),
    (-e1).col_join(-e2).col_join(f),
]
gy = [
    e1.col_join(e2).col_join(-f),
    e1.col_join(-e2).col_join(e3),
    (-e1).col_join(e2).col_join(f),
]

expected_13 = Matrix([[Rational(3, 4), 0, Rational(1, 4)], [0, 1, 0], [1, 0, 0]])
expected_2 = Matrix([[0, 1, 0], [Rational(4, 7), Rational(2, 7), Rational(1, 7)], [1, 0, 0]])

assert source.det() == Rational(-7, 12)
assert operator.det() == 4
assert operator * source == target
assert gx[0] * operator.inv() * gy[0].inv() == expected_13
assert gx[1] * operator.inv() * gy[1].inv() == expected_2
assert gx[2] * operator.inv() * gy[2].inv() == expected_13

p = Matrix([1, 1, 1])
tp = operator * p
assert tp == Matrix([Rational(-4, 7), -1, Rational(-47, 7)])
functionals = [e1, e2, e3, f, -e1, -e2, -e3, -f]
assert max((row * tp)[0] for row in functionals) == Rational(47, 7)

print("exact counterexample verification passed")
