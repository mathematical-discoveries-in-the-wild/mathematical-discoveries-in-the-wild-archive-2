"""Exact audit for the arXiv:2108.05873 reverse-order counterexample."""

from sympy import Matrix, diag


J = diag(1, 1, -1)
u = Matrix([1, 0, 0])
v = Matrix([1, 1, 1])


def sharp(matrix: Matrix) -> Matrix:
    """J-adjoint, with the same weight J on domain and codomain."""
    return J * matrix.T * J


B = u * (u.T * J)
A = v * (v.T * J)
D = A * B
X = B * A

zero = Matrix.zeros(3)
assert A * A == A and B * B == B
assert sharp(A) == A and sharp(B) == B

# X is the indefinite Moore-Penrose inverse of D=AB.
assert D * X * D == D
assert X * D * X == X
assert sharp(D * X) == D * X
assert sharp(X * D) == X * D
assert X == B * A  # B^[dagger] A^[dagger], since A and B are projections.

# Theorem 3.5(i) fails: D=A^[*]ABB^[*] is not range Hermitian.
assert sharp(A) * A * B * sharp(B) == D
assert sharp(D) == X
assert D.row_join(sharp(D)).rank() == 2
assert D.rank() == 1

# Theorem 3.5(iv) fails entrywise.
first_lhs = B * B * sharp(A) * A * B
first_rhs = sharp(A) * A * B
second_lhs = A * A * B * sharp(B) * sharp(A)
second_rhs = B * sharp(B) * sharp(A)
assert first_lhs != first_rhs
assert second_lhs != second_rhs

# The rank hypothesis in Theorem 3.16 fails as 1 != 2.
block = (sharp(B) * sharp(A)).row_join(sharp(B) * B).col_join(
    (A * sharp(A)).row_join(A * B)
)
right = sharp(A).row_join(B)
assert block.rank() == 1
assert right.rank() == 2

print("all exact checks passed")
print("rank(block) =", block.rank())
print("rank([A^[*] B]) =", right.rank())

