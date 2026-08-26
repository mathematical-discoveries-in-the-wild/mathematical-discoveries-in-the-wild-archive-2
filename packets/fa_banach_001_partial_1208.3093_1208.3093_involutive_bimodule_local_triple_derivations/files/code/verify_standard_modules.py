#!/usr/bin/env python3
"""Numerical checks for the two standard ternary bimodule structures.

The proof is exact.  This script audits the formula-heavy endgame on matrix
bimodules: type-I/type-II Leibniz rules, inner normalization, symmetry, and
the unitary identities used in the proof.
"""

from __future__ import annotations

import numpy as np


def sharp(a: np.ndarray) -> np.ndarray:
    return a.conj().T


def e_triple(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return (a @ sharp(b) @ c + c @ sharp(b) @ a) / 2


def x_a_b(x: np.ndarray, a: np.ndarray, b: np.ndarray, kind: str) -> np.ndarray:
    if kind == "II":
        return (x @ sharp(a) @ b + b @ sharp(a) @ x) / 2
    if kind == "I":
        return (x @ a @ sharp(b) + sharp(b) @ a @ x) / 2
    raise ValueError(kind)


def a_x_b(a: np.ndarray, x: np.ndarray, b: np.ndarray, kind: str) -> np.ndarray:
    if kind == "II":
        return (a @ sharp(x) @ b + b @ sharp(x) @ a) / 2
    if kind == "I":
        return (sharp(a) @ sharp(x) @ sharp(b) + sharp(b) @ sharp(x) @ sharp(a)) / 2
    raise ValueError(kind)


def a_b_x(a: np.ndarray, b: np.ndarray, x: np.ndarray, kind: str) -> np.ndarray:
    return x_a_b(x, b, a, kind)


def derivation_residual(T, a, b, c, kind: str) -> float:
    lhs = T(e_triple(a, b, c))
    rhs = x_a_b(T(a), b, c, kind)
    rhs += a_x_b(a, T(b), c, kind)
    rhs += a_b_x(a, b, T(c), kind)
    return float(np.linalg.norm(lhs - rhs, ord="fro"))


def inner_map(x: np.ndarray, kind: str):
    ident = np.eye(x.shape[0], dtype=complex)

    def inner(a: np.ndarray) -> np.ndarray:
        return x_a_b(x, ident, a, kind) - a_x_b(ident, x, a, kind)

    return inner


def random_matrix(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))


def random_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    q, r = np.linalg.qr(random_matrix(rng, n))
    phases = np.diag(r)
    phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
    return q @ np.diag(np.conj(phases))


def main() -> None:
    rng = np.random.default_rng(12083093)
    n = 4
    h0 = random_matrix(rng, n)
    h = h0 - sharp(h0)

    def D(a: np.ndarray) -> np.ndarray:
        return h @ a - a @ h

    def T_ii(a: np.ndarray) -> np.ndarray:
        return D(a)

    def T_i(a: np.ndarray) -> np.ndarray:
        return D(sharp(a))

    maxima = {
        "type_II_triple_residual": 0.0,
        "type_I_triple_residual": 0.0,
        "inner_type_II_residual": 0.0,
        "inner_type_I_residual": 0.0,
        "type_II_symmetry_residual": 0.0,
        "type_I_symmetry_residual": 0.0,
        "type_II_unitary_identity": 0.0,
        "type_I_unitary_identity": 0.0,
    }

    x0 = random_matrix(rng, n)
    x = x0 - sharp(x0)
    inner_ii = inner_map(x, "II")
    inner_i = inner_map(x, "I")

    for _ in range(200):
        a, b, c = (random_matrix(rng, n) for _ in range(3))
        maxima["type_II_triple_residual"] = max(
            maxima["type_II_triple_residual"],
            derivation_residual(T_ii, a, b, c, "II"),
        )
        maxima["type_I_triple_residual"] = max(
            maxima["type_I_triple_residual"],
            derivation_residual(T_i, a, b, c, "I"),
        )
        maxima["inner_type_II_residual"] = max(
            maxima["inner_type_II_residual"],
            derivation_residual(inner_ii, a, b, c, "II"),
        )
        maxima["inner_type_I_residual"] = max(
            maxima["inner_type_I_residual"],
            derivation_residual(inner_i, a, b, c, "I"),
        )
        maxima["type_II_symmetry_residual"] = max(
            maxima["type_II_symmetry_residual"],
            float(np.linalg.norm(T_ii(sharp(a)) - sharp(T_ii(a)), ord="fro")),
        )
        maxima["type_I_symmetry_residual"] = max(
            maxima["type_I_symmetry_residual"],
            float(np.linalg.norm(T_i(sharp(a)) - sharp(T_i(a)), ord="fro")),
        )

        u = random_unitary(rng, n)
        maxima["type_II_unitary_identity"] = max(
            maxima["type_II_unitary_identity"],
            float(np.linalg.norm(T_ii(u) + u @ sharp(T_ii(u)) @ u, ord="fro")),
        )
        maxima["type_I_unitary_identity"] = max(
            maxima["type_I_unitary_identity"],
            float(np.linalg.norm(T_i(u) + sharp(u) @ sharp(T_i(u)) @ sharp(u), ord="fro")),
        )

    ident = np.eye(n, dtype=complex)
    normalization_ii = np.linalg.norm(inner_ii(ident) - 2 * x, ord="fro")
    normalization_i = np.linalg.norm(inner_i(ident) - 2 * x, ord="fro")

    print("matrix_size=4 trials=200 seed=12083093")
    for name, value in maxima.items():
        print(f"{name}={value:.6e}")
    print(f"inner_type_II_value_at_one_minus_2x={normalization_ii:.6e}")
    print(f"inner_type_I_value_at_one_minus_2x={normalization_i:.6e}")

    worst = max([*maxima.values(), normalization_ii, normalization_i])
    print(f"worst_residual={worst:.6e}")
    if worst >= 1e-10:
        raise SystemExit("verification residual exceeded tolerance")
    print("PASS")


if __name__ == "__main__":
    main()
