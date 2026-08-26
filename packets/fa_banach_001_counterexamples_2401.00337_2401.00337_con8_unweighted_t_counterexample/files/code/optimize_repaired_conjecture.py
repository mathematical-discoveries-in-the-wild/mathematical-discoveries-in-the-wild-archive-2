import numpy as np
from scipy.linalg import eigh
from scipy.optimize import differential_evolution


def mpow(a, q):
    w, v = eigh((a + a.T) / 2)
    w = np.maximum(w, 1e-14 * np.max(w))
    return (v * (w**q)) @ v.T


def geom(a, b, t=0.5):
    ah = mpow(a, 0.5)
    aih = mpow(a, -0.5)
    return ah @ mpow(aih @ b @ aih, t) @ ah


def pd(params):
    theta, spread, scale = params
    c, s = np.cos(theta), np.sin(theta)
    q = np.array([[c, -s], [s, c]])
    vals = np.exp([scale + spread, scale - spread])
    return (q * vals) @ q.T


def ratio(x, s=1.5, r=1.0, p=1.0, kyfan=1):
    mats = [pd(x[3*j:3*j+3]) for j in range(4)]
    aa, bb = mats[:2], mats[2:]
    left = sum((mpow(geom(mpow(a, s), mpow(b, s)), r) for a, b in zip(aa, bb)),
               np.zeros((2, 2)))
    sa, sb = sum(aa, np.zeros((2, 2))), sum(bb, np.zeros((2, 2)))
    alpha = s * r * p / 4
    right = mpow(mpow(sa, alpha) @ mpow(sb, s*r*p/2) @ mpow(sa, alpha), 1/p)
    sl = np.linalg.eigvalsh((left + left.T)/2)[::-1]
    sr = np.linalg.eigvalsh((right + right.T)/2)[::-1]
    return np.sum(sl[:kyfan]) / np.sum(sr[:kyfan])


bounds = [(0, np.pi), (-5, 5), (-3, 3)] * 4
for s in (1.1, 1.25, 1.5, 1.75, 1.9):
    for r, p in ((1, 1), (2, .5), (2, 1), (5, .2), (5, 1)):
        for k in (1, 2):
            res = differential_evolution(lambda x: -ratio(x, s, r, p, k), bounds,
                                         seed=240100337, maxiter=100, popsize=10,
                                         polish=True, workers=1, updating="immediate")
            print("s,r,p,k,ratio", s, r, p, k, -res.fun)
            if -res.fun > 1.0000001:
                print("FOUND", repr(res.x))
                raise SystemExit
