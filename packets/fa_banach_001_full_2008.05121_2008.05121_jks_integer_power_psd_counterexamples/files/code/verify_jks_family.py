#!/usr/bin/env python3
"""High-precision audit of the JKS one-corner-pair construction.

Usage:
    conda run --no-capture-output -n sandbox python code/verify_jks_family.py

This is numerical evidence only; the packet contains an exact proof.
"""

from __future__ import annotations

import mpmath as mp


def determinant_audit(m: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return det(A), -c^2 det(B), and their relative discrepancy."""
    n = m + 3
    lower = mp.pi / (2 * (n - 1))
    upper = mp.pi / (2 * (n - 2))
    delta = (lower + upper) / 2
    u = [(j - (n - 1) / 2) * delta for j in range(n)]

    def untruncated(t: mp.mpf) -> mp.mpf:
        return mp.mpf(1) if m == 0 else mp.cos(t) ** m

    def truncated(t: mp.mpf) -> mp.mpf:
        q = mp.cos(t)
        if q <= 0:
            return mp.mpf(0)
        return mp.mpf(1) if m == 0 else q**m

    c_matrix = mp.matrix(n, n)
    a_matrix = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            c_matrix[j, k] = untruncated(u[j] - u[k])
            a_matrix[j, k] = truncated(u[j] - u[k])

    b_matrix = mp.matrix(
        [[c_matrix[j, k] for k in range(1, n - 1)] for j in range(1, n - 1)]
    )
    span = (n - 1) * delta
    c = untruncated(span)
    det_a = mp.det(a_matrix)
    det_b = mp.det(b_matrix)
    predicted = -(c**2) * det_b
    relative_error = abs(det_a - predicted) / abs(predicted)

    if not det_b > 0:
        raise AssertionError(f"m={m}: middle determinant is not positive")
    if not det_a < 0:
        raise AssertionError(f"m={m}: constructed determinant is not negative")
    if not relative_error < mp.mpf("1e-70"):
        raise AssertionError(f"m={m}: determinant identity discrepancy too large")
    return det_a, predicted, relative_error


def main() -> None:
    mp.mp.dps = 180
    print("m  sign(det A)  sign(det B)  relative identity error")
    for m in range(17):
        det_a, predicted, relative_error = determinant_audit(m)
        print(
            f"{m:2d}      -            +       "
            f"{mp.nstr(relative_error, 5)}"
        )
        if mp.sign(det_a) != mp.sign(predicted):
            raise AssertionError(f"m={m}: predicted sign mismatch")
    print("PASS: m=0,...,16")


if __name__ == "__main__":
    main()
