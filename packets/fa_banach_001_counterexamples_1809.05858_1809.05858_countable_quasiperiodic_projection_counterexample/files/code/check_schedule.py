"""Finite-dimensional check of the exact orbit identity in the proof packet."""

from __future__ import annotations

import math

import numpy as np


STAGES = 8
DIM = STAGES + 2


def valuation_two(n: int) -> int:
    value = 0
    while n % 2 == 0:
        value += 1
        n //= 2
    return value


vectors: list[np.ndarray] = [np.eye(DIM)[0]]
step_stage: list[int] = [0]
stage_end: dict[int, int] = {}

for stage in range(1, STAGES + 1):
    count = 2**stage
    theta = math.pi / (2 * count)
    for r in range(1, count + 1):
        vector = np.zeros(DIM)
        vector[stage - 1] = math.cos(r * theta)
        vector[stage] = math.sin(r * theta)
        vectors.append(vector)
        step_stage.append(stage)
    stage_end[stage] = len(vectors) - 1

normals: list[np.ndarray | None] = [None]
cosines: list[float] = [1.0]
safe_index: list[int] = [0]

# Keep only steps whose following stage is available for the safety cutoff.
max_step = stage_end[STAGES - 1]
for step in range(1, max_step + 1):
    previous = vectors[step - 1]
    current = vectors[step]
    cosine = float(previous @ current)
    normal = (previous - cosine * current) / math.sqrt(1 - cosine**2)
    normals.append(normal)
    cosines.append(cosine)
    safe_index.append(stage_end[step_stage[step] + 1])


def project(vector: np.ndarray, normal: np.ndarray) -> np.ndarray:
    return vector - float(vector @ normal) * normal


def scheduled_normal(time: int) -> np.ndarray | None:
    if time % 2 == 1:
        step = (time + 1) // 2
        return normals[step]

    power = valuation_two(time)
    if power >= 2:
        step = power - 1
        if step < len(normals) and time >= 2 * safe_index[step]:
            return normals[step]
    return None


orbit = vectors[0].copy()
scale = 1.0
largest_error = 0.0

for time in range(1, 2 * max_step + 1):
    normal = scheduled_normal(time)
    if normal is not None:
        orbit = project(orbit, normal)

    step = (time + 1) // 2
    if time % 2 == 1:
        scale *= cosines[step]
    expected = scale * vectors[step]
    largest_error = max(largest_error, float(np.linalg.norm(orbit - expected)))

assert largest_error < 1.0e-10, largest_error
assert scale > 0.0
print(f"checked_steps={max_step}")
print(f"largest_orbit_error={largest_error:.3e}")
print(f"finite_product_scale={scale:.12f}")
