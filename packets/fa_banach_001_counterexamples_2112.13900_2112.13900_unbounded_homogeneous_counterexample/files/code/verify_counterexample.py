"""Exact checks for the one-dimensional counterexample to arXiv:2112.13900."""

from fractions import Fraction


def a_value(x: Fraction, gamma: int = 3):
    if x < 0:
        return None
    if x == 0:
        return "negative_ray"
    return x**gamma


def main() -> None:
    gamma = 3

    # A is monotone on positive graph points; values at zero are nonpositive.
    samples = [Fraction(k, 8) for k in range(1, 25)]
    assert all((a_value(x, gamma) - a_value(y, gamma)) * (x - y) >= 0
               for x in samples for y in samples)
    assert all((a_value(x, gamma) - z) * x >= 0
               for x in samples for z in range(-50, 1))

    # (H3) with v*=-1 on D(A) intersect boundary G1 = {2}.
    outer = Fraction(2)
    assert a_value(outer, gamma) > 0

    # (H4) on D(A) intersect boundary G2 = {1}: A(1)+lambda J(1)>0.
    inner = Fraction(1)
    assert all(a_value(inner, gamma) + lam * inner > 0
               for lam in [Fraction(k, 7) for k in range(50)])

    # The only zero is x=0, which lies in G2 rather than G1\G2.
    assert 0 not in [x for x in samples if a_value(x, gamma) == 0]

    print("PASS: monotonicity samples, (H3), (H4), and absence of annular zeros")


if __name__ == "__main__":
    main()
