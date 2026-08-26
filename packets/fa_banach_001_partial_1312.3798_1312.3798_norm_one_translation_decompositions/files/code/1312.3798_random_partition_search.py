#!/usr/bin/env python3
"""Test whether the norm-one splitting phenomenon is special to cyclic partitions."""

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


def partition_basis(labels: np.ndarray) -> np.ndarray:
    values = sorted(set(int(x) for x in labels))
    index = {value: j for j, value in enumerate(values)}
    basis = np.zeros((len(labels), len(values)))
    for row, value in enumerate(labels):
        basis[row, index[int(value)]] = 1.0
    return basis


def main() -> None:
    rng = np.random.default_rng(20260811)
    for q in range(5, 13):
        for trial in range(600):
            blocks = []
            labels_all = []
            for _ in range(3):
                labels = rng.integers(0, rng.integers(2, q), size=q)
                labels_all.append(labels.tolist())
                blocks.append(partition_basis(labels))
            a = np.concatenate(blocks, axis=1)
            for _ in range(25):
                f = MODULE.range_vertex(a, rng.normal(size=q))
                if f is None or np.max(np.abs(f)) < 1e-9:
                    continue
                f /= np.max(np.abs(f))
                quotient, _ = MODULE.quotient_norm(a, f)
                if quotient > 1.00001:
                    print(f"WITNESS q={q}, quotient={quotient:.12g}")
                    print("partitions=", labels_all)
                    print("f=", np.round(f, 10).tolist())
                    return
        print(f"q={q}: no witness")
    print("no random-partition witness found")


if __name__ == "__main__":
    main()
