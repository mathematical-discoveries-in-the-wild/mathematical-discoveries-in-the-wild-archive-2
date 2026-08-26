#!/usr/bin/env python3
"""High-precision audit of the S_64 generalized-Ewens counterexample."""

from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 100

n = 64
eps = Decimal(10) ** -200
r = Decimal(factorial(n)) * eps
assert r < Decimal("0.01")

den = Decimal(2) + r
entropy_upper = den.ln()
rhs = Decimal(n - 1) * entropy_upper

w_h = Decimal(n) / den
w_t = Decimal(n - 1) / den
that = Decimal(n) / den**2

checks = {
    "eq7_hamming": Decimal(2) / Decimal(9) * w_h**2,
    "eq7_transposition": Decimal(1) / Decimal(2) * w_t**2,
    "eq8_hamming": Decimal(1) / Decimal(18) * w_h**2,
    "eq8_transposition": Decimal(1) / Decimal(8) * w_t**2,
}

print(f"r_bound={r}")
print(f"entropy_upper=log(2+r_bound)={entropy_upper}")
print(f"part_a_rhs_upper=63*entropy_upper={rhs}")
for name, lhs in checks.items():
    print(f"{name}_lhs_lower={lhs}")
    assert lhs > rhs

eq9_lhs = that / Decimal(20)
print(f"eq9_lhs_lower={eq9_lhs}")
print(f"eq9_rhs_upper={entropy_upper}")
assert eq9_lhs > entropy_upper
print("ALL_STRICT_VIOLATIONS_VERIFIED")
