"""Finite real-valued checks for the conditional-tensor identities.

This is a sanity check, not a proof of the compactness theorem.
"""

from itertools import product

import numpy as np


def conditional_expectation(a: np.ndarray, blocks: np.ndarray) -> np.ndarray:
    out = np.empty_like(a, dtype=float)
    for block in np.unique(blocks):
        mask = blocks == block
        out[mask] = a[mask].mean()
    return out


def all_signs(n: int):
    return [np.asarray(v, dtype=float) for v in product((-1.0, 1.0), repeat=n)]


def check_instance(n: int, block_count: int, rng: np.random.Generator) -> None:
    blocks = rng.integers(0, block_count, size=(n, n))
    signs = all_signs(n)
    tests = [
        conditional_expectation(np.outer(f, g), blocks)
        for f in signs
        for g in signs
    ]

    block_values = rng.uniform(-1.0, 1.0, size=block_count)
    kernel = block_values[blocks]
    direct_cut = max(abs(np.mean(np.outer(f, g) * kernel)) for f in signs for g in signs)
    projected_cut = max(abs(np.mean(k * kernel)) for k in tests)
    assert np.isclose(direct_cut, projected_cut, atol=1e-12)

    i, j = rng.integers(0, len(tests), size=2)
    h = tests[i] - tests[j]
    phase = np.sign(h)
    dual_value = abs(np.mean(h * phase))
    assert np.isclose(dual_value, np.mean(np.abs(h)), atol=1e-12)


def main() -> None:
    rng = np.random.default_rng(10035588)
    count = 0
    for n in (2, 3, 4):
        for block_count in range(1, n * n + 1):
            for _ in range(12):
                check_instance(n, block_count, rng)
                count += 1
    print(f"PASS: {count} randomized finite product partitions")


if __name__ == "__main__":
    main()

