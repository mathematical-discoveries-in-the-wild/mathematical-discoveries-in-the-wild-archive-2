"""Exact certificate for the counterexample to Remark 4.2 of arXiv:2207.04830.

Coordinates are scaled by lambda.  A point is represented by (a,b,alpha,beta),
where x=a*lambda*u, y=b*lambda*v, alpha=<z,u>/lambda, and
beta=<z,v>/lambda.  Dividing the cost by lambda^2 gives

    c(a,b,alpha,beta) = a*b/2 + a*alpha + b*beta.

For a contact point, (a,b) maximizes this expression over [-1,1]^2;
checking the four vertices is sufficient.
"""

from fractions import Fraction as Q
from itertools import product


def cost(a: Q, b: Q, alpha: Q, beta: Q) -> Q:
    return a * b / 2 + a * alpha + b * beta


vertices = tuple(product((Q(-1), Q(1)), repeat=2))
zero = (Q(0), Q(0), Q(0), Q(0))
p1 = (Q(-1, 2), Q(1), Q(-1, 2), Q(1, 2))
p2 = (Q(1), Q(-1, 2), Q(1, 2), Q(-1, 2))
points = (zero, p1, p2)

for point in (p1, p2):
    a, b, alpha, beta = point
    attained = cost(a, b, alpha, beta)
    vertex_max = max(cost(s, t, alpha, beta) for s, t in vertices)
    assert attained == vertex_max == Q(1, 2)

original = sum(cost(*p) for p in points)

# sigma_x swaps 0 and 1; sigma_y swaps 0 and 2; sigma_z is the identity.
sigma_x = (1, 0, 2)
sigma_y = (2, 1, 0)
permuted = sum(
    cost(points[sigma_x[j]][0], points[sigma_y[j]][1], points[j][2], points[j][3])
    for j in range(3)
)

assert original == Q(1)
assert permuted == Q(9, 8)
assert permuted - original == Q(1, 8)

print(f"contact values: {cost(*p1)}, {cost(*p2)}")
print(f"original sum: {original}")
print(f"permuted sum: {permuted}")
print(f"violation: {permuted - original}")
