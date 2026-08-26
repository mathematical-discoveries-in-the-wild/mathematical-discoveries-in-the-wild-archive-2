"""Exact low-degree Gram determinants for the colored categories D_s.

The script treats D_s(0,k).  A colored block is stored modulo simultaneous
color reversal.  Overlaying two diagrams produces signed equality constraints
on tensor indices; a consistent connected component has N=2n choices.
"""

from itertools import product

import sympy as sp


def set_partitions(n):
    """Restricted-growth strings for all set partitions of range(n)."""
    if n == 0:
        yield ()
        return

    def extend(prefix, maximum):
        if len(prefix) == n:
            blocks = [[] for _ in range(maximum + 1)]
            for point, block in enumerate(prefix):
                blocks[block].append(point)
            yield tuple(tuple(block) for block in blocks)
            return
        for block in range(maximum + 2):
            yield from extend(prefix + (block,), max(maximum, block))

    yield from extend((0,), 0)


def is_noncrossing(partition):
    for i, block_a in enumerate(partition):
        a = set(block_a)
        for block_b in partition[i + 1 :]:
            b = set(block_b)
            for x1 in a:
                for y1 in b:
                    for x2 in a:
                        for y2 in b:
                            if x1 < y1 < x2 < y2:
                                return False
    return True


def block_colorings(size, s):
    """Admissible bit strings modulo complement for a lower-only block."""
    answer = set()
    for bits in product((0, 1), repeat=size):
        black = sum(bits)
        if (2 * black - size) % s:
            continue
        complement = tuple(1 - bit for bit in bits)
        answer.add(min(bits, complement))
    return tuple(sorted(answer))


def colored_partitions(k, s):
    diagrams = []
    for partition in set_partitions(k):
        if not is_noncrossing(partition):
            continue
        options = [block_colorings(len(block), s) for block in partition]
        if any(not choices for choices in options):
            continue
        for patterns in product(*options):
            diagrams.append(tuple(zip(partition, patterns)))
    return tuple(diagrams)


class ParityUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.parity = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            parent = self.parent[x]
            root, shift = self.find(parent)
            self.parity[x] ^= shift
            self.parent[x] = root
        return self.parent[x], self.parity[x]

    def join(self, x, y, parity):
        root_x, shift_x = self.find(x)
        root_y, shift_y = self.find(y)
        if root_x == root_y:
            return (shift_x ^ shift_y) == parity
        self.parent[root_x] = root_y
        self.parity[root_x] = shift_x ^ shift_y ^ parity
        return True


def impose(diagram, uf):
    for block, colors in diagram:
        anchor = block[0]
        for point, color in zip(block[1:], colors[1:]):
            if not uf.join(anchor, point, colors[0] ^ color):
                return False
    return True


def gram_entry(left, right, k, N):
    uf = ParityUnionFind(k)
    if not impose(left, uf) or not impose(right, uf):
        return sp.Integer(0)
    components = len({uf.find(point)[0] for point in range(k)})
    return N**components


def compute(k, s):
    N = sp.Symbol("N")
    diagrams = colored_partitions(k, s)
    gram = sp.Matrix(
        [[gram_entry(left, right, k, N) for right in diagrams] for left in diagrams]
    )
    determinant = sp.factor(gram.det(method="domain-ge"))
    print(f"k={k} s={s} size={len(diagrams)}")
    print(determinant)
    return determinant


if __name__ == "__main__":
    determinant = compute(6, 5)
    N = sp.Symbol("N")
    expected = N**33 * (N - 2) ** 26 * (N - 4) ** 2
    assert sp.expand(determinant - expected) == 0
    diagrams = colored_partitions(6, 5)
    gram_at_four = sp.Matrix(
        [[gram_entry(left, right, 6, sp.Integer(4)) for right in diagrams] for left in diagrams]
    )
    assert gram_at_four.rank() == 31
    print("PASS: exact D_5(0,6) determinant factorization verified.")
    print("PASS: at N=4 the 33-by-33 Gram matrix has rank 31.")
