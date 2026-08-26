#!/usr/bin/env python3
"""Global/local optimization of the three-variable 2x2 Alzer defect."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("search", HERE / "search_counterexample.py")
assert SPEC and SPEC.loader
SEARCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEARCH)


def unpack(parameters: np.ndarray) -> list[np.ndarray]:
    matrices = []
    for index in range(3):
        first, second, angle = parameters[3 * index : 3 * index + 3]
        rotation = np.array(
            [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        )
        matrices.append(rotation @ np.diag([first, second]) @ rotation.T)
    return matrices


def objective(parameters: np.ndarray) -> float:
    for index in range(3):
        first, second, angle = parameters[3 * index : 3 * index + 3]
        if not (0.002 <= first <= 0.498 and 0.002 <= second <= 0.498 and 0.0 <= angle <= np.pi):
            return 1e3
    try:
        defect = SEARCH.defect(unpack(parameters))
        return float(np.linalg.eigvalsh(defect)[0])
    except (np.linalg.LinAlgError, FloatingPointError):
        return 1e3


def main() -> None:
    bounds = [(0.002, 0.498), (0.002, 0.498), (0.0, np.pi)] * 3
    result = differential_evolution(
        objective, bounds, seed=180610806, popsize=20, maxiter=500,
        tol=1e-10, polish=False, updating="immediate", workers=1
    )
    local = minimize(
        objective, result.x, method="Powell", bounds=bounds,
        options={"maxiter": 20000, "xtol": 1e-12, "ftol": 1e-14}
    )
    parameters = local.x if local.fun < result.fun else result.x
    matrices = unpack(parameters)
    defect = SEARCH.defect(matrices)
    print(f"minimum={objective(parameters):.16e}")
    print("parameters=", parameters)
    for index, matrix in enumerate(matrices, start=1):
        print(f"A{index}=")
        print(matrix)
        print("eigenvalues=", np.linalg.eigvalsh(matrix))
    print("RHS_minus_LHS=")
    print(defect)
    print("eigenvalues=", np.linalg.eigvalsh(defect))


if __name__ == "__main__":
    main()
