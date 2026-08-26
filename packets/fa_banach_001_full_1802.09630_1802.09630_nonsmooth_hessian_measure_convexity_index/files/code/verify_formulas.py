#!/usr/bin/env python3
"""Numerical checks for the nonsmooth Hessian-measure convexity packet."""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def g(t):
    return 0.5 * (1.0 - t) ** 2 + 0.01 * t**0.25


def gp(t):
    return t - 1.0 + 0.0025 * t**-0.75


def gpp(t):
    return 1.0 - 0.001875 * t**-1.75


def spectral_masses(matrix):
    eigenvalues = np.linalg.eigvalsh(matrix)
    positive = np.maximum(eigenvalues, 0.0).sum()
    negative = np.maximum(-eigenvalues, 0.0).sum()
    return positive, negative


def check_matrix_distance(seed=180209630, trials=2000):
    rng = np.random.default_rng(seed)
    for _ in range(trials):
        raw = rng.standard_normal((4, 4))
        hessian = (raw + raw.T) / 2.0
        positive_mass, negative_mass = spectral_masses(hessian)

        raw_psd = rng.standard_normal((4, 4))
        psd = raw_psd @ raw_psd.T
        distance = np.abs(np.linalg.eigvalsh(hessian - psd)).sum()
        assert distance + 1.0e-10 >= negative_mass

        eigenvalues, eigenvectors = np.linalg.eigh(hessian)
        positive_part = (eigenvectors * np.maximum(eigenvalues, 0.0)) @ eigenvectors.T
        exact_distance = np.abs(np.linalg.eigvalsh(hessian - positive_part)).sum()
        assert abs(exact_distance - negative_mass) < 1.0e-9
        assert abs(positive_mass + negative_mass - np.abs(eigenvalues).sum()) < 1.0e-9


def smooth_power_mean_index(beta, lower=0.1, upper=0.9, grid_size=800):
    points = lower + (np.arange(grid_size) + 0.5) * (upper - lower) / grid_size
    x = points[:, None]
    y = points[None, :]
    u = g(x)
    v = g(y)
    log_u = np.log(u)
    log_v = np.log(v)

    logistic_argument = beta * (log_u - log_v)
    weight = np.empty_like(logistic_argument)
    nonnegative = logistic_argument >= 0.0
    weight[nonnegative] = 1.0 / (1.0 + np.exp(-logistic_argument[nonnegative]))
    exponential = np.exp(logistic_argument[~nonnegative])
    weight[~nonnegative] = exponential / (1.0 + exponential)

    log_mean = np.logaddexp(beta * log_u, beta * log_v) - np.log(2.0)
    mean = np.exp(log_mean / beta)

    ax = gp(x) / u
    by = gp(y) / v
    axx = gpp(x) / u - ax**2
    byy = gpp(y) / v - by**2
    mx = weight * ax
    my = (1.0 - weight) * by
    variance = weight * (1.0 - weight)

    hxx = mean * (mx**2 + weight * axx + beta * variance * ax**2)
    hyy = mean * (my**2 + (1.0 - weight) * byy + beta * variance * by**2)
    hxy = mean * (mx * my - beta * variance * ax * by)

    trace = hxx + hyy
    discriminant = np.sqrt((hxx - hyy) ** 2 + 4.0 * hxy**2)
    lambda_plus = (trace + discriminant) / 2.0
    lambda_minus = (trace - discriminant) / 2.0
    positive_mass = np.maximum(lambda_plus, 0.0).sum() + np.maximum(lambda_minus, 0.0).sum()
    total_mass = np.abs(lambda_plus).sum() + np.abs(lambda_minus).sum()
    return positive_mass / total_mass


def check_concrete_limit():
    lower, upper = 0.1, 0.9
    interface_mass = 2.0 * quad(lambda t: abs(gp(t)), lower, upper, epsabs=1.0e-13)[0]

    # g is strictly decreasing and convex on [0.1, 0.9].  For the minimum,
    # the selected smooth branch has weight (t-lower), while the ridge is negative.
    positive_bulk_min = 2.0 * quad(
        lambda t: (t - lower) * gpp(t), lower, upper, epsabs=1.0e-13
    )[0]
    nonsmooth_min_index = positive_bulk_min / (positive_bulk_min + interface_mass)

    computed_min_index = smooth_power_mean_index(-100.0, lower, upper)
    computed_max_index = smooth_power_mean_index(100.0, lower, upper)
    assert abs(computed_min_index - nonsmooth_min_index) < 2.0e-3
    assert abs(computed_max_index - 1.0) < 1.0e-10

    print(f"interface mass J = {interface_mass:.12f}")
    print(f"positive bulk mass for min = {positive_bulk_min:.12f}")
    print(f"nonsmooth min index = {nonsmooth_min_index:.12f}")
    print(f"beta=-100 smooth index = {computed_min_index:.12f}")
    print(f"beta=+100 smooth index = {computed_max_index:.12f}")


if __name__ == "__main__":
    check_matrix_distance()
    check_concrete_limit()
    print("all checks passed")
