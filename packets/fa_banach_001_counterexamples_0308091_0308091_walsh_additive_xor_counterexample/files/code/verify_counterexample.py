"""Exact verifier for the arXiv:math/0308091 B-conjecture counterexample."""

from __future__ import annotations


Q = (
    0, 1, 2, 3, 4, 11, 10, 9,
    8, 15, 14, 13, 12, 19, 18, 5,
    16, 7, 6, 25, 24, 27, 26, 29,
    28, 31, 30, 17, 22, 23, 20, 21,
)

EXPECTED_HISTOGRAM = (
    1, 2, 2, 4, 2, 2, 4, 4,
    8, 4, 6, 6, 10, 2, 4, 6,
    6, 12, 10, 6, 6, 10, 12, 8,
    8, 12, 14, 10, 8, 14, 14, 32,
)


def score(p):
    size = len(p)
    return sum(
        (p[x] ^ p[y]) == p[x + y]
        for x in range(size)
        for y in range(size - x)
    )


def histogram(p):
    return tuple(
        sum((p[x] ^ p[s - x]) == p[s] for x in range(s + 1))
        for s in range(len(p))
    )


def a_score(p):
    size = len(p)
    total = 0
    for x in range(size):
        for y in range(size):
            for z in range(size):
                w = x + y - z
                if 0 <= w < size and (p[x] ^ p[y] ^ p[z]) == p[w]:
                    total += 1
    return total


assert sorted(Q) == list(range(32))
assert histogram(Q) == EXPECTED_HISTOGRAM
assert sum(EXPECTED_HISTOGRAM) == 249
assert score(Q) == 249 > 3**5
assert score(tuple(range(32))) == 3**5 == 243
assert a_score(Q) == 6912 < 7776 == 6**5

for n in range(5, 11):
    lifted = tuple(Q[x % 32] + 32 * (x // 32) for x in range(1 << n))
    assert sorted(lifted) == list(range(1 << n))
    observed = score(lifted)
    predicted = 249 * 3 ** (n - 5)
    assert observed == predicted, (n, observed, predicted)
    print(f"n={n}: score={observed}, conjectured_bound={3**n}")

print("PASS: base histogram, permutation, lift, and scope checks are exact")
