#!/usr/bin/env python3
"""Finite-cyclic audit for the proposed UTC(p), p <= 5, structure theorem.

This uses floating-point root-of-unity tests only as a bounded audit.  The
packet proof is analytic and does not depend on this computation.
"""

from __future__ import annotations

import cmath
import itertools
import math


TOL = 1.0e-8
LIMITS = {2: 60, 3: 36, 4: 24, 5: 18}


def zero_differences(q: int, cols: tuple[int, ...]) -> set[int]:
    out: set[int] = set()
    for d in range(1, q):
        value = sum(cmath.exp(2j * math.pi * d * ell / q) for ell in cols)
        if abs(value) < TOL:
            out.add(d)
    return out


def spectra_containing_zero(q: int, p: int, zeros: set[int]):
    for tail in itertools.combinations(range(1, q), p - 1):
        rows = (0,) + tail
        if all(((a - b) % q) in zeros for a, b in itertools.combinations(rows, 2)):
            yield rows


def unique_sum_mod(a: tuple[int, ...], c: tuple[int, ...], modulus: int) -> bool:
    sums = [(x + y) % modulus for x in a for y in c]
    return len(sums) == modulus and len(set(sums)) == modulus


def audit_23(p: int, families: list[tuple[int, ...]]) -> None:
    diffs = [abs(a - b) for rows in families for a, b in itertools.combinations(rows, 2)]
    g = math.gcd(*diffs)
    complement = tuple(range(g))
    modulus = p * g
    for rows in families:
        base = rows[0]
        residues = {((a - base) // g) % p for a in rows}
        assert all((a - base) % g == 0 for a in rows)
        assert residues == set(range(p))
        assert unique_sum_mod(rows, complement, modulus)


def order_four_form(rows: tuple[int, ...], q: int) -> tuple[int, int]:
    n = q // 2
    pairs = []
    unused = set(rows)
    while unused:
        x = min(unused)
        y = (x + n) % q
        assert y in unused
        pairs.append(x)
        unused.remove(x)
        unused.remove(y)
    assert len(pairs) == 2
    e = (pairs[1] - pairs[0]) % n
    assert e != 0
    return pairs[0], e


def audit_4(q: int, families: list[tuple[int, ...]]) -> None:
    assert q % 4 == 0
    n = q // 2
    forms = [order_four_form(rows, q) for rows in families]
    valuations = []
    for _, e in forms:
        valuations.append((e & -e).bit_length() - 1)
    assert len(set(valuations)) == 1
    d = math.gcd(n, *(e for _, e in forms))
    assert (n // d) % 2 == 0
    complement = tuple(r + 2 * d * k for r in range(d) for k in range(n // (2 * d)))
    for rows in families:
        assert unique_sum_mod(rows, complement, q)


def audit_5(q: int, families: list[tuple[int, ...]]) -> None:
    assert q % 5 == 0
    h = q // 5
    subgroup = {(k * h) % q for k in range(5)}
    complement = tuple(range(h))
    for rows in families:
        translated = {(a - rows[0]) % q for a in rows}
        assert translated == subgroup
        assert unique_sum_mod(rows, complement, q)


def main() -> None:
    total_column_sets = 0
    total_nonempty_families = 0
    total_spectra = 0
    by_p: dict[int, tuple[int, int, int]] = {}

    for p, qmax in LIMITS.items():
        p_columns = p_families = p_spectra = 0
        for q in range(p, qmax + 1):
            for tail in itertools.combinations(range(1, q), p - 1):
                cols = (0,) + tail
                if math.gcd(q, *cols) != 1:
                    continue  # q is not the minimal character period
                p_columns += 1
                zeros = zero_differences(q, cols)
                families = list(spectra_containing_zero(q, p, zeros))
                if not families:
                    continue
                p_families += 1
                p_spectra += len(families)
                if p in (2, 3):
                    audit_23(p, families)
                elif p == 4:
                    audit_4(q, families)
                else:
                    audit_5(q, families)
        by_p[p] = (p_columns, p_families, p_spectra)
        total_column_sets += p_columns
        total_nonempty_families += p_families
        total_spectra += p_spectra

    for p in sorted(by_p):
        cols, fams, specs = by_p[p]
        print(f"p={p}: column_sets={cols}, nonempty_families={fams}, spectra={specs}")
    print(
        "PASS: "
        f"{total_column_sets} primitive column sets, "
        f"{total_nonempty_families} nonempty spectrum families, "
        f"{total_spectra} spectra"
    )


if __name__ == "__main__":
    main()
