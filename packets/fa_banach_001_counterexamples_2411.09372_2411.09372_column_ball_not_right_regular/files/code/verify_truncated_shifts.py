#!/usr/bin/env python3
"""Finite-matrix checks for the truncated-shift obstruction.

These checks illustrate the exact proof; they are not a substitute for it.
"""

from itertools import product

import numpy as np


def truncated_left_shifts(d: int, depth: int) -> list[np.ndarray]:
    words = [w for length in range(depth + 1) for w in product(range(d), repeat=length)]
    index = {w: i for i, w in enumerate(words)}
    shifts = []
    for letter in range(d):
        matrix = np.zeros((len(words), len(words)))
        for word in words:
            if len(word) < depth:
                matrix[index[(letter,) + word], index[word]] = 1.0
        shifts.append(matrix)
    return shifts


def check_case(d: int, depth: int, radius: float = 0.83) -> None:
    left = truncated_left_shifts(d, depth)
    x = [radius * shift.T for shift in left]

    column_square = sum(operator.T @ operator for operator in x)
    column_norm = np.linalg.norm(column_square, 2)

    row_square = np.zeros_like(column_square)
    for word in product(range(d), repeat=depth):
        word_operator = np.eye(column_square.shape[0])
        for letter in word:
            word_operator = word_operator @ x[letter]
        row_square += word_operator @ word_operator.T
    row_norm = np.sqrt(np.linalg.norm(row_square, 2))

    expected_column = radius**2
    expected_row = (radius**depth) * (d ** (depth / 2))
    assert np.isclose(column_norm, expected_column)
    assert np.isclose(row_norm, expected_row)
    print(
        f"d={d}, N={depth}, dim={column_square.shape[0]}: "
        f"column-square norm={column_norm:.12g}, word-row norm={row_norm:.12g}"
    )


def main() -> None:
    for d in (2, 3):
        for depth in range(1, 5):
            check_case(d, depth)
    print("all truncated-shift checks passed")


if __name__ == "__main__":
    main()
