#!/usr/bin/env python3
"""Numerical checks for the mutually-unbiased-basis SD-tuple obstruction."""

from __future__ import annotations

import argparse
import numpy as np


def mub_bases(p: int, d: int) -> list[np.ndarray]:
    if p % 2 == 0:
        raise ValueError("Use an odd prime.")
    if d > p + 1:
        raise ValueError("The explicit construction provides p+1 bases.")
    bases = [np.eye(p, dtype=complex)]
    x = np.arange(p)
    root = np.exp(2j*np.pi/p)
    for r in range(d-1):
        basis = np.empty((p, p), dtype=complex)
        for k in range(p):
            basis[:, k] = root**((r*x*x+k*x) % p)/np.sqrt(p)
        bases.append(basis)
    return bases


def verify(p: int, d: int, exhaustive: bool) -> None:
    bases = mub_bases(p, d)
    ortho_error = max(np.max(abs(b.conj().T@b-np.eye(p))) for b in bases)
    unbiased_error = max(
        np.max(abs(abs(bases[i].conj().T@bases[j])-1/np.sqrt(p)))
        for i in range(d) for j in range(i+1, d)
    )
    bound = 1+(d-1)/np.sqrt(p)
    rng = np.random.default_rng(180309212+p+d)
    if exhaustive and p**d <= 2_000_000:
        choices = np.ndindex(*(p,)*d)
    else:
        choices = (tuple(rng.integers(p, size=d)) for _ in range(5000))
    max_norm = 0.0
    count = 0
    for choice in choices:
        s = np.zeros((p, p), dtype=complex)
        for i, k in enumerate(choice):
            v = bases[i][:, k]
            s += np.outer(v, v.conj())
        max_norm = max(max_norm, float(np.linalg.eigvalsh(s)[-1]))
        count += 1
    assert ortho_error < 2e-12
    assert unbiased_error < 2e-12
    assert max_norm <= bound+2e-12
    print(f"PASS p={p} d={d} choices={count}")
    print(f"  orthogonality error {ortho_error:.3e}")
    print(f"  unbiasedness error {unbiased_error:.3e}")
    print(f"  max selected-projection norm {max_norm:.12g}")
    print(f"  Gershgorin bound {bound:.12g}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=11)
    parser.add_argument("--d", type=int, default=3)
    parser.add_argument("--suite", action="store_true")
    parser.add_argument("--exhaustive", action="store_true")
    args = parser.parse_args()
    if args.suite:
        for p, d in ((3, 2), (5, 3), (7, 4), (11, 5), (17, 7)):
            verify(p, d, exhaustive=True)
        print("VERDICT: PASS")
    else:
        verify(args.p, args.d, args.exhaustive)
