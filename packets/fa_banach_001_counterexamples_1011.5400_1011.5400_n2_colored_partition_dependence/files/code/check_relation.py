"""Direct tensor-coordinate audit of the 11-diagram relation at n=2."""

from itertools import product


# A diagram is a tuple of blocks; a block lists (point, color) pairs.
# Points are zero-based and colors are 0=w, 1=b.  Each block is understood
# modulo simultaneous color reversal, exactly as in the source definition.
RELATION = (
    (+2, (((0, 0), (1, 1), (2, 0), (3, 1), (4, 0), (5, 1)),)),
    (+2, (((0, 0), (1, 1), (2, 0), (3, 1), (4, 1), (5, 0)),)),
    (+2, (((0, 0), (1, 1), (2, 1), (3, 0), (4, 0), (5, 1)),)),
    (+2, (((0, 0), (1, 1), (2, 1), (3, 0), (4, 1), (5, 0)),)),
    (-1, (((0, 0), (1, 1), (2, 0), (3, 1)), ((4, 0), (5, 1)))),
    (-1, (((0, 0), (1, 1), (2, 1), (3, 0)), ((4, 0), (5, 1)))),
    (-1, (((0, 0), (1, 1), (4, 0), (5, 1)), ((2, 0), (3, 1)))),
    (-1, (((0, 0), (1, 1), (4, 1), (5, 0)), ((2, 0), (3, 1)))),
    (-1, (((0, 0), (1, 1)), ((2, 0), (3, 1), (4, 0), (5, 1)))),
    (-1, (((0, 0), (1, 1)), ((2, 0), (3, 1), (4, 1), (5, 0)))),
    (+1, (((0, 0), (1, 1)), ((2, 0), (3, 1)), ((4, 0), (5, 1)))),
)


def bar(index):
    base, color = index
    return base, 1 - color


def diagram_coefficient(diagram, assignment):
    for block in diagram:
        point0, color0 = block[0]
        root = assignment[point0] if color0 == 0 else bar(assignment[point0])
        for point, color in block:
            expected = root if color == 0 else bar(root)
            if assignment[point] != expected:
                return 0
    return 1


indices = tuple(product(range(2), range(2)))
nonzero_terms_seen = set()
for assignment in product(indices, repeat=6):
    terms = [coefficient * diagram_coefficient(diagram, assignment) for coefficient, diagram in RELATION]
    total = sum(terms)
    assert total == 0, (assignment, terms, total)
    nonzero_terms_seen.update(i for i, term in enumerate(terms) if term)

assert len(nonzero_terms_seen) == len(RELATION)
print("PASS: all 4^6=4096 tensor coordinates satisfy the 11-diagram relation.")
print("PASS: every one of the 11 diagrams occurs with a nonzero coordinate.")
