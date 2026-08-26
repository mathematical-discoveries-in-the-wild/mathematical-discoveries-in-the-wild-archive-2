"""Verify the 4-by-12 maximal row-Hadamard certificate exactly."""

from __future__ import annotations

import itertools


H4 = (
    (1, 1, 1, 1),
    (1, -1, 1, -1),
    (1, 1, -1, -1),
    (1, -1, -1, 1),
)
H = tuple(tuple(value for value in row for _ in range(3)) for row in H4)


def dot(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(x, y))


def main() -> None:
    gram = [[dot(x, y) for y in H] for x in H]
    assert gram == [[12 if i == j else 0 for j in range(4)] for i in range(4)]

    extensions = []
    for x in itertools.product((-1, 1), repeat=12):
        if all(dot(x, row) == 0 for row in H):
            extensions.append(x)
    assert not extensions
    print("verified H H^T = 12 I_4 and zero sign-row extensions among 2^12 cases")


if __name__ == "__main__":
    main()

