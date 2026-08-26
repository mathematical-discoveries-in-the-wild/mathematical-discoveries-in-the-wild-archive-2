#!/usr/bin/env python3
"""Sanity checks for the hidden-width-two sparse-product classification.

The checks are not a proof. They verify that the theorem's cases partition all
small support patterns and that its multinomial probability equals direct
weighted enumeration.
"""

from __future__ import annotations

from itertools import product
from math import factorial


def subsets(n: int):
    for mask in range(1 << n):
        yield frozenset(i for i in range(n) if mask & (1 << i))


def nonclosed(s1, s2, t1, t2) -> bool:
    sr = s1 & s2
    tr = t1 & t2
    if not sr or not tr:
        return False
    return (
        (bool(s1 - s2) and bool(t1 - t2))
        or (bool(s2 - s1) and bool(t2 - t1))
        or (len(sr) >= 2 and bool(t1 - t2) and bool(t2 - t1))
        or (len(tr) >= 2 and bool(s1 - s2) and bool(s2 - s1))
    )


def proved_closed_case(s1, s2, t1, t2) -> bool:
    if not (s1 & s2) or not (t1 & t2):
        return True  # disjoint coordinate supports
    if (s1 <= s2 and t2 <= t1) or (s2 <= s1 and t1 <= t2):
        return True  # cross-nested rectangles
    if s1 == s2 and len(s1) == 1:
        return True  # common one-dimensional row space
    if t1 == t2 and len(t1) == 1:
        return True  # common one-dimensional column space
    return False


def membership_counts(a, b, size):
    counts = [0, 0, 0, 0]  # 11, 10, 01, 00
    for i in range(size):
        code = (i in a, i in b)
        counts[{(True, True): 0, (True, False): 1,
                (False, True): 2, (False, False): 3}[code]] += 1
    return tuple(counts)


def event_from_counts(rho, tau):
    r11, r10, r01, _ = rho
    t11, t10, t01, _ = tau
    return r11 >= 1 and t11 >= 1 and (
        (r10 >= 1 and t10 >= 1)
        or (r01 >= 1 and t01 >= 1)
        or (r11 >= 2 and t10 >= 1 and t01 >= 1)
        or (t11 >= 2 and r10 >= 1 and r01 >= 1)
    )


def multinomial_weight(counts, p):
    n = sum(counts)
    probs = (p * p, p * (1 - p), p * (1 - p), (1 - p) ** 2)
    coeff = factorial(n)
    for c in counts:
        coeff //= factorial(c)
    ans = float(coeff)
    for q, c in zip(probs, counts):
        ans *= q ** c
    return ans


def count_vectors(n):
    for a in range(n + 1):
        for b in range(n - a + 1):
            for c in range(n - a - b + 1):
                yield (a, b, c, n - a - b - c)


def formula_probability(m, n, alpha, beta):
    total = 0.0
    for rho in count_vectors(m):
        wr = multinomial_weight(rho, alpha)
        for tau in count_vectors(n):
            if event_from_counts(rho, tau):
                total += wr * multinomial_weight(tau, beta)
    return total


def exhaustive_probability(m, n, alpha, beta):
    total = 0.0
    row_sets = list(subsets(m))
    col_sets = list(subsets(n))
    for s1, s2, t1, t2 in product(row_sets, row_sets, col_sets, col_sets):
        if not nonclosed(s1, s2, t1, t2):
            continue
        ones_r = len(s1) + len(s2)
        ones_c = len(t1) + len(t2)
        total += (
            alpha ** ones_r
            * (1 - alpha) ** (2 * m - ones_r)
            * beta ** ones_c
            * (1 - beta) ** (2 * n - ones_c)
        )
    return total


def main():
    checked = 0
    for m, n in product(range(1, 5), repeat=2):
        rs = list(subsets(m))
        cs = list(subsets(n))
        for s1, s2, t1, t2 in product(rs, rs, cs, cs):
            nc = nonclosed(s1, s2, t1, t2)
            pc = proved_closed_case(s1, s2, t1, t2)
            assert nc != pc, (m, n, s1, s2, t1, t2, nc, pc)
            assert nc == event_from_counts(
                membership_counts(s1, s2, m),
                membership_counts(t1, t2, n),
            )
            checked += 1

    probability_checks = 0
    for m, n in product(range(1, 4), repeat=2):
        for alpha, beta in ((0.2, 0.35), (0.5, 0.5), (0.73, 0.41)):
            p1 = formula_probability(m, n, alpha, beta)
            p2 = exhaustive_probability(m, n, alpha, beta)
            assert abs(p1 - p2) < 1e-12, (m, n, alpha, beta, p1, p2)
            probability_checks += 1

    # The smallest detector-false-negative degeneration (type II).
    s1 = s2 = frozenset((0, 1))
    t1, t2 = frozenset((0, 2)), frozenset((1, 2))
    assert nonclosed(s1, s2, t1, t2)
    assert not (bool(s1 - s2) and bool(t1 - t2))
    assert not (bool(s2 - s1) and bool(t2 - t1))

    print(f"partition checks passed: {checked}")
    print(f"probability checks passed: {probability_checks}")
    print("minimal type-II false-negative pattern passed")


if __name__ == "__main__":
    main()
