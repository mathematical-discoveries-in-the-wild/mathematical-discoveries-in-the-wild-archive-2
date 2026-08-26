# Full-solution packet: uniqueness without monotonicity by spectral dynamics

Status: candidate full answer, likely valid, needs human review.

Source target: Faruk Alpay, Hamdi Alakkad, and Taylan Alpay,
*Transfinite Operator Fixed Points on Hilbert Spaces: An Alpay Algebra
Approach*, arXiv:2508.04890, Appendix A, Problem 1 (PDF page 11).

Result: monotonicity is not essential for a unique iterated limit.  On the
self-adjoint unit ball of any nonzero Hilbert space, the spectral transform
`Phi(A) = A^2` is neither Loewner-order nor spectral-order preserving, but
every orbit converges strongly to the uniquely determined fixed projection
`E_A({-1,1})`.  The damped transform `Psi(A) = A^2/2` goes further: it violates
the source's explicit requirement that projections remain fixed, but every
orbit converges in norm to `0`, the unique global fixed point.

General theorem: for a continuous self-map `f` of a compact real spectral set,
pointwise convergence of the scalar iterates `f^n` implies strong convergence
of `f^n(A)` for every self-adjoint `A`, by the spectral theorem and dominated
convergence.  A common scalar attractor is necessary and sufficient for a
common strong limit over all scalar and operator inputs, and it gives a unique
global fixed point.  Uniform scalar convergence upgrades the conclusion to
operator-norm convergence.

Scope: the source does not define its phrase “order of spectral projections.”
The packet therefore verifies the requested failure under the standard
spectral order (and Loewner order) and separately gives a transformation that
fails the source's formally stated projection-stability axiom.  This is a
full answer in the natural fixed-H spectral-transform setting, a special case
of the paper's non-expanding framework.  It is not a validation of the
paper's broader transfinite theorem.

Files:

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2508.04890.
- `figures/open_problem_crop.png`: full-width crop of Appendix A, Problem 1.
- `code/check_examples.py`: finite-dimensional and scalar sanity checks.

Novelty check: the run indexes and bounded arXiv searches on 2026-08-17 used
the exact title, arXiv id, problem label, quoted order phrase, and close
spectral-dynamics keywords.  No later explicit answer or correction was
located.  Since the proof uses elementary spectral calculus, novelty
confidence is moderate even though no duplicate was found.

Review recommendation: verify that the intended meaning of “unique
`Phi^infinity(A)`” is uniqueness of the orbit limit for each `A`; check the
source's undefined order terminology; and check the fixed-point uniqueness
argument for the common-attractor criterion.  Human review remains pending.
