"""Regression checks for the full Y^2=1 single-2x2-atom reduction.

The script generates finite tracial direct sums with random symmetric corner
matrices A,C and rectangular B.  It checks the exact moment identities,
residual cubic cancellation, and the analytic lower bound for G(v0).
It is numerical evidence only; the packet proof is analytic.
"""

from __future__ import annotations

import numpy as np


def sym(rng: np.random.Generator, n: int) -> np.ndarray:
    x = rng.normal(size=(n, n))
    return (x + x.T) / 2


def one_case(rng: np.random.Generator) -> tuple[float, float]:
    count = int(rng.integers(1, 5))
    dims: list[tuple[int, int]] = []
    blocks: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
    for _ in range(count):
        p = int(rng.integers(1, 6))
        q = int(rng.integers(1, 6))
        dims.append((p, q))
        blocks.append((sym(rng, p), rng.normal(size=(p, q)), sym(rng, q)))
    rho = rng.dirichlet(np.ones(count))

    def tau(fn) -> float:
        return float(sum(r * fn(a, b, c) / (p + q)
                         for r, (p, q), (a, b, c) in zip(rho, dims, blocks)))

    w = tau(lambda a, b, c: np.trace(b @ b.T))
    s = tau(lambda a, b, c: np.trace((b @ b.T) @ (b @ b.T)))
    a_bar = tau(lambda a, b, c: np.trace(a @ b @ b.T)) / w
    c_bar = tau(lambda a, b, c: np.trace(c @ b.T @ b)) / w

    ap = [tau(lambda a, b, c, k=k: np.trace(np.linalg.matrix_power(a, k)))
          for k in range(5)]
    cp = [tau(lambda a, b, c, k=k: np.trace(np.linalg.matrix_power(c, k)))
          for k in range(5)]
    # k=0 above traces identity only inside the corner, as desired.
    ua = tau(lambda a, b, c: np.trace(a @ a @ b @ b.T))
    uc = tau(lambda a, b, c: np.trace(c @ c @ b.T @ b))
    cross = tau(lambda a, b, c: np.trace(a @ b @ c @ b.T))
    va = ua - w * a_bar**2
    vc = uc - w * c_bar**2
    centered_cross = cross - w * a_bar * c_bar
    t_energy = va + vc + centered_cross

    # Base scalar Hankel projections.
    ha = np.array([[ap[0], ap[1]], [ap[1], ap[2]]])
    hc = np.array([[cp[0], cp[1]], [cp[1], cp[2]]])
    ga = np.array([ap[2], ap[3]])
    gc = np.array([cp[2], cp[3]])
    ia = np.linalg.pinv(ha, rcond=1e-12)
    ic = np.linalg.pinv(hc, rcond=1e-12)
    eva = np.array([1.0, a_bar])
    evc = np.array([1.0, c_bar])
    kappa_a = float(eva @ ia @ eva)
    kappa_c = float(evc @ ic @ evc)
    hval_a = float(eva @ ia @ ga)
    hval_c = float(evc @ ic @ gc)
    delta_a = hval_a - a_bar**2
    delta_c = hval_c - c_bar**2
    e_a = ap[4] - float(ga @ ia @ ga)
    e_c = cp[4] - float(gc @ ic @ gc)
    sa2 = s / w**2 - kappa_a
    sc2 = s / w**2 - kappa_c

    if va * va + vc * vc > 1e-24:
        vpar = np.sqrt(va * va + vc * vc) / (np.sqrt(2.0) * w * w)
    else:
        vpar = 0.0
    if vpar == 0.0:
        # Random instances essentially never enter this branch; use a tiny
        # positive value for stable evaluation of the limiting formula.
        vpar = 1e-12
    lam = 1.0 / (s / w**2 + vpar)
    b2 = w / lam

    # Direct residual cubic cancellation.
    plus_direct = np.array([
        ap[0], ap[1], ap[2] + w,
        ap[3] + 2 * w * a_bar + w * c_bar,
    ])
    plus_atom = lam * np.array([
        1, a_bar, a_bar**2 + b2,
        a_bar**3 + b2 * (2 * a_bar + c_bar),
    ])
    plus_expected = np.array(ap[:4]) - lam * np.array(
        [1, a_bar, a_bar**2, a_bar**3]
    )
    minus_direct = np.array([
        cp[0], cp[1], cp[2] + w,
        cp[3] + w * a_bar + 2 * w * c_bar,
    ])
    minus_atom = lam * np.array([
        1, c_bar, c_bar**2 + b2,
        c_bar**3 + b2 * (a_bar + 2 * c_bar),
    ])
    minus_expected = np.array(cp[:4]) - lam * np.array(
        [1, c_bar, c_bar**2, c_bar**3]
    )
    identity_error = max(
        np.max(np.abs(plus_direct - plus_atom - plus_expected)),
        np.max(np.abs(minus_direct - minus_atom - minus_expected)),
    )

    g_value = (
        e_a + e_c + 4 * t_energy - 2 * w * w * vpar
        - delta_a**2 / max(sa2 + vpar, 1e-15)
        - delta_c**2 / max(sc2 + vpar, 1e-15)
    )
    lower = (
        4 * t_energy - 2 * w * w * vpar
        - (va * va + vc * vc) / (w * w * vpar)
    )
    if identity_error > 2e-8 or g_value < lower - 2e-7 or lower < -2e-7:
        raise AssertionError((identity_error, g_value, lower, va, vc, t_energy))
    return identity_error, min(g_value, lower)


def main() -> None:
    rng = np.random.default_rng(20260809)
    max_error = 0.0
    min_margin = np.inf
    for _ in range(5000):
        error, margin = one_case(rng)
        max_error = max(max_error, error)
        min_margin = min(min_margin, margin)
    print(f"cases=5000 max_identity_error={max_error:.3e} min_margin={min_margin:.3e}")


if __name__ == "__main__":
    main()
