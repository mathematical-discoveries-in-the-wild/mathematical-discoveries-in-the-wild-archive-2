import numpy as np


def kernel(a: float, z: np.ndarray, w: np.ndarray) -> np.ndarray:
    return 1.0 + a * z[:, None] * np.conjugate(w[None, :])


points = np.exp(2j * np.pi * np.arange(32) / 32)
for a in (0.2, 0.5, 0.8):
    gram = kernel(a, points, points)
    eigenvalues = np.linalg.eigvalsh(gram)
    assert eigenvalues.min() > -1e-10
    assert np.abs(gram).min() >= 1.0 - a - 1e-12
    for theta in np.linspace(0.0, 2.0 * np.pi, 41):
        rotated = np.exp(1j * theta) * points
        assert np.allclose(kernel(a, rotated, rotated), gram)

ka = kernel(0.25, points, points)
kb = kernel(0.50, points, points)
ratio = kb[0, 0] / ka[0, 0]
assert not np.allclose(kb, ratio * ka)
assert not np.isclose(ka[0, 0], ka[0, 16])
print("all checks passed")

