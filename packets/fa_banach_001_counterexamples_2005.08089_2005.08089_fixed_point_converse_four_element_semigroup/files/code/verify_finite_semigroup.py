#!/usr/bin/env python3
"""Exact finite check for the counterexample to Remark 5.3.

The proof in the packet is conceptual.  This script independently checks the
four-element multiplication table, the character identity, the right-zero
kernel, and inconsistency of the normalized right-phi invariant-functional
equations.  All linear algebra is over the rational numbers.
"""

from fractions import Fraction


ELEMENTS = tuple((eps, index) for eps in (0, 1) for index in (0, 1))


def multiply(left, right):
    eps, _ = left
    delta, index = right
    return ((eps + delta) % 2, index)


def phi(element):
    return Fraction(1 if element[0] == 0 else -1)


def rank(matrix):
    """Return the rank of a rational matrix by Gauss-Jordan elimination."""
    work = [list(map(Fraction, row)) for row in matrix]
    if not work:
        return 0
    row = 0
    for col in range(len(work[0])):
        pivot = next((r for r in range(row, len(work)) if work[r][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][col]
        work[row] = [value / scale for value in work[row]]
        for other in range(len(work)):
            if other != row and work[other][col]:
                scale = work[other][col]
                work[other] = [
                    value - scale * pivot_value
                    for value, pivot_value in zip(work[other], work[row])
                ]
        row += 1
        if row == len(work):
            break
    return row


def invariant_system():
    """Build A mu=b for m(R_s f)=phi(s)m(f), m(phi)=1."""
    rows = []
    rhs = []
    for s in ELEMENTS:
        # Equality for every f is equality of the coefficient of each f(y).
        for y in ELEMENTS:
            row = []
            for x in ELEMENTS:
                row.append(
                    Fraction(multiply(x, s) == y)
                    - phi(s) * Fraction(x == y)
                )
            rows.append(row)
            rhs.append(Fraction(0))
    rows.append([phi(x) for x in ELEMENTS])
    rhs.append(Fraction(1))
    return rows, rhs


def main():
    assert all(
        multiply(multiply(x, y), z) == multiply(x, multiply(y, z))
        for x in ELEMENTS
        for y in ELEMENTS
        for z in ELEMENTS
    )
    assert all(
        phi(multiply(x, y)) == phi(x) * phi(y)
        for x in ELEMENTS
        for y in ELEMENTS
    )

    kernel = tuple(x for x in ELEMENTS if phi(x) == 1)
    assert kernel == ((0, 0), (0, 1))
    assert all(multiply(x, y) == y for x in kernel for y in kernel)

    rows, rhs = invariant_system()
    coefficient_rank = rank(rows)
    augmented_rank = rank([row + [value] for row, value in zip(rows, rhs)])
    assert augmented_rank > coefficient_rank

    print("associativity: PASS (64 triples)")
    print("character identity: PASS (16 pairs)")
    print("P(phi) is the two-element right-zero semigroup: PASS")
    print(
        "normalized right-phi invariant functional: IMPOSSIBLE "
        f"(rank {coefficient_rank} < augmented rank {augmented_rank})"
    )


if __name__ == "__main__":
    main()
