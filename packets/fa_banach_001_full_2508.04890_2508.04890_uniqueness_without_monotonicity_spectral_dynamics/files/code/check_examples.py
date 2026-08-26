#!/usr/bin/env python3
"""Sanity checks for the two spectral-transform examples.

These finite/scalar checks are not part of the proof.  The proof in main.tex
uses the spectral theorem and dominated convergence.
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    eigenvalues = np.array([-1.0, -0.9, 0.3, 1.0])
    expected = np.array([1.0, 0.0, 0.0, 1.0])

    phi_orbit = eigenvalues.copy()
    for _ in range(12):
        phi_orbit = phi_orbit**2
    phi_error = float(np.max(np.abs(phi_orbit - expected)))

    psi_orbit = eigenvalues.copy()
    for n in range(1, 8):
        psi_orbit = 0.5 * psi_orbit**2
        closed_form = (2.0 ** (1 - 2**n)) * eigenvalues ** (2**n)
        if not np.allclose(psi_orbit, closed_form, rtol=0.0, atol=1e-15):
            raise AssertionError(f"closed form failed at n={n}")

    # Scalar order failure: -1 <= 0, but both maps send -1 above the image of 0.
    if not (-1.0 <= 0.0 and (-1.0) ** 2 > 0.0**2):
        raise AssertionError("order counterexample failed for Phi")
    if not (-1.0 <= 0.0 and 0.5 * (-1.0) ** 2 > 0.5 * 0.0**2):
        raise AssertionError("order counterexample failed for Psi")

    print(f"Phi finite-spectrum max error after 12 steps: {phi_error:.3e}")
    print(f"Psi max norm after 7 steps: {np.max(np.abs(psi_orbit)):.3e}")
    print("closed-form and scalar-order checks: PASS")


if __name__ == "__main__":
    main()
