#!/usr/bin/env python3
"""Finite-state checks for the bounded-reweighting proof.

This script does not replace the proof.  It checks, by exhaustive summation over
all ordered collision pairs for small Boolean cubes, the exact entropy-production
identity, its rho^2 comparison with J=0, the bounded-reweighting KL inequality,
and the information-projection comparison used in the packet.
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np
from scipy.optimize import minimize


def phi(x: float, y: float) -> float:
    if x == y:
        return 0.0
    if x <= 0.0 or y <= 0.0:
        return np.inf
    return (x - y) * np.log(x / y)


def kl(p: np.ndarray, q: np.ndarray) -> float:
    return float(np.sum(np.where(p > 0.0, p * np.log(p / q), 0.0)))


def tilt(w: np.ndarray, q: np.ndarray) -> np.ndarray:
    z = float(w @ q)
    return w * q / z


def equilibrium_projection(
    p: np.ndarray,
    w: np.ndarray,
    sufficient_statistics: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """KL-project p onto {w exp(<theta,S>)/Z}."""

    target = p @ sufficient_statistics

    def value_grad(theta: np.ndarray) -> tuple[float, np.ndarray]:
        log_weight = np.log(w) + sufficient_statistics @ theta
        shift = float(np.max(log_weight))
        unnormalized = np.exp(log_weight - shift)
        z = float(np.sum(unnormalized))
        mu = unnormalized / z
        value = shift + np.log(z) - float(theta @ target)
        gradient = mu @ sufficient_statistics - target
        return value, gradient

    result = minimize(
        lambda theta: value_grad(theta),
        np.zeros(sufficient_statistics.shape[1]),
        jac=True,
        method="BFGS",
        options={"gtol": 1e-12, "maxiter": 2000},
    )
    if np.linalg.norm(result.jac, ord=np.inf) > 1e-7:
        raise RuntimeError(f"projection did not converge: {result.message}; grad={result.jac}")
    theta = np.asarray(result.x)
    log_weight = np.log(w) + sufficient_statistics @ theta
    log_weight -= np.max(log_weight)
    mu = np.exp(log_weight)
    mu /= np.sum(mu)
    return mu, theta


def exchange(
    states: np.ndarray, state_index: dict[tuple[int, ...], int],
    s: int, t: int, ell: int, k: int,
) -> tuple[int, int]:
    u = states[s].copy()
    v = states[t].copy()
    u[ell], v[k] = v[k], u[ell]
    return state_index[tuple(u)], state_index[tuple(v)]


def entropy_productions(
    p: np.ndarray,
    q: np.ndarray,
    w: np.ndarray,
    states: np.ndarray,
    transport: np.ndarray,
) -> tuple[float, float, float]:
    """Return source D_J, transformed closed form, and source D_0."""

    n = states.shape[1]
    index = {tuple(row): i for i, row in enumerate(states)}
    mu = w / np.sum(w)  # h=0; the dissipation is independent of matching h.
    f = p / mu
    z = float(w @ q)
    d_j_source = 0.0
    d_j_closed = 0.0
    d_zero = 0.0

    for s in range(len(states)):
        for t in range(len(states)):
            for ell in range(n):
                for k in range(n):
                    proposal = transport[ell, k] / n
                    if proposal == 0.0:
                        continue
                    u, v = exchange(states, index, s, t, ell, k)
                    pair_a = w[s] * w[t]
                    pair_b = w[u] * w[v]
                    accept = pair_b / (pair_a + pair_b)

                    d_j_source += (
                        0.25
                        * mu[s]
                        * mu[t]
                        * proposal
                        * accept
                        * phi(f[s] * f[t], f[u] * f[v])
                    )
                    d_j_closed += (
                        0.25
                        * proposal
                        * pair_a
                        * pair_b
                        / (z * z * (pair_a + pair_b))
                        * phi(q[s] * q[t], q[u] * q[v])
                    )
                    d_zero += (
                        0.25
                        * proposal
                        * 0.5
                        * phi(q[s] * q[t], q[u] * q[v])
                    )
    return d_j_source, d_j_closed, d_zero


def run(trials: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    worst_identity = 0.0
    worst_dissipation_slack = np.inf
    worst_kl_slack = np.inf
    worst_projection_slack = np.inf
    worst_final_slack = np.inf
    cases = 0

    for n, blocks in ((2, ((0,), (1,))), (3, ((0, 1), (2,)))):
        states = np.asarray(list(itertools.product((-1, 1), repeat=n)), dtype=int)
        statistic = np.column_stack(
            [np.sum(states[:, block], axis=1) for block in blocks]
        )
        transport = np.zeros((n, n))
        for block in blocks:
            for ell in block:
                for k in block:
                    transport[ell, k] = 1.0 / len(block)

        for _ in range(trials):
            raw_j = rng.normal(scale=1.1, size=(n, n))
            interaction = 0.5 * (raw_j + raw_j.T)
            energy = 0.5 * np.einsum("si,ij,sj->s", states, interaction, states)
            w = np.exp(energy - np.max(energy))
            rho = float(np.min(w) / np.max(w))

            p = rng.dirichlet(np.full(len(states), 0.8))
            q = p / w
            q /= np.sum(q)
            assert np.allclose(tilt(w, q), p, atol=2e-14)

            d_j, d_closed, d_zero = entropy_productions(
                p, q, w, states, transport
            )
            identity_error = abs(d_j - d_closed) / max(1.0, abs(d_j), abs(d_closed))
            worst_identity = max(worst_identity, identity_error)
            dissipation_slack = d_j - rho * rho * d_zero
            worst_dissipation_slack = min(worst_dissipation_slack, dissipation_slack)

            r = rng.dirichlet(np.full(len(states), 0.9))
            kl_slack = (1.0 / rho) * kl(q, r) - kl(tilt(w, q), tilt(w, r))
            worst_kl_slack = min(worst_kl_slack, kl_slack)

            mu_j, _ = equilibrium_projection(p, w, statistic)
            mu_zero, _ = equilibrium_projection(q, np.ones_like(w), statistic)
            i_j = kl(p, mu_j)
            i_zero = kl(q, mu_zero)
            projection_slack = i_zero - rho * i_j
            worst_projection_slack = min(worst_projection_slack, projection_slack)

            # The J=0 nonlinear MLSI is a theorem in the source.  This finite
            # check evaluates the resulting full bound on the sampled laws.
            final_slack = d_j - (rho**3 / (4.0 * n)) * i_j
            worst_final_slack = min(worst_final_slack, final_slack)
            cases += 1

    if worst_identity > 2e-10:
        raise AssertionError(f"entropy-production identity error {worst_identity}")
    for name, slack in (
        ("dissipation comparison", worst_dissipation_slack),
        ("KL reweighting", worst_kl_slack),
        ("projection comparison", worst_projection_slack),
        ("final bound", worst_final_slack),
    ):
        if slack < -2e-9:
            raise AssertionError(f"{name} failed with slack {slack}")

    print(f"verified {cases} randomized positive-law cases")
    print(f"maximum relative identity error: {worst_identity:.3e}")
    print(f"minimum D_J-rho^2 D_0 slack: {worst_dissipation_slack:.3e}")
    print(f"minimum KL comparison slack: {worst_kl_slack:.3e}")
    print(f"minimum information-projection slack: {worst_projection_slack:.3e}")
    print(f"minimum final-inequality slack: {worst_final_slack:.3e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=251105223)
    args = parser.parse_args()
    run(args.trials, args.seed)
