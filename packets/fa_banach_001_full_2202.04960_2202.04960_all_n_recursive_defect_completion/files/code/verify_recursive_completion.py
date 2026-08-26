#!/usr/bin/env python3
"""Finite-matrix checks for the recursive defect-completion theorem.

This is numerical evidence only.  The proof in the packet is analytic.
"""

from __future__ import annotations

import numpy as np


RNG = np.random.default_rng(220204960)


def offsets(sizes: list[int]) -> list[int]:
    out = [0]
    for size in sizes:
        out.append(out[-1] + size)
    return out


def assemble(diagonal: list[np.ndarray], off: dict[tuple[int, int], np.ndarray]) -> np.ndarray:
    sizes = [d.shape[0] for d in diagonal]
    pos = offsets(sizes)
    total = pos[-1]
    matrix = np.zeros((total, total))
    for i, d in enumerate(diagonal):
        matrix[pos[i] : pos[i + 1], pos[i] : pos[i + 1]] = d
    for (i, j), a in off.items():
        matrix[pos[i] : pos[i + 1], pos[j] : pos[j + 1]] = a
    return matrix


def diagonal_blocks(defects: list[int], ranks: list[int]) -> list[np.ndarray]:
    blocks = []
    for defect, rank in zip(defects, ranks):
        h = RNG.normal(size=(rank, rank))
        h += (rank + 1.0) * np.eye(rank)
        d = np.zeros((defect + rank, defect + rank))
        d[defect:, defect:] = h
        blocks.append(d)
    return blocks


def positive_defect_and_schur_model() -> tuple[np.ndarray, np.ndarray]:
    # Range defect dimensions (3,1,1), domain defect dimensions (1,1,3).
    # This upper-triangular permutation realizes the recursive matching.
    defect = np.zeros((5, 5))
    defect[0, 0] = 1.0
    defect[3, 1] = 1.0
    defect[1, 2] = 1.0
    defect[2, 3] = 1.0
    defect[4, 4] = 1.0

    # Embed it as the Schur complement of a generic reduced 2x2 block matrix.
    p = RNG.normal(size=(7, 7)) + 8.0 * np.eye(7)
    q = RNG.normal(scale=0.2, size=(7, 5))
    v = RNG.normal(scale=0.2, size=(5, 7))
    w = defect + v @ np.linalg.solve(p, q)
    reduced = np.block([[p, q], [v, w]])
    return reduced, defect


def random_schur_check() -> tuple[float, float]:
    defects = [2, 1, 2, 1]
    ranks = [2, 3, 2, 2]
    diagonal = diagonal_blocks(defects, ranks)
    sizes = [d.shape[0] for d in diagonal]
    off = {
        (i, j): RNG.normal(scale=0.2, size=(sizes[i], sizes[j]))
        for i in range(4)
        for j in range(i + 1, 4)
    }
    full = assemble(diagonal, off)
    pos = offsets(sizes)
    n_idx = [pos[i] + k for i, d in enumerate(defects) for k in range(d)]
    m_idx = [pos[i] + k for i, d in enumerate(defects) for k in range(d, sizes[i])]
    k_idx = n_idx.copy()
    r_idx = m_idx.copy()
    reordered = full[np.ix_(r_idx + k_idx, m_idx + n_idx)]
    rdim = len(r_idx)
    p = reordered[:rdim, :rdim]
    q = reordered[:rdim, rdim:]
    v = reordered[rdim:, :rdim]
    w = reordered[rdim:, rdim:]
    schur = w - v @ np.linalg.solve(p, q)

    # Forbidden defect blocks have i >= j in original indices.
    dpos = offsets(defects)
    forbidden = 0.0
    for i in range(4):
        for j in range(4):
            if i >= j:
                block = schur[dpos[i] : dpos[i + 1], dpos[j] : dpos[j + 1]]
                if block.size:
                    forbidden = max(forbidden, float(np.max(np.abs(block))))
    determinant_error = abs(np.linalg.det(reordered) - np.linalg.det(p) * np.linalg.det(schur))
    return forbidden, determinant_error


def obstructed_rank_trials(trials: int = 500) -> int:
    # Range defect dimensions (1,3,1), domain defect dimensions (3,1,1).
    # Totals agree, but the first 3-dimensional domain block can map only to
    # the first 1-dimensional range block, so every upper-triangular map is singular.
    f = [1, 3, 1]
    e = [3, 1, 1]
    fp = offsets(f)
    ep = offsets(e)
    max_rank = 0
    for _ in range(trials):
        u = np.zeros((sum(f), sum(e)))
        for i in range(3):
            for j in range(i, 3):
                u[fp[i] : fp[i + 1], ep[j] : ep[j + 1]] = RNG.normal(size=(f[i], e[j]))
        max_rank = max(max_rank, int(np.linalg.matrix_rank(u)))
    return max_rank


def main() -> None:
    reduced, defect = positive_defect_and_schur_model()
    print(f"positive defect determinant={np.linalg.det(defect):.6e}")
    print(f"positive reduced determinant={np.linalg.det(reduced):.6e}")
    print(f"positive reduced minimum singular value={np.linalg.svd(reduced, compute_uv=False)[-1]:.6e}")
    forbidden, det_error = random_schur_check()
    print(f"random Schur maximum forbidden block entry={forbidden:.6e}")
    print(f"random Schur determinant identity error={det_error:.6e}")
    print(f"obstructed pattern maximum rank over 500 trials={obstructed_rank_trials()} of 5")


if __name__ == "__main__":
    main()
