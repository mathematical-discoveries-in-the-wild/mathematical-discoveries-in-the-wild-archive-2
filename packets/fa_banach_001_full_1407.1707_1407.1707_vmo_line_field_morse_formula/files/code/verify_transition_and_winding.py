#!/usr/bin/env python3
"""Sanity checks for the double-angle transition and boundary-winding signs.

This is not a proof.  It checks the local matrix identities used in the packet
and finite-difference winding numbers on the disk and annulus.
"""

from __future__ import annotations

import numpy as np


def q_coordinates(v: np.ndarray) -> np.ndarray:
    """Coordinates of sqrt(2)(v⊗v-I/2) in the standard Q-frame."""
    x, y = v
    return np.array([x * x - y * y, 2.0 * x * y])


def winding(z: np.ndarray) -> float:
    phases = np.unwrap(np.angle(z))
    return float((phases[-1] - phases[0]) / (2.0 * np.pi))


def main() -> None:
    theta = np.linspace(0.0, 2.0 * np.pi, 20001)

    # The Q-coordinate of a tangent-frame vector at angle theta is e^{2 i theta}.
    vec = np.stack([np.cos(theta), np.sin(theta)], axis=1)
    q = np.stack([q_coordinates(v) for v in vec])
    expected = np.stack([np.cos(2.0 * theta), np.sin(2.0 * theta)], axis=1)
    transition_error = float(np.max(np.abs(q - expected)))

    # Positively oriented boundary tangent on the unit disk.
    tau = np.stack([-np.sin(theta), np.cos(theta)], axis=1)
    q_tau = np.stack([q_coordinates(v) for v in tau])
    z_tau = q_tau[:, 0] + 1j * q_tau[:, 1]

    # A constant Q-section extends over the disk without zeros.
    z_const = np.ones_like(z_tau)
    relative_disk = z_const / z_tau

    # On an annulus, outer and inner boundary orientations are opposite; the
    # total winding of the tangent-generated reference section is zero.
    outer = winding(z_tau)
    inner = -outer

    print(f"double_angle_max_error={transition_error:.3e}")
    print(f"disk_winding_q_tau={winding(z_tau):.12f}")
    print(f"disk_relative_winding_constant_vs_q_tau={winding(relative_disk):.12f}")
    print(f"disk_relative_euler=2*chi+w={2.0 + winding(relative_disk):.12f}")
    print(f"annulus_total_reference_winding={outer + inner:.12f}")

    assert transition_error < 1e-12
    assert abs(winding(z_tau) - 2.0) < 1e-10
    assert abs(winding(relative_disk) + 2.0) < 1e-10
    assert abs(2.0 + winding(relative_disk)) < 1e-10
    assert abs(outer + inner) < 1e-10


if __name__ == "__main__":
    main()
