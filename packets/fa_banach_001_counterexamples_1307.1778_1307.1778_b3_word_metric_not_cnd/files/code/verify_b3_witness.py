"""Exact verifier for the eight-point B_3 negative-type obstruction."""

from __future__ import annotations

from collections import deque


Elt = tuple[int, int, int, int, int]

IDENTITY: Elt = (1, 0, 0, 1, 0)
LETTERS: dict[str, Elt] = {
    "a": (1, 1, 0, 1, 1),
    "b": (1, 0, -1, 1, 1),
    "A": (1, -1, 0, 1, -1),
    "B": (1, 0, 1, 1, -1),
}


def multiply(g: Elt, h: Elt) -> Elt:
    a, b, c, d, exponent = g
    p, q, r, s, other_exponent = h
    return (
        a * p + b * r,
        a * q + b * s,
        c * p + d * r,
        c * q + d * s,
        exponent + other_exponent,
    )


def inverse(g: Elt) -> Elt:
    a, b, c, d, exponent = g
    return (d, -b, -c, a, -exponent)


def evaluate(word: str) -> Elt:
    result = IDENTITY
    for letter in word:
        result = multiply(result, LETTERS[letter])
    return result


def exact_ball(radius: int) -> dict[Elt, int]:
    distance = {IDENTITY: 0}
    queue = deque([IDENTITY])
    while queue:
        g = queue.popleft()
        if distance[g] == radius:
            continue
        for generator in LETTERS.values():
            h = multiply(g, generator)
            if h not in distance:
                distance[h] = distance[g] + 1
                queue.append(h)
    return distance


def main() -> None:
    # Upper bounds between length-two points are four, so this finite ball
    # contains every difference and certifies every required distance.
    ball = exact_ball(4)
    words = ["ab", "BA", "Ab", "bA", "ba", "AB", "Ba", "aB"]
    points = [evaluate(word) for word in words]
    assert len(set(points)) == 8

    matrix = [
        [ball[multiply(inverse(g), h)] for h in points]
        for g in points
    ]
    expected = [
        [0, 4, 4, 4, 2, 4, 2, 2],
        [4, 0, 4, 4, 4, 2, 2, 2],
        [4, 4, 0, 4, 2, 2, 4, 4],
        [4, 4, 4, 0, 2, 2, 4, 4],
        [2, 4, 2, 2, 0, 4, 4, 4],
        [4, 2, 2, 2, 4, 0, 4, 4],
        [2, 2, 4, 4, 4, 4, 0, 4],
        [2, 2, 4, 4, 4, 4, 4, 0],
    ]
    assert matrix == expected

    coefficients = [1, 1, 1, 1, -1, -1, -1, -1]
    assert sum(coefficients) == 0
    quadratic_form = sum(
        coefficients[i] * coefficients[j] * matrix[i][j]
        for i in range(8)
        for j in range(8)
    )
    assert quadratic_form == 8

    print("word order:", " ".join(words))
    for row in matrix:
        print(" ".join(str(value) for value in row))
    print("coefficients:", " ".join(str(value) for value in coefficients))
    print("sum coefficients:", sum(coefficients))
    print("quadratic form:", quadratic_form)
    print("verified: the standard word metric of B_3 is not CND")


if __name__ == "__main__":
    main()

