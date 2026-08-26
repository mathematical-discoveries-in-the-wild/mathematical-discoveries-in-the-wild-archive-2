# Verification record

## Target match

- Source: Simon Foucart, arXiv:2310.18565, Section 6, equation (19), page 14.
- Exact challenge: deterministic modified matrix RIP in the ell_1 measurement
  norm at a subquadratic measurement count, with rank-one measurement matrices
  explicitly highlighted.
- Result scope: complete affirmative construction for rank at most one over R
  and C; no claim for rank greater than one.

The packet includes the original PDF as `source_paper.pdf` and a full-width,
readable render of page 14 as `figures/open_problem_crop.png`.

## Proof audit

1. Indyk's recursive map begins with a dictionary `D` formed by vertically
   concatenating `L` orthonormal matrices, hence `D^*D=L I`.
2. Its extractor graph is left `d`-regular. The map only routes/repeats every
   coordinate of `Dx` exactly `d` times, hence `F^*F=Ld I`. After normalization
   every recursion level is an exact isometry, including when applied blockwise.
3. Indyk's block estimate says that the sum of block ell_2 norms is within a
   `1-O(zeta)` factor of `sqrt(b)||x||_2`. Iterating for `O(log log n)` levels
   with `zeta=O(eta/log log n)` keeps total loss below `eta`.
4. A fixed-dimensional, signed-permutation-symmetrized spherical quadrature is
   an exact tight frame and uniformly approximates the rotational first
   absolute moment. This closes the leaves without affecting the
   `n exp(O_eta((log log n)^2))` dimension bound.
5. For C, realify in dimension `2n`, write the real tight frame as `[P Q]`, and
   set `C=P-iQ`. Orthogonality of the real column blocks gives `C^*C=2I`.
   Averaging `|Re(e^{it}w)|` over phase recovers `(2/pi)|w|`, so complexification
   preserves the relative ell_1 distortion.
6. Noga Alon's all-orders construction supplies, on exactly `M` vertices, a
   deterministic constant-degree graph with normalized nontrivial spectrum as
   small as prescribed. Its bipartite double cover gives the required mixing
   inequality.
7. If rows of the normalized frame are `b_j^*`, assign
   `A_(j,k)=b_j b_k^*` to expander edges. For `X=uv^*`, the measurement
   magnitude factors as `|b_j^*u||b_k^*v|`.
8. Flatness controls the mean term and tightness controls the mixing error,
   yielding raw constants `d(a^2-theta)` and `d(b^2+theta)` times `||X||_F`.
   A scalar rescaling gives a `(1+-delta)` inequality for any fixed delta.
9. The edge count is `m=dM`; since degree depends only on delta,
   `m=n^(1+o(1))=o(n^2)`.

## Mechanical regression check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2310.18565_expander_tensor_rank_one_matrix_rip/code/verify_rank_one_expander.py
```

Observed output on 2026-08-11:

```text
real: n=8, M=256, d=48, theta=0.282923, flat_sample=[0.773398,1.000000], delta_bound=0.710564, pairs=2025, slack=[5.252e-01,5.808e-01]
complex: n=3, M=64, d=32, theta=0.328561, flat_sample=[0.898071,1.000000], delta_bound=0.643394, pairs=2025, slack=[6.408e-01,4.423e-01]
VERIFIED: tight frames, expander mixing, factorization, and rank-one RIP bounds
```

The script checks both fields, exact tightness to numerical precision, graph
regularity and second singular value, the Frobenius factorization identity,
the mixing error, raw bounds, and rescaled RIP inequalities for 2025 vector
pairs per field. The frames in this finite test use every sign vector, and the
graphs are reproducible unions of permutations. These checks are not a proof
of the asymptotic explicit constructions.

## Deep upgrade audit for rank greater than one

Six routes were pushed after the rank-one result:

1. SVD/triangle inequalities: upper bound only, with nuclear-norm loss;
   cancellations kill the lower bound.
2. Full tensor frame: controls general matrices but uses `M^2` measurements.
3. Spectral sampling of `|BXB^*|`: entrywise absolute value can have full rank,
   so the trace-norm mixing error loses `sqrt(M)` and forces quadratic degree.
4. Positive semidefinite restriction: trace gives distortion `sqrt(r)` and
   does not cover the general target.
5. Phase/sign-rank lifting: independent edge phases destroy low-rank
   factorization and require a stronger sampler.
6. Polynomial approximation of absolute value: higher tensor designs incur
   nonrelative error near zero or dependence exponential in degree/rank.

No credible elementary route remained after attempt 6. The precise missing
object is a deterministic sampler for entrywise absolute values of low-rank
bilinear arrays with polynomial dependence on the rank.

## Novelty check

- Cheap indexes searched: all four lightweight indexes under
  `runs/fa_banach_001`.
- Local keys: `2310.18565`, full title, `modified RIP`, `rank-one
  measurements`, `low-rank recovery`, `tensor embedding`, `expander mixing`.
- Adjacent indexed records checked: arXiv:1003.2990, 1202.1234, 1406.4089.
- Bounded external primary-source searches: exact theorem/construction phrases
  on arXiv, the source's citations, Indyk's ECCC paper, and Alon's exact-size
  expander theorem, through 2026-08-11.
- Result: no located paper stated this rank-one expander-sparsified theorem.

This was bounded rather than exhaustive, so novelty confidence is moderate and
independent literature review remains necessary.

## Artifact audit and human recommendation

- `source_paper.pdf` is a 19-page PDF downloaded from arXiv.
- `source_indyk_eccc.pdf` is ECCC Report TR06-126, a 9-page primary-source PDF.
- The open-problem image is a real page render, not retyped text.
- `main.tex` is self-contained except for local figures and cites every
  external theorem used.
- LaTeX is compiled twice with build artifacts confined to `tmp/`.
- Every rendered packet page is visually inspected after compilation.

Recommendation: review Lemma 1's exact tight-frame extraction first. If it is
accepted, the remaining proof is a direct expander-mixing calculation and the
packet should be promoted as a substantial rank-one partial answer.
