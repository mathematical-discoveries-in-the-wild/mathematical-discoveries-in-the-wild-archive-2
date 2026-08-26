# Literature answer: higher-rank numerical ranges

- **Source:** M.-D. Choi, D. W. Kribs, K. Życzkowski, *Higher-Rank
  Numerical Ranges and Compression Problems*, arXiv:math/0511278.
- **Answer:** C.-K. Li, N.-S. Sze, *Canonical forms, higher rank numerical
  range, convexity, totally isotropic subspace, matrix equations*,
  arXiv:0706.1536; Proc. Amer. Math. Soc. 136 (2008), 3013–3023.
- **Model:** GPT5.6
- **Disposition:** `literature_already_answered` (complete answer to
  Conjecture 2.8 and Problem 2.9).

## Exact match

The source defines

\[
\Lambda_k(A)=\{\mu\in\mathbb C:PAP=\mu P\text{ for some rank-}k
\text{ orthogonal projection }P\}.
\]

Its Conjecture 2.8 says that for a normal `n × n` matrix, this set equals
the intersection of the convex hulls of all `(n-k+1)`-element spectral
submultisets. Problem 2.9 asks whether `Λ_k(A)` is convex whenever it is
nonempty, for arbitrary matrices.

Li–Sze answer both questions exactly:

- Theorem 2.2 represents `Λ_k(A)` for every complex matrix as an
  intersection of closed half-planes.
- Corollary 2.3 therefore proves that `Λ_k(A)` is always convex (the empty
  set is harmless, so this is slightly stronger than the source wording).
- Corollary 2.4 specializes the representation to a normal matrix and gives
  precisely the spectral convex-hull intersection in Conjecture 2.8.

Consequently, the source's first open test case—the cyclic five-shift with
`n=5`, `k=2`—contains every point of the indicated inner pentagon, not only
its boundary and center.

## Files

- `source_paper.pdf`: arXiv:math/0511278.
- `supporting_paper_0706.1536.pdf`: the complete Li–Sze answer.
- `source_0511278.tar.gz` and `source_metadata_0511278.json`: locally
  inspected source materials.
- `main.tex` and `solution_packet.pdf`: compact theorem-to-question status
  note.

## Novelty boundary

This packet records a direct later-literature answer, not a new proof. The
identification is exact at the theorem-label and formula level.
