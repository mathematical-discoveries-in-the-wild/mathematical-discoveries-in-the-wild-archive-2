#!/usr/bin/env python3
"""Finite-Trotter probes for the XXZ quantum transfer matrix in arXiv:2305.06679.

This is diagnostic only.  It implements the monodromy matrix displayed in the
paper's proof of Theorem 1.2, traces out the auxiliary spin, and checks simple
Perron--Frobenius routes (entrywise positivity, diagonal phase gauges, and
positive low powers).
"""

from __future__ import annotations

import argparse
import collections
import math

import numpy as np


def r_matrix(lam: complex, eta: complex) -> np.ndarray:
    a = np.sinh(eta + lam) / np.sinh(eta)
    b = np.sinh(lam) / np.sinh(eta)
    return np.array(
        [[a, 0, 0, 0], [0, b, 1, 0], [0, 1, b, 0], [0, 0, 0, a]],
        dtype=complex,
    )


def six_vertex_matrix(a: float, b: float, c: float = 1.0) -> np.ndarray:
    return np.array(
        [[a, 0, 0, 0], [0, b, c, 0], [0, c, b, 0], [0, 0, 0, a]],
        dtype=float,
    )


def partial_transpose_first(op: np.ndarray) -> np.ndarray:
    tensor = op.reshape(2, 2, 2, 2)  # out_a, out_b, in_a, in_b
    return tensor.transpose(2, 1, 0, 3).reshape(4, 4)


def embed_two_site(op: np.ndarray, first: int, second: int, site_count: int) -> np.ndarray:
    """Embed op whose local tensor order is (first, second)."""
    dim = 1 << site_count
    out = np.zeros((dim, dim), dtype=complex)
    for col in range(dim):
        in_first = (col >> (site_count - 1 - first)) & 1
        in_second = (col >> (site_count - 1 - second)) & 1
        local_col = 2 * in_first + in_second
        for local_row in range(4):
            coeff = op[local_row, local_col]
            if abs(coeff) < 1e-15:
                continue
            out_first, out_second = divmod(local_row, 2)
            row = col
            mask_first = 1 << (site_count - 1 - first)
            mask_second = 1 << (site_count - 1 - second)
            row = (row | mask_first) if out_first else (row & ~mask_first)
            row = (row | mask_second) if out_second else (row & ~mask_second)
            out[row, col] += coeff
    return out


def qtm(n: int, temperature: float, zeta: float, field: float, coupling: float) -> np.ndarray:
    # The paper has aleph=-i J sin(zeta)/T and eta=-i*zeta.
    eta = -1j * zeta
    lam = 1j * coupling * math.sin(zeta) / (n * temperature)
    r = r_matrix(lam, eta)
    rt = partial_transpose_first(r)
    site_count = 2 * n + 1  # auxiliary site 0, quantum sites 1,...,2N
    monodromy = np.eye(1 << site_count, dtype=complex)
    # Written product: R_{2N,0}^{t_{2N}} R_{0,2N-1} ... R_{2,0}^{t_2} R_{0,1} field.
    for k in range(n, 0, -1):
        monodromy = monodromy @ embed_two_site(rt, 2 * k, 0, site_count)
        monodromy = monodromy @ embed_two_site(r, 0, 2 * k - 1, site_count)
    aux_field = np.diag([math.exp(field / (2 * temperature)), math.exp(-field / (2 * temperature))])
    monodromy = monodromy @ np.kron(aux_field, np.eye(1 << (2 * n)))
    qdim = 1 << (2 * n)
    blocks = monodromy.reshape(2, qdim, 2, qdim)
    return blocks[0, :, 0, :] + blocks[1, :, 1, :]


def positive_staggered_transfer(
    n: int, temperature: float, zeta: float, field: float, coupling: float
) -> np.ndarray:
    """The positive transfer matrix appearing in the signed-block reduction."""
    u = coupling * math.sin(zeta) / (n * temperature)
    a = math.sin(zeta - u) / math.sin(zeta)
    d = math.sin(u) / math.sin(zeta)
    if not (a > 0 and d > 0):
        raise ValueError("positive-weight regime requires 0 < u < zeta")
    odd = six_vertex_matrix(a, d)
    even = six_vertex_matrix(d, a)
    site_count = 2 * n + 1
    monodromy = np.eye(1 << site_count)
    for k in range(n, 0, -1):
        monodromy = monodromy @ embed_two_site(even, 2 * k, 0, site_count)
        monodromy = monodromy @ embed_two_site(odd, 0, 2 * k - 1, site_count)
    aux_field = np.diag([math.exp(field / (2 * temperature)), math.exp(-field / (2 * temperature))])
    monodromy = monodromy @ np.kron(aux_field, np.eye(1 << (2 * n)))
    qdim = 1 << (2 * n)
    blocks = monodromy.reshape(2, qdim, 2, qdim)
    return blocks[0, :, 0, :] + blocks[1, :, 1, :]


def signed_reduction_residual(
    n: int, temperature: float, zeta: float, field: float, coupling: float
) -> float:
    raw = qtm(n, temperature, zeta, field, coupling)
    positive = positive_staggered_transfer(n, temperature, zeta, field, coupling)
    dimension = 1 << (2 * n)
    permutation = []
    for state in range(dimension):
        flipped = state
        for site in range(2, 2 * n + 1, 2):
            flipped ^= 1 << (2 * n - site)
        permutation.append(flipped)
    conjugated = raw[np.ix_(permutation, permutation)]
    parity = np.diag([(-1) ** state.bit_count() for state in range(dimension)])
    predicted = ((-1) ** n) * parity @ positive
    return float(np.max(np.abs(conjugated - predicted)))


def diagonal_phase_gauge(matrix: np.ndarray, tol: float = 1e-10) -> tuple[bool, float]:
    """Can D^{-1} A D be entrywise nonnegative real for diagonal unitary D?"""
    size = matrix.shape[0]
    theta: list[float | None] = [None] * size
    adjacency: list[list[tuple[int, float]]] = [[] for _ in range(size)]
    rows, cols = np.nonzero(np.abs(matrix) > tol)
    for i, j in zip(rows, cols):
        # arg(A_ij) + theta_j - theta_i = 0 mod 2*pi.
        alpha = float(np.angle(matrix[i, j]))
        adjacency[i].append((j, -alpha))  # theta_j = theta_i-alpha
        adjacency[j].append((i, alpha))
    worst = 0.0
    for root in range(size):
        if theta[root] is not None:
            continue
        theta[root] = 0.0
        todo = collections.deque([root])
        while todo:
            i = todo.popleft()
            assert theta[i] is not None
            for j, delta in adjacency[i]:
                candidate = theta[i] + delta
                if theta[j] is None:
                    theta[j] = candidate
                    todo.append(j)
                else:
                    residual = math.remainder(theta[j] - candidate, 2 * math.pi)
                    worst = max(worst, abs(residual))
                    if abs(residual) > 1e-7:
                        return False, worst
    return True, worst


def diagnostics(matrix: np.ndarray) -> dict[str, object]:
    tol = 1e-10
    real = np.real_if_close(matrix, tol=1000)
    imag_max = float(np.max(np.abs(matrix.imag)))
    negatives = int(np.sum(real.real < -tol))
    positives = int(np.sum(real.real > tol))
    gauge, residual = diagonal_phase_gauge(matrix, tol)
    vals = np.linalg.eigvals(matrix)
    moduli = np.sort(np.abs(vals))[::-1]
    gap = float(moduli[0] - moduli[1])
    ratio = float(moduli[1] / moduli[0]) if moduli[0] else math.inf
    positive_power = None
    nonnegative_powers: list[int] = []
    negative_counts_by_power: list[int] = []
    power = np.eye(matrix.shape[0], dtype=complex)
    for exponent in range(1, 9):
        power = power @ matrix
        negative_count = int(np.sum(power.real < -tol)) if np.max(np.abs(power.imag)) < tol else -1
        negative_counts_by_power.append(negative_count)
        if negative_count == 0:
            nonnegative_powers.append(exponent)
        if np.max(np.abs(power.imag)) < tol and np.min(power.real) > tol:
            positive_power = exponent
            break
    n = int(round(math.log2(matrix.shape[0]) / 2))
    sectors: dict[int, list[int]] = collections.defaultdict(list)
    for basis in range(matrix.shape[0]):
        bits = [(basis >> (2 * n - site)) & 1 for site in range(1, 2 * n + 1)]
        charge = sum(bits[0::2]) - sum(bits[1::2])
        sectors[charge].append(basis)
    sector_data: dict[int, tuple[int, float, str]] = {}
    for charge, indices in sorted(sectors.items()):
        block = matrix[np.ix_(indices, indices)]
        radius = float(np.max(np.abs(np.linalg.eigvals(block))))
        signs = set(np.sign(block.real[np.abs(block) > tol]).astype(int).tolist())
        sector_data[charge] = (len(indices), radius, "/".join(map(str, sorted(signs))))
    off_sector_max = 0.0
    for charge, indices in sectors.items():
        outside = [j for other, js in sectors.items() if other != charge for j in js]
        off_sector_max = max(off_sector_max, float(np.max(np.abs(matrix[np.ix_(indices, outside)]))))
    return {
        "dimension": matrix.shape[0],
        "max_imaginary_entry": imag_max,
        "positive_entries": positives,
        "negative_entries": negatives,
        "diagonal_phase_gauge": gauge,
        "gauge_cycle_residual": residual,
        "dominant_modulus": float(moduli[0]),
        "second_modulus": float(moduli[1]),
        "spectral_gap": gap,
        "second_to_first_ratio": ratio,
        "strictly_positive_power_le_8": positive_power,
        "nonnegative_powers_le_8": nonnegative_powers,
        "negative_counts_by_power": negative_counts_by_power,
        "off_sector_max": off_sector_max,
        "sector_size_radius_signs": sector_data,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=4)
    args = parser.parse_args()
    for n in range(1, args.max_n + 1):
        for zeta in (0.7, 1.1, 2.0):
            for temperature in (0.2, 0.5, 1.0, 5.0):
                matrix = qtm(n, temperature, zeta, field=0.7, coupling=1.0)
                report = diagnostics(matrix)
                if temperature == 1.0:
                    report["signed_reduction_residual"] = signed_reduction_residual(
                        n, temperature, zeta, 0.7, 1.0
                    )
                fields = " ".join(f"{key}={value}" for key, value in report.items())
                print(f"N={n} zeta={zeta} T={temperature} {fields}")


if __name__ == "__main__":
    main()
