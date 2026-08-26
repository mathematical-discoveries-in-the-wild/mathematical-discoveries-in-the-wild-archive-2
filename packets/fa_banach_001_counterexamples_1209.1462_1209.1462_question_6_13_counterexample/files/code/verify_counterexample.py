"""Exact and diagnostic checks for the Question 6.13 counterexample."""

from fractions import Fraction
import cmath
import math


def main() -> None:
    # Exact squared comparisons used to eliminate radicals in the proof.
    assert Fraction(2) > Fraction(34, 25) ** 2
    assert Fraction(2) > Fraction(13, 10) ** 2

    head_budget = 6 * Fraction(2, 5) ** 2
    tail_budget = Fraction(3, 25) * Fraction(1, 3)
    assert head_budget == Fraction(24, 25)
    assert tail_budget == Fraction(1, 25)
    assert head_budget + tail_budget == 1

    # Each of the six coefficient pairs has ell_1 norm one.
    roots = (1, -1, 1j, -1j)
    vectors = [(1, 0), (0, 1)] + [
        (0.5, -0.5 * omega.conjugate()) for omega in roots
    ]
    assert all(abs(a) + abs(b) == 1 for a, b in vectors)

    # Dense diagnostic grid: a nearest fourth root always lies within 4/5
    # throughout the projective annulus.  The symbolic endpoint proof is the
    # rigorous argument; this catches transcription or sign errors.
    worst = 0.0
    worst_point = None
    for j in range(1001):
        rho = 0.4 + 0.6 * j / 1000
        for k in range(2048):
            theta = 2 * math.pi * k / 2048
            z = rho * cmath.exp(1j * theta)
            distance = min(abs(z - omega) for omega in roots)
            if distance > worst:
                worst = distance
                worst_point = (rho, theta)
    assert worst < 0.8, (worst, worst_point)

    endpoint_one = 2 - math.sqrt(2)
    endpoint_two_fifths = Fraction(29, 25) - 2 * math.sqrt(2) / 5
    print("all checks passed")
    print(f"head squared budget = {head_budget}")
    print(f"tail squared budget = {tail_budget}")
    print(f"endpoint squared bounds = {endpoint_one:.12f}, "
          f"{float(endpoint_two_fifths):.12f}")
    print(f"diagnostic worst distance = {worst:.12f} at {worst_point}")


if __name__ == "__main__":
    main()
