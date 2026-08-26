"""Sanity checks for the arXiv:1904.05239 block counterexample.

The direct-sum proof in main.tex is the proof.  This script checks the explicit
matrix arithmetic and samples random words at several epsilon values.
"""

from __future__ import annotations

import itertools
import numpy as np


A = np.diag([2.0, 1.0, 4.0])
B = np.array([[2.0, 1.0, 0.0], [1.0, 2.0, 0.0], [0.0, 0.0, 4.0]])


def product(word: str, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.eye(a.shape[0])
    for letter in word:
        out = out @ (a if letter == "A" else b)
    return out


def ordered(word: str, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.linalg.matrix_power(a, word.count("A")) @ np.linalg.matrix_power(
        b, word.count("B")
    )


def check_pair(a: np.ndarray, b: np.ndarray, max_length: int = 10) -> int:
    tested = 0
    for length in range(2, max_length + 1):
        for letters in itertools.product("AB", repeat=length):
            word = "".join(letters)
            if "A" not in word or "B" not in word:
                continue
            lhs = np.linalg.norm(product(word, a, b), 2)
            rhs = np.linalg.norm(ordered(word, a, b), 2)
            assert lhs <= rhs + 1e-8 * max(1.0, rhs), (word, lhs, rhs)
            tested += 1
    return tested


def main() -> None:
    expected = np.array([[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    assert np.array_equal(A @ B - B @ A, expected)
    assert np.all(np.linalg.eigvalsh(A) > 0)
    assert np.all(np.linalg.eigvalsh(B) > 0)

    total = check_pair(A, B)
    identity = np.eye(3)
    for epsilon in (1e-6, 0.01, 0.1, 1.0, 10.0):
        total += check_pair(identity + epsilon * A, identity + epsilon * B)
    print(f"verified {total} word/pair cases; explicit commutator and positivity checks passed")


if __name__ == "__main__":
    main()
