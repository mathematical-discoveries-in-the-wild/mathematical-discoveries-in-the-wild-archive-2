"""Exhaustively verify the free-word translate identity on finite balls.

This is a finite sanity check, not a substitute for the packet's general proof.
We use exact rational arithmetic and test several ranks, parameters, and radii.
"""

from fractions import Fraction
from itertools import product


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(-letter for letter in reversed(word))


def multiply(left, right):
    return reduce_word(left + right)


def reduced_words(k, radius):
    alphabet = tuple(range(1, k + 1)) + tuple(range(-k, 0))
    words = {()}
    frontier = {()}
    for _ in range(radius):
        frontier = {
            word + (letter,)
            for word in frontier
            for letter in alphabet
            if not word or word[-1] != -letter
        }
        words.update(frontier)
    return words


def check(k, r, radius=6):
    q = 2 * k - 1
    generators = tuple(range(1, k + 1)) + tuple(range(-k, 0))
    for word in reduced_words(k, radius):
        f = r ** len(word)
        left_sum = sum(
            r ** len(multiply(inverse((s,)), word)) for s in generators
        )
        delta = Fraction(1) if not word else Fraction(0)
        right = (1 / r + q * r) * f - ((1 - r * r) / r) * delta
        assert left_sum == right, (k, r, word, left_sum, right)


cases = tuple(product((2, 3, 4), (Fraction(1, 3), Fraction(2, 3), Fraction(4, 5))))
for rank, parameter in cases:
    check(rank, parameter)
    print(f"PASS k={rank}, r={parameter}, all reduced words of length <= 6")

print("All exact-arithmetic checks passed.")
