"""Exact symbolic verification of the kappa=3, n=2 orbit counterexample."""

from sympy import Matrix, eye, zeros


e1 = Matrix([1, 0, 0])
e2 = Matrix([0, 1, 0])
e3 = Matrix([0, 0, 1])

# Each matrix is specified by its three columns.  Its first two columns give
# one of the six orbit points used in the proof packet.
rotations = [
    Matrix.hstack(e1, e2, e3),
    Matrix.hstack(e1, -e2, -e3),
    Matrix.hstack(e2, e3, e1),
    Matrix.hstack(e2, -e3, -e1),
    Matrix.hstack(e3, e1, e2),
    Matrix.hstack(e3, -e1, -e2),
]

for sigma in rotations:
    assert sigma.T * sigma == eye(3)
    assert sigma.det() == 1

orbit_vectors = [Matrix.vstack(sigma[:, 0], sigma[:, 1]) for sigma in rotations]
orbit_matrix = Matrix.hstack(*orbit_vectors)

assert orbit_matrix.rank() == 6
assert Matrix.hstack(e1, e2).rank() == 2

expected_basis = [
    Matrix.vstack(e1, zeros(3, 1)),
    Matrix.vstack(e2, zeros(3, 1)),
    Matrix.vstack(e3, zeros(3, 1)),
    Matrix.vstack(zeros(3, 1), e1),
    Matrix.vstack(zeros(3, 1), e2),
    Matrix.vstack(zeros(3, 1), e3),
]
for vector in expected_basis:
    assert orbit_matrix.row_join(vector).rank() == 6

print("all six rotations lie in SO(3)")
print("rank(X) = 2")
print("dimension of orbit span = 6")

