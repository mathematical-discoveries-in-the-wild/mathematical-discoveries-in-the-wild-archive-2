#!/usr/bin/env python3
"""Arithmetic checks for the fat-Cantor threshold proof."""

from decimal import Decimal, getcontext


getcontext().prec = 60


def ln(x: Decimal) -> Decimal:
    return x.ln()


def check(alpha_text: str, p_text: str) -> None:
    alpha = Decimal(alpha_text)
    p = Decimal(p_text)
    two = Decimal(2)
    s0 = (Decimal(1) + ln(two) / ln(alpha)) / p
    a0 = Decimal(1) - p * s0
    critical = two * (alpha ** a0)
    assert Decimal(0) < s0 < Decimal(1) / p
    assert abs(critical - Decimal(1)) < Decimal("1e-50")

    eps = min(s0 / Decimal(5), Decimal("0.01"))
    below = two * (alpha ** (Decimal(1) - p * (s0 - eps)))
    above = two * (alpha ** (Decimal(1) - p * (s0 + eps)))
    assert below < 1 < above

    # The localized lower-bound ratio decays geometrically.
    decay = (two * alpha) ** (Decimal(1) - p * (s0 - eps))
    assert Decimal(0) < decay < Decimal(1)
    print(alpha_text, p_text, "s0=", s0, "critical=", critical)


for alpha_text, p_text in [
    ("0.25", "2"),
    ("0.1", "1.2"),
    ("0.49", "7"),
    ("0.0001", "3.5"),
]:
    check(alpha_text, p_text)

print("checked 4 parameter configurations")
