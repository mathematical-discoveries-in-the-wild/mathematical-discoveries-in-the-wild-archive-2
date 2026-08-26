#!/usr/bin/env python3
"""Finite-dimensional checks for the transfer-operator characterization.

The tests deliberately use noninjective maps, so phi^{-r}(Sigma) is a proper
sub-sigma-algebra.  All adjoints are taken in the weighted l2(mu) inner
product.  The script compares the theorem's formulas with direct matrix
products and checks the sharp transfer norm formula.
"""

from __future__ import annotations

import itertools
import numpy as np


TOL = 2.0e-10


def adjoint(a: np.ndarray, mu: np.ndarray) -> np.ndarray:
    d = np.diag(mu)
    return np.diag(1.0 / mu) @ a.conj().T @ d


def composition(phi: np.ndarray) -> np.ndarray:
    size = len(phi)
    c = np.zeros((size, size), dtype=complex)
    c[np.arange(size), phi] = 1.0
    return c


def orbit_weight(phi: np.ndarray, pi: np.ndarray, power: int) -> np.ndarray:
    out = np.ones(len(phi), dtype=complex)
    at = np.arange(len(phi))
    for _ in range(power):
        out *= pi[at]
        at = phi[at]
    return out


def mpower(a: np.ndarray, power: int) -> np.ndarray:
    return np.linalg.matrix_power(a, power)


def transfer(c_star: np.ndarray, power: int, f: np.ndarray) -> np.ndarray:
    return mpower(c_star, power) @ f


def weighted_hermitian_error(a: np.ndarray, mu: np.ndarray) -> float:
    return float(np.max(np.abs(a - adjoint(a, mu))))


def assert_close(label: str, left: np.ndarray, right: np.ndarray) -> float:
    err = float(np.max(np.abs(left - right)))
    if err > TOL:
        raise AssertionError(f"{label}: max error {err:.3e}")
    return err


def sharp_relative_constant(
    a: np.ndarray, q: np.ndarray, mu: np.ndarray
) -> float:
    """Return sup ||Af||^2 / int q|f|^2, with infinity convention."""
    positive = q > 5e-13
    if np.max(np.abs(a[:, ~positive]), initial=0.0) > TOL:
        return float("inf")
    if not np.any(positive):
        return 0.0
    dhalf = np.diag(np.sqrt(mu))
    dinvhalf = np.diag(1.0 / np.sqrt(mu))
    a_euclidean = dhalf @ a @ dinvhalf
    reduced = a_euclidean[:, positive] @ np.diag(1.0 / np.sqrt(q[positive]))
    return float(np.linalg.svd(reduced, compute_uv=False)[0] ** 2)


def one_case(
    phi: np.ndarray,
    mu: np.ndarray,
    pi: np.ndarray,
    k: int,
    n: int,
) -> tuple[float, float, float, float]:
    c = composition(phi)
    c_star = adjoint(c, mu)
    w = np.diag(pi) @ c
    w_star = adjoint(w, mu)

    def q(power: int) -> np.ndarray:
        pi_power = orbit_weight(phi, pi, power)
        return transfer(c_star, power, np.abs(pi_power) ** 2).real

    # Basic identities W^j=M_{pi_j}C^j and W*^j W^j=M_{q_j}.
    max_power_error = 0.0
    max_gram_error = 0.0
    for j in range(0, max(k + 1, n) + 1):
        pi_j = orbit_weight(phi, pi, j)
        max_power_error = max(
            max_power_error,
            assert_close(
                f"power j={j}", mpower(w, j), np.diag(pi_j) @ mpower(c, j)
            ),
        )
        max_gram_error = max(
            max_gram_error,
            assert_close(
                f"Gram j={j}",
                mpower(w_star, j) @ mpower(w, j),
                np.diag(q(j)),
            ),
        )

    a_direct = mpower(w_star, n) @ mpower(w, k)
    lhs_direct = adjoint(a_direct, mu) @ a_direct
    rhs_direct = mpower(w_star, k + 1) @ mpower(w, k + 1)
    assert_close("right Gram", rhs_direct, np.diag(q(k + 1)))
    if weighted_hermitian_error(lhs_direct, mu) > TOL:
        raise AssertionError("left Gram is not weighted-self-adjoint")

    if k >= n:
        r = k - n
        pi_r = orbit_weight(phi, pi, r)
        a_formula = np.diag(q(n) * pi_r) @ mpower(c, r)
        factor_error = assert_close("k>=n factorization", a_direct, a_formula)
        multiplier = transfer(c_star, r, q(n) ** 2 * np.abs(pi_r) ** 2).real
        formula_error = assert_close("k>=n Gram", lhs_direct, np.diag(multiplier))

        ratios = np.divide(
            multiplier,
            q(k + 1),
            out=np.full_like(multiplier, np.inf),
            where=q(k + 1) > 5e-13,
        )
        ratios[(multiplier < 5e-13) & (q(k + 1) < 5e-13)] = 0.0
        theorem_constant = float(np.max(ratios))
    else:
        r = n - k
        pi_r = orbit_weight(phi, pi, r)
        b = np.conj(pi_r) * q(k)
        a_formula = mpower(c_star, r) @ np.diag(b)
        factor_error = assert_close("k<n factorization", a_direct, a_formula)
        formula_error = assert_close(
            "k<n Gram", lhs_direct, adjoint(a_formula, mu) @ a_formula
        )

        denominator = q(k + 1)
        quotient = np.divide(
            np.abs(b) ** 2,
            denominator,
            out=np.full_like(denominator, np.inf),
            where=denominator > 5e-13,
        )
        quotient[(np.abs(b) < 5e-13) & (denominator < 5e-13)] = 0.0
        if np.any(~np.isfinite(quotient)):
            theorem_constant = float("inf")
        else:
            theorem_constant = float(np.max(transfer(c_star, r, quotient).real))

    matrix_constant = sharp_relative_constant(a_direct, q(k + 1), mu)
    if np.isfinite(theorem_constant) and np.isfinite(matrix_constant):
        if abs(theorem_constant - matrix_constant) > 3e-9:
            raise AssertionError(
                f"sharp constant: theorem={theorem_constant}, matrix={matrix_constant}"
            )
    elif not (np.isinf(theorem_constant) and np.isinf(matrix_constant)):
        raise AssertionError(
            f"finiteness mismatch: theorem={theorem_constant}, matrix={matrix_constant}"
        )
    return max_power_error, max_gram_error, factor_error, formula_error


def main() -> None:
    rng = np.random.default_rng(250706511)
    cases = 0
    maxima = np.zeros(4)
    noninjective = 0

    # Four fixed maps plus randomized maps.  Every fixed map is noninjective.
    maps = [
        np.array([0, 0, 1, 1]),
        np.array([1, 1, 1, 2, 2]),
        np.array([0, 2, 2, 0, 3, 3]),
        np.array([2, 2, 0, 0, 2, 4, 4]),
    ]
    for size in range(3, 9):
        for _ in range(7):
            maps.append(rng.integers(0, size, size=size))

    for phi in maps:
        size = len(phi)
        if len(np.unique(phi)) < size:
            noninjective += 1
        mu = rng.uniform(0.15, 3.0, size=size)
        # Include zeros and genuinely complex phases without making all weights zero.
        radii = rng.uniform(0.2, 2.0, size=size)
        radii[rng.random(size) < 0.13] = 0.0
        phases = rng.uniform(-np.pi, np.pi, size=size)
        pi = radii * np.exp(1j * phases)
        if np.max(np.abs(pi)) == 0:
            pi[0] = 1.0

        for k, n in itertools.product(range(0, 5), range(1, 5)):
            maxima = np.maximum(maxima, one_case(phi, mu, pi, k, n))
            cases += 1

    print("VERDICT: PASS")
    print(f"systems={len(maps)} noninjective_systems={noninjective}")
    print(f"(system,k,n)_cases={cases}")
    print("regimes: k>=n and k<n; weights: zero/nonzero complex")
    print(
        "max_errors: power={:.3e} Gram={:.3e} factor={:.3e} formula={:.3e}".format(
            *maxima
        )
    )
    print("sharp relative constants matched in every case")


if __name__ == "__main__":
    main()
