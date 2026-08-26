# Verification record

Verified at: 2026-08-17T21:06:58Z

Verdict: `candidate_partial_likely_valid` — a dimension-free partial
affirmative answer to the arbitrary-normal extension proposed in Remark 2 of
arXiv:1708.05338.

## Mathematical audit

- A normal matrix with at most `M` distinct eigenvalues is unitarily
  diagonalizable, and Lagrange interpolation on its spectrum gives
  `A*=p(A)` with `degree(p)<=M-1`.
- The telescoping identity
  `[X^l,Y]=sum_{q=0}^{l-1} X^q[X,Y]X^{l-1-q}` and rank subadditivity give
  `rank([p(X),Y])<=m(m+1)/2 rank([X,Y])` for `degree(p)<=m`.
- With `K=max(1,M(M-1)/2)`, every commutator in
  `(A_1,...,A_n,A_1*,...,A_n*)` has normalized rank at most `K^2 delta`.
  This tuple is star-closed, so Theorem 6 of the source applies uniformly in
  matrix dimension.  Its first `n` output coordinates prove the theorem.
- Invertibility is not used.
- For the concentration corollary, replacing exceptional eigenvalues changes
  each matrix in rank at most `kappa d`.  The identity
  `[C_i,C_j]-[A_i,A_j]=[C_i-A_i,C_j]+[A_i,C_j-A_j]` bounds the resulting
  normalized-commutator increase by `4 kappa`.  The choices in the packet
  therefore put the modified tuple inside the bounded-spectrum modulus and
  preserve the final `epsilon` rank tolerance.
- In the obstruction example, the displayed Householder matrix is unitary,
  hence both displayed matrices are normal.  Exact symbolic row reduction
  gives `rank([A,B])=2` and `rank([A*,B])=4`.  The packet correctly presents
  this only as failure of a proof shortcut, not as a stability
  counterexample.

## Upgrade record

Eight focused stages were completed: direct star-closure, later-literature
audit, exact rank-Fuglede stress test, finite-spectrum interpolation,
quantitative polynomial-commutator control, application of the source's
star-closed theorem, spectral-concentration upgrade, and an unrestricted plus
same-type obstruction audit.  The remaining obstruction is the loss of a
dimension-free modulus when the number of spectral values grows with the
matrix dimension.

## Literature audit

- The exact source question is Remark 2 on PDF page 3 of arXiv:1708.05338.
- The introduction of Bauer--Blachar--Greenfeld, arXiv:2401.04676, explicitly
  states that rank-stability of the commuting equations without spectral
  restrictions remains open and cites the source's Remark 2.
- Bounded primary-source searches through 2026-08-17 found no later arXiv
  paper settling the unrestricted question or stating this bounded-spectral-
  complexity partial theorem.  This is a novelty screen, not a definitive
  priority determination.

## Computational and packet checks

- `conda run --no-capture-output -n sandbox python code/verify_rank_bounds.py`
  passed.  It checks exact normality and commutator ranks in the obstruction,
  exact adjoint interpolation on a sample spectrum, the polynomial
  commutator bound, and the rank-perturbation inequality.
- LaTeX compiled without matched warnings, overfull boxes, underfull boxes,
  undefined references, or errors in the final log.
- The final packet has three A4 pages.  Every page was rendered at 180 dpi
  and visually inspected; the source crop, theorem statements, formulas,
  proof, limitations, and references are readable and unclipped.
- Text extraction from the final PDF contains the theorem, concentration
  upgrade, obstruction, and references.

SHA-256:

- `solution_packet.pdf`: `b9eff0c657c7ad8f44a39b5961f7a338269094c159e0cc55854b22562edbe5a3`
- `source_paper.pdf`: `e50820740b5daefe240a86389ada0c91017812330e98a9166dee14897941f2d3`
- `supporting_rank_stability_2024.pdf`: `bb3c1b4351d970d94d5d0d5a143e4d8bac7173c2d8d1c73a06a84d118094c42e`
- `figures/open_problem_crop.png`: `a116fe3e8a3453485b66f1e5c468898e2f0e0948a5ff9384225c2a5b96f06c27`
- `code/verify_rank_bounds.py`: `c9947890b8a5fbf5d771f875bfdf780f376f99f3d2bb78f94aa48bc553a5906f`

## Human review priorities

1. Recheck that Theorem 6 of the source uses exactly the same normalized-rank
   modulus for arbitrary star-closed tuples of fixed length.
2. Audit the double use of the polynomial commutator lemma and the constants
   in the spectral-concentration corollary.
3. Repeat the novelty search beyond arXiv before dissemination.

