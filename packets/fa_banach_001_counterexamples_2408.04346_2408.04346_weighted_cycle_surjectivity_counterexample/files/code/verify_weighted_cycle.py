from fractions import Fraction
from itertools import permutations

n = 6
weights = [Fraction(1, 3), Fraction(2, 3)] * 3
P = [[Fraction(0) for _ in range(n)] for _ in range(n)]
for i, w in enumerate(weights):
    j = (i + 1) % n
    P[i][j] = w
    P[j][i] = w

assert P == [list(row) for row in zip(*P)]
assert all(sum(row) == 1 for row in P)
assert all(P[i][j] >= 0 for i in range(n) for j in range(n))

def allowed(i, j):
    return (i - j) % n in (1, n - 1)

compatible = []
images = []
for perm in permutations(range(n)):
    if not all(allowed(i, perm[i]) for i in range(n)):
        continue
    compatible.append(perm)
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i, j in enumerate(perm):
        A[i][j] = 1
    Q = [
        [(A[i][j] + A[j][i]) / 2 for j in range(n)]
        for i in range(n)
    ]
    images.append(Q)

assert len(compatible) == 4
assert all(
    qij in (Fraction(0), Fraction(1, 2), Fraction(1))
    for Q in images for row in Q for qij in row
)
assert all(Q != P for Q in images)

print("symmetric_doubly_stochastic=true")
print("cycle_supported_permutations=4")
print("all_image_entries_in={0,1/2,1}")
print("weighted_cycle_in_image=false")

