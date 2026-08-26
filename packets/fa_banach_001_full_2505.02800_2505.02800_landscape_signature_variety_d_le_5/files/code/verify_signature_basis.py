#!/usr/bin/env python3
"""Exact certificate for Conjecture 4.3 of arXiv:2505.02800.

For a finite barcode B, its persistence landscape is the decreasing rearrangement
of the tent functions h_[b,e](t)=max(0,min(t-b,e-t)).  This script inserts every
tent kink and every crossing of two affine tent pieces, so the resulting list is
the exact vertex list of the landscape path.  It then uses the polygon formula

  S_ij(B) = 1/2 sum_r (v_r[i] v_{r+1}[j] - v_r[j] v_{r+1}[i])

for the skew coordinates of its second Chen signature.  All arithmetic is in
fractions; no numerical tolerance or third-party package is used.
"""

from fractions import Fraction as Q
from itertools import combinations


# A hierarchical certificate: the first C(d,2) barcodes have at most d intervals.
BARCODES = (
    ((0, 14), (7, 11)),
    ((1, 13), (4, 9), (2, 14)),
    ((3, 15), (0, 14), (4, 9)),
    ((6, 9), (4, 16), (2, 15), (0, 14)),
    ((6, 15), (2, 14), (0, 11), (7, 17)),
    ((1, 9), (3, 16), (7, 15), (6, 12)),
    ((4, 9), (2, 14), (0, 10), (7, 17), (1, 16)),
    ((0, 17), (4, 16), (6, 10), (7, 12), (5, 15)),
    ((2, 11), (1, 16), (5, 17), (7, 9), (0, 14)),
    ((2, 17), (4, 14), (5, 15), (0, 16), (1, 9)),
)

EXPECTED_DETERMINANTS = {
    2: Q(4),
    3: Q(44),
    4: Q(-781, 8),
    5: Q(-667755, 2048),
}


def affine_piece(interval, t):
    """Return slope/intercept of a tent on the open base cell containing t."""
    b, e = map(Q, interval)
    midpoint = (b + e) / 2
    if t < b or t > e:
        return Q(0), Q(0)
    if t < midpoint:
        return Q(1), -b
    return Q(-1), e


def tent(interval, t):
    b, e = map(Q, interval)
    return max(Q(0), min(t - b, e - t))


def landscape_vertices(barcode, ambient_dimension):
    """Return all exact vertices of the padded persistence-landscape path."""
    base = sorted(
        {x for b0, e0 in barcode for x in (Q(b0), (Q(b0) + Q(e0)) / 2, Q(e0))}
    )
    breakpoints = set(base)

    # On each base cell every tent is affine.  Insert all ordering changes.
    for left, right in zip(base[:-1], base[1:]):
        probe = (left + right) / 2
        pieces = [affine_piece(interval, probe) for interval in barcode]
        for (s1, c1), (s2, c2) in combinations(pieces, 2):
            if s1 == s2:
                continue
            crossing = (c2 - c1) / (s1 - s2)
            if left < crossing < right:
                breakpoints.add(crossing)

    vertices = []
    for t in sorted(breakpoints):
        levels = sorted((tent(interval, t) for interval in barcode), reverse=True)
        levels.extend([Q(0)] * (ambient_dimension - len(levels)))
        vertices.append(tuple(levels))

    assert vertices[0] == (Q(0),) * ambient_dimension
    assert vertices[-1] == (Q(0),) * ambient_dimension
    return vertices


def second_signature_vector(barcode, ambient_dimension):
    vertices = landscape_vertices(barcode, ambient_dimension)
    coordinates = []
    for i in range(ambient_dimension):
        for j in range(i + 1, ambient_dimension):
            coordinates.append(
                sum(
                    (x[i] * y[j] - x[j] * y[i]) / 2
                    for x, y in zip(vertices[:-1], vertices[1:])
                )
            )
    return tuple(coordinates)


def determinant(matrix):
    """Exact Gaussian-elimination determinant over the rationals."""
    a = [list(map(Q, row)) for row in matrix]
    n = len(a)
    det = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col]
        det *= pivot_value
        for j in range(col, n):
            a[col][j] /= pivot_value
        for r in range(col + 1, n):
            factor = a[r][col]
            if factor:
                for j in range(col, n):
                    a[r][j] -= factor * a[col][j]
    return det


def show(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def main():
    for d in range(2, 6):
        size = d * (d - 1) // 2
        rows = [second_signature_vector(b, d) for b in BARCODES[:size]]
        det = determinant(rows)
        assert det == EXPECTED_DETERMINANTS[d]
        print(f"d={d}; coordinate order=" + ",".join(f"{i}{j}" for i in range(1, d + 1) for j in range(i + 1, d + 1)))
        for k, (barcode, row) in enumerate(zip(BARCODES[:size], rows), 1):
            print(f"B{k}={barcode}; S=(" + ", ".join(map(show, row)) + ")")
        print(f"det={show(det)}; rank={size}")
        print()

    print("PASS: the displayed landscape signatures span wedge^2 R^d for d=2,3,4,5.")


if __name__ == "__main__":
    main()
