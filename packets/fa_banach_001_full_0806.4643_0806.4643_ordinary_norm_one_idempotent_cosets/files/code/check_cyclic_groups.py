"""Finite cyclic sanity check for the ordinary multiplier theorem.

For C_n, A(C_n) is the group algebra of the dual cyclic group.  Multiplication
by chi_E corresponds to convolution by its inverse discrete Fourier transform,
so its operator norm is exactly the l1 norm of that transform.
"""

from itertools import combinations
from math import gcd, pi
from cmath import exp


def multiplier_norm(n: int, subset: frozenset[int]) -> float:
    measure = [
        sum(exp(2j * pi * k * x / n) for x in subset) / n
        for k in range(n)
    ]
    return sum(abs(value) for value in measure)


def cosets(n: int) -> set[frozenset[int]]:
    answer: set[frozenset[int]] = set()
    for step in range(n):
        subgroup = frozenset((j * step) % n for j in range(n // gcd(n, step)))
        for shift in range(n):
            answer.add(frozenset((shift + x) % n for x in subgroup))
    return answer


def main() -> None:
    tolerance = 1e-9
    tested = 0
    smallest_noncoset_norm = float("inf")
    witness = None
    for n in range(2, 13):
        known_cosets = cosets(n)
        for size in range(1, n + 1):
            for values in combinations(range(n), size):
                subset = frozenset(values)
                norm = multiplier_norm(n, subset)
                is_contractively_idempotent = abs(norm - 1.0) <= tolerance
                is_coset = subset in known_cosets
                assert is_contractively_idempotent == is_coset, (n, subset, norm)
                if not is_coset and norm < smallest_noncoset_norm:
                    smallest_noncoset_norm = norm
                    witness = (n, sorted(subset), norm)
                tested += 1
    print(f"verified {tested} nonempty subsets of C_n for 2 <= n <= 12")
    print(f"smallest noncoset norm encountered: {witness}")


if __name__ == "__main__":
    main()
