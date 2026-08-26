# Partial-solution packet: horizontal Gevrey quasianalyticity

Status: candidate substantial partial result, likely valid, needs human review.

Source target: Véronique Fischer, Michael Ruzhansky, and Chiara Alba Taranto,
*Subelliptic Gevrey spaces*, arXiv:1805.08667, Introduction, Question 3
(PDF page 4).

Result: let a finite smooth Hörmander family `X={X_1,...,X_r}` act on a
connected manifold.  Every function satisfying the paper's horizontal
Gevrey bounds of order `0<s<=1` has open-set uniqueness.  Indeed, repeated
`X_j` derivatives have ordinary factorial growth, so the function is real
analytic along every `X_j` flow; its open zero set is invariant under all
local flows, and the Hörmander orbit theorem propagates it across the whole
manifold.

Consequences:

- `gamma_{X,L-infinity}^s` has no nonzero properly compactly supported
  functions for `0<s<=1`; on a connected noncompact manifold it is trivial
  under the paper's compact-support convention.
- Under the source's horizontal Sobolev embedding, the same holds for compactly
  supported members of `gamma_{X,L2}^s`.
- On every Heisenberg group `H_n`, the source's equivalence theorem transfers
  the result to `gamma_L^s`, so all three source definitions have no nonzero
  compactly supported members for `0<s<=1`.

Scope: this gives a complete affirmative answer to the no-compact-support
subquestion for the two horizontal definitions and for all definitions in the
paper's flagship noncompact Heisenberg setting.  It does not establish the
general spectral/sub-Laplacian version on manifolds where
`gamma_L^s subset gamma_{X,L2}^s` is unknown; that missing upgrade is the
paper's separate higher-order-Riesz/equivalence problem.  On compact manifolds,
literal compact support is vacuous, so the invariant conclusion is open-set
uniqueness.

Files:

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1805.08667.
- `figures/open_problem_crop.png`: full-width source crop containing Question 3.

Novelty check: bounded run-index and arXiv searches on 2026-08-17 used the
exact title/id, authors, question wording, compact-support, quasi-analytic,
Hörmander-flow, and higher-Riesz keywords.  No later explicit answer was
located.  Novelty confidence is moderate because the proof is elementary.

Review recommendation: check the source's word-factorial convention for a
repeated index, the analytic-continuation step on maximal local-flow
intervals, the orbit-saturation argument, and the exact transfer from the
source's Proposition 2.6 and Theorem 4.1.  Human review remains pending.
