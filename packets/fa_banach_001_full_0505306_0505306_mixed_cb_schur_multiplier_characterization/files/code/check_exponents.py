"""Exact arithmetic checks for the exponents in the proof packet.

This is a consistency check only, not part of the proof.
"""

from fractions import Fraction


def check(p_inv: Fraction, q_inv: Fraction) -> None:
    delta_1 = Fraction(1, 2) - p_inv
    delta_2 = q_inv - Fraction(1, 2)
    delta = q_inv - p_inv
    assert delta == delta_1 + delta_2
    if delta == 0:
        return
    total_exp = Fraction(2, 1) / delta
    reciprocal = delta / 2
    pieces = Fraction(0)
    if delta_1:
        s_p = Fraction(2, 1) / delta_1
        pieces += 1 / s_p
    if delta_2:
        s_q = Fraction(2, 1) / delta_2
        pieces += 1 / s_q
    assert reciprocal == pieces
    assert total_exp * reciprocal == 1


CASES = [
    (Fraction(0), Fraction(1, 2)),      # infinity -> 2
    (Fraction(1, 2), Fraction(1)),      # 2 -> 1
    (Fraction(0), Fraction(1)),         # infinity -> 1
    (Fraction(1, 4), Fraction(3, 4)),   # 4 -> 4/3 (dual line)
    (Fraction(1, 6), Fraction(2, 3)),   # 6 -> 3/2 (off dual line)
]

for p_inv, q_inv in CASES:
    check(p_inv, q_inv)

print(f"checked {len(CASES)} exponent configurations")

