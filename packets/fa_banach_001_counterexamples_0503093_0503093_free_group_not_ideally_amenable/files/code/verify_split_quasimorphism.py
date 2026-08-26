#!/usr/bin/env python3
"""Finite exact checks for the split-quasimorphism algebra in the packet.

The infinite-dimensional bounded-cohomology vanishing is a theorem-level input,
not a finite computation.  This script checks the word reduction, the claimed
defect bound on a large finite ball, the cocycle identity, and the growth values
used to prove nontriviality.
"""

from itertools import product


LETTERS = ("a", "A", "b", "B")
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == INV[letter]:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def multiply(g, h):
    return reduce_word(g + h)


def split_phi(g):
    """Sum signs of maximal a/A syllables in the reduced word."""
    g = reduce_word(g)
    total = 0
    index = 0
    while index < len(g):
        family = g[index].lower()
        letter = g[index]
        while index < len(g) and g[index].lower() == family:
            index += 1
        if family == "a":
            total += 1 if letter == "a" else -1
    return total


def cocycle(g, h):
    return split_phi(g) + split_phi(h) - split_phi(multiply(g, h))


def words(radius):
    answer = {()}
    for length in range(1, radius + 1):
        for raw in product(LETTERS, repeat=length):
            reduced = reduce_word(raw)
            if len(reduced) == length:
                answer.add(reduced)
    return sorted(answer, key=lambda w: (len(w), w))


def main():
    ball = words(5)
    maximum = 0
    witness = None
    for g in ball:
        for h in ball:
            value = abs(cocycle(g, h))
            if value > maximum:
                maximum = value
                witness = (g, h)
    assert maximum <= 3, (maximum, witness)

    smaller = words(3)
    for g in smaller:
        for h in smaller:
            for k in smaller:
                # Trivial-coefficient two-cocycle identity.
                lhs = cocycle(h, k) - cocycle(multiply(g, h), k)
                rhs = -cocycle(g, multiply(h, k)) + cocycle(g, h)
                assert lhs == rhs, (g, h, k, lhs, rhs)

    for n in range(1, 25):
        an = tuple("a" for _ in range(n))
        bn = tuple("b" for _ in range(n))
        abn = tuple("ab" * n)
        assert split_phi(an) == 1
        assert split_phi(bn) == 0
        assert split_phi(abn) == n

    print(f"reduced words in radius-5 ball: {len(ball)}")
    print(f"largest observed split-quasimorphism defect: {maximum}")
    print("two-cocycle identity checked on every radius-3 triple")
    print("growth checks phi(a^n)=1, phi(b^n)=0, phi((ab)^n)=n passed")


if __name__ == "__main__":
    main()

