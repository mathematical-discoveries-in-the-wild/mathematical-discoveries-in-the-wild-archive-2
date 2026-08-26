"""Finite-matrix sanity checks for the non-Hermitian pencil proof.

This verifies the algebraic decomposition, numerical projection onto the
kernel of the skew-Hermitian part, and the final positive rescaling. It does
not replace the abstract uniform-amplification argument.
"""

from __future__ import annotations

import numpy as np


N_VARS = 3
DEGREE = 3
LEVEL = 2
TRIALS = 200


def pack(xs: list[np.ndarray]) -> np.ndarray:
    return np.concatenate(
        [np.concatenate((x.real.ravel(), x.imag.ravel())) for x in xs]
    )


def unpack(v: np.ndarray) -> list[np.ndarray]:
    block = 2 * LEVEL * LEVEL
    xs = []
    for j in range(N_VARS):
        piece = v[j * block : (j + 1) * block]
        re = piece[: LEVEL * LEVEL].reshape(LEVEL, LEVEL)
        im = piece[LEVEL * LEVEL :].reshape(LEVEL, LEVEL)
        xs.append(re + 1j * im)
    return xs


def eval_p(
    xs: list[np.ndarray], aa: list[np.ndarray], bb: list[np.ndarray]
) -> np.ndarray:
    out = np.zeros((DEGREE * LEVEL, DEGREE * LEVEL), dtype=complex)
    for a, b, x in zip(aa, bb, xs):
        out += np.kron(a, x) + np.kron(b, x.conj().T)
    return out


def hermitian_parts(z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    q = (z + z.conj().T) / 2
    r = (z - z.conj().T) / (2j)
    return q, r


def pack_matrix(z: np.ndarray) -> np.ndarray:
    return np.concatenate((z.real.ravel(), z.imag.ravel()))


def skew_real_matrix(
    aa: list[np.ndarray], bb: list[np.ndarray]
) -> np.ndarray:
    dim = 2 * N_VARS * LEVEL * LEVEL
    cols = []
    for j in range(dim):
        e = np.zeros(dim)
        e[j] = 1.0
        _, r = hermitian_parts(eval_p(unpack(e), aa, bb))
        cols.append(pack_matrix(r))
    return np.column_stack(cols)


def random_matrix(rng: np.random.Generator, size: int) -> np.ndarray:
    return rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))


def main() -> None:
    worst_decomposition = 0.0
    worst_skew_after_projection = 0.0
    worst_feasibility = 0.0

    for seed in range(TRIALS):
        rng = np.random.default_rng(seed)
        aa = [random_matrix(rng, DEGREE) / 8 for _ in range(N_VARS)]
        bb = [random_matrix(rng, DEGREE) / 8 for _ in range(N_VARS)]
        rmat = skew_real_matrix(aa, bb)
        kernel_projection = np.eye(rmat.shape[1]) - np.linalg.pinv(rmat) @ rmat

        xs = [random_matrix(rng, LEVEL) / 3 for _ in range(N_VARS)]
        p_x = eval_p(xs, aa, bb)
        q_x, r_x = hermitian_parts(p_x)
        worst_decomposition = max(
            worst_decomposition, np.linalg.norm(p_x - (q_x + 1j * r_x), ord=2)
        )

        y_vec = kernel_projection @ pack(xs)
        ys = unpack(y_vec)
        p_y = eval_p(ys, aa, bb)
        q_y, r_y = hermitian_parts(p_y)
        worst_skew_after_projection = max(
            worst_skew_after_projection, np.linalg.norm(r_y, ord=2)
        )

        top = float(np.linalg.eigvalsh(q_y).max())
        scale = max(1.0, top)
        zs = [y / scale for y in ys]
        p_z = eval_p(zs, aa, bb)
        identity = np.eye(DEGREE * LEVEL)
        hermitian_error = np.linalg.norm(p_z - p_z.conj().T, ord=2)
        min_eigenvalue = float(
            np.linalg.eigvalsh((identity - p_z + (identity - p_z).conj().T) / 2).min()
        )
        violation = max(hermitian_error, max(0.0, -min_eigenvalue))
        worst_feasibility = max(worst_feasibility, violation)

    tolerance = 5e-9
    assert worst_decomposition < tolerance
    assert worst_skew_after_projection < tolerance
    assert worst_feasibility < tolerance
    print(f"trials={TRIALS}")
    print(f"worst_decomposition_error={worst_decomposition:.3e}")
    print(f"worst_skew_after_projection={worst_skew_after_projection:.3e}")
    print(f"worst_final_feasibility_violation={worst_feasibility:.3e}")
    print("status=PASS")


if __name__ == "__main__":
    main()
