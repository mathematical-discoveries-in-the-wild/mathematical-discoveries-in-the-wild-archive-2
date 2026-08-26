# Minimal K-sets in `ell_infinity^n`: a strong partial program

Status: `strong_partial_result_likely_valid`.  This packet settles the exact
K-number, all vertex-supported sets, all finite minimal sets in dimension
two, and a continuum of optimal genuinely nonvertex examples in every
dimension at least three.  It also gives an exact local certificate at every
boundary point.  A closed classification of every nonvertex minimal set in
dimensions at least three remains open.

## Source question

Debmalya Sain, Jayanta Manna, and Kallol Paul, *On local preservation of
orthogonality and its application to isometries*, Linear Algebra and its
Applications 690 (2024), 112-131; arXiv:2407.08900.

On page 17 the authors ask for a characterization of the minimal K-sets in
`ell_infinity^n` and the value of `kappa(ell_infinity^n)`.

## Main results

- **Exact arbitrary-face criterion.**  If `w=Tx!=0`, local preservation at
  `x` is equivalent to

  ```text
  J(x) subset ||w||_infinity^{-1} T^* J(w),
  ```

  or, equivalently, to a nonnegative row-stochastic factorization between
  the two norming simplices.
- **All vertex-supported sets.**  A set of cube vertices is a K-set exactly
  when it spans.  Its minimal members are precisely vertex bases.
- **Exact K-number.**  Every K-set must span and a vertex basis works, so
  `kappa(ell_infinity^n)=n` for every `n>=2`.
- **Continuum of nonvertex minimal sets.**  For `n>=3`, arbitrary
  `t_i in (-1,1)` give a minimal K-set

  ```text
  x^i_j=1 (j!=i),   x^i_i=t_i,   i=1,...,n.
  ```
- **Complete finite two-dimensional classification.**  The finite minimal
  sets in `ell_infinity^2` are exactly an independent vertex pair, or one
  vertex together with one smooth point of each active-coordinate type.
- **Stochastic-parallelotope reduction.**  After normalizing a contained
  vertex, nonzero preservers are inverses of invertible row-stochastic
  matrices `R`, and preservation at a further point `x` is exactly
  `x in R(B_infinity)`.
- **Sharp obstruction.**  In dimension three, `T=J-2I` preserves at
  `{1,e_1,e_2,e_3}` but is not an isometry up to scalar.  Thus the most
  obvious coordinate-test generalization fails.

## Boundary

The exact factorization theorem converts every finite test set into explicit
nonnegative matrix constraints, but the packet does not claim an intrinsic
classification of all nonvertex minimal sets for `n>=3`, nor does it rule out
infinite minimal sets.  The literature search was bounded rather than
exhaustive.

## Files

- `main.tex` and `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: page-17 source evidence.
- `code/verify_cube_vertex_k_sets.py`: deterministic exhaustive and randomized
  matrix checks covering every theorem family in the packet.
- `verification.md`: commands, outputs, analytic review checklist, literature
  boundary, and PDF QA.
