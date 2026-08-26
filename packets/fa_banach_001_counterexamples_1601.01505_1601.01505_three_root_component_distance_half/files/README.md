# Three-root algebraic components at distance one half

Status: `candidate counterexample (likely valid; human review requested)`

Source/open problem:

- E. Makai, Jr. and J. Zemanek, *Nice connecting paths in connected
  components of sets of algebraic elements in a Banach algebra*,
  arXiv:1601.01505, Czechoslovak Math. J. 66 (2016), 821-828.
- The conjecture on PDF page 5 asks whether distinct connected components of
  `E_p(A)` are always separated by at least the minimum distance between two
  roots of `p`.

Candidate result:

The Banach-algebra part of the conjecture is false already in
`A=M_2(C)` with its usual operator norm and

`p(lambda)=lambda(lambda-1)(lambda-2)`.

Let `C_01` be the component with spectral multiplicities `(1,1,0)` and
`C_02` the component with multiplicities `(1,0,1)`.  The packet proves

`dist(C_01,C_02)=1/2`,

whereas the minimum root separation is `1`.

The construction starts from rank-one idempotents

`e=diag(1,0)` and `f=[[9/8,1],[-9/64,-1/8]]`.

Then `2f-e=(1/2)I+N`, where `N` is a nonzero square-zero matrix.  A
simultaneous similarity shrinks `N` to `tN` without changing either spectral
multiplicity component.  This gives the upper bound `1/2`; the ordinary
matrix trace gives the matching lower bound.

Scope:

- This disproves the `E_p(A)` Banach-algebra assertion, even though the
  ambient algebra is a finite-dimensional C*-algebra.
- The constructed elements are not self-adjoint.  The separate conjecture for
  the self-adjoint set `S_p(A)` remains untouched.
- The construction does not decide whether distinct Banach-algebra components
  always have some positive lower separation depending on the roots.

Verification and novelty:

- `verification_report.md` gives an independent proof audit.
- `code/verify_matrices.py` checks all rational matrix identities exactly and
  samples the operator-norm convergence numerically.  The code is
  supplementary and is not used as proof.
- A bounded 2026-08-09 search covered the run indexes/local arXiv corpus,
  exact web/arXiv phrases, arXiv:1807.01552 (where the authors repeat the same
  problem in 2018), and the two substantive works in the OpenAlex citation
  graph of the source DOI.  No explicit resolution or counterexample was
  found; novelty remains subject to specialist review.

Files:

- `solution_packet.pdf`: complete proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: conjecture on source PDF page 5.

