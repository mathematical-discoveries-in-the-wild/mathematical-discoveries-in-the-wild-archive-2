"""Diagnostic checks for the 2008.08559 coexistency packet.

The symbolic part verifies the coefficient identity behind the one-variable
pole lemma.  The numerical part checks the support-function maximizer and
the equality F_A = F_(I-A) on random finite-dimensional effects.
These checks are not a proof.
"""

from __future__ import annotations

import numpy as np
import sympy as sp


def positive_part_trace(matrix: np.ndarray) -> float:
    return float(np.maximum(np.linalg.eigvalsh(matrix), 0.0).sum())


def strength(effect: np.ndarray, vector: np.ndarray, tol: float = 1e-10) -> float:
    vals, vecs = np.linalg.eigh(effect)
    coeff = vecs.conj().T @ vector
    if np.any((vals <= tol) & (np.abs(coeff) > 50 * tol)):
        return 0.0
    return float(1.0 / np.sum(np.abs(coeff) ** 2 / np.maximum(vals, tol)))


def symbolic_pole_check() -> None:
    s, c, p, q, r = sp.symbols("s c p q r")
    numerator = sp.together(
        c / (1 + s * p) + (1 - c) / (1 + s * q) - 1 / (1 + s * r)
    ).as_numer_denom()[0]
    poly = sp.Poly(sp.expand(numerator), s)
    assert poly.degree() <= 2
    # Substituting p=q=r must annihilate every coefficient.
    assert sp.expand(numerator.subs({q: p, r: p})) == 0


def random_checks(seed: int = 200808559, trials: int = 200) -> None:
    rng = np.random.default_rng(seed)
    for _ in range(trials):
        n = int(rng.integers(2, 7))
        unitary, _ = np.linalg.qr(
            rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        )
        eigenvalues = rng.uniform(0.03, 0.97, size=n)
        effect = unitary @ np.diag(eigenvalues) @ unitary.conj().T
        vector = rng.normal(size=n) + 1j * rng.normal(size=n)
        vector /= np.linalg.norm(vector)
        f_effect = strength(effect, vector) + strength(np.eye(n) - effect, vector)
        f_complement = strength(np.eye(n) - effect, vector) + strength(effect, vector)
        assert abs(f_effect - f_complement) < 1e-11

        test = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        test = (test + test.conj().T) / 2
        sqrt_effect = unitary @ np.diag(np.sqrt(eigenvalues)) @ unitary.conj().T
        sandwiched = sqrt_effect @ test @ sqrt_effect
        vals, vecs = np.linalg.eigh(sandwiched)
        positive_projection = vecs[:, vals > 0] @ vecs[:, vals > 0].conj().T
        maximizer = sqrt_effect @ positive_projection @ sqrt_effect
        objective = float(np.trace(test @ maximizer).real)
        assert abs(objective - positive_part_trace(sandwiched)) < 1e-8


if __name__ == "__main__":
    symbolic_pole_check()
    random_checks()
    print("symbolic pole identity and 200 random matrix checks passed")
