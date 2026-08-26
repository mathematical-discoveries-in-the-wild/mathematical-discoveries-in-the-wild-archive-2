#!/usr/bin/env python3
"""Exact exponent checks for the subspace-power Morrey counterexample.

The proof is analytic.  This script only checks the strict parameter
inequalities and displays the predicted norm quotient at several tube widths.
"""

from fractions import Fraction


def main() -> None:
    n = 2
    d = 1
    m = 1
    p = Fraction(2, 1)
    lam = Fraction(1, 1)
    beta = Fraction(5, 4)

    q = p + lam / n
    reverse_holder_exponent = Fraction(n, 1) / (n - lam)
    a_q_upper = m * (q - 1)
    failure_threshold = m * (p - 1)
    input_exponent = Fraction(m, 1) + beta
    input_exponent /= p
    output_exponent = Fraction(m, 1)
    quotient_exponent = output_exponent - input_exponent

    assert d + m == n
    assert 0 < lam < n
    assert d >= lam
    assert failure_threshold < beta < a_q_upper
    assert reverse_holder_exponent == 2
    assert input_exponent == Fraction(9, 8)
    assert output_exponent == 1
    assert quotient_exponent == Fraction(-1, 8)

    print("explicit parameters")
    print(f"  (n,d,m,p,lambda,beta) = ({n},{d},{m},{p},{lam},{beta})")
    print(f"  q = p+lambda/n = {q}")
    print(f"  A_q interval: -{m} < beta < {a_q_upper}")
    print(f"  RH exponent requested: {reverse_holder_exponent}")
    print(f"  failure condition: beta > {failure_threshold}")
    print(f"  input exponent:  {input_exponent}")
    print(f"  output exponent: {output_exponent}")
    print(f"  quotient exponent: {quotient_exponent}")

    previous = 0.0
    for k in (1, 2, 4, 8, 16, 32):
        t = 10.0 ** (-k)
        quotient = t ** float(quotient_exponent)
        assert quotient > previous
        previous = quotient
        print(f"  t=1e-{k:02d}: predicted lower quotient factor {quotient:.8g}")

    print("PASS: all strict class-membership and blow-up inequalities hold")


if __name__ == "__main__":
    main()

