"""Optional numerical check of the clamped-beam constant (not used in proof)."""

from math import cos, cosh, pi


def characteristic(x):
    return cos(x) * cosh(x) - 1


left, right = 4.7, 4.8
assert characteristic(left) < 0 < characteristic(right)
for _ in range(80):
    middle = (left + right) / 2
    if characteristic(middle) < 0:
        left = middle
    else:
        right = middle

beta = (left + right) / 2
c20 = pi * pi / (beta * beta)
assert beta > pi
assert c20 < 1
print("first positive clamped-beam root beta ~=", beta)
print("C_20(0,pi) = pi^2/beta^2 ~=", c20)
print("C_10(0,pi)^2 = 1")

