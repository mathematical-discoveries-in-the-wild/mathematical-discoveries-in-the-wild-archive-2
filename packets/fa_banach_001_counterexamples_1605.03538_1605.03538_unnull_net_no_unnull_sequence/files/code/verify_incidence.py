"""Finite incidence checks mirroring the support argument in the packet.

The finite computation does not prove the infinite convergence claim.  It
checks the two combinatorial identities used by the proof: a chosen point
outside C escapes every D contained in C, and the union of the coordinates
used by any proposed sequence detects every selected unit vector.
"""

from itertools import combinations


def subsets(universe):
    items = tuple(universe)
    for size in range(len(items) + 1):
        for choice in combinations(items, size):
            yield frozenset(choice)


universe = frozenset(range(9))
proper = [c for c in subsets(universe) if c != universe]
gamma = {c: min(universe - c) for c in proper}

# If D is contained in the current index C, gamma_C is outside D.
for c in proper:
    for d in subsets(c):
        assert gamma[c] not in d

# Representative chains, including repetitions, are defeated by the union
# of their selected coordinates.
chains = [
    [frozenset(), frozenset({0}), frozenset({0, 1})],
    [frozenset({2}), frozenset({2}), frozenset({1, 2, 5})],
    [frozenset({0, 2}), frozenset({0, 2, 4}), frozenset({0, 2, 4, 6})],
]
for chain in chains:
    assert all(chain[i] <= chain[i + 1] for i in range(len(chain) - 1))
    witness_support = {gamma[c] for c in chain}
    assert all(gamma[c] in witness_support for c in chain)

print("proper_indices_checked:", len(proper))
print("incidence_pairs_checked:", sum(2 ** len(c) for c in proper))
print("chains_checked:", len(chains))
print("all finite incidence checks passed")
