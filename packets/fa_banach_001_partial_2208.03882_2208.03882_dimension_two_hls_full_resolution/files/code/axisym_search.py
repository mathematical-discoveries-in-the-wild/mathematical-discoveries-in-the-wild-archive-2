"""Numerical search for axisymmetric violations of Yaskin's sharp I_p inequality."""

import argparse
import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.special import eval_legendre, gammaln


def lambda_even(n, p, degree):
    # The Fourier transform contributes i^{-degree}=(-1)^{degree/2}.
    return (-1.0) ** (degree // 2) * np.exp(
        gammaln((n - p) / 2)
        + gammaln((degree + p) / 2)
        - gammaln(p / 2)
        - gammaln((degree + n - p) / 2)
    )


def build(n, p, max_degree, nodes):
    if n != 3:
        raise ValueError("This first search uses the Legendre model n=3.")
    t, w = np.polynomial.legendre.leggauss(nodes)
    w = w / 2.0
    degrees = np.arange(0, max_degree + 1, 2)
    basis = np.stack([eval_legendre(int(k), t) for k in degrees], axis=1)
    lambdas = np.array([lambda_even(n, p, int(k)) for k in degrees])
    return t, w, degrees, basis, lambdas


def objective(coeffs, w, basis, lambdas, s, r, opt_dim):
    # Positivity is enforced by exponentiating an even Legendre polynomial.
    logf = basis[:, 1 : opt_dim + 1] @ coeffs
    logf -= np.max(logf)
    f = np.exp(logf)
    # Orthogonal Legendre coefficients under probability measure dt/2.
    degrees = 2 * np.arange(basis.shape[1])
    a = (2 * degrees + 1) * (basis.T @ (w * f))
    image = basis @ (lambdas * a)
    lhs = np.sum(w * np.abs(image) ** r) ** (1.0 / r)
    rhs = np.sum(w * f**s) ** (1.0 / s)
    return -np.log(lhs / rhs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--degree", type=int, default=20)
    parser.add_argument("--transform-degree", type=int, default=80)
    parser.add_argument("--nodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    n = 3
    s = n / (n - args.p)
    r = n / args.p
    if args.transform_degree < args.degree:
        raise ValueError("transform degree must be at least optimization degree")
    _, w, degrees, basis, lambdas = build(
        n, args.p, args.transform_degree, args.nodes
    )
    dim = args.degree // 2
    result = differential_evolution(
        objective,
        [(-6.0, 6.0)] * dim,
        args=(w, basis, lambdas, s, r, dim),
        seed=args.seed,
        popsize=12,
        maxiter=300,
        polish=False,
        workers=1,
        updating="immediate",
    )
    local = minimize(
        objective,
        result.x,
        args=(w, basis, lambdas, s, r, dim),
        method="Nelder-Mead",
        options={"maxiter": 10000, "xatol": 1e-10, "fatol": 1e-12},
    )
    print(
        f"n={n} p={args.p} s={s} r={r} "
        f"degree={args.degree} transform_degree={args.transform_degree}"
    )
    print(f"best_ratio={np.exp(-local.fun):.12g}")
    print("coefficients=" + np.array2string(local.x, precision=8, separator=","))


if __name__ == "__main__":
    main()
