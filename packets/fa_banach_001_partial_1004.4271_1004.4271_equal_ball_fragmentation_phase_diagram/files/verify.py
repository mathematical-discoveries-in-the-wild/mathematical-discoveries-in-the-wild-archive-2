import math
import numpy as np
from scipy.optimize import minimize


a = (36.0 * math.pi) ** (1.0 / 3.0)
b = (2.0 / 5.0) * (3.0 / (4.0 * math.pi)) ** (2.0 / 3.0)


def f(x):
    return a * x ** (2.0 / 3.0) + b * x ** (5.0 / 3.0)


def transition(n):
    x = n ** (1.0 / 3.0)
    y = (n + 1) ** (1.0 / 3.0)
    return (a / b) * x * x * y * y / (x + y)


assert abs(a / b - 10.0 * math.pi) < 1e-12
assert abs(a / (5.0 * b) - 2.0 * math.pi) < 1e-12
assert abs(a / (2.0 * b) - 5.0 * math.pi) < 1e-12

thresholds = [transition(n) for n in range(1, 80)]
assert all(x < y for x, y in zip(thresholds, thresholds[1:]))
assert abs(thresholds[0] - 22.066998682967206) < 1e-11

for n, mn in enumerate(thresholds[:25], start=1):
    fn = n * f(mn / n)
    fn1 = (n + 1) * f(mn / (n + 1))
    assert abs(fn - fn1) <= 2e-11 * max(1.0, fn)

# At a mixed stationary point y=r^3 x, the positive curvature is strictly
# smaller in magnitude than the negative curvature at x.
for r in np.geomspace(1.000001, 1e5, 1000):
    ratio = (2.0 * r + 1.0) / (r ** 3 * (r + 2.0))
    assert 0.0 < ratio < 1.0

# Numerical stress test: random finite simplices agree with the exact envelope.
rng = np.random.default_rng(10044271)
for total in np.geomspace(0.2, 500.0, 40):
    exact = min(n * f(total / n) for n in range(1, 250))
    for k in range(2, 10):
        for _ in range(50):
            masses = total * rng.dirichlet(np.ones(k))
            assert sum(f(float(x)) for x in masses) >= exact - 1e-10

print("a/b", a / b)
print("inflection_mass", a / (5.0 * b))
print("asymptotic_component_mass", a / (2.0 * b))
print("first_transition", thresholds[0])
print("verified_transitions", len(thresholds))
print("random_partition_checks", 40 * 8 * 50)
