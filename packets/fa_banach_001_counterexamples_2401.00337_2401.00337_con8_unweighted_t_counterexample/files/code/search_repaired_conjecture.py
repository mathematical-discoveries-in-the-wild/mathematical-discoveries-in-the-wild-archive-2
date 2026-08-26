import numpy as np
from scipy.linalg import eigh


def mpow(a, q):
    w, v = eigh((a + a.conj().T) / 2)
    if np.min(w) <= -1e-10 * np.max(w):
        raise ValueError("not positive definite")
    w = np.maximum(w, 1e-14 * np.max(w))
    return (v * (w**q)) @ v.conj().T


def geom(a, b, t):
    ah = mpow(a, 0.5)
    aih = mpow(a, -0.5)
    return ah @ mpow(aih @ b @ aih, t) @ ah


def random_pd(n, rng, spread=3.5):
    q, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    vals = np.exp(rng.uniform(-spread, spread, size=n))
    return (q * vals) @ q.conj().T


def evaluate(aa, bb, s, t, r, p):
    left = sum((mpow(geom(mpow(a, s), mpow(b, s), t), r) for a, b in zip(aa, bb)),
               np.zeros_like(aa[0]))
    sa = sum(aa, np.zeros_like(aa[0]))
    sb = sum(bb, np.zeros_like(bb[0]))
    alpha = (1 - t) * s * r * p / 2
    middle = mpow(sa, alpha) @ mpow(sb, t * s * r * p) @ mpow(sa, alpha)
    right = mpow(middle, 1 / p)
    sl = np.linalg.svd(left, compute_uv=False)
    sr = np.linalg.svd(right, compute_uv=False)
    return sl, sr


rng = np.random.default_rng(240100337)
best = (0.0, None)
for n in (2, 3):
    for m in (1, 2, 3, 4):
        for s in (1.01, 1.1, 1.25, 1.5, 1.75, 1.9, 1.99):
            for t in (0.5,):
                for r, p in ((1, 1), (1, 2), (1, 5), (1.5, 2/3), (2, 0.5),
                             (2, 1), (3, 1/3), (3, 1), (5, 0.2), (5, 1)):
                    for _ in range(500):
                        aa = [random_pd(n, rng) for _ in range(m)]
                        bb = [random_pd(n, rng) for _ in range(m)]
                        sl, sr = evaluate(aa, bb, s, t, r, p)
                        for k in range(1, n + 1):
                            ratio = np.sum(sl[:k]) / np.sum(sr[:k])
                            if ratio > best[0]:
                                best = (ratio, (n, m, s, t, r, p, k, aa, bb, sl, sr))
                            if ratio > 1.000001:
                                print("FOUND", ratio, "n,m,s,t,r,p,k=", n, m, s, t, r, p, k)
                                print("sl", sl, "sr", sr)
                                for j, (a, b) in enumerate(zip(aa, bb)):
                                    print("A", j, repr(a))
                                    print("B", j, repr(b))
                                raise SystemExit

print("NO VIOLATION; best ratio", best[0])
if best[1] is not None:
    print("best parameters", best[1][:7])
    print("sl", best[1][-2], "sr", best[1][-1])
