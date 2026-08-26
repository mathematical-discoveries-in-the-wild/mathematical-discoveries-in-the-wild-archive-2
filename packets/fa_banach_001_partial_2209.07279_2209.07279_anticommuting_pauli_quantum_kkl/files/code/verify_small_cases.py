#!/usr/bin/env python3
"""Finite consistency checks for the anticommuting-Pauli KKL packet.

The proof is analytic. This script exhausts all two-qubit Pauli subsets,
filters for pairwise anticommutation, and checks deterministic weight samples.
It also checks random greedy three-qubit families.
"""

from __future__ import annotations

import itertools
import math
import random


PAULIS = (0, 1, 2, 3)  # I, X, Y, Z


def anticommutes(p: tuple[int, ...], q: tuple[int, ...]) -> bool:
    local = sum(a != 0 and b != 0 and a != b for a, b in zip(p, q))
    return local % 2 == 1


def is_pairwise_anticommuting(family: tuple[tuple[int, ...], ...]) -> bool:
    return all(anticommutes(p, q) for p, q in itertools.combinations(family, 2))


def rho(n: int) -> float:
    return 6.0 / (math.sqrt(24.0 * n + 9.0) + 3.0)


def samples(m: int, rng: random.Random):
    yield [1.0 / m] * m
    for index in range(m):
        weights = [0.0] * m
        weights[index] = 1.0
        yield weights
    for _ in range(12):
        raw = [-math.log(max(rng.random(), 1e-15)) for _ in range(m)]
        total = sum(raw)
        yield [value / total for value in raw]


def check_family(family: tuple[tuple[int, ...], ...], rng: random.Random) -> int:
    n = len(family[0])
    checks = 0
    for weights in samples(len(family), rng):
        q = [
            sum(weight for weight, pauli in zip(weights, family) if pauli[j] != 0)
            for j in range(n)
        ]
        maximum = max(q)
        assert maximum + 1e-12 >= rho(n), (family, weights, maximum, rho(n))

        pair_weight = sum(
            weights[s] * weights[t]
            for s in range(len(family))
            for t in range(s + 1, len(family))
        )
        local_cover = 0.0
        for j in range(n):
            mass = [
                sum(weight for weight, pauli in zip(weights, family) if pauli[j] == label)
                for label in (1, 2, 3)
            ]
            local_cover += mass[0] * mass[1] + mass[0] * mass[2] + mass[1] * mass[2]
        assert pair_weight <= local_cover + 1e-12
        assert local_cover <= sum(value * value for value in q) / 3.0 + 1e-12
        checks += 1
    return checks


def main() -> None:
    rng = random.Random(20260809)
    strings2 = tuple(p for p in itertools.product(PAULIS, repeat=2) if any(p))
    families = 0
    checks = 0
    for mask in range(1, 1 << len(strings2)):
        family = tuple(strings2[i] for i in range(len(strings2)) if mask & (1 << i))
        if is_pairwise_anticommuting(family):
            families += 1
            checks += check_family(family, rng)

    strings3 = tuple(p for p in itertools.product(PAULIS, repeat=3) if any(p))
    for _ in range(500):
        order = list(strings3)
        rng.shuffle(order)
        family_list: list[tuple[int, ...]] = []
        for pauli in order:
            if all(anticommutes(pauli, prior) for prior in family_list):
                family_list.append(pauli)
        checks += check_family(tuple(family_list), rng)

    print(f"two_qubit_families={families}")
    print(f"weighted_checks={checks}")
    print("status=PASS")


if __name__ == "__main__":
    main()
