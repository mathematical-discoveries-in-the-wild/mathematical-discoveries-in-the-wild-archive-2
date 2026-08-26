"""Exact finite sanity checks for the dyadic-digit counterexample.

The mathematical proof is symbolic.  These checks guard against indexing or
carry mistakes in the two binary-arithmetic identities used in the packet.
"""

from fractions import Fraction


Q = Fraction(3, 4)


def bits(j: int, depth: int) -> list[int]:
    """The first ``depth`` binary digits of j / 2**depth."""
    return [(j >> (depth - k)) & 1 for k in range(1, depth + 1)]


def h_truncated(j: int, depth: int) -> Fraction:
    return sum((Q**k) * bit for k, bit in enumerate(bits(j, depth), 1))


def check_large_quotients() -> int:
    cases = 0
    for n in range(1, 8):
        depth = n + 5
        step = 1 << (depth - n)
        for j in range(1 << depth):
            digit_n = bits(j, depth)[n - 1]
            if digit_n == 0:
                assert j + step < 1 << depth
                difference = h_truncated(j + step, depth) - h_truncated(j, depth)
                assert difference == Q**n
                quotient = difference / Fraction(1, 1 << n)
                assert quotient == Fraction(3, 2) ** n
                cases += 1
    return cases


def check_finite_prefix_cocycles() -> int:
    cases = 0
    for n in range(1, 8):
        depth = n + 5
        tail_size = 1 << (depth - n)
        for m in range(1 << n):
            for prefix in range(1 << n):
                expected = None
                for tail in range(tail_size):
                    j = prefix * tail_size + tail
                    translated = ((prefix - m) % (1 << n)) * tail_size + tail
                    increment = h_truncated(translated, depth) - h_truncated(j, depth)
                    if expected is None:
                        expected = increment
                    assert increment == expected
                    cases += 1
    return cases


if __name__ == "__main__":
    quotient_cases = check_large_quotients()
    cocycle_cases = check_finite_prefix_cocycles()
    print(f"large-quotient identities checked: {quotient_cases}")
    print(f"finite-prefix cocycle identities checked: {cocycle_cases}")
    print("all exact checks passed")

