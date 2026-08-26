"""Finite-field search for the rank-one frame-path reformulation.

For k=n-1, a rank-n completion of the normalized block cycle exists if there
are full-column-rank (k+1)-by-k matrices

    X_0=[I;0], X_1, ..., X_{k+1}=[H^{-1};0]

such that each difference X_{i+1}-X_i has rank one and the two adjacent
column spaces span the ambient (k+1)-space.  This script exhaustively checks
small prime fields and records the shortest path lengths.
"""

from __future__ import annotations

from collections import deque
from itertools import product


def rank_mod(rows: tuple[tuple[int, ...], ...], p: int) -> int:
    a = [list(row) for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % p, -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] % p:
                q = a[i][c] % p
                a[i] = [(x - q * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def mat(rows: list[list[int]]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(row) for row in rows)


def mul(a, b, p):
    return mat(
        [
            [sum(a[i][t] * b[t][j] for t in range(len(b))) % p for j in range(len(b[0]))]
            for i in range(len(a))
        ]
    )


def inverse(a, p):
    k = len(a)
    aug = [list(a[i]) + [int(i == j) for j in range(k)] for i in range(k)]
    for c in range(k):
        pivot = next(i for i in range(c, k) if aug[i][c] % p)
        aug[c], aug[pivot] = aug[pivot], aug[c]
        inv = pow(aug[c][c] % p, -1, p)
        aug[c] = [(inv * x) % p for x in aug[c]]
        for i in range(k):
            if i != c and aug[i][c] % p:
                q = aug[i][c] % p
                aug[i] = [(x - q * y) % p for x, y in zip(aug[i], aug[c])]
    return mat([row[k:] for row in aug])


def dot(x, y, p):
    return sum(a * b for a, b in zip(x, y)) % p


def columns_to_matrix(columns):
    return mat([[columns[j][i] for j in range(len(columns))] for i in range(len(columns[0]))])


def strong_basis(a, p):
    """Find S such that S^{-1}AS has all leading principal minors nonzero.

    This implements the induction used in the proof packet.  Write A in a
    decomposition Fv + ker(f), where f(v)=1 and f(Av) is nonzero.  Its first
    pivot is then nonzero, while the Schur complement is invertible; recurse
    on that complement.
    """
    k = len(a)
    if k == 1:
        return mat([[1]])
    vectors = list(product(range(p), repeat=k))
    pair = None
    for v in vectors:
        if not any(v):
            continue
        av = tuple(sum(a[i][j] * v[j] for j in range(k)) % p for i in range(k))
        for f in vectors:
            if dot(f, v, p) == 1 and dot(f, av, p):
                pair = v, f
                break
        if pair:
            break
    if pair is None:
        raise RuntimeError("failed to find the first pivot")
    v, f = pair
    pivot = next(i for i, value in enumerate(f) if value)
    fp_inv = pow(f[pivot], -1, p)
    kernel_basis = []
    for j in range(k):
        if j == pivot:
            continue
        w = [0] * k
        w[j] = 1
        w[pivot] = (-f[j] * fp_inv) % p
        kernel_basis.append(tuple(w))
    b = columns_to_matrix([v] + kernel_basis)
    b_inv = inverse(b, p)
    in_split_basis = mul(mul(b_inv, a, p), b, p)
    alpha = in_split_basis[0][0]
    alpha_inv = pow(alpha, -1, p)
    schur = mat(
        [
            [
                (in_split_basis[i][j] - in_split_basis[i][0] * alpha_inv * in_split_basis[0][j])
                % p
                for j in range(1, k)
            ]
            for i in range(1, k)
        ]
    )
    t = strong_basis(schur, p)
    block_t = mat(
        [[1] + [0] * (k - 1)]
        + [[0] + list(t[i]) for i in range(k - 1)]
    )
    return mul(b, block_t, p)


def constructive_path(endpoint, p):
    """Construct the lift-and-replace path from [I;0] to [endpoint;0]."""
    k = len(endpoint)
    s = strong_basis(endpoint, p)
    s_inv = inverse(s, p)
    c = mul(mul(s_inv, endpoint, p), s, p)
    ident = mat([[int(i == j) for j in range(k)] for i in range(k)])
    r = [0] * k

    # Choose the lift row backwards.  At stage j the relevant determinant is
    # affine in r_j, and its coefficient is the j-th leading minor of C.
    for j in reversed(range(k)):
        for value in range(p):
            r[j] = value
            current_columns = []
            for ell in range(k):
                if ell < j:
                    current_columns.append(tuple(list(c[row][ell] for row in range(k)) + [0]))
                else:
                    current_columns.append(tuple(list(ident[row][ell] for row in range(k)) + [r[ell]]))
            target_j = tuple(list(c[row][j] for row in range(k)) + [0])
            if rank_mod(columns_to_matrix(current_columns + [target_j]), p) == k + 1:
                break
        else:
            raise RuntimeError("failed to choose a lift coordinate")

    frames = [mat([list(row) for row in ident] + [[0] * k])]
    lifted = mat([list(row) for row in ident] + [r])
    frames.append(lifted)
    for j in range(k):
        next_frame = [list(row) for row in frames[-1]]
        for row in range(k):
            next_frame[row][j] = c[row][j]
        next_frame[k][j] = 0
        frames.append(mat(next_frame))

    # Undo the similarity: X maps to diag(S,1) X S^{-1}.
    left = mat([list(s[i]) + [0] for i in range(k)] + [[0] * k + [1]])
    return [mul(mul(left, x, p), s_inv, p) for x in frames]


def validate_constructive_paths(k, p):
    total = 0
    for entries in product(range(p), repeat=k * k):
        a = mat([list(entries[i * k : (i + 1) * k]) for i in range(k)])
        if rank_mod(a, p) < k:
            continue
        total += 1
        path = constructive_path(a, p)
        assert len(path) == k + 2
        start = mat([[int(i == j) for j in range(k)] for i in range(k)] + [[0] * k])
        target = mat([list(row) for row in a] + [[0] * k])
        assert path[0] == start and path[-1] == target
        for x, y in zip(path, path[1:]):
            difference = mat([[(y[i][j] - x[i][j]) % p for j in range(k)] for i in range(k + 1)])
            joined = mat([list(x[i]) + list(y[i]) for i in range(k + 1)])
            assert rank_mod(difference, p) == 1
            assert rank_mod(joined, p) == k + 1
    return total


def add_rank_one(a, w, phi, p):
    return mat(
        [
            [(a[i][j] + w[i] * phi[j]) % p for j in range(len(phi))]
            for i in range(len(w))
        ]
    )


def column_space_contains(a, w, p):
    joined = tuple(tuple(list(a[i]) + [w[i]]) for i in range(len(a)))
    return rank_mod(joined, p) == len(a[0])


def neighbors(a, p):
    rows, k = len(a), len(a[0])
    seen = set()
    for w in product(range(p), repeat=rows):
        if not any(w) or column_space_contains(a, w, p):
            continue
        for phi in product(range(p), repeat=k):
            if not any(phi):
                continue
            b = add_rank_one(a, w, phi, p)
            if b not in seen:
                seen.add(b)
                yield b


def distances(k: int, p: int):
    x = mat([[int(i == j) for j in range(k)] for i in range(k)] + [[0] * k])
    dist = {x: 0}
    queue = deque([x])
    while queue:
        a = queue.popleft()
        for b in neighbors(a, p):
            if b not in dist:
                dist[b] = dist[a] + 1
                queue.append(b)

    qualifying = 0
    histogram: dict[int, int] = {}
    missing = []
    for entries in product(range(p), repeat=k * k):
        h = mat([list(entries[i * k : (i + 1) * k]) for i in range(k)])
        ident = mat([[int(i == j) for j in range(k)] for i in range(k)])
        h_minus_i = mat([[(h[i][j] - ident[i][j]) % p for j in range(k)] for i in range(k)])
        if rank_mod(h, p) < k or rank_mod(h_minus_i, p) < k:
            continue
        qualifying += 1
        hinv = inverse(h, p)
        y = mat([list(row) for row in hinv] + [[0] * k])
        d = dist.get(y)
        if d is None:
            missing.append(h)
        else:
            histogram[d] = histogram.get(d, 0) + 1
    return len(dist), qualifying, histogram, missing


def first_sample_path(k: int, p: int):
    """Return one shortest path to an admissible endpoint, for pattern mining."""
    x = mat([[int(i == j) for j in range(k)] for i in range(k)] + [[0] * k])
    parent = {x: None}
    queue = deque([x])
    while queue:
        a = queue.popleft()
        for b in neighbors(a, p):
            if b not in parent:
                parent[b] = a
                queue.append(b)

    ident = mat([[int(i == j) for j in range(k)] for i in range(k)])
    for entries in product(range(p), repeat=k * k):
        h = mat([list(entries[i * k : (i + 1) * k]) for i in range(k)])
        h_minus_i = mat([[(h[i][j] - ident[i][j]) % p for j in range(k)] for i in range(k)])
        if rank_mod(h, p) < k or rank_mod(h_minus_i, p) < k:
            continue
        target = mat([list(row) for row in inverse(h, p)] + [[0] * k])
        path = []
        cursor = target
        while cursor is not None:
            path.append(cursor)
            cursor = parent[cursor]
        return h, list(reversed(path))
    raise RuntimeError("no admissible matrix")


if __name__ == "__main__":
    for k, p in [(1, 3), (2, 2), (2, 3), (3, 2)]:
        reached, qualifying, histogram, missing = distances(k, p)
        print(
            f"k={k} p={p} reached={reached} qualifying={qualifying} "
            f"distances={histogram} missing={len(missing)}"
        )
    h, path = first_sample_path(3, 2)
    print(f"sample k=3 p=2 H={h}")
    for index, frame in enumerate(path):
        print(f"X_{index}={frame}")
    for k, p in [(2, 2), (2, 3), (3, 2)]:
        total = validate_constructive_paths(k, p)
        print(f"constructive validation k={k} p={p}: all {total} invertible endpoints passed")
