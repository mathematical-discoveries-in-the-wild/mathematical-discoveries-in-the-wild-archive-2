#!/usr/bin/env python3
"""Exhaustively compare leading pairing weights for the two block patterns."""

from __future__ import annotations

import argparse
import itertools


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[b] = a


def leading_graphs(word: str):
    m = len(word)
    plus = [i for i, c in enumerate(word) if c == "x"]
    star = [i for i, c in enumerate(word) if c == "X"]
    if len(plus) != len(star):
        return
    n = len(plus)
    for perm in itertools.permutations(star):
        dsu = DSU(m)
        for a, b in zip(plus, perm):
            dsu.union(a, (b + 1) % m)
            dsu.union((a + 1) % m, b)
        roots = {dsu.find(i) for i in range(m)}
        if len(roots) != n + 1:
            continue
        relabel = {r: k for k, r in enumerate(sorted(roots))}
        edges = {
            (relabel[dsu.find(a)], relabel[dsu.find((a + 1) % m)])
            for a in plus
        }
        yield n + 1, edges


def block_weight(vertices: int, edges, unequal: bool) -> float:
    good = 0
    for labels in itertools.product((0, 1), repeat=vertices):
        if all((labels[u] != labels[v]) == unequal for u, v in edges):
            good += 1
    return good / (2**vertices)


def check(max_length: int) -> None:
    checked_words = checked_terms = 0
    for m in range(2, max_length + 1, 2):
        n = m // 2
        for plus_positions in itertools.combinations(range(m), n):
            plus_positions = set(plus_positions)
            word = "".join("x" if i in plus_positions else "X" for i in range(m))
            equal_total = unequal_total = 0.0
            for vertices, edges in leading_graphs(word):
                assert len(edges) == n
                weq = block_weight(vertices, edges, unequal=False)
                wne = block_weight(vertices, edges, unequal=True)
                assert abs(weq - 2 ** (-n)) < 1e-15
                assert abs(wne - 2 ** (-n)) < 1e-15
                equal_total += weq
                unequal_total += wne
                checked_terms += 1
            assert abs(equal_total - unequal_total) < 1e-15
            checked_words += 1
    print(f"verified {checked_words} balanced words and {checked_terms} leading pairings")


def positive_overlap(interval, half: int) -> bool:
    a, b = interval
    c, d = ((0.0, 0.5) if half == 0 else (0.5, 1.0))
    return min(b, d) > max(a, c)


def diagonal_support_count(n: int, unequal: bool) -> int:
    count = 0
    for i in range(1, n + 1):
        x_interval = ((i - 1) / n, i / n)
        y_interval = ((n - i) / n, (n - i + 1) / n)
        active = any(
            positive_overlap(x_interval, hx)
            and positive_overlap(y_interval, hy)
            and ((hx != hy) == unequal)
            for hx, hy in itertools.product((0, 1), repeat=2)
        )
        count += active
    return count


def check_diagonal_supports() -> None:
    # In pattern coordinates S_ne becomes diagonal-block matrix support after
    # the source's vertical row reversal, while S_= becomes off-diagonal.
    for n in range(2, 33):
        assert diagonal_support_count(n, unequal=True) == n
        assert diagonal_support_count(n, unequal=False) == n % 2
    print("verified diagonal support counts for sizes 2 through 32")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=10)
    args = parser.parse_args()
    if args.max_length < 2 or args.max_length % 2:
        raise SystemExit("--max-length must be a positive even integer")
    check(args.max_length)
    check_diagonal_supports()
