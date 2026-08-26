"""Numerical probe for the explicit qubit [sigma]_{p,0}-DBC example.

This implements the channel in Appendix A of arXiv:2207.06422 and searches
for non-positive p-Dirichlet entropy production away from the invariant state.
"""

import numpy as np
from scipy.optimize import differential_evolution


def matrix_power(matrix, exponent):
    eigenvalues, eigenvectors = np.linalg.eigh((matrix + matrix.conj().T) / 2)
    return (eigenvectors * (eigenvalues**exponent)) @ eigenvectors.conj().T


def gamma_power(sigma, matrix, exponent):
    sigma_half_power = matrix_power(sigma, exponent / 2)
    return sigma_half_power @ matrix @ sigma_half_power


def power_operator(sigma, matrix, q, p):
    weighted = gamma_power(sigma, matrix, 1 / p)
    return gamma_power(sigma, matrix_power(weighted, p / q), -1 / q)


def channel(matrix, eta):
    k1 = np.diag([np.sqrt(eta), np.sqrt(1 - eta)])
    k2 = np.array([[0, np.sqrt(eta)], [np.sqrt(1 - eta), 0]], dtype=complex)
    return k1.conj().T @ matrix @ k1 + k2.conj().T @ matrix @ k2


def hs_adjoint(kraus_operators, matrix):
    return sum(k @ matrix @ k.conj().T for k in kraus_operators)


def apply_gamma(sigma, matrix):
    root = matrix_power(sigma, 0.5)
    return root @ matrix @ root


def apply_gamma_inverse(sigma, matrix):
    inverse_root = matrix_power(sigma, -0.5)
    return inverse_root @ matrix @ inverse_root


def kappa(alpha, value):
    if abs(value - 1) < 1e-10:
        return 1.0
    return alpha / (alpha - 1) * (value ** (alpha - 1) - 1) / (value**alpha - 1)


def bracket_inverse(sigma, matrix, p):
    eigenvalues, eigenvectors = np.linalg.eigh(sigma)
    in_basis = eigenvectors.conj().T @ matrix @ eigenvectors
    result = np.empty_like(in_basis)
    for i in range(2):
        for j in range(2):
            result[i, j] = (
                kappa(1 / p, eigenvalues[i] / eigenvalues[j])
                / eigenvalues[j]
                * in_basis[i, j]
            )
    return eigenvectors @ result @ eigenvectors.conj().T


def appendix_tilde_channel(matrix, p):
    v1 = np.array([1, 1], dtype=complex) / np.sqrt(2)
    v2 = np.array([1, 2], dtype=complex) / np.sqrt(5)
    k1 = np.outer(v1, np.array([1, 0], dtype=complex))
    k2 = np.outer(v2, np.array([0, 1], dtype=complex))
    kraus = [k1, k2]
    sigma = np.array([[2, 3], [3, 5]], dtype=complex) / 7

    def phi(value):
        return sum(k.conj().T @ value @ k for k in kraus)

    def phi_kms_adjoint(value):
        return apply_gamma_inverse(sigma, hs_adjoint(kraus, apply_gamma(sigma, value)))

    def psi(value):
        return phi_kms_adjoint(phi(value))

    # Obtain the Hilbert--Schmidt adjoint of Psi from its matrix representation.
    basis = []
    for i in range(2):
        for j in range(2):
            unit = np.zeros((2, 2), dtype=complex)
            unit[i, j] = 1
            basis.append(unit)
    superoperator = np.column_stack([psi(unit).reshape(-1) for unit in basis])
    # numpy's row-major flattening uses the same ordered basis above.
    psi_adjoint_vector = superoperator.conj().T @ apply_gamma(sigma, matrix).reshape(-1)
    psi_adjoint_value = psi_adjoint_vector.reshape(2, 2)
    return bracket_inverse(sigma, psi_adjoint_value, p)


def appendix_dirichlet_from_unconstrained_bloch(vector, p):
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)
    bloch = np.tanh(norm) * vector / norm if norm else vector
    rho = np.array(
        [
            [1 + bloch[2], bloch[0] - 1j * bloch[1]],
            [bloch[0] + 1j * bloch[1], 1 - bloch[2]],
        ],
        dtype=complex,
    ) / 2
    sigma = np.array([[2, 3], [3, 5]], dtype=complex) / 7
    x = gamma_power(sigma, rho, -1)
    y = power_operator(sigma, x, p / (p - 1), p)
    generator_x = appendix_tilde_channel(x, p) - x
    inner_product = np.trace(gamma_power(sigma, y, 1) @ generator_x).real
    return -p * (p / (p - 1)) * inner_product / 4


def dirichlet_from_unconstrained_bloch(vector, eta, p):
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)
    bloch = np.tanh(norm) * vector / norm if norm else vector
    rho = np.array(
        [
            [1 + bloch[2], bloch[0] - 1j * bloch[1]],
            [bloch[0] + 1j * bloch[1], 1 - bloch[2]],
        ],
        dtype=complex,
    ) / 2
    sigma = np.diag([eta, 1 - eta]).astype(complex)
    x = gamma_power(sigma, rho, -1)
    y = power_operator(sigma, x, p / (p - 1), p)
    generator_x = channel(x, eta) - x
    inner_product = np.trace(gamma_power(sigma, y, 1) @ generator_x).real
    return -p * (p / (p - 1)) * inner_product / 4


def main():
    minima = []
    for eta in [0.02, 0.05, 0.1, 0.2, 0.35, 0.49]:
        for p in [1.05, 1.2, 1.5, 1.8, 1.95]:
            result = differential_evolution(
                lambda vector: dirichlet_from_unconstrained_bloch(vector, eta, p),
                [(-6, 6)] * 3,
                tol=1e-10,
                popsize=20,
                maxiter=600,
                polish=True,
                seed=123,
            )
            minima.append((result.fun, eta, p, result.x))
            print(
                f"eta={eta:.2g} p={p:.2g} min={result.fun:.12g} "
                f"vector={result.x}"
            )
    print("global", min(minima, key=lambda item: item[0]))

    print("testing the transformed non-KMS appendix channel")
    appendix_minima = []
    for p in [1.05, 1.2, 1.5, 1.8, 1.95]:
        result = differential_evolution(
            lambda vector: appendix_dirichlet_from_unconstrained_bloch(vector, p),
            [(-6, 6)] * 3,
            tol=1e-10,
            popsize=20,
            maxiter=600,
            polish=True,
            seed=456,
        )
        appendix_minima.append((result.fun, p, result.x))
        print(f"p={p:.2g} min={result.fun:.12g} vector={result.x}")
    print("appendix global", min(appendix_minima, key=lambda item: item[0]))


if __name__ == "__main__":
    main()
