"""Exact rational transcription check for the isolated-point obstruction."""

from fractions import Fraction


a = Fraction(1, 4)
b = Fraction(3, 4)
c = Fraction(1, 2)
trace = -a + b * c

# Row norms of I + T^2 at p, q, and any other point, respectively.
row_p = abs(1 - trace * a) + trace * b
row_q = trace * c * a + abs(1 + trace * c * b)
row_other_bound = 1 + trace * c * (a + b)

operator_norm = max(row_p, row_q, row_other_bound)
rhs = 1 + trace

print(f"trace(T)={trace}")
print(f"row_p={row_p}, row_q={row_q}, row_other_bound={row_other_bound}")
print(f"||I+T^2||={operator_norm}, 1+||T^2||={rhs}, gap={rhs-operator_norm}")

assert trace == Fraction(1, 8)
assert operator_norm == Fraction(17, 16)
assert rhs == Fraction(9, 8)
assert rhs - operator_norm == Fraction(1, 16)
