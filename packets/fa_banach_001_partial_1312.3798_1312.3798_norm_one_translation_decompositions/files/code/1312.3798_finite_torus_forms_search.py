#!/usr/bin/env python3
"""Search additive linear-form models on finite tori for C_n>1."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path

import numpy as np


SEARCH = Path(__file__).with_name("1312.3798_cyclic_constant_search.py")
SPEC = importlib.util.spec_from_file_location("cyclic_search", SEARCH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def forms_basis(m: int, rank: int, forms: tuple[tuple[int, ...], ...]) -> np.ndarray:
    points = list(itertools.product(range(m), repeat=rank))
    blocks = []
    for form in forms:
        block = np.zeros((len(points), m))
        for row, point in enumerate(points):
            value = sum(a * x for a, x in zip(form, point)) % m
            block[row, value] = 1.0
        blocks.append(block)
    return np.concatenate(blocks, axis=1)


def main() -> None:
    rng = np.random.default_rng(20260811)
    cases = [(2, 4, 5), (3, 2, 4), (3, 3, 4)]
    for m, rank, count in cases:
        all_forms = [
            form for form in itertools.product(range(m), repeat=rank) if any(form)
        ]
        form_sets = list(itertools.combinations(all_forms, count))
        if len(form_sets) > 500:
            chosen = rng.choice(len(form_sets), size=500, replace=False)
            form_sets = [form_sets[index] for index in chosen]
        for forms in form_sets:
            a = forms_basis(m, rank, forms)
            directions = [rng.normal(size=m**rank) for _ in range(20)]
            for direction in directions:
                f = MODULE.range_vertex(a, direction)
                if f is None or np.max(np.abs(f)) < 1e-9:
                    continue
                f /= np.max(np.abs(f))
                quotient, coeffs = MODULE.quotient_norm(a, f)
                if quotient > 1.00001:
                    print(
                        f"WITNESS m={m}, rank={rank}, n={count}, "
                        f"quotient={quotient:.12g}, forms={forms}"
                    )
                    print("f=", np.round(f, 8).tolist())
                    print("components=", np.round(coeffs.reshape(count, m), 8))
                    return
        print(f"m={m}, rank={rank}, n={count}: no witness")
    print("no finite-torus witness found")


if __name__ == "__main__":
    main()
