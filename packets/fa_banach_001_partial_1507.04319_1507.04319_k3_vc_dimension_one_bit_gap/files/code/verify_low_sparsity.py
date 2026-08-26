#!/usr/bin/env python3
"""Finite checks for the low-sparsity VC-dimension packet.

The proof in the packet is symbolic.  This script independently checks the
class count, the explicit shattering synthesis, two-term rigidity on finite
coefficient representatives, and the exact small-n VC dimensions.
"""

from itertools import combinations, product


def parity(x: int) -> int:
    return x.bit_count() & 1


def affine_masks(n: int) -> set[int]:
    size = 1 << n
    full = (1 << size) - 1
    result = set()
    for a in range(size):
        mask = sum(parity(a & x) << x for x in range(size))
        result.add(mask)
        result.add(mask ^ full)
    return result


def product_masks(n: int) -> set[int]:
    size = 1 << n
    affine = []
    for a in range(size):
        mask = sum(parity(a & x) << x for x in range(size))
        affine.extend((mask, mask ^ ((1 << size) - 1)))
    return {left & right for left in affine for right in affine}


def c3_masks(n: int) -> set[int]:
    return {a ^ p for a in affine_masks(n) for p in product_masks(n)}


def gaussian_two_planes(n: int) -> int:
    if n < 2:
        return 0
    return ((1 << n) - 1) * ((1 << n) - 2) // 6


def two_term_masks(n: int) -> set[int]:
    """Enumerate all strict signs using coefficient order representatives."""
    size = 1 << n
    chars = [tuple(1 if parity(a & x) == 0 else -1 for x in range(size))
             for a in range(size)]
    result = set()
    coefficients = (-2, -1, 0, 1, 2)
    for i in range(size):
        for j in range(i, size):
            for a in coefficients:
                for b in coefficients:
                    if a == b == 0:
                        continue
                    values = [a * chars[i][x] + b * chars[j][x]
                              for x in range(size)]
                    if 0 in values:
                        continue
                    result.add(sum((value < 0) << x
                                   for x, value in enumerate(values)))
    return result


def shattering_set(n: int) -> list[int]:
    basis = [1 << i for i in range(n)]
    if n == 3:
        edges = [(0, 1), (0, 2), (1, 2)]
    else:
        edges = [(i, j) for i in (0, 1) for j in range(2, n)]
    return [0, *basis, *(basis[i] ^ basis[j] for i, j in edges)]


def synthesize(n: int, labels: int) -> int:
    """Return the truth mask of ell+(u.x)(v.x) matching labels on S."""
    points = shattering_set(n)
    wanted = [(labels >> t) & 1 for t in range(len(points))]
    y0 = wanted[0]
    yi = wanted[1 : n + 1]

    deltas = {}
    for t, x in enumerate(points[n + 1 :], start=n + 1):
        support = [i for i in range(n) if (x >> i) & 1]
        i, j = support
        deltas[i, j] = y0 ^ yi[i] ^ yi[j] ^ wanted[t]

    if n == 3:
        target = tuple(deltas[i, j] for i, j in ((0, 1), (0, 2), (1, 2)))
        uv = None
        for u in range(1 << n):
            for v in range(1 << n):
                got = tuple((((u >> i) & 1) & ((v >> j) & 1)) ^
                            (((u >> j) & 1) & ((v >> i) & 1))
                            for i, j in ((0, 1), (0, 2), (1, 2)))
                if got == target:
                    uv = (u, v)
                    break
            if uv is not None:
                break
        assert uv is not None
        u, v = uv
    else:
        u = 1 << 0
        v = 1 << 1
        for j in range(2, n):
            if deltas[1, j]:
                u |= 1 << j
            if deltas[0, j]:
                v |= 1 << j

    def quadratic(x: int) -> int:
        return parity(u & x) & parity(v & x)

    b = y0 ^ quadratic(0)
    a = 0
    for i in range(n):
        if yi[i] ^ quadratic(1 << i) ^ b:
            a |= 1 << i

    size = 1 << n
    return sum((b ^ parity(a & x) ^ quadratic(x)) << x for x in range(size))


def trace(mask: int, points: tuple[int, ...]) -> int:
    return sum(((mask >> x) & 1) << j for j, x in enumerate(points))


def exact_vc(n: int, functions: set[int]) -> tuple[int, tuple[int, ...]]:
    size = 1 << n
    upper = min(size, len(functions).bit_length() - 1)
    for m in range(upper, -1, -1):
        for points in combinations(range(size), m):
            if len({trace(f, points) for f in functions}) == 1 << m:
                return m, points
    raise AssertionError("empty class")


def main() -> None:
    for n in range(1, 6):
        assert two_term_masks(n) == affine_masks(n)
        functions = c3_masks(n)
        expected = (1 << (n + 1)) * (1 + gaussian_two_planes(n))
        assert len(functions) == expected, (n, len(functions), expected)
        print(f"n={n}: |C_n,3|={len(functions)}; two-term class={len(affine_masks(n))}")

    for n in range(3, 7):
        points = shattering_set(n)
        for labels in range(1 << len(points)):
            mask = synthesize(n, labels)
            assert trace(mask, tuple(points)) == labels
        print(f"n={n}: synthesized all {1 << len(points)} labelings on {len(points)} points")

    for n, expected in ((1, 2), (2, 4), (3, 7), (4, 9)):
        dimension, witness = exact_vc(n, c3_masks(n))
        assert dimension == expected
        print(f"n={n}: exact VC(C_n,3)={dimension}; witness={witness}")

    print("all checks passed")


if __name__ == "__main__":
    main()

