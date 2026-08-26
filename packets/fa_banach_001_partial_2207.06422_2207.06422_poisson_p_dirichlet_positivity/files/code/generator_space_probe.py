"""Search the qubit [sigma]_{p,0}-DBC Lindbladian cone.

The generator is parametrized in GKSL form by a positive 3x3 Kossakowski
matrix and a traceless Hamiltonian. Detailed balance is imposed as a linear
constraint on the resulting 4x4 superoperator.
"""

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import differential_evolution

from numerical_probe import gamma_power, matrix_power, power_operator


PAULIS = [
    np.array([[0, 1], [1, 0]], dtype=complex) / np.sqrt(2),
    np.array([[0, -1j], [1j, 0]], dtype=complex) / np.sqrt(2),
    np.array([[1, 0], [0, -1]], dtype=complex) / np.sqrt(2),
]


def kappa(alpha, value):
    if abs(value - 1) < 1e-12:
        return 1.0
    return alpha / (alpha - 1) * (value ** (alpha - 1) - 1) / (value**alpha - 1)


def coefficient_matrix(theta):
    c00, c11, c22, r01, i01, r02, i02, r12, i12 = theta[:9]
    return np.array(
        [
            [c00, r01 + 1j * i01, r02 + 1j * i02],
            [r01 - 1j * i01, c11, r12 + 1j * i12],
            [r02 - 1j * i02, r12 - 1j * i12, c22],
        ],
        dtype=complex,
    )


def hamiltonian(theta):
    return sum(theta[9 + index] * PAULIS[index] for index in range(3))


def apply_generator(theta, matrix):
    coefficient = coefficient_matrix(theta)
    ham = hamiltonian(theta)
    result = 1j * (ham @ matrix - matrix @ ham)
    for a, fa in enumerate(PAULIS):
        for b, fb in enumerate(PAULIS):
            product = fa.conj().T @ fb
            result += coefficient[a, b] * (
                fa.conj().T @ matrix @ fb
                - (product @ matrix + matrix @ product) / 2
            )
    return result


def superoperator(theta):
    columns = []
    for i in range(2):
        for j in range(2):
            unit = np.zeros((2, 2), dtype=complex)
            unit[i, j] = 1
            columns.append(apply_generator(theta, unit).reshape(-1))
    return np.column_stack(columns)


def metric_matrix(eta, p):
    sigma_values = [eta, 1 - eta]
    diagonal = []
    for i in range(2):
        for j in range(2):
            ratio = sigma_values[i] / sigma_values[j]
            diagonal.append(sigma_values[j] / kappa(1 / p, ratio))
    return np.diag(diagonal)


def detailed_balance_constraints(eta, p):
    metric = metric_matrix(eta, p)
    basis_superoperators = []
    for index in range(12):
        theta = np.zeros(12)
        theta[index] = 1
        basis_superoperators.append(superoperator(theta))
    columns = []
    for generator in basis_superoperators:
        defect = generator.conj().T @ metric - metric @ generator
        columns.append(np.concatenate([defect.real.reshape(-1), defect.imag.reshape(-1)]))
    return np.column_stack(columns)


def sample_generators(eta, p, count=12):
    constraints_matrix = detailed_balance_constraints(eta, p)
    kernel = null_space(constraints_matrix, rcond=1e-9)
    print(
        f"eta={eta} p={p} constraint-rank={12-kernel.shape[1]} "
        f"nullity={kernel.shape[1]}"
    )
    trace_row = np.zeros(12)
    trace_row[:3] = 1
    trace_in_kernel = trace_row @ kernel
    normalized_origin = trace_in_kernel / (trace_in_kernel @ trace_in_kernel)
    trace_zero_kernel = null_space(trace_in_kernel.reshape(1, -1))

    def theta_from_free(free):
        return kernel @ (normalized_origin + trace_zero_kernel @ free)

    def feasibility_objective(free):
        theta = theta_from_free(free)
        smallest_eigenvalue = np.linalg.eigvalsh(coefficient_matrix(theta))[0]
        return -smallest_eigenvalue + 1e-7 * np.dot(free, free)

    free_dimension = trace_zero_kernel.shape[1]
    feasibility = differential_evolution(
        feasibility_objective,
        [(-8, 8)] * free_dimension,
        maxiter=1000,
        popsize=25,
        tol=1e-10,
        polish=True,
        seed=314159,
    )
    central_theta = theta_from_free(feasibility.x)
    central_minimum = np.linalg.eigvalsh(coefficient_matrix(central_theta))[0]
    print(f"  best central Kossakowski minimum={central_minimum:.8g}")
    if central_minimum < -1e-7:
        return []

    rng = np.random.default_rng(12345)
    results = [(central_theta, np.linalg.eigvals(superoperator(central_theta)))]
    attempts = 0
    while len(results) < count and attempts < 20000:
        attempts += 1
        scale = 10 ** rng.uniform(-3, 0.7)
        free = feasibility.x + scale * rng.normal(size=free_dimension)
        numeric_theta = theta_from_free(free)
        if np.linalg.eigvalsh(coefficient_matrix(numeric_theta))[0] < -1e-9:
            continue
        eigenvalues = np.linalg.eigvals(superoperator(numeric_theta))
        results.append((numeric_theta, eigenvalues))
    return results


def dirichlet(vector, eta, p, theta):
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
    generator_x = apply_generator(theta, x)
    inner_product = np.trace(gamma_power(sigma, y, 1) @ generator_x).real
    return -p * (p / (p - 1)) * inner_product / 4


def main():
    for eta in [0.1, 0.25, 0.4]:
        for p in [1.1, 1.5, 1.9]:
            generators = sample_generators(eta, p)
            for index, (theta, eigenvalues) in enumerate(generators):
                result = differential_evolution(
                    lambda vector: dirichlet(vector, eta, p, theta),
                    [(-6, 6)] * 3,
                    maxiter=350,
                    popsize=15,
                    tol=1e-9,
                    seed=1000 + index,
                    polish=True,
                )
                print(
                    f"  sample={index} min={result.fun:.11g} vector={result.x} "
                    f"spectrum={np.sort(eigenvalues.real)}"
                )


if __name__ == "__main__":
    main()
